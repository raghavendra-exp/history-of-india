import json
import re

with open('data/history.json', 'r', encoding='utf-8') as f:
    hist = json.load(f)
periods = hist.get('periods', [])
period_map = {p['id']: p for p in periods}

with open('syllabus.html', 'r', encoding='utf-8') as f:
    syl = f.read()

with open('art-culture.html', 'r', encoding='utf-8') as f:
    cult = f.read()

with open('society.html', 'r', encoding='utf-8') as f:
    soc = f.read()

with open('up-history.html', 'r', encoding='utf-8') as f:
    up = f.read()

with open('practice.html', 'r', encoding='utf-8') as f:
    prac = f.read()

# Let's inspect key concepts from the user's prompt across our entire codebase
topics = [
    # Section 1
    ("Epigraphy: Brahmi, Kharosthi, Ashokan edicts, Allahabad Pillar, Aihole", ["brahmi", "kharosthi", "aihole", "allahabad pillar"]),
    ("Numismatics: punch-marked, Indo-Greek, Kushana gold, Gupta coins", ["punch-marked", "indo-greek", "kushana", "gupta dynastic"]),
    ("Literary Sources: Vedangas, Agamas, Charaka, Sushruta, Aryabhata", ["vedanga", "agama", "charaka", "sushruta", "aryabhata"]),
    ("Foreign Accounts: Megasthenes, Periplus, Ptolemy, Faxian, Xuanzang, Yijing, Al-Biruni", ["megasthenes", "periplus", "ptolemy", "faxian", "xuanzang", "yijing", "al-biruni"]),
    ("Historiography: Colonial, Nationalist, Marxist, Subaltern, Revisionist", ["colonial", "nationalist", "marxist", "subaltern", "revisionist"]),
    ("Palaeolithic: Soan, Bhimbetka, Hunsgi, Attirampakkam, Acheulian", ["soan", "bhimbetka", "hunsgi", "attirampakkam"]),
    ("Mesolithic: Microliths, Bagor, Adamgarh", ["microlith", "bagor", "adamgarh"]),
    ("Neolithic: V. Gordon Childe, Burzahom, Mehrgarh, Ashmounds", ["gordon childe", "burzahom", "mehrgarh", "ashmound"]),
    ("Chalcolithic: Ahar-Banas, Kayatha, Malwa, Jorwe, Daimabad, Inamgaon", ["ahar-banas", "kayatha", "malwa", "jorwe", "daimabad", "inamgaon"]),
    ("IVC: Kot Diji, Amri, Sutkagendor, Alamgirpur, Manda, Daimabad", ["kot diji", "amri", "sutkagendor", "alamgirpur", "manda"]),
    ("IVC Engineering: Citadel/Lower Town, grid, Dholavira, Lothal dockyard", ["dholavira", "lothal", "grid iron", "citadel"]),
    ("IVC Trade: Meluhha, Dilmun, Makan, seals, weights", ["meluhha", "dilmun", "makan"]),
    ("IVC Society & Religion: Pashupati, Mother Goddess, bead-making Chanhudaro", ["pashupati", "chanhudaro", "mother goddess"]),
    ("IVC Decline: Saraswati drying, Wheeler Aryan invasion, climate change", ["saraswati", "mortimer wheeler", "aryan invasion"]),
    ("Early Vedic: Sapta-Sindhu, Rajan, Sabha, Samiti, Vidatha, Gana, Apala, Ghosha", ["sapta-sindhu", "rajan", "sabha", "samiti", "vidatha", "apala", "ghosha"]),
    ("Later Vedic: Gangetic Doab, Janapadas, Rajasuya, Ashvamedha, Vajapeya, Ratnins, Gotra", ["gangetic doab", "rajasuya", "ashvamedha", "vajapeya", "ratnin", "gotra"]),
    ("Mahajanapadas: 16 states, Anguttara Nikaya, Ganasanghas Vrijis Mallas", ["anguttara nikaya", "ganasangha", "vriji", "malla"]),
    ("Magadhan Hegemony: Bimbisara, Ajatashatru, Mahashilakantaka, Rathamusala, Nandas", ["bimbisara", "ajatashatru", "mahashilakantaka", "rathamusala", "nanda"]),
    ("Persian & Alexander: Darius I, Kharosthi, Alexander 326 BCE", ["darius", "alexander", "326 bce"]),
    ("Heterodox: Four Noble Truths, Ashtangika Marga, Pratityasamutpada, Councils 1-4", ["noble truths", "eightfold path", "pratityasamutpada", "buddhist council"]),
    ("Jainism: Tirthankaras, Anekantavada, Syadvada, Triratna, Digambara, Svetambara", ["anekantavada", "syadvada", "triratna", "digambara", "svetambara"]),
    ("Other Sects: Ajivikas Makkhali Gosala, Charvakas Lokayata", ["ajivika", "makkhali gosala", "charvaka", "lokayata"]),
    ("Mauryas: Kautilya Saptanga, Samaharta, Sannidhata, Gudha Purushas, Sitadhyaksha", ["saptanga", "samaharta", "sannidhata", "gudha purusha", "sitadhyaksha"]),
    ("Ashoka Dhamma: Kalinga, Dhamma Mahamattas, Rock/Pillar edicts", ["kalinga", "dhamma mahamatta", "pillar edict"]),
    ("Post-Mauryan: Shungas, Kanvas, Satavahanas Gautamiputra, Karle, Bhaja", ["shunga", "kanva", "satavahana", "gautamiputra", "karle", "bhaja"]),
    ("Foreign: Indo-Greeks Menander Milinda Panha, Rudradaman Junagadh, Kushanas Kanishka", ["menander", "milinda panha", "rudradaman", "junagadh", "kanishka"]),
    ("Sangam Age: Cheras, Cholas, Pandyas, Ettutogai, Pattupattu, Silappadikaram, Tinai, Arikamedu", ["ettutogai", "pattupattu", "silappadikaram", "tinai", "arikamedu"]),
    ("Guptas: Samudragupta Digvijaya, Grahana-Moksha-Anugraha, Chandragupta II, Samantas, Agraharas", ["samudragupta", "grahana-moksha", "chandragupta ii", "samanta", "agrahara"]),
    ("Vakatakas: Matrimonial alliances, Ajanta cave patronage", ["vakataka", "ajanta"]),
    ("Harsha: Kannauj assembly, Prayag assembly, Xuanzang", ["harshavardhana", "kannauj assembly", "prayag assembly"]),
    ("South: Pallavas Mahabalipuram, Chalukyas Pulakeshin II, Rashtrakutas Ellora, Cholas Uttiramerur Kudavolai", ["pulakeshin ii", "mahabalipuram", "uttiramerur", "kudavolai"]),

    # Section 2: Medieval
    ("Early Medieval: Indian Feudalism debate, Rajputs, Muhammad bin Qasim 712, Mahmud Ghazni Somnath, Muhammad Ghori Tarain", ["indian feudalism", "muhammad bin qasim", "ghazni", "somnath", "tarain"]),
    ("Delhi Sultanate: Iltutmish Iqta Turkan-i-Chahalgani, Balban Sajda Paibos", ["iltutmish", "iqta", "turkan-i-chahalgani", "balban", "sajda", "paibos"]),
    ("Alauddin Khalji: Dag, Chehra, Sarai-i-Adl, Shahna-i-Mandi, Masahat", ["dag", "chehra", "sarai-i-adl", "shahna-i-mandi", "masahat"]),
    ("Muhammad bin Tughlaq: Daulatabad, token currency, Diwan-i-Kohi, Sondhar", ["daulatabad", "token currency", "diwan-i-kohi", "sondhar"]),
    ("Firoz Shah Tughlaq: Canals, Karkhanas, Jizya", ["firoz shah tughlaq", "karkhana"]),
    ("Sultanate Admin: Diwan-i-Wizarat, Diwan-i-Arz, Diwan-i-Insha, Diwan-i-Rasalat", ["diwan-i-wizarat", "diwan-i-arz", "diwan-i-insha", "diwan-i-rasalat"]),
    ("Vijayanagara: Sangama, Saluva, Tuluva, Aravidu, Krishnadeva Raya Amuktamalyada, Nayankara, Ayagar, Talikota 1565", ["amuktamalyada", "nayankara", "ayagar", "talikota", "krishnadeva raya"]),
    ("Mughals: Babur Tulughma, Sher Shah Rai Rupiya Sadak-e-Azam", ["tulughma", "sher shah", "rupiya", "sadak-e-azam"]),
    ("Akbar: Mansabdari Zat Sawar Du-aspa, Dahsala Todar Mal, Polaj Parauti, Sulh-i-kul, Ibadat Khana, Mazhar Nama", ["mansabdari", "zat", "sawar", "dahsala", "todar mal", "polaj", "parauti", "sulh-i-kul", "mazhar nama"]),
    ("Marathas: Shivaji Hindavi Swarajya, Ashta Pradhan, Chauth, Sardeshmukhi, Panipat 1761", ["hindavi swarajya", "ashta pradhan", "chauth", "sardeshmukhi", "panipat 1761"]),

    # Section 3: Modern
    ("18th C: Murshid Quli, Saadat Khan, Nizam-ul-Mulk, Haidar Ali, Tipu, Ranjit Singh, Carnatic Dupleix", ["murshid quli", "saadat khan", "nizam-ul-mulk", "haidar ali", "tipu sultan", "ranjit singh", "carnatic"]),
    ("British Conquest: Plassey 1757, Buxar 1764, Treaty of Allahabad, Dual Govt, Subsidiary Alliance, Doctrine of Lapse", ["plassey", "buxar", "treaty of allahabad", "subsidiary alliance", "doctrine of lapse"]),
    ("Economic: R.P. Dutt 3 phases, Permanent Cornwallis Sunset Law, Ryotwari Munro, Mahalwari Mackenzie, Drain of Wealth Naoroji", ["r.p. dutt", "permanent settlement", "sunset law", "ryotwari", "mahalwari", "drain of wealth"]),
    ("Admin: Regulating 1773, Pitt 1784, Charter 1813/1833/1853, Cornwallis Code, Macaulay Downward Filtration, Wood Despatch 1854", ["regulating act 1773", "pitt's india act", "downward filtration", "wood's despatch"]),
    ("1857: Santhal Hool, Munda Ulgulan, 1857 causes/leaders, 1858 Act, Peel Commission", ["santhal hool", "munda ulgulan", "1857", "peel commission"]),
    ("Reform: Brahmo, Vidyasagar Widow 1856, Phule Satyashodhak Gulamgiri, Dayanand Arya, Vivekananda, Aligarh", ["vidyasagar", "satyashodhak", "gulamgiri", "dayanand", "vivekananda", "aligarh"]),
    ("National Movement: Moderates 3Ps, Extremists Lal-Bal-Pal, Bengal 1905, Surat 1907, Morley-Minto 1909, Ghadar, Lucknow 1916", ["lal-bal-pal", "surat split", "morley-minto", "ghadar", "lucknow pact"]),
    ("Gandhian: Champaran, Ahmedabad, Kheda, Rowlatt, Jallianwala, Montford Dyarchy, NCM Chauri Chaura, Swaraj Party, HSRA, CDM Dandi, Poona Pact, 1935 Act, QIM, INA, Mountbatten", ["champaran", "rowlatt", "jallianwala", "chauri chaura", "swaraj party", "dandi", "poona pact", "government of india act 1935", "quit india", "ina", "mountbatten"]),

    # Section 4: Post-Independence
    ("Nation-Building: Patel/Menon, Junagadh, Hyderabad Polo, J&K Accession, Dhar/JVP/Fazl Ali, States Reorganisation 1956, Tribal Panchsheel", ["operation polo", "instrument of accession", "fazl ali", "states reorganisation", "tribal panchsheel"]),
    ("Economy: Mahalanobis model, PSUs, Land Reforms, Green Revolution HYV", ["mahalanobis", "green revolution"]),
    ("Foreign & Crisis: NAM, Panchsheel 1954, 1962 China, 1965/1971 Pakistan, Emergency 1975-77", ["panchsheel", "sino-indian", "shimla agreement", "emergency"]),

    # Section 5: World History
    ("Revolutions: Locke/Rousseau, Industrial Revolution, American 1776, French 1789 Bastille Robespierre Napoleon", ["locke", "rousseau", "industrial revolution", "american revolution", "french revolution", "bastille", "robespierre", "napoleon"]),
    ("Nationalism: Italy Mazzini/Cavour/Garibaldi, Germany Bismarck Blood and Iron, Scramble for Africa Berlin 1884, Opium Wars", ["cavour", "garibaldi", "bismarck", "blood and iron", "scramble for africa", "opium wars"]),
    ("World Wars: WWI, Versailles 1919, Russian 1917 Lenin/Bolshevik, Fascism Mussolini, Nazism Hitler, WWII Stalingrad Pearl Harbor", ["versailles", "russian revolution", "bolshevik", "mussolini", "hitler", "pearl harbor"]),
    ("Cold War & Decol: Bipolarity, Truman, Marshall, NATO/Warsaw, Cuban Crisis, USSR disintegration 1991 Glasnost Perestroika", ["truman doctrine", "marshall plan", "nato", "cuban missile", "glasnost", "perestroika"]),

    # Section 6: Art & Culture
    ("Numismatics/Epigraphy art: Scripts evolution, Samudragupta Veena, Kumaragupta elephant", ["samudragupta playing", "kumaragupta"]),
    ("Temple Architecture: Nagara (Latina/Phamsana/Valabhi), Dravida (Vimana/Gopuram/Prakara), Khajuraho Panchayatana, Solanki Modhera, Odisha Deul Jagamohana, Hoysala soapstone stellate", ["latina", "phamsana", "valabhi", "prakara", "gopuram", "panchayatana", "modhera", "jagamohana", "stellate"]),
    ("Indo-Islamic: Trabeate to Arcuate, Pietra Dura, Jali, Charbagh, Double-dome", ["trabeate", "arcuate", "pietra dura", "jali", "charbagh", "double-dome"]),
    ("Philosophy & ICH: Samkhya Kapila, Yoga Patanjali, Nyaya Gautama, Vaisheshika Kanada, Mimamsa Jaimini, Vedanta (Advaita/Vishishtadvaita/Dvaita), UNESCO ICH list", ["samkhya", "kapila", "nyaya", "vaisheshika", "mimamsa", "advaita", "unesco intangible"]),

    # Part A: UP Special
    ("UP Ancient: Belan, Lahuradewa, Koldihwa, Alamgirpur, Sanauli, 8 Mahajanapadas, Sarnath, Kushinagar, Bhitargaon, Deogarh Dashavatara, Bhitari Skandagupta", ["lahuradewa", "koldihwa", "sanauli", "bhitargaon", "deogarh dashavatara", "bhitari"]),
    ("UP Medieval: Jaunpur Sharqi Shiraz-i-Hind, Agra capital, Fatehpur Sikri, Kalinjar Sher Shah, Awadh Saadat Khan Asaf-ud-Daula", ["jaunpur", "shiraz-i-hind", "fatehpur sikri", "kalinjar", "asaf-ud-daula"]),
    ("UP Modern: Meerut 1857, Begum Hazrat Mahal, Maulvi Ahmadullah, Aligarh AMU, Deoband, BHU Malaviya, Oudh Kisan Sabha, Eka Madari Pasi, AIKS 1936, HRA Kakori Bismil Ashfaqullah, Azad Alfred Park, Ballia Chittu Pandey", ["begum hazrat mahal", "deoband", "madari pasi", "kakori", "chittu pandey"]),
    ("UP Art/Culture: Atala Masjid Jaunpur, Bara Imambara Bhool Bhulaiya, Rumi Darwaza, Kathak Lucknow Gharana (Wajid Ali Shah, Birju Maharaj), Musical gharanas (Banaras, Kirana Bhimsen Joshi, Agra), Folk (Kajri, Alha, Nautanki, Ramlila), Kumbh Mela, GI crafts (Chikan, Moradabad brass, Khurja pottery)", ["atala masjid", "bara imambara", "bhool bhulaiya", "rumi darwaza", "kathak", "wajid ali shah", "birju maharaj", "kirana", "kajri", "alha", "nautanki", "kumbh mela", "moradabad"]),

    # Part B & Exam Tracks
    ("UPPSC vs UPSC Disparities & GS5/6", ["gs paper 5", "factual precision"]),
    ("UP RO/ARO Prelims/Mains: General Hindi 6 topics (Vilom, Vartani, Anek shabdon, Tatsam-Tadbhav, Visheshya-Visheshan, Paryayvachi), Patrachar Drafting, Saraniruparn", ["ro/aro", "vilom", "patrachar", "saraniruparn"]),
    ("RRB NTPC CBT-1 & CBT-2 Breakdown, CBAT Psychometric, Typing speed, Medical A-2", ["rrb ntpc", "cbt-1", "cbt-2", "cbat", "station master"])
]

all_text = (syl + cult + soc + up + prac + json.dumps(hist)).lower()

print(f"Total topics/concept bundles to verify: {len(topics)}")
missing = []
for title, keywords in topics:
    found_keys = [k for k in keywords if k.lower() in all_text]
    ratio = len(found_keys) / len(keywords)
    if ratio < 0.5:
        missing.append((title, keywords, found_keys))

print(f"\nMissing or low-coverage topics count: {len(missing)}")
for m in missing:
    print(f"LOW COVERAGE: {m[0]}")
    print(f"  Missing: {[k for k in m[1] if k not in m[2]]}")
