// Simulate DOM environment and test society.html interactions
const fs = require('fs');

const html = fs.readFileSync('society.html', 'utf-8');

const elements = {
  societyCardsSection: { style: {} },
  societyMainsSection: { style: {}, scrollIntoView: () => {} },
  societySearchInput: { value: '' },
  societyGrid: { innerHTML: '' },
  societyNavPills: {
    buttons: [
      { textContent: 'All Society Dimensions (11)', getAttribute: () => 'all', classList: { add: () => {}, remove: () => {} } },
      { textContent: 'Salient Features & Diversity', getAttribute: () => 'diversity', classList: { add: () => {}, remove: () => {} } },
      { textContent: 'Role of Women', getAttribute: () => 'women', classList: { add: () => {}, remove: () => {} } },
      { textContent: 'Population & Demographics', getAttribute: () => 'demography', classList: { add: () => {}, remove: () => {} } },
      { textContent: 'Poverty & Development', getAttribute: () => 'poverty', classList: { add: () => {}, remove: () => {} } },
      { textContent: 'Urbanization & Slums', getAttribute: () => 'urbanization', classList: { add: () => {}, remove: () => {} } },
      { textContent: 'Effects of Globalization', getAttribute: () => 'globalization', classList: { add: () => {}, remove: () => {} } },
      { textContent: 'Social Empowerment', getAttribute: () => 'empowerment', classList: { add: () => {}, remove: () => {} } },
      { textContent: 'Communalism', getAttribute: () => 'communalism', classList: { add: () => {}, remove: () => {} } },
      { textContent: 'Regionalism', getAttribute: () => 'regionalism', classList: { add: () => {}, remove: () => {} } },
      { textContent: 'Secularism vs UCC', getAttribute: () => 'secularism', classList: { add: () => {}, remove: () => {} } },
      { textContent: 'Mains Model Frameworks', getAttribute: () => 'mains-models', classList: { add: () => {}, remove: () => {} } }
    ]
  }
};

global.document = {
  addEventListener: () => {},
  getElementById: (id) => elements[id] || null,
  querySelectorAll: (selector) => {
    if (selector.includes('societyNavPills')) return elements.societyNavPills.buttons;
    return [];
  },
  querySelector: (selector) => {
    if (selector.includes('societyNavPills')) {
      for (const btn of elements.societyNavPills.buttons) {
        if (selector.includes(btn.getAttribute())) return btn;
      }
      return elements.societyNavPills.buttons[0];
    }
    return null;
  }
};

const scriptMatch = html.match(/<script>\s*(\/\/ Master Data Store[\s\S]*?)<\/script>/);
if (!scriptMatch) {
  console.error("FAIL: Could not extract society script");
  process.exit(1);
}

const modifiedScript = scriptMatch[1]
  .replace('const SOCIETY_DATA =', 'global.SOCIETY_DATA =')
  .replace('function switchSocietyTab', 'global.switchSocietyTab = function')
  .replace('function renderSocietyCards', 'global.renderSocietyCards = function')
  .replace('function handleSocietySearch', 'global.handleSocietySearch = function');

eval(modifiedScript);

console.log("=== RUNNING SOCIETY INTERACTION TESTS ===");
console.log("Total SOCIETY_DATA items loaded:", SOCIETY_DATA.length);
if (SOCIETY_DATA.length !== 11) {
  console.error("FAIL: Expected 11 items, got", SOCIETY_DATA.length);
  process.exit(1);
}

// Test 1: Render All
renderSocietyCards('all', '');
const allMatches = (elements.societyGrid.innerHTML.match(/<article class="society-card"/g) || []).length;
console.log("Test 1 (render 'all'):", allMatches, "cards rendered (expected 11)");
if (allMatches !== 11) process.exit(1);

// Test 2: Filter Diversity
renderSocietyCards('diversity', '');
const divMatches = (elements.societyGrid.innerHTML.match(/<article class="society-card"/g) || []).length;
console.log("Test 2 (render 'diversity'):", divMatches, "cards rendered (expected 2)");
if (divMatches !== 2) process.exit(1);

// Test 3: Filter Women
renderSocietyCards('women', '');
const womenMatches = (elements.societyGrid.innerHTML.match(/<article class="society-card"/g) || []).length;
console.log("Test 3 (render 'women'):", womenMatches, "cards rendered (expected 1)");
if (womenMatches !== 1) process.exit(1);

// Test 4: Search Query "urbanization"
renderSocietyCards('all', 'urbanization');
const urbanMatches = (elements.societyGrid.innerHTML.match(/<article class="society-card"/g) || []).length;
console.log("Test 4 (search 'urbanization'):", urbanMatches, "cards found");
if (urbanMatches === 0) process.exit(1);

// Test 5: Switch Tab to mains-models
switchSocietyTab('mains-models');
console.log("Test 5 (switch to 'mains-models'): Section visibility:", elements.societyMainsSection.style.display);
if (elements.societyMainsSection.style.display !== 'block') process.exit(1);

// Test 6: Switch back to all
switchSocietyTab('all');
console.log("Test 6 (switch to 'all'): Section visibility:", elements.societyCardsSection.style.display);
if (elements.societyCardsSection.style.display !== 'block') process.exit(1);

console.log("=== ALL SOCIETY TESTS PASSED 100%! ===");
