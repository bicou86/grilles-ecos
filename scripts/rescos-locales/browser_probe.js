/*
 * Harnais de controle en navigateur pour le corpus `cases/rescos-locales`.
 *
 * POURQUOI IL EXISTE, ET POURQUOI IL EST VERSIONNE
 * ------------------------------------------------
 * Les 156 grilles notees de ce corpus embarquent CHACUNE leur propre copie du
 * moteur de calcul (aucune ne charge `cases/scoring.js`). Aucune analyse
 * statique ne peut prouver qu'un moteur ne leve pas d'exception a l'execution :
 * c'est precisement ce qui avait laisse passer RESCOS-7 et RESCOS-9, dont les
 * copies levaient 16 et 51 exceptions par remplissage sans qu'aucune porte
 * Python ne bronche. Trois campagnes ont donc ecrit trois fois le meme harnais
 * dans un scratchpad de session (voir r6, r7, et la preoccupation n°4 de
 * `r7-report.md`). Celui-ci est versionne pour clore ce cycle.
 *
 * CE QU'IL MESURE, PAR GRILLE
 *   - exceptions JavaScript et erreurs de console au CHARGEMENT ;
 *   - idem apres REMPLISSAGE COMPLET (toutes les cases de detail cochees,
 *     chaque radio a sa valeur maximale, communication au niveau A) ;
 *   - le pourcentage global et la note affichee apres remplissage ;
 *   - la presence d'une entree dans `localStorage.ecos_registry` — le canal par
 *     lequel le tableau de bord recupere le score. Ecrit a un seul endroit du
 *     projet, `cases/scoring.js:saveToRegistry()`.
 *
 * STRICTEMENT LOCAL. Serveur statique sur 127.0.0.1, Chrome for Testing lance
 * avec `--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE 127.0.0.1` : aucune
 * requete ne peut sortir de la boucle locale. Aucun paquet n'est installe — le
 * pilotage passe par le protocole DevTools sur le WebSocket natif de Node 22.
 *
 * Usage :
 *   node scripts/rescos-locales/browser_probe.js [FILTRE] > rapport.json
 *   node scripts/rescos-locales/browser_probe.js --summary   # resume lisible
 */
'use strict';
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const DIR = path.join(ROOT, 'cases', 'rescos-locales');
const CHROME = findChrome();

function findChrome() {
    const base = path.join(process.env.HOME, '.cache', 'puppeteer', 'chrome-headless-shell');
    if (!fs.existsSync(base)) throw new Error('chrome-headless-shell introuvable dans ' + base);
    const versions = fs.readdirSync(base).sort().reverse();
    for (const v of versions) {
        const p = path.join(base, v, 'chrome-headless-shell-mac-arm64', 'chrome-headless-shell');
        if (fs.existsSync(p)) return p;
    }
    throw new Error('binaire chrome-headless-shell introuvable');
}

const MIME = {'.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css',
              '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.svg': 'image/svg+xml'};

function serve() {
    return new Promise(resolve => {
        const srv = http.createServer((req, res) => {
            const rel = decodeURIComponent(req.url.split('?')[0]).replace(/^\/+/, '');
            const file = path.join(ROOT, rel);
            if (!file.startsWith(ROOT) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
                res.writeHead(404); res.end('404'); return;
            }
            res.writeHead(200, {'Content-Type': MIME[path.extname(file).toLowerCase()] || 'application/octet-stream'});
            fs.createReadStream(file).pipe(res);
        });
        srv.listen(0, '127.0.0.1', () => resolve(srv));
    });
}

