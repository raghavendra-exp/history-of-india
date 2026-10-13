import re

with open('art-culture.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find CULTURE_DATA array
match = re.search(r'const CULTURE_DATA = (\[[\s\S]*?\]);', text)
if match:
    import json
    data_str = match.group(1)
    # let's find titles with regex
    titles = re.findall(r'title:\s*["\']([^"\']+)["\']', data_str)
    print(f"Total modules in CULTURE_DATA: {len(titles)}")
    for i, t in enumerate(titles):
        print(f"  {i+1:2d}. {t}")
else:
    print("CULTURE_DATA not found")
