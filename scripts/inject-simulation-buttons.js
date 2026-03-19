#!/usr/bin/env node
/**
 * inject-simulation-buttons.js
 * Injects a "Simuler cette station" bar after the <h1> in every case HTML file.
 * Idempotent: skips files that already contain the simulation-bar.
 */
const fs = require('fs');
const path = require('path');

const CASES_DIR = path.join(__dirname, '..', 'cases');
const CORPORA = ['amboss', 'german', 'rescos', 'usmle', 'triage'];

let injected = 0;
let skipped = 0;
let errors = 0;

CORPORA.forEach(function(corpus) {
  const dir = path.join(CASES_DIR, corpus);
  if (!fs.existsSync(dir)) return;

  fs.readdirSync(dir).filter(f => f.endsWith('.html')).forEach(function(file) {
    const filePath = path.join(dir, file);
    let html = fs.readFileSync(filePath, 'utf8');

    // Skip if already injected
    if (html.includes('simulation-bar')) {
      skipped++;
      return;
    }

    // Derive case ID from filename (without extension)
    const caseId = path.basename(file, '.html');

    // Extract h1 content for the title
    const h1Match = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i);
    if (!h1Match) {
      console.error('  [SKIP] No <h1> found in', file);
      errors++;
      return;
    }
    const caseTitle = h1Match[1].replace(/<[^>]+>/g, '').trim();

    // Build the simulation bar HTML
    const simBar = `
    <div class="simulation-bar" data-case-id="${caseId}" data-case-title="${caseTitle.replace(/"/g, '&quot;')}" data-corpus="${corpus}">
      <a href="../../simulation/launcher.html?case=${encodeURIComponent(caseId)}&corpus=${corpus}" class="btn-simulate">
        &#x1FA7A; Simuler cette station avec Patient ECOS
      </a>
    </div>`;

    // Inject after closing </h1>
    const newHtml = html.replace(/<\/h1>/i, '</h1>' + simBar);

    fs.writeFileSync(filePath, newHtml, 'utf8');
    injected++;
  });
});

console.log(`Done: ${injected} files injected, ${skipped} already had buttons, ${errors} errors.`);
