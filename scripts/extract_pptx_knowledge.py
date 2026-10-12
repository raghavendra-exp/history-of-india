import os
import zipfile
import xml.etree.ElementTree as ET
import json
import re

def extract_text_from_slide_xml(xml_bytes):
    try:
        tree = ET.fromstring(xml_bytes)
        texts = []
        for elem in tree.iter():
            if elem.tag.endswith('}t') and elem.text:
                texts.append(elem.text)
        return ' '.join(texts).strip()
    except Exception as e:
        return ""

def process_pptx_folder(folder_path):
    results = {}
    if not os.path.exists(folder_path):
        return results

    for fname in sorted(os.listdir(folder_path)):
        if fname.lower().endswith('.pptx'):
            full_path = os.path.join(folder_path, fname)
            try:
                with zipfile.ZipFile(full_path, 'r') as z:
                    slide_files = [n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')]
                    # Sort numerically
                    def slide_num(name):
                        m = re.search(r'slide(\d+)\.xml', name)
                        return int(m.group(1)) if m else 0
                    slide_files.sort(key=slide_num)

                    slides_data = []
                    for s in slide_files:
                        text = extract_text_from_slide_xml(z.read(s))
                        if text:
                            slides_data.append(text)
                    results[fname] = {
                        "total_slides": len(slide_files),
                        "slides": slides_data
                    }
                    print(f"Loaded {fname}: {len(slides_data)} slides with text")
            except Exception as e:
                print(f"Error loading {fname}: {e}")
    return results

if __name__ == "__main__":
    fs_results = process_pptx_folder(r"D:\My notes for exams\History\History_Freedom_Struggle_PRATIK_NAYAK")
    wh_results = process_pptx_folder(r"D:\My notes for exams\History\History_World_PRATIK_NAYAK")
    
    with open("scripts/extracted_fs_notes.json", "w", encoding="utf-8") as f:
        json.dump(fs_results, f, ensure_ascii=False, indent=2)
    with open("scripts/extracted_wh_notes.json", "w", encoding="utf-8") as f:
        json.dump(wh_results, f, ensure_ascii=False, indent=2)

    print("Extracted notes saved!")
