import subprocess

with open('art-culture.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', html, re.IGNORECASE)
script2 = scripts[1] # the second inline script

with open('scripts/temp_script.js', 'w', encoding='utf-8') as f:
    f.write(script2)

res = subprocess.run(['node', '--check', 'scripts/temp_script.js'], capture_output=True, text=True)
print("Return code:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)
