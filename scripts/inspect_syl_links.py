import re
import json

with open('syllabus.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('data/history.json', 'r', encoding='utf-8') as f:
    hist = json.load(f)
existing_period_ids = set(p['id'] for p in hist.get('periods', []))

period_links = re.findall(r'href="period\.html\?id=([^"]+)"', text)
print(f"Total period links in syllabus.html: {len(period_links)}")

missing_periods = []
for pid in set(period_links):
    if pid not in existing_period_ids:
        missing_periods.append(pid)

print(f"Missing periods in history.json: {len(missing_periods)}")
for m in missing_periods:
    print(f"  - {m}")
