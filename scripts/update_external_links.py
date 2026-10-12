import json

with open('data/external-links.json', 'r', encoding='utf-8') as f:
    ext = json.load(f)

new_links = {
    "B.L. Grover": {"url": "https://www.britannica.com/place/India/The-British-1600-1947", "source": "Britannica"},
    "Col. James Tod": {"url": "https://en.wikipedia.org/wiki/James_Tod", "source": "Wikipedia"},
    "Pratik Nayak": {"url": "https://raghavendra-exp.github.io/history-of-india/timeline.html", "source": "History of India"},
    "Yuval Noah Harari": {"url": "https://www.ynharari.com/book/sapiens/", "source": "Official"},
    "Hindustan Socialist Republican Association": {"url": "https://www.britannica.com/topic/Hindustan-Socialist-Republican-Association", "source": "Britannica"},
    "Chittagong Armoury Raid": {"url": "https://en.wikipedia.org/wiki/Chittagong_armoury_raid", "source": "Wikipedia"},
    "Vithalbhai J. Patel": {"url": "https://en.wikipedia.org/wiki/Vithalbhai_Patel", "source": "Wikipedia"},
    "Mehrgarh": {"url": "https://www.britannica.com/place/Mehrgarh", "source": "Britannica"},
    "Vijay Stambha": {"url": "https://en.wikipedia.org/wiki/Vijaya_Stambha", "source": "Wikipedia"},
    "Rana Kumbha": {"url": "https://en.wikipedia.org/wiki/Rana_Kumbha", "source": "Wikipedia"},
    "Royal Indian Navy Mutiny": {"url": "https://en.wikipedia.org/wiki/Royal_Indian_Navy_mutiny", "source": "Wikipedia"},
    "Maharana Pratap": {"url": "https://www.britannica.com/biography/Rana-Pratap-Singh", "source": "Britannica"}
}

ext.update(new_links)

with open('data/external-links.json', 'w', encoding='utf-8') as f:
    json.dump(ext, f, ensure_ascii=False, indent=2)

print(f"Updated external links! Total now: {len(ext)}")
