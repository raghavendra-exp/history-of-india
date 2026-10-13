import re

with open('art-culture.html', 'r', encoding='utf-8') as f:
    text = f.read()

scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', text, re.IGNORECASE)
for idx, s in enumerate(scripts):
    vars = re.findall(r'(?:const|let|var)\s+([a-zA-Z0-9_]+)\s*=', s)
    if vars:
        print(f"Script {idx}: variables -> {vars}")
