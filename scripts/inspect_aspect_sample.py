import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for p in d['periods'][:10]:
    asp = p.get('aspects', {})
    print(f"[{p['id']}] Aspects: {list(asp.keys())}")
    for k, v in asp.items():
        if isinstance(v, list):
            print(f"   - {k}: {len(v)} points")
        elif isinstance(v, dict):
            pts = v.get('points', [])
            print(f"   - {k} (dict): {len(pts)} points")
