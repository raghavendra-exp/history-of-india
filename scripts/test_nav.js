const fs = require('fs');
const vm = require('vm');

global.location = { pathname: '/art-culture.html', search: '' };
global.localStorage = { 
  store: {},
  getItem: (k) => global.localStorage.store[k] || null, 
  setItem: (k, v) => { global.localStorage.store[k] = v; } 
};
global.window = { matchMedia: () => ({ matches: false }), innerWidth: 1200 };

const elements = {};
const bodyClasses = new Set();

const documentMock = {
  documentElement: { setAttribute: () => {}, removeAttribute: () => {}, getAttribute: () => null },
  body: { 
    classList: { 
      add: (c) => bodyClasses.add(c), 
      remove: (c) => bodyClasses.delete(c), 
      toggle: (c) => { 
        if (bodyClasses.has(c)) { bodyClasses.delete(c); return false; }
        else { bodyClasses.add(c); return true; }
      }, 
      contains: (c) => bodyClasses.has(c) 
    }, 
    appendChild: (el) => {
      if (el.id) elements[el.id] = el;
    } 
  },
  getElementById: (id) => {
    if (!elements[id]) {
      elements[id] = { innerHTML: '', setAttribute: () => {}, classList: { add: () => {}, remove: () => {} }, querySelectorAll: () => [] };
    }
    return elements[id];
  },
  querySelectorAll: (selector) => {
    return [
      {
        getAttribute: (attr) => (attr === 'data-id' ? 'art-culture' : ''),
        classList: { add: () => {}, remove: () => {} },
        setAttribute: () => {},
        scrollIntoView: () => {}
      }
    ];
  },
  createElement: (tag) => ({ id: '', className: '', innerHTML: '', setAttribute: () => {}, classList: { add: () => {} } }),
  addEventListener: () => {}
};
global.document = documentMock;
global.URLSearchParams = URLSearchParams;

// Evaluate app.js in global context
const code = fs.readFileSync('js/app.js', 'utf8');
vm.runInThisContext(code);

console.log('--- Testing Vertical Left Sidebar & Breadcrumbs ---');
renderNav('art-culture.html');
const siteNavContent = elements['siteNav'] ? elements['siteNav'].innerHTML : '';
const siteSidebarContent = elements['siteSidebar'] ? elements['siteSidebar'].innerHTML : '';

if (siteNavContent.includes('header-breadcrumb') && siteNavContent.includes('sidebarToggle')) {
  console.log('SUCCESS: siteNav contains header-breadcrumb and sidebar toggle!');
} else {
  console.error('FAILURE: siteNav does not contain expected header elements.');
  process.exit(1);
}

if (siteSidebarContent.includes('verticalBreadcrumb') && siteSidebarContent.includes('sb-nav-item') && siteSidebarContent.includes('Flagship Modules')) {
  console.log('SUCCESS: siteSidebar contains verticalBreadcrumb and categorized sb-nav-items!');
} else {
  console.error('FAILURE: siteSidebar does not contain expected sidebar elements.');
  process.exit(1);
}

renderBreadcrumb([
  { label: 'Home', href: 'index.html' },
  { label: 'Art and Culture', href: 'art-culture.html' },
  { label: 'Temple Architecture' }
]);

const headerBcContent = elements['headerBreadcrumb'] ? elements['headerBreadcrumb'].innerHTML : '';
const verticalBcContent = elements['verticalBreadcrumb'] ? elements['verticalBreadcrumb'].innerHTML : '';

console.log('Header Breadcrumb Output:', headerBcContent);
console.log('Vertical Breadcrumb Output:', verticalBcContent);

if (headerBcContent.includes('Art and Culture') && headerBcContent.includes('Temple Architecture')) {
  console.log('SUCCESS: headerBreadcrumb updated correctly!');
} else {
  console.error('FAILURE: headerBreadcrumb was not updated.');
  process.exit(1);
}

if (verticalBcContent.includes('vbc-rail') && verticalBcContent.includes('vbc-bullet') && verticalBcContent.includes('Temple Architecture')) {
  console.log('SUCCESS: verticalBreadcrumb tree updated correctly with rails & bullets!');
} else {
  console.error('FAILURE: verticalBreadcrumb tree was not updated correctly.');
  process.exit(1);
}

// Test Toggle Sidebar
console.log('Initial collapsed state:', bodyClasses.has('sidebar-collapsed'));
toggleSidebar(false); // collapse
if (bodyClasses.has('sidebar-collapsed')) {
  console.log('SUCCESS: toggleSidebar collapsed correctly!');
} else {
  console.error('FAILURE: toggleSidebar did not collapse sidebar.');
  process.exit(1);
}

toggleSidebar(true); // open
if (!bodyClasses.has('sidebar-collapsed')) {
  console.log('SUCCESS: toggleSidebar opened correctly!');
} else {
  console.error('FAILURE: toggleSidebar did not open sidebar.');
  process.exit(1);
}

console.log('ALL VERTICAL SIDEBAR TESTS PASSED PERFECTLY!');
