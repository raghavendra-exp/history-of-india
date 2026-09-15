# scripts/merge_prelims.py
import json

def merge_all():
    files = [
        'data/prelims_part2.json',
        'data/batch_ancient.json',
        'data/batch_medieval.json',
        'data/batch_modern.json',
        'data/batch_art_culture.json',
        'data/batch_world.json',
        'data/batch_up.json'
    ]
    
    all_qs = []
    seen_ids = set()
    
    for fpath in files:
        with open(fpath, 'r', encoding='utf8') as f:
            data = json.load(f)
            for q in data:
                q_id = q['id']
                if q_id in seen_ids:
                    raise ValueError(f"Duplicate ID found: {q_id}")
                seen_ids.add(q_id)
                # Validation checks
                assert len(q['options']) == 4, f"Question {q_id} does not have exactly 4 options!"
                assert 0 <= q['correctIndex'] <= 3, f"Question {q_id} has invalid correctIndex: {q['correctIndex']}"
                assert len(q['question'].strip()) > 10, f"Question {q_id} has too short question text!"
                assert len(q['explanation'].strip()) > 10, f"Question {q_id} has too short explanation!"
                all_qs.append(q)

    print(f"Total merged Prelims questions: {len(all_qs)}")
    
    # Check breakdown by category
    cats = {}
    pyqs = 0
    for q in all_qs:
        c = q.get('category', 'uncategorized')
        cats[c] = cats.get(c, 0) + 1
        if q.get('isPyq'):
            pyqs += 1
            
    print("Breakdown by category:")
    for c, count in cats.items():
        print(f"  - {c}: {count}")
    print(f"Total authentic PYQs: {pyqs}")

    with open('data/prelims-questions.json', 'w', encoding='utf8') as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
        
    print("Saved successfully to data/prelims-questions.json")

if __name__ == '__main__':
    merge_all()
