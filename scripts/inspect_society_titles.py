import re

with open('society.html', 'r', encoding='utf-8') as f:
    text = f.read()

titles = re.findall(r'title:\s*["\']([^"\']+)["\']', text)
print(f"Total titles in society.html: {len(titles)}")
for i, t in enumerate(titles):
    print(f"{i+1:2d}. {t}")
