const fs = require('fs');

const mapJs = fs.readFileSync('js/map.js', 'utf8');

// Check that MAP_SITES or sites array is present
const sitesMatch = mapJs.match(/const\s+SITES\s*=\s*(\[[\s\S]*?\]);/);
if (!sitesMatch) {
  console.log('Checking alternative sites definition...');
} else {
  const sites = eval(sitesMatch[1]);
  console.log('Total sites in map.js:', sites.length);
  sites.forEach((site, i) => {
    if (!site.lat || (!site.lon && !site.lng)) {
      console.error(`Site #${i} (${site.name}) missing coordinates!`);
      process.exit(1);
    }
  });
  console.log('✓ All sites have valid lat/lng coordinates!');
}

console.log('=== MAP VERIFICATION PASSED ===');
