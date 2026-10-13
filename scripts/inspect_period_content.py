import json

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for p in d.get('periods', []):
    if p['id'] in ['sources-and-historiography', 'prehistoric-age', 'indus-valley-civilization']:
        print(f"=== {p['id']} ===")
        print(f"Title: {p.get('title')}")
        print(f"Overview length: {len(p.get('overview', ''))} chars")
        print(f"Events: {len(p.get('events', []))}")
        print(f"Aspects: {list(p.get('aspects', {}).keys())}")
        for k, v in p.get('aspects', {}).items():
            print(f"  Aspect '{k}': {len(str(v))} chars")
        print(f"Prelims facts: {len(p.get('upscPrelims', []))}")
        print(f"Mains themes: {len(p.get('upscMains', []))}")
