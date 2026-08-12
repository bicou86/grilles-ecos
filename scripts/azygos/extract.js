/**
 * Extracteur du mode apprentissage azygos.ch.
 *
 * À exécuter via Chrome DevTools MCP (evaluate_script) sur la page
 * https://azygos.ch/fr/app/learning-mode/<uuid>, session authentifiée, en
 * enregistrant la sortie dans .azygos-extraction/<uuid>.json.
 *
 * Trois particularités de l'interface dictent la forme de ce script :
 *
 * 1. Un dialogue de présentation du poste s'ouvre au chargement et intercepte
 *    les clics. Non refermé, il rend certains onglets inatteignables — et
 *    l'échec est SILENCIEUX : on obtient simplement moins de données.
 *
 * 2. Les onglets sont à DEUX niveaux. « Infos du cas », « Préparation » et
 *    « Tableau de bord » forment le niveau haut ; les onglets cliniques ne
 *    vivent que sous « Tableau de bord ». Leurs libellés varient selon le
 *    format du poste (« Status clinique », « État clinique », « Partie 1 / … »),
 *    d'où leur découverte plutôt que leur présupposition.
 *
 * 3. Deux contenus ne sont rendus qu'à la demande, et doivent donc être
 *    déclenchés un par un :
 *      - les « Informations complémentaires » (justification clinique de
 *        chaque item), dont le bouton est un FRÈRE du bloc de texte ;
 *      - les images pleine résolution, dont l'URL signée expire en une heure
 *        (/object/sign/… ; la vignette /render/image/sign/… est réduite).
 */
async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const nom = b => (b.getAttribute('aria-label') || b.innerText || '').trim();
  const FIXES = ['Infos du cas', 'Préparation', 'Tableau de bord'];
  const echap = async () => { document.body.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true })); await sleep(60); };

  // Un dialogue de présentation du poste s'ouvre au chargement et intercepte
  // les clics : on le referme avant toute chose.
  const fermeIntro = async () => {
    for (const t of ['Ne plus afficher cette information', 'Continuer', 'Fermer']) {
      const b = [...document.querySelectorAll('button')].find(x => nom(x) === t);
      if (b) { b.click(); await sleep(350); }
    }
    await echap();
  };

  const clic = async t => {
    const b = [...document.querySelectorAll('[data-slot="tabs-tab"], button')].find(x => nom(x) === t);
    if (!b) return false;
    b.click(); await sleep(650);
    for (const c of document.querySelectorAll('[data-slot="collapsible-trigger"][aria-expanded="false"]')) { c.click(); await sleep(35); }
    await sleep(300); return true;
  };
  const clinique = async t => { await clic('Tableau de bord'); return clic(t); };

  const lireOnglet = (onglet) => {
    const panels = [...document.querySelectorAll('[data-slot="tabs-panel"]')];
    const panel = panels[panels.length - 1];
    if (!panel) return null;
    return [...panel.querySelectorAll('[data-slot="card"]')].map((card, gi) => {
      const titre = ((card.querySelector('[data-slot="card-title"]') || {}).innerText || '').trim();
      const contenu = card.querySelector('[data-slot="card-content"]') || card;
      const vus = new Set(); const items = [];
      contenu.querySelectorAll('span.font-medium').forEach(sp => {
        let cont = sp;
        for (let i = 0; i < 6 && cont.parentElement; i++) {
          cont = cont.parentElement;
          if (cont.querySelector('p') || cont.querySelector('img[src*="case-media"]')) break;
        }
        if (vus.has(cont)) return; vus.add(cont);
        const lab = cont.querySelector('span.font-medium');
        if (!lab) return;
        const ii = items.length;
        // Clé stable par position : les intitulés se répètent (Antécédents…).
        const cle = onglet + '#' + gi + '#' + ii;
        // Le déclencheur d'info est un frère du bloc de texte, pas un enfant :
        // on remonte tant qu'on ne happe pas l'item voisin (même nombre de
        // libellés que le conteneur de départ).
        const SEL = '[data-slot="popover-trigger"][aria-label="Information complémentaire"]';
        const nLab = cont.querySelectorAll('span.font-medium').length;
        let hote = cont;
        for (let k = 0; k < 3 && hote.parentElement; k++) {
          if (hote.querySelector(SEL)) break;
          const par = hote.parentElement;
          if (par.querySelectorAll('span.font-medium').length !== nLab) break;
          hote = par;
        }
        const trig = hote.querySelector(SEL);
        if (trig) trig.setAttribute('data-az-cle', cle);
        items.push({
          label: lab.innerText.trim(),
          valeurs: [...cont.querySelectorAll('p')].map(p => p.innerText.trim()).filter(Boolean),
          nbEnfants: cont.querySelectorAll('span.font-medium').length - 1,
          cle, aInfo: !!trig
        });
      });
      return { groupe: titre, items };
    });
  };

  // Ouvre chaque « Information complémentaire » de l'onglet courant.
  // Deux passes : 90 ms suffisent presque toujours, mais quelques popovers
  // tardent. La seconde passe ne reprend que les muets, avec plus de marge.
  const lireInfos = async (cible) => {
    for (const attente of [90, 300]) {
      for (const trig of [...document.querySelectorAll('[data-slot="popover-trigger"][data-az-cle]')]) {
        const cle = trig.getAttribute('data-az-cle');
        if (cible[cle]) continue;
        trig.click();
        await sleep(attente);
        const pop = document.querySelector('[data-slot="popover-content"]');
        const txt = pop ? pop.innerText.trim() : '';
        if (txt) cible[cle] = txt;
        await echap();
      }
    }
  };

  await fermeIntro();
  const data = { meta: { url: location.href, id: location.pathname.split('/').pop(), titre: (document.querySelector('h1') || {}).innerText || '' }, onglets: {}, images: [], infos: {}, ordre: [] };

  for (const t of ['Infos du cas', 'Préparation']) {
    if (await clic(t)) data.onglets[t] = document.querySelector('main').innerText.split('\n').map(s => s.trim()).filter(Boolean);
  }
  await clic('Tableau de bord');
  const cliniques = [...document.querySelectorAll('[data-slot="tabs-tab"]')].map(nom).filter(t => t && !FIXES.includes(t));
  data.ordre = cliniques;
  for (const t of cliniques) {
    if (!(await clinique(t))) continue;
    data.onglets[t] = lireOnglet(t);
    await lireInfos(data.infos);
  }

  for (const t of cliniques) {
    if (!(await clinique(t))) continue;
    for (const b of [...document.querySelectorAll('button')].filter(x => /^Ouvrir l'aperçu/.test(nom(x)))) {
      const label = nom(b).replace(/^Ouvrir l'aperçu\s*:\s*/, '');
      if (data.images.some(i => i.label === label)) continue;
      b.click(); await sleep(1100);
      const plein = [...document.querySelectorAll('img')].find(i => /\/object\/sign\/case-media/.test(i.src));
      if (plein) data.images.push({ onglet: t, label, url: plein.src, dim: plein.naturalWidth + 'x' + plein.naturalHeight });
      await echap();
      const f = [...document.querySelectorAll('button')].find(x => /Fermer|Close/.test(nom(x)));
      if (f) f.click();
      await sleep(350);
    }
  }
  data.nbInfos = Object.keys(data.infos).length;
  return data;
}
