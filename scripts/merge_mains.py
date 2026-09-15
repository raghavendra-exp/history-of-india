# -*- coding: utf-8 -*-
"""
Merge and validate all Mains question batches into data/mains-questions.json
"""

import json
import glob
import os

BATCH_FILES = [
    'data/batch_mains_ancient.json',
    'data/batch_mains_medieval.json',
    'data/batch_mains_modern.json',
    'data/batch_mains_art_culture.json',
    'data/batch_mains_world.json',
    'data/batch_mains_up.json'
]

def main():
    all_mains = []
    seen_ids = set()
    category_counts = {}
    pyq_count = 0

    for path in BATCH_FILES:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing required batch file: {path}")
        with open(path, 'r', encoding='utf-8') as f:
            batch = json.load(f)
            print(f"Loaded {len(batch)} items from {path}")
            for q in batch:
                qid = q['id']
                if qid in seen_ids:
                    raise ValueError(f"Duplicate ID found: {qid} in {path}")
                seen_ids.add(qid)
                
                # Normalize category and categoryLabel
                if 'category' not in q or not q['category']:
                    if qid.startswith('mains_anc_'):
                        q['category'] = 'ancient'
                        q['categoryLabel'] = 'Ancient India'
                    elif qid.startswith('mains_med_'):
                        q['category'] = 'medieval'
                        q['categoryLabel'] = 'Medieval India'
                    elif qid.startswith('mains_mod_'):
                        q['category'] = 'modern'
                        q['categoryLabel'] = 'Modern India'
                    elif qid.startswith('mains_art_'):
                        q['category'] = 'art-culture'
                        q['categoryLabel'] = 'Art & Culture'
                    elif qid.startswith('mains_wor_'):
                        q['category'] = 'world-history'
                        q['categoryLabel'] = 'World History'
                    elif qid.startswith('mains_up_'):
                        q['category'] = 'up-history'
                        q['categoryLabel'] = 'UP Special'
                    else:
                        q['category'] = 'general'
                        q['categoryLabel'] = 'General'

                # Schema validation
                assert 'category' in q and q['category'], f"Empty category in {qid}"
                assert 'periodId' in q and q['periodId'], f"Empty periodId in {qid}"
                assert q['marks'] in (10, 15, 20), f"Invalid marks {q.get('marks')} in {qid}"
                assert q['wordLimit'] in (150, 250), f"Invalid wordLimit {q.get('wordLimit')} in {qid}"
                assert isinstance(q['isPyq'], bool), f"Invalid isPyq in {qid}"
                assert 'question' in q and len(q['question']) > 20, f"Question too short in {qid}"
                assert 'bookRef' in q and q['bookRef'], f"Empty bookRef in {qid}"
                
                fw = q.get('framework', {})
                assert 'intro' in fw and len(fw['intro']) > 20, f"Intro missing/short in {qid}"
                assert 'body' in fw and len(fw['body']) >= 2, f"Body should have at least 2 headings in {qid}"
                for b in fw['body']:
                    assert 'heading' in b and b['heading'], f"Missing heading in {qid}"
                    assert 'points' in b and len(b['points']) >= 1, f"Empty points in {qid}"
                assert 'conclusion' in fw and len(fw['conclusion']) > 20, f"Conclusion missing/short in {qid}"
                assert 'diagramMapIdea' in fw and fw['diagramMapIdea'], f"Diagram idea missing in {qid}"

                all_mains.append(q)
                cat = q.get('category', 'unknown')
                category_counts[cat] = category_counts.get(cat, 0) + 1
                if q.get('isPyq'):
                    pyq_count += 1

    out_path = 'data/mains-questions.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(all_mains, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully merged {len(all_mains)} Mains questions into {out_path}!")
    print(f"Total Authentic PYQs: {pyq_count}")
    print("Category Breakdown:")
    for cat, count in category_counts.items():
        print(f"  - {cat}: {count}")

if __name__ == '__main__':
    main()
