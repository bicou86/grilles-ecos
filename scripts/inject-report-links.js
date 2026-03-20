#!/usr/bin/env node
/**
 * inject-report-links.js
 * Adds a small inline script after the simulation-bar in every case HTML file.
 * The script checks localStorage for existing reports and shows a link if found.
 * Idempotent: skips files that already contain report-link-bar.
 */
const fs = require('fs');
const path = require('path');

const CASES_DIR = path.join(__dirname, '..', 'cases');
const CORPORA = ['amboss', 'german', 'rescos', 'usmle', 'triage'];

let injected = 0;
let skipped = 0;

const REPORT_LINK_SNIPPET = `
    <div class="report-link-bar" id="reportLinkBar" style="display:none"></div>
    <script>
    (function(){
      var bar = document.querySelector('.simulation-bar');
      if (!bar) return;
      var caseId = bar.getAttribute('data-case-id');
      var corpus = bar.getAttribute('data-corpus');
      if (!caseId) return;
      function updateReportLink() {
        var best = null;
        for (var i = 0; i < localStorage.length; i++) {
          var k = localStorage.key(i);
          if (k && k.indexOf('ecos_report_' + caseId + '_') === 0) {
            try {
              var d = JSON.parse(localStorage.getItem(k));
              var s = d.score != null ? d.score : null;
              if (s === null && d.markdown) {
                var m = d.markdown.match(/Score\\s*global\\s*[:=]\\s*(\\d+)/i) || d.markdown.match(/(\\d+)\\s*\\/\\s*100/);
                if (m) s = parseInt(m[1], 10);
              }
              if (!best || (d.date && (!best.date || d.date > best.date))) {
                best = { key: k, score: s, date: d.date, corpus: d.corpus || corpus };
              }
            } catch(e) {}
          }
        }
        var rlb = document.getElementById('reportLinkBar');
        if (best) {
          var scoreText = best.score != null ? ' (Score: ' + best.score + '/100)' : '';
          rlb.innerHTML = '<a href="../../report/viewer.html?case=' + encodeURIComponent(caseId) + '&corpus=' + encodeURIComponent(best.corpus) + '&key=' + encodeURIComponent(best.key) + '">\\u{1F4CA} Voir mon dernier rapport' + scoreText + '</a>';
          rlb.style.display = '';
        } else {
          rlb.style.display = 'none';
        }
      }
      updateReportLink();
      window.addEventListener('storage', updateReportLink);
      window.addEventListener('focus', updateReportLink);
    })();
    </script>`;

CORPORA.forEach(function(corpus) {
  const dir = path.join(CASES_DIR, corpus);
  if (!fs.existsSync(dir)) return;

  fs.readdirSync(dir).filter(f => f.endsWith('.html')).forEach(function(file) {
    const filePath = path.join(dir, file);
    let html = fs.readFileSync(filePath, 'utf8');

    // Skip if already injected
    if (html.includes('report-link-bar')) {
      skipped++;
      return;
    }

    // Must have simulation-bar to inject after
    if (!html.includes('simulation-bar')) {
      return;
    }

    // Inject after the closing </div> of the simulation-bar
    // The simulation-bar block ends with </div>
    const simBarEnd = html.indexOf('</div>', html.indexOf('simulation-bar'));
    if (simBarEnd === -1) return;

    const insertPos = simBarEnd + '</div>'.length;
    const newHtml = html.slice(0, insertPos) + REPORT_LINK_SNIPPET + html.slice(insertPos);

    fs.writeFileSync(filePath, newHtml, 'utf8');
    injected++;
  });
});

console.log(`Done: ${injected} files injected, ${skipped} already had report links.`);
