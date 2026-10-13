import json

with open('data/prelims-questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

none_qs = [q for q in qs if not q.get('examTag')]
print(f"Total untagged: {len(none_qs)}")

sources = {}
for q in none_qs:
    s = q.get('source', 'unknown')
    sources[s] = sources.get(s, 0) + 1

for s, count in sorted(sources.items(), key=lambda x: -x[1])[:15]:
    print(f"  {s}: {count}")

categories = {}
for q in none_qs:
    c = q.get('category', 'unknown')
    categories[c] = categories.get(c, 0) + 1
print("Categories in untagged:")
for c, count in sorted(categories.items(), key=lambda x: -x[1]):
    print(f"  {c}: {count}")
