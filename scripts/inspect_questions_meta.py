import json

with open('data/prelims-questions.json', 'r', encoding='utf-8') as f:
    pq = json.load(f)

categories = {}
exams = {}
for q in pq:
    cat = q.get('category', 'unknown')
    ex = q.get('exam', 'unknown')
    categories[cat] = categories.get(cat, 0) + 1
    exams[ex] = exams.get(ex, 0) + 1

print("Prelims Questions Count by Category:")
for k, v in sorted(categories.items()):
    print(f"  {k}: {v}")

print("\nPrelims Questions Count by Exam:")
for k, v in sorted(exams.items()):
    print(f"  {k}: {v}")
