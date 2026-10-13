import json

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Total periods in history.json: {len(d['periods'])}")
thin_prelims = []
thin_mains = []
for p in d['periods']:
    u = p.get('upsc', {})
    pr = u.get('prelims', [])
    m = u.get('mains', [])
    if len(pr) < 3:
        thin_prelims.append((p['id'], len(pr)))
    if len(m) < 2:
        thin_mains.append((p['id'], len(m)))

print(f"Periods with < 3 prelims facts: {len(thin_prelims)}")
if thin_prelims:
    print("  ", thin_prelims[:10])
print(f"Periods with < 2 mains themes: {len(thin_mains)}")
if thin_mains:
    print("  ", thin_mains[:10])

# Check average lengths
avg_pr = sum(len(p.get('upsc', {}).get('prelims', [])) for p in d['periods']) / len(d['periods'])
avg_m = sum(len(p.get('upsc', {}).get('mains', [])) for p in d['periods']) / len(d['periods'])
print(f"Average prelims items per period: {avg_pr:.2f}")
print(f"Average mains items per period: {avg_m:.2f}")
