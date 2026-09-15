# scripts/batch_ancient.py
import json

questions = [
    # Mauryan Empire (anc_056 - anc_075)
    {
        "id": "anc_056",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2020",
        "isPyq": true,
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
    },
    {
        "id": "anc_057",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2019",
        "isPyq": true,
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
        "explanation": "At Kanganahalli near Sannati in Kalaburagi (Gulbarga) district, Karnataka, excavations revealed a limestone relief depicting King Ashoka with his queens, inscribed with the label 'Ranyo Ashoka' in Brahmi script.",
        "trap": "Sanchi has grand stupas, but the labeled portrait sculpture was unearthed at Kanganahalli.",
        "topperTip": "Kanganahalli on the Bhima river is the only site with an identified labeled portrait of Ashoka.",
        "periodId": "mauryan-empire"
    },
    {
        "id": "anc_058",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2016",
        "isPyq": true,
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
    },
    {
        "id": "anc_059",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2022",
        "isPyq": true,
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
    },
    {
        "id": "anc_060",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "Standard Practice",
        "isPyq": false,
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
        "explanation": "Major Rock Edict XIII, which recounts the remorse of the Kalinga War, explicitly records that Ashoka achieved 'Dhamma Vijaya' (conquest through righteousness) across frontiers ruled by five Hellenistic kings: Amtiyoka (Antiochus), Tulamaya (Ptolemy), Antekina (Antigonus), Maka (Magas), and Alikasudara (Alexander).",
        "trap": "MRE II mentions sending medical treatment (chikitsha) and herbs to Greek territories, but MRE XIII provides the complete diplomatic list for Dhamma Vijaya.",
        "topperTip": "MRE XIII = Kalinga remorse + 5 Hellenistic contemporary kings.",
        "periodId": "mauryan-empire"
    },
    {
        "id": "anc_061",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPPSC Prelims 2021",
        "isPyq": true,
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
    },
    {
        "id": "anc_062",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2023",
        "isPyq": true,
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
    },
    {
        "id": "anc_063",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "Standard Practice",
        "isPyq": false,
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
        "explanation": "Statements 1 and 2 are correct. Megasthenes states that Pataliputra was run by 30 commissioners in 6 boards of 5 each. Statement 3 is incorrect because Megasthenes explicitly notes that the military was ALSO administered by a board of 30 members divided into 6 committees (navy, transport/commissariat, infantry, cavalry, war chariots, and war elephants).",
        "trap": "Both City (Astynomoi) and Military (Navarchs/Military board) had identical 6x5=30 member board structures!",
        "topperTip": "6 boards of 5 members each governed both the capital city and the armed forces.",
        "periodId": "mauryan-empire"
    },
    {
        "id": "anc_064",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2022",
        "isPyq": true,
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
    },
    {
        "id": "anc_065",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "Standard Practice",
        "isPyq": false,
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
    },
    # Post-Mauryan & Sangam Age (anc_066 - anc_085)
    {
        "id": "anc_066",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2020",
        "isPyq": true,
        "year": 2020,
        "bookRef": "R.S. Sharma, Ch. 16; Upinder Singh, Ch. 7",
        "question": "With reference to the period of the Gupta and post-Gupta dynasties in India, the term 'Araghatta' referred to:",
        "options": [
            "Bonded labour",
            "Land grants made to military officers",
            "Waterwheel used in the irrigation of land",
            "Wasteland converted to cultivated land"
        ],
        "correctIndex": 2,
        "explanation": "Araghatta (from 'ara' meaning spoke and 'ghatta' meaning pot) refers to the mechanical Persian-style waterwheel with pots attached to the rim used for lifting water from wells for irrigation.",
        "trap": "Do not confuse with 'Vishti' (bonded/forced labour) or 'Agrahara' (brahmanical land grants).",
        "topperTip": "Araghatta = Ara (spoke) + Ghatta (pot) = Waterwheel for irrigation.",
        "periodId": "gupta-period"
    },
    {
        "id": "anc_067",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2022",
        "isPyq": true,
        "year": 2022,
        "bookRef": "Upinder Singh, Ch. 7; Nitin Singhania, Ch. 13",
        "question": "Which of the following Sangam texts describes the tragic love story of Kovalan and Kannagi, culminating in the burning of Madurai after the Pandyan king wrongly executes Kovalan?",
        "options": [
            "Silappadikaram",
            "Manimekalai",
            "Tolkappiyam",
            "Purananuru"
        ],
        "correctIndex": 0,
        "explanation": "Silappadikaram ('The Jewelled Anklet'), composed by Ilango Adigal (a Jain prince), narrates the story of Kovalan, his wife Kannagi, and the courtesan Madhavi. Kannagi seeks justice from Neduncheliyan (Pandyan king) and curses Madurai to burn.",
        "trap": "Manimekalai is the Buddhist sequel to Silappadikaram written by Sittalai Sattanar, chronicling the life of Kovalan and Madhavi's daughter.",
        "topperTip": "Silappadikaram = Ilango Adigal (Anklet, Kannagi). Manimekalai = Sattanar (Daughter, Buddhist).",
        "periodId": "sangam-period"
    },
    {
        "id": "anc_068",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2023",
        "isPyq": true,
        "year": 2023,
        "bookRef": "Upinder Singh, Ch. 7; NCERT Themes Theme 2",
        "question": "In the context of ancient South Indian history, consider the following terms:\n1. Ur : General village assembly of tax-paying peasants\n2. Sabha : Assembly of learned Brahman landholders in Brahmadeya villages\n3. Nagaram : Assembly of merchants and traders in urban trading centers\nHow many of the pairs given above are correctly matched?",
        "options": [
            "Only one pair",
            "Only two pairs",
            "All three pairs",
            "None of the pairs"
        ],
        "correctIndex": 2,
        "explanation": "All three pairs are correctly matched. In ancient and early medieval Tamil country (Sangam through Chola period), the Ur was the ordinary non-Brahman village assembly, the Sabha (or Mahasabha) was the assembly of Brahman proprietors in Brahmadeyas, and the Nagaram was the autonomous mercantile assembly in trading towns.",
        "trap": "Sabha was strictly Brahmadeya (brahmin agrahara); Ur was general peasant village (vellala).",
        "topperTip": "Ur = Common village. Sabha = Brahman agrahara. Nagaram = Merchants.",
        "periodId": "sangam-period"
    },
    {
        "id": "anc_069",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2017",
        "isPyq": true,
        "year": 2017,
        "bookRef": "R.S. Sharma, Ch. 15; Upinder Singh, Ch. 7",
        "question": "Which of the following dynasties issued the largest hoard of gold coins (dinaras) with high degree of purity and introduced the image of Buddha on coins for the first time?",
        "options": [
            "Kushans",
            "Guptas",
            "Indo-Greeks",
            "Satavahanas"
        ],
        "correctIndex": 0,
        "explanation": "The Kushans (especially Kanishka I and Huvishka) issued gold coins of remarkable purity modeled on Roman denarii. Kanishka's coins feature the earliest verified numismatic representation of the standing and seated Buddha with Greek legends 'BODDO' and 'SAKAMANO BODDO'.",
        "trap": "Indo-Greeks were the first to issue gold coins in India with portraits/legends, but Kushans issued the purest gold coins and introduced Buddha on coins. Guptas issued the largest total number of gold coins, but their gold purity declined in the later phase.",
        "topperTip": "First gold coins = Indo-Greeks. Purest gold coins + Buddha on coins = Kushans. Largest number of gold coins = Guptas.",
        "periodId": "kushan-empire"
    },
    {
        "id": "anc_070",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPPSC Prelims 2022",
        "isPyq": true,
        "year": 2022,
        "bookRef": "R.S. Sharma, Ch. 15; Upinder Singh, Ch. 7",
        "question": "The Junagadh Rock Inscription of Rudradaman I (c. 150 CE) is significant in Indian history because:",
        "options": [
            "It is the first long, chaste Sanskrit inscription in ornate kavya style in India.",
            "It records the victory of the Satavahanas over the Western Kshatrapas.",
            "It contains the earliest known mention of the Bhakti movement.",
            "It marks the official adoption of Jainism by the Shaka rulers."
        ],
        "correctIndex": 0,
        "explanation": "The Junagadh rock inscription of Shaka Mahakshatrapa Rudradaman I is the earliest long inscription written in classical, ornate chaste Sanskrit prose (Kavya style). It records the repairing of the Sudarshana Lake dam originally constructed by Pushyagupta under Chandragupta Maurya and canalized by Tushaspha under Ashoka.",
        "trap": "Remember: Ashoka's edicts were in Prakrit. Rudradaman was a Saka (foreigner) who championed classical Sanskrit in royal inscriptions!",
        "topperTip": "Junagadh = Rudradaman (150 CE) + Chaste Sanskrit + Sudarshana Lake repair.",
        "periodId": "post-mauryan-period"
    },
    {
        "id": "anc_071",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2021",
        "isPyq": true,
        "year": 2021,
        "bookRef": "Upinder Singh, Ch. 7; R.S. Sharma, Ch. 15",
        "question": "With reference to the history of ancient India, Bhavabhuti, Hastimalla, and Kshemeshvara were famous:",
        "options": [
            "Jain monks",
            "Playwrights / Dramatists",
            "Temple architects",
            "Philosophers of the Charvaka school"
        ],
        "correctIndex": 1,
        "explanation": "Bhavabhuti (author of Malatimadhava, Mahaviracharita, Uttararamacharita), Hastimalla (Jain playwright author of Vikrantakaurava and Subhadraharana), and Kshemeshvara (author of Chandakaushika and Naishadhananda) were celebrated ancient and early medieval Sanskrit dramatists/playwrights.",
        "trap": "Hastimalla was indeed a Jain by faith, but in this triad, their common profession was Sanskrit playwrights/dramatists.",
        "topperTip": "Bhavabhuti is universally renowned as the greatest master of Sanskrit drama after Kalidasa.",
        "periodId": "post-gupta-period"
    },
    {
        "id": "anc_072",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "Standard Practice",
        "isPyq": false,
        "year": 2024,
        "bookRef": "R.S. Sharma, Ch. 16; Upinder Singh, Ch. 8",
        "question": "Which Satavahana ruler is praised in the Nasik Prasasti of his mother Gautami Balashri as 'Eka-Brahmana' (peerless Brahmana) and 'Khatiya-dapa-mana-madana' (destroyer of the pride and conceit of Kshatriyas)?",
        "options": [
            "Simuka",
            "Satakarni I",
            "Gautamiputra Satakarni",
            "Yajna Sri Satakarni"
        ],
        "correctIndex": 2,
        "explanation": "The Nasik cave inscription of Gautami Balashri eulogizes Gautamiputra Satakarni (c. 106-130 CE) as 'Eka-Brahmana' and destroyer of the Kshatriyas, as well as the vanquisher of Shakas, Yavanas, and Pahlavas (destroying the Kshaharata king Nahapana).",
        "trap": "Gautamiputra Satakarni overstruck Nahapana's silver coins discovered in the Jogalthambi hoard.",
        "topperTip": "Jogalthambi hoard = Gautamiputra Satakarni overstriking Nahapana's coins.",
        "periodId": "satavahana-dynasty"
    },
    {
        "id": "anc_073",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2020",
        "isPyq": true,
        "year": 2020,
        "bookRef": "Upinder Singh, Ch. 7; Nitin Singhania, Ch. 1",
        "question": "With reference to the scholars/literary figures of ancient India, consider the following statements:\n1. Harishena was the court poet of Chandragupta II.\n2. Kalidasa was associated with Chandragupta II (Vikramaditya).\n3. Amarasimha was patronized by Pushyamitra Shunga.\nWhich of the statements given above is/are correct?",
        "options": [
            "1 and 2 only",
            "2 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 1,
        "explanation": "Only statement 2 is correct. Kalidasa was one of the Navaratnas (Nine Gems) in the court of Chandragupta II Vikramaditya. Statement 1 is incorrect because Harishena was the court poet (sandhivigrahika) of Samudragupta (author of Allahabad Pillar Inscription / Prayag Prasasti). Statement 3 is incorrect because Amarasimha (author of Amarakosha) was also one of the Navaratnas in Chandragupta II's court, not Pushyamitra Shunga's court.",
        "trap": "Harishena = Samudragupta; Kalidasa & Amarasimha = Chandragupta II.",
        "topperTip": "Prayag Prasasti was composed by Harishena in Champu kavya style for Samudragupta.",
        "periodId": "gupta-period"
    },
    {
        "id": "anc_074",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2019",
        "isPyq": true,
        "year": 2019,
        "bookRef": "Upinder Singh, Ch. 8; R.S. Sharma, Ch. 19",
        "question": "With reference to the forced labour (Vishti) in India during the Gupta period, which one of the following statements is correct?",
        "options": [
            "It was considered a source of income for the State, a sort of tax paid by the people.",
            "It was totally absent in the Madhya Pradesh and Kathiawar regions of the Gupta Empire.",
            "The forced labourer was entitled to weekly wages fixed by the guild.",
            "The eldest son of the labourer was permanently sent as the forced labourer."
        ],
        "correctIndex": 0,
        "explanation": "During the Gupta period, Vishti (forced unpaid labour) was treated as a legitimate royal prerogative and a tax paid by the people to the king or landed beneficiaries. Inscriptions frequently grant lands along with the right to extract vishti.",
        "trap": "Vishti was unpaid; labourers did NOT receive regular wages.",
        "topperTip": "Gupta land grants explicitly mention 'sarva-vishti-parihara' (exempt from all forced labour) when granted to Brahmanas.",
        "periodId": "gupta-period"
    },
    {
        "id": "anc_075",
        "category": "ancient",
        "categoryLabel": "Ancient India",
        "source": "UPSC CSE 2023",
        "isPyq": true,
        "year": 2023,
        "bookRef": "Upinder Singh, Ch. 8; NCERT Themes Theme 2",
        "question": "Consider the following dynasties:\n1. Hoysala\n2. Gahadavala\n3. Kakatiya\n4. Yadava\nHow many of the above dynasties established their kingdoms in the early eighth century CE?",
        "options": [
            "Only one",
            "Only two",
            "Only three",
            "None"
        ],
        "correctIndex": 3,
        "explanation": "None of these dynasties established their kingdoms in the early 8th century CE (700-750 CE). Gahadavalas established their power in Kannauj/Varanasi in the late 11th century (c. 1090 CE by Chandradeva). Hoysalas (Dwarasamudra), Kakatiyas (Warangal), and Seuna Yadavas (Devagiri) all arose as independent sovereign powers in the late 11th and 12th centuries CE after the decline of the Western Chalukyas and Cholas.",
        "trap": "Early 8th century CE is the era of Yashovarman of Kanauj, Lalitaditya of Kashmir, and the early Rashtrakutas (Dantidurga c. 753 CE). Hoysalas, Kakatiyas, Yadavas are 11th-12th century kingdoms!",
        "topperTip": "Chronology check: Kakatiyas, Hoysalas, Yadavas, and Pandyas were contemporaries who faced Alauddin Khalji's invasions (1296-1311 CE).",
        "periodId": "early-medieval-period"
    }
]

with open('data/batch_ancient.json', 'w', encoding='utf8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)
print(f"Generated {len(questions)} ancient questions successfully.")
