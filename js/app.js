/* Shared across every page — Complete History of India. */

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
  const dbtn = document.getElementById('drawerThemeToggle');
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  const icon = isDark
    ? '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
    : '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.8A9 9 0 1111.2 3 7 7 0 0021 12.8z"/></svg>';
  if (btn) {
    btn.innerHTML = icon;
    btn.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
  }
  if (dbtn) {
    dbtn.innerHTML = `${icon} <span>${isDark ? 'Light Mode' : 'Dark Mode'}</span>`;
  }
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
  const dbtn = document.getElementById('drawerUpscToggle');
  if (btn) btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  if (dbtn) dbtn.setAttribute('aria-pressed', on ? 'true' : 'false');
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
    ['map.html', 'Map Lab'],
    ['practice.html', 'UPSC Hub'],
    ['up-history.html', 'UP Track'],
    ['themes.html', 'Themes'],
    ['people.html', 'People'],
    ['women.html', 'Women'],
    ['graph.html', 'Graph']
  ];

  el.innerHTML = `
    <div class="wrap nav-inner">
      <a href="index.html" class="brand">
        <svg class="mark" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="currentColor" stroke-width="2"/><path d="M16 6v20M8 12h16M8 20h16" stroke="currentColor" stroke-width="1.4" opacity=".6"/></svg>
        <span>Complete History of India<small>Interactive Atlas &amp; UPSC Companion</small></span>
      </a>

      <div class="nav-links">
        ${links.map(([href,label]) => `<a href="${href}" class="${active===href?'active':''}">${label}</a>`).join('')}
      </div>

      <div class="nav-tools">
        <button class="spotlight-btn" onclick="openSpotlight()" title="Search anything (Ctrl+K)">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
          <span class="spotlight-label">Search</span>
          <kbd class="spotlight-kbd">⌘K</kbd>
        </button>
        <button class="icon-btn calc-btn" onclick="openCalculator()" title="Quick Era &amp; Number Calculator" aria-label="Open Calculator">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="16" y1="14" x2="16" y2="18"/><path d="M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M8 18h.01M12 18h.01"/></svg>
        </button>
        <button class="upsc-toggle" id="upscToggle" aria-pressed="${document.body.classList.contains('upsc-on')}" onclick="toggleUpsc()" title="Toggle UPSC revision mode">
          <span class="dot"></span> UPSC Mode
        </button>
        <button class="icon-btn" id="themeToggle" onclick="toggleTheme()" aria-label="Toggle dark mode"></button>
        <button class="icon-btn hamburger-btn" id="mobileMenuBtn" onclick="toggleMobileDrawer()" aria-label="Open navigation menu">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>`;

  renderMobileDrawer(active);
  renderBottomNav(active);
  initSpotlight();
  initCalculator();
  updateThemeIcon();
}

/* Mobile Slide-out Drawer */
function renderMobileDrawer(active){
  let drawer = document.getElementById('mobileDrawer');
  if (!drawer) {
    drawer = document.createElement('div');
    drawer.id = 'mobileDrawer';
    drawer.className = 'mobile-drawer';
    document.body.appendChild(drawer);
  }

  const navItems = [
    { href: 'index.html', label: 'Home', icon: '🏠' },
    { href: 'timeline.html', label: 'Master Timeline', icon: '⏱️' },
    { href: 'map.html', label: 'Historical Map Lab', icon: '🗺️', badge: 'New' },
    { href: 'practice.html', label: 'UPSC Practice Hub', icon: '🎯', badge: 'New' },
    { href: 'up-history.html', label: 'Uttar Pradesh (UPPSC)', icon: '🏛️' },
    { href: 'themes.html', label: 'Themes Explorer', icon: '🎨' },
    { href: 'people.html', label: 'Key Personalities', icon: '👥' },
    { href: 'women.html', label: 'Women in History', icon: '👑' },
    { href: 'graph.html', label: 'Knowledge Graph', icon: '🕸️' },
    { href: 'search.html', label: 'Search Atlas', icon: '🔍' },
    { href: 'about.html', label: 'Sources & Method', icon: 'ℹ️' }
  ];

  drawer.innerHTML = `
    <div class="drawer-backdrop" onclick="closeMobileDrawer()"></div>
    <div class="drawer-panel">
      <div class="drawer-header">
        <div class="drawer-brand">
          <svg width="24" height="24" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="currentColor" stroke-width="2"/><path d="M16 6v20M8 12h16M8 20h16" stroke="currentColor" stroke-width="1.4" opacity=".6"/></svg>
          <b>History of India</b>
        </div>
        <button class="drawer-close" onclick="closeMobileDrawer()" aria-label="Close menu">&times;</button>
      </div>

      <div class="drawer-search">
        <button class="spotlight-trigger-btn" onclick="closeMobileDrawer(); openSpotlight();">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
          <span>Search everything (⌘K)...</span>
        </button>
      </div>

      <div class="drawer-links">
        ${navItems.map(item => `
          <a href="${item.href}" class="drawer-link ${active === item.href ? 'active' : ''}" onclick="closeMobileDrawer()">
            <span class="d-icon">${item.icon}</span>
            <span class="d-label">${item.label}</span>
            ${item.badge ? `<span class="badge badge-site badge-freedom" style="font-size:0.65rem; padding:2px 6px;">${item.badge}</span>` : ''}
          </a>
        `).join('')}
      </div>

      <div class="drawer-footer">
        <button class="drawer-tool-btn" id="drawerThemeToggle" onclick="toggleTheme()">
          <span>Toggle Theme</span>
        </button>
        <button class="drawer-tool-btn" onclick="closeMobileDrawer(); openCalculator();">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="16" y1="14" x2="16" y2="18"/></svg>
          <span>Era Calculator</span>
        </button>
        <button class="drawer-tool-btn upsc-toggle" id="drawerUpscToggle" onclick="toggleUpsc()">
          <span class="dot"></span> UPSC Mode
        </button>
      </div>
    </div>`;
}

