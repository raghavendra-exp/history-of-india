/* Client-side search across periods, events, people, themes — no backend. */

const Search = (() => {
  let index = null;

  async function build(){
    if (index) return index;
    const d = await HistoryData.load();
    index = [];
    d.periods.forEach(p => {
      index.push({ kind: 'Period', title: p.title, sub: p.dateRange, href: `period.html?id=${p.id}`, text: (p.title + ' ' + p.tagline + ' ' + p.overview).toLowerCase() });
      (p.events || []).forEach(e => {
        index.push({ kind: 'Event', title: e.title, sub: `${e.year} · ${p.title}`, href: `period.html?id=${p.id}#event-${slug(e.title)}`, text: (e.title + ' ' + e.desc + ' ' + e.year + ' ' + p.title).toLowerCase() });
      });
      (p.people || []).forEach(pe => {
        index.push({ kind: 'Person', title: pe.name, sub: `${pe.role || ''} · ${p.title}`, href: `period.html?id=${p.id}#people`, text: (pe.name + ' ' + (pe.role||'') + ' ' + (pe.note||'') + ' ' + p.title).toLowerCase() });
      });
      (p.women || []).forEach(w => {
        index.push({ kind: 'Woman in History', title: w.name, sub: `${w.role || ''} · ${p.title}`, href: `period.html?id=${p.id}#women`, text: (w.name + ' ' + (w.note||'') + ' ' + p.title).toLowerCase() });
      });
      (p.themes || []).forEach(t => {
        const label = HistoryData.THEME_LABELS[t] || t;
        index.push({ kind: 'Theme', title: label, sub: p.title, href: `themes.html#${t}`, text: (label + ' ' + p.title).toLowerCase() });
      });
    });
    return index;
  }

  function slug(s){ return s.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/(^-|-$)/g,''); }

  async function query(q){
    const idx = await build();
    const terms = q.toLowerCase().trim().split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    return idx.filter(item => terms.every(t => item.text.includes(t))).slice(0, 40);
  }

  return { build, query, slug };
})();

/* Wires up an <input> + results container for live search */
function wireQuickSearch(inputId, resultsId){
  const input = document.getElementById(inputId);
  const results = document.getElementById(resultsId);
  if (!input || !results) return;
  let t;
  input.addEventListener('input', () => {
    clearTimeout(t);
    t = setTimeout(async () => {
      const q = input.value.trim();
      if (!q){ results.classList.remove('open'); results.innerHTML=''; return; }
      const hits = await Search.query(q);
      results.innerHTML = hits.length
        ? hits.map(h => `<a class="search-result" href="${h.href}"><span class="r-kind">${h.kind}</span><span class="r-title">${h.title}</span><span class="r-sub">${h.sub}</span></a>`).join('')
        : `<div class="search-empty">No matches for “${q}”. Try a year, event, person or theme.</div>`;
      results.classList.add('open');
    }, 160);
  });
  document.addEventListener('click', e => {
    if (!input.contains(e.target) && !results.contains(e.target)) results.classList.remove('open');
  });
}
