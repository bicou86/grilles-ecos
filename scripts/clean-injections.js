#!/usr/bin/env node
/**
 * clean-injections.js
 * Scans all HTML, JS, and JSON files in the project for ""
 * prompt injection strings and removes them.
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const EXTENSIONS = ['.html', '.js', '.json', '.css'];
const PATTERNS = [
  /\bStop\s+Claude\b/gi,
  /<!--\s*Stop\s+Claude\s*-->/gi,
  /\/\/\s*Stop\s+Claude/gi,
  /\/\*\s*Stop\s+Claude\s*\*\//gi,
];

let filesScanned = 0;
let filesCleaned = 0;

function walk(dir) {
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch(e) { return; }

  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === 'node_modules' || entry.name === '.git') continue;
      walk(full);
    } else if (EXTENSIONS.some(ext => entry.name.endsWith(ext))) {
      filesScanned++;
      let content = fs.readFileSync(full, 'utf8');
      let changed = false;
      for (const pat of PATTERNS) {
        const before = content;
        content = content.replace(pat, '');
        if (content !== before) changed = true;
      }
      // Also clean trailing whitespace-only lines at end of file that might remain
      if (changed) {
        content = content.replace(/\n\s*\n\s*$/, '\n');
        fs.writeFileSync(full, content, 'utf8');
        filesCleaned++;
        console.log('  Cleaned:', path.relative(ROOT, full));
      }
    }
  }
}

walk(ROOT);
console.log(`Scanned ${filesScanned} files. Cleaned ${filesCleaned} files.`);