function toggleMobileDrawer(){
  const drawer = document.getElementById('mobileDrawer');
  if (drawer) drawer.classList.toggle('open');
}
function closeMobileDrawer(){
  const drawer = document.getElementById('mobileDrawer');
  if (drawer) drawer.classList.remove('open');
}

/* Sticky Mobile Bottom Navigation Ribbon */
function renderBottomNav(active){
  let bnav = document.getElementById('mobileBottomNav');
  if (!bnav) {
    bnav = document.createElement('nav');
    bnav.id = 'mobileBottomNav';
    bnav.className = 'mobile-bottom-nav';
    document.body.appendChild(bnav);
  }

  bnav.innerHTML = `
    <a href="index.html" class="bnav-item ${active==='index.html'?'active':''}">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
      <span>Home</span>
    </a>
    <a href="timeline.html" class="bnav-item ${active==='timeline.html'?'active':''}">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
      <span>Timeline</span>
    </a>
    <a href="map.html" class="bnav-item ${active==='map.html'?'active':''}">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/></svg>
      <span>Map Lab</span>
    </a>
    <a href="practice.html" class="bnav-item ${active==='practice.html'?'active':''}">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
      <span>UPSC Hub</span>
    </a>
    <button class="bnav-item" onclick="openSpotlight()">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
      <span>Search</span>
    </button>`;
}

