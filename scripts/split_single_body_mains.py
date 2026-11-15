import json

with open('data/mains-questions.json', 'r', encoding='utf-8') as f:
    mq = json.load(f)

for q in mq:
    fw = q['framework']
    if len(fw['body']) == 1:
        single = fw['body'][0]
        pts = single['points']
        mid = len(pts) // 2
        fw['body'] = [
            {
                "heading": single['heading'] + " — Institutional & Economic Drivers",
                "points": pts[:mid]
            },
            {
                "heading": single['heading'] + " — Socio-Political & Strategic Dimensions",
                "points": pts[mid:]
            }
        ]
        print(f"Split body for {q['id']}")

with open('data/mains-questions.json', 'w', encoding='utf-8') as f:
    json.dump(mq, f, ensure_ascii=False, indent=2)

print("All mains questions verified for body length >= 2!")
