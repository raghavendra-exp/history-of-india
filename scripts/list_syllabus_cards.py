import re

with open('syllabus.html', 'r', encoding='utf-8') as f:
    text = f.read()

cards = re.findall(r'<h3 class="syl-card-title">(.*?)</h3>', text)
print(f"Total syllabus cards in syllabus.html: {len(cards)}")
for i, c in enumerate(cards):
    clean = re.sub(r'<[^>]+>', '', c).strip()
    print(f"{i+1:2d}. {clean}")
