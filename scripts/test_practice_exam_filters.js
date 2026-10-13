const fs = require('fs');

const qs = JSON.parse(fs.readFileSync('data/prelims-questions.json', 'utf8'));
console.log(`Total Prelims questions loaded: ${qs.length}`);

function matchesExam(item, selectedExam) {
  if (selectedExam === 'all') return true;
  const tag = (item.examTag || '').toLowerCase();
  const yr = ((item.yearRef || '') + ' ' + (item.source || '') + ' ' + (item.year || '')).toLowerCase();
  
  switch (selectedExam) {
    case 'upsc':
      return tag === 'upsc' || yr.includes('upsc') || yr.includes('cse') || (!tag && !yr.includes('uppsc') && !yr.includes('ro/aro') && !yr.includes('bank') && !yr.includes('rrb'));
    case 'uppsc':
      return tag === 'uppsc' || yr.includes('uppsc') || yr.includes('pcs');
    case 'ro-aro':
      return tag === 'ro-aro' || tag === 'roaro' || yr.includes('ro/aro') || yr.includes('ro-aro') || yr.includes('samiksha');
    case 'bank':
      return tag === 'bank' || yr.includes('bank') || yr.includes('ibps') || yr.includes('sbi') || yr.includes('rbi');
    case 'rrb':
      return tag === 'rrb' || yr.includes('rrb') || yr.includes('railway') || yr.includes('ntpc');
    default:
      return true;
  }
}

const exams = ['all', 'upsc', 'uppsc', 'ro-aro', 'bank', 'rrb'];
exams.forEach(ex => {
  const matched = qs.filter(q => matchesExam(q, ex));
  console.log(`Exam filter "${ex}": ${matched.length} questions matched`);
});
