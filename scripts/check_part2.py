import json
with open('data/prelims_part2.json', 'r', encoding='utf8') as f:
    data = json.load(f)
print(f"Total in part 2: {len(data)}")
print("First 3 IDs:", [d['id'] for d in data[:3]])
print("Last 3 IDs:", [d['id'] for d in data[-3:]])
