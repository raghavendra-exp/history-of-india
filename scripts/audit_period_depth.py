import json

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

periods = d.get('periods', [])
print(f"Total periods: {len(periods)}")

empty_prelims = 0
empty_mains = 0
short_aspects = 0

for p in periods:
    pf = len(p.get('upscPrelims', []))
    mf = len(p.get('upscMains', []))
    if pf == 0: empty_prelims += 1
    if mf == 0: empty_mains += 1
    total_aspect_chars = sum(len(str(v)) for v in p.get('aspects', {}).values())
    if total_aspect_chars < 500:
        short_aspects += 1
        print(f"Short aspects: {p['id']} ({total_aspect_chars} chars)")

print(f"\nPeriods with 0 upscPrelims: {empty_prelims}/{len(periods)}")
print(f"Periods with 0 upscMains: {empty_mains}/{len(periods)}")
print(f"Periods with <500 chars aspects: {short_aspects}/{len(periods)}")
