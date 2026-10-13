import re

with open('syllabus.html', 'r', encoding='utf-8') as f:
    text = f.read()

panes = re.findall(r'<div class="syl-section-pane[^"]*"\s+id="([^"]+)">([\s\S]*?)(?=<div class="syl-section-pane|<!-- =+ END|<!-- Footer|\Z)', text)

print(f"Total panes found: {len(panes)}")
for pid, pcontent in panes:
    cards = re.findall(r'<h3 class="syl-card-title">([^<]+)</h3>', pcontent)
    print(f"\nPane: {pid} ({len(cards)} cards)")
    for c in cards:
        print(f"  - {c.strip()}")
