import json

with open('data/history.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total periods: {len(data['periods'])}")
national = [p for p in data['periods'] if not p.get('region')]
up = [p for p in data['periods'] if p.get('region') == 'up']
print(f"National periods: {len(national)}")
print(f"UP periods: {len(up)}")

print("\n--- National Periods List ---")
for i, p in enumerate(national):
    print(f"{i+1:2d}. {p['id']:35s} | {p['category']:12s} | {p['title']}")

print("\n--- UP Periods List ---")
for i, p in enumerate(up):
    print(f"{i+1:2d}. {p['id']:35s} | {p['category']:12s} | {p['title']}")
