const fs = require('fs');

const data = JSON.parse(fs.readFileSync('data/history.json', 'utf8'));

console.log('=== HISTORY DATA INTEGRITY AUDIT ===\n');
console.log('Total periods:', data.periods.length);

let errors = [];

data.periods.forEach((p, idx) => {
  if (!p.id) errors.push(`Period #${idx} missing id`);
  if (!p.title) errors.push(`Period #${idx} missing title`);
  if (!p.dateRange) errors.push(`Period #${idx} (${p.id}) missing dateRange`);
  if (!p.overview) errors.push(`Period #${idx} (${p.id}) missing overview`);
  if (!p.category) errors.push(`Period #${idx} (${p.id}) missing category`);
  if (!Array.isArray(p.events)) errors.push(`Period #${idx} (${p.id}) events is not an array`);
  if (!Array.isArray(p.people)) errors.push(`Period #${idx} (${p.id}) people is not an array`);
  if (!p.aspects || typeof p.aspects !== 'object') errors.push(`Period #${idx} (${p.id}) aspects missing`);
});

console.log('Total issues found:', errors.length);
if (errors.length > 0) {
  errors.forEach(e => console.log(' - ' + e));
  process.exit(1);
} else {
  console.log('✓ ALL PERIODS VALIDATED 100%!');
}
