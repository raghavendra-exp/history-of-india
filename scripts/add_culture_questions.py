# -*- coding: utf-8 -*-
import json
import sys

# Configure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 36 HIGH-YIELD PRELIMS QUESTIONS (Culture & Sociology)
# ==============================================================================
new_prelims = [
    # 1. Indus Art & Metallurgy
    {
        "id": "prelims-cult-001",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L1; Upinder Singh, Ch. 4",
        "question": "Regarding the artistic traditions of the Indus Valley Civilisation, consider the following statements:\n1. The bronze 'Dancing Girl' from Mohenjo-daro was cast using the 'lost-wax' (cire perdue) technique.\n2. The steatite bust of the 'Priest-King' depicts a trefoil floral motif embroidered on his shawl draped over the left shoulder.\n3. Harappan pottery was predominantly hand-made and devoid of any painted geometric decorations.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 0,
        "explanation": "Statements 1 and 2 are correct: The bronze 'Dancing Girl' was created using the lost-wax casting method, showcasing advanced Harappan metallurgy. The 'Priest-King' bust in steatite is draped in a shawl with trefoil motifs over the left shoulder. Statement 3 is incorrect because Harappan pottery was predominantly wheel-thrown fine red ware painted with glossy black geometric patterns, pipal leaves, and intersecting circles.",
        "trap": "Beware of extreme words like 'predominantly hand-made' — Harappan pottery was exceptionally sophisticated wheel-made pottery.",
        "topperTip": "Lost-wax bronze casting is still practiced today by traditional Dokra artisans in Bastar and West Bengal, proving 4,500 years of living technological continuity."
    },
    # 2. Ashokan Pillars vs Achaemenian Pillars
    {
        "id": "prelims-cult-002",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L1; Nitin Singhania, Ch. 1",
        "question": "With reference to the architectural differences between Mauryan Ashokan pillars and Persian Achaemenian pillars, which of the following is correct?",
        "options": [
            "Ashokan pillars were constructed from multiple segmented stone drums cemented together, whereas Persian pillars were monolithic shafts.",
            "Ashokan pillars were free-standing imperial edicts erected in open public grounds, whereas Persian pillars were structural components of palace halls.",
            "Ashokan pillars carried bell-shaped capitals with inverted lotuses derived exclusively from Greek Corinthian orders.",
            "Persian pillars bore inscriptions addressed directly to the common public in Kharosthi script, unlike Ashokan edicts."
        ],
        "correctIndex": 1,
        "explanation": "Option B is correct: Ashokan pillars were monolithic free-standing commemorative and ethical monuments erected across public routes, whereas Achaemenian (Persepolitan) pillars were constructed from multiple stone drums and served structural functions supporting palace hypostyle roofs. Ashokan shafts are single blocks of Chunar sandstone.",
        "trap": "Don't confuse monolithic shafts (Ashokan) with segmented drum columns (Achaemenian).",
        "topperTip": "Ashokan pillars do not have a base, tapering directly from the ground to the capital, whereas Persian pillars rested on elaborate bell-shaped or tiered bases."
    },
    # 3. Barabar Caves & Lomas Rishi
    {
        "id": "prelims-cult-003",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE 2013 / Re-engineered",
        "bookRef": "Ishani Pandya Compendium L1; A.L. Basham, Ch. 3",
        "question": "With reference to the rock-cut Barabar Caves in Bihar, consider the following statements:\n1. They were originally excavated by Emperor Ashoka and his grandson Dasharatha for monks belonging to the Ajivika sect.\n2. The façade of the Lomas Rishi Cave features a carved horseshoe-shaped Chaitya arch replicating contemporary timber architecture.\n3. The interiors of the caves exhibit the glassy 'Mauryan polish' on granite rock surfaces.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 3,
        "explanation": "All three statements are correct: The Barabar (Ashoka) and Nagarjuni (Dasharatha) caves were excavated for Ajivika ascetics (founded by Makkhali Gosala). The Lomas Rishi Cave façade has a decorative semicircular chaitya horseshoe arch with a frieze of elephants, directly replicating wooden barrel-vault beam architecture, and possesses the celebrated mirror-like Mauryan polish.",
        "trap": "Many candidates assume Barabar caves were exclusively Buddhist, whereas their epigraphs explicitly dedicate them to the Ajivikas.",
        "topperTip": "The Ajivika sect believed in strict determinism (Niyati) and was one of the foremost heterodox Shramana traditions of the 6th-3rd century BCE."
    },
    # 4. Didarganj Yakshini
    {
        "id": "prelims-cult-004",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L1; Upinder Singh, Ch. 7",
        "question": "The celebrated Didarganj Yakshini, discovered near Patna and datable to the Mauryan/Post-Mauryan period, is distinguished by which of the following artistic attributes?",
        "options": [
            "Carved in grey schist stone holding an alms bowl with Hellenistic facial contours",
            "Carved from polished buff sandstone holding a flywhisk (chauri) in her right hand",
            "Sculpted in white spotted limestone seated in dynamic dancing tribhanga posture",
            "A bronze lost-wax image adorned with a high tiered crown holding a lotus bud"
        ],
        "correctIndex": 1,
        "explanation": "Option B is correct: The life-sized Didarganj Yakshini (now in Patna Museum) is carved from polished buff Chunar sandstone, holds a flywhisk (chauri) in her right hand, features voluptuous proportions symbolizing fertility and abundance, and possesses the mirror-like Mauryan polish.",
        "trap": "Grey schist is the signature material of Gandhara art, not Mauryan popular sculpture.",
        "topperTip": "Yakshas and Yakshinis represent popular/folk indigenous fertility cults that were later absorbed into Buddhist, Jain, and Hindu iconography."
    },
    # 5. Gandhara vs Mathura vs Amaravati
    {
        "id": "prelims-cult-005",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L1; Nitin Singhania, Ch. 2",
        "question": "Which of the following pairs of ancient Indian sculptural schools and their primary raw materials is/are correctly matched?\n1. Gandhara School — Grey/bluish schist stone and stucco\n2. Mathura School — Spotted red sandstone\n3. Amaravati School — White crystalline limestone\nSelect the correct answer using the code given below:",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 3,
        "explanation": "All three pairs are correctly matched: Gandhara School used grey/bluish schist and stucco (plaster); Mathura School predominantly used indigenous spotted red sandstone from Sikri; Amaravati School in the Krishna-Godavari valley utilized white crystalline limestone (often called Palnad marble).",
        "trap": "Don't confuse the materials: Schist = Gandhara, Red Sandstone = Mathura, White Limestone = Amaravati.",
        "topperTip": "While Gandhara was heavily influenced by Greco-Roman Hellenistic aesthetics, Mathura was purely indigenous and pioneered images of both the Buddha and Hindu deities simultaneously."
    },
    # 6. Ajanta vs Ellora Caves
    {
        "id": "prelims-cult-006",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE 2015 / Re-engineered",
        "bookRef": "Ishani Pandya Compendium L2; A.L. Basham, Ch. 8",
        "question": "Regarding the rock-cut cave complexes of Western India, consider the following statements:\n1. Ajanta caves consist exclusively of Buddhist shrines and monasteries, whereas Ellora caves encompass Buddhist, Brahmanical, and Jain excavations.\n2. Ajanta murals were painted using true Italian 'buon fresco' on wet lime plaster.\n3. The monolithic rock-cut Kailash Temple at Ellora (Cave 16) was excavated from top to bottom by Rashtrakuta King Krishna I.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 1,
        "explanation": "Statements 1 and 3 are correct: Ajanta (29 caves) is purely Buddhist (Hinayana & Mahayana phases). Ellora (34 caves) represents Buddhist (1-12), Hindu/Brahmanical (13-29), and Jain (30-34) traditions. Cave 16 (Kailasanatha) is a top-down cliff excavation under Rashtrakuta Krishna I. Statement 2 is incorrect because Ajanta paintings are tempera (fresco secco) on a dry surface coated with clay, cow dung, straw, and fine gypsum/lime ground, not true wet buon fresco.",
        "trap": "Ajanta paintings are NOT 'buon fresco' (wet plaster); they are tempera on dry ground.",
        "topperTip": "The famous Bodhisattva Padmapani and Vajrapani are located in Cave 1 of Ajanta, datable to the Vakataka period (5th century CE)."
    },
    # 7. Kailash Temple Ellora
    {
        "id": "prelims-cult-007",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L2; Satish Chandra, Ch. 2",
        "question": "The Kailash Temple at Ellora (Cave 16) is celebrated as a pinnacle of ancient Indian rock-cut engineering because:",
        "options": [
            "It was built using segmented granite blocks transported across 100 miles using wooden rollers.",
            "It was carved monolithically from a single basalt volcanic cliff face using vertical top-down quarrying without structural jointing.",
            "It features the earliest surviving brick shikhara crowned by an amalaka and kalasha.",
            "It was the first structural temple dedicated jointly to Shiva, Vishnu, and the Jinas."
        ],
        "correctIndex": 1,
        "explanation": "Option B is correct: Kailash Temple (Cave 16) was sculpted out of a single volcanic basalt cliff at Ellora by excavating downward from the top of the hill, removing an estimated 200,000 tonnes of rock without any scaffolding or assembled joints. It is dedicated to Lord Shiva.",
        "trap": "It is NOT a structural temple built from blocks; it is an entirely monolithic rock-hewn marvel.",
        "topperTip": "The chief sculptor is recorded in tradition to have exclaimed in awe upon its completion: 'Oh, how was it that I built it?'"
    },
    # 8. Gupta Temple Architecture
    {
        "id": "prelims-cult-008",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L2; Upinder Singh, Ch. 9",
        "question": "Which of the following represents the correct sequence in the architectural evolution of the freestanding Hindu temple during the Gupta period?",
        "options": [
            "Flat-roofed square sanctum with shallow portico -> Covered circumambulatory path (pradakshinapatha) -> Addition of curvilinear shikhara on raised plinth -> Complete Panchayatana layout",
            "Curvilinear shikhara -> Flat-roofed sanctum -> Hypostyle mandapa -> Gopuram",
            "Panchayatana layout -> Monolithic rock-cut ratha -> Trabeate cave shrine -> Double dome",
            "Pillared cloister -> Circular chaitya hall -> Trabeate entrance -> Miniature vimana"
        ],
        "correctIndex": 0,
        "explanation": "Option A is correct: Gupta temple architecture progressed through four key stages: Stage 1: Flat-roofed square sanctum with a shallow 4-pillared portico (Temple 17 at Sanchi). Stage 2: Covered circumambulatory path (pradakshinapatha) around the garbhagriha (Parvati temple at Nachna Kuthara). Stage 3: Low curvilinear shikhara built on a raised platform (Dashavatara Temple at Deogarh). Stage 4: Comprehensive Panchayatana layout with 4 subsidiary shrines.",
        "trap": "Gopurams belong to South Indian Dravidian architecture (Pallava/Chola/Vijayanagara), not Gupta temples.",
        "topperTip": "The Dashavatara temple at Deogarh (Jhansi district, UP) features the iconic Sheshashayi Vishnu carving on its outer wall."
    },
    # 9. Nagara vs Dravida vs Vesara
    {
        "id": "prelims-cult-009",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE 2012 / Re-engineered",
        "bookRef": "Ishani Pandya Compendium L2; Nitin Singhania, Ch. 3",
        "question": "In the context of traditional Indian temple architecture, how does the Dravida style distinctly differ from the Nagara style?",
        "options": [
            "Dravida temples lack enclosed boundary walls and water tanks, whereas Nagara temples always possess fortified prakaras.",
            "The tower above the sanctum in Dravida temples is a stepped pyramid (Vimana), whereas in Nagara temples it is a curving spire (Shikhara) crowned by an Amalaka.",
            "Dravida temples place the deity directly under a flat roof, whereas Nagara temples use bulbous double domes.",
            "Nagara temples feature towering entry gateways called Gopurams, which are absent in Dravida temples."
        ],
        "correctIndex": 1,
        "explanation": "Option B is correct: In Dravida architecture, the tower over the garbhagriha is a stepped pyramid rising linearly called a 'Vimana' crowned by a domical octagonal or circular shikhara (stupika). In Nagara architecture, the tower is a beehive-shaped curving spire (Shikhara/Rekha-Prasad) crowned by a grooved stone disk (Amalaka) and Kalasha. Also, Dravida temples are enclosed within high boundary walls (Prakara) with colossal Gopurams and sacred water tanks (Kalyani), which Nagara temples generally lack.",
        "trap": "Gopurams belong to Dravida temples, NOT Nagara temples. In Nagara, the main shikhara is the tallest component.",
        "topperTip": "Vesara (or Karnataka Dravida) style developed under Chalukyas and Hoysalas, synthesizing elements of both Nagara and Dravida traditions."
    },
    # 10. Chola Bronzes & Nataraja
    {
        "id": "prelims-cult-010",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE 2019 / Re-engineered",
        "bookRef": "Ishani Pandya Compendium L2; A.L. Basham, Ch. 8",
        "question": "Regarding the iconic Chola bronze sculpture of Nataraja (Dancing Shiva), which of the following symbolic interpretations is NOT correct?",
        "options": [
            "The upper right hand holds the Damaru (drum), symbolizing the sound of creation (Srishti).",
            "The upper left hand holds Agni (flame of destruction), symbolizing cosmic dissolution (Samhara).",
            "The right foot crushes the dwarf demon Apasmara Purusha, symbolizing the subjugation of spiritual ignorance.",
            "The lower left hand is raised in Abhaya Mudra, symbolizing fearlessness and royal sovereignty."
        ],
        "correctIndex": 3,
        "explanation": "Option D is incorrect (and hence the correct answer to the question): The LOWER RIGHT hand is raised in Abhaya Mudra (granting protection and freedom from fear). The LOWER LEFT hand points downward across the torso towards the raised left foot in Gajahasta Mudra, signifying the path of spiritual liberation (Moksha/Anugraha).",
        "trap": "Pay close attention to right hand vs. left hand mudras in Nataraja iconography.",
        "topperTip": "Nataraja dances within a flaming aureole (Prabhavali), which represents the cyclical cosmic rhythm of the universe."
    },
    # 11. Indo-Islamic Architectural Elements
    {
        "id": "prelims-cult-011",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L2; Satish Chandra, Ch. 12",
        "question": "Consider the following architectural techniques:\n1. Arcuate engineering utilizing the true keystone arch and mortar\n2. Double dome design to balance interior acoustic volume with exterior monumentality\n3. Pietra dura inlay of semi-precious stones in marble\n4. Trabeate lintel and corbelled bracket construction\nWhich of the above were introduced into Indian architecture during the Delhi Sultanate and Mughal periods?",
        "options": [
            "1, 2 and 3 only",
            "2, 3 and 4 only",
            "1, 3 and 4 only",
            "1, 2, 3 and 4"
        ],
        "correctIndex": 0,
        "explanation": "Statements 1, 2, and 3 were introduced by the Islamic dynasties (Arcuate true arch/dome by Delhi Sultanate; double dome seen first in Sikandar Lodi's tomb and perfected in Humayun's tomb; pietra dura brought to zenith by Jahangir and Shah Jahan). In contrast, Statement 4 (Trabeate post-and-lintel and corbelled brackets) was the traditional indigenous Indian Hindu architectural method.",
        "trap": "Trabeate architecture is indigenous Indian (Hindu/Jain), not an Islamic import.",
        "topperTip": "Akbar's buildings at Fatehpur Sikri deliberately synthesised Islamic arcuate geometry with Rajasthani and Gujarati trabeate stone brackets."
    },
    # 12. Hamzanama & Mughal Ateliers
    {
        "id": "prelims-cult-012",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L3; Satish Chandra, Ch. 13",
        "question": "With reference to the evolution of Mughal miniature painting, which of the following statements is correct?",
        "options": [
            "Humayun abolished royal painting workshops because orthodox theologians prohibited human representation.",
            "The Hamzanama manuscript, executed under Akbar's royal Tasvir Khana, was painted on cotton cloth rather than paper.",
            "Jahangir discouraged portraits of living creatures, restricting painters solely to geometrical arabesques.",
            "Shah Jahan replaced miniature paintings entirely with European oil on canvas paintings."
        ],
        "correctIndex": 1,
        "explanation": "Option B is correct: The monumental Dastan-i-Amir Hamza (Hamzanama), comprising around 1,400 large folio paintings supervised by Mir Sayyid Ali and Abdus Samad under Akbar, was uniquely executed on layers of cotton cloth backed with paper. Humayun founded the royal atelier, Jahangir was the supreme patron of naturalism (animals, flora, portraits), and Shah Jahan promoted formal court durbar miniatures with gold borders.",
        "trap": "Mughal miniatures were usually on paper, but the monumental Hamzanama was painted on cloth.",
        "topperTip": "Under Akbar, miniature painting was a collaborative enterprise where one master drew the outline (tarh), another applied color (rangamezi), and a specialist painted faces (chihranama)."
    },
    # 13. Jahangir & Ustad Mansur
    {
        "id": "prelims-cult-013",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 5",
        "question": "During the reign of Mughal Emperor Jahangir, which court painter was conferred the title 'Nadir-ul-Asr' (Wonder of the Age) for his extraordinary scientific depictions of birds, animals, and flowers?",
        "options": [
            "Mir Sayyid Ali",
            "Abdus Samad",
            "Ustad Mansur",
            "Basawan"
        ],
        "correctIndex": 2,
        "explanation": "Option C is correct: Ustad Mansur was conferred the title 'Nadir-ul-Asr' by Jahangir for his unmatched mastery in biological naturalism. Famous works include the 'Siberian Crane', the 'Dodo', the 'Bengal Florican', and the 'Zebra'. Abul Hasan was conferred 'Nadir-uz-Zaman' (Wonder of the Time) for portraiture.",
        "trap": "Don't confuse Ustad Mansur (Nadir-ul-Asr - flora/fauna) with Abul Hasan (Nadir-uz-Zaman - portraits/allegorical scenes).",
        "topperTip": "Jahangir wrote in Tuzuk-i-Jahangiri that he could identify the artist of any painting simply by looking at the stroke of the eyes or brows."
    },
    # 14. Rajasthani & Pahari Miniatures: Bani Thani
    {
        "id": "prelims-cult-014",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE 2018",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 5",
        "question": "The well-known painting 'Bani Thani' belongs to which of the following schools of Rajasthani miniature painting?",
        "options": [
            "Bundi School",
            "Jaipur School",
            "Kangra School",
            "Kishangarh School"
        ],
        "correctIndex": 3,
        "explanation": "Option D is correct: 'Bani Thani' is the masterpiece of the Kishangarh School, painted by Nihal Chand under the patronage of Raja Sawant Singh (Nagari Das). She is depicted with elongated sharp features, arched eyebrows, curved lotus-petal eyes, and a sheer transparent odhni (veil), often celebrated as India's 'Mona Lisa'.",
        "trap": "Bundi is famous for lush vegetation and water bodies, Kangra is Pahari; Kishangarh is the home of Bani Thani.",
        "topperTip": "Kishangarh paintings are distinguished by exaggerated lyrical idealization of Radha and Krishna."
    },
    # 15. Folk Paintings: Warli vs Madhubani vs Pattachitra vs Kalamkari
    {
        "id": "prelims-cult-015",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE 2015 / Re-engineered",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 6",
        "question": "Consider the following traditional Indian folk painting traditions and their geographic associations:\n1. Madhubani — Mithila region of Bihar\n2. Warli — Sahyadri tribal belt of Maharashtra\n3. Pattachitra — Raghurajpur heritage village of Odisha\n4. Kalamkari — Srikalahasti and Machilipatnam in Andhra Pradesh\nWhich of the pairs given above are correctly matched?",
        "options": [
            "1 and 2 only",
            "1, 2 and 3 only",
            "3 and 4 only",
            "1, 2, 3 and 4"
        ],
        "correctIndex": 3,
        "explanation": "All four pairs are correctly matched:\n- Madhubani/Mithila painting: Done by women in Bihar using rice paste and natural dyes (Kohbar and Aripan).\n- Warli painting: Tribal ritual art of Maharashtra using rice paste and gum on mud walls, characterized by basic geometric shapes (circle, triangle, square).\n- Pattachitra: Traditional cloth-based scroll painting from Odisha (Raghurajpur), depicting Jagannath and Vaishnava lore.\n- Kalamkari: Pen art ('kalam') in Srikalahasti (freehand mythological panels) and Machilipatnam (block-printed textiles) in Andhra Pradesh.",
        "trap": "All four are authentic GI-tagged geographical associations.",
        "topperTip": "Warli murals uniquely avoid religious icons, focusing on the Mother Goddess of fertility (Palghat) and the communal Tarpa dance."
    },
    # 16. Classical Dances: 8 Traditions
    {
        "id": "prelims-cult-016",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE 2014 / Re-engineered",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 7",
        "question": "With reference to the Classical Dance traditions recognized by the Sangeet Natak Akademi, consider the following statements:\n1. Sattriya was introduced in the 15th century CE by the Vaishnavite saint Sankaradeva in Assam's monastic institutions (Sattras).\n2. Mohiniyattam from Kerala is performed exclusively in the dynamic, vigorous Tandava style accompanied by brass drums.\n3. In Kuchipudi of Andhra Pradesh, the dancer often performs the 'Tarangam' balancing on the rim of a brass plate.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 1,
        "explanation": "Statements 1 and 3 are correct: Sattriya was created by Mahapurusha Sankaradeva as part of the Neo-Vaishnavite movement in Assam. In Kuchipudi, the climax of the performance frequently involves dancing on a brass plate with a pitcher of water on the head (Tarangam). Statement 2 is incorrect because Mohiniyattam is characterized by graceful, swaying feminine movements representing the delicate Lasya aspect, NOT vigorous Tandava.",
        "trap": "Mohiniyattam represents Lasya (graceful feminine style), whereas Kathakali incorporates strong Tandava elements.",
        "topperTip": "The Sangeet Natak Akademi recognizes 8 classical dances: Bharatanatyam, Kathak, Kathakali, Kuchipudi, Odissi, Manipuri, Mohiniyattam, and Sattriya (Ministry of Culture also includes Chhau)."
    },
    # 17. Kathak Gharanas & Features
    {
        "id": "prelims-cult-017",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 7",
        "question": "Regarding the classical dance form Kathak, consider the following statements:\n1. It traces its origin to travelling storytellers (Kathakars) in ancient Northern India.\n2. The Lucknow Gharana, patronized by Nawab Wajid Ali Shah, emphasized Bhava, grace, and expressive Abhinaya.\n3. The Jaipur Gharana placed greater emphasis on intricate rhythmic footwork (Tatkar) and rapid pirouettes (Chakkars).\n4. Dancers perform with straight knees and wear ankle bells (ghungroos) that synchronize with the Tabla bol.\nWhich of the statements given above are correct?",
        "options": [
            "1, 2 and 3 only",
            "2, 3 and 4 only",
            "1, 3 and 4 only",
            "1, 2, 3 and 4"
        ],
        "correctIndex": 3,
        "explanation": "All four statements are correct: Kathak originated from temple Kathakars reciting epics. It flourished under Mughal and Awadh patronage. The Lucknow Gharana (founded by Ishwari Prasad, nurtured by Nawab Wajid Ali Shah) specializes in subtle Abhinaya and Nazakat. The Jaipur Gharana (founded by Bhanuji) is famous for virtuosic Tatkar and dizzying Chakkars. Unlike Bharatanatyam/Odissi which require bent knees (Araimandi/Chowk), Kathak is performed with upright straight knees.",
        "trap": "Note that Kathak dancers dance with upright legs, while South Indian dances predominantly use half-sitting (Araimandi) positions.",
        "topperTip": "Birju Maharaj, Lachhu Maharaj, and Shambhu Maharaj belonged to the illustrious Kalka-Bindadin lineage of the Lucknow Gharana."
    },
    # 18. Puppetry Traditions: 4 Typologies
    {
        "id": "prelims-cult-018",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE 2013 / Re-engineered",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 8",
        "question": "Which of the following puppetry traditions of India uses shadow puppets made of translucent deer or goat skin to cast silhouettes on an illuminated screen?",
        "options": [
            "Kathputli of Rajasthan",
            "Tholu Bommalata of Andhra Pradesh",
            "Putul Nach of West Bengal",
            "Pavakoothu of Kerala"
        ],
        "correctIndex": 1,
        "explanation": "Option B is correct: Tholu Bommalata (Andhra Pradesh) is a shadow puppetry tradition using translucent colored leather figures manipulated behind a white cotton screen. Kathputli (Rajasthan) is string puppetry; Putul Nach (West Bengal) is rod puppetry; Pavakoothu (Kerala) is glove puppetry based on Kathakali themes.",
        "trap": "Match the category: Kathputli = String; Tholu Bommalata/Ravanachhaya/Togalu Gombeyaatta = Shadow; Putul Nach = Rod; Pavakoothu = Glove.",
        "topperTip": "Ravanachhaya of Odisha is a unique shadow puppetry form that uses opaque deer skin puppets with no joints, casting stark, monochrome shadows."
    },
    # 19. Ravanachhaya vs Tholu Bommalata
    {
        "id": "prelims-cult-019",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 8",
        "question": "With reference to the shadow puppetry forms of India, consider the following statements:\n1. Ravanachhaya of Odisha uses non-jointed deer skin puppets that cast non-colored, monochrome shadows.\n2. Togalu Gombeyaatta is the traditional shadow puppetry of Karnataka.\n3. Tholu Bommalata of Andhra Pradesh uses large, multi-jointed translucent colored leather puppets.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 3,
        "explanation": "All three statements are correct: Ravanachhaya (Odisha) uses single-piece unjointed deer skin puppets creating poetic black shadows (named because Ravana's shadow is cast). Togalu Gombeyaatta is native to Karnataka. Tholu Bommalata (Andhra Pradesh) features large figures up to 6 feet high with colored perforations and articulate limb joints.",
        "trap": "Shadow puppetry varies from colored (Andhra/Karnataka) to strictly uncolored silhouettes (Odisha).",
        "topperTip": "Puppetry is mentioned in ancient Tamil literature (Silappadikaram) and the Mahabharata, indicating its hoary antiquity."
    },
    # 20. Classical Music: Hindustani vs Carnatic
    {
        "id": "prelims-cult-020",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE 2012 / Re-engineered",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 9",
        "question": "Regarding the two major traditions of Indian classical music, which of the following statements is correct?",
        "options": [
            "Carnatic music has numerous gharanas with distinct performance lineages, unlike Hindustani music.",
            "Hindustani music assimilated Persian and Central Asian influences, whereas Carnatic music developed relatively insulated in the South.",
            "Carnatic music gives primary importance to instrumental solo improvisation rather than vocal compositions.",
            "Hindustani music classifies ragas into a rigid 72 Melakarta parent scale system formulated by Venkatamakhin."
        ],
        "correctIndex": 1,
        "explanation": "Option B is correct: Hindustani music absorbed significant Persian, Arab, and Central Asian aesthetics under the Sultanate and Mughal periods (Amir Khusrau introducing Khayal, Qawwali, Tarana). Carnatic music remained predominantly indigenous, deeply rooted in Hindu temple bhakti traditions. Option A is incorrect (Gharana system belongs to Hindustani music). Option C is incorrect (Carnatic is heavily vocal/Kriti-oriented). Option D is incorrect (the 72 Melakarta system belongs to Carnatic music).",
        "trap": "The 72 Melakarta raga system belongs to CARNATIC music (devised by Venkatamakhin in Chaturdandi Prakasika), not Hindustani.",
        "topperTip": "The Trinity of Carnatic Music consists of Tyagaraja, Muthuswami Dikshitar, and Syama Sastri (all contemporaries born in Tiruvarur, Tamil Nadu)."
    },
    # 21. S.C. Dube: Indian Village & 'Little Republic' Myth
    {
        "id": "prelims-cult-021",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Prof. S.C. Dube, Indian Village (1955); Sociology Dube",
        "question": "In his seminal ethnographic study 'Indian Village' (1955) based on the village Shamirpet (Telangana), Prof. S.C. Dube challenged which colonial assumption about rural India?",
        "options": [
            "That Indian villages were self-sufficient, unchanging, and isolated 'little republics'",
            "That caste was an entirely British administrative invention created by census officials",
            "That agriculture was the exclusive monopoly of Shudra cultivating castes",
            "That rural women possessed complete customary ownership over ancestral agricultural land"
        ],
        "correctIndex": 0,
        "explanation": "Option A is correct: Sir Charles Metcalfe had famously characterized Indian village communities in 1830 as 'little republics, having nearly everything that they want within themselves, and almost independent of any foreign relations.' Prof. S.C. Dube (along with M.N. Srinivas) systematically debunked this myth, proving that the village was never economically, socially, or politically self-sufficient, but was deeply integrated into regional market networks, pilgrimage circuits, and matrimonial ties.",
        "trap": "Metcalfe proposed the 'little republic' myth; modern Indian sociologists like Dube and Srinivas conclusively disproved it.",
        "topperTip": "S.C. Dube identified that Indian village life operates on two simultaneous axes: internal caste hierarchy and village-wide solidarity."
    },
    # 22. Jajmani System & Reciprocity
    {
        "id": "prelims-cult-022",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Prof. S.C. Dube, Indian Society; William Wiser",
        "question": "With reference to the traditional 'Jajmani System' in rural India, consider the following statements:\n1. It was a non-monetary, hereditary institutional relationship between landowning patron castes (Jajmans) and service/artisan castes (Kamins/Kaminis).\n2. Payments were traditionally made in kind, such as grain shares at harvest time and customary gifts during life-cycle rituals.\n3. The system completely dissolved during the Mauryan period due to the widespread circulation of punch-marked silver coins.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 0,
        "explanation": "Statements 1 and 2 are correct: The Jajmani system (analyzed by William Wiser and S.C. Dube) was an institutionalized system of socio-economic reciprocity where artisan and service castes provided hereditary labor to landowning Jajmans in exchange for grain, clothing, and customary ritual perquisites. Statement 3 is incorrect because the Jajmani system persisted well into the 20th century and only weakened under modern market monetization, land reforms, and industrialization.",
        "trap": "The Jajmani system did NOT dissolve in ancient times; it survived as a cornerstone of rural social structure until late 20th century modernisation.",
        "topperTip": "While functionalists viewed Jajmani as harmonious interdependence, conflict theorists emphasized its exploitative power asymmetry favoring dominant landowning castes."
    },
    # 23. Tribal Approaches: Isolation vs Assimilation vs Integration
    {
        "id": "prelims-cult-023",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Prof. S.C. Dube, Indian Society; Verrier Elwin; G.S. Ghurye",
        "question": "In the historical debate on tribal policy in post-independent India, which approach was championed by Jawaharlal Nehru and Verrier Elwin as encapsulated in the 'Tribal Panchsheel'?",
        "options": [
            "Complete Isolation (National Park approach leaving tribes in undisturbed seclusion)",
            "Total Assimilation (Rapidly absorbing tribes into the mainstream Hindu social hierarchy)",
            "Integration (Developing tribes along their own genius while preserving their rights in land and forests)",
            "Privatization of tribal ancestral territories to encourage commercial extractive industries"
        ],
        "correctIndex": 2,
        "explanation": "Option C is correct: Verrier Elwin and Jawaharlal Nehru formulated the policy of 'Integration' embodied in the 'Tribal Panchsheel' (1958). It rejected both extreme isolation (zoo/museum policy) and forced assimilation (which destroyed tribal culture), advocating instead that tribals should develop along lines of their own genius without imposing outside values, while protecting their land and forest rights.",
        "trap": "Nehru's policy was INTEGRATION, not isolation (Elwin's early stance) nor assimilation (Ghurye's stance).",
        "topperTip": "Nehru stated: 'We should judge results not by statistics or the amount of money spent, but by the quality of human character that is evolved.'"
    },
    # 24. A.L. Basham: The Wonder That Was India
    {
        "id": "prelims-cult-024",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "A.L. Basham, A Cultural History of India & Wonder That Was India",
        "question": "According to historian A.L. Basham in 'A Cultural History of India', what is the most remarkable civilizational characteristic of Indian culture across millennia?",
        "options": [
            "Its rigid doctrinal intolerance towards foreign religious philosophical systems",
            "Its remarkable capacity for cultural assimilation and synthesis without losing its core continuity",
            "Its complete reliance on military conquest to enforce cultural homogeneity",
            "Its rejection of speculative philosophy in favor of pure materialistic statecraft"
        ],
        "correctIndex": 1,
        "explanation": "Option B is correct: A.L. Basham famously emphasized that the central genius of Indian civilization lies in its immense power of synthesis and assimilation. From the Indo-Aryans, Greeks, Sakas, and Kushanas to the Islamic and European arrivals, Indian culture absorbed diverse artistic, philosophical, and social traditions while preserving an unbroken thread of civilizational identity.",
        "trap": "Basham emphasizes continuity through absorption and peaceful assimilation, not violent enforcement.",
        "topperTip": "Basham noted that ancient India enjoyed a degree of religious tolerance and cultural diversity rarely matched in the ancient Mediterranean world."
    },
    # 25. Sittanavasal Cave Murals
    {
        "id": "prelims-cult-025",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE 2013",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 5",
        "question": "The rock-cut cave paintings of Sittanavasal in Pudukkottai district of Tamil Nadu are associated with which religious tradition?",
        "options": [
            "Buddhism",
            "Jainism",
            "Shaivism",
            "Vaishnavism"
        ],
        "correctIndex": 1,
        "explanation": "Option B is correct: The Sittanavasal cave complex (Arivar Koil) in Tamil Nadu contains celebrated 7th-9th century CE murals associated with JAINISM, commissioned under Pandya patronage. The ceiling fresco depicts 'Samavasarana' — the celestial garden pavilion of the Jain Tirthankaras, featuring a lotus tank (Khatika-bhumi) filled with blooming lotuses, fish, elephants, and Bhavya souls gathering flowers.",
        "trap": "While Ajanta is Buddhist and Ellora is multi-religious, Sittanavasal is distinctly JAIN.",
        "topperTip": "Sittanavasal murals represent the southern counterpart of Ajanta classical tempera painting traditions."
    },
    # 26. Lepakshi Veerabhadra Temple
    {
        "id": "prelims-cult-026",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE 2016 / Re-engineered",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 5",
        "question": "The Veerabhadra Temple at Lepakshi (Andhra Pradesh), famed for its hanging pillar and ceiling murals depicting the Kiratarjuniya epic, was built during the reign of which empire?",
        "options": [
            "Kakatiya Dynasty",
            "Hoysala Empire",
            "Vijayanagara Empire",
            "Chola Empire"
        ],
        "correctIndex": 2,
        "explanation": "Option C is correct: The Lepakshi Veerabhadra temple was constructed in 1530 CE by brothers Virupanna and Viranna, governors under Vijayanagara Emperor Achyuta Deva Raya. It is world-renowned for Vijayanagara mural art (including a monumental 24x14 ft ceiling painting of Veerabhadra), intricate granite pillars, and the colossal monolithic Nandi nearby.",
        "trap": "Lepakshi is located in Andhra Pradesh but represents VIJAYANAGARA imperial architecture and mural art.",
        "topperTip": "Lepakshi paintings show human figures in three-quarter profile with protruding outer eyes, anticipating late medieval South Indian textile art."
    },
    # 27. Hoysala Architecture: Belur & Halebidu
    {
        "id": "prelims-cult-027",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L2; Upinder Singh, Ch. 10",
        "question": "Regarding the Hoysala temple architecture of Karnataka (inscribed as a UNESCO World Heritage Site in 2023), consider the following features:\n1. Steatite (chloritic schist / soapstone) was used as the primary building material.\n2. The temple sanctum is laid out on a stellate (star-shaped) ground plan.\n3. The temples are built directly on flat ground without any elevated platform (Jagati).\nWhich of the features given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 0,
        "explanation": "Statements 1 and 2 are correct: Hoysala architects utilized soft chloritic schist (soapstone) which allowed delicate, jewel-like deep undercutting and filigree carving. Their sanctums feature a unique multi-pointed star-shaped (stellate) ground plan. Statement 3 is incorrect because Hoysala temples (Chennakeshava at Belur, Hoysaleswara at Halebidu, Keshava at Somanathapura) always rest on a wide, elevated, star-shaped stone platform called a 'Jagati' that serves as an open-air circumambulation terrace.",
        "trap": "Hoysala temples DO have an elevated platform (Jagati); statement 3 is false.",
        "topperTip": "Hoysala artists signed their sculptures (e.g., Ruvari Mallitamma, Dasoja), a rare occurrence in ancient Indian anonymous art."
    },
    # 28. Sun Temple Konark & Kalinga Style
    {
        "id": "prelims-cult-028",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L2; Nitin Singhania, Ch. 3",
        "question": "The 13th-century Sun Temple at Konark, built by Eastern Ganga King Narasimhadeva I, belongs to the Kalinga school of architecture. What are the three classic structural components of a full-fledged Kalinga temple?",
        "options": [
            "Deula (sanctum spire), Jagamohana (assembly hall), and Natamandira (dance pavilion)",
            "Vimana, Gopuram, and Kalyana Mandapa",
            "Stupika, Torana, and Chaitya Griha",
            "Garbhagriha, Buland Darwaza, and Charbagh"
        ],
        "correctIndex": 0,
        "explanation": "Option A is correct: Kalinga architecture consists of the Deula/Rekha Deula (the curvilinear sanctum tower), the Jagamohana/Pidha Deula (stepped pyramidal roof assembly hall), and often an aligned Natamandira (festive dance hall) and Bhogamandapa (offering hall). Konark is designed as a colossal solar chariot with 24 carved stone wheels pulled by 7 horses.",
        "trap": "Vimana and Gopuram belong to Dravida style; Deula and Jagamohana are unique Kalinga terminology.",
        "topperTip": "Rabindranath Tagore wrote of Konark: 'Here the language of stone surpasses the language of human man.'"
    },
    # 29. Khajuraho Temples & Nagara Panchayatana
    {
        "id": "prelims-cult-029",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L2; Upinder Singh, Ch. 10",
        "question": "With reference to the Chandela temples of Khajuraho (Madhya Pradesh), consider the following statements:\n1. The Kandariya Mahadeva Temple is the largest and most elaborate monument in the complex.\n2. In contrast to standard Nagara temples, Khajuraho temples lack high plinths and are entered directly from ground level.\n3. The subsidiary shikharas (Urushringas) cluster around the central tower, creating the visual impression of a rising mountain range (Mount Kailash).\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 1,
        "explanation": "Statements 1 and 3 are correct: Kandariya Mahadeva is the crowning achievement of Chandela architecture. Its central shikhara is graded with ascending miniature spires (urushringas), evoking the peaks of Mount Kailash. Statement 2 is incorrect because Khajuraho temples are built on exceptionally high solid stone plinths (Jagati) that elevate the entire monument high above the surrounding ground.",
        "trap": "Khajuraho temples stand on remarkably HIGH plinths, not ground level.",
        "topperTip": "Khajuraho temples are celebrated for harmonious unity of architecture and sculpture, encompassing both spiritual deities and secular erotic Mithuna reliefs."
    },
    # 30. Classical Puppetry: Pavakoothu & Kathputli
    {
        "id": "prelims-cult-030",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 8",
        "question": "Regarding the traditional puppetry forms of India, consider the following statements:\n1. Pavakoothu of Kerala is a glove-puppet tradition whose figurines wear colorful headgears and facial makeup identical to Kathakali dancers.\n2. Kathputli of Rajasthan puppets are carved from light mango wood, lack legs, and are draped in flowing pleated skirts.\n3. Yampuri of Bihar is a rod puppet tradition made of single-piece wood depicting scenes from Yama's court.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 3,
        "explanation": "All three statements are correct: Pavakoothu (Kerala) glove puppets closely replicate Kathakali costumes and character types. Kathputli (Rajasthan) string puppets are legless, manipulated by strings tied to the puppeteer's fingers, producing high-pitched squeaks via a bamboo reed (boli). Yampuri (Bihar) is an ancient rod puppetry tradition portraying Yama's judgement on human souls.",
        "trap": "Notice that Kathputli puppets have no legs; their movements are conveyed entirely through the swirl of their skirts.",
        "topperTip": "Rajasthan's Bhat community are traditional hereditary custodians of the Kathputli craft."
    },
    # 31. Matrilineal Tribal Societies: Khasi & Garo
    {
        "id": "prelims-cult-031",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Prof. S.C. Dube, Indian Society; Bipan Chandra",
        "question": "In Indian sociological studies on kinship, the Khasi and Garo tribal communities of Meghalaya are celebrated examples of which social system?",
        "options": [
            "Patriarchal and Patrilineal society",
            "Matrilineal and Matrilocal society",
            "Fraternal Polyandry society",
            "Endogamous Totemic Moiety without clan descent"
        ],
        "correctIndex": 1,
        "explanation": "Option B is correct: The Khasi, Jaintia, and Garo communities of Meghalaya practice matrilineal descent (ancestry traced through the mother) and matrilocal residence (husband moves to the wife's family home). Among the Khasis, the youngest daughter (Khadduh) inherits the ancestral ancestral property and acts as custodian of clan rituals.",
        "trap": "Do not confuse 'matrilineal' (lineage through female line) with 'matriarchal' (exclusive political rule by women).",
        "topperTip": "Even in matrilineal societies like the Khasi, political decisions in traditional councils (Dorbar Shnong) were traditionally led by maternal uncles (Kni)."
    },
    # 32. Sanskrit Theater & Natya Shastra
    {
        "id": "prelims-cult-032",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "A.L. Basham, Ch. 8; Bharata Muni Natya Shastra",
        "question": "In classical Sanskrit dramaturgy formulated in Bharata Muni's 'Natya Shastra', the comic character who acts as the loyal jester, confidant, and gluttonous companion to the hero (Nayaka) is known as the:",
        "options": [
            "Sutradhara",
            "Vidushaka",
            "Pratihara",
            "Nandi"
        ],
        "correctIndex": 1,
        "explanation": "Option B is correct: The Vidushaka is the traditional buffoon/jester in classical Sanskrit drama (prominent in Kalidasa's Abhijnanashakuntalam and Shudraka's Mrichchhakatika). Ironically portrayed as an uneducated Brahmin who speaks Prakrit (while kings speak formal Sanskrit), the Vidushaka serves as comic relief and provides moral commentary. Sutradhara is the stage manager/director.",
        "trap": "Sutradhara opens the play; Vidushaka is the jester companion.",
        "topperTip": "Sanskrit plays always have a happy ending; tragedy was forbidden by the conventions of the Natya Shastra."
    },
    # 33. Dhrupad vs Khayal
    {
        "id": "prelims-cult-033",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearRef": "UPSC CSE 2012 / Re-engineered",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 9",
        "question": "Regarding the Dhrupad genre of Hindustani classical music, consider the following statements:\n1. It is the oldest surviving classical vocal tradition of North India, traditionally performed with severe meditative gravity and spiritual devotion.\n2. It places supreme emphasis on syllables derived from Vedic mantras (Nom-Tom Alap) without instrumental rhythmic accompaniment during the opening phase.\n3. The primary percussion accompaniment for Dhrupad is the Tabla.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 0,
        "explanation": "Statements 1 and 2 are correct: Dhrupad is the oldest form of Hindustani classical singing, rooted in the Sama Veda. The performance begins with an elaborate, unmetered Nom-Tom Alap exploring the microtonal purity (shruti) of each note. Statement 3 is incorrect because Dhrupad is traditionally accompanied by the barrel drum PAKHAWAJ (or Mridangam), NOT the Tabla (which is used for Khayal and Thumri).",
        "trap": "Dhrupad uses the PAKHAWAJ, not the Tabla!",
        "topperTip": "Mian Tansen and Swami Haridas were legendary exponents of Dhrupad in the 16th century."
    },
    # 34. South Indian Cultural Diffusion to Southeast Asia
    {
        "id": "prelims-cult-034",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "A.L. Basham, A Cultural History of India, Ch. 29",
        "question": "With reference to the maritime transmission of Indian culture to Southeast Asia (Suvarnabhumi) between the 1st and 12th centuries CE, consider the following statements:\n1. The Borobudur monument in Java (Indonesia) is a colossal Mahayana Buddhist stupa constructed by the Sailendra dynasty.\n2. The temple complex of Angkor Wat in Cambodia was originally founded by Khmer King Suryavarman II as a dedicated Hindu temple to Lord Vishnu.\n3. Indian cultural diffusion was achieved primarily through direct military conquest and colonial annexation by the Mauryan Empire.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 0,
        "explanation": "Statements 1 and 2 are correct: Borobudur (Java) was built by the Sailendra dynasty (~8th-9th century CE) as an stepped mandala stupa. Angkor Wat (Cambodia) was constructed by Suryavarman II in the 12th century dedicated to Vishnu. Statement 3 is incorrect because Indian cultural influence ('Indianization') occurred peacefully through maritime trade guilds (Manigramam, Ayyavole), Buddhist monks, and Brahmin scholars invited by Southeast Asian rulers, NOT through Mauryan military conquest.",
        "trap": "Indian cultural diffusion across Southeast Asia was peaceful and commercial/religious, not military imperialism.",
        "topperTip": "Sanskrit inscriptions written in Pallava Grantha script have been discovered across Vietnam (Champa), Cambodia (Funan), and Indonesia (Kutei)."
    },
    # 35. Prof. S.C. Dube: Changing Social Stratification
    {
        "id": "prelims-cult-035",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Prof. S.C. Dube, Indian Society; NCERT Sociology",
        "question": "According to sociologist Prof. S.C. Dube, the introduction of adult franchise, land reforms, and democratic decentralization (Panchayati Raj) in post-independent rural India has led to:",
        "options": [
            "The total elimination of caste consciousness across all agrarian social strata",
            "A shift from purely ritualistic, ascribed hierarchy toward secular economic and political competition among dominant castes",
            "The complete replacement of the joint family by Western nuclear individualism in every village",
            "The revival of pre-modern feudal forced labor (begar) across all states"
        ],
        "correctIndex": 1,
        "explanation": "Option B is correct: Prof. S.C. Dube documented that modernization, democratic elections, and statutory Panchayats shifted the axis of power in rural India. While ritual purity-pollution hierarchy weakened, caste assumed a new 'secular-political' role as an instrument for electoral mobilization, political bargaining, and economic patronage among dominant agricultural castes.",
        "trap": "Caste did NOT disappear; its role shifted from ritual status to secular political mobilization.",
        "topperTip": "Sociologists refer to this transformation as the 'secularization and politicization of caste'."
    },
    # 36. Classical Puppetry: Bommalattam
    {
        "id": "prelims-cult-036",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearRef": "UPSC CSE Pattern",
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 8",
        "question": "Bommalattam, a complex and heavy puppetry tradition of Tamil Nadu, is unique among Indian puppetry forms because:",
        "options": [
            "It combines the operational mechanisms of both string puppetry and rod puppetry, with strings attached to an iron ring worn on the puppeteer's head.",
            "It is performed underwater using watertight painted wooden dolls.",
            "It uses shadows cast by live performers wearing animal masks behind an oil lamp.",
            "It excludes any spoken dialogue and is accompanied purely by temple conch horns."
        ],
        "correctIndex": 0,
        "explanation": "Option A is correct: Bommalattam of Tamil Nadu features the largest, heaviest mechanical puppets in India (up to 10 kg). They uniquely combine string and rod manipulation: the strings are attached to an iron ring (crown) fitted tightly around the master puppeteer's head, while thin rods are used to articulate the puppet's hands and arms.",
        "trap": "Bommalattam is both string AND rod puppetry controlled by an iron ring crown on the puppeteer's head.",
        "topperTip": "Bommalattam performances traditionally lasted all night during temple festivals, narrating episodes from the Ramayana and Mahabharata."
    }
]

