import urllib.request
import urllib.parse
import json
import os
import sys

TOPICS = [
    ('harappan-town-planning', 'Great Bath Mohenjo-daro', 'Great Bath & Citadel of Mohenjo-daro (Indus Valley)'),
    ('mauryan-pillars-caves', 'Ashoka pillar at Vaishali', 'Monolithic Ashokan Column with Bell-Lotus Capital'),
    ('stupa-architecture', 'Great Stupa at Sanchi', 'Great Stupa at Sanchi (Toranas, Anda, Medhi & Harmika)'),
    ('cave-architecture', 'Karla Caves Chaitya hall', 'Karle Chaitya Hall & Barabar Rock-Cut Excavations'),
    ('ajanta-ellora-elephanta', 'Kailasa temple Ellora', 'Kailash Monolithic Temple (Cave 16, Ellora) & Ajanta Murals'),
    ('nagara-temple-style', 'Kandariya Mahadeva temple', 'Kandariya Mahadeva Temple at Khajuraho (Nagara Style)'),
    ('dravida-temple-style', 'Brihadisvara Temple Thanjavur', 'Brihadisvara Temple at Thanjavur (Chola Dravidian Vimana)'),
    ('vesara-temple-style', 'Hoysaleswara temple Halebidu', 'Hoysaleswara Temple at Halebidu (Stellate Vesara Order)'),
    ('indo-islamic-sultanate', 'Qutb Minar Delhi', 'Qutb Minar & Alai Darwaza (Delhi Sultanate Arcuate System)'),
    ('indo-islamic-provincial', 'Gol Gumbaz Bijapur', 'Gol Gumbaz Whispering Gallery & Provincial Indo-Islamic Splendor'),
    ('mughal-architecture', 'Taj Mahal Agra', 'Taj Mahal at Agra (Mughal Double Dome & Pietra Dura)'),
    ('rajput-sikh-architecture', 'Amber Fort Jaipur', 'Hill Forts of Rajasthan & Harmandir Sahib Golden Temple'),
    ('colonial-modern-architecture', 'Chhatrapati Shivaji Maharaj Terminus', 'CSMT Victorian Gothic & Lutyens Imperial Architecture'),
    ('sculptural-schools', 'Seated Buddha Gandhara British Museum', 'Gandhara, Mathura & Amaravati Sculptural Buddha Icons'),
    ('prehistoric-rock-paintings', 'Rock Shelters of Bhimbetka', 'Bhimbetka Mesolithic Rock Art & Sacred Cave Ochre Murals'),
    ('indus-valley-sculptures', 'Dancing Girl of Mohenjo-daro', 'Bronze Dancing Girl & Steatite Priest-King Sculptures'),
    ('mauryan-classical-sculpture', 'Lion Capital of Ashoka', 'Ashokan Quadruple Lion Capital at Sarnath (National Emblem)'),
    ('gupta-golden-age-sculpture', 'Sarnath Seated Buddha', 'Sarnath Seated Buddha in Dharmachakra Mudra (Gupta Age)'),
    ('chola-bronze-sculpture', 'Chola Nataraja bronze', 'Chola Lost-Wax Bronze Nataraja in Ananda Tandava'),
    ('mural-paintings', 'Ajanta cave paintings Padmapani', 'Padmapani Bodhisattva Fresco at Ajanta Caves (Cave 1)'),
    ('miniature-paintings-court', 'Mughal miniature painting Jahangir', 'Mughal Imperial Tasvir Khana & Court Miniatures'),
    ('rajasthani-pahari-miniature', 'Bani Thani Kishangarh', 'Bani Thani (Kishangarh) & Kangra Valley Romantic Miniatures'),
    ('folk-tribal-paintings', 'Madhubani painting Bihar', 'Madhubani, Warli, Pattachitra & Kalamkari Folk Art'),
    ('modern-indian-painting', 'Raja Ravi Varma painting', 'Raja Ravi Varma, Abanindranath Tagore & Modern Masters'),
    ('pottery-chronology', 'Painted Grey Ware pottery', 'Archaeological Ceramic Sequence: OCP, BRW, PGW & NBPW'),
    ('classical-dances', 'Bharatanatyam dancer', '8 Classical Dance Traditions (Bharatanatyam, Kathak, Kathakali...)'),
    ('folk-semi-classical-dances', 'Chhau dance', 'Chhau Martial Dance, Kalbelia, Garba & Regional Folk Celebrations'),
    ('indian-classical-music', 'Hindustani classical music sitar', 'Hindustani Gharanas, 10 Thaats & Carnatic Trinity System'),
    ('musical-instruments-vadya', 'Saraswati veena instrument', '4 Canonical Vadya Families: Tata, Sushira, Avanaddha & Ghana'),
    ('regional-folk-music', 'Baul singer Bengal', 'Baul Minstrels, Pandavani Ballads & Regional Folk Music'),
    ('classical-folk-theatre', 'Koodiyattam Kerala', 'Koodiyattam Sanskrit Theatre, Yakshagana & Folk Stages'),
    ('puppetry-traditions', 'Kathputli puppets Rajasthan', '4 Puppetry Forms: String (Kathputli), Shadow, Rod & Glove'),
    ('martial-arts-india', 'Kalaripayattu Kerala combat', 'Kalaripayattu, Silambam, Gatka & Indian Martial Traditions'),
    ('classical-languages', 'Tolkappiyam Tamil manuscript', '11 Classical Languages of India (Updated 2024 Gazette)'),
    ('vedic-sanskrit-literature', 'Rigveda manuscript Sanskrit', 'Vedic Corpus, Upanishadic Philosophy & Sanskrit Epics'),
    ('buddhist-jain-literature', 'Tripitaka Buddhist canon', 'Pali Tripitaka, Jataka Tales & Jain Ardhamagadhi Agamas'),
    ('sangam-dravidian-literature', 'Thiruvalluvar statue Kanyakumari', 'Sangam Tamil Corpus, 5 Thinais & Post-Sangam Epics'),
    ('bhakti-sufi-literature', 'Kabir Das saint painting', 'Bhakti Mystics (Kabir, Mirabai, Tulsidas) & Sufi Poetry'),
    ('indo-persian-literature', 'Akbarnama miniature painting', 'Indo-Persian Chronicles, Amir Khusrau & Ain-i-Akbari'),
    ('unesco-intangible-heritage', 'Kumbh Mela festival India', 'UNESCO 14 Intangible Cultural Heritage Masterpieces of India'),
    ('fairs-festivals-calendars', 'Hornbill Festival Nagaland', 'Pan-Indian Fairs, Sacred Festivals & Astronomical Calendars')
]

