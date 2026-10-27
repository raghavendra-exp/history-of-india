import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

culture_dir = r'C:\Users\ragha\.gemini\antigravity\scratch\history-of-india\assets\culture'
if os.path.exists(culture_dir):
    files = os.listdir(culture_dir)
    print(f"Total files in assets/culture: {len(files)}")
    for f in sorted(files)[:20]:
        print(" -", f)
else:
    print("assets/culture does not exist")