# ==============================================================================
# 12 HIGH-YIELD MAINS QUESTIONS (Culture & Sociology)
# ==============================================================================
new_mains = [
    # 1. Rock-cut Cave Architecture Evolution
    {
        "id": "mains-cult-001",
        "question": "Trace the architectural and ideological evolution of rock-cut cave shrines in ancient India from the simple ascetic cells of Barabar to the elaborate multi-storeyed complexes of Ajanta and Ellora.",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Ishani Pandya Compendium L1 & L2; A.L. Basham, Ch. 8; Upinder Singh, Ch. 7 & 9",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearSource": "UPSC CSE Mains Pattern",
        "framework": {
            "intro": "Indian rock-cut architecture represents a thousand-year journey of lithic mastery, evolving from the austere 3rd-century BCE Ajivika hermitages at Barabar into the grand Buddhist, Brahmanical, and Jain cavernous marvels of Ajanta and Ellora.",
            "body": [
                {
                    "heading": "Phase 1: Mauryan Origins & Wood-Imitative Lithic Architecture (3rd Century BCE)",
                    "points": [
                        "Barabar and Nagarjuni Caves (Bihar): Commissioned by Ashoka and Dasharatha for Ajivika ascetics; feature single rectangular chambers with circular domed sanctums (e.g., Sudama Cave).",
                        "Lomas Rishi Cave façade: Earliest imitation of timber vaulted architecture in stone, featuring an ogee Chaitya horseshoe arch and decorative elephant friezes with mirror-like Mauryan polish."
                    ]
                },
                {
                    "heading": "Phase 2: Early Hinayana Buddhist Shrines (2nd Century BCE – 2nd Century CE)",
                    "points": [
                        "Western Ghats (Bhaja, Karle, Bedse, early Ajanta): Monks adapted Western Deccan basalt cliffs along trade routes into Chaitya-grihas (pillared congregational halls with barrel vaults) and Viharas (residential cells surrounding a central court).",
                        "Aniconic symbolism: Central object of veneration was an unadorned rock-hewn Stupa symbolizing the Mahaparinirvana of Gautama Buddha."
                    ]
                },
                {
                    "heading": "Phase 3: Mahayana Transformation & Ajanta Murals (5th Century CE)",
                    "points": [
                        "Iconic shift: Under Vakataka patronage (Harishena), the Stupa integrated a colossal seated image of Buddha in the sanctum (e.g., Ajanta Cave 19 and 26).",
                        "Synthesis of Architecture and Painting: Caves became artistic showcases with Tempera murals depicting Jataka tales, Bodhisattvas (Padmapani, Vajrapani), and court life."
                    ]
                },
                {
                    "heading": "Phase 4: Climax of Multi-Religious Monoliths at Ellora (6th – 10th Century CE)",
                    "points": [
                        "Pluralistic ecumenism: 34 caves encompassing Buddhist (1–12), Hindu (13–29), and Jain (30–34) shrines carved side-by-side along the Charanandri hills.",
                        "Kailash Temple (Cave 16): Zenith of rock-cut architecture under Rashtrakuta Krishna I; a complete two-storeyed Dravidian temple carved vertically from top to bottom out of a single basalt cliff face."
                    ]
                }
            ],
            "conclusion": "Rock-cut architecture transformed raw cliff faces into sacred civilizational landscapes, transitioning from imitating perishable timber prototypes to commanding monumental freestanding structural expression in living stone.",
            "diagramMapIdea": "Evolutionary Flowchart: Barabar (Ascetic Cell) -> Karle (Hinayana Stupa Chaitya) -> Ajanta (Mahayana Buddha Icon + Murals) -> Ellora Kailash (Monolithic Dravida Temple)."
        }
    },
    # 2. Sculptural Schools: Gandhara vs Mathura vs Amaravati
    {
        "id": "mains-cult-002",
        "question": "Critically analyze the stylistic, ideological, and material distinctions among the Gandhara, Mathura, and Amaravati schools of sculpture. How did they reflect the regional cultural milieus of post-Mauryan India?",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Ishani Pandya Compendium L1; Nitin Singhania, Ch. 2; Upinder Singh, Ch. 8",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearSource": "UPSC CSE Mains Pattern",
        "framework": {
            "intro": "The post-Mauryan era (c. 2nd century BCE – 3rd century CE) witnessed an unprecedented sculptural renaissance, as Gandhara, Mathura, and Amaravati pioneered the visual anthropomorphic transition from aniconic symbols to magnificent divine iconographies.",
            "body": [
                {
                    "heading": "Materiality & Geographic Settings",
                    "points": [
                        "Gandhara (Peshawar, Taxila, Swat): Utilized grey-blue schist stone, green phyllite, and later stucco, situated at the crossroads of the Silk Route.",
                        "Mathura (Yamuna basin, UP): Sculpted purely from indigenous spotted red sandstone from Sikri.",
                        "Amaravati (Krishna-Godavari delta, AP): Used gleaming white crystalline limestone (Palnad marble) along fertile maritime trade arteries."
                    ]
                },
                {
                    "heading": "Aesthetic Style & Foreign Influences",
                    "points": [
                        "Gandhara (Greco-Roman Synthesis): Apollo-like facial idealism, heavy drapery folds resembling Roman togas, wavy curly hair, sharp facial contours, and anatomically precise musculature.",
                        "Mathura (Indigenous Sensibility): Earthy, robust masculinity, clinging transparent muslin drapery, round energetic face with smiling expression, raised right hand in Abhaya Mudra, and seated on a lion throne.",
                        "Amaravati (Dynamic Narrative Vitality): Emphasized narrative panels filled with lively crowd scenes, ecstatic postures, graceful Tribhanga curves, and deep psychological emotion rather than isolated iconic statues."
                    ]
                },
                {
                    "heading": "Religious Ideology & Patronage",
                    "points": [
                        "Gandhara: Exclusively Mahayana Buddhist, patronized primarily by Kushana rulers (Kanishka) and wealthy Silk Route merchants.",
                        "Mathura: Eclectic and pluralistic; pioneered images of the Buddha, Jinas (Ayagapatas), and Hindu deities (Vishnu, Shiva lingas, Surya, Kartikeya) under Kushana patronage.",
                        "Amaravati: Predominantly Hinayana and Mahayana Buddhist stupa reliefs, patronized by Satavahana and Ikshvaku rulers, royal ladies, and merchant guilds (Nigamas)."
                    ]
                }
            ],
            "conclusion": "While Gandhara mirrored the cosmopolitan Indo-Greek frontier and Amaravati expressed the sensuous maritime ethos of the Deccan, Mathura served as the indigenous fountainhead that defined the pan-Indian classical aesthetic of the Gupta golden age.",
            "diagramMapIdea": "Comparative 4-Column Table: Dimension, Gandhara School, Mathura School, Amaravati School."
        }
    },
    # 3. South Indian Temple Architecture Evolution
    {
        "id": "mains-cult-003",
        "question": "Examine the developmental trajectory of South Indian temple architecture from the rock-cut monolithic rathas of the Pallavas to the architectural grandeur of the Imperial Cholas and Vijayanagara rayagopurams.",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Ishani Pandya Compendium L2; A.L. Basham, Ch. 8; Satish Chandra, Ch. 2",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearSource": "UPSC CSE Mains Pattern",
        "framework": {
            "intro": "Dravidian temple architecture embodies a spectacular thousand-year evolutionary continuity, progressing from early Pallava rock-cut experiments to the soaring imperial Vimanas of the Cholas and the colossal fortified urban temple complexes of Vijayanagara.",
            "body": [
                {
                    "heading": "The Pallava Foundation: Rock-cut to Structural Transition (600–900 CE)",
                    "points": [
                        "Mahendra Style: Excavated pillared rock-cut mandapas with simple dwarapala guardians.",
                        "Mamalla Style: Monolithic freestanding Pancha Pandava Rathas at Mahabalipuram, showcasing varied roof designs (Dharmaraja ratha's stepped pyramid, Bhima ratha's wagon vault).",
                        "Rajasimha Style: Birth of structural masonry temples, exemplified by the Shore Temple at Mahabalipuram and Kailasanathar Temple at Kanchipuram with nascent enclosure walls."
                    ]
                },
                {
                    "heading": "The Imperial Chola Zenith: The Monumental Vimana (900–1200 CE)",
                    "points": [
                        "Brihadisvara Temple, Thanjavur (1010 CE): Rajaraja I elevated the Dravida style to unprecedented heights with a 66-meter high pyramidal Vimana dominating the complex, crowned by an 80-tonne monolithic granite cupola.",
                        "Architectural features: Focus remained exclusively on the sanctum Vimana; entry gopurams were subordinate in height; temples functioned as multi-functional economic centers owning land, hiring artisans, and maintaining devadasis."
                    ]
                },
                {
                    "heading": "Pandya Shift to Gopurams (1150–1350 CE)",
                    "points": [
                        "Inversion of scale: As temples were repeatedly expanded with concentric enclosure walls (prakaras), the outer entrance gateways (Gopurams) grew taller than the interior Vimana."
                    ]
                },
                {
                    "heading": "Vijayanagara Imperial Grandeur (1336–1646 CE)",
                    "points": [
                        "Colossal Rayagopurams: Towering entrance gateways rising up to 11 storeys with terracotta stucco figures, visible across miles.",
                        "Kalyana Mandapa & Yali Pillars: Ornate marriage pavilions featuring monolithic granite pillars carved with rearing mythical hippogryphs (Yalis) and rider warriors (e.g., Vittala Temple at Hampi).",
                        "Unique shrines: Monolithic stone chariot shrines, sacred water tanks, and musical pillars."
                    ]
                }
            ],
            "conclusion": "The evolution of Dravidian architecture mirrors the shift in political authority: the temple evolved from a quiet royal sanctuary under the Pallavas into a colossal cosmos of sacred civic authority under the Cholas and Vijayanagara emperors.",
            "diagramMapIdea": "Schematic Section of Dravidian Temple Evolution: Pallava Ratha -> Chola High Vimana (Brihadisvara) -> Vijayanagara Towering Raya-Gopuram & Kalyana Mandapa."
        }
    },
    # 4. Mughal Miniature Painting Synthesis
    {
        "id": "mains-cult-004",
        "question": "Analyze how Mughal miniature painting synthesized Persian artistic traditions with indigenous Indian sensibilities, and examine how its thematic focus shifted under Akbar, Jahangir, and Shah Jahan.",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Ishani Pandya Compendium L3; Satish Chandra, Ch. 13; Nitin Singhania, Ch. 5",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearSource": "UPSC CSE Mains Pattern",
        "framework": {
            "intro": "Mughal miniature painting was not a mere provincial transplant of Persian art, but a vibrant cultural synthesis that harmonized Safavid Persian two-dimensional decorative refinement with the dynamic realism, rich palette, and emotional warmth of indigenous Indian traditions.",
            "body": [
                {
                    "heading": "The Indo-Persian Synthesis",
                    "points": [
                        "Humayun's initiative: Brought Persian masters Mir Sayyid Ali and Abdus Samad from Shah Tahmasp's Safavid court to Delhi.",
                        "Indianization in Akbar's Tasvir Khana: Over 80% of royal painters (Daswanth, Basawan, Kesu) were indigenous Hindus from Gujarat, Gwalior, and Kashmir. They infused Persian arabesque with Indian flora/fauna, dynamic movement, and realistic Indian skin tones.",
                        "Collaborative manuscript enterprise: Monumental projects like the Hamzanama (cloth folios) and Razmnama (Persian Mahabharata) synthesized epic narrative action with vibrant Indian ochres, lapis lazuli, and peacocks."
                    ]
                },
                {
                    "heading": "Shift Under Akbar (1556–1605): Epic Dynamism & Statecraft",
                    "points": [
                        "Multi-figured battle scenes, court pageantry, hunting expeditions, and historical chronicles (Akbarnama).",
                        "High physical energy, crowded compositions, and bird's-eye perspective depicting imperial vitality."
                    ]
                },
                {
                    "heading": "Shift Under Jahangir (1605–1627): Scientific Naturalism & Portraiture",
                    "points": [
                        "Dissolution of mass workshops in favor of individual master artists (Ustad Mansur, Abul Hasan, Bishandas).",
                        "Keen scientific observation: Detailed biological studies of exotic birds (Siberian crane, dodo) and flora.",
                        "Western contact: Introduction of European perspective, cherubs, and golden halos around the Emperor."
                    ]
                },
                {
                    "heading": "Shift Under Shah Jahan (1628–1658): Imperial Formalism & Grandeur",
                    "points": [
                        "Shift from emotional naturalism to static ceremonial grandeur and symmetrical court durbars.",
                        "Extensive use of burnished gold leaf, luminous lapis borders, and jewel-like refinement, mirroring the aesthetic of the Taj Mahal."
                    ]
                }
            ],
            "conclusion": "Mughal painting served as a visual manifestation of composite culture (Ganga-Jamuni Tehzeeb), whose techniques subsequently cross-fertilized regional Rajasthani and Pahari schools across northern India.",
            "diagramMapIdea": "Comparative Timeline: Akbar (Narrative Action & Hamzanama) -> Jahangir (Naturalism & Ustad Mansur) -> Shah Jahan (Imperial Durbar & Gold Burnish)."
        }
    },
    # 5. Traditional Indian Puppetry
    {
        "id": "mains-cult-005",
        "question": "Indian puppetry is not merely an ancient theatrical art but a profound medium of oral historiography and community moral education. Elucidate the four primary puppetry traditions of India and discuss the modern threats to their survival.",
        "marks": 10,
        "wordLimit": 150,
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 8",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearSource": "UPSC CSE Mains Pattern",
        "framework": {
            "intro": "Mentioned in the Mahabharata and the 2nd-century CE Tamil epic Silappadikaram, puppetry (Kattabommalattam) is one of India's oldest performing arts, synthesizing storytelling, sculpture, music, and community philosophy.",
            "body": [
                {
                    "heading": "The Four Primary Typologies of Indian Puppetry",
                    "points": [
                        "String Puppets: Kathputli (Rajasthan) — legless wooden figures with pleated skirts and boli reeds; Kundhei (Odisha); Gombeyatta (Karnataka) mimicking Yakshagana costumes.",
                        "Shadow Puppets: Togalu Gombeyaatta (Karnataka); Tholu Bommalata (Andhra Pradesh) using large translucent leather figures; Ravanachhaya (Odisha) casting uncolored deer skin silhouettes.",
                        "Rod Puppets: Putul Nach (West Bengal) using jointed wooden arms operated by bamboo rods; Yampuri (Bihar) depicting Yama's court.",
                        "Glove Puppets: Pavakoothu (Kerala) featuring miniature Kathakali costumes and character types."
                    ]
                },
                {
                    "heading": "Contemporary Threats & Preservation Imperatives",
                    "points": [
                        "Digital diversion: Competition from digital television, cinema, and social media eroding rural audiences.",
                        "Economic precariousness: Traditional puppeteer families (like Rajasthan's Bhat community) facing loss of royal/temple patronage and acute livelihood distress.",
                        "Policy needs: National integration into school curricula, modern puppet festivals, and creative deployment in development communication (e.g., health awareness, literacy drives)."
                    ]
                }
            ],
            "conclusion": "Safeguarding puppetry requires elevating it from endangered folklore to an active, remunerative performing art that bridges timeless civilizational wisdom with modern social communication.",
            "diagramMapIdea": "Mind Map: Indian Puppetry Typologies (String, Shadow, Rod, Glove) with Regional Representatives."
        }
    },
    # 6. Classical Dances & Natya Shastra
    {
        "id": "mains-cult-006",
        "question": "Discuss the spiritual and philosophical foundations of Indian Classical Dance as codified in Bharata's Natya Shastra. How do these traditions bridge the sacred and the secular in Indian artistic consciousness?",
        "marks": 10,
        "wordLimit": 150,
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 7",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearSource": "UPSC CSE Mains Pattern",
        "framework": {
            "intro": "Indian classical dance originated as 'Natya Veda' (the Fifth Veda), synthesized by Brahma from the Rigveda (words), Samaveda (music), Yajurveda (gestures/abhinaya), and Atharvaveda (rasa/emotions) to elevate human consciousness.",
            "body": [
                {
                    "heading": "Philosophical Foundations in the Natya Shastra",
                    "points": [
                        "Tandava and Lasya duality: Represents the cosmic dance of Shiva (vigorous masculine cosmic rhythm) and Parvati (graceful feminine lyrical beauty).",
                        "Tripartite Structure: Nritta (pure rhythmic abstract movement without narrative), Nritya (interpretative expressive dance using facial bhava and mudras), and Natya (dramatic storytelling).",
                        "Rasa Theory: Transmuting everyday human emotions (bhavas) into transcendent, universal aesthetic bliss (Rasa) across the Nine Rasas (Navarasas)."
                    ]
                },
                {
                    "heading": "Bridging Sacred Devotion and Secular Aesthetics",
                    "points": [
                        "Temple Sanctum (Sacred): Began as divine seva by Devadasis in Bharatanatyam (Tamil Nadu) and Maharis in Odissi, symbolizing the human soul's longing for union with the Paramatma (Madhura Bhakti).",
                        "Royal Court & Public Stage (Secular): Kathak in northern courts absorbed secular nazakat and technical jugalbandi with tabla, while modern adaptations address contemporary social issues like ecology and gender justice."
                    ]
                }
            ],
            "conclusion": "Indian classical dance dissolves the dichotomy between the physical body and spiritual devotion, transforming somatic movement into a living prayer and an enduring symbol of cultural unity.",
            "diagramMapIdea": "Triangular Diagram: Natya Veda components (Nritta, Nritya, Natya) culminating in Universal Rasa."
        }
    },
    # 7. Folk & Tribal Paintings
    {
        "id": "mains-cult-007",
        "question": "Examine how Indian folk and tribal painting traditions (such as Warli, Madhubani, Pattachitra, and Kalamkari) encapsulate ecological harmony, sacred rituals, and community identity.",
        "marks": 10,
        "wordLimit": 150,
        "bookRef": "Ishani Pandya Compendium L3; Nitin Singhania, Ch. 6",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearSource": "UPSC CSE Mains Pattern",
        "framework": {
            "intro": "Unlike court miniatures commissioned by monarchs, Indian folk and tribal paintings are living communal expressions rooted in agrarian cycles, ecological reverence, and sacred rites of passage.",
            "body": [
                {
                    "heading": "Ecological Reverence and Sacred Rituals",
                    "points": [
                        "Warli (Maharashtra): Uses basic geometric motifs (circles for sun/moon, triangles for sacred mountains/trees) on mud walls using rice paste; celebrates the Mother of Fertility (Palghat) and the communal Tarpa dance without hierarchical gods.",
                        "Madhubani (Bihar): Women paint fertility murals (Kohbar) and courtyards (Aripan) using bamboo twigs and plant pigments, portraying sacred lotus ponds, bamboo stalks, and birds as symbols of abundance."
                    ]
                },
                {
                    "heading": "Textile Storytelling & Sacred Transmission",
                    "points": [
                        "Pattachitra (Odisha): Sacred cloth scrolls prepared with tamarind seed glue and chalk, narrating the Dashavatara and Jagannath lore with fluid lines and mineral colors.",
                        "Kalamkari (Andhra Pradesh): Natural vegetable dyed storytelling cloths from Srikalahasti (temple hangings drawn with bamboo pens) and Machilipatnam (block prints) depicting epics."
                    ]
                }
            ],
            "conclusion": "These folk traditions embody indigenous ecological wisdom and egalitarian community heritage, demonstrating that art in India has always been an organic dimension of everyday life.",
            "diagramMapIdea": "Concept Matrix: Painting Tradition, Ecological Motif, Ritual Context, Geographic Core."
        }
    },
    # 8. S.C. Dube: Indian Village Community
    {
        "id": "mains-cult-008",
        "question": "Critically examine the colonial myth of the Indian village as an 'isolated, self-sufficient little republic' in light of Prof. S.C. Dube's sociological findings. How do caste, jajmani, and factionalism structure village social reality?",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Prof. S.C. Dube, Indian Village (1955) & Indian Society; Sociology Dube",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearSource": "UPSC CSE Mains Pattern",
        "framework": {
            "intro": "Colonial administrators like Charles Metcalfe portrayed the Indian village as an unchanging, self-sufficient 'little republic.' Pioneering Indian sociologists, particularly Prof. S.C. Dube in his landmark study 'Indian Village' (1955), systematically deconstructed this romanticized fiction.",
            "body": [
                {
                    "heading": "Deconstructing the 'Little Republic' Myth",
                    "points": [
                        "Regional Interdependence: Shamirpet village (Dube's study) demonstrated that no village was economically, culturally, or politically self-sufficient.",
                        "Exogamous matrimonial networks: Village exogamy compelled families to forge marital and kinship alliances across dozens of surrounding settlements.",
                        "Economic and religious links: Periodic weekly markets (haats), pilgrimage circuits, revenue payments to state authorities, and regional caste councils (Jati Panchayats) continually tied the village into broader supra-local structures."
                    ]
                },
                {
                    "heading": "Internal Structural Axes of Village Reality",
                    "points": [
                        "Caste (Jati) Hierarchy: Social organization was sharply stratified based on purity and pollution, determining occupational specialization, residential segregation, and unequal land ownership.",
                        "Jajmani System of Reciprocity: An institutionalized network of reciprocal obligations where service and artisan castes (Kamins) served landowning patrons (Jajmans) for grain shares, combining functional interdependence with structural exploitation.",
                        "Dual Axis of Solidarity & Factionalism: The village exhibited both collective identity during crises/temple festivals and bitter factional rivalries (dharas) centered around dominant landowning lineage groups."
                    ]
                },
                {
                    "heading": "Post-Independence Transformations",
                    "points": [
                        "Impact of land reforms, the Green Revolution, and statutory Panchayati Raj weakened traditional Jajmani ties and monetized the rural economy.",
                        "Shift from ritual deference to active electoral political competition among intermediate backward classes and Dalits."
                    ]
                }
            ],
            "conclusion": "Prof. S.C. Dube proved that the Indian village was never an isolated museum of the past, but an open, dynamic social system shaped by constant interactions between tradition, power, and state interventions.",
            "diagramMapIdea": "S.C. Dube Village Model: Dual Axis Diagram showing Vertical Inter-caste Jajmani ties vs Horizontal Intra-caste Supra-village Kinship networks."
        }
    },
    # 9. Tribal Integration Debate: Elwin vs Ghurye
    {
        "id": "mains-cult-009",
        "question": "Evaluate the ideological debate between 'Isolation', 'Assimilation', and 'Integration' regarding tribal communities in India (Verrier Elwin vs. G.S. Ghurye). How did the 'Tribal Panchsheel' seek to harmonize tribal autonomy with national development?",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Prof. S.C. Dube, Indian Society; Verrier Elwin; G.S. Ghurye; Bipan Chandra",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearSource": "UPSC CSE Mains Pattern",
        "framework": {
            "intro": "The tribal question in modern India revolves around a fundamental policy dilemma: how to bring socioeconomic advancement to indigenous communities (Adivasis) without obliterating their distinctive cultural heritage, customary institutions, and ecological autonomy.",
            "body": [
                {
                    "heading": "The Competing Ideological Paradigms",
                    "points": [
                        "The Isolationist Approach (Verrier Elwin's early thesis): Advocated establishing 'National Parks' for tribals, keeping them sheltered from predatory moneylenders, timber contractors, and Hindu caste society to prevent cultural demoralization.",
                        "The Assimilationist Approach (G.S. Ghurye): Termed tribals 'backward Hindus' and argued for their rapid assimilation into the mainstream socioeconomic hierarchy, viewing isolation as an imperialist divide-and-rule strategy."
                    ]
                },
                {
                    "heading": "Nehru-Elwin's 'Tribal Panchsheel' (1958) as the Integrational Golden Mean",
                    "points": [
                        "Development along own genius: Tribals should develop along lines of their own genius, avoiding the imposition of alien values or lifestyles.",
                        "Respect for Land & Forests: Absolute protection of tribal customary rights in ancestral land and forest resources.",
                        "Building Local Cadres: Train and build up a team of their own people to administer governance and development work.",
                        "Avoiding Over-Administration: Administer through their own traditional social and cultural institutions rather than overwhelming them with outside bureaucratic schemes.",
                        "Human Quality as Metric: Judge success not by money spent or statistical targets, but by the quality of human character and freedom evolved."
                    ]
                },
                {
                    "heading": "Contemporary Realities & Unfinished Agendas",
                    "points": [
                        "Developmental displacement: Mining, dams, and industrial projects have disproportionately displaced tribal populations.",
                        "Constitutional safeguards: Fifth and Sixth Schedules, PESA Act (1996), and Forest Rights Act (2006) provide legal instruments for self-governance, but effective implementation remains hindered by administrative apathy."
                    ]
                }
            ],
            "conclusion": "The Tribal Panchsheel remains a visionary compass, proving that genuine national integration is achieved not by erasing diversity through forced assimilation, but by empowering tribal communities as equal partners in India's plural democracy.",
            "diagramMapIdea": "Tribal Policy Trilemma Triangle: Isolation (Elwin 1930s) vs Assimilation (Ghurye) -> Integration via Tribal Panchsheel (Nehru-Elwin 1958)."
        }
    },
    # 10. Jajmani System & Rural Transformation
    {
        "id": "mains-cult-010",
        "question": "Examine the socio-economic mechanisms of the traditional Jajmani system in rural India. What factors have led to its gradual breakdown in contemporary times?",
        "marks": 10,
        "wordLimit": 150,
        "bookRef": "Prof. S.C. Dube, Indian Society; William Wiser",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearSource": "UPSC CSE Mains Pattern",
        "framework": {
            "intro": "The Jajmani system was a hereditary institutional framework of reciprocal goods and service relationships between patron landowning families (Jajmans) and occupational service/artisan castes (Kamins).",
            "body": [
                {
                    "heading": "Socio-Economic Mechanisms",
                    "points": [
                        "Non-monetary reciprocity: Services (blacksmithing, carpentry, barbering, leatherwork) were compensated with grain shares at harvest, free housing sites, and customary gifts during weddings and rites of passage.",
                        "Power asymmetry: While functionalists emphasized mutual interdependence, critical sociologists highlighted that it institutionalized hereditary subordination and prevented upward mobility for lower castes."
                    ]
                },
                {
                    "heading": "Key Drivers of its Breakdown",
                    "points": [
                        "Monetization & Market Economy: Cash wages and commercial retail markets replaced customized hereditary barter arrangements.",
                        "Agricultural Mechanization: Tractors, combine harvesters, and factory-made tools rendered traditional artisans redundant.",
                        "Democratic Consciousness & Migration: Constitutional equality, education, reservations, and rural-urban migration provided alternative livelihoods, freeing Kamins from servitude."
                    ]
                }
            ],
            "conclusion": "The erosion of the Jajmani system marks a fundamental transition in rural India from pre-modern feudal status relationships toward contractual, monetized, and democratic citizenship ties.",
            "diagramMapIdea": "Flowchart: Jajmani Network -> Modern Forces (Monetization + Mechanization + Education) -> Contractual Agrarian Economy."
        }
    },
    # 11. A.L. Basham: Composite Civilization
    {
        "id": "mains-cult-011",
        "question": "'The civilization of India has not remained static; rather, its greatest virtue has been its immense power of synthesis.' Discuss this assertion of A.L. Basham with reference to India's cultural evolution across historical eras.",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "A.L. Basham, The Wonder That Was India & A Cultural History of India",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": False,
        "yearSource": "UPSC CSE Mains Pattern",
        "framework": {
            "intro": "In his seminal works, British Indologist A.L. Basham highlighted that Indian civilization survived and flourished across millennia not through rigid isolation or dogmatic resistance, but through an extraordinary capacity for cultural assimilation, continuous synthesis, and harmonious pluralism.",
            "body": [
                {
                    "heading": "Ancient Synthesis: Vedic, Shramanic & Tribal Absorption",
                    "points": [
                        "Indo-Aryan and Indigenous Synthesis: Absorption of indigenous Harappan and non-Aryan deities (Pashupati/Shiva, Mother Goddess, sacred trees) into the evolving Vedic pantheon.",
                        "Shramana Dialogues: Buddhism and Jainism challenged sacrificial orthodoxy, yet their core values of Ahimsa (non-violence) and ethical self-discipline were absorbed directly into classical Hinduism.",
                        "Greco-Roman and Central Asian Incursions: Indo-Greeks, Sakas, and Kushanas were assimilated into Indian society through marriage and conversion (e.g., Heliodorus pillar at Vidisha, Menander's Milinda Panha)."
                    ]
                },
                {
                    "heading": "Medieval Synthesis: The Ganga-Jamuni Tehzeeb",
                    "points": [
                        "Bhakti and Sufi Convergence: Kabir, Guru Nanak, and Chaitanya rejected caste orthodoxies and dogmatism, emphasizing personal devotion to a formless supreme reality (Nirguna) alongside Sufi pirs.",
                        "Language and Literature: Emergence of Urdu and Hindustani as bridges between Persian, Arabic, and regional Prakrit/Bhasha idioms.",
                        "Artistic & Architectural Syncretism: Indo-Islamic architecture harmonized Persian domes and arches with Rajasthani jali lattices, chhatris, and lotus finials; Hindustani music absorbed Khayal and Qawwali through Amir Khusrau."
                    ]
                },
                {
                    "heading": "Modern Synthesis: Colonial Encounter to Democratic Republic",
                    "points": [
                        "Socio-Religious Reformers: Raja Ram Mohan Roy, Swami Vivekananda, and Rabindranath Tagore synthesized Western rational science and enlightenment humanism with timeless Vedantic universalism.",
                        "Constitutional Synthesis: The Indian Constitution integrated Westminster parliamentary democracy with American fundamental rights and indigenous panchayati traditions."
                    ]
                }
            ],
            "conclusion": "As A.L. Basham observed, India's cultural continuity is not an inert relic, but a flowing river that renews itself by assimilating every tributary it encounters without ever losing its core civilizational direction.",
            "diagramMapIdea": "Synthesis Flow Diagram: Ancient (Vedic + Shramanic) -> Medieval (Bhakti + Sufi) -> Modern (Universalist Reform + Constitution)."
        }
    },
    # 12. Indian Cultural Diffusion in Southeast Asia
    {
        "id": "mains-cult-012",
        "question": "Assess the nature and legacy of Indian cultural and commercial diffusion across Southeast Asia ('Suvarnabhumi') during the ancient and early medieval periods. Why did historians term this phenomenon 'cultural transmission without colonization'?",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "A.L. Basham, A Cultural History of India, Ch. 29; Upinder Singh, Ch. 10",
        "category": "art-culture",
        "categoryLabel": "Art & Culture",
        "isPyq": True,
        "yearSource": "UPSC CSE Mains Pattern",
        "framework": {
            "intro": "Between the early centuries of the Common Era and the 13th century, South Asia and Southeast Asia were bound in an expansive cultural and commercial matrix, giving rise to what George Coedès termed the 'Indianized States of Southeast Asia.'",
            "body": [
                {
                    "heading": "Distinctive Modalities: Diffusion Without Military Conquest",
                    "points": [
                        "No Imperial Annexation: Unlike European colonial conquest or Roman imperialism, Indianization was completely peaceful and non-exploitative, driven by monsoon maritime trade networks.",
                        "Key Agents of Transmission: Indian merchant guilds (Manigramam, Nanadesi, Ayyavole), Buddhist monks, and Brahmin scholars invited by indigenous Southeast Asian rulers to legitimize royal statecraft.",
                        "Indigenous Agency: Local elites voluntarily adopted Sanskrit titles, epics, and cosmic statecraft (Devaraja concept) while retaining their own languages, customs, and matrilineal kinship structures."
                    ]
                },
                {
                    "heading": "Enduring Monumental & Epigraphic Legacies",
                    "points": [
                        "Epigraphy and Scripts: Sanskrit inscriptions using Pallava Grantha script found across Funan (Cambodia), Champa (Vietnam), and Java (Indonesia).",
                        "Architectural Wonders: Borobudur (Java, Indonesia) — the world's largest Mahayana Buddhist stupa mandala built by the Sailendra dynasty; Angkor Wat (Cambodia) — the colossal Vishnu temple built by Suryavarman II, depicting Mahabharata and Ramayana friezes.",
                        "Prambanan (Java): Dedicated to the Hindu Trimurti (Brahma, Vishnu, Shiva), representing the zenith of Indonesian temple sculpture."
                    ]
                },
                {
                    "heading": "Living Cultural Continuities",
                    "points": [
                        "Epic Traditions: The Ramayana remains a living performance tradition (e.g., Wayang Kulit shadow puppetry in Indonesia, Ramakien royal ballet in Thailand).",
                        "State Symbols: Garuda is the national emblem of Indonesia and Thailand; Sanskrit vocabulary heavily influences Bahasa Indonesia, Thai, and Khmer.",
                        "Chola Maritime Excursion: The only military naval expedition was Rajendra Chola I's raid on Srivijaya (1025 CE) to protect free trade routes, which established no territorial colony."
                    ]
                }
            ],
            "conclusion": "The Indianization of Southeast Asia stands as one of world history's finest examples of cultural diffusion based on commerce, intellectual sharing, and artistic admiration rather than military coercion.",
            "diagramMapIdea": "Maritime Map Concept: Coromandel & Kalinga Ports -> Bay of Bengal -> Malacca Strait -> Funan (Angkor), Champa, Srivijaya & Majapahit (Borobudur)."
        }
    }
]

# ==============================================================================
# INJECT INTO DATA FILES
# ==============================================================================

# 1. Prelims Questions
with open('data/prelims-questions.json', 'r', encoding='utf-8') as f:
    prelims_data = json.load(f)

existing_p_ids = {q['id'] for q in prelims_data}
added_p = 0
for q in new_prelims:
    if q['id'] not in existing_p_ids:
        prelims_data.append(q)
        added_p += 1

with open('data/prelims-questions.json', 'w', encoding='utf-8') as f:
    json.dump(prelims_data, f, ensure_ascii=False, indent=2)

print(f"Added {added_p} new Prelims questions. Total count now: {len(prelims_data)}")

# 2. Mains Questions
with open('data/mains-questions.json', 'r', encoding='utf-8') as f:
    mains_data = json.load(f)

existing_m_ids = {m['id'] for m in mains_data}
added_m = 0
for m in new_mains:
    if m['id'] not in existing_m_ids:
        mains_data.append(m)
        added_m += 1

with open('data/mains-questions.json', 'w', encoding='utf-8') as f:
    json.dump(mains_data, f, ensure_ascii=False, indent=2)

print(f"Added {added_m} new Mains questions. Total count now: {len(mains_data)}")
