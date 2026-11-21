import zipfile
import os

docx_path = r'C:\Users\ragha\.gemini\antigravity\brain\219bbe0f-9510-4e70-890a-27eb04002bcb\.user_uploaded\media_1795252867861_d6780294.docx'
out_dir = r'C:\Users\ragha\.gemini\antigravity\scratch\history-of-india\assets\images\mauryan'
os.makedirs(out_dir, exist_ok=True)

image_mapping = {
    'word/media/image1.png': 'sarnath_lion_capital.png',
    'word/media/image2.png': 'mauryan_pillar_diagram.png',
    'word/media/image3.png': 'rampurva_lauriya_pillar.png',
    'word/media/image4.png': 'ashokan_pillar_inscription.png',
    'word/media/image5.png': 'ashoka_major_rock_edicts_table.png',
    'word/media/image6.png': 'ashokan_sandstone_shaft.png'
}

with zipfile.ZipFile(docx_path, 'r') as z:
    for src, dst in image_mapping.items():
        if src in z.namelist():
            dst_path = os.path.join(out_dir, dst)
            with open(dst_path, 'wb') as f:
                f.write(z.read(src))
            print(f"Extracted {src} -> {dst_path} ({os.path.getsize(dst_path)} bytes)")
