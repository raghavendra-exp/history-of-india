import re
from gen_schematics_code import generate_visual_schematics_html

with open('art-culture.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '<!-- Comparison 1: Nagara vs Dravida vs Vesara -->'

if target not in content:
    print("Target comment not found!")
    exit(1)

schematics_html = generate_visual_schematics_html()

# Let's insert before target
new_content = content.replace(target, schematics_html + '\n      ' + target)

with open('art-culture.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully injected visual schematics into art-culture.html!")
