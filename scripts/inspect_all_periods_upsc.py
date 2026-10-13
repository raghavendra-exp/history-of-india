import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for p in d['periods']:
    u = p.get('upsc', {})
    pr = u.get('prelims', [])
    m = u.get('mains', [])
    print(f"[{p['id']}] Prelims ({len(pr)}): {pr[:1]} ... Mains ({len(m)}): {m[:1]}")
