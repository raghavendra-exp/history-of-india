import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

thin_periods = []
for p in d['periods']:
    u = p.get('upsc', {})
    pr = u.get('prelims', [])
    m = u.get('mains', [])
    if len(pr) < 5 or len(m) < 3:
        thin_periods.append((p['id'], len(pr), len(m), p.get('category')))

print(f"Total periods needing prelims/mains enrichment to reach 5+ Prelims and 3+ Mains: {len(thin_periods)} of {len(d['periods'])}")
for p in thin_periods[:15]:
    print(f"  {p[0]} (cat: {p[3]}): {p[1]} prelims, {p[2]} mains")
