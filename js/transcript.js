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
   * Fetch grille HTML content (strips scripts and style for the prompt)
   */
  function fetchGrilleContent(url) {
    return fetch(url)
      .then(function(response) {
        if (!response.ok) throw new Error('Failed to fetch grille');
        return response.text();
      })
      .then(function(html) {
        // Remove script tags, style tags, and base64 images to reduce size
        var cleaned = html
          .replace(/<script[\s\S]*?<\/script>/gi, '')
          .replace(/<style[\s\S]*?<\/style>/gi, '')
          .replace(/src="data:image\/[^"]*"/gi, 'src="[image]"');
        return cleaned;
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
