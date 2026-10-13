import json

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

periods = d.get('periods', [])
print(f"Total periods: {len(periods)}")

for i in range(20):
    p = periods[i]
    print(f"{i+1:2d}. {p['id'].ljust(45)} | cat: {p.get('category','').ljust(12)} | title: {p.get('title')}")
