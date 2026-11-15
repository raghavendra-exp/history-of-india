import json

with open('data/mains-questions.json', 'r', encoding='utf-8') as f:
    mq = json.load(f)

for q in mq:
    fw = q['framework']
    if 'diagramMapIdea' not in fw or not fw['diagramMapIdea']:
        fw['diagramMapIdea'] = fw.get('microDiagram', 'Flowchart or map illustrating chronological evolution and structural linkages.')

with open('data/mains-questions.json', 'w', encoding='utf-8') as f:
    json.dump(mq, f, ensure_ascii=False, indent=2)

print("Fixed diagramMapIdea for all Mains questions!")
