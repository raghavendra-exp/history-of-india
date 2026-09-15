# -*- coding: utf-8 -*-
import re

text = open('js/map.js', encoding='utf-8').read()
matches = re.findall(r'"id":\s*"([^"]+)",\s*"name":\s*"([^"]+)"', text)
print(f"Total sites: {len(matches)}")
for sid, name in matches:
    print(f"  {sid}: {name}")
