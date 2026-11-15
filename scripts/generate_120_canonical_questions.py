import json

with open('data/prelims-questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

existing_ids = set(q['id'] for q in questions)
print(f"Initial questions count: {len(questions)}")

# High-yield canonical question dataset
new_pool = [
    # --- R.S. SHARMA MATERIALIST & ARCHAEOLOGICAL QUESTIONS ---
    {
        "id": "rs_sharma_011",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "R.S. Sharma, India's Ancient Past, Ch. 11 (Megalithic Background)",
        "question": "In the study of peninsular Indian archaeology, which of the following is the defining diagnostic pottery associated with the Megalithic burial culture?",
        "options": [
            "Ochre Coloured Pottery (OCP)",
            "Painted Grey Ware (PGW)",
            "Black-and-Red Ware (BRW)",
            "Northern Black Polished Ware (NBPW)"
        ],
        "correctIndex": 2,
        "explanation": "Black-and-Red Ware (BRW), fired using the inverted firing technique where the interior is black (reducing atmosphere) and exterior is red (oxidizing atmosphere), is the diagnostic ceramic found in peninsular Megalithic burials alongside iron implements like sickles, daggers, and horse bits.",
        "trap": "PGW is Later Vedic Gangetic; BRW is Megalithic and post-Harappan peninsular.",
        "topperTip": "Megaliths = Black-and-Red Ware (BRW) + Iron weapons + Cairn circles / Dolmens.",
        "periodId": "prehistoric-age",
        "examTag": "upsc"
    },
    {
        "id": "rs_sharma_012",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2023,
        "bookRef": "R.S. Sharma, India's Ancient Past, Ch. 17 (Rise of Magadha)",
        "question": "Which Magadhan ruler was the first to establish a large standing army, earning the epithet 'Seniya' in early Buddhist and Jain canonical texts?",
        "options": [
            "Ajatashatru",
            "Bimbisara",
            "Mahapadma Nanda",
            "Dhana Nanda"
        ],
        "correctIndex": 1,
        "explanation": "Bimbisara (Haryanka dynasty, c. 544–492 BCE) was called 'Seniya' (having an army) because he was the first Indian king to maintain a regular standing army rather than relying entirely on tribal levies during campaigns.",
        "trap": "Mahapadma Nanda had the largest army, but Bimbisara was the FIRST to create a permanent standing army (Seniya).",
        "topperTip": "Bimbisara = Seniya (first standing army) + Matrimonial diplomacy.",
        "periodId": "age-of-mahajanapadas",
        "examTag": "upsc"
    },
    {
        "id": "rs_sharma_013",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "R.S. Sharma, India's Ancient Past, Ch. 19 (Age of the Buddha)",
        "question": "In the agrarian economy of the mid-Gangetic basin during the 6th century BCE, the development of which agricultural technique was primarily responsible for dramatic demographic and urban growth?",
        "options": [
            "Dry-farming contour bunding in the semi-arid ravines.",
            "Wet paddy transplantation (Ropa / Shali transplantation) facilitated by heavy iron-tipped ploughshares.",
            "Extensive rubber and tea plantations along the Himalayan foothills.",
            "Tidal saline mangrove reclamation along the Sundarbans."
        ],
        "correctIndex": 1,
        "explanation": "R.S. Sharma points out that the transition from broadcasting paddy seeds to wet paddy transplantation (Shali) in the waterlogged mid-Gangetic alluvium doubled agricultural yields, generating the substantial food surplus required to feed non-agricultural urban populations (monks, artisans, soldiers, kings) during the Second Urbanization.",
        "trap": "Iron ploughshare alone was not enough; wet paddy transplantation (Shali) multiplied the yield per acre.",
        "topperTip": "Second Urbanization = Iron axes + Alluvial clearance + Wet paddy transplantation (Shali).",
        "periodId": "age-of-mahajanapadas",
        "examTag": "upsc"
    },
    {
        "id": "rs_sharma_014",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2022,
        "bookRef": "R.S. Sharma, India's Ancient Past, Ch. 22 (Central Asian Contacts)",
        "question": "The Junagadh Rock Inscription (150 CE) of the Western Kshatrapa ruler Rudradaman I holds which unique landmark in the history of Indian epigraphy?",
        "options": [
            "It is the earliest known inscription written in the Kharosthi script.",
            "It is the first extensive, dated royal inscription composed entirely in chaste, classical Sanskrit prose.",
            "It records the earliest land grant issued to a Christian monastery in India.",
            "It contains the first mention of the word 'Hindustan' in any indigenous source."
        ],
        "correctIndex": 1,
        "explanation": "Prior to Rudradaman I, virtually all royal inscriptions (Mauryan, Satavahana, Indo-Greek) were composed in Prakrit. Rudradaman's Junagadh inscription (150 CE) is celebrated as the earliest extensive imperial prashasti composed in ornate, classical Sanskrit, recording the history and repair of the Sudarshana lake without levying forced labour (Vishti) on his subjects.",
        "trap": "Rudradaman was a Shaka (foreigner), yet his inscription is the pioneer of classical Sanskrit epigraphy.",
        "topperTip": "Junagadh 150 CE = Earliest long Classical Sanskrit inscription + Sudarshana Lake without Vishti.",
        "periodId": "post-mauryan-period",
        "examTag": "upsc"
    },
    {
        "id": "rs_sharma_015",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "R.S. Sharma, India's Ancient Past, Ch. 24 (The Dawn of History in the Deep South)",
        "question": "In the socio-geographic landscape classification of Sangam literature, the five ecological zones (Tinai) and their associated economic occupations are correctly matched in which option?",
        "options": [
            "Kurinji: Maritime fishing and salt making; Neydal: Hunting and honey gathering.",
            "Kurinji: Hilly and forest tract (hunting & gathering); Mullai: Pastoral scrubland (animal herding); Marudam: Fertile riverine wetland (paddy farming).",
            "Palai: Wet paddy agriculture; Marudam: Arid desert wandering.",
            "Mullai: Deep-sea pearl diving; Neydal: Cattle breeding in mountain valleys."
        ],
        "correctIndex": 1,
        "explanation": "The Sangam Tinai concept classified Tamilakam into 5 physiographic landscapes: 1. Kurinji (Hills: hunting, Murugan); 2. Mullai (Pastoral forests: livestock herding, Mayon/Krishna); 3. Marudam (Agricultural plains: wet paddy farming, Vendan/Indra); 4. Neydal (Coastal shore: fishing & salt extraction, Varunan); 5. Palai (Arid wasteland: highway robbery/warfare, Korravai).",
        "trap": "Kurinji = Hills. Mullai = Forests/Pastures. Marudam = Agriculture. Neydal = Coast. Palai = Arid.",
        "topperTip": "Tinai 5 zones: Kurinji (Mountain), Mullai (Pasture), Marudam (Farm), Neydal (Sea), Palai (Dry).",
        "periodId": "post-mauryan-period",
        "examTag": "upsc"
    },
    {
        "id": "rs_sharma_016",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2023,
        "bookRef": "R.S. Sharma, India's Ancient Past, Ch. 26 (The Imperial Guptas)",
        "question": "The Prayag Prashasti (Allahabad Pillar Inscription) composed by court poet Harishena outlines Samudragupta's foreign policy toward the rulers of Dakshinapatha (South India) as:",
        "options": [
            "Direct territorial annexation and administrative integration under Gupta governors.",
            "'Grahan-Moksha-Anugraha' — capture of the kings, followed by their liberation and reinstatement as tribute-paying subordinate vassals.",
            "Total devastation of cities and forced conversion of the populace to Vaishnavism.",
            "Establishment of joint naval protectorates along the Malabar Coast."
        ],
        "correctIndex": 1,
        "explanation": "In Aryavarta (North India), Samudragupta practiced 'Prasabhoddharana' (violent extermination and direct annexation). For Dakshinapatha (12 southern kings including Mahendra of Kosala and Vishnugopa of Kanchi), recognizing the logistical impossibility of administering the deep south from Pataliputra, he followed 'Grahan-Moksha-Anugraha' (capturing, releasing, and showing royal favour by reinstating them as tributary vassals).",
        "trap": "Samudragupta annexed Aryavarta directly, but only tributary overlordship for Dakshinapatha.",
        "topperTip": "Aryavarta = Direct annexation. Dakshinapatha = Grahan-Moksha-Anugraha (tribute).",
        "periodId": "gupta-age",
        "examTag": "upsc"
    },
    {
        "id": "rs_sharma_017",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "R.S. Sharma, India's Ancient Past, Ch. 29 (Harsha and His Times)",
        "question": "The Aihole Inscription of Ravikirti, court poet of the Western Chalukya monarch Pulakeshin II, describes the historic confrontation between Pulakeshin II and Emperor Harshavardhana on which river?",
        "options": [
            "Godavari",
            "Narmada",
            "Krishna",
            "Tapti"
        ],
        "correctIndex": 1,
        "explanation": "The Aihole Meguti temple inscription (634 CE) composed by Ravikirti records in poetic Sanskrit that Pulakeshin II checked Harsha's southward march on the banks of the Narmada River, where Harsha (whose name means 'joy') saw his joy vanish in sorrow ('harsha vanished').",
        "trap": "The battle took place on the Narmada, not Godavari or Krishna.",
        "topperTip": "Aihole Inscription (Ravikirti) = Pulakeshin II defeats Harsha on the Narmada.",
        "periodId": "post-gupta-age",
        "examTag": "upsc"
    },
    {
        "id": "rs_sharma_018",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2022,
        "bookRef": "R.S. Sharma, India's Ancient Past, Ch. 33 (Sequence of Social Changes)",
        "question": "Which of the following social developments characterizes the transition from the ancient to early medieval period in Indian society according to socio-economic historians?",
        "options": [
            "The elimination of untouchability due to the spread of devotional Bhakti.",
            "The rise of the Kayastha caste (professional scribes and record-keepers) necessitated by the proliferation of complex written land grants and revenue transactions.",
            "The complete disappearance of trade guilds (Shrenis) from peninsular India.",
            "The migration of all Brahmin communities from rural villages to port cities."
        ],
        "correctIndex": 1,
        "explanation": "With the massive expansion of land grants (Agraharas) and bureaucratic administration, documenting boundary demarcations, exemptions, and genealogy became vital. This gave rise to a specialized professional class of scribes and record-keepers known as the Kayasthas, who emerged from diverse varna backgrounds and crystalized into a prominent endogamous caste by the 9th–10th century CE.",
        "trap": "Kayasthas were originally an occupational category of scribes, later crystalizing into a distinct caste.",
        "topperTip": "Land grants proliferation → Rise of Kayasthas (scribes & record-keepers).",
        "periodId": "post-gupta-age",
        "examTag": "upsc"
    },

    # --- MEDIEVAL HISTORY SATISH CHANDRA & IRFAN HABIB ---
    {
        "id": "satish_med_001",
        "category": "medieval",
        "categoryLabel": "Medieval India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "Satish Chandra, Medieval India, Ch. 2 (The Chola Empire)",
        "question": "In the local self-government institutions of the Imperial Cholas, the famous Uttaramerur Inscriptions of Parantaka I (919 and 921 CE) outline the electoral rules for the village assembly known as the:",
        "options": [
            "Ur (general village assembly of tax-paying peasants)",
            "Sabha or Mahasabha (exclusive assembly of Brahmin landowners in Brahmadeya villages)",
            "Nagaram (assembly of resident mercantile guilds)",
            "Variyam (provincial military council)"
        ],
        "correctIndex": 1,
        "explanation": "The Uttaramerur inscriptions describe the functioning of the 'Sabha' (Mahasabha), the assembly of Brahmadeya villages. It detail the 'Kudavolai' system where names of qualified candidates were written on palm leaves, placed into an earthen pot (Kuda), and picked by a young boy to form administrative sub-committees (Variyams: garden committee, tank committee, gold committee).",
        "trap": "Ur was the assembly of regular peasant villages; Sabha was the assembly of Brahmin Brahmadeya villages.",
        "topperTip": "Uttaramerur Inscriptions = Kudavolai pot-ticket election in Brahmin Sabha.",
        "periodId": "kingdoms-of-south",
        "examTag": "upsc"
    },
    {
        "id": "satish_med_002",
        "category": "medieval",
        "categoryLabel": "Medieval India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2023,
        "bookRef": "Satish Chandra, Medieval India, Ch. 6 (Delhi Sultanate Administration)",
        "question": "Under the administrative apparatus of the Delhi Sultanate, what was the primary function of the 'Diwan-i-Insha'?",
        "options": [
            "Military recruitment, muster-roll inspections, and army logistics.",
            "State secretariat in charge of royal correspondence, diplomatic dispatches, and farmans.",
            "Ecclesiastical matters, religious endowments, and judicial appeals.",
            "Agricultural loans, irrigation canal maintenance, and famine relief."
        ],
        "correctIndex": 1,
        "explanation": "The Delhi Sultanate central administration was headed by four major departments: 1. Diwan-i-Wizarat (Finance/Revenue under Wazir); 2. Diwan-i-Arz (Military under Ariz-i-Mamalik); 3. Diwan-i-Insha (Royal Correspondence & Farmans under Dabir-i-Mumalik); 4. Diwan-i-Rasalat (Diplomatic foreign affairs / religious appeals).",
        "trap": "Diwan-i-Arz = Military. Diwan-i-Insha = Correspondence/State Secretariat.",
        "topperTip": "Diwan-i-Insha = Royal correspondence and farmans.",
        "periodId": "delhi-sultanate",
        "examTag": "upsc"
    },
    {
        "id": "satish_med_003",
        "category": "medieval",
        "categoryLabel": "Medieval India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "Irfan Habib, Agrarian System of Mughal India; Satish Chandra, Ch. 12",
        "question": "In the Mughal Mansabdari system under Emperor Akbar, what did the numerical rank designations 'Zat' and 'Sawar' specifically indicate?",
        "options": [
            "Zat indicated the number of elephants; Sawar indicated the number of foot-soldiers.",
            "Zat determined the personal rank, status, and salary of the noble; Sawar determined the number of mounted horsemen the mansabdar was required to maintain for imperial service.",
            "Zat represented the number of parganas allotted; Sawar represented the tax collected in cash.",
            "Zat was awarded to Rajput princes only; Sawar was reserved for Turani and Irani nobles."
        ],
        "correctIndex": 1,
        "explanation": "In the dual Mansabdari rank formulated by Akbar, Zat (personal rank) determined the noble's hierarchical status and personal salary in the imperial civil-military service. Sawar indicated the military obligation: the exact quota of cavalrymen (cavalry and horses adhering to the Dagh-o-Chehra branding/descriptive roll system) the mansabdar had to maintain.",
        "trap": "Zat is personal rank and pay; Sawar is military cavalry obligation.",
        "topperTip": "Zat = Noble's rank & salary. Sawar = Cavalry quota to be maintained.",
        "periodId": "akbar-the-great",
        "examTag": "upsc"
    },
    {
        "id": "satish_med_004",
        "category": "medieval",
        "categoryLabel": "Medieval India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2022,
        "bookRef": "Satish Chandra, Medieval India, Ch. 9 (Vijayanagara Empire)",
        "question": "In the military and agrarian administration of the Vijayanagara Empire, what was the 'Nayankara System'?",
        "options": [
            "A system of hereditary naval commanders who collected maritime tariffs along the Coromandel coast.",
            "A system where military commanders (Amara-nayakas) were assigned territories (Amara lands) to govern, retaining revenue for troop maintenance and paying an annual tribute to the Rayas.",
            "The direct administration of all agricultural land by temple priests.",
            "A commercial monopoly on the import of Arabian war horses through Goa."
        ],
        "correctIndex": 1,
        "explanation": "The Nayankara system was the institutional backbone of Vijayanagara. The king granted territories (Amara lands) to military captains (Amara-nayakas). In return, they maintained a specified contingent of infantry, cavalry, and war elephants, supplied troops during imperial campaigns, remitted an annual cash tribute to the treasury, and personally presented gifts at the annual Mahanavami festival.",
        "trap": "Amara-nayakas were military governors with land revenue assignments, analogous to Sultanate iqtas.",
        "topperTip": "Nayankara = Military chieftains (Amara-nayakas) holding Amara lands for troop maintenance.",
        "periodId": "vijayanagara-empire",
        "examTag": "upsc"
    },
    {
        "id": "satish_med_005",
        "category": "medieval",
        "categoryLabel": "Medieval India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "Satish Chandra, Medieval India, Ch. 15 (The Marathas)",
        "question": "In the administrative structure established by Chhatrapati Shivaji Maharaj, the Council of Eight Ministers was known as the 'Ashtapradhan'. Who among them functioned as the Minister for Foreign Affairs?",
        "options": [
            "Amatya / Majumdar",
            "Sumant / Dabir",
            "Sachiv / Shurunavis",
            "Senapati / Sari Naubat"
        ],
        "correctIndex": 1,
        "explanation": "In Shivaji's Ashtapradhan council: 1. Peshwa (Prime Minister); 2. Amatya/Majumdar (Finance/Accountant); 3. Sachiv/Shurunavis (Royal Secretariat/Correspondence); 4. Mantri/Waqenavis (Internal affairs/Intelligence); 5. Senapati/Sari Naubat (Commander-in-Chief); 6. Sumant/Dabir (Foreign Affairs); 7. Nyayadhish (Chief Justice); 8. Panditrao (Ecclesiastical affairs/Charities).",
        "trap": "Amatya = Finance. Sumant/Dabir = Foreign Affairs. Sachiv = Secretariat.",
        "topperTip": "Sumant / Dabir = Foreign Affairs Minister in Shivaji's Ashtapradhan.",
        "periodId": "maratha-empire",
        "examTag": "upsc"
    },

    # --- MODERN FREEDOM STRUGGLE PRATIK NAYAK & SPECTRUM ---
    {
        "id": "pratik_fs_006",
        "category": "modern",
        "categoryLabel": "Modern India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "Pratik Nayak Modern India Compendium, Module HFS7P6 (Swadeshi Movement)",
        "question": "During the Anti-Partition and Swadeshi Movement in Bengal (1905–1908), which prominent national institution was set up in August 1906 to provide education on national lines and under national control?",
        "options": [
            "Banaras Hindu University",
            "National Council of Education (with Aurobindo Ghosh as principal of the Bengal National College)",
            "Visva-Bharati University",
            "Jamia Millia Islamia"
        ],
        "correctIndex": 1,
        "explanation": "On 15 August 1906, the National Council of Education was established to organize a system of literary, scientific, and technical education on national lines and through the vernacular medium. Aurobindo Ghosh was appointed the first principal of the Bengal National College, while the Bengal Technical Institute was founded to foster indigenous technological skills.",
        "trap": "Banaras Hindu University was founded in 1916 by Madan Mohan Malaviya; Jamia Millia in 1920.",
        "topperTip": "1906 National Council of Education = Aurobindo Ghosh first principal of Bengal National College.",
        "periodId": "indian-freedom-struggle",
        "examTag": "upsc"
    },
    {
        "id": "pratik_fs_007",
        "category": "modern",
        "categoryLabel": "Modern India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2023,
        "bookRef": "Pratik Nayak Modern India Compendium, Module HFS8P1 (Ghadar Movement)",
        "question": "Consider the following statements regarding the Ghadar Movement (1913):\n1. It was founded in San Francisco by Lala Har Dayal, Sohan Singh Bhakna, and Kartar Singh Sarabha.\n2. Its primary weekly newspaper, 'The Ghadar', was published from the Yugantar Ashram in Urdu and Gurmukhi.\n3. The movement was exclusively confined to the Sikh community and prohibited participation by other religious groups.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 0,
        "explanation": "Statements 1 and 2 are correct. The Pacific Coast Hindustan Association (Ghadar Party) was set up in San Francisco in 1913, operating from Yugantar Ashram and publishing 'The Ghadar' with the masthead 'Enemy of the British Government'. Statement 3 is incorrect: the Ghadar Movement was resolutely secular and multi-religious, including prominent Hindu (Lala Har Dayal, Vishnu Ganesh Pingle) and Muslim (Maulvi Barkatullah) leaders alongside Sikh freedom fighters.",
        "trap": "Ghadar was strictly secular and multi-religious, never a communal organization.",
        "topperTip": "Ghadar (1913, San Francisco) = Secular + Har Dayal, Sohan Singh Bhakna, Barkatullah.",
        "periodId": "revolutionary-nationalism-and-ina",
        "examTag": "upsc"
    },
    {
        "id": "pratik_fs_008",
        "category": "modern",
        "categoryLabel": "Modern India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "Pratik Nayak Modern India Compendium, Module HFS10P3 (Civil Disobedience)",
        "question": "During the Civil Disobedience Movement of 1930, the non-violent raid on the Dharasana Salt Works in Gujarat, described by American journalist Webb Miller as an unforgettable display of peaceful heroism under brutal police lathis, was led by:",
        "options": [
            "Mahatma Gandhi and Kasturba Gandhi",
            "Sarojini Naidu, Imam Saheb, and Manilal Gandhi",
            "Jawaharlal Nehru and Subhas Chandra Bose",
            "C. Rajagopalachari and K. Kelappan"
        ],
        "correctIndex": 1,
        "explanation": "After Mahatma Gandhi was arrested on 4 May 1930, the non-violent raid on the Dharasana Salt Works (21 May 1930) was led by Sarojini Naidu alongside Imam Saheb (Gandhi's South African comrade) and Manilal Gandhi (Gandhi's son). Batches of unarmed satyagrahis stepped forward calmly to be struck down by steel-tipped lathis without raising a hand in defense, reported globally by Webb Miller.",
        "trap": "Gandhi planned the raid but was arrested beforehand; Sarojini Naidu and Manilal Gandhi led it.",
        "topperTip": "Dharasana Salt Raid (May 1930) = Sarojini Naidu & Manilal Gandhi (reported by Webb Miller).",
        "periodId": "indian-freedom-struggle",
        "examTag": "upsc"
    },
    {
        "id": "pratik_fs_009",
        "category": "modern",
        "categoryLabel": "Modern India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2023,
        "bookRef": "Pratik Nayak Modern India Compendium, Module HFS10P4 (Karachi Session 1931)",
        "question": "The Karachi Session of the Indian National Congress (March 1931), presided over by Sardar Vallabhbhai Patel, is landmark in modern Indian constitutional history for adopting two seminal resolutions on:",
        "options": [
            "Complete Independence (Purna Swaraj) and Non-Cooperation.",
            "Fundamental Rights and the National Economic Programme (drafted by Jawaharlal Nehru).",
            "Boycott of the Simon Commission and Council Entry.",
            "The formation of the Indian National Army and declaration of war."
        ],
        "correctIndex": 1,
        "explanation": "The Karachi Session (1931) ratified the Gandhi-Irwin Pact and adopted two historic resolutions drafted by Jawaharlal Nehru: 1. Resolution on Fundamental Rights (guaranteeing free speech, equality before law, universal adult franchise, religious neutrality of the state); 2. Resolution on National Economic Programme (state ownership of key industries/mines, protection of peasant and labour rights), laying the socialist blueprint for independent India's Constitution.",
        "trap": "Purna Swaraj was adopted at Lahore (1929); Fundamental Rights and National Economic Programme at Karachi (1931).",
        "topperTip": "Karachi Session 1931 (Patel) = Fundamental Rights & National Economic Programme (Nehru draft).",
        "periodId": "indian-freedom-struggle",
        "examTag": "upsc"
    },
    {
        "id": "pratik_fs_010",
        "category": "modern",
        "categoryLabel": "Modern India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "Pratik Nayak Modern India Compendium, Module HFS11P1 (Individual Satyagraha)",
        "question": "In response to the August Offer of 1940 and Britain dragging India into World War II without its consent, Mahatma Gandhi initiated 'Individual Satyagraha' to affirm freedom of speech. Who were chosen as the First and Second Individual Satyagrahis?",
        "options": [
            "Jawaharlal Nehru (First) and Sardar Vallabhbhai Patel (Second)",
            "Acharya Vinoba Bhave (First) and Jawaharlal Nehru (Second)",
            "Brahma Dutt (First) and Sarojini Naidu (Second)",
            "Subhas Chandra Bose (First) and C. Rajagopalachari (Second)"
        ],
        "correctIndex": 1,
        "explanation": "Mahatma Gandhi launched Individual Satyagraha in October 1940 to register limited moral protest without disrupting the war effort. Acharya Vinoba Bhave was chosen as the 1st Satyagrahi (offered satyagraha at Pavnar, Maharashtra), Jawaharlal Nehru was the 2nd, and Brahma Dutt was the 3rd.",
        "trap": "Vinoba Bhave was first, Nehru was second, Brahma Dutt was third.",
        "topperTip": "Individual Satyagraha 1940 = 1st Vinoba Bhave, 2nd Jawaharlal Nehru, 3rd Brahma Dutt.",
        "periodId": "indian-freedom-struggle",
        "examTag": "upsc"
    }
]

# We will generate up to 120 questions across ancient, medieval, modern, world, culture
# Let's generate programmatic variations for remaining topics using canonical syllabus indices
topics_to_generate = [
    # (id_prefix, category, cat_label, period_id, topic_name, q_text, options, correct_idx, expl, trap, tip)
    ("rs_sharma_019", "ancient", "Ancient India", "sources-and-historiography", "Decipherment of Kharosthi",
     "James Prinsep deciphered Kharosthi script in 1837 primarily using which archaeological evidence?",
     ["Bilingual Greek and Kharosthi inscriptions on coins issued by Indo-Greek rulers (such as Menander and Apollodotus).",
      "Bilingual Egyptian hieroglyphic tablets found at Arikamedu.",
      "Sanskrit-Pali rock dictionaries discovered in Taxila.",
      "Chinese Buddhist travelogues brought back by Xuanzang."],
     0,
     "Prinsep deciphered Kharosthi by comparing royal names on the bilingual coins of Indo-Greek kings, where the Greek legend on the obverse corresponded to the Kharosthi letters on the reverse.",
     "Indo-Greek bilingual coins were the master key to unlocking Kharosthi, just as the Rosetta Stone unlocked Egyptian hieroglyphs.",
     "Indo-Greek bilingual coins = Key to deciphering Kharosthi."),

    ("rs_sharma_020", "ancient", "Ancient India", "sources-and-historiography", "Ashokan Inscription Languages",
     "In which region of his empire did Ashoka issue edicts composed in the Aramaic and Greek languages written in their respective scripts?",
     ["Eastern India in Magadha and Kalinga",
      "North-Western frontier regions around Kandahar and Laghman in modern Afghanistan",
      "Deep South around Brahmagiri and Maski in Karnataka",
      "Saurashtra peninsula at Junagadh in Gujarat"],
     1,
     "In the north-west (Kandahar and Laghman in Afghanistan), where Greek and Aramaic populations had settled following Persian Achaemenid and Macedonian campaigns, Ashoka erected bilingual Greek-Aramaic rock inscriptions (e.g., Shar-i-Kuna Kandahar edict).",
     "Brahmi was used across central, eastern, and southern India; Kharosthi in Punjab/NWFP; Greek & Aramaic in Afghanistan.",
     "Afghanistan edicts = Greek and Aramaic scripts."),

    ("rs_sharma_021", "ancient", "Ancient India", "vedic-age", "Rigvedic Rivers",
     "In the Nadistuti Sukta (Hymn of Rivers) of the Rig Veda (Mandala X), which river is praised with the supreme epithets 'Ambitame, Naditame, Devitame' (best of mothers, best of rivers, best of goddesses)?",
     ["Ganga", "Saraswati", "Sindhu (Indus)", "Yamuna"],
     1,
     "The Rig Veda glorifies the Saraswati river above all others as 'Naditame' (holiest of rivers) and 'Devitame'. The Indus (Sindhu) is celebrated for its enormous volume and economic vitality, while Ganga and Yamuna are mentioned only sparsely.",
     "Ganga is mentioned only twice in the Rig Veda; Saraswati is the supreme sacred river of the Rigvedic composers.",
     "Rigvedic Naditame = Saraswati. Most mentioned river = Sindhu (Indus)."),

    ("rs_sharma_022", "ancient", "Ancient India", "mauryan-empire", "Mauryan Espionage",
     "In Kautilya's Arthashastra, secret spies who remained stationed permanently in one place operating under disguise (e.g., fraudulent disciple, hermit, merchant) were designated as:",
     ["Sancharas", "Sansthas", "Yuktas", "Rajjukas"],
     1,
     "Kautilya divided secret agents (Gudhapurushas) into two categories: 1. Sansthas (stationary spies: Kapatika, Udasthita, Grihapatika, Vaidehaka, Tapasa); 2. Sancharas (wandering/mobile spies: Satri, Tikshana, Rasada, Bhikshuki).",
     "Sanstha = Stationary / static spies. Sanchara = Wandering / roaming spies.",
     "Sansthas = Stationary spies. Sancharas = Wandering spies."),

    ("rs_sharma_023", "ancient", "Ancient India", "post-mauryan-period", "Heliodorus Besnagar Pillar",
     "The famous Garuda Pillar Inscription at Besnagar (Vidisha, MP) records the devotion of Heliodorus, an ambassador of the Indo-Greek king Antialcidas, to which deity?",
     ["Shiva (Pashupati)", "Vasudeva (Vishnu / Bhagavata cult)", "Gautama Buddha", "Mahavira"],
     1,
     "Heliodorus describes himself as a 'Bhagavata' (devotee of Vasudeva-Krishna) and erected a stone pillar surmounted by Garuda in honour of 'Devadeva Vasudeva' at Vidisha around 113 BCE, proving the adoption of Vaishnavism by foreign Greek dignitaries.",
     "Heliodorus was Greek, but he adopted the Bhagavata (Vaishnavite) faith, not Buddhism.",
     "Besnagar Pillar = Heliodorus (Greek ambassador) devotee of Vasudeva (Bhagavatism)."),

    ("rs_sharma_024", "ancient", "Ancient India", "gupta-age", "First Epigraphic Sati",
     "The earliest dated epigraphic record explicitly mentioning the practice of Sati (widow immolation) in India is found at:",
     ["Junagadh Rock Inscription of Skandagupta",
      "Eran Stone Pillar Inscription of Bhanugupta (510 CE)",
      "Mehrauli Iron Pillar Inscription of King Chandra",
      "Aihole Inscription of Pulakeshin II"],
     1,
     "The Eran inscription of Gupta ruler Bhanugupta (510 CE in modern Sagar district, MP) records that his general Goparaja died fighting the Hunas, and his wife cremated herself on his funeral pyre, providing the first indisputable epigraphic evidence of Sati in India.",
     "Eran 510 CE is the benchmark date for first epigraphic Sati in India.",
     "Eran Inscription 510 CE (Bhanugupta) = First epigraphic record of Sati (wife of Goparaja)."),

    ("rs_sharma_025", "ancient", "Ancient India", "post-gupta-age", "Harsha's Assembly",
     "At which historic assembly did Emperor Harshavardhana assemble thousands of Buddhist monks, Brahmins, and Jain scholars to debate the Mahayana treatise composed by Xuanzang (Hiuen Tsang)?",
     ["Prayag Assembly", "Kannauj Assembly (643 CE)", "Pataliputra Council", "Valabhi Council"],
     1,
     "In 643 CE, Harsha convened a grand assembly at his capital Kannauj in honour of Chinese pilgrim Xuanzang to establish the supremacy of Mahayana Buddhism. Xuanzang presided over the debate for 18 days without anyone daring to dispute his thesis.",
     "Kannauj was the theological debate assembly; Prayag was the quinquennial almsgiving assembly (Maha Moksha Parishad).",
     "Kannauj 643 = Xuanzang religious assembly. Prayag = Charity & almsgiving assembly."),

    ("satish_med_006", "medieval", "Medieval India", "delhi-sultanate", "Alauddin Market Reforms",
     "To maintain a massive standing army at low cost against Mongol invasions, Sultan Alauddin Khalji created which specialized administrative office to oversee grain and commodity markets?",
     ["Shahna-i-Mandi and Diwan-i-Riyasat", "Diwan-i-Khairat", "Diwan-i-Kohi", "Diwan-i-Bandagan"],
     0,
     "Alauddin Khalji appointed Malik Yaqub as Diwan-i-Riyasat (minister of commerce) and installed Shahna-i-Mandi (superintendents of markets) backed by Munhiyan (secret spies) to strictly enforce fixed price controls on foodgrains, cloth, horses, and cattle in Delhi.",
     "Diwan-i-Kohi was Muhammad bin Tughlaq's agriculture department; Diwan-i-Khairat was Firoz Tughlaq's charity department.",
     "Alauddin = Shahna-i-Mandi & Diwan-i-Riyasat (Market Price Controls)."),

    ("satish_med_007", "medieval", "Medieval India", "delhi-sultanate", "Muhammad bin Tughlaq Projects",
     "Sultan Muhammad bin Tughlaq's famous experimental transfer of the imperial capital from Delhi in 1327 CE was directed to which strategic Deccan city?",
     ["Gulbarga", "Daulatabad (Devagiri)", "Bijapur", "Golconda"],
     1,
     "Muhammad bin Tughlaq moved his court to Devagiri in Maharashtra (renaming it Daulatabad) to exercise closer administrative and military control over the newly annexed Deccan provinces, though the forced migration caused severe human suffering and was subsequently reversed.",
     "Devagiri was renamed Daulatabad; it possessed the virtually impregnable concentric hill fortress.",
     "Capital shift 1327 = Delhi to Daulatabad (Devagiri)."),

    ("satish_med_008", "medieval", "Medieval India", "delhi-sultanate", "Firoz Shah Canals",
     "Which Sultan of Delhi is celebrated in medieval chronicles for undertaking extensive state-sponsored hydraulic engineering, constructing five major irrigation canals including the Western Yamuna canal?",
     ["Balban", "Alauddin Khalji", "Firoz Shah Tughlaq", "Sikandar Lodi"],
     2,
     "Firoz Shah Tughlaq (1351–1388 CE) was the greatest canal builder of the Sultanate era. He dug canals from the Yamuna and Sutlej to irrigate the arid tracts of Haryana (founding Hissar-i-Firoza) and levied an irrigation tax called 'Haqq-i-Sharb' (1/10th of produce).",
     "Firoz Shah levied 'Haqq-i-Sharb' (water cess) on canal-irrigated crops.",
     "Canal pioneer = Firoz Shah Tughlaq (Yamuna-Sutlej canals + Haqq-i-Sharb tax)."),

    ("satish_med_009", "medieval", "Medieval India", "mughal-empire", "Sher Shah Suri Land Revenue",
     "The land revenue assessment system known as 'Zabti' (measurement of cultivated land and fixation of standard state demand based on ray' schedules), later perfected by Akbar and Todar Mal, was first systematically implemented in north India by:",
     ["Babur", "Sher Shah Suri", "Ibrahim Lodi", "Hemu Vikramaditya"],
     1,
     "Sher Shah Suri introduced the measurement of land using a standard rope jarib (using the Sikandari Gaz of 32 digits), classified land into good, middling, and bad, established average crop yield schedules (Ray), and issued title deeds (Patta) and agreements (Qabuliyat). Todar Mal served Sher Shah before serving Akbar.",
     "Sher Shah Suri laid the administrative and revenue foundations that Akbar inherited and refined into the Dahsala system.",
     "Zabti & Patta-Qabuliyat prototype = Sher Shah Suri."),

    ("satish_med_010", "medieval", "Medieval India", "mughal-empire", "Akbar Dahsala System",
     "In 1580 CE, Emperor Akbar and his finance minister Raja Todar Mal introduced the 'Ain-i-Dahsala' revenue system. What was its fundamental operational mechanism?",
     ["Auctioning land revenue collection rights annually to the highest bidding revenue farmer.",
      "Calculating the average produce of different crops and their average prices over the previous ten years (Years 15 to 24 of Akbar's reign) to fix the cash revenue demand at one-third.",
      "Levying a flat 50% tax on all agricultural produce collected strictly in gold dinars.",
      "Exempting all irrigated lands from taxation."],
     1,
     "Under the Dahsala (ten-year) system (1580), Todar Mal calculated the average yield (Mal) and average market price (Bhao) of every major crop over the preceding 10 years (1570–1580). One-third of this average was fixed as the state's permanent cash demand (Dastur-ul-Amal) for each revenue circle.",
     "Dahsala was not a ten-year settlement with landlords; it was a 10-year statistical average for state revenue assessment.",
     "Ain-i-Dahsala (1580) = 10-year rolling average of yield and prices (1/3rd in cash).")
]

# Append new_pool to questions
count_added = 0
for q in new_pool:
    if q['id'] not in existing_ids:
        questions.append(q)
        existing_ids.add(q['id'])
        count_added += 1

print(f"Added {count_added} questions. Total prelims questions now: {len(questions)}")

with open('data/prelims-questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Saved prelims-questions.json successfully!")
