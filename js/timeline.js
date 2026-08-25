let TL_STATE = { filter: 'all', periods: [] };

async function renderTimelinePage(){
  renderNav('timeline.html');
  renderBreadcrumb([{ label: 'Home', href: 'index.html' }, { label: 'Master Timeline' }]);
  const d = await HistoryData.load();
  TL_STATE.periods = d.periods;

  const themeSet = new Set();
  d.periods.forEach(p => (p.themes||[]).forEach(t => themeSet.add(t)));

  document.getElementById('filterBar').innerHTML = ['all', ...themeSet].map(t => `
    <button class="filter-chip ${t==='all'?'active':''}" data-filter="${t}">${t==='all' ? 'All' : (HistoryData.THEME_LABELS[t]||t)}</button>
  `).join('');

  document.querySelectorAll('.filter-chip').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-chip').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      TL_STATE.filter = btn.dataset.filter;
      draw();
    });
  });

  draw();
  renderFooter();

  document.getElementById('modalBackdrop').addEventListener('click', e => {
    if (e.target.id === 'modalBackdrop') closeModal();
  });
}

function draw(){
  const wrap = document.getElementById('mtimeline');
  const f = TL_STATE.filter;
  const periods = TL_STATE.periods.filter(p => f==='all' || (p.themes||[]).includes(f));

  wrap.innerHTML = periods.map((p, i) => {
    const events = f==='all' ? (p.events||[]) : (p.events||[]).filter(e => e.theme === f);
    if (f !== 'all' && events.length === 0) return '';
    return `
    <div class="tl-period ${i===0?'open':''}" data-id="${p.id}">
      <div class="tl-period-head" role="button" tabindex="0" aria-expanded="${i===0}">
        <div class="tlh-left">
          <h3>${p.title}</h3>
          <span class="t-range">${p.dateRange}</span>
        </div>
        <div style="display:flex; align-items:center; gap:14px;">
          <a href="period.html?id=${p.id}" class="btn btn-ghost btn-sm" onclick="event.stopPropagation()">Open Period Page →</a>
          <span class="tl-caret">▸</span>
        </div>
      </div>
      <div class="tl-events">
        ${events.map(e => `
          <button class="tl-event" data-title="${encodeURIComponent(e.title)}" data-period="${p.id}">
            <span class="ev-year">${e.year}</span>
            <div class="ev-title">${e.title}</div>
            <span class="theme-chip">${HistoryData.THEME_LABELS[e.theme]||e.theme}</span>
          </button>`).join('') || '<p style="color:var(--ink-faint); font-size:.85rem;">No events tagged for this filter in this period.</p>'}
      </div>
    </div>`;
  }).join('') || '<p class="loading-note">No periods match this filter.</p>';

  wrap.querySelectorAll('.tl-period-head').forEach(head => {
    head.addEventListener('click', () => {
      const row = head.parentElement;
      const willOpen = !row.classList.contains('open');
      row.classList.toggle('open');
      head.setAttribute('aria-expanded', willOpen);
    });
  });

  wrap.querySelectorAll('.tl-event').forEach(btn => {
    btn.addEventListener('click', async () => {
      const p = TL_STATE.periods.find(x => x.id === btn.dataset.period);
      const e = (p.events||[]).find(x => x.title === decodeURIComponent(btn.dataset.title));
      await openEventModal(e, p);
    });
  });
}

async function openEventModal(e, p){
  const modal = document.getElementById('modalBackdrop');
  document.getElementById('modalBody').innerHTML = `
    <button class="modal-close" onclick="closeModal()" aria-label="Close">&times;</button>
    <span class="m-year">${e.year}</span>
    <h3>${e.title}</h3>
    <span class="theme-chip">${HistoryData.THEME_LABELS[e.theme]||e.theme}</span>
    <p style="margin-top:14px; color:var(--ink-soft);">${e.desc}</p>
    <div class="m-related">
      <a class="btn btn-outline btn-sm" href="period.html?id=${p.id}">Open Full Period: ${p.title} →</a>
    </div>
  `;
  modal.classList.add('open');
}
function closeModal(){ document.getElementById('modalBackdrop').classList.remove('open'); }

document.addEventListener('DOMContentLoaded', renderTimelinePage);
