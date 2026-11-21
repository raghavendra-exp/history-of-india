import zipfile
import xml.etree.ElementTree as ET
import json
import os
import re

docx_path = r'C:\Users\ragha\.gemini\antigravity\brain\219bbe0f-9510-4e70-890a-27eb04002bcb\.user_uploaded\media_1795252867861_d6780294.docx'

with zipfile.ZipFile(docx_path, 'r') as z:
    xml_content = z.read('word/document.xml')

tree = ET.fromstring(xml_content)
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

master_tbl = tree.find('.//w:tbl', ns)
rows = master_tbl.findall('./w:tr', ns)

def clean_text(t):
    if not t: return ""
    # Normalize spaces
    t = re.sub(r'\s+', ' ', t).strip()
    return t

ERA_MAP = {
    1: "Sources & Historiography",
    2: "Sources & Historiography",
    3: "Sources & Historiography",
    4: "Chronology & Eras",
    5: "Chronology & Eras",
    6: "Chronology & Eras",
    7: "Prehistory & Proto-History",
    8: "Early Historic Continuum",
    9: "Imperial Eras Overview",
    10: "Sources & Historiography",
    11: "Modern Historiography",
    12: "Colonial Historiography",
    13: "Nationalist Historiography",
    14: "Nationalist Historiography",
    15: "Socio-Economic Historiography",
    16: "Archaeological & Literary Sources",
    17: "Archaeological Chronology",
    18: "Geographical Settings",
    19: "Palaeolithic Age",
    20: "Mesolithic Age",
    21: "Neolithic Age",
    22: "Chalcolithic Cultures",
    23: "Chalcolithic Features",
    24: "Indus Valley Civilization",
    25: "Harappan Economy & Trade",
    26: "Harappan Religion & Burials",
    27: "Harappan Polity & Script",
    28: "Harappan Cities Guide",
    29: "Harappan Decline Theories",
    30: "Vedic Architecture & Literature",
    31: "Vedic Corpus & Vedangas",
    32: "Vedic Sacrifices & Yajnas",
    33: "Early Vedic Age",
    34: "Later Vedic Age",
    35: "Rise of Heterodox Sects",
    36: "Jainism",
    37: "Buddhism",
    38: "Ajivikas & Charvaka",
    39: "Mahajanapadas Overview",
    40: "Guide to 16 Mahajanapadas",
    41: "Rise of Magadha",
    42: "Haryanka Dynasty",
    43: "Ajatashatru",
    44: "End of Haryankas",
    45: "Shishunaga Dynasty",
    46: "Nanda Dynasty",
    47: "Magadha Supremacy Factors",
    48: "Mahajanapada Material Life",
    49: "Persian Achaemenid Invasion",
    50: "Alexander's Invasion",
    51: "Mauryan Empire Foundation",
    52: "Ashoka the Great",
    53: "Later Mauryans & Fall",
    54: "Mauryan Administration",
    55: "Mauryan Society",
    56: "Mauryan Economy & Revenue",
    57: "Ashoka's Policy of Dhamma",
    58: "Mauryan Art & Architecture",
    59: "Post-Mauryan Foreign Invasions",
    60: "Post-Mauryan Synthesis & Impact",
    61: "The Satavahanas",
    62: "Dawn of History in Deep South",
    63: "Post-Mauryan Crafts & Commerce",
    64: "Shunga Dynasty",
    65: "Kanva Dynasty",
    66: "Gupta Empire Foundation",
    67: "The Gupta Classical Golden Age",
    68: "Spread of Civilization in Eastern India",
    69: "Harshavardhana and His Times",
    70: "Hiuen Tsang (Xuanzang) Account",
    72: "Peninsular States & Rural Expansion",
    73: "Religion, Philosophy & Asian Contacts",
    74: "Sequence of Social Changes",
    75: "Feudal Transformation of Ancient Phase",
    76: "Economic Transformation & De-urbanization",
    77: "Religious Transformation & Tantrism",
    78: "Cultural Transformation & Languages",
    79: "Indian Temple Architecture",
    80: "Science & Technology Across Eras"
}

def extract_nested_table(tbl_element):
    rows_data = []
    for r in tbl_element.findall('./w:tr', ns):
        cells_data = []
        for c in r.findall('./w:tc', ns):
            # Recursively collect text
            txt = ' '.join([t.text for t in c.iter(f"{{{ns['w']}}}t") if t.text])
            cells_data.append(clean_text(txt))
        if any(cells_data):
            rows_data.append(cells_data)
    if not rows_data:
        return None
    headers = rows_data[0]
    data_rows = rows_data[1:]
    return {
        "headers": headers,
        "rows": data_rows
    }

