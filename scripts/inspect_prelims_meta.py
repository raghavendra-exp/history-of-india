import json
from collections import Counter

with open('data/prelims-questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

print(f"Total prelims questions: {len(qs)}")
sample = qs[0]
print("Keys in question object:", list(sample.keys()))

exam_tags = Counter(q.get('examTag', 'NONE') for q in qs)
print("examTag counts:", exam_tags)

exam_refs = Counter(q.get('exam', 'NONE') for q in qs)
print("exam field counts:", exam_refs)

category_counts = Counter(q.get('category', 'NONE') for q in qs)
print("Top 10 categories:", category_counts.most_common(10))

# Check how many have specific exam keywords in yearRef or tags
rrb_count = sum(1 for q in qs if 'rrb' in str(q).lower() or 'railway' in str(q).lower())
ro_count = sum(1 for q in qs if 'ro' in str(q).lower() or 'aro' in str(q).lower())
bank_count = sum(1 for q in qs if 'bank' in str(q).lower() or 'ibps' in str(q).lower() or 'sbi' in str(q).lower())
uppsc_count = sum(1 for q in qs if 'uppsc' in str(q).lower() or 'pcs' in str(q).lower())
upsc_count = sum(1 for q in qs if 'upsc' in str(q).lower() or 'ias' in str(q).lower() or 'cse' in str(q).lower())

print(f"Text matches -> UPSC: {upsc_count}, UPPSC: {uppsc_count}, RO/ARO: {ro_count}, RRB: {rrb_count}, Bank: {bank_count}")
