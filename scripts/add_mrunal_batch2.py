import json

with open('data/mains-questions.json', 'r', encoding='utf-8') as f:
    mq = json.load(f)

existing_ids = set(q['id'] for q in mq)
print(f"Current count: {len(mq)}")

BATCH2 = [
    {
        "id": "mains_pyq_2020_01",
        "periodId": "cave-architecture",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2020 GS-1",
        "bookRef": "NCERT Class 11 Fine Arts, Ch. 3; Nitin Singhania, Ch. 1",
        "question": "The rock-cut architecture represents one of the most important sources of our knowledge of early Indian art and history. Discuss.",
        "framework": {
            "intro": "Rock-cut architecture in India, spanning from the Mauryan Barabar caves (3rd c. BCE) to the monolithic Kailasha temple at Ellora (8th c. CE), serves as an enduring lithic archive that chronicles the technological evolution, artistic mastery, and socio-religious transformations of ancient India.",
            "body": [
                {
                    "heading": "Artistic & Architectural Evolution in Rock",
                    "points": [
                        "Mauryan Foundations: Barabar and Nagarjuni caves (Sudama, Lomas Rishi) demonstrate the earliest imitation of wooden architecture in granite with mirror-like Mauryan polish, dedicated to Ajivika ascetics.",
                        "Buddhist Chaitya-Vihara Complexes: Hinayana and Mahayana rock-cut architecture at Karle, Bhaja, Kanheri, and Ajanta reveal the transition from aniconic stupa worship to iconic Buddha representation and narrative Jataka wall murals.",
                        "Monolithic Structural Climax: Cave 16 (Kailash Temple) at Ellora under Rashtrakuta Krishna I represents the world's greatest top-down vertical excavation, recreating Mount Kailasha from a single basalt cliff."
                    ]
                },
                {
                    "heading": "Historical & Socio-Economic Reflections",
                    "points": [
                        "Trade Routes & Merchant Guilds: Rock-cut caves along Western Ghat passes (Bhor Ghat, Thal Ghat) directly mapped ancient trade arteries (Kalyan, Sopara to Paithan), financed by merchant guilds (Dhammakathikas, Shrenis).",
                        "Epigraphic Records: Hundreds of donor inscriptions (Vakatakas, Satavahanas, royal queens, monks, and goldsmiths) record the socio-religious patronage networks of ancient India.",
                        "Religious Harmony: Ellora's 34 caves uniquely integrate Buddhist (1–12), Hindu (13–29), and Jain (30–34) sanctuaries side by side, proving institutional syncretism."
                    ]
                }
            ],
            "conclusion": "Carved out of living rock, these monuments have outlived wooden and brick structures, serving as an indestructible visual encyclopedia of India's aesthetic genius and spiritual heritage.",
            "diagramMapIdea": "Chronological Arrow: Barabar (Mauryan Polish) ──▶ Western Ghat Chaityas (Karle/Bhaja) ──▶ Ajanta (Murals & Viharas) ──▶ Ellora Kailash (Monolithic Climax)"
        }
    },
    {
        "id": "mains_pyq_2020_02",
        "periodId": "early-medieval-period",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2020 GS-1",
        "bookRef": "R.S. Sharma, Ch. 28; Upinder Singh, Ch. 9",
        "question": "Pala period is the most significant phase in the history of Buddhism in India. Enumerate.",
        "framework": {
            "intro": "The Pala Empire of Bengal and Bihar (c. 8th–12th century CE) represented the final, glorious Indian summer and institutional refuge of Buddhism in its homeland, transforming Eastern India into the intellectual and spiritual capital of the Asian Buddhist world.",
            "body": [
                {
                    "heading": "Imperial Monastic Foundations (Mahaviharas)",
                    "points": [
                        "Foundation of Global Universities: Gopala revived Nalanda; Dharmapala founded Vikramashila (Bhagalpur) and Somapura (Paharpur, UNESCO World Heritage); Devapala patronized Odantapuri and Jagaddala.",
                        "Global Buddhist Confluence: Monasteries attracted scholars from Tibet, China, Southeast Asia, and Sri Lanka; Balaputradeva (Sailendra king of Sumatra) endowed a monastery at Nalanda via copper plate grant."
                    ]
                },
                {
                    "heading": "Doctrinal Evolution & Cultural Dissemination",
                    "points": [
                        "Evolution of Vajrayana & Tantric Buddhism: Shift from classic Mahayana to esoteric Vajrayana (Diamond Vehicle), synthesizing ritual mandalas, mudras, and mantras.",
                        "Missionary Dissemination to Tibet: Atisha Dipankara Srijnana and Santaraksita journeyed from Vikramashila to Tibet, founding the second dissemination of Tibetan Buddhism (Lamaism).",
                        "Pala School of Art: Master sculptors Dhiman and Vitapala developed exquisite, highly polished black basalt sculptures and illustrated palm-leaf Buddhist manuscripts (Ashtasahasrika Prajnaparamita)."
                    ]
                }
            ],
            "conclusion": "Through unmatched imperial patronage, monastic institution-building, and international missionary exchange, the Palas immortalized Buddhist scholasticism and safeguarded its sacred teachings before the destruction of Nalanda in the late 12th century.",
            "diagramMapIdea": "Pala Buddhist Matrix: [Dharmapala/Devapala Patronage] ──▶ [Nalanda & Vikramashila Universities] ──▶ [Vajrayana Philosophy] ──▶ [Atisha to Tibet & Sailendras of Sumatra]"
        }
    },
    {
        "id": "mains_pyq_2020_03",
        "periodId": "colonial-administration",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2020 GS-1",
        "bookRef": "Spectrum, Ch. 12; Bipan Chandra, Ch. 10",
        "question": "Evaluate the policies of Lord Curzon and their long-term implications on the national movement.",
        "framework": {
            "intro": "Lord Curzon (Viceroy 1899–1905), the consummate imperialist whom Lord Rosebery called 'the magnificent autocrat', pursued an aggressive policy of centralized bureaucratic efficiency that, paradoxically, galvanized Indian national consciousness and hastened the end of British rule.",
            "body": [
                {
                    "heading": "Curzon's Autocratic Imperial Policies",
                    "points": [
                        "Calcutta Corporation Act (1899): Slashed elected Indian representation, reducing municipal self-governance to an official Anglo-Indian oligarchy.",
                        "Indian Universities Act (1904): Imposed stringent official controls over university senates and higher education, which Curzon viewed as 'nurseries of sedition'.",
                        "Official Secrets Act (1904): Curtailed freedom of the nationalist press by expanding definitions of treason.",
                        "Partition of Bengal (1905): Ostensibly for administrative efficiency, but explicitly designed to divide Bengal along communal lines (Muslim East vs Hindu West) to blunt the vanguard of Indian nationalism."
                    ]
                },
                {
                    "heading": "Long-Term Implications on the National Movement",
                    "points": [
                        "Birth of Mass Agitation (Swadeshi & Boycott): The Anti-Partition movement moved nationalism out of drawing rooms onto the streets; introduced picketing, bonfire of foreign cloth, and national schools.",
                        "Rise of Extremism & Surat Split: Radicalized youth rejected the 'mendicancy' of Moderates, elevating Extremist leaders (Lal-Bal-Pal, Aurobindo Ghosh) and culminating in the 1907 Surat Split.",
                        "Spawned Revolutionary Nationalism: Humiliation over Curzon's partition triggered the first wave of revolutionary societies (Anushilan Samiti, Jugantar).",
                        "Inadvertent Unification of National Resolve: Curzon acted as the 'unconscious catalyst' of Indian nationhood, uniting disparate regional groups against imperial insolence."
                    ]
                }
            ],
            "conclusion": "Curzon aimed to throttle Indian nationalism; instead, his reactionary policies radicalized it, transforming the freedom struggle from polite constitutional appeals into a militant mass movement for Purna Swaraj.",
            "diagramMapIdea": "Curzon Policies (Corporation Act, Universities Act, Bengal Partition 1905) ──▶ National Reactions (Swadeshi & Boycott, Rise of Extremism, Revolutionary Societies, Pan-Indian Consciousness)"
        }
    },
    {
        "id": "mains_pyq_2019_01",
        "periodId": "sculptural-schools",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2019 GS-1",
        "bookRef": "Nitin Singhania, Ch. 2; Upinder Singh, Ch. 8",
        "question": "Highlight the Central Asian and Greco-Bactrian elements in the Gandhara art.",
        "framework": {
            "intro": "Gandhara art (c. 1st century BCE to 4th century CE), flourishing in the north-western borderlands (Peshwar, Taxila, Swat) under Indo-Greek, Shaka, and Kushana patronage, represents an extraordinary syncretic synthesis: Indian Buddhist iconography embodied in Hellenistic and Greco-Roman classical forms.",
            "body": [
                {
                    "heading": "Greco-Bactrian & Hellenistic Anatomical Realism",
                    "points": [
                        "Apollo-like Depiction of the Buddha: The Buddha is rendered with the idealized masculine facial contours of Greek god Apollo—sharp aquiline nose, defined cheekbones, and wavy or curly hair arranged in an ushnisha.",
                        "Drapery & Toga-like Garments: Heavy, realistic drapery folds falling in deep rhythmic cascades over both shoulders, reminiscent of Roman togas, revealing anatomical contours underneath.",
                        "Musculature & Physical Proportions: Realistic rendering of skeletal and muscular anatomy, prominent in the iconic 'Fasting Siddhartha' of Swat (Lahore Museum) with protruding ribs and sunken abdomen."
                    ]
                },
                {
                    "heading": "Central Asian, Roman & Decorative Motifs",
                    "points": [
                        "Central Asian Kushana Attire: Donor figures and Bodhisattvas depicted wearing heavy nomadic Central Asian coats, tunics, trousers, and riding boots.",
                        "Western Classical Motifs: Decorative use of Corinthian capitals, acanthus leaves, marine centaurs, cupids bearing garlands, and cherubs.",
                        "Materials: Use of local grey-blue schist stone, green phyllite, and later stucco and terracotta."
                    ]
                }
            ],
            "conclusion": "Gandhara art was an aesthetic bridge between East and West: while its heart and soul were deeply Buddhist, its artistic vocabulary was Hellenistic, reflecting the cosmopolitan cross-roads of the ancient Silk Route.",
            "diagramMapIdea": "Gandhara Fusion: [Buddhist Iconography (Ushnisha, Urna, Dhyana Mudra)] + [Greco-Roman Aesthetics (Apollo face, Wavy hair, Heavy Toga drapery, Corinthian capitals)]"
        }
    },
    {
        "id": "mains_pyq_2019_02",
        "periodId": "revolt-of-1857",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2019 GS-1",
        "bookRef": "Bipan Chandra, Ch. 1 & 4; Spectrum, Ch. 6 & 7",
        "question": "The 1857 Uprising was the culmination of the recurrent big and small local rebellions that had occurred in the preceding hundred years of British rule. Elucidate.",
        "framework": {
            "intro": "The Great Revolt of 1857 was neither an isolated sepoy mutiny nor an abrupt historical accident; it was the explosive volcanic culmination of a century-long continuum of armed civil, peasant, and tribal rebellions against British territorial conquest and economic drain from 1757 to 1856.",
            "body": [
                {
                    "heading": "Pre-1857 Precursor Rebellions (Civil & Religious)",
                    "points": [
                        "Sanyasi-Fakir Rebellion (Bengal, 1763–1800): Displaced peasants and religious ascetics fought against British revenue exactions and famine devastation, celebrated in Bankim Chandra's Anandamath.",
                        "Paika Rebellion (Odisha, 1817): Armed landed militia of the Gajapati kingdom led by Bakshi Jagabandhu revolted against British land resumption and the oppressive salt tax.",
                        "South Indian Poligar Wars (1799–1805): Kattabomman and Marudu brothers resisted British sovereignty in Tirunelveli and Malabar.",
                        "Wahabi & Faraizi Movements (1820s–1840s): Religious reform movements transforming into anti-landlord and anti-British agrarian resistance in Bengal and northern India."
                    ]
                },
                {
                    "heading": "Tribal Uprisings (The Vanguard of Militant Resistance)",
                    "points": [
                        "Chuar and Ho Uprisings (1768–1820): Armed resistance by jungle tribes against the penetration of British zamindars.",
                        "Kol Mutiny (Chota Nagpur, 1831–32): Under Buddho Bhagat, resisting British judicial laws and outsider moneylenders (Dikus).",
                        "Santhal Hul (1855–56): Just eighteen months before 1857, Sidhu and Kanhu mobilized 60,000 Santhals with bows and arrows against British revenue police and Bengali mahajans."
                    ]
                }
            ],
            "conclusion": "The 1857 Revolt coalesced the smoldering subterranean embers of a hundred localized rebellions into a single massive anti-colonial conflagration, uniting sepoys, dispossessed princes, and impoverished peasants in a desperate bid to overthrow foreign rule.",
            "diagramMapIdea": "Century of Resistance (1757-1857): Sanyasi (1763) ──▶ Poligars (1799) ──▶ Paika (1817) ──▶ Kol (1831) ──▶ Santhal Hul (1855) ──▶ Great Revolt of 1857"
        }
    },
    {
        "id": "mains_pyq_2016_01",
        "periodId": "stupa-architecture",
        "marks": 15,
        "wordLimit": 250,
        "isPyq": True,
        "yearSource": "UPSC CSE 2016 GS-1",
        "bookRef": "NCERT Class 11 Fine Arts, Ch. 2; Upinder Singh, Ch. 7",
        "question": "Early Buddhist stupa-art, while depicting folk motifs and narratives successfully expounds Buddhist ideals. Elucidate.",
        "framework": {
            "intro": "Early Buddhist stupa art (Bharhut, Sanchi, Amaravati, c. 3rd c. BCE to 2nd c. CE) represents an extraordinary visual dialogue between high Buddhist philosophical dogma and exuberant indigenous folk traditions, creating an open-air stone sermon accessible to literate monks and lay peasants alike.",
            "body": [
                {
                    "heading": "Assimilation of Indigenous Folk Motifs",
                    "points": [
                        "Yakshas & Yakshis: Nature spirits and fertility deities absorbed as guardian deities; the sensuous Salabhanjika (bracket maiden clinging to a flowering mango tree) on Sanchi toranas symbolizes fertility and cosmic auspiciousness.",
                        "Animal & Floral Motifs: Elephants, lions, deer, makaras (sea monsters), and meandering lotus creepers (Kalpalatas) celebrate the sacred interconnectedness of all life.",
                        "Naga & Tree Cults: Serpent kings paying homage to the Buddha, preserving pre-Aryan animistic nature reverence within a Buddhist framework."
                    ]
                },
                {
                    "heading": "Expounding Core Buddhist Ideals through Folk Art",
                    "points": [
                        "Aniconic Symbolism of Enlightenment: In accordance with early Buddhist non-anthropomorphic tenets, the Buddha's presence was visualized through sacred symbols: Footprints (Paduka), Empty Throne, Bodhi Tree, Wheel of Law (Dharmachakra), and Stupa.",
                        "Visual Jataka Storytelling: Continuous narrative panels depicting previous lives of the Buddha: Vessantara Jataka (supreme generosity), Shibi Jataka (compassion for all creatures), and Chhadanta Jataka (forgiveness).",
                        "Democratization of Spiritual Path: The synthesis of folk motifs enabled ordinary lay devotees (Upasakas) to grasp the core Buddhist ethics of Ahimsa, Karuna, and Dana without wading through complex Pali canonical philosophy."
                    ]
                }
            ],
            "conclusion": "By sanctifying folk symbols and wrapping lofty spiritual truths in the familiar artistic vocabulary of the soil, early stupa art achieved the peaceful conversion of ancient India, making Buddhism a truly universal mass religion.",
            "diagramMapIdea": "Stupa Art Synthesis: [Folk Layer: Yakshis, Makaras, Lotus Creepers, Naga Cults] + [Buddhist Core: Jataka Narratives, Dharmachakra, Aniconic Symbols, Compassion Ethics]"
        }
    },
    {
        "id": "mains_pyq_2016_02",
        "periodId": "vijayanagara-empire",
        "marks": 15,
        "wordLimit": 250,
        "isPyq": True,
        "yearSource": "UPSC CSE 2016 GS-1",
        "bookRef": "Satish Chandra, Ch. 9; Nilakanta Sastri, History of South India",
        "question": "Krishnadeva Raya, the King of Vijayanagar, was not only an accomplished scholar himself but was also a great patron of learning and literature. Discuss.",
        "framework": {
            "intro": "Emperor Krishnadeva Raya of Vijayanagara (reigned 1509–1529 CE, Tuluva dynasty), hailed with titles like 'Andhra Bhoja' and 'Sahiti Samarangana Sarvabhauma' (Emperor of Literature and Warfare), presided over the golden age of South Indian literature, combining personal scholarly genius with munificent multilingual patronage.",
            "body": [
                {
                    "heading": "Krishnadeva Raya's Personal Literary Genius",
                    "points": [
                        "Masterpiece Amuktamalyada (Telugu): Regarded as one of the five great Telugu Mahakavyas; narrates the life of Andal (Periyalvar's daughter) and expounds mature political statecraft (Raja-niti) in the fourth canto.",
                        "Sanskrit Treatises: Composed the drama Jambavati Kalyanam and Usha Parinayam, demonstrating equal fluency in Sanskrit classical grammar.",
                        "Statecraft Maxims: Amuktamalyada contains profound governance principles: protecting merchants, digging irrigation tanks, patronizing scholars, and treating conquered subjects with justice."
                    ]
                },
                {
                    "heading": "Imperial Patronage & The Ashtadiggajas",
                    "points": [
                        "The Ashtadiggajas (Eight Literary Pillars): Assembled eight literary giants in his court assembly hall (Bhuvana Vijayam):",
                        "Allasani Peddana: The 'Andhra Kavita Pitamaha' (Father of Telugu Poetry), author of Manucharitram; Krishnadeva Raya personally lifted Peddana's palanquin in tribute.",
                        "Nandi Thimmana: Authored Parijatapaharanam in graceful lyrical style.",
                        "Tenali Ramakrishna: Renowned for wit, political counsel, and the masterpiece Panduranga Mahatmyam.",
                        "Multilingual Patronage: Lavished grants on Kannada poets (Kumara Vyasa's Mahabharata completed), Tamil poets (Haridasa), and Sanskrit philosophers (Vyasatirtha, Dvaita guru)."
                    ]
                }
            ],
            "conclusion": "Krishnadeva Raya personified the classical Indian ideal of the philosopher-king (Rajarshi), whose pen was as mighty as his sword, leaving a literary legacy that continues to define Telugu and South Indian cultural consciousness.",
            "diagramMapIdea": "Krishnadeva Raya Heritage: [Personal Works: Amuktamalyada (Telugu), Jambavati Kalyanam (Sanskrit)] + [Bhuvana Vijayam Court: Ashtadiggajas (Peddana, Thimmana, Tenali Rama)]"
        }
    },
    {
        "id": "mains_pyq_2014_01",
        "periodId": "maratha-empire",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2014 GS-1",
        "bookRef": "B.L. Grover, Marathas; Satish Chandra, Ch. 17",
        "question": "The third battle of Panipat was fought in 1761. Why were so many empire-shaking battles fought at Panipat?",
        "framework": {
            "intro": "Panipat, a plain in modern Haryana situated approximately 90 km north of Delhi, witnessed three decisive battles that altered the destiny of India: 1526 (Babur overthrew Ibrahim Lodi), 1556 (Akbar defeated Hemu), and 1761 (Ahmad Shah Abdali crushed the Marathas).",
            "body": [
                {
                    "heading": "Geographical & Strategic Gateway to Delhi",
                    "points": [
                        "Natural Frontier of the Gangetic Plain: Invaders entering through the north-western passes (Khyber, Bolan) had to pass through Punjab before reaching the imperial prize of Delhi. Panipat formed the natural threshold where defenders could intercept invaders before Delhi's walls.",
                        "Grand Trunk Road Conduit: Panipat lay directly on the historic Uttarapatha / Shershah Suri Marg, ensuring smooth paved movement for massive supply wagons and siege artillery."
                    ]
                },
                {
                    "heading": "Topographical, Logistical & Seasonal Factors",
                    "points": [
                        "Flat Open Plains for Cavalry Maneuver: The vast, level, tree-free plains of Panipat were ideally suited for large-scale cavalry maneuvers, war-elephant charges, and field cannon deployments.",
                        "Agrarian Hinterland & Logistics: The fertile Yamuna-Ganga doab surrounding Panipat provided ample standing foodgrains, fodder for thousands of horses, and water during dry winter campaigning months.",
                        "Shorter Supply Lines for North-Western Invaders: Invaders (Babur, Abdali) enjoyed secure rear communication lines back to Kabul/Kandahar, whereas southern or eastern defenders fought far from their home bases."
                    ]
                }
            ],
            "conclusion": "Panipat was the geopolitical boxing ring of northern India—a flat, logistically rich, strategic bottleneck where imperial ambitions collided to decide the ruler of Hindustan.",
            "diagramMapIdea": "Panipat Strategic Choke-Point: [Hindu Kush Passes ──▶ Punjab Plains] ──▶ [PANIPAT BATTLEGROUND] ──▶ [DELHI IMPERIAL SEAT]"
        }
    },
    {
        "id": "mains_pyq_2013_01",
        "periodId": "post-mauryan-period",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2013 GS-1",
        "bookRef": "R.S. Sharma, Ch. 24; K.A. Nilakanta Sastri, Sangam Literature",
        "question": "Though not very useful from the point of view of a connected political history of South India, the Sangam literature portrays the social and economic conditions of its time with remarkable fairness. Discuss.",
        "framework": {
            "intro": "Sangam literature (c. 3rd century BCE to 3rd century CE), compiled across the Ettutogai (Eight Anthologies) and Pattuppattu (Ten Idylls), lacks coherent dynastic chronologies or kingly dates, but constitutes an exceptionally vivid, realistic, and unvarnished socio-economic mirror of early Tamilakam.",
            "body": [
                {
                    "heading": "Economic Prosperity & Maritime Commerce",
                    "points": [
                        "Ecological Agrarian Economy: Meticulous classification into 5 Tinais (Kurinji, Mullai, Marudam, Neydal, Palai) documenting specialized subsistence (paddy farming, cattle herding, pearl diving, salt pans).",
                        "Flourishing Indo-Roman Trade: Vivid descriptions of foreign Yavanas (Romans/Greeks) arriving in gold-laden ships at Puhar (Kaveripattinam) and Muziris, exchanging Roman gold and silver denarii for black pepper (Yavanapriya), pearls, beryl, and fine textiles.",
                        "Artisan Specialization: References to weavers, goldsmiths, shipwrights, and bustling night markets (Allangadi) and day markets (Nalangadi)."
                    ]
                },
                {
                    "heading": "Social Stratification & Everyday Life",
                    "points": [
                        "Absence of Rigid Aryan Varna: Society was organized around occupational and lineage groups (Kudi) rather than orthodox fourfold varna: Vellalars (landlords), Karalars (cultivators), Paratavars (fisherfolk), and Panars (wandering bards).",
                        "Position of Women: Active in economic life and poetry (30+ female poets including Avvaiyar); yet customs like sati (Tippaydal), strict widow codes, and ascetic mourning were emerging.",
                        "Heroic Ethos & Hero Stones (Nadukal): Honoring warriors slain in battle or cattle raids, reflecting a vibrant heroic clan culture."
                    ]
                }
            ],
            "conclusion": "While deficient as political dynastic chronicles, the Sangam poems are unmatched in ancient Indian literature for their realistic secular portraiture of agrarian life, maritime wealth, and social egalitarianism.",
            "diagramMapIdea": "Sangam Socio-Economic Spectrum: [5 Ecological Tinais] ──▶ [Yavana Maritime Trade (Muziris/Puhar)] ──▶ [Clan Society (Vellalar/Panar/Nadukal Hero Stones)]"
        }
    }
]

# Append BATCH2 to mains_questions
count_added = 0
for q in BATCH2:
    if q['id'] not in existing_ids:
        # Validate diagramMapIdea
        if 'diagramMapIdea' not in q['framework']:
            q['framework']['diagramMapIdea'] = "Chronological flowchart or thematic diagram."
        mq.append(q)
        existing_ids.add(q['id'])
        count_added += 1

print(f"Added {count_added} questions. Total Mains questions now: {len(mq)}")

with open('data/mains-questions.json', 'w', encoding='utf-8') as f:
    json.dump(mq, f, ensure_ascii=False, indent=2)

print("Saved mains-questions.json successfully!")