function renderFooter(){
  const el = document.getElementById('siteFooter');
  if (!el) return;
  el.innerHTML = `
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <h5>Complete History of India</h5>
          <p style="color:var(--ink-soft); font-size:.88rem; max-width:34ch;">An interactive historical atlas and UPSC study companion, built from a curated set of revision-sheet infographics spanning Prehistory to the Delhi Sultanate and modern India.</p>
        </div>
        <div>
          <h5>Explore</h5>
          <a href="timeline.html">Master Timeline</a>
          <a href="map.html">Historical Map Lab (New)</a>
          <a href="up-history.html">Uttar Pradesh History (UPPSC)</a>
          <a href="themes.html">Themes</a>
          <a href="people.html">People</a>
          <a href="women.html">Women in History</a>
        </div>
        <div>
          <h5>Study &amp; Practice</h5>
          <a href="practice.html">UPSC Prelims &amp; Mains Hub (New)</a>
          <a href="search.html">Search Atlas</a>
          <a href="graph.html">Knowledge Graph</a>
          <a href="index.html#periods">All Periods</a>
          <a href="index.html#upsc">UPSC Mode</a>
        </div>
        <div>
          <h5>About</h5>
          <a href="about.html">Sources &amp; Method</a>
          <a href="https://github.com/raghavendra-exp/history-of-india" target="_blank" rel="noopener noreferrer">GitHub Repository ↗</a>
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

/* ---------- External link helper ---------- */
let _extLinks = null;
async function extLink(keyword, displayText){
  if (!_extLinks) _extLinks = await HistoryData.loadLinks();
  const entry = _extLinks[keyword];
  const text = displayText || keyword;
  if (!entry) return text;
  return `<a class="ext-link" href="${entry.url}" target="_blank" rel="noopener noreferrer">${text}<span class="arrow">↗</span><span class="ext-tooltip">${entry.source} — open external resource</span></a>`;
}

async function linkifyPeopleList(names){
  const out = [];
  for (const n of names) out.push(await extLink(n));
  return out;
}

/* ---------- Spotlight Search (Ctrl+K / ⌘K) ---------- */
function initSpotlight(){
  if (document.getElementById('spotlightModal')) return;

  const modal = document.createElement('div');
  modal.id = 'spotlightModal';
  modal.className = 'spotlight-modal';
  modal.innerHTML = `
    <div class="spotlight-backdrop" onclick="closeSpotlight()"></div>
    <div class="spotlight-box">
      <div class="spotlight-input-wrap">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
        <input type="text" id="spotlightInput" placeholder="Search periods, events, people, archaeological sites, or questions..." autocomplete="off">
        <kbd class="spotlight-esc" onclick="closeSpotlight()">ESC</kbd>
      </div>
      <div class="spotlight-results" id="spotlightResults">
        <div class="spotlight-hint">
          <span>Type to search across 80 periods, 400+ events, key sites, and UPSC drills.</span>
        </div>
      </div>
    </div>`;
  document.body.appendChild(modal);

  const input = document.getElementById('spotlightInput');
  const results = document.getElementById('spotlightResults');
  let timer;

  input.addEventListener('input', () => {
    clearTimeout(timer);
    timer = setTimeout(async () => {
      const q = input.value.trim();
      if (!q){
        results.innerHTML = '<div class="spotlight-hint"><span>Type to search across 80 periods, 400+ events, key sites, and UPSC drills.</span></div>';
        return;
      }
      const hits = await Search.query(q);
      if (!hits.length){
        results.innerHTML = `<div class="spotlight-empty">No historical records found for "${q}". Try searching "Harappa", "Ashoka", "1857", "Chola", or "Bhakti".</div>`;
        return;
      }
      results.innerHTML = hits.map((h, i) => `
        <a class="spotlight-item ${i===0?'selected':''}" href="${h.href}" onclick="closeSpotlight()">
          <span class="sp-kind sp-${h.kind.toLowerCase().replace(/[^a-z]/g,'')}">${h.kind}</span>
          <div class="sp-text">
            <span class="sp-title">${h.title}</span>
            <span class="sp-sub">${h.sub}</span>
          </div>
          <span class="sp-arrow">&rarr;</span>
        </a>`).join('');
    }, 120);
  });

  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openSpotlight();
    } else if (e.key === 'Escape') {
      closeSpotlight();
      closeCalculator();
    }
  });
}

function openSpotlight(){
  const modal = document.getElementById('spotlightModal');
  if (!modal) return;
  modal.classList.add('open');
  const input = document.getElementById('spotlightInput');
  if (input) {
    input.value = '';
    setTimeout(() => input.focus(), 50);
  }
}
function closeSpotlight(){
  const modal = document.getElementById('spotlightModal');
  if (modal) modal.classList.remove('open');
}

/* ---------- Modern Animated Calculator Modal ---------- */
let calcState = { expr: '', curr: '0', justEvaluated: false };

function initCalculator(){
  if (document.getElementById('calcModal')) return;

  const modal = document.createElement('div');
  modal.id = 'calcModal';
  modal.className = 'calc-modal';
  modal.innerHTML = `
    <div class="calc-backdrop" onclick="closeCalculator()"></div>
    <div class="calc-card">
      <div class="calc-header">
        <div class="calc-title">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="16" y1="14" x2="16" y2="18"/></svg>
          <b>Era &amp; Year Calculator</b>
        </div>
        <button class="calc-close" onclick="closeCalculator()" aria-label="Close calculator">&times;</button>
      </div>

      <div class="calc-display">
        <div class="calc-expr" id="calcExpr"></div>
        <div class="calc-val" id="calcVal">0</div>
      </div>

      <div class="calc-keypad">
        <button class="ck-btn ck-fn" onclick="calcAction('clear')">C</button>
        <button class="ck-btn ck-fn" onclick="calcAction('backspace')">⌫</button>
        <button class="ck-btn ck-fn" onclick="calcAction('percent')">%</button>
        <button class="ck-btn ck-op" onclick="calcAction('/')">&divide;</button>

        <button class="ck-btn ck-num" onclick="calcAction('7')">7</button>
        <button class="ck-btn ck-num" onclick="calcAction('8')">8</button>
        <button class="ck-btn ck-num" onclick="calcAction('9')">9</button>
        <button class="ck-btn ck-op" onclick="calcAction('*')">&times;</button>

        <button class="ck-btn ck-num" onclick="calcAction('4')">4</button>
        <button class="ck-btn ck-num" onclick="calcAction('5')">5</button>
        <button class="ck-btn ck-num" onclick="calcAction('6')">6</button>
        <button class="ck-btn ck-op" onclick="calcAction('-')">&minus;</button>

        <button class="ck-btn ck-num" onclick="calcAction('1')">1</button>
        <button class="ck-btn ck-num" onclick="calcAction('2')">2</button>
        <button class="ck-btn ck-num" onclick="calcAction('3')">3</button>
        <button class="ck-btn ck-op" onclick="calcAction('+')">+</button>

        <button class="ck-btn ck-fn" onclick="calcAction('plusminus')">&plusmn;</button>
        <button class="ck-btn ck-num" onclick="calcAction('0')">0</button>
        <button class="ck-btn ck-num" onclick="calcAction('.')">.</button>
        <button class="ck-btn ck-eq" onclick="calcAction('eval')">=</button>
      </div>

      <div class="calc-footer-hint">Quick calculation for years, spans, and dates without navigating away.</div>
    </div>`;
  document.body.appendChild(modal);

  // Physical keyboard support for calculator when open
  document.addEventListener('keydown', (e) => {
    const modal = document.getElementById('calcModal');
    if (!modal || !modal.classList.contains('open')) return;

    if (e.key >= '0' && e.key <= '9') calcAction(e.key);
    else if (['+', '-', '*', '/'].includes(e.key)) calcAction(e.key);
    else if (e.key === 'Enter' || e.key === '=') { e.preventDefault(); calcAction('eval'); }
    else if (e.key === 'Backspace') calcAction('backspace');
    else if (e.key === 'Escape') closeCalculator();
    else if (e.key === '.') calcAction('.');
  });
}

function calcAction(act){
  const exprEl = document.getElementById('calcExpr');
  const valEl = document.getElementById('calcVal');

  if (act === 'clear') {
    calcState.expr = '';
    calcState.curr = '0';
    calcState.justEvaluated = false;
  } else if (act === 'backspace') {
    if (calcState.justEvaluated) {
      calcState.curr = '0';
    } else {
      calcState.curr = calcState.curr.length > 1 ? calcState.curr.slice(0, -1) : '0';
    }
  } else if (act === 'plusminus') {
    if (calcState.curr !== '0') {
      calcState.curr = calcState.curr.startsWith('-') ? calcState.curr.slice(1) : '-' + calcState.curr;
    }
  } else if (act === 'percent') {
    const num = parseFloat(calcState.curr);
    calcState.curr = String(num / 100);
  } else if (['+', '-', '*', '/'].includes(act)) {
    calcState.expr += ` ${calcState.curr} ${act}`;
    calcState.curr = '0';
    calcState.justEvaluated = false;
  } else if (act === 'eval') {
    try {
      const fullExpr = (calcState.expr + ' ' + calcState.curr).trim();
      // Safe math evaluator using tokens
      const sanitized = fullExpr.replace(/[^0-9+\-*/. ]/g, '');
      const res = Function(`"use strict"; return (${sanitized})`)();
      calcState.expr = fullExpr + ' =';
      calcState.curr = String(Math.round(res * 100000) / 100000);
      calcState.justEvaluated = true;
    } catch(err) {
      calcState.curr = 'Error';
    }
  } else if (act === '.') {
    if (!calcState.curr.includes('.')) calcState.curr += '.';
  } else {
    // Number typed
    if (calcState.curr === '0' || calcState.justEvaluated) {
      calcState.curr = act;
      calcState.justEvaluated = false;
    } else {
      calcState.curr += act;
    }
  }

  if (exprEl) exprEl.textContent = calcState.expr;
  if (valEl) valEl.textContent = calcState.curr;
}

function openCalculator(){
  const modal = document.getElementById('calcModal');
  if (!modal) return;
  modal.classList.add('open');
}
function closeCalculator(){
  const modal = document.getElementById('calcModal');
  if (modal) modal.classList.remove('open');
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

document.addEventListener('DOMContentLoaded', updateThemeIcon);
