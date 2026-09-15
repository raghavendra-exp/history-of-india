# scripts/gen_ancient.py
import json

def get_ancient_questions():
    qs = []
    
    # Mauryan Empire & Ashoka (anc_056 - anc_075)
    qs.append({
        "id": "anc_056",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2020",
        "isPyq": True,
        "year": 2020,
        "bookRef": "R.S. Sharma, Ch. 14; NCERT Class 11 Themes Theme 2",
        "question": "Who among the following rulers advised his subjects through this inscription?\n'Whosoever praises his religious sect or blames other sects out of excessive devotion to his own sect, with the view of glorifying his own sect, he rather injures his own sect very severely.'",
        "options": [
            "Ashoka",
            "Samudragupta",
            "Harshavardhana",
            "Krishnadevaraya"
        ],
        "correctIndex": 0,
        "explanation": "This famous edict is Major Rock Edict XII of Ashoka, which explicitly preaches religious tolerance, restraint in speech (vachoguti), and honoring other sects to strengthen one's own faith.",
        "trap": "Do not confuse with Harshavardhana, who organized the Kannauj assembly for Buddhism but did not issue such rock edicts.",
        "topperTip": "MRE XII = Religious tolerance and syncretism. MRE XIII = Kalinga war remorse.",
        "periodId": "mauryan-empire"
    })

    qs.append({
        "id": "anc_057",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2019",
        "isPyq": True,
        "year": 2019,
        "bookRef": "Upinder Singh, Ch. 6; R.S. Sharma, Ch. 14",
        "question": "In which of the following relief sculpture inscriptions is 'Ranyo Ashoka' (King Ashoka) mentioned along with the stone portrait of the Emperor?",
        "options": [
            "Kanganahalli",
            "Sanchi",
            "Shahbazgarhi",
            "Sohgaura"
        ],
        "correctIndex": 0,
        "explanation": "At Kanganahalli near Sannati in Kalaburagi district, Karnataka, excavations revealed a limestone relief depicting King Ashoka with his queens, inscribed with the label 'Ranyo Ashoka' in Brahmi script.",
        "trap": "Sanchi has grand stupas, but the labeled portrait sculpture was unearthed at Kanganahalli.",
        "topperTip": "Kanganahalli on the Bhima river is the only site with an identified labeled portrait of Ashoka.",
        "periodId": "mauryan-empire"
    })

    qs.append({
        "id": "anc_058",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2016",
        "isPyq": True,
        "year": 2016,
        "bookRef": "R.S. Sharma, Ch. 14; Upinder Singh, Ch. 6",
        "question": "Regarding the taxation system of the Mauryas, consider the following terms:\n1. Bhaga : Share of agricultural produce, usually 1/6th\n2. Bali : Religious tribute or customary voluntary offering converted into compulsory levy\n3. Vishti : Forced unpaid labour rendered to the state\n4. Kara : Periodic tax levied on orchards and flower gardens\nHow many of the above are correctly matched?",
        "options": [
            "Only one",
            "Only two",
            "Only three",
            "All four"
        ],
        "correctIndex": 3,
        "explanation": "All four terms are correctly matched according to Kautilya's Arthashastra. Bhaga was the principal agricultural tax (1/6th); Bali was an additional levy; Vishti was unpaid forced labour; and Kara was a periodic or special tax levied on fruits, gardens, or subjects.",
        "trap": "Remember: Vishti in the Mauryan and Gupta periods was considered a legitimate source of state labour.",
        "topperTip": "Kautilya categorizes revenue into Rashtra (countryside), Durga (fortified city), Vana (forests), and Khani (mines).",
        "periodId": "mauryan-empire"
    })

    qs.append({
        "id": "anc_059",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2022",
        "isPyq": True,
        "year": 2022,
        "bookRef": "R.S. Sharma, Ch. 14; NCERT Themes in Indian History I",
        "question": "According to Kautilya's Arthashastra, which of the following are correct?\n1. A person could be a slave as a result of a judicial punishment.\n2. If a female slave bore her master a son, she was legally free.\n3. If a son born to a female slave was fathered by her master, the son was entitled to the legal status of the master's son.",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 3,
        "explanation": "Kautilya's Arthashastra devotes a detailed chapter (Book 3, Ch. 13) to Dasas (slaves). Dasa status could result from judicial sentence or capture in war. A female slave who bore her master a child gained freedom, and the child acquired legitimate legal inheritance rights.",
        "trap": "Megasthenes claimed there was no slavery in India, but Indian texts (Arthashastra, Smritis) clearly describe multiple categories of Dasas.",
        "topperTip": "Megasthenes could not distinguish between Indian Dasas and Greek chattel slaves who had no legal rights.",
        "periodId": "mauryan-empire"
    })

    qs.append({
        "id": "anc_060",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "Standard Practice",
        "isPyq": False,
        "year": 2024,
        "bookRef": "Upinder Singh, Ch. 6; R.S. Sharma, Ch. 14",
        "question": "Which of the following Ashokan edicts explicitly mentions five contemporary Greek (Yavana) kings: Antiochus II Theos, Ptolemy II Philadelphus, Antigonus Gonatas, Magas of Cyrene, and Alexander of Epirus?",
        "options": [
            "Major Rock Edict II",
            "Major Rock Edict V",
            "Major Rock Edict XIII",
            "Pillar Edict VII"
        ],
        "correctIndex": 2,
        "explanation": "Major Rock Edict XIII, which recounts the remorse of the Kalinga War, explicitly records that Ashoka achieved 'Dhamma Vijaya' across frontiers ruled by five Hellenistic kings: Amtiyoka (Antiochus), Tulamaya (Ptolemy), Antekina (Antigonus), Maka (Magas), and Alikasudara (Alexander).",
        "trap": "MRE II mentions medical care and herbs to Greek territories, but MRE XIII provides the complete diplomatic list for Dhamma Vijaya.",
        "topperTip": "MRE XIII = Kalinga remorse + 5 Hellenistic contemporary kings.",
        "periodId": "mauryan-empire"
    })

    qs.append({
        "id": "anc_061",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPPSC Prelims 2021",
        "isPyq": True,
        "year": 2021,
        "bookRef": "R.S. Sharma, Ch. 14; Upinder Singh, Ch. 6",
        "question": "The famous Mauryan official 'Samaharta' was primarily responsible for which department?",
        "options": [
            "Assessment and collection of revenue",
            "Custody of the state treasury and storehouse",
            "Administration of the military war council",
            "Chief justice of the civil courts"
        ],
        "correctIndex": 0,
        "explanation": "In Mauryan administration, the 'Samaharta' was the Chief Collector-General / Assessor of Revenue, responsible for maintaining accounts and collecting taxes from across the empire. The 'Sannidhata' was the Chief Treasurer / Keeper of storehouses.",
        "trap": "Samaharta = Assessor/Collector. Sannidhata = Treasurer/Storehouse custodian.",
        "topperTip": "Pair to remember: Samaharta (Collection) vs Sannidhata (Treasury Vault).",
        "periodId": "mauryan-empire"
    })

    qs.append({
        "id": "anc_062",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2023",
        "isPyq": True,
        "year": 2023,
        "bookRef": "Upinder Singh, Ch. 6; NCERT Themes Theme 2",
        "question": "Consider the following pairs of Ashokan sites and their states:\n1. Dhauli : Odisha\n2. Erragudi : Andhra Pradesh\n3. Jaugada : Madhya Pradesh\n4. Kalsi : Karnataka\nHow many of the pairs given above are correctly matched?",
        "options": [
            "Only one pair",
            "Only two pairs",
            "Only three pairs",
            "All four pairs"
        ],
        "correctIndex": 1,
        "explanation": "Pairs 1 and 2 are correctly matched. Jaugada is located in Ganjam district, Odisha (not MP). Kalsi is situated on the banks of Yamuna in Dehradun district, Uttarakhand (not Karnataka).",
        "trap": "Dhauli and Jaugada are the two Major Rock Edict sites in Odisha that contain the Separate Kalinga Edicts.",
        "topperTip": "Kalsi = Uttarakhand; Dhauli & Jaugada = Odisha; Erragudi = Andhra Pradesh.",
        "periodId": "mauryan-empire"
    })

    qs.append({
        "id": "anc_063",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "Standard Practice",
        "isPyq": False,
        "year": 2024,
        "bookRef": "R.S. Sharma, Ch. 14; Upinder Singh, Ch. 6",
        "question": "Regarding the administration of Pataliputra described by Megasthenes in 'Indica', consider the following statements:\n1. The municipal administration was managed by a board of 30 members divided into 6 committees of 5 members each.\n2. The six committees oversaw industrial arts, foreign visitors, registration of births and deaths, trade and commerce, inspection of manufactured goods, and collection of the 1/10th sales tax.\n3. Military administration was managed by a single imperial commander without any committee structure.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 0,
        "explanation": "Statements 1 and 2 are correct. Megasthenes states that Pataliputra was run by 30 commissioners in 6 boards of 5 each. Statement 3 is incorrect because Megasthenes explicitly notes that the military was ALSO administered by a board of 30 members divided into 6 committees.",
        "trap": "Both City (Astynomoi) and Military (Navarchs/Military board) had identical 6x5=30 member board structures!",
        "topperTip": "6 boards of 5 members each governed both the capital city and the armed forces.",
        "periodId": "mauryan-empire"
    })

    qs.append({
        "id": "anc_064",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2022",
        "isPyq": True,
        "year": 2022,
        "bookRef": "Upinder Singh, Ch. 6; R.S. Sharma, Ch. 14",
        "question": "Which one of the following statements about the Barabar and Nagarjuni rock-cut caves is NOT correct?",
        "options": [
            "They were excavated during the Mauryan period for the monks of the Ajivika sect.",
            "Ashoka dedicated the Barabar caves (Karna Chaupar, Sudama, Lomas Rishi).",
            "Dasharatha, the grandson of Ashoka, dedicated caves in the Nagarjuni hills.",
            "The caves contain inscriptions in the Kharosthi script dating to the 1st century CE."
        ],
        "correctIndex": 3,
        "explanation": "Option D is NOT correct. The inscriptions in the Barabar and Nagarjuni caves are written in the Brahmi script in Prakrit language, dating to the 3rd century BCE (reigns of Ashoka and Dasharatha), not Kharosthi or 1st century CE.",
        "trap": "Kharosthi script was restricted to the North-West (Shahbazgarhi, Mansehra). Barabar caves are in Jehanabad district, Bihar.",
        "topperTip": "Barabar = Ashoka + Ajivikas; Nagarjuni = Dasharatha + Ajivikas. Script = Ashokan Brahmi.",
        "periodId": "mauryan-empire"
    })

    qs.append({
        "id": "anc_065",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "Standard Practice",
        "isPyq": False,
        "year": 2024,
        "bookRef": "R.S. Sharma, Ch. 14; Kautilya Arthashastra",
        "question": "In Kautilya's Saptanga theory of the state, what are the seven constituent elements (prakritis) in correct sequence?",
        "options": [
            "Svamin (King), Amatya (Ministers), Janapada (Territory/People), Durga (Fort), Kosha (Treasury), Danda (Army), Mitra (Ally)",
            "Svamin, Danda, Kosha, Durga, Purohita, Amatya, Mitra",
            "Raja, Sena, Sangha, Kosha, Desha, Gramani, Samaharta",
            "Svamin, Janapada, Varna, Ashrama, Danda, Kosha, Shudra"
        ],
        "correctIndex": 0,
        "explanation": "The Saptanga theory (Book 6, Ch. 1 of Arthashastra) defines the state as an organic body with 7 limbs: 1. Svamin (head/ruler), 2. Amatya (eyes/ministers), 3. Janapada (thighs/territory & population), 4. Durga (arms/fortified city), 5. Kosha (mouth/treasury), 6. Danda/Bala (brain/military power), 7. Mitra (ears/allies).",
        "trap": "Purohita is not listed as one of the 7 formal limbs in the Saptanga theory, though highly revered in council.",
        "topperTip": "Mnemonic: S-A-J-D-K-D-M (Svamin, Amatya, Janapada, Durga, Kosha, Danda, Mitra).",
        "periodId": "mauryan-empire"
    })

    # Additional Ancient Qs (anc_066 - anc_130)
    more_ancient = [
        ("anc_066", "gupta-period", "UPSC CSE 2020", True, 2020, "R.S. Sharma, Ch. 16; Upinder Singh, Ch. 7",
         "With reference to the period of the Gupta and post-Gupta dynasties in India, the term 'Araghatta' referred to:",
         ["Bonded labour", "Land grants made to military officers", "Waterwheel used in the irrigation of land", "Wasteland converted to cultivated land"],
         2, "Araghatta (from 'ara' meaning spoke and 'ghatta' meaning pot) refers to the mechanical waterwheel with pots attached to the rim used for lifting water from wells for irrigation.",
         "Do not confuse with Vishti (forced labour) or Agrahara (brahmanical land grants).",
         "Araghatta = Ara (spoke) + Ghatta (pot) = Waterwheel for irrigation."),

        ("anc_067", "sangam-period", "UPSC CSE 2022", True, 2022, "Upinder Singh, Ch. 7; Nitin Singhania, Ch. 13",
         "Which of the following Sangam texts describes the tragic love story of Kovalan and Kannagi, culminating in the burning of Madurai after the Pandyan king wrongly executes Kovalan?",
         ["Silappadikaram", "Manimekalai", "Tolkappiyam", "Purananuru"],
         0, "Silappadikaram ('The Jewelled Anklet'), composed by Ilango Adigal (a Jain prince), narrates the story of Kovalan, his wife Kannagi, and courtesan Madhavi.",
         "Manimekalai is the Buddhist sequel written by Sittalai Sattanar.",
         "Silappadikaram = Ilango Adigal (Anklet, Kannagi). Manimekalai = Sattanar (Daughter, Buddhist)."),

        ("anc_068", "sangam-period", "UPSC CSE 2023", True, 2023, "Upinder Singh, Ch. 7; NCERT Themes Theme 2",
         "In the context of ancient South Indian history, consider the following terms:\n1. Ur : General village assembly of tax-paying peasants\n2. Sabha : Assembly of learned Brahman landholders in Brahmadeya villages\n3. Nagaram : Assembly of merchants and traders in urban trading centers\nHow many of the pairs given above are correctly matched?",
         ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
         2, "All three pairs are correctly matched. In Tamil country, Ur was the non-Brahman village assembly, Sabha was the assembly of Brahman proprietors, and Nagaram was the mercantile assembly.",
         "Sabha was strictly Brahmadeya; Ur was general peasant village.",
         "Ur = Common village. Sabha = Brahman agrahara. Nagaram = Merchants."),

        ("anc_069", "kushan-empire", "UPSC CSE 2017", True, 2017, "R.S. Sharma, Ch. 15; Upinder Singh, Ch. 7",
         "Which of the following dynasties issued the largest hoard of gold coins (dinaras) with high degree of purity and introduced the image of Buddha on coins for the first time?",
         ["Kushans", "Guptas", "Indo-Greeks", "Satavahanas"],
         0, "The Kushans (especially Kanishka I and Huvishka) issued gold coins of remarkable purity. Kanishka's coins feature the earliest verified numismatic representation of the Buddha with legends 'BODDO'.",
         "Indo-Greeks were first to issue gold coins, but Kushans issued the purest gold coins and introduced Buddha.",
         "First gold coins = Indo-Greeks. Purest gold + Buddha = Kushans. Largest total number = Guptas."),

        ("anc_070", "post-mauryan-period", "UPPSC Prelims 2022", True, 2022, "R.S. Sharma, Ch. 15; Upinder Singh, Ch. 7",
         "The Junagadh Rock Inscription of Rudradaman I (c. 150 CE) is significant in Indian history because:",
         ["It is the first long, chaste Sanskrit inscription in ornate kavya style in India.", "It records the victory of the Satavahanas over the Western Kshatrapas.", "It contains the earliest known mention of the Bhakti movement.", "It marks the official adoption of Jainism by the Shaka rulers."],
         0, "The Junagadh rock inscription of Shaka Mahakshatrapa Rudradaman I is the earliest long inscription written in classical, ornate chaste Sanskrit prose (Kavya style) recording repairs to Sudarshana lake.",
         "Ashoka's edicts were in Prakrit. Rudradaman was a Saka ruler who championed classical Sanskrit in royal epigraphs.",
         "Junagadh = Rudradaman (150 CE) + Chaste Sanskrit + Sudarshana Lake repair."),

        ("anc_071", "post-gupta-period", "UPSC CSE 2021", True, 2021, "Upinder Singh, Ch. 7; R.S. Sharma, Ch. 15",
         "With reference to the history of ancient India, Bhavabhuti, Hastimalla, and Kshemeshvara were famous:",
         ["Jain monks", "Playwrights / Dramatists", "Temple architects", "Philosophers of the Charvaka school"],
         1, "Bhavabhuti (author of Malatimadhava, Uttararamacharita), Hastimalla (Jain dramatist), and Kshemeshvara (Chandakaushika) were celebrated Sanskrit dramatists/playwrights.",
         "Hastimalla was a Jain by faith, but in this triad, their common profession was Sanskrit playwrights.",
         "Bhavabhuti is universally renowned as the greatest master of Sanskrit drama after Kalidasa."),

        ("anc_072", "satavahana-dynasty", "Standard Practice", False, 2024, "R.S. Sharma, Ch. 16; Upinder Singh, Ch. 8",
         "Which Satavahana ruler is praised in the Nasik Prasasti of his mother Gautami Balashri as 'Eka-Brahmana' (peerless Brahmana) and 'Khatiya-dapa-mana-madana'?",
         ["Simuka", "Satakarni I", "Gautamiputra Satakarni", "Yajna Sri Satakarni"],
         2, "The Nasik cave inscription of Gautami Balashri eulogizes Gautamiputra Satakarni (c. 106-130 CE) as 'Eka-Brahmana' and destroyer of Kshatriya pride, who overthrew Nahapana.",
         "Gautamiputra Satakarni overstruck Nahapana's silver coins in the Jogalthambi hoard.",
         "Jogalthambi hoard = Gautamiputra Satakarni overstriking Nahapana's coins."),

        ("anc_073", "gupta-period", "UPSC CSE 2020", True, 2020, "Upinder Singh, Ch. 7; Nitin Singhania, Ch. 1",
         "With reference to the scholars/literary figures of ancient India, consider the following statements:\n1. Harishena was the court poet of Chandragupta II.\n2. Kalidasa was associated with Chandragupta II (Vikramaditya).\n3. Amarasimha was patronized by Pushyamitra Shunga.\nWhich of the statements given above is/are correct?",
         ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
         1, "Only statement 2 is correct. Kalidasa was in Chandragupta II's court. Harishena was court poet of Samudragupta (Prayag Prasasti). Amarasimha was also in Chandragupta II's court.",
         "Harishena = Samudragupta; Kalidasa & Amarasimha = Chandragupta II.",
         "Prayag Prasasti was composed by Harishena in Champu kavya style for Samudragupta."),

        ("anc_074", "gupta-period", "UPSC CSE 2019", True, 2019, "Upinder Singh, Ch. 8; R.S. Sharma, Ch. 19",
         "With reference to the forced labour (Vishti) in India during the Gupta period, which one of the following statements is correct?",
         ["It was considered a source of income for the State, a sort of tax paid by the people.", "It was totally absent in the Madhya Pradesh and Kathiawar regions of the Gupta Empire.", "The forced labourer was entitled to weekly wages fixed by the guild.", "The eldest son of the labourer was permanently sent as the forced labourer."],
         0, "During the Gupta period, Vishti was treated as a legitimate royal prerogative and a tax paid by people to the king or landed beneficiaries.",
         "Vishti was unpaid; labourers did not receive wages.",
         "Gupta land grants explicitly mention 'sarva-vishti-parihara' (exempt from all forced labour) when granted to Brahmanas."),

        ("anc_075", "early-medieval-period", "UPSC CSE 2023", True, 2023, "Upinder Singh, Ch. 8; NCERT Themes Theme 2",
         "Consider the following dynasties:\n1. Hoysala\n2. Gahadavala\n3. Kakatiya\n4. Yadava\nHow many of the above dynasties established their kingdoms in the early eighth century CE?",
         ["Only one", "Only two", "Only three", "None"],
         3, "None of these dynasties established their kingdoms in the early 8th century CE. Gahadavalas, Hoysalas, Kakatiyas, and Seuna Yadavas arose in the late 11th and 12th centuries CE.",
         "Early 8th century CE is the era of Yashovarman, Lalitaditya, and early Rashtrakutas.",
         "Kakatiyas, Hoysalas, Yadavas, and Pandyas faced Alauddin Khalji's invasions (1296-1311 CE)."),

        ("anc_076", "gupta-period", "UPSC CSE 2021", True, 2021, "R.S. Sharma, Ch. 19; Upinder Singh, Ch. 8",
         "According to ancient Indian texts, land revenue in the Gupta period was classified into various categories. Which of the following terms denoted cultivable land?",
         ["Kshetra", "Khila", "Aprahata", "Vasti"],
         0, "In Gupta land records (e.g. Paharpur copper plate), Kshetra = cultivated land; Khila = waste/fallow land; Aprahata = uncultivated jungle land; Vasti = habitable land; Gapata-saraha = pasture land.",
         "Khila means fallow/waste, whereas Kshetra is cultivated land.",
         "Kshetra = Cultivated; Khila = Waste; Aprahata = Jungle; Vasti = Habitable."),

        ("anc_077", "gupta-period", "UPSC CSE 2020", True, 2020, "R.S. Sharma, Ch. 19; Upinder Singh, Ch. 8",
         "With reference to the cultural history of India, which of the following is the correct description of the term 'paramitas'?",
         ["The earliest Dharmashastra texts written in aphoristic style", "Philosophical schools that did not accept the authority of the Vedas", "Perfections whose attainment led to the Bodhisattva path", "Powerful merchant guilds of early South India"],
         2, "In Mahayana Buddhism, Paramitas are transcendent virtues or perfections (Dana, Shila, Kshanti, Virya, Dhyana, Prajna) cultivated by a Bodhisattva to attain Buddhahood.",
         "Paramitas are virtues of Bodhisattvas, not merchant guilds or Vedic aphorisms.",
         "Six Paramitas: Generosity, Morality, Patience, Energy, Meditation, Wisdom."),

        ("anc_078", "sangam-period", "UPSC CSE 2023", True, 2023, "Upinder Singh, Ch. 7; Nitin Singhania, Ch. 13",
         "With reference to ancient South India, 'Korkai', 'Poompuhar' and 'Muchiri' were well known as:",
         ["Ports", "Capital cities of the Pallavas", "Buddhist rock-cut cave centers", "Iron smelting sites"],
         0, "Korkai (Pandya pearl fishery port), Poompuhar / Kaveripattinam (Chola port on the Kaveri delta), and Muchiri / Muziris (Chera port on the Malabar coast) were celebrated ancient ports that conducted maritime trade with Rome and Southeast Asia.",
         "Do not confuse these ports with political inland capitals (Uraiyur, Madurai, Vanji).",
         "Muziris = Chera (Pepper & Roman coins); Poompuhar = Chola; Korkai = Pandya (Pearls)."),

        ("anc_079", "sangam-period", "UPSC CSE 2022", True, 2022, "Upinder Singh, Ch. 7; R.S. Sharma, Ch. 16",
         "In ancient Southern India, the five eco-zones or landscapes (Tinais) mentioned in Sangam poetry and their corresponding deities were:\n1. Kurinji (Hills) : Murugan\n2. Mullai (Pastoral) : Mayon (Vishnu)\n3. Marudam (Agricultural plains) : Vendan (Indra)\n4. Neydal (Coastal) : Varunan\n5. Palai (Arid/Desert) : Kotravai\nHow many of the pairs given above are correctly matched?",
         ["Only two", "Only three", "Only four", "All five"],
         3, "All five pairs are correctly matched according to Tolkappiyam Porulatikaram. Kurinji = Murugan (hunting/hills); Mullai = Mayon (pastoral/cattle); Marudam = Vendan (wet paddy fields); Neydal = Varunan (sea/fishing); Palai = Kotravai (war goddess of arid lands).",
         "Tolkappiyam classifies human emotions and geography into five distinct Tinais.",
         "All 5 Tinais reflect direct ecological adaptation to nature and livelihood."),

        ("anc_080", "kushan-empire", "UPSC CSE 2021", True, 2021, "R.S. Sharma, Ch. 15; Upinder Singh, Ch. 7",
         "The Fourth Buddhist Council was held during the reign of which ruler and presided over by which Buddhist scholar?",
         ["Ashoka; Moggaliputta Tissa", "Kanishka; Vasumitra (with Asvagosha as deputy)", "Harshavardhana; Hiuen Tsang", "Ajatashatru; Mahakassapa"],
         1, "The Fourth Buddhist Council was convened by Kushan emperor Kanishka I at Kundalavana in Kashmir. Vasumitra was the President and Ashvaghosha was the Vice-President. It marked the formal division into Mahayana and Hinayana.",
         "Ashoka convened the 3rd Council at Pataliputra; Kanishka convened the 4th Council in Kashmir.",
         "4 Councils: 1st-Rajgriha (Ajatashatru), 2nd-Vaishali (Kalasoka), 3rd-Pataliputra (Ashoka), 4th-Kashmir (Kanishka)."),

        ("anc_081", "post-mauryan-period", "Standard Practice", False, 2024, "Upinder Singh, Ch. 7; R.S. Sharma, Ch. 15",
         "The Heliodorus pillar inscription at Besnagar (Vidisha, MP) is historically invaluable because it records:",
         ["The conversion of a Greek ambassador of king Antialcidas to the Bhagavata (Vaishnava) faith.", "The earliest depiction of the Dashavatara of Vishnu.", "The victory of Pushyamitra Shunga over Demetrius.", "The celebration of an Ashvamedha sacrifice by Kharavela."],
         0, "Heliodorus, an Indo-Greek ambassador sent by King Antialcidas of Taxila to the court of Shunga king Bhagabhadra at Vidisha, erected a Garuda-dhvaja pillar and proclaimed himself a 'Bhagavata' (devotee of Vasudeva-Krishna).",
         "This proves that Greeks (Yavanas) adopted Bhagavata Vaishnavism by the 2nd century BCE.",
         "Besnagar Pillar = Heliodorus + Garuda pillar + Devotion to Vasudeva."),

        ("anc_082", "post-mauryan-period", "UPPSC Prelims 2020", True, 2020, "Upinder Singh, Ch. 7; R.S. Sharma, Ch. 15",
         "The Hathigumpha Inscription of King Kharavela in the Udayagiri hills near Bhubaneswar is composed in which language and script?",
         ["Sanskrit language in Devanagari script", "Prakrit language in Brahmi script", "Odia language in Kalinga script", "Magadhi Prakrit in Kharosthi script"],
         1, "The Hathigumpha inscription of the Chedi ruler Kharavela of Kalinga is engraved in deep-cut Brahmi script and Prakrit language. It documents his military campaigns, canals, and patronage of Jainism in 17 lines.",
         "It is in Prakrit, not Sanskrit or modern Odia.",
         "Hathigumpha = Kharavela + Prakrit Brahmi + Jain patronage + repairs to canal dug by Nandaraja."),

        ("anc_083", "gupta-period", "UPSC CSE 2018", True, 2018, "R.S. Sharma, Ch. 19; Upinder Singh, Ch. 8",
         "With reference to the Indian history of art and culture, consider the following pairs:\n1. Mrichchhakatika : Shudraka\n2. Mudrarakshasa : Vishakhadatta\n3. Devichandraguptam : Vishakhadatta\n4. Malavikagnimitram : Kalidasa\nHow many of the pairs given above are correctly matched?",
         ["Only one pair", "Only two pairs", "Only three pairs", "All four pairs"],
         3, "All four pairs are correctly matched. Shudraka wrote Mrichchhakatika ('The Little Clay Cart'); Vishakhadatta wrote both Mudrarakshasa (Chandragupta Maurya's rise) and Devichandraguptam (Ramagupta and Dhruvadevi); Kalidasa wrote Malavikagnimitram (love story of Shunga prince Agnimitra and Malavika).",
         "Mudrarakshasa is unique as a Sanskrit play without female lead or romantic theme.",
         "All four are masterworks of classical Sanskrit drama."),

        ("anc_084", "gupta-period", "UPSC CSE 2017", True, 2017, "R.S. Sharma, Ch. 19; Upinder Singh, Ch. 8",
         "In the Allahabad Pillar Inscription (Prayag Prasasti), Samudragupta's policy towards the rulers of Dakshinapatha (South India) is described as:",
         ["Prasabhoddharana (violent extermination)", "Grahana-Mokshanugraha (capturing, releasing, and reinstating as tributary vassals)", "Sarva-karadana (complete annexation and direct administrative rule)", "Kanyopayanadana (matrimonial alliances)"],
         1, "Samudragupta pursued 'Prasabhoddharana' (complete extermination and annexation) for the rulers of Aryavarta (North India), but for the 12 kings of Dakshinapatha, he followed 'Grahana-Mokshanugraha' (capturing them, liberating them, and reinstating them on payment of tribute).",
         "Do not confuse the North Indian annexation policy with the South Indian suzerainty policy.",
         "North India = Annexation; South India = Capture, release, and tributary suzerainty."),

        ("anc_085", "gupta-period", "UPPSC Prelims 2021", True, 2021, "R.S. Sharma, Ch. 19; Upinder Singh, Ch. 8",
         "Which Gupta emperor assumed the title of 'Mahendraditya' and founded the famous Nalanda Mahavihara (University) in modern Bihar?",
         ["Chandragupta I", "Samudragupta", "Kumaragupta I", "Skandagupta"],
         2, "Kumaragupta I (c. 415-455 CE), who assumed the title Mahendraditya, founded Nalanda Mahavihara as confirmed by seals, inscriptions, and accounts of Chinese pilgrims Xuanzang and Yijing.",
         "Skandagupta was Vikramaditya who defeated the Hunas; Kumaragupta I was the founder of Nalanda.",
         "Kumaragupta I = Shakraditya / Mahendraditya = Founder of Nalanda Mahavihara."),

        ("anc_086", "post-gupta-period", "UPSC CSE 2021", True, 2021, "R.S. Sharma, Ch. 20; Upinder Singh, Ch. 9",
         "During the reign of Harshavardhana, which Chinese Buddhist pilgrim spent several years at Nalanda University studying Yogachara philosophy under Shilabhadra?",
         ["Fa-Hien (Faxian)", "Xuanzang (Hiuen Tsang)", "Yijing (I-Tsing)", "Song Yun"],
         1, "Xuanzang (Hiuen Tsang) visited India during Harsha's reign (629-645 CE) and studied at Nalanda for over five years under the venerable abbot Shilabhadra. He recorded his journey in 'Si-Yu-Ki'.",
         "Fa-Hien visited during Chandragupta II's reign; Xuanzang during Harsha; Yijing visited in the late 7th century.",
         "Chronology of Chinese pilgrims: Fa-Hien (5th c.) -> Xuanzang (7th c. Harsha) -> Yijing (late 7th c.)."),

        ("anc_087", "post-gupta-period", "UPPSC Prelims 2023", True, 2023, "Upinder Singh, Ch. 9; R.S. Sharma, Ch. 20",
         "The Aihole Inscription, composed by Ravikirti, celebrates the military triumph of which Chalukya monarch over Emperor Harshavardhana on the banks of the Narmada river?",
         ["Pulakeshin I", "Pulakeshin II", "Vikramaditya I", "Kirtivarman I"],
         1, "The Aihole prasasti (c. 634 CE) in Karnataka was composed in Sanskrit by the Jain poet Ravikirti. It describes how Chalukya king Pulakeshin II defeated Harshavardhana, whose 'harsha' (joy) melted away in fear on the Narmada.",
         "Ravikirti compared himself to Kalidasa and Bharavi at the end of the Aihole inscription.",
         "Aihole = Ravikirti + Pulakeshin II + Meguti temple + Defeat of Harsha on Narmada."),

        ("anc_088", "pallava-dynasty", "UPSC CSE 2022", True, 2022, "Upinder Singh, Ch. 9; Nitin Singhania, Ch. 1",
         "The monolithic rock-cut Rathas (Pancha Rathas) and the Shore Temple at Mamallapuram (Mahabalipuram) were patronized respectively by which Pallava rulers?",
         ["Narasimhavarman I (Mamalla) and Narasimhavarman II (Rajasimha)", "Mahendravarman I and Simhavishnu", "Nandivarman II and Aparajita", "Dantivarman and Paramesvaravarman I"],
         0, "The Pancha Rathas (Dharmaraja, Bhima, Arjuna, Draupadi, Nakula-Sahadeva) were carved out of living granite under Narasimhavarman I 'Mamalla' (mid-7th c.). The structural Shore Temple was built under Narasimhavarman II 'Rajasimha' (early 8th c.).",
         "Monolithic rathas = Rock-cut (Mamalla); Shore Temple = Structural stone masonry (Rajasimha).",
         "Mamalla = Monolithic Rathas. Rajasimha = Structural Kailasanatha (Kanchi) & Shore Temple."),

        ("anc_089", "early-medieval-period", "UPSC CSE 2018", True, 2018, "Satish Chandra, Ch. 1; Upinder Singh, Ch. 10",
         "The Tripartite Struggle for the supremacy over Kanauj in early medieval northern India was fought among which three major powers?",
         ["Palas, Pratiharas, and Rashtrakutas", "Cholas, Chalukyas, and Rashtrakutas", "Palas, Senas, and Gahadavalas", "Pratiharas, Paramaras, and Chandellas"],
         0, "The Tripartite Struggle (8th to 10th centuries CE) was a prolonged contest for the control of Kanauj (symbol of sovereignty in the fertile Gangetic basin) among the Gurjara-Pratiharas of Western India, the Palas of Bengal/Bihar, and the Rashtrakutas of the Deccan.",
         "Cholas were not part of the Tripartite struggle; they were expanding in the deep south.",
         "Tripartite = Gurjara-Pratihara (West) + Pala (East) + Rashtrakuta (South)."),

        ("anc_090", "early-medieval-period", "Standard Practice", False, 2024, "Satish Chandra, Ch. 2; Upinder Singh, Ch. 10",
         "The rock-cut monolithic Kailash Temple at Ellora (Cave 16), which was chiselled out of a single basalt cliff from top to bottom, was commissioned by which Rashtrakuta king?",
         ["Dantidurga", "Krishna I", "Amoghavarsha I", "Govinda III"],
         1, "The monumental monolithic Kailasha Temple (Cave 16) at Ellora was carved under the patronage of the Rashtrakuta king Krishna I (reigned c. 756-774 CE).",
         "Dantidurga was the founder who performed Hiranyagarbha; Krishna I built Kailash Temple.",
         "Cave 16 Ellora = Krishna I Rashtrakuta = Top-to-bottom monolithic mountain temple.")
    ]

    for item in more_ancient:
        qs.append({
            "id": item[0],
            "category": "ancient",
            "categoryLabel": "Ancient India",
            "periodId": item[1],
            "source": item[2],
            "isPyq": item[3],
            "year": item[4],
            "bookRef": item[5],
            "question": item[6],
            "options": item[7],
            "correctIndex": item[8],
            "explanation": item[9],
            "trap": item[10],
            "topperTip": item[11]
        })

    # Systematic coverage up to anc_130
    topics = [
        ("Indo-Greeks and Menander (Milinda-panha dialog with Nagasena)", "post-mauryan-period", "Upinder Singh, Ch. 7",
         "The Buddhist philosophical text 'Milindapanha' (Questions of King Menander) records a profound metaphysical debate between King Menander I and which Buddhist monk?",
         ["Nagasena", "Vasumitra", "Buddhaghosha", "Dharmakirti"], 0,
         "Milindapanha records the philosophical dialogues between Indo-Greek king Menander I (Milinda) and the Buddhist sage Nagasena, leading to Menander embracing Buddhism.",
         "Nagasena is the interlocutor; Nagarjuna was the Madhyamaka philosopher from a different period.",
         "Milinda + Nagasena = Milindapanha (Pali text)."),

        ("Kushana Empire Administration and Kanishka Era (78 CE)", "kushan-empire", "R.S. Sharma, Ch. 15",
         "The Shaka Era, which was adopted by the Government of India as the National Calendar in 1957, was initiated in 78 CE by which ruler?",
         ["Kanishka I", "Rudradaman I", "Chandragupta Vikramaditya", "Gautamiputra Satakarni"], 0,
         "The Shaka Era of 78 CE was founded by Kushan emperor Kanishka I upon his coronation, though later known as Shaka era due to prolonged usage by Western Kshatrapas.",
         "Vikram Era began in 57 BCE; Shaka Era began in 78 CE.",
         "National Calendar = Shaka Era (78 CE) starting on Chaitra 1."),

        ("Satavahana Inscriptions and Matronymics", "satavahana-dynasty", "Upinder Singh, Ch. 7",
         "The Satavahana rulers are notable in Indian epigraphy for using metronymics (mother's name). What does this practice signify according to historians?",
         ["The society was strictly matriarchal where property passed to daughters.", "Royal princes took their mother's gotra/lineage prefix, but succession to the throne was strictly patrilineal.", "Women were the supreme commanders of the armed forces.", "Religious sacrifices could only be performed by royal queens."], 1,
         "While Satavahana kings used metronymics (Gautamiputra, Vashishtiputra) indicating high honor for mothers, succession to the throne was strictly patrilineal from father to son.",
         "Metronymic names did NOT mean the society was matriarchal!",
         "High maternal respect in naming != Matriarchy. Succession was patrilineal."),

        ("Gupta Numismatics and Coin Types", "gupta-period", "R.S. Sharma, Ch. 19",
         "Samudragupta issued various distinct gold coin types commemorating his personal achievements and accomplishments. Which of the following coin types was issued by him?",
         ["Archer type, Battle-axe type, Tiger-slayer type, and Lyrist (Veena) type", "Horseman type and Lion-slayer type only", "Elephant-rider type and Buddha type only", "Ship-with-double-mast type only"], 0,
         "Samudragupta issued six distinct gold coin types: Archer, Standard (Dhvaja), Battle-axe, Tiger-slayer, Ashvamedha, and Lyrist (playing the Veena).",
         "Ship-with-double-mast was issued by Satavahana ruler Yajna Sri Satakarni.",
         "Lyrist coin proves Samudragupta's title 'Kaviraja' and passion for music."),

        ("Iron Pillar of Mehrauli and King Chandra", "gupta-period", "Upinder Singh, Ch. 8",
         "The rustless Iron Pillar located in the Qutb Complex at Mehrauli, Delhi, bears a Sanskrit inscription eulogizing King 'Chandra', generally identified by historians as:",
         ["Chandragupta Maurya", "Chandragupta I", "Chandragupta II (Vikramaditya)", "Harshavardhana"], 2,
         "The Mehrauli iron pillar inscription in Gupta Brahmi script celebrates King Chandra who conquered Vanga (Bengal) and crossed the seven mouths of the Indus to vanquish the Vahlikas, universally identified with Chandragupta II.",
         "It stands in the courtyard of Quwwat-ul-Islam mosque, brought from Udayagiri or Vishnupadagiri.",
         "Mehrauli Pillar = Chandragupta II + Metallurgical marvel (high phosphorus, pure wrought iron)."),

        ("Fa-Hien's observations on Gupta India", "gupta-period", "NCERT Themes Theme 2; Upinder Singh, Ch. 8",
         "What did the Chinese pilgrim Fa-Hien observe regarding the judicial and social system of India during the reign of Chandragupta II?",
         ["Capital punishment was frequent and executions were public.", "The administration was mild, capital punishment was unknown, and crimes were punished mainly with fines according to gravity.", "Slavery was the predominant form of agricultural labour.", "All meat consumption was legally banned under imperial decree."], 1,
         "Fa-Hien noted that the government was benevolent; travellers moved freely without passports; capital punishment was nonexistent; and repeat treason was punished merely by cutting off the right hand.",
         "Fa-Hien never mentioned Chandragupta II by name in his travelogue 'Fo-Kwo-Ki'!",
         "Fa-Hien observed peace, low taxes, vegetarianism in Madhyadesha, and mild punishments."),

        ("Harshavardhana's Literary Works", "post-gupta-period", "Upinder Singh, Ch. 9",
         "Emperor Harshavardhana was not only a patron of scholars but also an accomplished Sanskrit dramatist. Which three Sanskrit plays are attributed to him?",
         ["Ratnavali, Priyadarsika, and Nagananda", "Malavikagnimitram, Vikramorvasiyam, and Abhijnanashakuntalam", "Mudrarakshasa, Devichandraguptam, and Malatimadhava", "Kavyadarsha, Dashakumaracharita, and Kiratarjuniya"], 0,
         "Harsha composed three famous plays: Ratnavali, Priyadarsika (romantic comedies), and Nagananda (Buddhist story of Jimutavahana's self-sacrifice).",
         "Kalidasa wrote Shakuntalam; Harsha wrote Ratnavali, Priyadarshika, and Nagananda.",
         "Harsha's trio: Ratnavali, Priyadarsika, Nagananda."),

        ("Banabhatta and Kadambari", "post-gupta-period", "Upinder Singh, Ch. 9",
         "Banabhatta, the celebrated Asthana Kavi (court poet) of Harsha, authored which two foundational Sanskrit texts?",
         ["Harshacharita and Kadambari", "Rajatarangini and Kathasaritsagara", "Gita Govinda and Aryabhatiya", "Brihatkatha and Panchatantra"], 0,
         "Banabhatta wrote 'Harshacharita' (first historical biography in Sanskrit) and 'Kadambari' (one of the world's earliest novels).",
         "Kalhana wrote Rajatarangini; Jayadeva wrote Gita Govinda.",
         "Harshacharita = Historical kavya on Harsha; Kadambari = Complex Sanskrit romance."),

        ("Ancient Indian Guilds (Shrenis)", "ancient-republics", "R.S. Sharma, Ch. 18; Upinder Singh, Ch. 8",
         "Regarding the ancient Indian guilds (Shrenis) during the post-Mauryan and Gupta periods, which of the following statements is/are correct?\n1. Guilds acted as autonomous banking institutions receiving deposits and paying interest.\n2. Guilds had their own judicial courts and customary laws (Shrenidharma) recognized by the king.\n3. Guilds maintained their own private security militia (Shrenibala).",
         ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 3,
         "All three statements are correct. Guilds (Shrenis) functioned as banks taking permanent endowments (akshayanivi), operated internal tribunals whose customary rules kings had to respect, and maintained armed guards (shrenibala).",
         "Shrenis were not just economic cooperatives; they had corporate legal, judicial, and paramilitary authority.",
         "Shreni = Guild + Bank + Judiciary + Paramilitary militia."),

        ("Ancient Ports: Barygaza and Muziris in Periplus", "sangam-period", "Upinder Singh, Ch. 7",
         "The anonymous 1st century CE Greek navigational guide 'Periplus Maris Erythraei' mentions 'Barygaza'. What modern Indian port city corresponds to Barygaza?",
         ["Bharuch (Broach) in Gujarat", "Surat in Gujarat", "Tamralipti in West Bengal", "Calicut in Kerala"], 0,
         "Barygaza was the Greek name for Bharuch (ancient Bhrigukachchha) at the mouth of the Narmada River in Gujarat, the premier port for northern trade with the Roman world.",
         "Tamralipti was on the Bay of Bengal; Barygaza was on the Arabian Sea.",
         "Barygaza = Bharuch / Broach on the Narmada."),

        ("Tamralipti - The Great Eastern Sea Port", "ancient-republics", "R.S. Sharma, Ch. 19",
         "Tamralipti, located in the Ganges delta (modern Midnapore, West Bengal), served as the primary eastern seaport for trade with which regions in ancient times?",
         ["Sri Lanka, Southeast Asia (Suvarnabhumi), and China", "Roman Empire and Alexandria only", "East Africa and the Persian Gulf only", "Central Asian steppes"], 0,
         "Tamralipti (Tamluk) was the gateway for voyages to Suvarnadvipa/Suvarnabhumi (Java, Sumatra, Malaya), Sri Lanka, and Southern China, utilized by Fa-Hien and Xuanzang.",
         "Western ports traded with Rome/Alexandria; Tamralipti dominated Bay of Bengal & South-East Asia.",
         "Tamralipti = Eastern embarkation port for Southeast Asia & China."),

        ("Ancient Universities: Nalanda, Vikramashila, Vallabhi", "post-gupta-period", "Upinder Singh, Ch. 9; Satish Chandra, Ch. 1",
         "Consider the following ancient Indian universities and their patron dynasties:\n1. Nalanda : Guptas (Kumaragupta I)\n2. Vikramashila : Palas (Dharmapala)\n3. Vallabhi : Maitrakas of Saurashtra\n4. Odantapuri : Palas (Gopala)\nHow many of the pairs given above are correctly matched?",
         ["Only one pair", "Only two pairs", "Only three pairs", "All four pairs"], 3,
         "All four pairs are correctly matched. Kumaragupta I founded Nalanda; Dharmapala founded Vikramashila; the Maitraka dynasty of Saurashtra patronized Vallabhi; and Gopala I founded Odantapuri.",
         "Vallabhi in Gujarat was especially famous for Hinayana Buddhism and administrative sciences.",
         "Nalanda (Kumaragupta) -> Vikramashila (Dharmapala) -> Vallabhi (Maitrakas)."),

        ("Ancient Indian Astronomy: Aryabhata and Varahamihira", "gupta-period", "Upinder Singh, Ch. 8",
         "Regarding ancient Indian scientific treatises, consider the following matches:\n1. Aryabhatiya : Calculation of value of Pi, diurnal rotation of the Earth, causes of solar and lunar eclipses\n2. Panchasiddhantika : Five ancient astronomical systems (Surya, Romaka, Paulisa, Vasistha, Paitamaha)\n3. Sushruta Samhita : Rhinoplasty, surgical instruments, and cataract surgery\n4. Charaka Samhita : Internal medicine (Kayachikitsa) and plant pharmacology\nHow many of the above pairs are correctly matched?",
         ["Only two", "Only three", "All four", "Only one"], 2,
         "All four pairs are correctly matched. Aryabhata stated that the earth rotates on its axis and calculated Pi to 3.1416; Varahamihira synthesized the five astronomical systems in Panchasiddhantika; Sushruta is the father of Indian surgery (rhinoplasty); Charaka pioneered Ayurveda medicine.",
         "Sushruta = Surgery; Charaka = Internal medicine (Kaya-chikitsa).",
         "All 4 texts represent the golden age of classical Indian science."),

        ("Ashokan Inscriptions - Languages and Scripts", "mauryan-empire", "R.S. Sharma, Ch. 14",
         "Which combination of scripts and languages was used in the inscriptions of Ashoka across his vast empire?",
         ["Brahmi, Kharosthi, Aramaic, and Greek scripts; Prakrit, Greek, and Aramaic languages", "Only Sanskrit language written in Brahmi script", "Pali language written in Devanagari script", "Tamil language written in Vatteluttu script"], 0,
         "Ashoka's edicts utilized four scripts: Brahmi (pan-India), Kharosthi (north-west, e.g. Shahbazgarhi), Aramaic and Greek (Afghanistan, e.g. Kandahar bilingual edict). The dominant language was Prakrit, alongside Greek and Aramaic.",
         "Ashoka never used Sanskrit or Devanagari in his edicts!",
         "Scripts: Brahmi, Kharosthi, Greek, Aramaic. Language: Prakrit, Greek, Aramaic."),

        ("Rummin-dei Pillar Inscription and Taxation", "mauryan-empire", "R.S. Sharma, Ch. 14",
         "Which Ashokan pillar inscription records the historical visit of Emperor Ashoka to the birthplace of Gautama Buddha and the reduction of the land tax (Bhaga) to one-eighth?",
         ["Rummindei (Lumbini) Pillar Inscription", "Nigali Sagar Pillar Inscription", "Sarnath Pillar Inscription", "Rampurva Pillar Inscription"], 0,
         "The Rummindei (Lumbini, Nepal) Minor Pillar Inscription records that Ashoka visited the birthplace of Shakyamuni Buddha in his 20th regnal year, made the village tax-free of religious tribute (Bali) and reduced Bhaga to 1/8th (Atthabhagiya).",
         "Rummindei is the ONLY Ashokan inscription that explicitly discusses fiscal concessions and taxation rates.",
         "Lumbini / Rummindei = Birthplace of Buddha + Bhaga reduced to 1/8th."),

        ("Sangam Literature - Ettuthokai and Pattupattu", "sangam-period", "Upinder Singh, Ch. 7",
         "In Sangam Tamil literature, the corpus is broadly divided into 'Agam' (inner/love) and 'Puram' (outer/heroic war). Which of the following collections belongs to the Eight Anthologies (Ettuthokai)?",
         ["Ahananuru, Purananuru, Kuruntokai, Natrinai, and Padirruppattu", "Silappadikaram, Manimekalai, and Civaka Chintamani", "Tolkappiyam and Tirukkural", "Periyapuranam and Kamba Ramayanam"], 0,
         "Ettuthokai consists of eight poetic anthologies including Natrinai, Kuruntokai, Ainkurunuru, Padirruppattu, Paripadal, Kalittokai, Ahananuru, and Purananuru.",
         "Silappadikaram and Manimekalai are the twin epics, not part of the Ettuthokai anthologies.",
         "Ettuthokai = 8 Anthologies. Pattupattu = 10 Idylls. Pathinenkilkanakku = 18 Didactic works (including Tirukkural)."),

        ("Pallava-Chalukya Conflict", "pallava-dynasty", "Upinder Singh, Ch. 9",
         "The rivalry between the Pallavas of Kanchipuram and the Chalukyas of Badami centered primarily around the control of which fertile river doab?",
         ["Raichur Doab (Krishna-Tungabhadra)", "Ganga-Yamuna Doab", "Kaveri Delta", "Narmada-Tapti valley"], 0,
         "The protracted military struggle between the Badami Chalukyas and Pallavas (and later Rashtrakutas and Cholas) was fought over the fertile Krishna-Tungabhadra Doab (Raichur Doab) and Vengi.",
         "This same geographic corridor witnessed the Vijayanagara-Bahmani conflict centuries later!",
         "Raichur Doab between Krishna and Tungabhadra was South India's perpetual cock-pit of warfare."),

        ("Chola Maritime Expeditions - Rajaraja I and Rajendra I", "imperial-cholas", "Satish Chandra, Ch. 2; Upinder Singh, Ch. 10",
         "Which Chola monarch led a naval expedition across the Bay of Bengal, conquered the Srivijaya Empire (Sumatra/Malaya), and assumed the title 'Kadaramkonda'?",
         ["Rajendra I", "Rajaraja I", "Kulottunga I", "Parantaka I"], 0,
         "Rajendra I (reigned 1014-1044 CE) launched a massive naval campaign in 1025 CE against Sangrama Vijayottungavarman of the Srivijaya Empire to secure maritime trade routes with Song China, earning the title 'Kadaramkonda' (conqueror of Kedah).",
         "Rajaraja I conquered Sri Lanka's northern half; Rajendra I completed the conquest of all of Sri Lanka and invaded Srivijaya.",
         "Rajendra I = Gangaikondachola + Kadaramkonda + Bay of Bengal as 'Chola Lake'."),

        ("Uttaramerur Inscription and Kudavolai System", "imperial-cholas", "Satish Chandra, Ch. 2; Upinder Singh, Ch. 10",
         "The famous 10th-century Uttaramerur Inscriptions of Parantaka I Chola provide unparalleled constitutional details about:",
         ["The military organization of the naval fleet", "The qualifications, disqualifications, and lottery system (Kudavolai) for selecting members of village executive committees (Variyams)", "The assessment of maritime customs duties", "The conversion of Shaiva temples into Vaishnava shrines"], 1,
         "The two inscriptions at the Vaikunta Perumal temple at Uttaramerur (919 and 921 CE) detail the functioning of the Brahmanical Sabha, committee structure (Eri-variyam, Thotta-variyam, Pon-variyam), qualifications (age 35-70, Vedic knowledge, property), and selection by lottery (Kudavolai).",
         "Uttaramerur is the cornerstone of democratic local self-government in ancient India.",
         "Uttaramerur = Parantaka I + Kudavolai (Pot-ticket lottery) + Variyams (Committees)."),

        ("Vakataka Dynasty and Ajanta Caves", "gupta-period", "Upinder Singh, Ch. 8; Nitin Singhania, Ch. 1",
         "The majority of the magnificent Mahayana rock-cut caves and fresco paintings at Ajanta (Caves 1, 2, 16, 17, 19, 26) were excavated under the patronage of which dynasty?",
         ["Vakatakas of the Vatsagulma branch (under King Harishena and his minister Varahadeva)", "Guptas directly", "Early Rashtrakutas", "Satavahanas exclusively"], 0,
         "The second and most spectacular phase of Ajanta (the Mahayana phase) was patronized by the Vakatakas of the Vatsagulma branch, particularly King Harishena (c. 460-477 CE) and his minister Varahadeva.",
         "Satavahanas patronized the early Hinayana caves (9, 10); Vakatakas patronized the late classical paintings.",
         "Ajanta late phase = Vakatakas (Harishena)."),

        ("Megasthenes on Indian Castes", "mauryan-empire", "R.S. Sharma, Ch. 14; Upinder Singh, Ch. 6",
         "Megasthenes, in his 'Indica', divided Indian society into how many distinct classes/castes?",
         ["Four (Brahmana, Kshatriya, Vaishya, Shudra)", "Seven classes (Philosophers, Farmers, Herdsmen/Hunters, Artisans/Traders, Soldiers, Overseers/Spies, Councillors/Assessors)", "Five classes (including Untouchables)", "Ten classes based on occupational guilds"], 1,
         "Megasthenes divided Indian society into 7 classes based on their social and professional functions rather than the theoretical fourfold Varna system.",
         "Do not select 4 varnas! Megasthenes specifically observed 7 functional classes.",
         "Megasthenes = 7 Castes/Classes in Indica."),

        ("Buddhism: Hinayana vs Mahayana vs Vajrayana", "ancient-republics", "NCERT Themes Theme 4; Nitin Singhania, Ch. 13",
         "Consider the following characteristics of Buddhist sects:\n1. Hinayana (Theravada) : Emphasizes individual salvation through self-discipline and meditation; considers Buddha an enlightened human teacher.\n2. Mahayana : Emphasizes universal salvation through the grace of Bodhisattvas; worships Buddha as a divine saviour.\n3. Vajrayana : Emphasizes esoteric mantras, mudras, mandalas, and mystical tantric rituals to achieve Buddhahood rapidly.\nWhich of the statements given above are correct?",
         ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 3,
         "All three statements are correct. Hinayana represents the pristine orthodox tradition relying on the Pali canon. Mahayana developed the Bodhisattva ideal and image worship. Vajrayana (Thunderbolt vehicle) developed from the 5th-8th century CE centered in Bengal/Bihar (Vikramashila).",
         "Vajrayana is Tantric Buddhism, heavily patronized by the Pala rulers.",
         "Hinayana (Arhat) -> Mahayana (Bodhisattva) -> Vajrayana (Siddha/Tantra)."),

        ("Jain Tirthankaras and their Symbols", "ancient-republics", "Nitin Singhania, Ch. 13; Upinder Singh, Ch. 6",
         "Consider the following pairs of Jain Tirthankaras and their traditional cognizance symbols:\n1. Rishabhanatha (Adinatha) : Bull\n2. Parshvanatha : Serpent / Hooded Snake\n3. Mahavira : Lion\n4. Neminatha : Conch shell (Shankha)\nHow many of the pairs given above are correctly matched?",
         ["Only two", "Only three", "All four", "Only one"], 2,
         "All four pairs are correctly matched. 1st Tirthankara Rishabhanatha = Bull; 23rd Tirthankara Parshvanatha = Snake; 24th Tirthankara Mahavira = Lion; 22nd Tirthankara Neminatha = Conch.",
         "Parshvanatha was born in Varanasi (Kashi) 250 years before Mahavira.",
         "Rishabha = Bull; Parshva = Serpent; Mahavira = Lion."),

        ("Jain Councils - Pataliputra and Vallabhi", "ancient-republics", "Upinder Singh, Ch. 6",
         "The Second Jain Council, which codified the Svetambara canonical texts (the 12 Angas and Upangas) into written form, was held at Vallabhi in 512 CE under the chairmanship of:",
         ["Sthulabhadra", "Devardhi Kshamasramana", "Bhadrabahu", "Hemachandra"], 1,
         "The First Jain Council was held at Pataliputra under Sthulabhadra (c. 300 BCE). The Second Jain Council was held at Vallabhi in Gujarat under Devardhi Kshamasramana in the 5th/6th century CE, where the canons were definitively written down.",
         "Sthulabhadra led the 1st council; Devardhi Kshamasramana led the 2nd council.",
         "1st Council = Pataliputra (Sthulabhadra). 2nd Council = Vallabhi (Devardhi)."),

        ("Ancient Indian Inscriptions - Pillar Edicts of Ashoka", "mauryan-empire", "R.S. Sharma, Ch. 14",
         "Which Ashokan Major Pillar Edict explicitly forbids animal sacrifices on specific sacred calendar days and bans castration of animals and brandings of horses?",
         ["Pillar Edict V", "Pillar Edict II", "Pillar Edict VII", "Major Rock Edict I"], 0,
         "Major Pillar Edict V (often termed the Game Law or Delhi-Topra edict) provides an elaborate list of animals and birds that must not be killed, strictly banning animal slaughter on designated festive days.",
         "Major Rock Edict I bans animal sacrifice at the royal kitchen; Pillar Edict V provides the full ecological wildlife protection law.",
         "Pillar Edict V = Comprehensive Ashokan wildlife protection and forest preservation edict."),

        ("Mauryan Espionage System - Gudhapurushas", "mauryan-empire", "Upinder Singh, Ch. 6",
         "In Kautilya's Arthashastra, the intelligence and secret service apparatus is staffed by 'Gudhapurushas' divided into which two primary branches?",
         ["Sanstha (stationary spies stationed at headquarters) and Sanchara (wandering roving agents)", "Yuktas and Rajukas", "Mahamatras and Anta-mahamatras", "Pradeshtris and Sthanikas"], 0,
         "Kautilya details two intelligence divisions: 'Sanstha' (stationary spies disguised as hermits, students, fraudulent ascetics, householders) and 'Sanchara' (mobile roving spies such as mendicants, poisoners, bravos).",
         "Yuktas and Rajukas were revenue and judicial officials, not secret spies.",
         "Gudhapurushas = Sanstha (Stationary) + Sanchara (Roving)."),

        ("Harappan Bead-Making and Craft Specialization", "indus-valley-civilization", "NCERT Themes Theme 1; R.S. Sharma, Ch. 5",
         "Chanhudaro was an exclusive Harappan industrial settlement almost entirely devoted to craft production. Which craft operations were carried out there?",
         ["Bead-making, shell-cutting, seal-making, and metalworking", "Gold mining and iron smelting", "Monumental stone temple construction", "Silk weaving and paper making"], 0,
         "Excavations by N.G. Majumdar and Ernest Mackay at Chanhudaro (Sindh) proved it was a specialized manufacturing hub with bead factories, drill tools, shell bangles, and steatite seals.",
         "Iron and paper were completely unknown to Harappans!",
         "Chanhudaro & Lothal = Specialized bead factories with carnelian heating kilns."),

        ("Ashoka's Dhamma Mahamatras", "mauryan-empire", "R.S. Sharma, Ch. 14",
         "In which regnal year did Emperor Ashoka create the brand-new cadre of administrative officers known as 'Dhamma Mahamatras', as recorded in Major Rock Edict V?",
         ["14th regnal year", "8th regnal year", "20th regnal year", "26th regnal year"], 0,
         "In Major Rock Edict V, Ashoka announces: 'In the past, there were no Dhamma Mahamatras. They were appointed by me for the first time in the fourteenth year of my coronation.'",
         "Kalinga war was in the 8th year (9th regnal); Dhamma Mahamatras were created in the 14th year.",
         "14th Regnal Year = Creation of Dhamma Mahamatras to propagate ethical conduct."),

        ("Post-Mauryan Coinage - Lead and Potin", "satavahana-dynasty", "R.S. Sharma, Ch. 16",
         "Which ancient Indian dynasty is particularly renowned for issuing a massive volume of coins made of lead and potin (an alloy of copper, lead, and tin)?",
         ["Satavahanas", "Guptas", "Kushans", "Mauryas"], 0,
         "The Satavahanas in the Deccan issued coins primarily in lead, potin, copper, and bronze, with occasional silver portrait issues for kings like Gautamiputra and Vashishtiputra.",
         "Guptas are famous for gold dinaras; Satavahanas are uniquely famous for lead and potin currency.",
         "Satavahanas = Lead, potin, and ship-motif maritime coins."),

        ("Ajivika Sect and Makkhali Gosala", "heterodox-sects", "Upinder Singh, Ch. 6; R.S. Sharma, Ch. 12",
         "The Ajivika school of thought, founded by Makkhali Gosala, was anchored upon which philosophical doctrine?",
         ["Niyati (absolute fatalism or determinism), asserting that human effort (purushakara) cannot alter destiny", "Syadvada (relativity of knowledge)", "Karmavada (freedom of action shaping rebirth)", "Shunyavada (emptiness of inherent existence)"], 0,
         "Makkhali Gosala's Ajivikas propounded the doctrine of 'Niyati' (destiny), holding that all cosmic phenomena and individual destinies are rigidly predetermined by fate, rendering karma and moral effort powerless.",
         "Ajivikas were strict determinists; Jainism and Buddhism championed moral human agency.",
         "Ajivika = Makkhali Gosala + Niyati (Strict Determinism)."),

        ("Vedic River Names and Modern Equivalents", "vedic-age", "R.S. Sharma, Ch. 10",
         "Consider the following Rigvedic rivers and their modern equivalents:\n1. Askini : Chenab\n2. Parushni : Ravi\n3. Vitasta : Jhelum\n4. Vipas : Beas\n5. Shutudri : Sutlej\nHow many of the pairs given above are correctly matched?",
         ["Only two pairs", "Only three pairs", "Only four pairs", "All five pairs"], 3,
         "All five pairs are correctly matched according to the Nadistuti Sukta of Rigveda Mandala X. Askini = Chenab; Parushni = Ravi (battle of 10 kings); Vitasta = Jhelum; Vipas = Beas; Shutudri = Sutlej.",
         "The Battle of Ten Kings (Dasharajna) took place on the banks of Parushni (Ravi).",
         "All 5 Punjab rivers have precise Vedic correspondences in Rigveda."),

        ("Gupta Golden Age Debate - Urban Decay", "gupta-period", "R.S. Sharma (Urban Decay in India); Upinder Singh, Ch. 8",
         "According to Marxist historian R.S. Sharma, what significant socio-economic transition occurred during the late Gupta and post-Gupta periods?",
         ["Widespread urban decay, decline of long-distance trade, demonetisation, and the emergence of Indian feudalism based on land grants", "Unprecedented industrialization and establishment of factory monopolies", "Total abolition of caste hierarchy and agrarian slavery", "Expansion of Roman gold inflows to peak levels"], 0,
         "R.S. Sharma argued that the post-Gupta era witnessed 'urban decay' (abandonment of urban centers), shrinkage of trade, scarcity of coins, and rise of feudalism through tax-free agrahara land grants with administrative rights.",
         "Upinder Singh and B.D. Chattopadhyaya present an alternative view emphasizing agrarian expansion and local exchange networks.",
         "R.S. Sharma thesis: Land grants -> Serfdom & Decentered polity -> Indian Feudalism.")
    ]

    for idx, item in enumerate(topics):
        q_id = f"anc_{91 + idx:03d}"
        qs.append({
            "id": q_id,
            "category": "ancient",
            "categoryLabel": "Ancient India",
            "periodId": item[1],
            "source": "UPSC / Standard Pattern",
            "isPyq": False,
            "year": 2024,
            "bookRef": item[2],
            "question": item[3],
            "options": item[4],
            "correctIndex": item[5],
            "explanation": item[6],
            "trap": item[7],
            "topperTip": item[8]
        })

    # Additional systematic questions to reach anc_130
    additional_anc = [
        ("Chalukya Architecture - Aihole, Badami, Pattadakal", "chalukyas-of-badami", "Nitin Singhania, Ch. 1; Upinder Singh, Ch. 9",
         "Pattadakal in Karnataka, a UNESCO World Heritage site, represents the harmonious synthesis of which architectural styles under the Badami Chalukyas?",
         ["Nagara (North Indian) and Dravida (South Indian) architectural styles", "Greco-Roman and Indian styles exclusively", "Islamic true arch and Hindu trabeate styles", "Kalinga and Gandhara styles"], 0,
         "Pattadakal features temples built side by side in both northern Nagara style (Papanatha, Kadasiddheshwara) and southern Dravida style (Virupaksha, Sangameshwara) patronized by Queens Lokamahadevi and Trailokyamahadevi.",
         "Aihole is called the 'cradle of temple architecture', while Pattadakal represents the culminating confluence.",
         "Pattadakal = Vesara confluence: Virupaksha (Dravida) + Papanatha (Nagara)."),

        ("Indus Valley - Fire Altars and Ritual Bathing", "indus-valley-civilization", "R.S. Sharma, Ch. 5; NCERT Themes Theme 1",
         "Brick-lined ritual 'fire altars' (vedis) containing ash, charcoal, and animal bones have been unearthed at which Indus Valley sites?",
         ["Kalibangan and Lothal", "Mohenjo-daro and Harappa", "Dholavira and Suktagendor", "Kot Diji and Amri"], 0,
         "Kalibangan (Rajasthan) and Lothal (Gujarat) yielded rows of clay-plastered fire altars with central clay stele, indicating sacrificial rituals involving fire.",
         "Mohenjo-daro is famous for the Great Bath; fire altars are absent in the citadel of Mohenjo-daro!",
         "Fire Altars = Kalibangan & Lothal. Great Bath = Mohenjo-daro."),

        ("Ancient Indian Inscriptions - Sohgaura and Mahasthangarh", "mauryan-empire", "Upinder Singh, Ch. 6; R.S. Sharma, Ch. 14",
         "The Sohgaura copper plate (Gorakhpur, UP) and Mahasthangarh stone inscription (Bogra, Bangladesh) are crucial historical documents because they record:",
         ["Famine relief measures and the construction of state granaries to store grain during emergencies.", "The declaration of war against the Yavanas.", "The dedication of caves to Ajivika ascetics.", "The first recorded solar eclipse in Indian epigraphy."], 0,
         "Both the Sohgaura copper plate and Mahasthangarh inscription date to the Mauryan era (Prakrit in Brahmi) and instruct district officials (Mahamatras) to maintain twin granaries (Koshthagara) to provide relief to drought-stricken people.",
         "These are the earliest administrative famine relief epigraphs in Indian history.",
         "Sohgaura (UP) & Mahasthangarh (Bengal) = Mauryan State Granaries & Famine Management."),

        ("Buddhism: Four Noble Truths and Eightfold Path", "ancient-republics", "NCERT Themes Theme 4; Nitin Singhania, Ch. 13",
         "In Buddhism, the concept of 'Pratityasamutpada' (Dependent Origination) signifies that:",
         ["Nothing exists in isolation; every phenomenon arises in dependence upon conditions and ceases when those conditions cease.", "The soul is permanent, immutable, and eternal.", "Worldly misery can only be expiated through self-mortification.", "The universe was created out of nothingness by Brahma."], 0,
         "Pratityasamutpada (if this exists, that comes to be; from the cessation of this, that ceases) is the core philosophical pillar of the Buddha's Four Noble Truths, explaining the 12-linked chain of dependent causation (Dvadasa Nidana).",
         "Buddhism denies both eternalism (Sassatavada) and annihilationism (Ucchedavada), preaching the Middle Path.",
         "Pratityasamutpada = Dependent Origination = Cause-and-effect law of reality."),

        ("Sangam Polity - Chera, Chola, Pandya Emblems", "sangam-period", "Upinder Singh, Ch. 7",
         "Match the ancient Tamil dynasties of the Sangam Age with their royal dynastic emblems:\n1. Cheras : Bow and Arrow\n2. Cholas : Tiger\n3. Pandyas : Twin Fish (Carp)\nWhich of the combinations given above is/are correct?",
         ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 3,
         "All three combinations are correct. The Cheras ruled Kerala and western Tamil Nadu with the Bow emblem; the Cholas held the Kaveri basin with the Tiger emblem; the Pandyas held Madurai with the Fish emblem.",
         "Sangam Mu-vendan: Chera (Bow), Chola (Tiger), Pandya (Fish).",
         "Chera = Bow; Chola = Tiger; Pandya = Fish."),

        ("Samkhya Philosophy - Purusha and Prakriti", "ancient-republics", "Nitin Singhania, Ch. 13",
         "The classical Samkhya philosophy founded by Sage Kapila is fundamentally:",
         ["Dualistic, positing two ultimate, uncreated eternal realities: Purusha (pure consciousness) and Prakriti (matter/nature)", "Monistic, asserting that the phenomenal world is Maya (illusion)", "Strictly theistic, declaring God as the efficient cause of creation", "Materialistic, rejecting rebirth and karma"], 0,
         "Samkhya is dualistic realism. It posits Purusha (passive conscious witness) and Prakriti (dynamic primal nature made of three gunas: Sattva, Rajas, Tamas). Creation begins when Purusha comes into contact with Prakriti.",
         "Original Samkhya was non-theistic (Nirishvara Samkhya); Patanjali's Yoga added Ishvara.",
         "Samkhya = Dualism of Purusha (Consciousness) + Prakriti (Matter)."),

        ("Nyaya and Vaisheshika Schools", "ancient-republics", "Nitin Singhania, Ch. 13",
         "Regarding the Shad-Darshanas (Six Orthodox Schools), consider the following pairs:\n1. Nyaya : Sage Gautama (Logic, epistemology, and syllogistic reasoning)\n2. Vaisheshika : Sage Kanada (Atomic theory of matter and categories/Padarthas)\n3. Mimamsa (Purva) : Sage Jaimini (Vedic rituals and hermeneutics)\n4. Vedanta (Uttara) : Sage Badarayana (Brahma Sutras and Upanishadic wisdom)\nHow many of the above pairs are correctly matched?",
         ["Only two", "Only three", "All four", "Only one"], 2,
         "All four pairs are correctly matched. Nyaya = Gautama (4 pramanas); Vaisheshika = Kanada (Paramanu atomic doctrine); Purva Mimamsa = Jaimini (Dharma as Vedic injunction); Uttara Mimamsa = Badarayana (Brahman).",
         "Nyaya and Vaisheshika are complementary sister schools of logic and physics.",
         "Gautama (Nyaya), Kanada (Vaisheshika), Jaimini (Mimamsa), Badarayana (Vedanta)."),

        ("Ancient Indian Medicine - Ashtanga Hridaya", "gupta-period", "Upinder Singh, Ch. 8",
         "The classical Ayurvedic medical treatise 'Ashtanga Hridaya' and 'Ashtanga Samgraha' were composed by which master physician in the 7th century CE?",
         ["Vagbhata", "Charaka", "Sushruta", "Dhanvantari"], 0,
         "Vagbhata (c. 7th century CE) synthesized the earlier works of Charaka and Sushruta into two authoritative verse medical compendiums: Ashtanga Samgraha and Ashtanga Hridaya.",
         "Charaka lived around 1st-2nd c. CE; Sushruta was earlier; Vagbhata brought Ayurveda into concise poetic verse.",
         "The Great Trio of Ayurveda (Brihat Trayi): Charaka, Sushruta, and Vagbhata.")
    ]

    for idx, item in enumerate(additional_anc):
        q_id = f"anc_{123 + idx:03d}"
        qs.append({
            "id": q_id,
            "category": "ancient",
            "categoryLabel": "Ancient India",
            "periodId": item[1],
            "source": "Standard Practice",
            "isPyq": False,
            "year": 2024,
            "bookRef": item[2],
            "question": item[3],
            "options": item[4],
            "correctIndex": item[5],
            "explanation": item[6],
            "trap": item[7],
            "topperTip": item[8]
        })

    return qs

if __name__ == '__main__':
    res = get_ancient_questions()
    print(f"Generated {len(res)} ancient questions (anc_056 to {res[-1]['id']})")
    with open('data/batch_ancient.json', 'w', encoding='utf8') as f:
        json.dump(res, f, indent=2, ensure_ascii=False)
