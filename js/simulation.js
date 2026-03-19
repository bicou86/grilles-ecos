// simulation.js — Logic for the ECOS simulation flow

(function() {
  'use strict';

  var PATIENT_ECOS_URL = 'https://chatgpt.com/g/g-699864f041888191b3f512be2e0e1834';

  /**
   * Read URL parameters
   */
  function getParams() {
    var params = new URLSearchParams(window.location.search);
    return {
      caseId: params.get('case') || '',
      corpus: params.get('corpus') || ''
    };
  }

  /**
   * Build the case file URL from corpus and caseId (filename without extension)
   */
  function getCaseFileUrl(corpus, caseId) {
    return '../cases/' + corpus + '/' + caseId + '.html';
  }

  /**
   * Extract the case title from fetched HTML content
   */
  function extractTitle(html) {
    var match = html.match(/<h1[^>]*>(.*?)<\/h1>/i);
    if (match) return match[1].replace(/<[^>]*>/g, '').trim();
    var titleMatch = html.match(/<title>(.*?)<\/title>/i);
    if (titleMatch) return titleMatch[1].replace(/ - Grille ECOS$/i, '').trim();
    return '';
  }

  /**
   * Save simulation start timestamp
   */
  function saveSimStart(caseId) {
    try {
      localStorage.setItem('ecos_sim_start_' + caseId, new Date().toISOString());
    } catch(e) {}
  }

  /**
   * Copy text to clipboard (returns a promise)
   */
  function copyToClipboard(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    // Fallback
    return new Promise(function(resolve, reject) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.left = '-9999px';
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand('copy');
        resolve();
      } catch(e) {
        reject(e);
      } finally {
        document.body.removeChild(ta);
      }
    });
  }

  /**
   * Format a human-readable case name from the filename
   * e.g. "AMBOSS-1_-_Douleurs_abdominales_-_Femme_47_ans_-_Grille_ECOS" -> "AMBOSS-1 - Douleurs abdominales - Femme 47 ans"
   */
  function formatCaseName(caseId) {
    return caseId
      .replace(/_-_/g, ' - ')
      .replace(/_/g, ' ')
      .replace(/ - Grille ECOS$/i, '')
      .trim();
  }

  // Expose utilities
  window.EcosSimulation = {
    PATIENT_ECOS_URL: PATIENT_ECOS_URL,
    getParams: getParams,
    getCaseFileUrl: getCaseFileUrl,
    extractTitle: extractTitle,
    saveSimStart: saveSimStart,
    copyToClipboard: copyToClipboard,
    formatCaseName: formatCaseName
  };
})();
