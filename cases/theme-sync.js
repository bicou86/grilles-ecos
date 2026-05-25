(function () {
  var t = null;
  try {
    t = localStorage.getItem("ecos_theme");
  } catch (e) {}
  document.documentElement.setAttribute(
    "data-theme",
    t === "light" ? "light" : "dark",
  );
})();
