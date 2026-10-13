import re

with open('art-culture.html', 'r', encoding='utf-8') as f:
    text = f.read()

scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', text, re.IGNORECASE)
s6 = scripts[6]
lines = s6.splitlines()
print(f"Total lines in script 6: {len(lines)}")
for l in lines[:40]:
    print(l)