def generate_pointers_from_text(title, text):
    """Generate high-yield concise revision bullet points from notes"""
    pointers = []
    
    # Split by section headers or bullets
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line: continue
        # Look for colon-separated definitions or bullet points
        if ':' in line and len(line.split(':')[0]) < 60:
            k, v = line.split(':', 1)
            k = k.strip().lstrip('•-–*1234567890. ')
            v = v.strip()
            if len(v) > 20:
                pointers.append(f"<strong>{k}:</strong> {v[:250]}{'...' if len(v)>250 else ''}")
        elif line.startswith(('•', '-', '–', '*')) and len(line) > 25:
            clean_l = line.lstrip('•-–* ').strip()
            pointers.append(clean_l[:280] + ('...' if len(clean_l)>280 else ''))
        elif any(k in line.lower() for k in ['key feature', 'significance', 'founder', 'capital', 'ruler', 'date', 'inscription', 'excavated']):
            if len(line) > 30 and len(pointers) < 8:
                pointers.append(line[:280] + ('...' if len(line)>280 else ''))

    # If few pointers found, split sentences
    if len(pointers) < 3:
        sentences = re.split(r'\.\s+', text)
        for s in sentences:
            s = clean_text(s)
            if len(s) > 35 and len(s) < 260:
                pointers.append(s)
            if len(pointers) >= 6:
                break
                
    return pointers[:8]

topics = []
all_comparison_tables = []

