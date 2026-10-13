import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

periods = d['periods']
print(f"Total periods: {len(periods)}")

stats = {
    'aspects': sum(1 for p in periods if p.get('aspects')),
    'events': sum(1 for p in periods if p.get('events')),
    'phases': sum(1 for p in periods if p.get('phases')),
    'people': sum(1 for p in periods if p.get('people')),
    'women': sum(1 for p in periods if p.get('women')),
    'quickFacts': sum(1 for p in periods if p.get('quickFacts')),
    'upsc_prelims': sum(len(p.get('upsc', {}).get('prelims', [])) for p in periods),
    'upsc_mains': sum(len(p.get('upsc', {}).get('mains', [])) for p in periods),
}
print("Field presence statistics:", stats)
