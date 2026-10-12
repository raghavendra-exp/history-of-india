import glob
import re

print(f"{'FILE':20} | {'siteNav':7} | {'renderNav':9} | {'breadcrumb':10} | {'renderBreadcrumb':16} | {'<header>':8} | {'TOP_HEADER/NAV_BAR'}")
print("-" * 100)

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    has_nav = bool(re.search(r'<nav[^>]*id=["\']siteNav["\']', content))
    calls_nav = 'renderNav(' in content
    has_bc = bool(re.search(r'id=["\']breadcrumb["\']', content))
    calls_bc = 'renderBreadcrumb(' in content
    has_header = bool(re.search(r'<header\b', content))

    # Check for visible hero / title banner
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    h1 = h1_match.group(1).strip().replace('\n', ' ')[:40] if h1_match else 'NO H1'

    print(f"{f:20} | {str(has_nav):7} | {str(calls_nav):9} | {str(has_bc):10} | {str(calls_bc):16} | {str(has_header):8} | {h1}")
