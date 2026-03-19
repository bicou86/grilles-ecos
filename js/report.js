// report.js — Report viewer logic

(function() {
  'use strict';

  /**
   * Save a report to localStorage
   */
  function saveReport(caseId, corpus, reportMarkdown) {
    var timestamp = Date.now();
    var key = 'ecos_report_' + caseId + '_' + timestamp;
    var score = extractScore(reportMarkdown);
    try {
      localStorage.setItem(key, JSON.stringify({
        caseId: caseId,
        corpus: corpus,
        markdown: reportMarkdown,
        score: score,
        date: new Date().toISOString()
      }));
    } catch(e) {}
    return key;
  }

  /**
   * Extract score from report markdown
   * Looks for patterns like "Score global : XX/100" or "Score global: XX%"
   */
  function extractScore(markdown) {
    var patterns = [
      /Score\s*global\s*[:\u2013\u2014-]\s*(\d+)\s*\/\s*100/i,
      /Score\s*global\s*[:\u2013\u2014-]\s*(\d+)\s*%/i,
      /(\d+)\s*\/\s*100\s*(?:global|total)/i,
      /Note\s*(?:finale|globale)\s*[:\u2013\u2014-]\s*(\d+)/i
    ];
    for (var i = 0; i < patterns.length; i++) {
      var match = markdown.match(patterns[i]);
      if (match) return parseInt(match[1], 10);
    }
    return null;
  }

  /**
   * Get all saved reports from localStorage
   */
  function getAllReports() {
    var reports = [];
    for (var i = 0; i < localStorage.length; i++) {
      var key = localStorage.key(i);
      if (key && key.indexOf('ecos_report_') === 0) {
        try {
          var data = JSON.parse(localStorage.getItem(key));
          data._key = key;
          reports.push(data);
        } catch(e) {}
      }
    }
    // Sort by date descending
    reports.sort(function(a, b) {
      return new Date(b.date) - new Date(a.date);
    });
    return reports;
  }

  /**
   * Delete a report from localStorage
   */
  function deleteReport(key) {
    localStorage.removeItem(key);
  }

  /**
   * Format case name for display
   */
  function formatCaseDisplay(caseId) {
    return caseId
      .replace(/_-_/g, ' - ')
      .replace(/_/g, ' ')
      .replace(/ - Grille ECOS$/i, '')
      .trim();
  }

  // Expose
  window.EcosReport = {
    saveReport: saveReport,
    extractScore: extractScore,
    getAllReports: getAllReports,
    deleteReport: deleteReport,
    formatCaseDisplay: formatCaseDisplay
  };
})();
