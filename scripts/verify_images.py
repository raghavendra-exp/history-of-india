import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'C:\Users\ragha\.gemini\antigravity\scratch\history-of-india'
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

missing_images = []
total_images = 0

for hf in html_files:
    path = os.path.join(base_dir, hf)
    content = open(path, 'r', encoding='utf-8').read()
    srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for s in srcs:
        if s.startswith('http') or s.startswith('data:') or '${' in s:
            continue
        total_images += 1
        img_path = os.path.join(base_dir, s.replace('/', os.sep))
        if not os.path.exists(img_path):
            missing_images.append((hf, s))

print(f"Total static local images verified across all HTML files: {total_images}")
print(f"Missing images: {len(missing_images)}")
if not missing_images:
    print("ALL STATIC IMAGES VERIFIED AND PRESENT ON DISK (100% OK)!")
