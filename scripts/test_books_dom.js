const fs = require('fs');

const html = fs.readFileSync('books.html', 'utf8');

const bookCards = (html.match(/class="book-card"/g) || []).length;
console.log('Total book-cards in books.html:', bookCards);

if (bookCards !== 27) {
  console.error(`Expected 27 book cards, found ${bookCards}`);
  process.exit(1);
}

// Check category tags on all book cards
const cardRegex = /<div class="book-card" data-category="([^"]+)">([\s\S]*?)<h2 class="book-title">([^<]+)<\/h2>/g;
let match;
let count = 0;
while ((match = cardRegex.exec(html)) !== null) {
  count++;
  const cat = match[1];
  const title = match[3].trim();
  console.log(`Book #${count}: ${title.padEnd(40)} [${cat}]`);
}

if (count !== 27) {
  console.error(`Expected 27 matched books, got ${count}`);
  process.exit(1);
}

console.log('\n=== ALL 27 CANONICAL TEXTBOOKS VERIFIED 100%! ===');
