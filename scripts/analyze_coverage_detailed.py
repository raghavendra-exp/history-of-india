import re
import json

# Check syllabus.html
with open('syllabus.html', 'r', encoding='utf-8') as f:
    syl_text = f.read()

syl_cards = re.findall(r'id="(card-[^"]+)"', syl_text)
print(f"Total cards in syllabus.html: {len(syl_cards)}")
print("Cards:", syl_cards)

# Check history.json
with open('data/history.json', 'r', encoding='utf-8') as f:
    hist_data = json.load(f)

periods = hist_data.get('periods', [])
print(f"\nTotal periods in history.json: {len(periods)}")

# Topics from the user request
user_topics = [
    # Section 1: Ancient Indian History & Archaeology
    ("sec1-1", "Sources and Historiography (Archaeological, Epigraphy, Numismatics, Literary, Foreign Accounts, Historiographical schools)"),
    ("sec1-2", "Prehistoric and Proto-Historic Eras (Palaeolithic, Mesolithic, Neolithic Revolution, Chalcolithic)"),
    ("sec1-3", "Indus Valley Civilization (Origins, Geography, Town planning, Economy, Society, Religion, Decline)"),
    ("sec1-4", "The Vedic Period (Early Vedic & Later Vedic, Polity, Society, Economy, Religion, Upanishads)"),
    ("sec1-5", "Mahajanapadas and Second Urbanization (16 Mahajanapadas, Magadhan hegemony, Haryanka/Shishunaga/Nanda, Persian & Alexander invasions)"),
    ("sec1-6", "Heterodox Religious Movements (Buddhism, Jainism, Councils, Sects, Ajivikas, Charvakas)"),
    ("sec1-7", "The Mauryan Empire (Chandragupta, Kautilya, Ashoka Dhamma, Administration, Saptanga, Sitadhyaksha, Decline)"),
    ("sec1-8", "The Post-Mauryan Period (Shungas, Kanvas, Satavahanas, Indo-Greeks, Shakas, Kushanas, Sangam Age, Tinai)"),
    ("sec1-9", "The Gupta and Vakataka Era (Samudragupta, Chandragupta II, Administration, Samantas, Golden Age debate, Vakatakas)"),
    ("sec1-10", "Post-Gupta Transition & Early Medieval (Harshavardhana, Pallavas, Chalukyas of Badami, Tripartite Struggle, Imperial Cholas)"),

    # Section 2: Medieval Indian History
    ("sec2-1", "Early Medieval India (Indian Feudalism, Rajputs, Arab conquest of Sindh, Mahmud Ghazni, Muhammad Ghori)"),
    ("sec2-2", "The Delhi Sultanate (Mamluk, Khalji market reforms, Tughlaq experiments, Sayyid, Lodi, Administration, Iqta)"),
    ("sec2-3", "Regional Kingdoms 14th-15th C (Vijayanagara Empire, Nayankara/Ayagar, Bahmani, Deccan Sultanates, Talikota)"),
    ("sec2-4", "The Mughal Empire (Babur, Sur Interregnum, Akbar Mansabdari/Dahsala/Sulh-i-kul, Jahangir, Shah Jahan, Aurangzeb)"),
    ("sec2-5", "Decline of Mughals & Rise of Marathas (Shivaji, Hindavi Swarajya, Ashta Pradhan, Chauth/Sardeshmukhi, Peshwas, Panipat 1761)"),

    # Section 3: Modern Indian History
    ("sec3-1", "The 18th-Century Transition (Successor states Bengal/Awadh/Hyderabad, Anglo-French Carnatic wars)"),
    ("sec3-2", "British Expansion & Consolidation (Plassey, Buxar, Dual Govt, Anglo-Mysore, Anglo-Maratha, Anglo-Sikh, Subsidiary Alliance, Doctrine of Lapse)"),
    ("sec3-3", "Economic Impact of Colonial Rule (R.P. Dutt 3 phases, Permanent/Ryotwari/Mahalwari, Commercialization, De-industrialization, Drain of Wealth)"),
    ("sec3-4", "Administrative & Constitutional Evolution (Regulating Act 1773 to Charter Acts, Police/Judicial, Macauley education, Wood's Despatch)"),
    ("sec3-5", "Early Resistance & Revolt of 1857 (Civil/Peasant/Tribal rebellions, 1857 causes, leaders, failure, 1858 Act, Peel Commission)"),
    ("sec3-6", "Socio-Religious Reform Movements (Brahmo, Arya, Aligarh, Phule, Vidyasagar, Vivekananda, Ambedkar, Periyar)"),
    ("sec3-7", "The Indian National Movement (Moderate 3Ps, Extremist Lal-Bal-Pal, Swadeshi, Surat split, Home Rule, Gandhian era, NCM, CDM, QIM, INA, Partition)"),

    # Section 4: Post-Independence Consolidation
    ("sec4-1", "Nation-Building & Integration (Partition rehabilitation, Princely States integration Patel/Menon, Linguistic reorganization, Tribal Panchsheel)"),
    ("sec4-2", "Institutional Framework & Economic Policy (Constitution, Planning Commission, Mahalanobis heavy industry, Land reforms, Green Revolution)"),
    ("sec4-3", "Foreign Policy & Political Crises (NAM, Panchsheel, 1962 Sino-Indian, 1965/1971 Indo-Pak, The Emergency 1975-77)"),

    # Section 5: World History
    ("sec5-1", "Enlightenment & Age of Revolutions (Locke/Rousseau, Industrial Revolution, American Revolution 1776, French Revolution 1789)"),
    ("sec5-2", "Nationalism & Imperialism (Unification of Italy, Unification of Germany, Scramble for Africa, Imperialism in Asia/China)"),
    ("sec5-3", "The World Wars Era (WWI, Treaty of Versailles, Russian Revolution 1917, Interwar Fascism/Nazism, WWII)"),
    ("sec5-4", "Post-WWII Dynamics (Cold War, Decolonization Third World, Disintegration of USSR 1991)"),

    # Section 6: Art & Culture
    ("sec6-1", "Epigraphic & Numismatic Art Traditions (Evolution of scripts, Coin portraits, Religious motifs)"),
    ("sec6-2", "Temple Architecture Structural Metrics (Nagara, Dravida, Vesara, Khajuraho, Solanki, Odisha, Hoysala)"),
    ("sec6-3", "Indo-Islamic & Syncretic Engineering (Trabeate to Arcuate, Pietra Dura, Jali, Charbagh, Double-dome)"),
    ("sec6-4", "Philosophical & Intangible Heritage (Six schools of philosophy, Shankara/Ramanuja/Madhva, UNESCO ICH list)"),

    # Part A: UP State Specific
    ("partA-1", "UP Ancient & Prehistoric (Belan Valley, Lahuradewa/Koldihwa, Alamgirpur, Sanauli, 8 Mahajanapadas in UP, Sarnath/Kushinagar)"),
    ("partA-2", "UP Medieval History (Jaunpur Sharqi Shiraz-e-Hind, Agra Mughal capital, Fatehpur Sikri, Sher Shah Kalinjar, Awadh Nawabs)"),
    ("partA-3", "UP Modern History & Freedom Struggle (1857 epicentres Meerut/Lucknow/Kanpur/Jhansi, Aligarh/Deoband, Kisan Sabha, HRA/Kakori, Ballia 1942)"),
    ("partA-4", "UP Art, Culture, Architecture & Festivals (Sarnath/Jaunpur/Mughal/Awadh architecture, Kathak Lucknow Gharana, Music gharanas, Folk arts, Kumbh Mela, GI crafts)"),

    # Part B & Exam Tracks
    ("partB-1", "UPPSC vs UPSC Critical Disparities & Exam Strategy"),
    ("partB-2", "UP RO/ARO Prelims & Mains Syllabus (General Hindi 60 marks, Patrachar Drafting, Essay)"),
    ("partB-3", "RRB NTPC CBT-1 & CBT-2 Stage Breakdown & Civil Services Comparison")
]

print("\n--- Check Presence in syllabus.html ---")
missing_in_syl = []
for cid, title in user_topics:
    # check if card exists
    found = False
    for sc in syl_cards:
        if cid in sc or sc in cid:
            found = True
            break
    if not found:
        # check text
        if cid.replace('-', '_') in syl_text or cid in syl_text:
            found = True
    if not found:
        missing_in_syl.append((cid, title))

print(f"Missing in syllabus.html: {len(missing_in_syl)}")
for m in missing_in_syl:
    print(f"  - {m[0]}: {m[1]}")
