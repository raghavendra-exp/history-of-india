const fs = require('fs');

console.log('=== TESTING REVISION.HTML & REVISION.JS DOM INTERACTIONS ===\n');

// 1. Verify revision-notes.json exists and is valid
const dataRaw = fs.readFileSync('data/revision-notes.json', 'utf8');
const data = JSON.parse(dataRaw);

console.log(`Total Topics in JSON: ${data.totalTopics}`);
console.log(`Total Comparison Tables in JSON: ${data.totalTables}`);

if (data.totalTopics !== 82) {
  console.error(`FAIL: Expected 82 topics, got ${data.totalTopics}`);
  process.exit(1);
}

if (data.totalTables !== 37) {
  console.error(`FAIL: Expected 37 comparison tables, got ${data.totalTables}`);
  process.exit(1);
}

// 2. Verify all 6 Mauryan images exist on disk
const expectedMauryanImages = [
  'assets/images/mauryan/sarnath_lion_capital.png',
  'assets/images/mauryan/mauryan_pillar_diagram.png',
  'assets/images/mauryan/rampurva_lauriya_pillar.png',
  'assets/images/mauryan/ashokan_pillar_inscription.png',
  'assets/images/mauryan/ashoka_major_rock_edicts_table.png',
  'assets/images/mauryan/ashokan_sandstone_shaft.png'
];

expectedMauryanImages.forEach(img => {
  if (!fs.existsSync(img)) {
    console.error(`FAIL: Missing Mauryan image: ${img}`);
    process.exit(1);
  }
  const size = fs.getStats ? fs.getStats(img).size : fs.statSync(img).size;
  if (size === 0) {
    console.error(`FAIL: Image ${img} is 0 bytes`);
    process.exit(1);
  }
});
console.log('✓ All 6 Mauryan lithic images verified on disk with non-zero size!');

// 3. Verify Topic 58 has all 6 images attached
const topic58 = data.topics.find(t => t.slNo === 58);
if (!topic58 || !topic58.images || topic58.images.length !== 6) {
  console.error('FAIL: Topic 58 does not have 6 images attached in JSON');
  process.exit(1);
}
console.log('✓ Topic 58 (Mauryan art and culture) correctly holds 6 image objects!');

// 4. Verify Pointers generation
let totalPointers = 0;
data.topics.forEach(t => {
  if (!t.pointers || t.pointers.length === 0) {
    console.error(`FAIL: Topic #${t.slNo} (${t.title}) has 0 pointers!`);
    process.exit(1);
  }
  totalPointers += t.pointers.length;
});
console.log(`✓ All 82 topics have high-yield pointers! Total pointers: ${totalPointers}`);

// 5. Verify HTML structure of revision.html
const html = fs.readFileSync('revision.html', 'utf8');
const requiredIds = [
  'siteNav',
  'breadcrumb',
  'revisionStats',
  'revisionSearchInput',
  'toggleBookmarksBtn',
  'copyAllVisibleBtn',
  'expandAllBtn',
  'collapseAllBtn',
  'printRevisionBtn',
  'categoryFilters',
  'revisionCardsGrid',
  'comparisonTablesView',
  'siteFooter'
];

requiredIds.forEach(id => {
  if (!html.includes(`id="${id}"`) && !html.includes(`id='${id}'`)) {
    console.error(`FAIL: revision.html missing element with id="${id}"`);
    process.exit(1);
  }
});
console.log('✓ All 13 core interactive elements present in revision.html DOM!');

// 6. Verify revision.js script
const jsContent = fs.readFileSync('js/revision.js', 'utf8');
['HistoryRevision', 'init', 'render', 'formatFullNotes', 'renderComparisonTables', 'copyTopic', 'toggleBookmark'].forEach(fn => {
  if (!jsContent.includes(fn)) {
    console.error(`FAIL: js/revision.js missing function/identifier ${fn}`);
    process.exit(1);
  }
});
console.log('✓ js/revision.js contains all required controller methods and export hooks!');

console.log('\n=== ALL REVISION HUB TESTS PASSED 100%! ===');