for r_idx, r in enumerate(rows):
    cells = r.findall('./w:tc', ns)
    if not cells: continue
    
    sl_raw = ''.join([t.text for t in cells[0].iter(f"{{{ns['w']}}}t") if t.text]).strip()
    if not sl_raw or sl_raw.lower().startswith('sl'):
        continue # Header row
        
    point_raw = ''.join([t.text for t in cells[1].iter(f"{{{ns['w']}}}t") if t.text]).strip()
    
    # Parse integer sl_num
    sl_match = re.search(r'\d+', sl_raw)
    sl_num = int(sl_match.group(0)) if sl_match else r_idx
    
    note_cell = cells[2] if len(cells) > 2 else None
    
    paragraphs = []
    nested_tables = []
    has_drawings = False
    
    if note_cell is not None:
        for child in note_cell:
            tag = child.tag.split('}')[-1]
            if tag == 'p':
                p_text = clean_text(''.join([t.text for t in child.iter(f"{{{ns['w']}}}t") if t.text]))
                if p_text:
                    paragraphs.append(p_text)
                if child.findall('.//w:drawing', ns):
                    has_drawings = True
            elif tag == 'tbl':
                tbl_data = extract_nested_table(child)
                if tbl_data:
                    nested_tables.append(tbl_data)
                    all_comparison_tables.append({
                        "topicSl": sl_num,
                        "topicTitle": point_raw,
                        "tableData": tbl_data
                    })

    full_note_text = '\n\n'.join(paragraphs)
    
    # Handle special case for Century (Point 5)
    if sl_num == 5 and not full_note_text:
        full_note_text = """Century Calculation & Historical Dating in Ancient India:
• Mathematical Rule of Century: In Gregorian/Julian reckoning, century refers to the 100-year block ending in that ordinal number. For BCE: 6th century BCE spans 600 BCE to 501 BCE; 1st century BCE spans 100 BCE to 1 BCE. For CE: 1st century CE spans 1 CE to 100 CE; 4th century CE spans 301 CE to 400 CE; 21st century spans 2001 to 2100 CE. Note: There is NO 'Year Zero' between 1 BCE and 1 CE.
• Major Historical Eras of India:
  - Vikrama Samvat (57/58 BCE): Commemorates King Vikramaditya of Ujjain defeating the Shakas; widely used in North and Western Indian Hindu calendars.
  - Shaka Samvat (78 CE): Traditionally started by Kushana ruler Kanishka I at his accession; also associated with Western Kshatrapa ruler Chastana. Adopted as India's National Calendar on 22 March 1957.
  - Kalachuri / Chedi Era (248–249 CE): Founded by Abhira king Ishvarasena in Western Deccan/Maharashtra.
  - Gupta Era (319–320 CE): Founded by Chandragupta I upon his Maharajadhiraja coronation and marriage to Lichchhavi princess Kumaradevi.
  - Valabhi Era (319 CE): Concurrent with Gupta era in Saurashtra.
  - Harsha Era (606 CE): Founded by Harshavardhana of Kannauj/Thanesar upon ascending the throne.
  - Hijri Era (622 CE): Commemorates Prophet Muhammad's migration from Mecca to Medina; lunar calendar used in medieval Islamic chronicles.
  - Kollam Era (825 CE): Solar calendar used in Kerala/Chera regions.
  - Chalukya-Vikrama Era (1076 CE): Founded by Western Chalukya king Vikramaditya VI.
  - Lakshmana Sena Era (1119 CE): Used in Bengal and Mithila."""

    pointers = generate_pointers_from_text(point_raw, full_note_text)
    
    # Assign specific local images where appropriate
    assigned_images = []
    if sl_num == 58 or has_drawings:
        assigned_images = [
            {"path": "assets/images/mauryan/sarnath_lion_capital.png", "caption": "Sarnath Lion Capital of Ashoka (National Emblem)", "type": "Artifact"},
            {"path": "assets/images/mauryan/mauryan_pillar_diagram.png", "caption": "Anatomy of a Mauryan Monolithic Pillar (Shaft, Bell, Abacus, Animal)", "type": "Schematic"},
            {"path": "assets/images/mauryan/rampurva_lauriya_pillar.png", "caption": "Rampurva / Lauriya-Nandangarh Ashokan Pillar in situ", "type": "Monument"},
            {"path": "assets/images/mauryan/ashokan_pillar_inscription.png", "caption": "Close-up of Brahmi Inscription on Chunar Sandstone Shaft", "type": "Epigraphy"},
            {"path": "assets/images/mauryan/ashoka_major_rock_edicts_table.png", "caption": "Master Chart of Ashoka's 14 Major Rock Edicts (I to XIV)", "type": "Chart"},
            {"path": "assets/images/mauryan/ashokan_sandstone_shaft.png", "caption": "Lustrous Mirror-like Mauryan Polish on Freestanding Shaft", "type": "Materiality"}
        ]
    elif sl_num in [24, 25, 26, 27, 28, 29]:
        assigned_images = [
            {"path": "assets/images/indusvalley.png", "caption": "Indus Valley Civilization Urban Grid & Harappan Seals", "type": "Overview"}
        ]
    elif sl_num in [30, 31, 32, 33, 34]:
        assigned_images = [
            {"path": "assets/images/vedic_age.png", "caption": "Vedic Society, Fire Yajnas & Sacred Shrutis", "type": "Overview"},
            {"path": "assets/images/vedic_age_2.png", "caption": "Later Vedic Agricultural Expansion & Painted Grey Ware", "type": "Archaeology"}
        ]
    elif sl_num in [39, 40, 41, 47, 48]:
        assigned_images = [
            {"path": "assets/images/age_of_mahajanpadas.png", "caption": "16 Mahajanapadas & Second Urbanization of India", "type": "Map"}
        ]
    elif sl_num in [51, 52, 54, 57]:
        assigned_images = [
            {"path": "assets/images/ashoka_the_great.png", "caption": "Emperor Ashoka Maurya & The Pan-Indian Empire", "type": "Portrait"}
        ]
    elif sl_num in [66, 67]:
        assigned_images = [
            {"path": "assets/images/gupta_age.png", "caption": "Classical Golden Age of the Guptas (Art, Sarnath, Literature)", "type": "Art"}
        ]
    elif sl_num in [69, 70]:
        assigned_images = [
            {"path": "assets/images/up_harsha_period.png", "caption": "Emperor Harshavardhana & Kannauj Assembly", "type": "History"}
        ]
    elif sl_num in [79]:
        assigned_images = [
            {"path": "assets/images/vijayanagara_empire.png", "caption": "Dravida & Vijayanagara Temple Architecture at Hampi", "type": "Architecture"}
        ]

    category = ERA_MAP.get(sl_num, "Ancient Indian History")
    
    # Create topic entry
    topic_entry = {
        "id": f"topic_{sl_num:02d}_{len(topics)+1}",
        "slNo": sl_num,
        "title": point_raw,
        "category": category,
        "pointers": pointers,
        "fullNotes": full_note_text,
        "tables": nested_tables,
        "images": assigned_images,
        "examKeywords": [w for w in re.findall(r'\b[A-Z][a-zA-Z]{3,}\b', point_raw + " " + full_note_text[:200]) if w not in ['This', 'That', 'With', 'From', 'After', 'Before', 'During', 'These', 'Their']][:8]
    }
    topics.append(topic_entry)

print(f"Extracted {len(topics)} topics!")
print(f"Extracted {len(all_comparison_tables)} total nested comparison tables!")

# Write to data/revision-notes.json
output_data = {
    "totalTopics": len(topics),
    "totalTables": len(all_comparison_tables),
    "topics": topics,
    "comparisonTables": all_comparison_tables
}

with open('data/revision-notes.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("Saved data/revision-notes.json successfully!")
