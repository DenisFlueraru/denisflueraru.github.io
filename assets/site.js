/* Denis Flueraru — portfolio behaviour: menu, image fallbacks, index filter, lightbox, logo flip. */
(function () {
  "use strict";
  var doc = document;

  /* ---- menu ---- */
  var btn = doc.querySelector(".menu-btn");
  var panel = doc.getElementById("menu");
  function setMenu(open) {
    if (!panel || !btn) return;
    panel.hidden = !open;
    btn.setAttribute("aria-expanded", String(open));
    doc.body.classList.toggle("menu-open", open);
    if (open) { var c = panel.querySelector(".menu-close"); if (c) c.focus(); } else { btn.focus(); }
  }
  if (btn && panel) {
    btn.addEventListener("click", function () { setMenu(true); });
    panel.querySelector(".menu-close").addEventListener("click", function () { setMenu(false); });
    doc.addEventListener("keydown", function (e) { if (e.key === "Escape" && !panel.hidden) setMenu(false); });
  }

  /* ---- image fallbacks: a failed image leaves the hatched frame with its label ---- */
  function markMissing(img) { var f = img.closest(".frame"); if (f) f.classList.add("missing"); }
  doc.addEventListener("error", function (e) {
    if (e.target && e.target.tagName === "IMG") markMissing(e.target);
  }, true);
  Array.prototype.forEach.call(doc.querySelectorAll(".frame img"), function (img) {
    if (img.complete && img.naturalWidth === 0 && img.getAttribute("src")) markMissing(img);
  });

  /* ---- index filter ---- */
  var filters = doc.querySelectorAll(".filters button");
  var rows = doc.querySelectorAll(".rows .row");
  var count = doc.querySelector(".count");
  function applyFilter(cat) {
    var n = 0;
    Array.prototype.forEach.call(rows, function (r) {
      var show = cat === "all" || r.getAttribute("data-cat") === cat;
      r.hidden = !show; if (show) n++;
    });
    Array.prototype.forEach.call(filters, function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-filter") === cat));
    });
    if (count) count.textContent = n + (n === 1 ? " entry" : " entries");
  }
  Array.prototype.forEach.call(filters, function (b) {
    b.addEventListener("click", function () {
      var cat = b.getAttribute("data-filter");
      applyFilter(cat);
      try { history.replaceState(null, "", cat === "all" ? location.pathname : "#" + cat); } catch (err) {}
    });
  });
  if (filters.length) {
    var h = (location.hash || "").slice(1);
    var valid = Array.prototype.some.call(filters, function (b) { return b.getAttribute("data-filter") === h; });
    applyFilter(valid ? h : "all");
  }

  /* ---- lightbox ---- */
  var lb = doc.getElementById("lightbox");
  if (lb) {
    var lbImg = lb.querySelector("img");
    var lbCount = lb.querySelector(".lb-count");
    var set = [], idx = 0, lastFocus = null;
    function show(i) {
      idx = (i + set.length) % set.length;
      var src = set[idx].getAttribute("data-full") || set[idx].currentSrc || set[idx].src;
      lbImg.src = src; lbImg.alt = set[idx].alt || "";
      lbCount.textContent = (idx + 1) + " / " + set.length;
    }
    function open(img) {
      var group = img.closest("[data-gallery]") || doc.body;
      set = Array.prototype.filter.call(group.querySelectorAll(".frame[data-zoom] img"), function (x) {
        return !x.closest(".frame").classList.contains("missing");
      });
      lastFocus = doc.activeElement;
      lb.hidden = false; doc.body.classList.add("menu-open");
      show(Math.max(0, set.indexOf(img)));
      lb.querySelector(".lb-close").focus();
    }
    function close() { lb.hidden = true; doc.body.classList.remove("menu-open"); lbImg.src = ""; if (lastFocus) lastFocus.focus(); }
    doc.addEventListener("click", function (e) {
      var f = e.target.closest && e.target.closest(".frame[data-zoom]");
      if (f && !f.classList.contains("missing")) { var im = f.querySelector("img"); if (im) open(im); }
    });
    doc.addEventListener("keydown", function (e) {
      if (lb.hidden) {
        var f = e.target.closest && e.target.closest(".frame[data-zoom]");
        if (f && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); var im = f.querySelector("img"); if (im) open(im); }
        return;
      }
      if (e.key === "Escape") close();
      if (e.key === "ArrowRight") show(idx + 1);
      if (e.key === "ArrowLeft") show(idx - 1);
    });
    lb.querySelector(".lb-close").addEventListener("click", close);
    lb.querySelector(".lb-next").addEventListener("click", function () { show(idx + 1); });
    lb.querySelector(".lb-prev").addEventListener("click", function () { show(idx - 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb || e.target === lbImg.parentNode) close(); });
    var x0 = null;
    lb.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 40) show(idx + (dx < 0 ? 1 : -1));
    });
  }

  /* ---- click-to-play YouTube (opens YouTube instead when the page is opened from disk) ---- */
  doc.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest(".yt-btn");
    if (!a || location.protocol === "file:") return;
    e.preventDefault();
    var f = doc.createElement("iframe");
    f.src = "https://www.youtube.com/embed/" + a.getAttribute("data-yt") + "?autoplay=1&rel=0&playsinline=1";
    f.title = a.getAttribute("aria-label") || "Video";
    f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
    f.allowFullscreen = true;
    f.referrerPolicy = "strict-origin-when-cross-origin";
    a.parentNode.replaceChild(f, a);
  });

  /* ---- ATOMAT LAB mark: swap logo / FIELD5 every few seconds ---- */
  var mark = doc.querySelector(".spin img");
  if (mark && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var srcs = [mark.getAttribute("src"), mark.getAttribute("data-alt")].filter(Boolean);
    srcs.forEach(function (s) { var i = new Image(); i.src = s; });
    var k = 0;
    setInterval(function () {
      mark.style.opacity = 0;
      setTimeout(function () { k = (k + 1) % srcs.length; mark.src = srcs[k]; mark.style.opacity = 1; }, 300);
    }, 3500);
  }
})();
