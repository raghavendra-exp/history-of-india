import json

with open('data/history.json', 'r', encoding='utf-8') as f:
    hdata = json.load(f)

periods = hdata['periods']
period_map = {p['id']: p for p in periods}

# 1. Indus Valley Civilization
p_ivc = period_map.get('indus-valley-civilization')
if p_ivc:
    p_ivc.setdefault('aspects', {})
    p_ivc['aspects']['Visual Art, Sculpture & Craft Metallurgic Mastery (Ishani Pandya Compendium)'] = [
        "Lost-Wax Bronze Casting (Cire Perdue): The bronze 'Dancing Girl' from Mohenjo-daro (~2500 BCE) exemplifies advanced metallurgical mastery — standing in an expressive Tribhanga-like posture with her right hand on her hip and left arm covered in bangles made of bone/shell.",
        "Stone & Terracotta Sculpture: The bearded Priest-King in steatite adorned with a trefoil patterned shawl draped over the left shoulder; alongside hand-pinched terracotta figurines of the Mother Goddess adorned with fan-shaped headdresses and heavy waist ornaments.",
        "Seals & Steatite Glyptic Art: Square steatite seals featuring intaglio carvings of animals (the unicorn bull, humped bull, tiger, elephant) and the celebrated Pashupati Seal (seated horned deity in yogic posture surrounded by elephant, tiger, rhino, buffalo, and two antelopes beneath the seat).",
        "Pottery & Bead Industry: Fine wheel-made red pottery painted with glossy black geometric designs, pipal leaves, and intersecting circles; alongside specialized lapidary factories at Chanhudaro and Lothal producing drilled carnelian, lapis lazuli, and steatite micro-beads for international export to Dilmun (Bahrain) and Magan (Oman)."
    ]
    print("Enriched indus-valley-civilization with culture notes")

# 2. Mauryan Empire & Ashoka
p_mau = period_map.get('mauryan-empire')
if p_mau:
    p_mau.setdefault('aspects', {})
    p_mau['aspects']['Mauryan Court Art vs. Popular Folk Art (Ishani Pandya Compendium)'] = [
        "Court Art (Monolithic Pillars & Palaces): Ashokan pillars carved from single shafts of buff Chunar sandstone with a distinctive glassy Mauryan polish; crowned by animal capitals (Sarnath Lion Capital with dharmachakra, Lauriya Nandangarh lion, Rampurva zebu bull). In contrast to Persian Achaemenian pillars (which were constructed of segmented stone drums and formed part of palace halls), Ashokan pillars were free-standing imperial epigraphic edicts.",
        "Imperial Palaces: Megasthenes and Faxian marveled at the monumental hypostyle wooden palace of Chandragupta Maurya at Kumrahar (Patna), featuring 80 carved stone pillars modeled on the Achaemenian Hall of Hundred Columns at Persepolis.",
        "Popular Art (Yaksha-Yakshi Sculptures): Monumental freestanding stone figures produced by independent artisan guilds for popular fertility cults — notably the polished sandstone Didarganj Yakshini (Patna) holding a flywhisk (chauri), the Besnagar Yakshi, and the Parkham Yaksha.",
        "Rock-Cut Cave Excavations: The earliest surviving rock-cut architecture in India — the Barabar and Nagarjuni caves (Bihar) excavated by Ashoka and Dasharatha for Ajivika ascetics; the Lomas Rishi cave façade features the earliest ornamental wooden-style horseshoe Chaitya arch carved into live granite."
    ]
    print("Enriched mauryan-empire with culture notes")

# 3. Post-Mauryan Period
p_pm = period_map.get('post-mauryan-period')
if p_pm:
    p_pm.setdefault('aspects', {})
    p_pm['aspects']['The Three Great Sculptural Schools: Gandhara, Mathura & Amaravati'] = [
        "Gandhara School: Flourished in northwestern India (Taxila, Peshawar, Bamiyan) under the Kushanas; Greco-Roman Hellenistic synthesis; utilized grey/bluish schist stone and stucco; characterized by realistic human musculature, wavy curly hair, sharp facial contours, deep toga-like drapery folds, and Buddha depicted with Apollo-like facial beauty in serene dhyana meditation.",
        "Mathura School: Flourished along the Yamuna basin in Uttar Pradesh under the Kushanas; purely indigenous Indian tradition; crafted from spotted red sandstone; Buddha depicted with broad masculine shoulders, transparent muslin drapery clinging to the torso, right hand raised in Abhaya Mudra, and a tranquil smiling countenance; simultaneously pioneered Hindu deities (Vishnu, Shiva, Surya) and Jain Ayagapatas.",
        "Amaravati School: Flourished in the Krishna-Godavari valley (Andhra Pradesh) under Satavahana and Ikshvaku patronage; sculpted in white crystalline limestone/marble; prioritized dynamic narrative relief panels on stupas (Jataka narratives) filled with human emotion, ecstatic movement, and graceful Tribhanga postures rather than individual statues."
    ]
    print("Enriched post-mauryan-period with culture notes")

