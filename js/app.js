/* Shared across every page. */

/* ---------- Theme (dark mode) ---------- */
(function initTheme(){
  const saved = localStorage.getItem('chi-theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const theme = saved || (prefersDark ? 'dark' : 'light');
  if (theme === 'dark') document.documentElement.setAttribute('data-theme', 'dark');
})();

function toggleTheme(){
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  if (isDark){ document.documentElement.removeAttribute('data-theme'); localStorage.setItem('chi-theme','light'); }
  else { document.documentElement.setAttribute('data-theme','dark'); localStorage.setItem('chi-theme','dark'); }
  updateThemeIcon();
}
function updateThemeIcon(){
  const btn = document.getElementById('themeToggle');
  if (!btn) return;
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  btn.innerHTML = isDark
    ? '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
    : '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.8A9 9 0 1111.2 3 7 7 0 0021 12.8z"/></svg>';
  btn.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
}

/* ---------- UPSC Mode ---------- */
(function initUpsc(){
  const on = localStorage.getItem('chi-upsc') === '1';
  if (on) document.body.classList.add('upsc-on');
})();
function toggleUpsc(){
  const on = document.body.classList.toggle('upsc-on');
  localStorage.setItem('chi-upsc', on ? '1' : '0');
  const btn = document.getElementById('upscToggle');
  if (btn) btn.setAttribute('aria-pressed', on ? 'true' : 'false');
}

/* ---------- Nav / Footer injection ---------- */
function currentPage(){
  const p = location.pathname.split('/').pop() || 'index.html';
  return p;
}

function renderNav(active){
  const el = document.getElementById('siteNav');
  if (!el) return;
  const links = [
    ['index.html', 'Home'],
    ['timeline.html', 'Timeline'],
    ['up-history.html', 'UP History (UPPSC)'],
    ['themes.html', 'Themes'],
    ['people.html', 'People'],
    ['women.html', 'Women'],
    ['graph.html', 'Knowledge Graph'],
    ['search.html', 'Search']
  ];
  el.innerHTML = `
    <div class="wrap">
      <a href="index.html" class="brand">
        <svg class="mark" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="currentColor" stroke-width="2"/><path d="M16 6v20M8 12h16M8 20h16" stroke="currentColor" stroke-width="1.4" opacity=".6"/></svg>
        <span>Complete History of India<small>Interactive Atlas &amp; UPSC Companion</small></span>
      </a>
      <div class="nav-links">
        ${links.map(([href,label]) => `<a href="${href}" class="${active===href?'active':''}">${label}</a>`).join('')}
      </div>
      <div class="nav-tools">
        <button class="upsc-toggle" id="upscToggle" aria-pressed="${document.body.classList.contains('upsc-on')}" onclick="toggleUpsc()" title="Toggle UPSC revision mode">
          <span class="dot"></span> UPSC Mode
        </button>
        <button class="icon-btn" id="themeToggle" onclick="toggleTheme()" aria-label="Toggle dark mode"></button>
      </div>
    </div>`;
  updateThemeIcon();
}

function renderFooter(){
  const el = document.getElementById('siteFooter');
  if (!el) return;
  el.innerHTML = `
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <h5>Complete History of India</h5>
          <p style="color:var(--ink-soft); font-size:.88rem; max-width:34ch;">An interactive historical atlas and UPSC study companion, built from a curated set of revision-sheet infographics spanning Prehistory to the Delhi Sultanate.</p>
        </div>
        <div>
          <h5>Explore</h5>
          <a href="timeline.html">Master Timeline</a>
          <a href="up-history.html">Uttar Pradesh History (UPPSC)</a>
          <a href="themes.html">Themes</a>
          <a href="people.html">People</a>
          <a href="women.html">Women in History</a>
        </div>
        <div>
          <h5>Study</h5>
          <a href="search.html">Search</a>
          <a href="graph.html">Knowledge Graph</a>
          <a href="index.html#periods">All Periods</a>
          <a href="index.html#upsc">UPSC Mode</a>
        </div>
        <div>
          <h5>About</h5>
          <a href="about.html">Sources &amp; Method</a>
          <a href="https://github.com" target="_blank" rel="noopener noreferrer">GitHub Repository ↗</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>Complete History of India — an educational project. Not an official Government resource.</span>
        <span>Content sourced from supplied revision sheets; external links point to official / encyclopedic sources.</span>
      </div>
    </div>`;
}

function renderBreadcrumb(trail){
  const el = document.getElementById('breadcrumb');
  if (!el) return;
  el.innerHTML = trail.map((t,i) => {
    const isLast = i === trail.length - 1;
    return (i>0 ? '<span class="sep">/</span>' : '') + (isLast || !t.href ? `<span>${t.label}</span>` : `<a href="${t.href}">${t.label}</a>`);
  }).join('');
}

/* ---------- External link helper ----------
   Renders a keyword as a styled external link if it exists in the
   external-links.json map; otherwise returns plain text. */
let _extLinks = null;
async function extLink(keyword, displayText){
  if (!_extLinks) _extLinks = await HistoryData.loadLinks();
  const entry = _extLinks[keyword];
  const text = displayText || keyword;
  if (!entry) return text;
  return `<a class="ext-link" href="${entry.url}" target="_blank" rel="noopener noreferrer">${text}<span class="arrow">↗</span><span class="ext-tooltip">${entry.source} — open external resource</span></a>`;
}

/* Linkify occurrences of known keywords inside a block of plain text/HTML-safe string (used sparingly, on names only) */
async function linkifyPeopleList(names){
  const out = [];
  for (const n of names) out.push(await extLink(n));
  return out;
}

/* ---------- Lightbox ---------- */
function openLightbox(src, title){
  let lb = document.getElementById('lightbox');
  if (!lb){
    lb = document.createElement('div');
    lb.id = 'lightbox';
    lb.className = 'lightbox';
    lb.innerHTML = `
      <button class="lightbox-close" aria-label="Close">&times;</button>
      <div class="lightbox-stage"><img id="lbImg" alt=""></div>
      <div class="lightbox-bar">
        <button id="lbZoomOut">− Zoom Out</button>
        <button id="lbZoomIn">+ Zoom In</button>
        <button id="lbReset">Reset</button>
        <a id="lbDownload" download>Download / Open Original ↗</a>
      </div>`;
    document.body.appendChild(lb);
    lb.querySelector('.lightbox-close').onclick = closeLightbox;
    lb.addEventListener('click', e => { if (e.target === lb) closeLightbox(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeLightbox(); });
    let scale = 1;
    const img = lb.querySelector('#lbImg');
    lb.querySelector('#lbZoomIn').onclick = () => { scale = Math.min(scale + 0.3, 4); img.style.transform = `scale(${scale})`; };
    lb.querySelector('#lbZoomOut').onclick = () => { scale = Math.max(scale - 0.3, 0.4); img.style.transform = `scale(${scale})`; };
    lb.querySelector('#lbReset').onclick = () => { scale = 1; img.style.transform = 'scale(1)'; };
  }
  document.getElementById('lbImg').src = src;
  document.getElementById('lbImg').alt = title || 'Original revision sheet';
  document.getElementById('lbImg').style.transform = 'scale(1)';
  document.getElementById('lbDownload').href = src;
  lb.classList.add('open');
}
function closeLightbox(){
  const lb = document.getElementById('lightbox');
  if (lb) lb.classList.remove('open');
}

/* ---------- Scroll reveal ---------- */
function initReveal(){
  const els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window) || !els.length) { els.forEach(e => e.classList.add('in')); return; }
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => { if (en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { threshold: 0.12 });
  els.forEach(e => io.observe(e));
}

/* ---------- Theme markers on load ---------- */
document.addEventListener('DOMContentLoaded', updateThemeIcon);
