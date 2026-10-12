import subprocess
import re

with open('art-culture.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', html, re.IGNORECASE)
for idx, s in enumerate(scripts):
    if not s.strip(): continue
    with open(f'scripts/temp_check_{idx}.js', 'w', encoding='utf-8') as tf:
        tf.write(s)
    res = subprocess.run(['node', '--check', f'scripts/temp_check_{idx}.js'], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error in script {idx}:")
        print(res.stderr)
    else:
        print(f"Script {idx}: OK")
