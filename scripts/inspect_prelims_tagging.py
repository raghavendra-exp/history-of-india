import json

with open('data/prelims-questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

for q in qs:
    tag = q.get('examTag')
    src = (q.get('source') or '').lower()
    cat = (q.get('category') or '').lower()
    q_text = (q.get('question') or '').lower()
    b_ref = (q.get('bookRef') or '').lower()
    
    if not tag or tag == 'NONE' or tag == 'unknown':
        if 'uppsc' in src or 'uppsc' in b_ref or cat == 'up-special' or cat == 'up-history':
            q['examTag'] = 'uppsc'
        elif 'ro' in src or 'aro' in src or cat == 'ro-hindi' or 'samiksha' in src:
            q['examTag'] = 'ro-aro'
        elif 'rrb' in src or 'railway' in src or 'ntpc' in src or 'lucent' in b_ref:
            q['examTag'] = 'rrb'
        elif 'bank' in src or 'ibps' in src or 'sbi' in src or 'rbi' in src or 'banking' in b_ref:
            q['examTag'] = 'bank'
        else:
            q['examTag'] = 'upsc'
    elif tag == 'roaro':
        q['examTag'] = 'ro-aro'

counts = {}
for q in qs:
    t = q.get('examTag')
    counts[t] = counts.get(t, 0) + 1

print("Updated examTag distribution:")
for k, v in sorted(counts.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
