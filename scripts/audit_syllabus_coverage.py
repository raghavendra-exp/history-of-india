import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'C:\Users\ragha\.gemini\antigravity\scratch\history-of-india'
target_files = [
    'syllabus.html',
    'art-culture.html',
    'up-history.html',
    'data/history.json',
    'data/mains-questions.json'
]

file_texts = {}
for rel_path in target_files:
    full_path = os.path.join(base_dir, rel_path)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            file_texts[rel_path] = f.read().lower()

combined_text = ' '.join(file_texts.values())

terms_by_category = {
    "Archaeology & Sources": [
        'Sanauli', 'Baghpat', 'Lahuradewa', 'Koldihwa', 'Chopani Mando', 'Attirampakkam', 'Hunsgi', 'Soan',
        'Ahar-Banas', 'Kayatha', 'Malwa', 'Jorwe', 'Inamgaon', 'Daimabad',
        'Prayag Prashasti', 'Aihole', 'Rudradaman', 'Junagadh', 'Mortimer Wheeler'
    ],
    "Ancient Polity & Philosophy": [
        'Rathamusala', 'Mahashilakantaka', 'Bimbisara', 'Ajatashatru', 'Mahapadma Nanda',
        'Anguttara Nikaya', 'Makkhali Gosala', 'Charvaka', 'Lokayata', 'Anekantavada', 'Syadvada',
        'Sitadhyaksha', 'Dhamma Mahamatta', 'Samaharta', 'Sannidhata', 'Gudha Purusha',
        'Uttiramerur', 'Kudavolai', 'Tripartite Struggle', 'Pulakeshin',
        'Samkhya', 'Yoga', 'Nyaya', 'Vaisheshika', 'Mimamsa', 'Advaita', 'Vishishtadvaita', 'Dvaita'
    ],
    "Medieval Systems": [
        'Sarai-i-Adl', 'Shahna-i-Mandi', 'Masahat', 'Diwan-i-Kohi', 'Sondhar', 'Turkan-i-Chahalgani',
        'Ashta Pradhan', 'Chauth', 'Sardeshmukhi', 'Nayankara', 'Ayagar',
        'Tulughma', 'Sadak-e-Azam', 'Dahsala', 'Zabt', 'Polaj', 'Parauti', 'Chachar', 'Banjar',
        'Sulh-i-kul', 'Mazhar', 'Din-i-Ilahi'
    ],
    "Modern & Freedom Movement": [
        'Drain of Wealth', 'Home Charges', 'Sunset Law', 'Holt Mackenzie', 'Merttins Bird',
        'Sanyasi Rebellion', 'Chuar', 'Kol Insurrection', 'Santhal Hool', 'Munda Ulgulan',
        'Peel Commission', 'Lex Loci', 'General Service Enlistment',
        'Satyashodhak', 'Gulamgiri', 'Young Bengal', 'Henry Vivian Derozio', 'Self-Respect',
        'Komagata Maru', 'Tinkathia', 'Chittagong Armoury', 'Surya Sen',
        'Dharasana', 'Vedaranyam', 'Khudai Khidmatgar', 'Poona Pact',
        'Tamluk', 'Satara', 'Ballia', 'Chittu Pandey', 'Aruna Asaf Ali', 'Usha Mehta', 'RIN Mutiny'
    ],
    "Post-Independence & World History": [
        'Dhar Commission', 'JVP Committee', 'Fazl Ali', 'Potti Sreeramulu',
        'Mahalanobis', 'Bandung', 'Panchsheel', 'Navnirman',
        'Three Estates', 'Robespierre', 'Waterloo', 'Cavour', 'Garibaldi', 'Bismarck',
        'Berlin Conference', 'Opium Wars', 'Boxer Rebellion',
        'Sarajevo', 'Triple Entente', 'Bolshevik', 'Stalinist', 'Lebensraum', 'Appeasement',
        'Stalingrad', 'Truman Doctrine', 'Warsaw Pact', 'Glasnost', 'Perestroika'
    ],
    "Art & Architecture Metrics": [
        'Rekha-Prasada', 'Phamsana', 'Valabhi', 'Amalaka', 'Kalasha', 'Upapitha', 'Prakara',
        'Kalyana Mandapa', 'Pushkarini', 'Modhera', 'Surya Kund', 'Deul', 'Jagamohana',
        'Hoysala', 'Soapstone', 'Stellate', 'Trabeate', 'Arcuate', 'Voussoir', 'Keystone',
        'Pietra Dura', 'Jali', 'Charbagh',
        'Kutiyattam', 'Ramman', 'Mudiyettu', 'Kalbelia', 'Chhau', 'Sankirtana', 'Jandiala Guru',
        'Nowruz', 'Kumbh Mela', 'Durga Puja'
    ],
    "UP State History & Culture": [
        'Sharqi', 'Shiraz of the East', 'Kalinjar', 'Asaf-ud-Daula', 'Ganga-Jamuni', 'Rohillas',
        'Khan Bahadur Khan', 'Maulvi Liaquat Ali', 'Maulvi Ahmadullah', 'Shah Mal',
        'Darul Uloom', 'Bharat Dharma Mahamandala', 'Oudh Kisan Sabha', 'Baba Ramchandra',
        'Eka Movement', 'Madari Pasi', 'All India Kisan Sabha', 'Swami Sahajanand',
        'Atala Masjid', 'Lal Darwaza', 'Bhool Bhulaiya', 'Rumi Darwaza',
        'Lucknow Gharana', 'Banaras Gharana', 'Kirana Gharana', 'Agra Gharana',
        'Girija Devi', 'Bismillah Khan', 'Samta Prasad', 'Bhimsen Joshi', 'Faiyyaz Khan',
        'Kajri', 'Chaiti', 'Alha', 'Hori', 'Rasiya', 'Birha', 'Nautanki', 'Ramlila', 'Raslila',
        'Bateshwar', 'Deva Sharif', 'Shakumbhari Devi', 'Nauchandi', 'Chikan', 'Zardozi',
        'Moradabad', 'Khurja'
    ],
    "Exam Specific Modules": [
        'Saraniruparn', 'Patrachar', 'CBAT', 'Typing Skill Test'
    ]
}

print("=== SYLLABUS TOPIC COVERAGE AUDIT ===")
total_tested = 0
total_found = 0
for cat, terms in terms_by_category.items():
    print(f"\n--- Category: {cat} ---")
    cat_missing = []
    for t in terms:
        total_tested += 1
        if t.lower() in combined_text:
            total_found += 1
        else:
            cat_missing.append(t)
    if cat_missing:
        print(f"Missing ({len(cat_missing)}/{len(terms)}): {', '.join(cat_missing)}")
    else:
        print(f"ALL {len(terms)} terms PRESENT!")

print(f"\nOverall Coverage: {total_found}/{total_tested} ({total_found*100.0/total_tested:.1f}%)")
