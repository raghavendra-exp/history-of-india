# -*- coding: utf-8 -*-
import json

# 1. Add Prelims Questions
with open('data/prelims-questions.json', 'r', encoding='utf-8') as f:
    prelims = json.load(f)

existing_p_ids = {q['id'] for q in prelims}

new_prelims = [
    {
        "id": "prelims-culture-paintings-01",
        "question": "With reference to the mural paintings of Ajanta, consider the following statements:\n1. The paintings were executed using pure fresco buono technique on wet lime plaster.\n2. The murals predominantly depict Jataka stories and episodes from the life of Gautama Buddha.\n3. The famous depiction of Bodhisattva Padmapani holding a blue lotus is located in Cave 1.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 1,
        "explanation": "Statement 1 is incorrect: Ajanta paintings are not pure fresco buono; they were executed using tempera on a dry ground (fresco secco) prepared with a layer of clay, cow dung, and rice husk finished with a coat of lime. Statements 2 and 3 are correct: They depict Jataka tales, and the masterwork Bodhisattva Padmapani is in Cave 1.",
        "category": "art-culture",
        "difficulty": "hard",
        "bookRef": "Nitin Singhania, Ch. 2; NCERT Class 11 Fine Arts Ch. 5"
    },
    {
        "id": "prelims-culture-dance-01",
        "question": "Consider the following pairs of Indian Classical Dance forms and their associated primary thematic or structural elements:\n1. Sattriya: Developed by Srimanta Sankaradeva and performed in Vaishnavite monastic Sattras\n2. Mohiniyattam: Known for dramatic facial makeup (Paccha, Kathi) and aggressive martial footwork\n3. Kuchipudi: Features the 'Tarangam' where the dancer balances on the brass rim of a plate\nWhich of the pairs given above are correctly matched?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 2,
        "explanation": "Pair 1 is correctly matched: Sattriya was introduced in the 15th century by Srimanta Sankaradeva in Assam. Pair 2 is incorrectly matched: Elaborate makeup with Paccha and Kathi belongs to Kathakali, whereas Mohiniyattam is characterized by graceful feminine Lasya movements and white-gold Kasavu attire. Pair 3 is correctly matched: Tarangam is a signature feature of Kuchipudi.",
        "category": "art-culture",
        "difficulty": "medium",
        "bookRef": "Nitin Singhania, Ch. 3; CCRT Performing Arts"
    },
    {
        "id": "prelims-culture-music-01",
        "question": "With reference to traditional Indian musical instruments and their classification in the ancient Natyashastra, which of the following is an example of an 'Avanaddha Vadya'?",
        "options": [
            "Santoor and Sitar",
            "Bansuri and Shehnai",
            "Mridangam and Tabla",
            "Manjira and Jaltarang"
        ],
        "correctIndex": 2,
        "explanation": "According to the Natyashastra: Tata Vadya = Stringed instruments (Sitar, Veena); Sushira Vadya = Wind instruments (Bansuri, Shehnai); Avanaddha Vadya = Percussion instruments with animal hide membranes (Mridangam, Tabla, Pakhawaj); Ghana Vadya = Solid idiophones (Manjira, Ghatam).",
        "category": "art-culture",
        "difficulty": "medium",
        "bookRef": "Nitin Singhania, Ch. 4; CCRT Music"
    },
    {
        "id": "prelims-culture-arch-01",
        "question": "With reference to Nagara temple architecture, the miniature towers or subsidiary turrets that cluster around the central main spire are known as:",
        "options": [
            "Amalaka",
            "Urushringa",
            "Antarala",
            "Gopuram"
        ],
        "correctIndex": 1,
        "explanation": "In Nagara temple architecture, especially in the Khajuraho / Chandela style, the miniature subsidiary tower spires that cling to the central Shikhara to accentuate its height and cosmic mountain symbolism are called Urushringas. Amalaka is the stone crowning disc; Antarala is the vestibule; Gopuram belongs to Dravidian architecture.",
        "category": "art-culture",
        "difficulty": "medium",
        "bookRef": "Nitin Singhania, Ch. 1; Percy Brown, Indian Architecture"
    },
    {
        "id": "prelims-culture-pottery-01",
        "question": "Which of the following represents the correct chronological sequence of archaeological pottery traditions in ancient India from earliest to latest?",
        "options": [
            "Northern Black Polished Ware (NBPW) -> Painted Grey Ware (PGW) -> Black and Red Ware (BRW) -> Ochre Coloured Pottery (OCP)",
            "Ochre Coloured Pottery (OCP) -> Black and Red Ware (BRW) -> Painted Grey Ware (PGW) -> Northern Black Polished Ware (NBPW)",
            "Painted Grey Ware (PGW) -> Ochre Coloured Pottery (OCP) -> Northern Black Polished Ware (NBPW) -> Black and Red Ware (BRW)",
            "Black and Red Ware (BRW) -> Northern Black Polished Ware (NBPW) -> Ochre Coloured Pottery (OCP) -> Painted Grey Ware (PGW)"
        ],
        "correctIndex": 1,
        "explanation": "The correct chronological sequence established by Indian archaeology is: OCP (Late Harappan/Copper Hoard, c. 2000-1500 BCE) -> BRW (Chalcolithic/Early Iron) -> PGW (Later Vedic, c. 1100-600 BCE) -> NBPW (Mahajanapadas and Mauryan Urbanization, c. 600-200 BCE).",
        "category": "ancient",
        "difficulty": "hard",
        "bookRef": "R.S. Sharma, Ch. 12; Upinder Singh, Ch. 6"
    },
    {
        "id": "prelims-society-diversity-01",
        "question": "With reference to the linguistic profile of India, consider the following statements:\n1. The Austroasiatic language family in India is primarily represented by the Munda and Khasi language branches.\n2. The Constitution of India under Article 343 declares Hindi in Devanagari script as the National Language of India.\n3. English was originally intended to be used for official purposes for a period of fifteen years from the commencement of the Constitution.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 1,
        "explanation": "Statement 1 is correct: Austroasiatic languages in India include Santhali, Mundari, Ho, and Khasi. Statement 2 is incorrect: Article 343 declares Hindi in Devanagari script as the 'Official Language of the Union', not the 'National Language' (the Indian Constitution has no national language). Statement 3 is correct: Article 343(2) provided that English would continue for 15 years (until 1965), which was later extended indefinitely by the Official Languages Act of 1963.",
        "category": "modern",
        "difficulty": "hard",
        "bookRef": "Ram Ahuja, Ch. 2; NCERT Class 12 Indian Society Ch. 6"
    },
    {
        "id": "prelims-society-poverty-01",
        "question": "Which of the following Expert Committees on Poverty Estimation in India first departed from the traditional minimum calorie intake norm and adopted per capita consumption expenditure on private health, education, and clothing?",
        "options": [
            "Y.K. Alagh Committee (1979)",
            "D.T. Lakdawala Committee (1993)",
            "Suresh Tendulkar Committee (2009)",
            "C. Rangarajan Committee (2014)"
        ],
        "correctIndex": 2,
        "explanation": "The Suresh Tendulkar Committee (appointed in 2005, submitted report in 2009) formally moved away from the calorie-anchored poverty line and based the poverty line basket on actual private per capita consumer expenditure on health, education, clothing, and shelter, calculating poverty at Rs 27/day in rural areas and Rs 33/day in urban areas.",
        "category": "modern",
        "difficulty": "medium",
        "bookRef": "Ram Ahuja, Ch. 3; NITI Aayog Poverty Reports"
    },
    {
        "id": "prelims-society-secularism-01",
        "question": "In which of the following landmark judgments did the Supreme Court of India hold that 'Secularism is a basic feature of the Constitution', empowering the President to dismiss any state government that acts against secular principles?",
        "options": [
            "Kesavananda Bharati v. State of Kerala (1973)",
            "Minerva Mills v. Union of India (1980)",
            "S.R. Bommai v. Union of India (1994)",
            "Shayara Bano v. Union of India (2017)"
        ],
        "correctIndex": 2,
        "explanation": "In S.R. Bommai v. Union of India (1994), a 9-judge Constitution bench explicitly affirmed that Secularism is an integral component of the Basic Structure of the Indian Constitution, and that state governments promoting communal polarization or violating secularism can be dissolved under Article 356.",
        "category": "modern",
        "difficulty": "medium",
        "bookRef": "Ram Ahuja, Ch. 16; NCERT Class 11 Political Theory Ch. 8"
    },
    {
        "id": "prelims-medieval-maratha-01",
        "question": "In the Ashtapradhan administrative council of Chhatrapati Shivaji Maharaj, what was the primary portfolio of the minister designated as 'Amatya'?",
        "options": [
            "Prime Minister and general administration",
            "Commander-in-Chief of military forces",
            "Finance and Revenue Minister maintaining state accounts",
            "Foreign Affairs and diplomatic relations"
        ],
        "correctIndex": 2,
        "explanation": "In Shivaji's Ashtapradhan council: Peshwa = Prime Minister; Amatya (or Mazumdar) = Finance and Revenue Minister; Senapati (Sari-Naubat) = Commander-in-Chief; Sumant (Dabir) = Foreign Affairs; Waqia-Navis (Mantri) = Intelligence and household records.",
        "category": "medieval",
        "difficulty": "medium",
        "bookRef": "Satish Chandra, Ch. 19; Spectrum Modern India"
    },
    {
        "id": "prelims-medieval-deccan-01",
        "question": "Which ruler of the Deccan Sultanates composed the celebrated musical and poetic treatise 'Kitab-i-Navras' in Dakhani Urdu, and was venerated by his subjects as 'Jagadguru Badshah'?",
        "options": [
            "Muhammad Quli Qutb Shah of Golconda",
            "Ibrahim Adil Shah II of Bijapur",
            "Malik Ambar of Ahmednagar",
            "Ali Adil Shah I of Bijapur"
        ],
        "correctIndex": 1,
        "explanation": "Ibrahim Adil Shah II (1580–1627) of the Bijapur Adil Shahi dynasty wrote the Kitab-i-Navras, an anthology of 59 songs and 17 couplets set to classical Indian ragas, paying reverent homage to Saraswati, Ganesha, and Hazrat Gesudaraz.",
        "category": "medieval",
        "difficulty": "medium",
        "bookRef": "Satish Chandra, Ch. 13; Nitin Singhania, Ch. 4"
    },
    {
        "id": "prelims-world-coldwar-01",
        "question": "With reference to the Cold War and Asian-African geopolitical developments, the 10 Principles of Peaceful Coexistence and South-South cooperation were formulated at the:",
        "options": [
            "Yalta Conference (1945)",
            "Potsdam Conference (1945)",
            "Bandung Conference (1955)",
            "Geneva Accords (1954)"
        ],
        "correctIndex": 2,
        "explanation": "The Asian-African Conference held in Bandung, Indonesia in April 1955, brought together 29 newly independent nations and adopted the Ten Principles of Bandung (incorporating the Panchsheel principles), which served as the philosophical and diplomatic springboard for the formal establishment of the Non-Aligned Movement (NAM) in Belgrade in 1961.",
        "category": "world",
        "difficulty": "medium",
        "bookRef": "Norman Lowe, Ch. 19; NCERT Class 12 Contemporary World Politics"
    }
]

