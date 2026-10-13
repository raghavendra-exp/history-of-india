import re

with open('up-history.html', 'r', encoding='utf-8') as f:
    text = f.read()

tabs = re.findall(r'<button class="up-tab-btn[^"]*"\s+onclick="switchUpTab\(\'([^\']+)\'\)">([^<]+)</button>', text)
print(f"Total tabs in up-history.html: {len(tabs)}")
for t in tabs:
    print(f"  Tab [{t[0]}]: {t[1].strip().encode('ascii', 'replace').decode('ascii')}")