out_dir = os.path.join(os.path.dirname(__file__), '..', 'assets', 'culture')
os.makedirs(out_dir, exist_ok=True)

headers = {'User-Agent': 'IndianHistoryEducationalPortal/2.0 (student-history-portal@gov.in)'}

results = {}

for item_id, query, caption in TOPICS:
    file_path = os.path.join(out_dir, f'{item_id}.jpg')
    if os.path.exists(file_path) and os.path.getsize(file_path) > 1000:
        print(f'[EXISTS] {item_id}: {os.path.getsize(file_path)} bytes')
        results[item_id] = {'caption': caption, 'file': f'assets/culture/{item_id}.jpg'}
        continue

    print(f'Fetching image for: {query} ({item_id})...')
    try:
        url = f'https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrlimit=1&prop=pageimages&pithumbsize=640&format=json'
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            img_url = None
            for pid, pdata in pages.items():
                if 'thumbnail' in pdata:
                    img_url = pdata['thumbnail']['source']
                    break
            
            if img_url:
                print(f'  Found URL: {img_url}')
                img_req = urllib.request.Request(img_url, headers=headers)
                with urllib.request.urlopen(img_req, timeout=12) as img_resp:
                    content = img_resp.read()
                    with open(file_path, 'wb') as f:
                        f.write(content)
                    print(f'  Saved {len(content)} bytes to {file_path}')
                    results[item_id] = {'caption': caption, 'file': f'assets/culture/{item_id}.jpg', 'remote': img_url}
            else:
                print(f'  No thumbnail found for {query}')
    except Exception as e:
        print(f'  Error for {item_id}: {e}')

print(f'\nTotal downloaded: {len([f for f in os.listdir(out_dir) if f.endswith(".jpg")])} / {len(TOPICS)}')
