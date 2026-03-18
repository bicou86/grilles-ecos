// Spaced Repetition System (SM-2 simplifié)
var SRS = (function() {
  var KEY = 'ecos_srs';

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch(e) { return {}; }
  }

  function save(data) {
    try { localStorage.setItem(KEY, JSON.stringify(data)); } catch(e) {}
  }

  function gradeToQ(grade) {
    var map = {A: 5, B: 4, C: 3, D: 2, E: 1};
    return map[(grade || '').toUpperCase()] || 1;
  }

  function todayStr() {
    return new Date().toISOString().slice(0, 10);
  }

  function addDays(days) {
    var d = new Date();
    d.setDate(d.getDate() + days);
    return d.toISOString().slice(0, 10);
  }

  return {
    update: function(filename, gradeStr) {
      var data = load();
      var card = data[filename] || {interval: 0, ease: 2.5, reps: 0, nextReview: null, lastGrade: null, lastReview: null};
      var q = gradeToQ(gradeStr);
      var today = todayStr();

      if (q >= 3) {
        // Successful recall
        if (card.reps === 0) card.interval = 1;
        else if (card.reps === 1) card.interval = 3;
        else card.interval = Math.round(card.interval * card.ease);
        card.reps++;
        // SM-2 ease factor update
        card.ease = Math.max(1.3, card.ease + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)));
      } else {
        // Failed recall (D or E) — reset
        card.reps = 0;
        card.interval = 1;
      }

      card.nextReview = addDays(card.interval);
      card.lastGrade = gradeStr;
      card.lastReview = today;
      data[filename] = card;
      save(data);
    },

    getDueToday: function() {
      var data = load();
      var today = todayStr();
      var due = [];
      Object.keys(data).forEach(function(f) {
        if (data[f].nextReview && data[f].nextReview <= today) due.push(f);
      });
      return due;
    },

    override: function(filename, action) {
      var data = load();
      var card = data[filename] || {interval: 0, ease: 2.5, reps: 0};
      var today = todayStr();

      if (action === 'mastered') {
        card.interval = 60;
        card.reps = 10;
        card.nextReview = addDays(60);
      } else if (action === 'review') {
        card.interval = 0;
        card.reps = 0;
        card.nextReview = today;
      }
      card.lastReview = today;
      data[filename] = card;
      save(data);
    },

    getStats: function() {
      var data = load();
      var today = todayStr();
      var stats = {due: 0, learning: 0, mastered: 0, total: 0};
      Object.keys(data).forEach(function(f) {
        var c = data[f];
        stats.total++;
        if (c.interval >= 30) stats.mastered++;
        else stats.learning++;
        if (c.nextReview && c.nextReview <= today) stats.due++;
      });
      return stats;
    },

    getCard: function(filename) {
      var data = load();
      return data[filename] || null;
    }
  };
})();