added_p = 0
for q in new_prelims:
    if q['id'] not in existing_p_ids:
        prelims.append(q)
        existing_p_ids.add(q['id'])
        added_p += 1

with open('data/prelims-questions.json', 'w', encoding='utf-8') as f:
    json.dump(prelims, f, indent=2, ensure_ascii=False)

print(f"Added {added_p} new Prelims MCQs! Total Prelims: {len(prelims)}")

# 2. Add Mains Questions
with open('data/mains-questions.json', 'r', encoding='utf-8') as f:
    mains = json.load(f)

existing_m_ids = {m['id'] for m in mains}

new_mains = [
    {
        "id": "mains-culture-architecture-01",
        "question": "Trace the technological and aesthetic transition from early rock-cut cave architectures to structural free-standing temples in Ancient India, highlighting the landmark contributions of the Gupta and early Chalukyan periods.",
        "marks": 15,
        "wordLimit": 250,
        "category": "art-culture",
        "bookRef": "Nitin Singhania, Ch. 1; Percy Brown, Indian Architecture; Upinder Singh, Ch. 9",
        "framework": {
            "intro": "Indian sacred architecture underwent a seminal structural evolution from subterranean rock-cut excavations (3rd c. BCE to 5th c. CE) to free-standing monumental structural masonry temples, symbolizing the shift from monastic seclusion to vibrant public community devotionalism.",
            "body": [
                {
                    "heading": "Rock-Cut Foundations: The Subterranean Phase",
                    "points": [
                        "Mauryan Barabar caves (Lomas Rishi) introduced barrel-vaulted chaitya halls excavated directly into granite cliffs.",
                        "Western Ghats Buddhist chaityas (Karle, Bhaja, Ajanta) simulated wooden architecture in basalt rock, creating soaring ribs, stupas, and circumambulatory corridors."
                    ]
                },
                {
                    "heading": "The Gupta Genesis: Birth of the Free-Standing Structural Temple",
                    "points": [
                        "Stage 1 (Temple 17 at Sanchi): Flat-roofed, square sanctum (Garbhagriha) with a shallow four-pillared portico (Mandapa).",
                        "Stage 2 (Nachna Kuthara & Parvati Temple): Addition of an ambulatory pathway (Pradakshina Path) around the sanctum.",
                        "Stage 3 (Dashavatara Temple, Deogarh): Introduction of the early curvilinear Shikhara (superstructure) and the Panchayatan cruciform layout with 4 corner subsidiary shrines.",
                        "Brick Masonry Innovation: Bhitargaon Temple (Kanpur) utilizing molded terracotta and true arch engineering."
                    ]
                },
                {
                    "heading": "The Early Chalukyan Crucible at Aihole & Pattadakal",
                    "points": [
                        "Aihole ('Cradle of Indian Temple Architecture'): Experimentation across styles (Lad Khan flat-roofed temple, Durga Temple featuring an apsidal chaitya-type floor plan).",
                        "Pattadakal (UNESCO site): Co-existence and cross-pollination of Nagara (Papanatha) and Dravida (Virupaksha) orders, laying the bedrock for the hybrid Vesara style."
                    ]
                }
            ],
            "conclusion": "This transition liberated Indian architecture from the geological limitations of rock cliffs, enabling vertical cosmic spires (Shikharas and Vimanas) that mirrored sacred cosmology and anchored urban socio-economic life.",
            "diagramMapIdea": "Schematic structural evolution flowchart: Barabar Cave arch -> Sanchi Temple 17 flat roof -> Deogarh Panchayatan with Shikhara -> Pattadakal Virupaksha Vimana."
        }
    },
    {
        "id": "mains-society-urbanization-01",
        "question": "Indian urbanization is paradoxically characterized by economic agglomeration on one hand and acute civic infrastructure collapse and slum proliferation on the other. Critically analyze the structural deficiencies of Urban Local Bodies (ULBs) in addressing this crisis.",
        "marks": 15,
        "wordLimit": 250,
        "category": "modern",
        "bookRef": "Ram Ahuja, Ch. 12; NCERT Class 12 Social Change Ch. 6; NITI Aayog Urban Reports",
        "framework": {
            "intro": "India's urban population (377 million in 2011, projected to exceed 600 million by 2036) drives over 65% of national GDP; however, this rapid economic agglomeration has outpaced municipal governance capacity, resulting in polluted, flood-prone cities and expanding informal settlements (slums).",
            "body": [
                {
                    "heading": "Manifestations of the Urban Civic Crisis",
                    "points": [
                        "Severe Service Delivery Deficits: Severe water stress ('Day Zero' threats in Bengaluru, Chennai), untreated sewage discharge into urban water bodies, and acute landfill crises (Ghazipur, Deonar).",
                        "Urban Flooding & Ecological Encroachment: Unchecked construction over natural wetlands, floodplains, and stormwater drains (e.g., Chennai 2015, Bengaluru 2022).",
                        "Informalization & Slum Proliferation: Over 17% of urban households residing in slums lacking tenure security, clean piped water, and private sanitation."
                    ]
                },
                {
                    "heading": "Structural Deficiencies of Urban Local Bodies (The 3Fs Crisis)",
                    "points": [
                        "Lack of Financial Autonomy (Funds): Municipal revenue accounts for less than 1% of GDP (compared to ~6% in South Africa and Brazil); chronic underutilization of property tax and extreme reliance on state grants.",
                        "Administrative Atrophy (Functionaries): Severe staff shortages, absence of dedicated municipal cadres, lack of trained urban planners and GIS specialists.",
                        "Withheld Devolution (Functions): State governments reluctant to devolve the 18 functions enumerated in the 12th Schedule; creation of parallel parastatal bodies (Development Authorities, Water Boards) that usurp municipal authority.",
                        "Weak Political Leadership: The position of the City Mayor remains largely ceremonial with short one-year tenures, while executive power is concentrated in the state-appointed Municipal Commissioner."
                    ]
                },
                {
                    "heading": "Strategic Policy Remedies",
                    "points": [
                        "Empower Mayors with directly elected 5-year terms and executive administrative powers.",
                        "Strengthen municipal municipal bond markets and credit rating of ULBs for self-sustaining capital mobilization.",
                        "Mandate GIS-based master spatial planning and Transit-Oriented Development (TOD) integrating Smart Cities and AMRUT missions."
                    ]
                }
            ],
            "conclusion": "True urban sustainability requires transitioning from ad-hoc programmatic missions to structural fiscal and political decentralization, breathing real democratic life into the 74th Constitutional Amendment.",
            "diagramMapIdea": "Vicious Cycle of Urban Governance Diagram: Low Fiscal Autonomy -> Poor Civic Delivery -> Low Citizen Tax Compliance -> Parastatal Encroachment -> Crippled ULBs."
        }
    },
    {
        "id": "mains-society-women-01",
        "question": "Examine the evolution of women's organizations in India from elite-led social reform associations of the early 20th century to grassroots mass-based movements in contemporary times.",
        "marks": 15,
        "wordLimit": 250,
        "category": "modern",
        "bookRef": "Ram Ahuja, Ch. 5; NCERT Class 12 Social Change Ch. 8; Bipan Chandra",
        "framework": {
            "intro": "The Indian women's movement has transformed over a century from top-down, urban elite-led institutional petitions in the colonial era into decentralized, autonomous, intersectional grassroots struggles for socio-economic justice, bodily autonomy, and political representation.",
            "body": [
                {
                    "heading": "Early 20th Century: Elite-Led Institutional Pioneers",
                    "points": [
                        "Pioneered by upper-class, educated women: Bharat Stree Mahamandal (1910, Sarala Devi Chaudhurani), Women's Indian Association (1917, Annie Besant), All India Women's Conference (1927).",
                        "Primary Focus: Focused on legal rights, female education, child marriage abolition (Sarda Act 1929), and limited franchise within the colonial constitutional framework.",
                        "Limitations: Lacked deep agrarian penetration and remained largely detached from the daily realities of peasant, working-class, and lower-caste women."
                    ]
                },
                {
                    "heading": "Peasant Struggles & Mass Freedom Mobilization",
                    "points": [
                        "Radical Agrarian Mobilization: Tebhaga Nari Bahini in Bengal, active armed resistance by peasant women in the Telangana Armed Struggle against feudal landlords.",
                        "Mass Nationalist Upsurge: Tens of thousands of ordinary women participating in picketing, salt satyagrahas, underground radio networks (Usha Mehta), and military regiments (Rani of Jhansi Regiment in INA)."
                    ]
                },
                {
                    "heading": "Post-Independence Radicalism & Contemporary Grassroots Surge",
                    "points": [
                        "The 1970s Turning Point: CSWI 'Towards Equality' Report (1974) sparked autonomous feminist collectives (Saheli, Stree Shakti Sanghatana) targeting dowry murders, rape laws, and domestic violence.",
                        "Economic Unionization: Self-Employed Women's Association (SEWA by Ela Bhatt, 1972) organizing millions of informal street vendors, waste pickers, and home-based artisans.",
                        "Self-Help Group (SHG) Revolution: Kudumbashree (Kerala) and Mission Shakti (Odisha) mobilizing rural women into micro-enterprises and local governance, dismantling caste and gender barriers at the village level.",
                        "Legislative Milestone: Passage of the Nari Shakti Vandan Adhiniyam (106th CAA 2023) guaranteeing 33% representation in Lok Sabha and Assemblies."
                    ]
                }
            ],
            "conclusion": "The contemporary Indian women's movement has achieved authentic democratization, transitioning from benevolence to rights, and from elite drawing rooms to the rural hinterland and democratic halls of power.",
            "diagramMapIdea": "Timeline flowchart: 1910s Elite Reform (AIWC, WIA) -> 1940s Agrarian & Freedom Struggles (Tebhaga, INA) -> 1970s Autonomous Collectives & SEWA -> 2000s SHGs (Kudumbashree) & 106th CAA."
        }
    },
    {
        "id": "mains-world-philosophies-01",
        "question": "The 20th century witnessed an ideological contest between Capitalism, Communism, and Democratic Socialism. Analyze their contrasting structural tenets and assess their respective impacts on human welfare and social equity.",
        "marks": 15,
        "wordLimit": 250,
        "category": "world-history",
        "bookRef": "Norman Lowe, Ch. 8, 14; NCERT Class 9 & 11 World History",
        "framework": {
            "intro": "The 20th century was defined by a titanic philosophical and economic conflict among three distinct modes of organizing human civilization: free-market Capitalism, state-monopolized Marxist Communism, and redistributive Democratic Socialism.",
            "body": [
                {
                    "heading": "Comparative Structural Tenets",
                    "points": [
                        "Capitalism (Adam Smith, Hayek): Private ownership of capital, profit motive, market price discovery, competition, and minimal state interference (laissez-faire).",
                        "Communism (Marx, Lenin): Elimination of private property, collective state ownership of all means of production, central command planning, and vanguard party dictatorship.",
                        "Democratic Socialism / Social Democracy (Fabians, Nordic Model): Synthesis of democratic political liberty with state regulation of commanding heights, progressive taxation, and universal social safety nets."
                    ]
                },
                {
                    "heading": "Impact on Human Welfare & Economic Efficiency",
                    "points": [
                        "Capitalism: Unleashed unprecedented technological innovation, industrial efficiency, global trade, and consumer prosperity; however, produced acute wealth inequality (Oxfam data), environmental degradation, and cyclical market crashes (Great Depression 1929).",
                        "Communism: Rapidly industrialized agrarian nations (USSR, China), eradicated extreme illiteracy, and guaranteed basic employment; however, caused totalitarian terror (Stalinist purges, Gulags), suppressed civil liberties, and collapsed under bureaucratic inefficiencies and shortages by 1991.",
                        "Democratic Socialism: Successfully institutionalized universal healthcare, public education, labor dignity, and low Gini coefficients in Western Europe (Nordic countries), proving that economic dynamism can co-exist with egalitarian social justice."
                    ]
                },
                {
                    "heading": "Relevance to India's Developmental Path",
                    "points": [
                        "Post-1947 India consciously adopted a 'Mixed Economy' model guided by Nehruvian democratic socialism, building core public infrastructure while preserving private enterprise and constitutional democracy.",
                        "Post-1991 LPG reforms infused capitalist market efficiency while maintaining massive direct welfare transfers (MGNREGA, NFSA, Ayushman Bharat)."
                    ]
                }
            ],
            "conclusion": "The 21st-century global consensus has gravitated toward a calibrated synthesis: harnessing the productive power of competitive markets while embedding robust social-democratic public investments to protect human dignity and planetary boundaries.",
            "diagramMapIdea": "Comparative triangle diagram linking Capitalism (Market Efficiency), Communism (State Equality), and Democratic Socialism (Balance of Liberty & Welfare)."
        }
    }
]

added_m = 0
for m in new_mains:
    if m['id'] not in existing_m_ids:
        mains.append(m)
        existing_m_ids.add(m['id'])
        added_m += 1

with open('data/mains-questions.json', 'w', encoding='utf-8') as f:
    json.dump(mains, f, indent=2, ensure_ascii=False)

print(f"Added {added_m} new Mains Question Frameworks! Total Mains: {len(mains)}")
