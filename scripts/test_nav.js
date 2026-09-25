const fs = require('fs');
const vm = require('vm');

global.location = { pathname: '/art-culture.html', search: '' };
global.localStorage = { getItem: () => null, setItem: () => {} };
global.window = { matchMedia: () => ({ matches: false }) };

const elements = {};
const documentMock = {
  documentElement: { setAttribute: () => {}, removeAttribute: () => {}, getAttribute: () => null },
  body: { classList: { add: () => {}, toggle: () => false, contains: () => false }, appendChild: () => {} },
  getElementById: (id) => {
    if (!elements[id]) {
      elements[id] = { innerHTML: '', setAttribute: () => {}, classList: { add: () => {}, remove: () => {} } };
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
  createElement: () => ({ setAttribute: () => {}, classList: { add: () => {} }, appendChild: () => {} }),
  addEventListener: () => {}
};
global.document = documentMock;
global.URLSearchParams = URLSearchParams;

// Evaluate app.js in global context
const code = fs.readFileSync('js/app.js', 'utf8');
vm.runInThisContext(code);

console.log('--- Testing Breadcrumb Nav and Subject Tabs ---');
renderNav('art-culture.html');
const siteNavContent = elements['siteNav'] ? elements['siteNav'].innerHTML : '';

if (siteNavContent.includes('header-breadcrumb') && siteNavContent.includes('nav-breadcrumb-bar') && siteNavContent.includes('bc-subject-tab')) {
  console.log('SUCCESS: siteNav contains header-breadcrumb and bc-subject-tab!');
} else {
  console.error('FAILURE: siteNav does not contain expected breadcrumb elements.');
  process.exit(1);
}

renderBreadcrumb([
  { label: 'Home', href: 'index.html' },
  { label: 'Art and Culture', href: 'art-culture.html' },
  { label: 'Temple Architecture' }
]);

const headerBcContent = elements['headerBreadcrumb'] ? elements['headerBreadcrumb'].innerHTML : '';
console.log('Header Breadcrumb Output:', headerBcContent);

if (headerBcContent.includes('Art and Culture') && headerBcContent.includes('Temple Architecture')) {
  console.log('SUCCESS: headerBreadcrumb updated correctly!');
} else {
  console.error('FAILURE: headerBreadcrumb was not updated.');
  process.exit(1);
}

console.log('ALL NAV TESTS PASSED PERFECTLY!');
