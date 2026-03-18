(function() {
  var pageKey = "ecos_" + location.pathname.split("/").pop().replace(/\.html$/, "");

  function saveState() {
    var state = { r: {}, c: {}, t: {} };
    var radios = document.querySelectorAll("input[type=radio]:checked");
    for (var i = 0; i < radios.length; i++) {
      state.r[radios[i].name] = radios[i].value;
    }
    var checks = document.querySelectorAll("input[type=checkbox]:checked");
    for (var i = 0; i < checks.length; i++) {
      if (checks[i].id) state.c[checks[i].id] = 1;
    }
    var texts = document.querySelectorAll("textarea");
    for (var i = 0; i < texts.length; i++) {
      if (texts[i].id && texts[i].value.trim()) state.t[texts[i].id] = texts[i].value;
    }
    try { localStorage.setItem(pageKey, JSON.stringify(state)); } catch(e) {}
    updateSaveIndicator(true);
  }

  function loadState() {
    var raw;
    try { raw = localStorage.getItem(pageKey); } catch(e) { return; }
    if (!raw) return;
    var state;
    try { state = JSON.parse(raw); } catch(e) { return; }

    if (state.r) {
      var names = Object.keys(state.r);
      for (var i = 0; i < names.length; i++) {
        var radio = document.querySelector('input[type=radio][name="' + names[i] + '"][value="' + state.r[names[i]] + '"]');
        if (radio) {
          radio.checked = true;
          radio.dispatchEvent(new Event("change"));
        }
      }
    }
    if (state.c) {
      var ids = Object.keys(state.c);
      for (var i = 0; i < ids.length; i++) {
        var cb = document.getElementById(ids[i]);
        if (cb && !cb.checked) {
          cb.checked = true;
          cb.dispatchEvent(new Event("change"));
        }
      }
    }
    if (state.t) {
      var tids = Object.keys(state.t);
      for (var i = 0; i < tids.length; i++) {
        var ta = document.getElementById(tids[i]);
        if (ta) {
          ta.value = state.t[tids[i]];
          if (typeof autoResizeTextarea === "function") autoResizeTextarea(ta);
        }
      }
    }
    updateSaveIndicator(true);
  }

  function clearState() {
    if (confirm("Effacer toutes les r\u00e9ponses enregistr\u00e9es pour ce cas ?")) {
      try { localStorage.removeItem(pageKey); } catch(e) {}
      location.reload();
    }
  }

  function updateSaveIndicator(saved) {
    var el = document.getElementById("save-indicator");
    if (!el) return;
    el.textContent = saved ? "\u2713 Sauvegard\u00e9" : "";
    el.style.opacity = saved ? "1" : "0";
    if (saved) { setTimeout(function() { el.style.opacity = "0.6"; }, 1500); }
  }

  var bar = document.createElement("div");
  bar.style.cssText = "position:fixed;bottom:1rem;right:1rem;z-index:9999;display:flex;align-items:center;gap:0.5rem;";
  var indicator = document.createElement("span");
  indicator.id = "save-indicator";
  indicator.style.cssText = "font-size:0.75rem;color:#16a34a;font-weight:600;transition:opacity 0.3s;opacity:0;font-family:Inter,sans-serif;background:white;padding:0.25rem 0.5rem;border-radius:6px;box-shadow:0 1px 3px rgba(0,0,0,0.1);";
  var resetBtn = document.createElement("button");
  resetBtn.textContent = "R\u00e9initialiser";
  resetBtn.style.cssText = "font-size:0.7rem;padding:0.3rem 0.6rem;border:1px solid #e2e8f0;border-radius:6px;background:white;color:#64748b;cursor:pointer;font-family:Inter,sans-serif;box-shadow:0 1px 3px rgba(0,0,0,0.1);transition:all 0.2s;";
  resetBtn.onmouseover = function() { this.style.borderColor="#f87171"; this.style.color="#dc2626"; };
  resetBtn.onmouseout = function() { this.style.borderColor="#e2e8f0"; this.style.color="#64748b"; };
  resetBtn.onclick = clearState;
  bar.appendChild(indicator);
  bar.appendChild(resetBtn);
  document.body.appendChild(bar);

  loadState();

  document.addEventListener("change", function(e) {
    if (e.target.type === "radio" || e.target.type === "checkbox") saveState();
  });
  document.addEventListener("input", function(e) {
    if (e.target.tagName === "TEXTAREA") saveState();
  });
})();
