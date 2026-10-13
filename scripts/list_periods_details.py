import json

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

periods = d.get('periods', [])
print(f"Total periods: {len(periods)}")
for i, p in enumerate(periods):
    title = p.get('title', '')
    pid = p.get('id', '')
    cat = p.get('category', '')
    events_count = len(p.get('events', []))
    aspects = list(p.get('aspects', {}).keys())
    print(f"{i+1:2d}. [{pid}] {title} ({cat}) - events: {events_count}, aspects: {aspects}")
