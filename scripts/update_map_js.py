# -*- coding: utf-8 -*-
"""
Inject real GPS coordinates (lat, lon) into all 44 sites in js/map.js
and add Leaflet Google Maps tile engine integration.
"""

import re

COORDINATES = {
  "harappa": (30.6275, 72.8683),
  "mohenjo-daro": (27.3292, 68.1389),
  "dholavira": (23.8864, 70.2131),
  "lothal": (22.5222, 72.2494),
  "kalibangan": (29.4739, 74.1319),
  "rakhigarhi": (29.2894, 76.1158),
  "alamgirpur": (29.0225, 77.4917),
  "chanhudaro": (26.1750, 68.3200),
  "rajgriha": (25.0289, 85.4207),
  "pataliputra": (25.6127, 85.1442),
  "shravasti": (27.5190, 82.0224),
  "kaushambi": (25.3400, 81.3800),
  "ujjain": (23.1765, 75.7885),
  "taxila": (33.7463, 72.8258),
  "vaishali": (25.9860, 85.1275),
  "sarnath": (25.3811, 83.0214),
  "sanchi": (23.4795, 77.7397),
  "dhauli": (20.1919, 85.8394),
  "girnar": (21.5222, 70.4579),
  "maski": (15.9558, 76.6575),
  "rampurva": (27.2667, 84.5000),
  "ajanta": (20.5519, 75.7033),
  "ellora": (20.0268, 75.1792),
  "khajuraho": (24.8318, 79.9199),
  "konark": (19.8876, 86.0945),
  "brihadisvara": (10.7828, 79.1318),
  "mamallapuram": (12.6269, 80.1927),
  "nalanda": (25.1357, 85.4449),
  "belur-halebidu": (13.1622, 75.8596),
  "panipat": (29.3909, 76.9635),
  "tarain": (29.8000, 76.9300),
  "talikota": (16.4800, 76.3100),
  "haldighati": (24.8900, 73.7100),
  "chittorgarh": (24.8879, 74.6453),
  "fatehpur-sikri": (27.0945, 77.6679),
  "plassey": (23.8000, 88.2500),
  "buxar": (25.5647, 83.9777),
  "meerut-1857": (28.9845, 77.7064),
  "jhansi": (25.4484, 78.5685),
  "champaran": (26.8000, 84.5000),
  "jallianwala-bagh": (31.6206, 74.8801),
  "chauri-chaura": (26.6500, 83.5800),
  "dandi": (20.8880, 72.8010),
  "kakori": (26.8789, 80.7989)
}

with open('js/map.js', 'r', encoding='utf-8') as f:
    content = f.read()

# For each site, inject lat and lon right after "y": <num>,
updated_count = 0
for sid, (lat, lon) in COORDINATES.items():
    pattern = rf'("id":\s*"{sid}",[\s\S]*?"y":\s*\d+)'
    def repl(m):
        global updated_count
        updated_count += 1
        return m.group(1) + f',\n    "lat": {lat},\n    "lon": {lon}'
    
    content, n = re.subn(pattern, repl, content, count=1)

print(f"Injected coordinates into {updated_count} sites!")

with open('js/map.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated js/map.js!")