async function launchChrome() {
    const {spawn} = require('child_process');
    const userDir = fs.mkdtempSync(path.join(require('os').tmpdir(), 'ecos-probe-'));
    const proc = spawn(CHROME, [
        '--remote-debugging-port=0',
        '--user-data-dir=' + userDir,
        '--no-first-run', '--no-default-browser-check', '--disable-gpu',
        '--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE 127.0.0.1',
        'about:blank',
    ], {stdio: ['ignore', 'ignore', 'pipe']});
    const wsUrl = await new Promise((resolve, reject) => {
        let buf = '';
        const t = setTimeout(() => reject(new Error('Chrome n\'a pas annonce son WebSocket')), 30000);
        proc.stderr.on('data', d => {
            buf += d.toString();
            const m = buf.match(/ws:\/\/127\.0\.0\.1:\d+\/devtools\/browser\/[-\w]+/);
            if (m) { clearTimeout(t); resolve(m[0]); }
        });
    });
    return {proc, wsUrl, userDir};
}

class CDP {
    constructor(ws) { this.ws = ws; this.id = 0; this.pending = new Map(); this.handlers = [];
        ws.addEventListener('message', ev => {
            const msg = JSON.parse(ev.data);
            if (msg.id !== undefined && this.pending.has(msg.id)) {
                const {resolve, reject} = this.pending.get(msg.id); this.pending.delete(msg.id);
                msg.error ? reject(new Error(JSON.stringify(msg.error))) : resolve(msg.result);
            } else if (msg.method) { this.handlers.forEach(h => h(msg)); }
        });
    }
    send(method, params, sessionId) {
        const id = ++this.id;
        this.ws.send(JSON.stringify({id, method, params: params || {}, sessionId}));
        return new Promise((resolve, reject) => this.pending.set(id, {resolve, reject}));
    }
    on(fn) { this.handlers.push(fn); }
}

function open(url) {
    return new Promise((resolve, reject) => {
        const ws = new WebSocket(url);
        ws.addEventListener('open', () => resolve(ws));
        ws.addEventListener('error', reject);
    });
}

// Remplissage pilote par le DOM : `checked = true` puis evenement `change`.
// Les gestionnaires `onchange` en ligne des grilles font le reste. C'est la
// meme voie que r7 : cliquer par coordonnees serait fragile a la mise en page.
const FILL = `(function(){
  var n=0;
  document.querySelectorAll('input[type="checkbox"]').forEach(function(cb){
    cb.checked = true; cb.dispatchEvent(new Event('change', {bubbles:true})); n++;
  });
  var byName = {};
  document.querySelectorAll('input[type="radio"]').forEach(function(r){
    (byName[r.name] = byName[r.name] || []).push(r);
  });
  Object.keys(byName).forEach(function(name){
    var group = byName[name];
    var best = null, bestVal = -1;
    group.forEach(function(r){
      var v = /^[A-E]$/.test(r.value) ? ({A:4,B:3,C:2,D:1,E:0})[r.value] : Number(r.value);
      if (!isNaN(v) && v > bestVal) { bestVal = v; best = r; }
    });
    if (best) { best.checked = true; best.dispatchEvent(new Event('change', {bubbles:true})); n++; }
  });
  return n;
})()`;

const READ = `(function(){
  var reg = null;
  try { reg = JSON.parse(localStorage.getItem('ecos_registry') || 'null'); } catch(e) {}
  var t = document.getElementById('totalScore');
  var g = document.getElementById('globalGrade');
  return JSON.stringify({
    total: t ? t.textContent.trim() : null,
    grade: g ? g.textContent.trim() : null,
    registryKeys: reg ? Object.keys(reg) : null,
    registry: reg
  });
})()`;