# 4. Gupta Age
p_gup = period_map.get('gupta-age')
if p_gup:
    p_gup.setdefault('aspects', {})
    p_gup['aspects']['The Golden Age of Classical Temple Architecture & Ajanta Murals'] = [
        "Genesis of the Hindu Temple: The Guptas transitioned Indian temple architecture from flat-roofed single-cell shrines (Temple 17 at Sanchi) to covered circumambulatory paths (Nachna Kuthara) and the classic Panchayatana layout (main shrine surrounded by four subsidiary shrines) exemplified by the 6th c. Dashavatara Temple at Deogarh (Jhansi, featuring the Sheshashayi Vishnu relief) and the Bhitargaon terracotta brick temple (Kanpur).",
        "Ajanta Caves Tempera Murals: 29 rock-cut Buddhist caves in Maharashtra; paintings executed using tempera technique (fresco secco on a layered clay-cowdung-lime ground); famous for the exquisite emotional depth and graceful hand mudras of Bodhisattva Padmapani (lotus bearer) and Bodhisattva Vajrapani (Cave 1), the Dying Princess (Cave 16), and celestial flying Apsaras.",
        "Classical Sanskrit Golden Age: The zenith of courtly Kavya and drama led by Kalidasa (Abhijnanashakuntalam, Meghaduta, Raghuvamsha), Vishakhadatta (Mudrarakshasa), Shudraka (Mrichchhakatika), and the scientific treatises of Aryabhata (Aryabhatiya) and Varahamihira (Brihat Samhita)."
    ]
    print("Enriched gupta-age with culture notes")

# 5. Kingdoms of South
p_ks = period_map.get('kingdoms-of-south')
if p_ks:
    p_ks.setdefault('aspects', {})
    p_ks['aspects']['South Indian Temple Architecture & Chola Lost-Wax Bronzes'] = [
        "Pallava Rock-Cut to Structural Evolution: Transitioned from Mahendra style rock-cut pillared mandapas to Mamalla style monolithic Five Rathas (Pancha Pandava Rathas at Mahabalipuram) and Rajasimha style structural masonry temples (Shore Temple at Mahabalipuram and Kailasanathar Temple at Kanchipuram).",
        "Chola Architectural & Metallurgical Zenith: Rajaraja I built the colossal Brihadisvara Temple at Thanjavur (1010 CE), featuring an astounding 66-meter high pyramidal Vimana crowned by an 80-tonne monolithic granite cupola; Rajendra I mirrored this at Gangaikonda Cholapuram. In sculpture, Chola lost-wax bronzes attained world renown, personified by the cosmic Nataraja (Shiva dancing the Ananda Tandava within a flaming prabhavali, crushing the demon of ignorance Apasmara beneath his right foot).",
        "Vijayanagara Grandeur: Monumental temple complexes featuring towering Raya Gopurams, intricately sculpted Kalyana Mandapas (marriage halls with carved yali pillars), musical granite pillars, and stone chariot shrines (Vittala and Hazara Rama temples at Hampi)."
    ]
    print("Enriched kingdoms-of-south with culture notes")

# 6. Mughal Empire
p_mu = period_map.get('mughal-empire')
if p_mu:
    p_mu.setdefault('aspects', {})
    p_mu['aspects']['Mughal Miniature Paintings & Architectural Synthesis'] = [
        "Mughal Miniature Evolution: Humayun brought Persian masters Mir Sayyid Ali and Abdus Samad from Safavid Tabriz. Akbar established the royal Tasvir Khana, overseeing vast collaborative manuscripts (Hamzanama on cloth, Razmnama Persian translation of Mahabharata). Jahangir shifted the atelier towards supreme naturalism, individual royal portraiture, halos, and scientific animal/botanical studies by Ustad Mansur ('Siberian Crane', 'Zebra'). Shah Jahan introduced formal imperial durbars with radiant lapis and burnished gold leaf borders.",
        "Indo-Islamic Architectural Masterpieces: Synthesized Persian arcuate engineering (true arch, bulbous double dome, Charbagh quadripartite garden layout) with indigenous Indian stone carving, trabeate brackets, and jali lattices. Exemplified by Humayun's Tomb (precursor to Taj Mahal), Akbar's red sandstone Fatehpur Sikri (Buland Darwaza, Panch Mahal), Itmad-ud-Daulah's tomb (introducing extensive white marble pietra dura inlay), and Shah Jahan's Taj Mahal (the jewel of symmetrical Indo-Islamic architecture)."
    ]
    print("Enriched mughal-empire with culture notes")

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(hdata, f, ensure_ascii=False, indent=2)

print("Successfully enriched data/history.json with culture aspects!")
