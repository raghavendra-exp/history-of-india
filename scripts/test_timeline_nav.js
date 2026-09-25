const fs = require('fs');
const vm = require('vm');

global.location = { pathname: '/timeline.html', search: '?era=ancient' };
global.localStorage = { getItem: () => null, setItem: () => {} };
global.window = { matchMedia: () => ({ matches: false }), location: global.location };

const elements = {};
const documentMock = {
  documentElement: { setAttribute: () => {}, removeAttribute: () => {}, getAttribute: () => null },
  body: { classList: { add: () => {}, toggle: () => false, contains: () => false }, appendChild: () => {} },
  getElementById: (id) => {
    if (!elements[id]) {
      elements[id] = { 
        innerHTML: '', 
        setAttribute: () => {}, 
        classList: { add: () => {}, remove: () => {} }, 
        addEventListener: () => {},
        querySelectorAll: () => [] 
      };
    }
    return elements[id];
  },
  querySelectorAll: (selector) => {
    return [
      {
        getAttribute: (attr) => (attr === 'data-id' ? 'ancient' : ''),
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
global.history = { replaceState: () => {} };

// Mock HistoryData
global.HistoryData = {
  load: async () => ({
    periods: [
      { id: 'prehistory', title: 'Prehistory', category: 'ancient', dateRange: '2.5M BCE - 2500 BCE', events: [] },
      { id: 'delhi-sultanate', title: 'Delhi Sultanate', category: 'sultanate', dateRange: '1206 - 1526 CE', events: [] }
    ]
  }),
  THEME_LABELS: {}
};

// Evaluate app.js and timeline.js in global context
vm.runInThisContext(fs.readFileSync('js/app.js', 'utf8'));
vm.runInThisContext(fs.readFileSync('js/timeline.js', 'utf8'));

(async () => {
  console.log('--- Testing Timeline Breadcrumb and Era Filtering ---');
  await renderTimelinePage();
  
  const headerBcContent = elements['headerBreadcrumb'] ? elements['headerBreadcrumb'].innerHTML : '';
  console.log('Timeline Header Breadcrumb Output:', headerBcContent);

  if (headerBcContent.includes('Ancient') && headerBcContent.includes('Master Timeline')) {
    console.log('SUCCESS: Timeline initialized with Ancient era breadcrumb correctly!');
  } else {
    console.error('FAILURE: Timeline breadcrumb was not set to Ancient.');
    process.exit(1);
  }

  // Test setEraFilter('world')
  setEraFilter('world');
  const worldBcContent = elements['headerBreadcrumb'] ? elements['headerBreadcrumb'].innerHTML : '';
  console.log('World Era Breadcrumb Output:', worldBcContent);

  if (worldBcContent.includes('World History')) {
    console.log('SUCCESS: Timeline updated to World History breadcrumb correctly!');
  } else {
    console.error('FAILURE: Timeline breadcrumb did not update for World History.');
    process.exit(1);
  }

  console.log('ALL TIMELINE NAV TESTS PASSED!');
})();
