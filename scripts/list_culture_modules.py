import re

with open('art-culture.html', 'r', encoding='utf-8') as f:
    text = f.read()

scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', text, re.IGNORECASE)
s6 = scripts[6]
items = re.findall(r'id":\s*"([^"]+)",\s*"category":\s*"([^"]+)",[\s\S]*?"title":\s*"([^"]+)"', s6)
print(f"Total modules in CULTURE_DATA: {len(items)}")
for i, it in enumerate(items):
    print(f"{i+1:2d}. [{it[0]}] ({it[1]}) {it[2]}")
