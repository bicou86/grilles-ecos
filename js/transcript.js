// transcript.js — Transcript submission and prompt builder for Examinateur ECOS

(function() {
  'use strict';

  var EXAMINATEUR_URL = 'https://claude.ai/project/019ca098-3dc7-70ce-b1f0-39244d852d52';

  /**
   * Build the evaluation prompt for Examinateur ECOS
   * @param {string} caseTitle - The case title
   * @param {string} corpus - The corpus name
   * @param {string} caseHtmlContent - The full HTML content of the grille
   * @param {string} transcription - The student's conversation transcript
   * @returns {string} The formatted prompt
   */
  function buildExaminateurPrompt(caseTitle, corpus, caseHtmlContent, transcription) {
    var date = new Date().toISOString().split('T')[0];
    return '/évaluer\n\n' +
      '**Station :** ' + caseTitle + '\n' +
      '**Corpus :** ' + corpus + '\n' +
      '**Date :** ' + date + '\n\n' +
      '**Grille d\'évaluation de référence (HTML) :**\n' +
      caseHtmlContent + '\n\n' +
      '**Transcription de la simulation :**\n' +
      transcription;
  }

  /**
   * Save transcript to localStorage
   */
  function saveTranscript(caseId, text) {
    var timestamp = Date.now();
    var key = 'ecos_transcript_' + caseId + '_' + timestamp;
    try {
      localStorage.setItem(key, JSON.stringify({
        caseId: caseId,
        text: text,
        date: new Date().toISOString()
      }));
    } catch(e) {}
    return key;
  }

  /**
   * Fetch grille HTML content, cleaned for the Examinateur prompt.
   * Keeps structural HTML (divs, spans, h1-h6, tables) readable.
   * Strips scripts, styles, buttons, comment textareas, event handlers.
   */
  function fetchGrilleContent(url) {
    return fetch(url)
      .then(function(response) {
        if (!response.ok) throw new Error('Failed to fetch grille');
        return response.text();
      })
      .then(function(html) {
        var cleaned = html
          // Remove non-content blocks
          .replace(/<script[\s\S]*?<\/script>/gi, '')
          .replace(/<style[\s\S]*?<\/style>/gi, '')
          .replace(/<link[^>]*>/gi, '')
          .replace(/<meta[^>]*>/gi, '')
          .replace(/<\/?(!DOCTYPE|html|head|body)[^>]*>/gi, '')
          // Remove embedded images
          .replace(/src="data:image\/[^"]*"/gi, 'src="[image]"')
          // Replace interactive elements with text symbols
          .replace(/<input[^>]*type=["']radio["'][^>]*>/gi, '( )')
          .replace(/<input[^>]*type=["']checkbox["'][^>]*>/gi, '[ ]')
          .replace(/<input[^>]*>/gi, '')
          .replace(/<textarea[^>]*>[\s\S]*?<\/textarea>/gi, '')
          .replace(/<select[\s\S]*?<\/select>/gi, '[selection]')
          .replace(/<button[\s\S]*?<\/button>/gi, '')
          // Remove event handler attributes only (keep class/id for structure)
          .replace(/\s*on(?:click|change|input|load|submit)="[^"]*"/gi, '')
          .replace(/\s*data-[a-z-]+="[^"]*"/gi, '')
          // Remove style attributes (but keep class for readability context)
          .replace(/\s*style="[^"]*"/gi, '')
          // Clean up whitespace
          .replace(/\n{3,}/g, '\n\n')
          .replace(/^\s+$/gm, '');
        return cleaned.trim();
      });
  }

  // Expose
  window.EcosTranscript = {
    EXAMINATEUR_URL: EXAMINATEUR_URL,
    buildExaminateurPrompt: buildExaminateurPrompt,
    saveTranscript: saveTranscript,
    fetchGrilleContent: fetchGrilleContent
  };
})();