async function probeOne(cdp, base, name) {
    const {targetId} = await cdp.send('Target.createTarget', {url: 'about:blank'});
    const {sessionId} = await cdp.send('Target.attachToTarget', {targetId, flatten: true});
    const errsLoad = [], errsFill = [];
    let phase = errsLoad;
    const handler = msg => {
        if (msg.sessionId !== sessionId) return;
        if (msg.method === 'Runtime.exceptionThrown') {
            const d = msg.params.exceptionDetails;
            const frames = (d.stackTrace && d.stackTrace.callFrames || [])
                .slice(0, 3).map(f => (f.functionName || '<top>') + ':' + (f.lineNumber + 1)).join(' < ');
            phase.push('EXCEPTION ' + (d.exception && d.exception.description || d.text).split('\n')[0]
                       + (frames ? '  @ ' + frames : ''));
        } else if (msg.method === 'Runtime.consoleAPICalled' && msg.params.type === 'error') {
            phase.push('CONSOLE ' + msg.params.args.map(a => a.value || a.description).join(' ').split('\n')[0]);
        } else if (msg.method === 'Log.entryAdded' && msg.params.entry.level === 'error') {
            phase.push('LOG ' + msg.params.entry.text.split('\n')[0]);
        }
    };
    cdp.on(handler);
    await cdp.send('Runtime.enable', {}, sessionId);
    await cdp.send('Log.enable', {}, sessionId);
    await cdp.send('Page.enable', {}, sessionId);
    const url = base + '/cases/rescos-locales/' + encodeURIComponent(name);
    await cdp.send('Page.navigate', {url}, sessionId);
    await new Promise(r => setTimeout(r, 1200));
    phase = errsFill;
    let filled = 0;
    try {
        const r = await cdp.send('Runtime.evaluate', {expression: FILL, returnByValue: true}, sessionId);
        filled = r.result.value;
    } catch (e) { errsFill.push('FILL-FAILED ' + e.message); }
    await new Promise(r => setTimeout(r, 400));
    let read = {};
    try {
        const r = await cdp.send('Runtime.evaluate', {expression: READ, returnByValue: true}, sessionId);
        read = JSON.parse(r.result.value);
    } catch (e) { read = {error: e.message}; }
    cdp.handlers.splice(cdp.handlers.indexOf(handler), 1);
    await cdp.send('Target.closeTarget', {targetId});
    return {name, filled, errsLoad, errsFill, ...read};
}

async function main() {
    const args = process.argv.slice(2);
    const summary = args.includes('--summary');
    const filter = args.filter(a => !a.startsWith('--'))[0];
    const srv = await serve();
    const base = 'http://127.0.0.1:' + srv.address().port;
    const {proc, wsUrl, userDir} = await launchChrome();
    const cdp = new CDP(await open(wsUrl));
    const names = fs.readdirSync(DIR).filter(n => n.endsWith('.html'))
                    .filter(n => !filter || n.includes(filter)).sort();
    const out = [];
    for (const n of names) { out.push(await probeOne(cdp, base, n)); }
    proc.kill(); srv.close();
    try { fs.rmSync(userDir, {recursive: true, force: true}); } catch (e) {}
    if (summary) {
        const nErr = out.filter(o => o.errsLoad.length || o.errsFill.length);
        const nReg = out.filter(o => o.registryKeys && o.registryKeys.length);
        const n100 = out.filter(o => o.total === '100%');
        console.log('grilles sondees            : ' + out.length);
        console.log('sans exception ni erreur   : ' + (out.length - nErr.length) + '/' + out.length);
        console.log('a 100 % apres remplissage  : ' + n100.length + '/' + out.length);
        console.log('ecrivant ecos_registry     : ' + nReg.length + '/' + out.length);
        console.log('\n--- grilles n\'atteignant pas 100 % ---');
        out.filter(o => o.total !== '100%').forEach(o =>
            console.log('  ' + (o.total || 'null').padStart(6) + '  ' + (o.grade || '-').padStart(3) + '  ' + o.name));
        console.log('\n--- grilles a exception / erreur ---');
        nErr.forEach(o => console.log('  ' + o.name + '\n      load: ' + JSON.stringify(o.errsLoad.slice(0, 3))
                                      + '\n      fill: ' + JSON.stringify(o.errsFill.slice(0, 3))));
    } else {
        console.log(JSON.stringify(out, null, 1));
    }
    process.exit(0);
}
main().catch(e => { console.error(e); process.exit(1); });
