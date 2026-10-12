# -*- coding: utf-8 -*-
import json
import os

with open('syllabus.html', 'r', encoding='utf-8') as f:
    syl = f.read()

print("Syllabus HTML length:", len(syl))

sections = [
    "sec-ancient", "sec-medieval", "sec-modern", "sec-post",
    "sec-world", "sec-culture", "sec-up", "sec-rrb-bank"
]

for s in sections:
    pos = syl.find(f'id="{s}"')
    print(f"Section {s} found at position {pos}")

with open('data/history.json', 'r', encoding='utf-8') as f:
    hist = json.load(f)

print(f"History.json periods: {len(hist['periods'])}")
period_ids = [p['id'] for p in hist['periods']]
print("Some period IDs:", period_ids[:10])
