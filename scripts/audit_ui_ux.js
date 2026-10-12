const fs = require('fs');
const path = require('path');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

console.log('=== UI / UX AUDIT ACROSS ALL HTML PAGES ===\n');

files.forEach(f => {
  const content = fs.readFileSync(f, 'utf8');
  const hasViewport = content.includes('viewport');
  const titleMatch = content.match(/<title>([^<]*)<\/title>/i);
  const title = titleMatch ? titleMatch[1].trim() : 'MISSING';
  
  // Check CSS stylesheets included
  const hasStyleCss = content.includes('css/style.css');
  const hasCommonJs = content.includes('js/common.js');
  
  // Check images
  const imgRegex = /<img\s+([^>]+)>/gi;
  let imgMatch;
  let imgCount = 0;
  let imgsWithoutAlt = 0;
  let imgsWithoutOnerror = 0;
  while ((imgMatch = imgRegex.exec(content)) !== null) {
    imgCount++;
    const attrs = imgMatch[1];
    if (!attrs.includes('alt=')) imgsWithoutAlt++;
    if (!attrs.includes('onerror=')) imgsWithoutOnerror++;
  }

  // Check buttons without aria-label or accessible text
  const btnRegex = /<button\s+([^>]+)>([\s\S]*?)<\/button>/gi;
  let btnMatch;
  let btnCount = 0;
  let emptyBtns = 0;
  while ((btnMatch = btnRegex.exec(content)) !== null) {
    btnCount++;
    const attrs = btnMatch[1];
    const inner = btnMatch[2].trim();
    if (!inner && !attrs.includes('aria-label')) emptyBtns++;
  }

  console.log(`${f.padEnd(18)} | Title: ${title.padEnd(45).substring(0, 45)} | CSS: ${hasStyleCss ? '✓' : '✗'} | JS: ${hasCommonJs ? '✓' : '✗'} | Imgs: ${imgCount} (no alt: ${imgsWithoutAlt}) | Btns: ${btnCount}`);
});
