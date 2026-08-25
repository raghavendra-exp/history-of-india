/* Central data access layer.
   All pages pull through HistoryData so future periods can be added
   just by editing data/history.json — no HTML changes required. */

const HistoryData = (() => {
  let _cache = null;
  let _links = null;

  function rootPath() {
    // works whether page is at / or /periods-style deep link (we use query-param routing, so root is constant)
    return '';
  }

  async function load() {
    if (_cache) return _cache;
    const res = await fetch('data/history.json');
    _cache = await res.json();
    _cache.periods.sort((a, b) => a.order - b.order);
    return _cache;
  }

  async function loadLinks() {
    if (_links) return _links;
    const res = await fetch('data/external-links.json');
    _links = await res.json();
    return _links;
  }

  async function getPeriod(id) {
    const d = await load();
    return d.periods.find(p => p.id === id) || null;
  }

  async function getAdjacent(id) {
    const d = await load();
    const idx = d.periods.findIndex(p => p.id === id);
    return {
      prev: idx > 0 ? d.periods[idx - 1] : null,
      next: idx < d.periods.length - 1 ? d.periods[idx + 1] : null
    };
  }

  async function allEvents() {
    const d = await load();
    const out = [];
    d.periods.forEach(p => (p.events || []).forEach(e => out.push({ ...e, periodId: p.id, periodTitle: p.title })));
    return out;
  }

  async function allPeople(includeWomen = true) {
    const d = await load();
    const out = [];
    d.periods.forEach(p => {
      (p.people || []).forEach(pe => out.push({ ...pe, periodId: p.id, periodTitle: p.title, isWomen: false }));
      if (includeWomen) (p.women || []).forEach(w => out.push({ name: w.name, role: w.role || 'Women in History', note: w.note, periodId: p.id, periodTitle: p.title, isWomen: true }));
    });
    return out;
  }

  const THEME_LABELS = {
    polity: 'Polity', war: 'War & Security', religion: 'Religion', economy: 'Economy',
    society: 'Society', women: "Women's History", art: 'Art & Culture', science: 'Science & Tech',
    foreign: 'Foreign Relations'
  };

  return { load, loadLinks, getPeriod, getAdjacent, allEvents, allPeople, THEME_LABELS, rootPath };
})();
