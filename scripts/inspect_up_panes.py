import re

with open('up-history.html', 'r', encoding='utf-8') as f:
    text = f.read()

panes = re.findall(r'<div class="up-tab-pane[^"]*"\s+id="([^"]+)">([\s\S]*?)(?=<div class="up-tab-pane|<!-- =+ END|<!-- Footer|\Z)', text)
print(f"Total panes in up-history.html: {len(panes)}")
for pid, pcontent in panes:
    h3s = re.findall(r'<h3[^>]*>([^<]+)</h3>', pcontent)
    print(f"\nPane [{pid}]: {len(h3s)} h3 headings")
    for h in h3s[:6]:
        print(f"  - {h.strip().encode('ascii', 'replace').decode('ascii')}")
