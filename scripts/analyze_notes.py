import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/extracted_fs_notes.json', encoding='utf-8') as f:
    fs_data = json.load(f)

print(f"Total files analyzed: {len(fs_data)}")
for k, v in fs_data.items():
    full_text = " ".join(v['slides'])
    # Find UPSC questions mentioned in slides
    upsc_qs = re.findall(r'(?:UPSC|Prelims|Mains|Q\.)\s*[:\-–]?[^\.\?\n]{10,120}[\.\?]', full_text)
    print(f"\n=== {k} ({v['total_slides']} slides, {len(full_text):,} chars) ===")
    # Print first few slide summaries
    print("Slide snippets:")
    for s in v['slides'][:4]:
        snippet = s[:120].replace('\n', ' ')
        print(f"  • {snippet}...")
    if upsc_qs:
        print(f"Exam questions found ({len(upsc_qs)}):")
        for q in upsc_qs[:3]:
            print(f"  ? {q.strip()}")
