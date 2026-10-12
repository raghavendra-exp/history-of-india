const fs = require('fs');

// Read app.js
const appJs = fs.readFileSync('js/app.js', 'utf-8');

// Mock browser window and document
let currentNavHtml = '';
global.localStorage = { getItem: () => null, setItem: () => {} };
global.window = { matchMedia: () => ({ matches: false }), innerWidth: 1200 };
global.location = { pathname: '/index.html' };
global.document = {
  documentElement: { setAttribute: () => {}, removeAttribute: () => {}, getAttribute: () => null },
  body: { classList: { add: () => {}, remove: () => {}, toggle: () => false, contains: () => false } },
  getElementById: (id) => {
    if (id === 'siteNav') return { set innerHTML(val) { currentNavHtml = val; }, get innerHTML() { return currentNavHtml; } };
    return { set innerHTML(v){}, get innerHTML(){return '';}, setAttribute: () => {}, appendChild: () => {}, querySelector: () => null, querySelectorAll: () => [] };
  },
  createElement: () => ({ setAttribute: () => {}, appendChild: () => {}, querySelector: () => null, querySelectorAll: () => [] }),
  querySelectorAll: () => [],
  addEventListener: () => {}
};

eval(appJs);

const pages = [
  'index.html', 'timeline.html', 'map.html', 'practice.html', 'art-culture.html',
  'society.html', 'books.html', 'up-history.html', 'themes.html', 'people.html',
  'women.html', 'graph.html', 'about.html', 'search.html', 'period.html'
];

for (const p of pages) {
  renderNav(p);
  console.log(`Page: ${p}`);
  console.log('Nav Inner Length:', currentNavHtml.length);
  // Check what links are inside currentNavHtml
  const links = (currentNavHtml.match(/href="[^"]*"/g) || []);
  console.log('Links in nav:', links);
}
