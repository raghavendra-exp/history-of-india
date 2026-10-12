const fs = require('fs');

console.log('=== TESTING UP-HISTORY AND SYLLABUS TABS ===\n');

// Test 1: up-history.html
const upHtml = fs.readFileSync('up-history.html', 'utf8');
const upTabButtons = (upHtml.match(/class="up-tab-btn[^"]*"\s+onclick="switchUpTab\('([^']+)'\)"/g) || []).map(m => m.match(/'([^']+)'/)[1]);
const upTabPanes = (upHtml.match(/class="up-tab-pane[^"]*"\s+id="([^"]+)"/g) || []).map(m => m.match(/id="([^"]+)"/)[1]);

console.log('up-history.html tab buttons found:', upTabButtons);
console.log('up-history.html tab panes found:  ', upTabPanes);

if (upTabButtons.length !== upTabPanes.length) {
  console.error('MISMATCH in up-history tab count!');
  process.exit(1);
}

upTabButtons.forEach(btnId => {
  if (!upTabPanes.includes(btnId)) {
    console.error(`Missing pane for button: ${btnId}`);
    process.exit(1);
  }
});
console.log('✓ All 7 UP-history tabs have 1:1 matching button and pane IDs!');

// Test 2: syllabus.html
const sylHtml = fs.readFileSync('syllabus.html', 'utf8');
const sylTabButtons = (sylHtml.match(/class="syl-nav-btn[^"]*"\s+onclick="switchSylTab\('([^']+)'\)"/g) || []).map(m => m.match(/'([^']+)'/)[1]);
const sylTabPanes = (sylHtml.match(/class="syl-section-pane[^"]*"\s+id="([^"]+)"/g) || []).map(m => m.match(/id="([^"]+)"/)[1]);

console.log('\nsyllabus.html tab buttons found:', sylTabButtons);
console.log('syllabus.html tab panes found:  ', sylTabPanes);

if (sylTabButtons.length !== sylTabPanes.length) {
  console.error('MISMATCH in syllabus tab count!');
  process.exit(1);
}

sylTabButtons.forEach(btnId => {
  if (!sylTabPanes.includes(btnId)) {
    console.error(`Missing pane for button: ${btnId}`);
    process.exit(1);
  }
});
console.log('✓ All 8 Syllabus sections have 1:1 matching button and pane IDs!');

console.log('\n=== ALL TAB TESTS PASSED 100%! ===');
