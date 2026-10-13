import re

with open('art-culture.html', 'r', encoding='utf-8') as f:
    text = f.read()

titles = re.findall(r'<h3 class="cult-card-title">([^<]+)</h3>', text)
print(f"Total cult-card-titles in art-culture.html: {len(titles)}")
for i, t in enumerate(titles):
    print(f"{i+1:2d}. {t.strip()}")
