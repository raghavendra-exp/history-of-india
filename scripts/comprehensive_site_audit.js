const fs = require('fs');
const path = require('path');

const htmlFiles = fs.readdirSync('.').filter(f => f.endsWith('.html'));

console.log('=== COMPREHENSIVE SITE AUDIT ===\n');

let issues = [];

htmlFiles.forEach(file => {
  const content = fs.readFileSync(file, 'utf8');

  // 1. Viewport & charset
  if (!content.includes('viewport')) issues.push(`${file}: Missing viewport meta tag`);
  if (!content.includes('charset')) issues.push(`${file}: Missing charset meta tag`);

  // 2. CSS & JS links
  if (!content.includes('css/style.css')) issues.push(`${file}: Missing css/style.css link`);
  if (!content.includes('js/app.js')) issues.push(`${file}: Missing js/app.js script tag`);
  if (!content.includes('js/data.js')) issues.push(`${file}: Missing js/data.js script tag`);

  // 3. Navigation container & Footer container
  if (!content.includes('id="siteNav"') && !content.includes("id='siteNav'")) {
    issues.push(`${file}: Missing #siteNav container`);
  }
  if (!content.includes('id="siteFooter"') && !content.includes("id='siteFooter'")) {
    issues.push(`${file}: Missing #siteFooter container`);
  }

  // 4. Breadcrumb container
  if (!content.includes('id="breadcrumb"') && !content.includes("id='breadcrumb'")) {
    issues.push(`${file}: Missing #breadcrumb container`);
  }

  // 5. Internal href checks
  const hrefRegex = /href=["']([^"']+)["']/gi;
  let match;
  while ((match = hrefRegex.exec(content)) !== null) {
    const href = match[1];
    if (href.includes('${') || href.startsWith('http://') || href.startsWith('https://') || href.startsWith('#') || href.startsWith('javascript:') || href.startsWith('mailto:')) {
      continue;
    }
    const cleanHref = href.split('?')[0].split('#')[0];
    if (cleanHref && !fs.existsSync(cleanHref)) {
      issues.push(`${file}: Broken internal link -> ${cleanHref} (full: ${href})`);
    }
  }

  // 6. Image src checks
  const imgRegex = /src=["']([^"']+)["']/gi;
  while ((match = imgRegex.exec(content)) !== null) {
    const src = match[1];
    if (src.includes('${') || src.startsWith('http://') || src.startsWith('https://') || src.startsWith('data:')) {
      continue;
    }
    const cleanSrc = src.split('?')[0].split('#')[0];
    if (cleanSrc && !fs.existsSync(cleanSrc)) {
      issues.push(`${file}: Broken image/script asset -> ${cleanSrc}`);
    }
  }
});

console.log('Total issues found:', issues.length);
if (issues.length > 0) {
  issues.forEach(i => console.log(' - ' + i));
} else {
  console.log('ALL HTML FILES PASSED STRUCTURAL, ASSET & INTERNAL LINK INTEGRITY CHECKS!');
}
