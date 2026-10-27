// Simulate DOM environment and test art-culture.html interactions
const fs = require('fs');

const html = fs.readFileSync('art-culture.html', 'utf-8');

// Simple DOM Mock
const elements = {
  cultureCardsSection: { style: {} },
  cultureComparisonsSection: { style: {}, scrollIntoView: () => {} },
  cultureMainsSection: { style: {}, scrollIntoView: () => {} },
  cultureSearchInput: { value: '' },
  cultureGrid: { innerHTML: '' },
  cultureNavPills: {
    buttons: [
      { textContent: 'All Culture Topics (47)', getAttribute: () => 'all', classList: { add: () => {}, remove: () => {} } },
      { textContent: '🎨 Art Forms & Textiles (24)', getAttribute: () => 'art-forms', classList: { add: () => {}, remove: () => {} } },
      { textContent: '📜 Literature & Scripts (10)', getAttribute: () => 'literature', classList: { add: () => {}, remove: () => {} } },
      { textContent: '🏛️ Architecture (13)', getAttribute: () => 'architecture', classList: { add: () => {}, remove: () => {} } },
      { textContent: '⚖️ Core Comparative Tables', getAttribute: () => 'comparisons', classList: { add: () => {}, remove: () => {} } },
      { textContent: '✍️ Mains Model Answers', getAttribute: () => 'mains-frameworks', classList: { add: () => {}, remove: () => {} } }
    ]
  }
};

global.document = {
  addEventListener: () => {},
  getElementById: (id) => elements[id] || null,
  querySelectorAll: (selector) => {
    if (selector.includes('cultureNavPills')) return elements.cultureNavPills.buttons;
    return [];
  },
  querySelector: (selector) => {
    if (selector.includes('cultureNavPills')) {
      for (const btn of elements.cultureNavPills.buttons) {
        if (selector.includes(btn.getAttribute())) return btn;
      }
      return elements.cultureNavPills.buttons[0];
    }
    return null;
  }
};

// Extract and evaluate the script
const scriptMatch = html.match(/<script>\s*(\/\/ Master Data Store[\s\S]*?)<\/script>/);
if (!scriptMatch) {
  console.error("FAIL: Could not extract script");
  process.exit(1);
}

const modifiedScript = scriptMatch[1]
  .replace('const CULTURE_DATA =', 'global.CULTURE_DATA =')
  .replace('function switchCultureTab', 'global.switchCultureTab = function')
  .replace('function renderCultureCards', 'global.renderCultureCards = function')
  .replace('function handleCultureSearch', 'global.handleCultureSearch = function');

eval(modifiedScript);

console.log("=== RUNNING CULTURE INTERACTION TESTS ===");
console.log("Total CULTURE_DATA items loaded:", CULTURE_DATA.length);
if (CULTURE_DATA.length !== 47) {
  console.error("FAIL: Expected 47 items, got", CULTURE_DATA.length);
  process.exit(1);
}

// Test 1: Render All
renderCultureCards('all', '');
const allMatches = (elements.cultureGrid.innerHTML.match(/<article class="culture-card"/g) || []).length;
console.log("Test 1 (render 'all'):", allMatches, "cards rendered (expected 47)");
if (allMatches !== 47) process.exit(1);

// Test 2: Filter Art Forms
renderCultureCards('art-forms', '');
const artMatches = (elements.cultureGrid.innerHTML.match(/<article class="culture-card"/g) || []).length;
console.log("Test 2 (render 'art-forms'):", artMatches, "cards rendered (expected 24)");
if (artMatches !== 24) process.exit(1);

// Test 3: Filter Literature
renderCultureCards('literature', '');
const litMatches = (elements.cultureGrid.innerHTML.match(/<article class="culture-card"/g) || []).length;
console.log("Test 3 (render 'literature'):", litMatches, "cards rendered (expected 10)");
if (litMatches !== 10) process.exit(1);

// Test 4: Filter Architecture
renderCultureCards('architecture', '');
const archMatches = (elements.cultureGrid.innerHTML.match(/<article class="culture-card"/g) || []).length;
console.log("Test 4 (render 'architecture'):", archMatches, "cards rendered (expected 13)");
if (archMatches !== 13) process.exit(1);

// Test 5: Search Query "ajanta"
renderCultureCards('all', 'ajanta');
const ajantaMatches = (elements.cultureGrid.innerHTML.match(/<article class="culture-card"/g) || []).length;
console.log("Test 5 (search 'ajanta'):", ajantaMatches, "cards found");
if (ajantaMatches === 0) process.exit(1);

// Test 6: switchCultureTab invocation
switchCultureTab('comparisons');
console.log("Test 6 (switch to 'comparisons'): Section visibility:", elements.cultureComparisonsSection.style.display);
if (elements.cultureComparisonsSection.style.display !== 'block') process.exit(1);

switchCultureTab('mains-frameworks');
console.log("Test 7 (switch to 'mains-frameworks'): Section visibility:", elements.cultureMainsSection.style.display);
if (elements.cultureMainsSection.style.display !== 'block') process.exit(1);

switchCultureTab('all');
console.log("Test 8 (switch to 'all'): Section visibility:", elements.cultureCardsSection.style.display);
if (elements.cultureCardsSection.style.display !== 'block') process.exit(1);

console.log("=== ALL CULTURE TESTS PASSED 100%! ===");
