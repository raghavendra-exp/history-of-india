# -*- coding: utf-8 -*-
"""
Enrich data/history.json with canonical periods covering the user's detailed syllabus:
1. sources-and-historiography
2. early-medieval-india-750-1200
3. bhakti-sufi-movements
4. eighteenth-century-transition-and-regional-states
5. colonial-economy-and-drain-of-wealth
6. revolutionary-nationalism-and-ina
"""
import json
import os

with open('data/history.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_ids = {p['id'] for p in data['periods']}
print(f"Existing periods: {len(existing_ids)}")

NEW_PERIODS = [
    {
        "id": "sources-and-historiography",
        "order": 1,
        "title": "Sources of Indian History & Historiography",
        "dateRange": "Antiquity to Modern Historiographical Debates",
        "category": "ancient",
        "tagline": "Epigraphy – Numismatics – Archaeology – Literary Classics – Colonial vs Marxist vs Subaltern Historiography",
        "heroImg": "prehistoric_age.png",
        "sourceImages": ["prehistoric_age.png", "indus_valley.png"],
        "overview": "The reconstruction of India's past relies upon a multifaceted synthesis of archaeological excavations, epigraphical inscriptions, numismatic evidence, indigenous literary traditions, and accounts of foreign travellers. Historiography has evolved dynamically over two centuries: from the early Colonial/Imperialist framework (James Mill, Vincent Smith) asserting oriental despotism and civilizing missions, to the Nationalist school (K.P. Jayaswal, R.C. Majumdar) celebrating ancient democratic assemblies and cultural golden ages. The post-independence Marxist materialist approach (D.D. Kosambi, R.S. Sharma, Romila Thapar) shifted the paradigm toward agrarian relations, social stratification, and the feudalism debate. Concurrently, the Subaltern Studies collective (Ranajit Guha) recovered marginalized peasant and tribal voices, while recent revisionist environmental and maritime scholarship explores climate shifts and Indian Ocean trading webs.",
        "phases": [
            {
                "name": "Archaeological & Scientific Methods",
                "range": "1861 (ASI Foundation) – Present",
                "points": [
                    "Stratigraphy, Radiocarbon (C-14), Thermoluminescence (TL), and AMS Dating.",
                    "Underwater archaeology at Dwarka and Lothal dockyard confirming maritime port infrastructure.",
                    "Sanauli (Baghpat) excavations uncovering copper-hoard era royal burials, solid-disc wheel chariots, and antennae swords."
                ]
            },
            {
                "name": "Epigraphical & Numismatic Decipherment",
                "range": "1837 (James Prinsep) – Present",
                "points": [
                    "James Prinsep deciphered Brahmi (1837) and Kharosthi scripts, unlocking Ashoka's Edicts.",
                    "Punch-Marked Coins (Ahat/Karshapana) of the Mahajanapada era carrying punch symbols (sun, six-armed symbol, hill, peacock).",
                    "Indo-Greek bilingual coins introducing royal portraits and Greek/Kharosthi legends; Kushana gold dinars reflecting Silk Route prosperity; Gupta gold coins (Dinaras) as mirrors of economic efflorescence."
                ]
            },
            {
                "name": "Historiographical Schools & Paradigm Shifts",
                "range": "Late 18th Century – 21st Century",
                "points": [
                    "Colonial/Orientalist: Asiatic Society of Bengal (William Jones, 1784), Max Muller, James Mill's tripartite communal periodization (Hindu, Muslim, British).",
                    "Nationalist: Refuted Asiatic despotism; highlighted ancient Republics (Ganasanghas) and maritime expansions.",
                    "Marxist & Subaltern: Kosambi's 'Introduction to the Study of Indian History' combining archaeology with ethnography; Ranajit Guha's subaltern agency in subverting colonial power."
                ]
            }
        ],
        "events": [
            {
                "year": "1837 CE",
                "title": "Decipherment of Ashokan Brahmi Script",
                "desc": "James Prinsep, founding secretary of Asiatic Society of Bengal, successfully deciphers the ancient Brahmi script on Ashokan edicts, identifying King Devanampiya Piyadassi as Emperor Ashoka.",
                "theme": "culture"
            },
            {
                "year": "1861 CE",
                "title": "Establishment of the Archaeological Survey of India (ASI)",
                "desc": "Alexander Cunningham appointed as the first Director-General of ASI, launching systematic archaeological surveys across northern India.",
                "theme": "society"
            },
            {
                "year": "1956 CE",
                "title": "Publication of D.D. Kosambi's Landmark Marxist Synthesis",
                "desc": "D.D. Kosambi publishes 'An Introduction to the Study of Indian History', pioneering Marxist historiography focused on means of production, technological shifts, and social formations.",
                "theme": "economy"
            }
        ],
        "people": [
            {
                "name": "James Prinsep",
                "role": "Antiquarian & Epigraphist (1799–1840)",
                "note": "Deciphered Brahmi and Kharosthi scripts, unlocking Ashoka's inscriptions and establishing ancient Indian chronology.",
                "isWomen": False
            },
            {
                "name": "Prof. Romila Thapar",
                "role": "Foremost Ancient Indian Historian (b. 1931)",
                "note": "Pioneered critical social and cultural historiography on the Mauryas, early India, and historical traditions.",
                "isWomen": True
            },
            {
                "name": "Alexander Cunningham",
                "role": "Father of Indian Archaeology (1814–1893)",
                "note": "First Director-General of ASI; mapped ancient sites along Xuanzang's travel itineraries.",
                "isWomen": False
            }
        ],
        "women": [
            {
                "name": "Prof. Romila Thapar",
                "role": "Eminent Historian of Ancient India",
                "note": "Author of landmark works 'Asoka and the Decline of the Mauryas' and 'From Lineage to State'; revolutionized the study of early Indian social formations.",
                "isWomen": True
            }
        ],
        "themes": ["culture", "polity", "economy", "society"],
        "upsc": {
            "prelims": [
                "Brahmi was deciphered by James Prinsep in 1837; Kharosthi script was written from right to left.",
                "Allahabad Pillar Inscription (Prayag Prashasti) was composed in chaste classical Sanskrit (Champukavya style) by court poet Harishena for Samudragupta.",
                "Aihole Inscription in Karnataka was composed by Ravikirti, court poet of Chalukya King Pulakeshin II, recording the defeat of Harshavardhana on the Narmada banks.",
                "Earliest coins of India are Punch-Marked Silver Coins (Puranas/Karshapanas) of 6th century BCE, carrying stamped symbols without royal portraits or inscriptions.",
                "James Mill's 'The History of British India' (1817) first introduced the communal division into Hindu Period, Muslim Period, and British Period."
            ],
            "mains": [
                "Critically evaluate the contribution of epigraphy and numismatics in reconstructing the socio-economic history of ancient India.",
                "Trace the evolution of Indian historiography from colonial-imperialist interpretations to Marxist and subaltern approaches."
            ]
        },
        "quickFacts": {
            "First ASI Director-General": "Alexander Cunningham (1861)",
            "Decipherer of Brahmi": "James Prinsep (1837)",
            "Key Prashastis": "Prayag Prashasti (Gupta), Aihole (Chalukya), Junagadh (Rudradaman)",
            "Earliest Coinage": "Punch-Marked Silver Coins (c. 6th Century BCE)",
            "Prominent Foreign Travellers": "Megasthenes (Greek), Faxian & Xuanzang (Chinese), Al-Biruni (Arab)"
        },
        "aspects": {
            "Epigraphy & Inscriptions": [
                "Ashokan Edicts: Inscribed in Prakrit language using Brahmi script across core areas; Kharosthi in North-West (Mansehra, Shahbazgarhi); Greek and Aramaic in Kandahar (bilingual edict).",
                "Royal Prashastis: Junagadh Rock Inscription of Rudradaman (150 CE) in pure classical Sanskrit recording repairs to Sudarshana Lake; Prayag Prashasti of Samudragupta; Aihole Prashasti of Pulakeshin II.",
                "Copper-Plate Land Grants (Tamra-shasana): Commencing with Satavahanas (1st century BCE) and proliferating under Guptas and early medieval dynasties, recording Agrahara/Brahmadeya tax exemptions."
            ],
            "Numismatics & Economic Indicators": [
                "Punch-Marked Coins: Stamped with 5 symbols, silver standard of 32 ratis (56 grains), issued by merchant guilds (Shrenis) and Janapadas.",
                "Indo-Greek Coins: First to bear portraiture of kings and bilingual legends (Greek obverse, Kharosthi reverse) like Menander/Milinda.",
                "Kushana Gold Standard: Introduced high-purity gold dinars modelled on Roman denarii, reflecting thriving trade along the overland Silk Route and maritime ports.",
                "Gupta Gold Coins: Issued in diverse motifs (Archer, Tiger Slayer, Lyrist/Veena player, Ashvamedha); debasement of gold in later Gupta issues under Skandagupta reflects economic strain."
            ],
            "Indigenous Literature & Scientific Treatises": [
                "Vedic Literature: Rigveda (1028 hymns), Samaveda (melodies), Yajurveda (rituals), Atharvaveda (charms); 6 Vedangas (Shiksha, Kalpa, Vyakarana, Nirukta, Chhanda, Jyotisha).",
                "Buddhist & Jain Canons: Pali Tripitakas (Vinaya, Sutta, Abhidhamma) and 547 Jataka tales; Jain Agamas compiled at Vallabhi council in Ardhamagadhi Prakrit.",
                "Scientific Treatises: Aryabhata's Aryabhatiya (astronomy, zero concept, earth's rotation); Varahamihira's Panchasiddhantika and Brihatsamhita; Charaka Samhita (medicine) and Sushruta Samhita (surgery)."
            ],
            "Foreign Travel Accounts": [
                "Greco-Roman: Megasthenes' Indica (Mauryan society, 7 castes, municipal board of Pataliputra); Periplus of the Erythraean Sea (maritime ports: Barygaza/Bharuch, Muziris, Arikamedu); Ptolemy's Geography.",
                "Chinese Buddhist Pilgrims: Faxian (c. 405–411 CE, Gupta era peaceful governance); Xuanzang (c. 629–645 CE, Harsha's court, Kannauj and Nalanda University); Yijing (c. 671–695 CE).",
                "Arab Chroniclers: Al-Biruni's Kitab-ul-Hind (Tahqiq-i-Hind, 1030 CE), encyclopedic analysis of Indian astronomy, philosophy, social stratification, and caste isolation."
            ],
            "Historiographical Schools": [
                "Colonial/Imperialist: Utilized history to justify Pax Britannica; portrayed Indian society as stagnant, unhistorical, and dependent on benevolent despotism.",
                "Nationalist: Emerged during the freedom struggle; defended Indian civilization against racial disparagement; highlighted constitutional assemblies (Sabha, Samiti) and cultural resilience.",
                "Marxist Paradigm: Replaced political dynasties with modes of production; pioneered by D.D. Kosambi and R.S. Sharma; analyzed urban decay, monetisation shifts, and peasant subjection.",
                "Subaltern Studies: Founded by Ranajit Guha; shifted focus from elite Congress/British negotiations to the autonomous political consciousness of subaltern peasants, tribals, and working classes."
            ]
        }
    },
    {
        "id": "early-medieval-india-750-1200",
        "order": 11,
        "title": "Early Medieval India & The Feudalism Debate (c. 750 – 1200 CE)",
        "dateRange": "c. 750 – 1200 CE",
        "category": "medieval",
        "tagline": "Indian Feudalism – Tripartite Struggle – Arab Conquest of Sindh – Ghaznavid & Ghorid Invasions",
        "heroImg": "early_medieval.png",
        "sourceImages": ["early_medieval.png", "delhi_sultanate.png"],
        "overview": "The Early Medieval period (c. 750 – 1200 CE) bridges classical antiquity and the establishment of the Delhi Sultanate. Historiographically, it is dominated by the 'Indian Feudalism' debate (propounded by R.S. Sharma): the proliferation of land grants (Brahmadeya and Agrahara) accompanied by surrender of fiscal and judicial rights, the rise of intermediaries (Samantas, Ranaks), sub-infeudation, peasant immobility (Vishti/forced labour), and urban contraction. In North India, the Tripartite Struggle between the Palas of Bengal, Gurjara-Pratiharas of Malwa, and Rashtrakutas of the Deccan contested paramountcy over Kannauj. Concurrently, regional Rajput clans crystallized. External shocks arrived with the Arab conquest of Sindh (712 CE) under Muhammad bin Qasim, followed by Mahmud of Ghazni's economic raids (1000–1027 CE, sacking Somnath), and Muhammad Ghori's decisive victories at the Battles of Tarain (1191 and 1192 CE), which shattered Rajput military resistance.",
        "phases": [
            {
                "name": "The Tripartite Struggle for Kannauj",
                "range": "c. 750 – 950 CE",
                "points": [
                    "Palas of Bengal (Gopala, Dharmapala, Devapala) patronizing Mahayana/Vajrayana Buddhism at Nalanda and Vikramashila.",
                    "Gurjara-Pratiharas (Nagabhata I, Vatsaraja, Mihira Bhoja) defending western borders against Arab incursions.",
                    "Rashtrakutas (Dantidurga, Dhruva, Govinda III, Amoghavarsha) crossing the Vindhyas, capturing Kannauj, and constructing the monolithic Kailasa Temple at Ellora."
                ]
            },
            {
                "name": "Rajput Clan Crystallization & Feudal Ethos",
                "range": "c. 900 – 1200 CE",
                "points": [
                    "Chauhans/Chahamanas of Shakambhari and Ajmer (Prithviraj Chauhan III).",
                    "Paramaras of Malwa (Raja Bhoja, patron of arts and Bhojpur temple).",
                    "Chandellas of Bundelkhand (Khajuraho temples) and Gahadavalas of Kannauj (Jaichand)."
                ]
            },
            {
                "name": "Arab & Turkish Invasions",
                "range": "712 – 1192 CE",
                "points": [
                    "712 CE: Muhammad bin Qasim conquers Sindh and Multan, introducing the first Jizya tax on non-Muslims in India.",
                    "1000–1027 CE: Mahmud of Ghazni conducts 17 plunder raids, targeting temple wealth at Nagarkot, Mathura, Kannauj, and Somnath (1026 CE).",
                    "1191 & 1192 CE: First and Second Battles of Tarain; Muhammad Ghori defeats Prithviraj Chauhan III, establishing Turkish imperial dominance in North India."
                ]
            }
        ],
        "events": [
            {
                "year": "712 CE",
                "title": "Arab Conquest of Sindh under Muhammad bin Qasim",
                "desc": "Umayyad general Muhammad bin Qasim defeats Raja Dahir at the Battle of Rawar, establishing Arab rule in Sindh and introducing Jizya tax.",
                "theme": "polity"
            },
            {
                "year": "1026 CE",
                "title": "Mahmud of Ghazni's Sack of Somnath Temple",
                "desc": "Mahmud of Ghazni plunders the wealthy Shiva temple of Somnath on the Saurashtra coast of Gujarat, carrying away enormous temple treasures to Ghazni.",
                "theme": "economy"
            },
            {
                "year": "1192 CE",
                "title": "Second Battle of Tarain",
                "desc": "Muhammad Ghori decisively defeats Prithviraj Chauhan III at Tarain (Haryana) using superior mounted archer tactics, opening Delhi and the Gangetic plains to Turkish conquest.",
                "theme": "polity"
            }
        ],
        "people": [
            {
                "name": "Prithviraj Chauhan III",
                "role": "Chahamana King of Delhi & Ajmer (1166–1192 CE)",
                "note": "Hero of Chand Bardai's epic Prithviraj Raso; won the First Battle of Tarain (1191), defeated in the Second Battle (1192).",
                "isWomen": False
            },
            {
                "name": "Dharmapala",
                "role": "Pala Emperor of Bengal (c. 770–810 CE)",
                "note": "Great patron of Buddhism; founded the monastic university of Vikramashila and Somapura Mahavihara.",
                "isWomen": False
            },
            {
                "name": "Raja Bhoja",
                "role": "Paramara Polymath King of Malwa (c. 1010–1055 CE)",
                "note": "Authored encyclopedic Sanskrit treatises on architecture (Samarangana Sutradhara), poetry, and philosophy; built Bhojpur temple.",
                "isWomen": False
            }
        ],
        "women": [
            {
                "name": "Rani Durgavati & Queen Sugandha",
                "role": "Early Medieval Rulers & Regents",
                "note": "Exemplified female political authority in Kashmir and regional polities; Queen Sugandha ruled Kashmir in early 10th century.",
                "isWomen": True
            }
        ],
        "themes": ["polity", "economy", "culture", "society"],
        "upsc": {
            "prelims": [
                "The Tripartite Struggle for Kannauj involved the Palas of Bengal, Gurjara-Pratiharas of Malwa/Rajasthan, and Rashtrakutas of the Deccan.",
                "The concept of Indian Feudalism was formulated by Prof. R.S. Sharma in 'Indian Feudalism' (1965), emphasizing land grants and peasant subjugation.",
                "Mahmud of Ghazni invaded India 17 times between 1000 and 1027 CE; his court scholar Al-Biruni authored Kitab-ul-Hind.",
                "First Battle of Tarain (1191) was won by Prithviraj Chauhan; Second Battle of Tarain (1192) was won by Muhammad Ghori.",
                "The Chandelas constructed the Khajuraho temples in Bundelkhand; Raja Bhoja Paramara authored 'Samarangana Sutradhara'."
            ],
            "mains": [
                "Critically evaluate the 'Indian Feudalism' debate in early medieval India. What were its socio-economic and political manifestations?",
                "Analyze the structural factors behind the military failure of Rajput kingdoms against Turkish invaders in the 11th and 12th centuries."
            ]
        },
        "quickFacts": {
            "Tripartite Struggle Triad": "Palas, Pratiharas, Rashtrakutas",
            "Target of Tripartite War": "Kannauj (Imperial capital of Madhyadesha)",
            "First Arab Victory in India": "Muhammad bin Qasim in Sindh (712 CE)",
            "Somnath Expedition Year": "1026 CE (Mahmud of Ghazni)",
            "Decisive Turkish Victory": "Second Battle of Tarain (1192 CE)"
        },
        "aspects": {
            "The Indian Feudalism Model (R.S. Sharma)": [
                "Fiscal & Judicial Alienation: Royal land charters surrendered state taxation rights (Bhaga, Bhoga, Kara) and police powers to beneficiaries.",
                "Rise of the Samanta Hierarchy: Vassals holding military fiefs graded from Mahasamanta, Samanta, to Ranaka and Thakura.",
                "Subjection of Peasantry: Peasants bound to the soil (Adhah-praja); imposition of forced unpaid labour (Vishti); restriction on geographic mobility.",
                "Urban Contraction Debate: Decline of long-distance Roman trade, decay of urban centres, and localized self-sufficient village barter economies."
            ],
            "Military Systems & Causes of Rajput Defeat": [
                "Cavalry & Mounted Archery: Turkish forces utilized central Asian swift horses, iron stirrups, and mounted composite-bow archery.",
                "Rajput Military Limitations: Heavy reliance on slow war-elephants, rigid codes of chivalry (Dharmayuddha) avoiding night warfare, and absence of unified central command.",
                "Political Fragmentation: Chronic inter-clan warfare between Chauhans, Gahadavalas, and Chandellas prevented a concerted national defence."
            ],
            "Pala & Rashtrakuta Cultural Achievements": [
                "Pala Buddhist Renaissance: Foundation of Vikramashila, Odantapuri, and patronage of Nalanda; flourishing of bronze casting school of Dhiman and Vitapala.",
                "Rashtrakuta Monolithic Wonder: Krishna I carved the monolithic rock-cut Kailasa Temple (Cave 16) at Ellora from top to bottom.",
                "Literature & Epics: Amoghavarsha authored Kavirajamarga (earliest Kannada poetic work); court poet Pampa composed Adipurana."
            ],
            "Architecture & Regional Styles": [
                "Khajuraho (Chandellas): Nagara style with Panchayatana layout, erotic Mithuna sculptures, and lofty Shikharas (Kandariya Mahadeva).",
                "Odisha Temples: Rekha Deul sanctum, Jagamohana assembly hall, wheel motifs (Mukteshvara, Lingaraja, Konark).",
                "Solanki Architecture (Gujarat): Sun Temple at Modhera with ornamental stepwell (Surya Kund) and intricate marble carving at Dilwara (Mount Abu)."
            ]
        }
    },
    {
        "id": "bhakti-sufi-movements",
        "order": 19,
        "title": "Bhakti and Sufi Confluence in Medieval India",
        "dateRange": "8th – 17th Century CE",
        "category": "medieval",
        "tagline": "Alvars & Nayanars – Saguna vs Nirguna – Kabir, Nanak, Mirabai – Chishti & Suhrawardi Silsilas",
        "heroImg": "delhi_sultanate.png",
        "sourceImages": ["delhi_sultanate.png", "mughal_empire.png"],
        "overview": "The medieval Bhakti and Sufi movements constituted an unprecedented socio-religious revolution across the Indian subcontinent. Rejecting rigid ritualism, caste hierarchy, Brahminical monopoly over scriptures, and dogmatic orthodoxy, saints emphasized personal devotion, egalitarian brotherhood, and mystical love of God expressed in regional vernacular languages. The Bhakti movement originated in South India (6th–9th centuries CE) with Tamil Alvar (Vaishnavite) and Nayanar (Shaivite) poet-saints, later expanding northward through Ramanuja, Ramananda, and dividing into two powerful streams: Nirguna (devotion to a formless, attribute-less Divine, led by Kabir, Guru Nanak, and Ravidas) and Saguna (devotion to anthropomorphic manifestations like Krishna and Rama, led by Chaitanya Mahaprabhu, Mirabai, Surdas, and Tulsidas). Parallelly, Sufi mysticism flourished via four major Silsilas (orders): the popular Chishti order (Khwaja Moinuddin Chishti, Nizamuddin Auliya) practicing Sama (spiritual music) and communal kitchens (Langar), alongside Suhrawardi, Qadiri, and Naqshbandi orders, fostering a resilient syncretic Ganga-Jamuni Tehzeeb.",
        "phases": [
            {
                "name": "South Indian Origins: Alvars & Nayanars",
                "range": "6th – 10th Century CE",
                "points": [
                    "12 Alvars (devotees of Vishnu) composing Nalayira Divya Prabandham; included female mystic Andal (Kodai).",
                    "63 Nayanars (devotees of Shiva) composing Tevaram and Tiruvachakam; included Appar, Sambandar, Sundarar, and female ascetic Karaikkal Ammaiyar.",
                    "Philosophical foundations laid by Adi Shankara (Advaita Vedanta - absolute monism) and Ramanuja (Vishishtadvaita - qualified non-dualism)."
                ]
            },
            {
                "name": "North Indian Efflorescence: Nirguna vs Saguna",
                "range": "14th – 17th Century CE",
                "points": [
                    "Swami Ramananda brought Bhakti to North India, admitting disciples from all castes (Kabir the weaver, Ravidas the leatherworker, Sena the barber, Sadhana the butcher).",
                    "Nirguna Stream: Sant Kabir's couplets (Bijak, Sakhis, Sabads) mocking both Hindu idol worship and Islamic ritualism; Guru Nanak (1469–1539) founding Sikhism on Ek Onkar, Langar, and Sangat.",
                    "Saguna Stream: Chaitanya Mahaprabhu in Bengal popularizing Sankirtana (ecstatic group singing); Mirabai's Krishna devotion in Rajasthan; Tulsidas composing Ramcharitmanas in Awadhi."
                ]
            },
            {
                "name": "Sufism & The Four Major Silsilas",
                "range": "12th – 18th Century CE",
                "points": [
                    "Chishti Order: Khwaja Moinuddin Chishti at Ajmer (1192 CE); Baba Farid (verses in Guru Granth Sahib); Hazrat Nizamuddin Auliya (Mehboob-e-Ilahi) and Amir Khusrau in Delhi.",
                    "Suhrawardi Order: Bahauddin Zakariya at Multan, accepting state patronage and court offices.",
                    "Qadiri & Naqshbandi Orders: Sheikh Ahmad Sirhindi (Naqshbandi Mujaddid) opposing Akbar's Sulh-i-kul and promoting orthodox revival."
                ]
            }
        ],
        "events": [
            {
                "year": "1192 CE",
                "title": "Establishment of the Chishti Silsila at Ajmer",
                "desc": "Khwaja Moinuddin Chishti arrives in India and establishes the Chishti Sufi order at Ajmer, preaching universal love, service to humanity, and detachment from worldly politics.",
                "theme": "culture"
            },
            {
                "year": "1499 CE",
                "title": "Guru Nanak's Divine Epiphany & Mission",
                "desc": "Guru Nanak proclaims 'Na koi hindu, na koi musalman' (There is no Hindu, there is no Muslim), establishing the foundational tenets of Sikhism based on honest labour, sharing, and meditation on God's name.",
                "theme": "society"
            },
            {
                "year": "1574 CE",
                "title": "Goswami Tulsidas Commences the Ramcharitmanas",
                "desc": "Tulsidas begins composing the epic Ramcharitmanas in vernacular Awadhi at Ayodhya, democratizing the Valmiki Ramayana for ordinary masses across North India.",
                "theme": "culture"
            }
        ],
        "people": [
            {
                "name": "Sant Kabir",
                "role": "Foremost Nirguna Bhakti Poet-Philosopher (1440–1518 CE)",
                "note": "Weaver of Varanasi; authored Bijak; attacked religious hypocrisy and untouchability; emphasized devotion to formless Rama.",
                "isWomen": False
            },
            {
                "name": "Guru Nanak Dev",
                "role": "Founder of Sikhism (1469–1539 CE)",
                "note": "Preached monotheism (Ek Onkar); instituted Langar (community kitchen) to eradicate caste distinctions; composed Japji Sahib.",
                "isWomen": False
            },
            {
                "name": "Hazrat Nizamuddin Auliya",
                "role": "Revered Chishti Sufi Saint (1238–1325 CE)",
                "note": "Known as Mehboob-e-Ilahi (Beloved of God); maintained ascetic detachment from Delhi Sultans; master of Amir Khusrau.",
                "isWomen": False
            }
        ],
        "women": [
            {
                "name": "Mirabai",
                "role": "Rajput Princess & Saguna Krishna Bhakti Saint (1498–1546 CE)",
                "note": "Defied royal patriarchal diktats of Mewar; composed passionate Krishna bhajans in Braj Bhasha and Rajasthani; embraced Raidas as guru.",
                "isWomen": True
            },
            {
                "name": "Andal (Kodai)",
                "role": "Only Female Alvar Saint of Tamil Nadu (8th Century CE)",
                "note": "Authored Tiruppavai and Nachiyar Tirumozhi expressing bride-mysticism (Nayika-Bhava) towards Lord Ranganatha.",
                "isWomen": True
            },
            {
                "name": "Lalleshwari (Lal Ded)",
                "role": "Kashmiri Shaivite Mystic Poetess (1320–1392 CE)",
                "note": "Composed mystical Vatsun (Vakhs) verses; foundational figure of Kashmiri literature and the Rishi Sufi tradition.",
                "isWomen": True
            }
        ],
        "themes": ["culture", "society", "polity"],
        "upsc": {
            "prelims": [
                "Alvars were 12 Vaishnavite saints (Andal was the only woman Alvar); Nayanars were 63 Shaivite saints (Karaikkal Ammaiyar was female).",
                "Kabir was a disciple of Swami Ramananda; his compilation is the Bijak, containing Sakhis, Sabads, and Ramainis.",
                "The Chishti order practiced Sama (musical sessions) and ran Langar (community kitchen) open to all castes and creeds.",
                "Nizamuddin Auliya famously said 'Hanooz Dilli Door Ast' (Delhi is yet far away) regarding Sultan Ghiyasuddin Tughlaq.",
                "Pushtimarga was founded by Vallabhacharya, focusing on the grace of Lord Krishna; Chaitanya Mahaprabhu introduced Sankirtana."
            ],
            "mains": [
                "Evaluate the role of the Bhakti and Sufi movements in fostering social integration, linguistic democracy, and religious syncretism in medieval India.",
                "Differentiate between Nirguna and Saguna streams of the Bhakti movement. How did they challenge contemporary socio-religious orthodoxies?"
            ]
        },
        "quickFacts": {
            "Only Woman Alvar": "Andal (composed Tiruppavai)",
            "Chishti Order Founder in India": "Khwaja Moinuddin Chishti (Ajmer, 1192 CE)",
            "Nirguna Pioneers": "Kabir, Guru Nanak, Ravidas, Dadu Dayal",
            "Saguna Pioneers": "Chaitanya Mahaprabhu, Mirabai, Surdas, Tulsidas",
            "Concept of Langar": "Institutionalized by Guru Nanak to break caste segregation"
        },
        "aspects": {
            "Philosophical Foundations (Vedantic Schools)": [
                "Advaita Vedanta (Adi Shankara, 8th c.): Absolute monism (Nirguna Brahman); empirical world is Maya (illusion); salvation via Jnana (knowledge).",
                "Vishishtadvaita (Ramanuja, 11th c.): Qualified non-dualism; Brahman has personal attributes (Saguna); salvation through Prapatti (complete self-surrender to Vishnu).",
                "Dvaita (Madhvacharya, 13th c.): Dualism; eternal distinction between God (Brahman) and individual souls (Jivas).",
                "Dvaitadvaita (Nimbarka) & Shuddhadvaita (Vallabhacharya): Dualistic non-dualism and pure non-dualism (Pushtimarga)."
            ],
            "The Four Sufi Silsilas in India": [
                "Chishti Silsila: Most influential and syncretic; practiced Wahdat-al-Wujud (unity of existence); avoided royal courts and state patronage; utilized local dialects (Hindawi).",
                "Suhrawardi Silsila: Founded in India by Bahauddin Zakariya; accepted royal land grants and state offices; centered in Multan and Sindh.",
                "Qadiri Silsila: Introduced by Sheikh Niamatullah; Dara Shikoh (author of Majma-ul-Bahrain) was a devout adherent.",
                "Naqshbandi Silsila: Founded by Khwaja Baqi Billah; prominent under Sheikh Ahmad Sirhindi; advocated strict Sharia orthodoxy against Akbar's eclectic policies."
            ],
            "Vernacular Literary Democracy": [
                "Democratization of Knowledge: Saints abandoned elite Sanskrit in favour of people's dialects (Braj Bhasha, Awadhi, Bhojpuri, Bengali, Punjabi, Marathi, Tamil, Telugu).",
                "Key Literary Works: Kabir's Bijak; Tulsidas's Ramcharitmanas and Kavitavali; Surdas's Sursagar; Mirabai's Padavali; Vidyapati's Maithili lyrics; Tukaram's Abhangas; Guru Granth Sahib compiled by Guru Arjan Dev (1604 CE)."
            ],
            "Social Reforms & Subversion of Hierarchy": [
                "Attack on Untouchability: Welcomed low castes, leatherworkers (Ravidas), weavers (Kabir), and women (Mirabai, Andal, Bahinabai) into the spiritual sanctum.",
                "Communal Synthesis: Shared veneration at Sufi Dargahs (Ajmer Sharif, Nizamuddin Dargah) by Hindus and Muslims; conceptual synthesis in Amir Khusrau's poetry and Dara Shikoh's Persian Upanishad translation (Sirr-i-Akbar)."
            ]
        }
    },
    {
        "id": "eighteenth-century-transition-and-regional-states",
        "order": 31,
        "title": "The 18th-Century Transition & Regional States",
        "dateRange": "1707 – 1800 CE",
        "category": "modern",
        "tagline": "Successor States (Bengal, Awadh, Hyderabad) – Tipu Sultan's Mysore – Anglo-French Carnatic Wars",
        "heroImg": "british_expansion.png",
        "sourceImages": ["british_expansion.png", "mughal_empire.png"],
        "overview": "The 18th century represents a critical transition in Indian history: the decentralization and fragmentation of the Mughal imperial umbrella gave rise to a constellation of assertive regional states, followed by intense European commercial and military intervention. Historiographically, the 'Dark Age' thesis of complete economic decay has been revised by historians (Muzaffar Alam, Sanjay Subrahmanyam, Seema Alavi) demonstrating vibrant regional economic re-alignments, urban growth in new capitals (Lucknow, Murshidabad, Hyderabad, Pune), and commercialization. Regional polities emerged in three categories: (1) Successor States (Bengal under Murshid Quli Khan, Awadh under Saadat Khan, Hyderabad under Nizam-ul-Mulk Asaf Jah); (2) Independent/Modernizing States (Mysore under Haidar Ali and Tipu Sultan); and (3) Rebel/Warrior States (the Maratha Confederacy, Sikh Misls, and Jat kingdom of Bharatpur under Suraj Mal). Concurrently, European mercantilist competition erupted between the English and French East India Companies in the three Carnatic Wars (1746–1763), culminating in British commercial and military supremacy under Robert Clive and Eyre Coote.",
        "phases": [
            {
                "name": "Mughal Decentralization & The Successor States",
                "range": "1707 – 1740 CE",
                "points": [
                    "Bengal: Murshid Quli Khan (1717) transfers capital to Murshidabad; reorganizes finances and introduces Malzamini revenue system.",
                    "Awadh: Saadat Khan Burhan-ul-Mulk (1722) creates an autonomous province; succeeded by Safdarjung and Asaf-ud-Daula.",
                    "Hyderabad: Mir Qamar-ud-din Khan (Nizam-ul-Mulk Asaf Jah, 1724) defeats Mubariz Khan at Shakr-Kheda, founding the Asaf Jahi dynasty."
                ]
            },
            {
                "name": "Anglo-French Rivalry & The Carnatic Wars",
                "range": "1746 – 1763 CE",
                "points": [
                    "First Carnatic War (1746–48): Extension of War of Austrian Succession; Battle of St. Thome; ended with Treaty of Aix-la-Chapelle.",
                    "Second Carnatic War (1749–54): Succession disputes in Hyderabad and Carnatic; Dupleix's proxy politics; ended with Treaty of Pondicherry.",
                    "Third Carnatic War (1758–63): Seven Years' War extension; decisive Battle of Wandiwash (1760); Treaty of Paris (1763) ending French political ambitions in India."
                ]
            },
            {
                "name": "Mysore's Resistance: Haidar Ali & Tipu Sultan",
                "range": "1761 – 1799 CE",
                "points": [
                    "Haidar Ali overthrows Wodeyars; modernizes army with French help at Dindigul arsenal; defeats British in First Anglo-Mysore War (1769).",
                    "Tipu Sultan ('Tiger of Mysore'): Introduced modern calendar, new coinage, state commercial corporation, silkworm farming (sericulture), and military rockets.",
                    "Jacobin Club of Seringapatam: Tipu planted the 'Tree of Liberty'; allied with revolutionary France and Ottoman Porte; died defending Seringapatam in the Fourth Anglo-Mysore War (1799)."
                ]
            }
        ],
        "events": [
            {
                "year": "1724 CE",
                "title": "Establishment of the Autonomous Asaf Jahi State of Hyderabad",
                "desc": "Nizam-ul-Mulk Asaf Jah defeats the Mughal governor Mubariz Khan at the Battle of Shakr-Kheda, establishing autonomous rule over the Deccan.",
                "theme": "polity"
            },
            {
                "year": "1760 CE",
                "title": "Decisive Battle of Wandiwash",
                "desc": "British General Sir Eyre Coote crushes the French forces under Count de Lally at Wandiwash (Tamil Nadu), completely ending French political and military power in India.",
                "theme": "polity"
            },
            {
                "year": "1799 CE",
                "title": "Fall of Seringapatam & Martyrdom of Tipu Sultan",
                "desc": "British forces under General Harris and Arthur Wellesley storm Seringapatam; Tipu Sultan falls sword in hand, terminating Mysore's fierce sovereignty.",
                "theme": "polity"
            }
        ],
        "people": [
            {
                "name": "Tipu Sultan",
                "role": "Ruler of Mysore (1750–1799 CE)",
                "note": "Known as Tiger of Mysore; deployed Mysorean iron-cased rockets; pioneered modern navy and state trading factories; member of Jacobin Club.",
                "isWomen": False
            },
            {
                "name": "Joseph François Dupleix",
                "role": "French Governor-General of Pondicherry (1697–1763)",
                "note": "Pioneered the strategy of subsidiary intervention in Indian dynastic rivalries, which the British later perfected.",
                "isWomen": False
            },
            {
                "name": "Murshid Quli Khan",
                "role": "First Nawab of Bengal (1660–1727)",
                "note": "Shifted capital from Dhaka to Murshidabad; streamlined revenue administration; consolidated Bengal as the richest province.",
                "isWomen": False
            }
        ],
        "women": [
            {
                "name": "Rani Velu Nachiyar",
                "role": "Queen of Sivaganga, Tamil Nadu (1730–1796 CE)",
                "note": "First Indian queen to wage war against the British East India Company; allied with Haidar Ali and defeated the British in 1780 using human bomb strategy of commander Kuyili.",
                "isWomen": True
            }
        ],
        "themes": ["polity", "economy", "culture"],
        "upsc": {
            "prelims": [
                "Battle of Wandiwash (1760) was won by the British under Sir Eyre Coote against French forces under Count de Lally.",
                "Tipu Sultan planted the 'Tree of Liberty' at Seringapatam and became a member of the Jacobin Club of France.",
                "First Carnatic War ended with the Treaty of Aix-la-Chapelle (1748); Third Carnatic War ended with the Treaty of Paris (1763).",
                "Nizam-ul-Mulk Asaf Jah founded the autonomous state of Hyderabad in 1724 after defeating Mubariz Khan at Shakr-Kheda.",
                "Mysorean rockets used by Haidar Ali and Tipu Sultan used iron cylinders to contain the propellant, inspiring William Congreve's British rockets."
            ],
            "mains": [
                "Was the 18th century in India a 'Dark Age' of economic ruin or a period of vibrant regional reconfiguration? Discuss in the light of recent historiographical scholarship.",
                "Analyze the factors that led to British triumph over the French East India Company during the Carnatic Wars."
            ]
        },
        "quickFacts": {
            "Decisive Anglo-French Battle": "Battle of Wandiwash (1760)",
            "Treaties of Carnatic Wars": "Aix-la-Chapelle (1st), Pondicherry (2nd), Paris (3rd)",
            "Mysore Resistance Leaders": "Haidar Ali (1761–1782) & Tipu Sultan (1782–1799)",
            "Tipu Sultan's Capital": "Seringapatam (Sri Ranga Patna)",
            "Successor State Capitals": "Murshidabad (Bengal), Lucknow (Awadh), Hyderabad (Deccan)"
        },
        "aspects": {
            "The Successor States Matrix": [
                "Bengal: Ruled by Murshid Quli Khan, Shuja-ud-din, Alivardi Khan; relied heavily on the banking house of Jagat Seth; fertile agrarian hinterland became the primary target for British exploitation.",
                "Awadh: Saadat Khan created a stable agrarian base in the Gangetic plain; Asaf-ud-Daula shifted capital to Lucknow in 1775, patronizing refined architectural and musical expressions.",
                "Hyderabad: Geostrategic heart of the Deccan; maintained balancing alliances between Marathas, Mysore, and European companies; signed the first Subsidiary Alliance with Wellesley in 1798."
            ],
            "Tipu Sultan's Modernizing State Model": [
                "Economic Innovations: Eradicated hereditary intermediaries; collected land revenue directly from ryots; established state monopoly over sandalwood, pepper, and timber.",
                "Military Technology: Created an elite rocket artillery corps (Rocket Troops); manufactured iron-cased Mysorean rockets with a range of nearly 1,000 yards.",
                "Global Diplomacy: Dispatched diplomatic embassies to France (Louis XVI), Ottoman Caliphate (Istanbul), Afghanistan (Zaman Shah), and Mauritius seeking anti-British coalitions."
            ],
            "Reasons for British Victory over the French": [
                "Commercial & Financial Superiority: English East India Company was a private joint-stock enterprise backed by the Bank of England; French Company was a state-controlled entity starved of funds.",
                "Naval Supremacy: Royal Navy controlled sea routes, allowing rapid troop reinforcements from Europe, Bombay, and Madras, while cutting off French supplies.",
                "Conquest of Bengal Base: The conquest of Bengal (1757) gave the British limitless financial and agrarian revenues to finance wars across South India, whereas the French had only impoverished Pondicherry."
            ]
        }
    },
    {
        "id": "colonial-economy-and-drain-of-wealth",
        "order": 35,
        "title": "Economic Impact of British Rule & Drain of Wealth",
        "dateRange": "1757 – 1947 CE",
        "category": "modern",
        "tagline": "Mercantile to Financial Capitalism – Zamindari, Ryotwari, Mahalwari – De-industrialization & Drain of Wealth",
        "heroImg": "british_colonial_rule.png",
        "sourceImages": ["british_colonial_rule.png", "british_administration.png"],
        "overview": "British colonial rule fundamentally transformed the economic landscape of India, converting a self-sufficient world-leading manufacturing economy (accounting for ~24.5% of world manufacturing output in 1750) into an impoverished, raw-material exporter and captive market for British factory goods. Marxist economic historian R. Palme Dutt delineated three successive stages of colonial exploitation: (1) The Mercantile Phase (1757–1813), characterized by direct plunder, revenue extraction, and monopolistic buying; (2) The Industrial Capitalism / Free Trade Phase (1813–1858), marked by one-way free trade, destruction of Indian cotton handlooms (De-industrialization), and commercialization of agriculture; and (3) Financial Imperialism (post-1858), characterized by British capital investments in railways, plantations, and irrigation guaranteeing guaranteed return rates at Indian taxpayer risk. Dadabhai Naoroji formulated the pioneering 'Drain of Wealth' theory in 'Poverty and Un-British Rule in India', exposing how a massive portion of India's annual revenue was siphoned off to Britain without any economic return through 'Home Charges', pensions, and imperial remittances.",
        "phases": [
            {
                "name": "Three Phases of Colonial Exploitation (R.P. Dutt)",
                "range": "1757 – 1947 CE",
                "points": [
                    "Phase I (1757–1813): Merchant Capital — East India Company used Bengal territorial revenues to purchase Indian goods for export ('Investment'), ending bullion inflow from England.",
                    "Phase II (1813–1858): Industrial Capital — Charter Act 1813 ended Company monopoly; influx of cheap Manchester textiles ruined Indian weavers ('bones of cotton weavers bleaching the plains of India' - William Bentinck).",
                    "Phase III (1858–1947): Finance Capital — Construction of railways under 'guaranteed 5% interest system'; British capital dominating jute mills, coal mines, tea/coffee plantations, and managing agencies."
                ]
            },
            {
                "name": "The Three Land Revenue Settlements",
                "range": "1793 – 1947 CE",
                "points": [
                    "Permanent Settlement (1793): Lord Cornwallis in Bengal, Bihar, Odisha (19% of British India); Zamindars declared proprietary owners; state share fixed at 10/11th, Zamindar share 1/11th; Sunset Law mechanics.",
                    "Ryotwari System (1820): Thomas Munro and Alexander Read in Madras and Bombay (51% of British India); direct contract with individual peasants (Ryots); arbitrary high revenue (50-60%) leading to catastrophic debt bondage.",
                    "Mahalwari System (1822/1833): Holt Mackenzie and Robert Merttins Bird in North-Western Provinces, Punjab, Central India (30% of British India); settlement with the village community/estate (Mahal) jointly."
                ]
            },
            {
                "name": "Drain of Wealth & The Nationalist Critique",
                "range": "1867 – 1947 CE",
                "points": [
                    "Dadabhai Naoroji read his paper 'England's Debt to India' (1867) in London; authored 'Poverty and Un-British Rule in India' (1901).",
                    "R.C. Dutt authored 'The Economic History of India' (2 vols); Dinshaw Wacha, G.V. Joshi, and G.K. Gokhale popularized the critique.",
                    "Mechanisms of Drain: Home Charges (Secretary of State office expenses, pensions of retired officials, interest on Indian debt, war expenses abroad, guaranteed railway profits)."
                ]
            }
        ],
        "events": [
            {
                "year": "1793 CE",
                "title": "Enactment of the Permanent Settlement in Bengal",
                "desc": "Lord Cornwallis introduces the Permanent Settlement, converting feudal revenue collectors into proprietary landlords and permanently fixing the state's revenue demand with a strict Sunset Law.",
                "theme": "economy"
            },
            {
                "year": "1867 CE",
                "title": "Dadabhai Naoroji Formulates the Drain of Wealth Theory",
                "desc": "Dadabhai Naoroji presents his economic drain paper to the East India Association in London, proving that India's persistent poverty was an outcome of unilateral wealth extraction by the British.",
                "theme": "economy"
            },
            {
                "year": "1901 CE",
                "title": "Publication of 'Poverty and Un-British Rule in India'",
                "desc": "Dadabhai Naoroji publishes his magnum opus, documenting statistical evidence of the moral and material drain that crippled the Indian subcontinental economy.",
                "theme": "economy"
            }
        ],
        "people": [
            {
                "name": "Dadabhai Naoroji",
                "role": "Grand Old Man of India (1825–1917)",
                "note": "Formulated the Drain of Wealth theory; first Indian MP in the British House of Commons (1892); thrice INC President; demanded 'Swaraj' in 1906.",
                "isWomen": False
            },
            {
                "name": "Romesh Chunder Dutt (R.C. Dutt)",
                "role": "Civil Servant & Economic Historian (1848–1909)",
                "note": "Authored the definitive 2-volume 'Economic History of India'; analyzed over-assessment in land revenue and destruction of rural crafts.",
                "isWomen": False
            },
            {
                "name": "Lord Cornwallis",
                "role": "Governor-General of India (1738–1805)",
                "note": "Introduced the Permanent Settlement in Bengal (1793) and the Cornwallis Code separating revenue and judicial branches.",
                "isWomen": False
            }
        ],
        "women": [
            {
                "name": "Women Textile Workers & Artisans",
                "role": "Victims and Resisters of De-industrialization",
                "note": "Millions of women spinning yarn (Charkha) in Bengal and Andhra lost their traditional livelihoods due to machine-made cloth imports from Lancashire.",
                "isWomen": True
            }
        ],
        "themes": ["economy", "society", "polity"],
        "upsc": {
            "prelims": [
                "The Permanent Settlement covered 19% of British India (Bengal, Bihar, Odisha, Northern Circars, Varanasi).",
                "The Ryotwari System covered 51% of British India (Madras, Bombay, parts of Assam and Coorg).",
                "The Mahalwari System covered 30% of British India (North-Western Provinces, Punjab, Central Provinces).",
                "Home Charges included: interest on public debt, guaranteed railway return, pensions and leave allowances of military and civil personnel, and costs of the India Office in London.",
                "Dadabhai Naoroji first presented his Drain of Wealth theory in 1867 in a paper titled 'England's Debt to India'."
            ],
            "mains": [
                "Examine how the commercialization of agriculture under British colonial rule altered the agrarian socio-economic structure of rural India.",
                "Critically evaluate the 'Drain of Wealth' theory propounded by early nationalist leaders. How did it undermine the moral legitimacy of British rule in India?"
            ]
        },
        "quickFacts": {
            "Permanent Settlement Architect": "Lord Cornwallis & Sir John Shore (1793)",
            "Ryotwari Architects": "Thomas Munro & Alexander Read (1820)",
            "Mahalwari Architects": "Holt Mackenzie (1822) & Merttins Bird (1833)",
            "Drain Theory Author": "Dadabhai Naoroji (1867 / 1901)",
            "Author of 'Economic History of India'": "R.C. Dutt (1901–1903)"
        },
        "aspects": {
            "The Three Land Systems Comparative Breakdown": [
                "Permanent Settlement (Zamindari): State revenue fixed perpetually; Zamindars given ownership; failure to pay by sunset on stipulated date led to land auction (Sunset Law); created parasitic absentee landlords and sub-infeudation (Pattani taluks).",
                "Ryotwari: State dealt directly with individual cultivator; revenue assessed on potential soil productivity (not actual crop output); periodic revisions every 20-30 years upward; led to rise of village moneylenders (Sahukars/Mahajans).",
                "Mahalwari: Revenue assessed collectively on the village unit (Mahal); village headman (Lambardar) collected and submitted revenue; joint and several liability of coparcenary brotherhoods."
            ],
            "De-industrialization & Commercialization of Agriculture": [
                "De-industrialization: One-way duty-free entry for British manufactured goods into India while prohibitive tariffs (up to 70-80%) blocked Indian textiles in Britain; forced weavers back into over-crowded agriculture, increasing landlessness.",
                "Commercialization of Agriculture: Forced transition from subsistence foodgrains (wheat, rice, millets) to commercial cash crops (indigo, opium, raw cotton, jute, sugarcane, tea) dictated by British industrial needs; rendered peasantry extraordinarily vulnerable to famines.",
                "Devastating Famines: Great Bengal Famine of 1770 (1/3rd population perished); series of late 19th-century famines (1876–78, 1896–97, 1899–1900) and Bengal Famine of 1943 (3 million dead)."
            ],
            "Drain of Wealth Component Breakdown": [
                "Home Charges: Annual remittances of £16 to £20 million sent to the India Office in London for imperial administration expenses.",
                "Guaranteed Railways: British railway companies guaranteed a 5% minimum profit paid from Indian taxes even if trains ran empty ('private enterprise at public risk').",
                "Unrequited Exports: India consistently exported more goods than it imported in value, yet the trade surplus was confiscated in London as tribute rather than returned in bullion."
            ]
        }
    },
    {
        "id": "revolutionary-nationalism-and-ina",
        "order": 42,
        "title": "Revolutionary Nationalism, Subhas Chandra Bose & The INA",
        "dateRange": "1897 – 1946 CE",
        "category": "modern",
        "tagline": "Anushilan Samiti – Ghadar Party – HRA & HSRA – Netaji's Azad Hind Fauj – RIN Mutiny 1946",
        "heroImg": "freedom_struggle.png",
        "sourceImages": ["freedom_struggle.png", "independence_india.png"],
        "overview": "Revolutionary nationalism provided a fierce, uncompromising parallel current to the mainstream constitutional and non-violent Gandhian streams of the Indian freedom struggle. Driven by youth disillusioned with moderate prayers and sudden withdrawals of mass satyagrahas, revolutionaries embraced armed resistance, political actions, and supreme martyrdom. Phase I (1905–1918) witnessed secret societies like Anushilan Samiti and Jugantar in Bengal (Barindra Ghosh, Prafulla Chaki, Khudiram Bose), the Chapekar brothers in Maharashtra, the Delhi Conspiracy case (Rash Behari Bose), and international networks like the Ghadar Movement in North America (Lala Hardayal, Kartar Singh Sarabha) and Madam Bhikaji Cama in Europe. Phase II (1922–1934) witnessed an ideological leap toward socialism and secularism under the Hindustan Republican Association (HRA, 1924: Bismil, Ashfaqullah, Sachindra Nath Sanyal) and its socialist reconstitution as HSRA (1928: Bhagat Singh, Chandrashekhar Azad, Sukhdev, Rajguru) and the Chittagong Armoury Raid (1930) led by Surya Sen (Masterda). The culmination arrived during World War II with Netaji Subhas Chandra Bose transforming the Indian National Army (Azad Hind Fauj) into an armed liberation force, whose post-war Red Fort trials and the Royal Indian Navy (RIN) Mutiny of 1946 dismantled the military pillars of British colonial dominion.",
        "phases": [
            {
                "name": "Phase I: Early Militancy & Ghadar Movement",
                "range": "1897 – 1918 CE",
                "points": [
                    "Maharashtra: Chapekar brothers assassinate Plague Commissioner Rand (1897); V.D. Savarkar founds Abhinav Bharat (1904).",
                    "Bengal: Anushilan Samiti (Promotha Mitter, Barindra Ghosh, Bhupendranath Dutta); Muzaffarpur bomb incident (1908: Khudiram Bose and Prafulla Chaki); Alipore Bomb Case (Sri Aurobindo).",
                    "International Networks: Ghadar Party founded in San Francisco (1913) by Lala Hardayal; Komagata Maru voyage (1914); Madam Cama unfurls first Indian tricolour flag at Stuttgart (1907)."
                ]
            },
            {
                "name": "Phase II: Socialism, HSRA & Chittagong",
                "range": "1924 – 1934 CE",
                "points": [
                    "HRA & Kakori Train Action (1925): Ram Prasad Bismil, Ashfaqullah Khan, Roshan Singh, Rajendra Lahiri martyred.",
                    "HSRA (1928): Founded at Feroz Shah Kotla, Delhi; Saunders' assassination (1928) avenging Lala Lajpat Rai; Central Legislative Assembly bombing (8 April 1929) by Bhagat Singh and Batukeshwar Dutt ('To make the deaf hear').",
                    "Martyrdom of Jatin Das (63-day hunger strike for political prisoner rights); martyrdom of Bhagat Singh, Rajguru, Sukhdev (23 March 1931); Chandrashekhar Azad at Alfred Park (1931).",
                    "Chittagong Armoury Raid (18 April 1930): Masterda Surya Sen leads daring raid, declares provisional revolutionary government; prominent women revolutionaries (Pritilata Waddedar, Kalpana Datta)."
                ]
            },
            {
                "name": "Subhas Chandra Bose, The INA & The RIN Mutiny",
                "range": "1941 – 1946 CE",
                "points": [
                    "Netaji's Great Escape (January 1941) from Calcutta house arrest via Peshawar and Moscow to Berlin (Free India Centre).",
                    "Azad Hind Fauj (INA): Founded originally by Mohan Singh with Japanese support; reorganized by Rash Behari Bose and handed to Netaji in Singapore (1943).",
                    "Provisional Government of Free India (Arzi Hukumat-e-Azad Hind) established in Singapore; slogans 'Jai Hind' and 'Dilli Chalo'; Rani of Jhansi Regiment under Captain Lakshmi Sahgal.",
                    "Red Fort INA Trials (1945–46): Trial of Prem Sahgal, Gurbaksh Singh Dhillon, and Shah Nawaz Khan sparks pan-Indian anti-imperialist solidarity.",
                    "Royal Indian Navy (RIN) Mutiny (18 February 1946): Ratings of HMIS Talwar strike at Bombay, spreading to 78 ships; soldiers refuse to fire on citizens, breaking the colonial armed apparatus."
                ]
            }
        ],
        "events": [
            {
                "year": "1925 CE",
                "title": "Kakori Train Action",
                "desc": "HRA revolutionaries led by Ram Prasad Bismil, Ashfaqullah Khan, and Chandrashekhar Azad stop and seize British government treasury from the 8-Down train near Kakori, Lucknow.",
                "theme": "polity"
            },
            {
                "year": "1929 CE",
                "title": "Central Legislative Assembly Bombing",
                "desc": "Bhagat Singh and Batukeshwar Dutt throw harmless smoke bombs and leaflets proclaiming 'Inquilab Zindabad' into the Central Assembly in Delhi to protest the Public Safety and Trade Disputes Bills.",
                "theme": "polity"
            },
            {
                "year": "1943 CE",
                "title": "Netaji Proclaims Arzi Hukumat-e-Azad Hind",
                "desc": "Netaji Subhas Chandra Bose proclaims the Provisional Government of Free India in Singapore, assuming Supreme Command of the Indian National Army (Azad Hind Fauj).",
                "theme": "polity"
            },
            {
                "year": "1946 CE",
                "title": "Royal Indian Navy (RIN) Mutiny",
                "desc": "Over 20,000 naval ratings mutiny on HMIS Talwar and across 78 ships in Bombay and Karachi, hoisting Congress, Muslim League, and Communist flags, shattering British military reliance.",
                "theme": "polity"
            }
        ],
        "people": [
            {
                "name": "Subhas Chandra Bose (Netaji)",
                "role": "Supreme Commander of INA & National Leader (1897–1945)",
                "note": "Twice INC President (Haripura 1938, Tripuri 1939); founded Forward Bloc; formed Azad Hind Fauj and Arzi Hukumat; slogan 'Give me blood and I will give you freedom'.",
                "isWomen": False
            },
            {
                "name": "Bhagat Singh",
                "role": "Socialist Revolutionary Thinker & Martyr (1907–1931)",
                "note": "Leading ideologue of HSRA; authored 'Why I am an Atheist'; transformed revolutionary struggle from individual assassination to mass socialist revolution.",
                "isWomen": False
            },
            {
                "name": "Chandrashekhar Azad",
                "role": "Commander-in-Chief of HSRA (1906–1931)",
                "note": "Vowed never to be captured alive by British police; masterminded Kakori action and HSRA underground operations; died in Alfred Park shootout (1931).",
                "isWomen": False
            },
            {
                "name": "Surya Sen (Masterda)",
                "role": "Leader of Chittagong Armoury Raid (1894–1934)",
                "note": "School teacher who organized the Indian Republican Army, Chittagong branch, capturing colonial armouries on 18 April 1930.",
                "isWomen": False
            }
        ],
        "women": [
            {
                "name": "Captain Lakshmi Sahgal (Swaminathan)",
                "role": "Commander of the Rani of Jhansi Regiment, INA (1914–2012)",
                "note": "Headed Asia's first all-female combat regiment in the Indian National Army; Minister of Women's Affairs in Netaji's Azad Hind government.",
                "isWomen": True
            },
            {
                "name": "Pritilata Waddedar",
                "role": "Revolutionary Martyr of Chittagong (1911–1932)",
                "note": "Led the armed assault on the Pahartali European Club ('Dogs and Indians not allowed'); consumed potassium cyanide to avoid capture.",
                "isWomen": True
            },
            {
                "name": "Bhikaji Rustom Cama (Madam Cama)",
                "role": "Pioneering Revolutionary Abroad (1861–1936)",
                "note": "Unfurled the first Indian National Flag at the International Socialist Conference in Stuttgart, Germany in 1907; co-founded Paris Indian Society.",
                "isWomen": True
            },
            {
                "name": "Kalpana Datta (Joshi)",
                "role": "Chittagong Revolutionary Leader (1913–1995)",
                "note": "Prepared gun-cotton explosives for Surya Sen's force; sentenced to transportation for life; later documented the Chittagong resistance.",
                "isWomen": True
            },
            {
                "name": "Bina Das",
                "role": "Bengal Revolutionary Student (1911–1986)",
                "note": "Fired revolver shots at Bengal Governor Stanley Jackson during the Calcutta University Convocation in 1932.",
                "isWomen": True
            }
        ],
        "themes": ["polity", "society", "culture"],
        "upsc": {
            "prelims": [
                "HRA was formed in Kanpur in October 1924 by Ram Prasad Bismil, Sachindra Nath Sanyal, and Jogesh Chandra Chatterjee.",
                "HSRA added 'Socialist' to its name at Feroz Shah Kotla, Delhi in September 1928 under the leadership of Bhagat Singh and Chandrashekhar Azad.",
                "Chittagong Armoury Raid was executed on 18 April 1930 under the banner of the Indian Republican Army led by Surya Sen.",
                "Rani of Jhansi Regiment of the INA was commanded by Captain Lakshmi Sahgal (Swaminathan).",
                "The Royal Indian Navy (RIN) Mutiny started on HMIS Talwar in Bombay on 18 February 1946."
            ],
            "mains": [
                "Trace the ideological evolution of revolutionary nationalism from early religious symbolism to scientific socialism and anti-imperialist internationalism.",
                "Examine the impact of the Indian National Army (INA) trials and the Royal Indian Navy (RIN) Mutiny in hastening the British decision to decolonize India."
            ]
        },
        "quickFacts": {
            "HRA Foundation": "Kanpur (1924, Manifesto: 'The Revolutionary')",
            "HSRA Foundation": "Feroz Shah Kotla, Delhi (1928)",
            "Chittagong Raid Date": "18 April 1930 (Surya Sen)",
            "INA Women's Wing": "Rani of Jhansi Regiment (Capt. Lakshmi Sahgal)",
            "RIN Mutiny Ship": "HMIS Talwar (Bombay, 18 Feb 1946)"
        },
        "aspects": {
            "Ideological Shift: From Militancy to Scientific Socialism": [
                "Philosophy of the Bomb: Authored by Bhagwati Charan Vohra with Bhagat Singh and Chandrashekhar Azad, replying to Mahatma Gandhi's 'Cult of the Bomb'; explained that revolution meant replacing the exploitative capitalist system with egalitarian socialism.",
                "Naujawan Bharat Sabha: Formed by Bhagat Singh in 1926 to mobilize youth, peasants, and workers through secular, anti-communal public education.",
                "Why I Am an Atheist: Bhagat Singh's classic essay written in Lahore Central Jail (1930), debunking religious mysticism and arguing that rational, critical thinking is the foremost prerequisite for a true revolutionary."
            ],
            "Women at the Frontline of Armed Resistance": [
                "Pritilata Waddedar: College graduate who led the raid on Pahartali European Club; fought bravely and took cyanide to avoid interrogation.",
                "Suniti Choudhury and Santi Ghosh: Teenage schoolgirls who shot dead British District Magistrate C.G.B. Stevens of Comilla in 1931.",
                "Rani of Jhansi Regiment: Full women's combat battalion trained in jungle warfare, rifle handling, and guerrilla combat during the Burma campaign under Captain Lakshmi Sahgal."
            ],
            "Netaji & The International Dimension of Freedom": [
                "Geopolitical Realpolitik: Netaji recognized that Britain's difficulty in World War II was India's opportunity; established embassies in Berlin, Tokyo, and Rome.",
                "Arzi Hukumat-e-Azad Hind: Recognized as a legitimate government by 9 sovereign states; established the Azad Hind Bank; issued national currency and postage stamps.",
                "Imphal & Kohima Campaigns (1944): INA forces along with the Japanese 15th Army crossed the Indo-Burma frontier, hoisting the Indian tricolour on Indian soil at Moirang, Manipur."
            ],
            "The 1945–46 Mass Upsurge & Decolonization Tipping Point": [
                "Red Fort INA Trials: Joint trial of Prem Sahgal (Hindu), Gurbaksh Singh Dhillon (Sikh), and Shah Nawaz Khan (Muslim) united all religious communities in protest; defended by Bhulabhai Desai, Tej Bahadur Sapru, and Jawaharlal Nehru.",
                "Royal Indian Navy Mutiny: Ratings on HMIS Talwar struck over racial abuse, bad food, and INA solidarity; 20,000 ratings took over ships in Bombay, Karachi, and Calcutta; British authorities realized native troops would no longer enforce colonial rule."
            ]
        }
    }
]

# Check existing IDs and append if missing
added = 0
for np in NEW_PERIODS:
    if np['id'] not in existing_ids:
        data['periods'].append(np)
        existing_ids.add(np['id'])
        added += 1
        print(f"Added period: {np['id']} - {np['title']}")
    else:
        print(f"Period {np['id']} already exists, updating...")
        # Update existing
        for i, p in enumerate(data['periods']):
            if p['id'] == np['id']:
                data['periods'][i] = np

# Re-sort periods logically: national first by chronological order, then up region
# National periods
national = [p for p in data['periods'] if not p.get('region')]
up = [p for p in data['periods'] if p.get('region') == 'up']

# Re-index orders for clean continuity
for idx, p in enumerate(national):
    p['order'] = idx + 1

for idx, p in enumerate(up):
    p['order'] = len(national) + idx + 1

data['periods'] = national + up

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully updated history.json! Total periods now: {len(data['periods'])} (National: {len(national)}, UP: {len(up)})")
