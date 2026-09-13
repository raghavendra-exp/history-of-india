/* UPSC Prelims & Mains Practice Hub
   Complete History of India — Interactive Test Simulator & Revision Suite */

const HistoryPractice = (() => {
  const QUESTIONS = [
  {
    "id": "q1",
    "category": "ancient",
    "categoryLabel": "Ancient India",
    "yearRef": "UPSC CSE Pattern",
    "question": "Which of the following statements regarding the Harappan city of Dholavira is/are correct?\n\n1. Unlike most Harappan settlements which were divided into two parts, Dholavira was divided into three distinct fortified sectors.\n2. A large signboard containing ten large-sized signs of the Indus script was discovered at the gateway of the city.\n3. It was constructed exclusively out of sun-dried mud bricks with no use of stone masonry.",
    "options": [
      "1 and 2 only",
      "2 only",
      "1 and 3 only",
      "1, 2 and 3"
    ],
    "correctIndex": 0,
    "explanation": "Statements 1 and 2 are correct. Dholavira (Kutch, Gujarat) is uniquely divided into three sectors: Citadel (Castle & Bailey), Middle Town, and Lower Town. A large wooden board with 10 large glyphs of the Indus script was found near the northern gateway. Statement 3 is incorrect because Dholavira is renowned for its extensive use of dressed stone masonry (sandstone and limestone) rather than exclusively mud bricks, which was atypical for Harappan cities.",
    "trap": "Look out for absolute words like 'exclusively'. Dholavira was built largely of stone, not purely mud brick.",
    "periodId": "indus-valley-civilization"
  },
  {
    "id": "q2",
    "category": "ancient",
    "categoryLabel": "Ancient India",
    "yearRef": "UPSC CSE Pattern",
    "question": "With reference to the religious practices of the Indus Valley Civilisation, consider the following statements:\n\n1. The presence of temples and monumental public shrines has been confirmed at Mohenjo-daro and Harappa.\n2. The 'Pashupati' seal discovered at Mohenjo-daro depicts a three-faced seated horned figure surrounded by an elephant, a tiger, a rhinoceros, and a buffalo.\n3. Fire altars have been discovered at both Lothal and Kalibangan.",
    "options": [
      "1 and 2 only",
      "2 and 3 only",
      "1 and 3 only",
      "1, 2 and 3"
    ],
    "correctIndex": 1,
    "explanation": "Statements 2 and 3 are correct. No temples or monumental public shrines have ever been found in any Harappan site; their religious life was non-monumental and iconographic. The Pashupati seal shows a yogic figure surrounded by 4 animals (elephant, tiger, rhino, buffalo) with two deer at the feet. Fire altars were excavated at both Kalibangan and Lothal.",
    "trap": "Remember: Harappans built no monumental stone temples or palaces of the Mesopotamian or Egyptian type!",
    "periodId": "indus-valley-civilization"
  },
  {
    "id": "q3",
    "category": "ancient",
    "categoryLabel": "Ancient India",
    "yearRef": "UPSC CSE Pattern",
    "question": "Regarding the socio-political institutions of the Later Vedic Period, consider the following pairs:\n\n1. Gramani \u2014 Village headman\n2. Bhagadugha \u2014 Tax collector / revenue assessor\n3. Suta \u2014 Royal charioteer and bard\n4. Sangrahitri \u2014 Chief priest and advisor\n\nHow many of the pairs given above are correctly matched?",
    "options": [
      "Only one pair",
      "Only two pairs",
      "Only three pairs",
      "All four pairs"
    ],
    "correctIndex": 2,
    "explanation": "Pairs 1, 2, and 3 are correctly matched. Pair 4 is incorrectly matched: Sangrahitri was the royal Treasurer / Collector of the treasury, whereas the Chief Priest was the Purohita. This Ratnin (king-maker) official list appears in the Shatapatha Brahmana.",
    "trap": "Sangrahitri means treasurer; Bhagadugha means collector of shares/taxes (bhaga = share).",
    "periodId": "vedic-age"
  },
  {
    "id": "q4",
    "category": "ancient",
    "categoryLabel": "Ancient India",
    "yearRef": "UPSC CSE Pattern",
    "question": "Which of the following factors contributed most decisively to the ultimate rise of Magadha as the supreme empire among the 16 Mahajanapadas?\n\n1. Abundant iron deposits in the Rajgir and Chotanagpur belts enabling superior weaponry and forest-clearing implements.\n2. Strategic geographical positioning of capitals (Rajgir surrounded by 5 hills; Pataliputra as a Jaladurga at river confluences).\n3. First extensive military deployment of elephants in war on a massive scale.\n4. Monopoly over maritime trade through the ports of Barygaza and Sopara.",
    "options": [
      "1, 2 and 3 only",
      "2, 3 and 4 only",
      "1 and 4 only",
      "1, 2, 3 and 4"
    ],
    "correctIndex": 0,
    "explanation": "Statements 1, 2, and 3 are historically accurate factors for Magadha's supremacy. Statement 4 is incorrect: Barygaza (Bharuch) and Sopara were on the western coast of India under the sphere of Avanti, Satavahanas, and Western Kshatrapas; Magadha dominated eastern inland trade along the Ganga and Tamralipti, not western peninsular ports.",
    "trap": "Barygaza and Sopara were western ports. Magadha's maritime outlet was Tamralipti in Bengal.",
    "periodId": "age-of-mahajanapadas"
  },
  {
    "id": "q5",
    "category": "ancient",
    "categoryLabel": "Ancient India",
    "yearRef": "UPSC CSE Pattern",
    "question": "With reference to Ashoka's Edicts, consider the following statements:\n\n1. The Kalinga War and Ashoka's remorse are described in Major Rock Edict XIII.\n2. At Dhauli and Jaugada, Major Rock Edicts XI, XII, and XIII are replaced by two Separate Kalinga Edicts.\n3. The bilingual Greek and Aramaic edict of Ashoka was discovered at Kandahar in modern Afghanistan.",
    "options": [
      "1 only",
      "1 and 2 only",
      "2 and 3 only",
      "1, 2 and 3"
    ],
    "correctIndex": 3,
    "explanation": "All three statements are correct. Major Rock Edict XIII details the conquest of Kalinga and Ashoka's subsequent conversion to Dhamma. In Kalinga itself (Dhauli and Jaugada), Ashoka omitted Edict XIII to avoid rubbing salt into wounds, substituting it with the Separate Edicts ('All men are my children'). The Shar-i-Kuna inscription at Kandahar is famously bilingual in Greek and Aramaic.",
    "trap": "Notice that Major Rock Edict XIII is absent specifically at the Kalinga sites!",
    "periodId": "ashoka-the-great"
  },
  {
    "id": "q6",
    "category": "ancient",
    "categoryLabel": "Ancient India",
    "yearRef": "UPSC CSE Pattern",
    "question": "In ancient Indian history, what was the term 'Vishti' used to denote?",
    "options": [
      "A religious cess levied on non-Buddhist pilgrims",
      "Forced and unpaid labour extracted by the state or landlords",
      "A category of military land grant given to royal feudatories",
      "A tribute paid in grain by conquered frontier tribes"
    ],
    "correctIndex": 1,
    "explanation": "In ancient India, particularly during the Mauryan and Gupta periods, 'Vishti' referred to forced, unpaid labour extracted by the sovereign or landlords from peasants and artisans. In the Junagadh rock inscription of Rudradaman I (150 CE), the king boasts that he repaired the Sudarshana lake embankment 'without oppressing the people with forced labour (apidhayitwa vishti) or extra cesses'.",
    "trap": "Vishti is consistently tested in UPSC as forced/unpaid labour.",
    "periodId": "gupta-age"
  },
  {
    "id": "q7",
    "category": "ancient",
    "categoryLabel": "Ancient India",
    "yearRef": "UPSC CSE Pattern",
    "question": "Consider the following ancient travelers to India and arrange them in correct chronological order of their arrival:\n\n1. Megasthenes\n2. Fa-Hien (Faxian)\n3. Xuanzang (Hiuen Tsang)\n4. Al-Biruni\n5. Yijing (I-Tsing)",
    "options": [
      "1 \u2014 2 \u2014 3 \u2014 5 \u2014 4",
      "1 \u2014 3 \u2014 2 \u2014 5 \u2014 4",
      "2 \u2014 1 \u2014 3 \u2014 4 \u2014 5",
      "1 \u2014 2 \u2014 5 \u2014 3 \u2014 4"
    ],
    "correctIndex": 0,
    "explanation": "Chronology: 1. Megasthenes (c. 302 BCE, Chandragupta Maurya) -> 2. Fa-Hien (c. 399-414 CE, Chandragupta II Vikramaditya) -> 3. Xuanzang (c. 629-645 CE, Harsha Vardhana) -> 5. Yijing (c. 671-695 CE, late 7th century Buddhist pilgrim) -> 4. Al-Biruni (1017 CE, accompanying Mahmud of Ghazni).",
    "trap": "Yijing arrived after Xuanzang (Hiuen Tsang), both during the 7th century.",
    "periodId": "post-gupta-age"
  },
  {
    "id": "q8",
    "category": "medieval",
    "categoryLabel": "Medieval India",
    "yearRef": "UPSC CSE Pattern",
    "question": "Which Delhi Sultan introduced the market control regulations (Shahna-i-Mandi), fixed the prices of essential commodities, and maintained a large standing army at low cost?",
    "options": [
      "Iltutmish",
      "Balban",
      "Alauddin Khilji",
      "Muhammad bin Tughlaq"
    ],
    "correctIndex": 2,
    "explanation": "Alauddin Khilji (1296\u20131316) implemented strict economic and market control reforms to maintain a huge standing army against Mongol incursions. He established separate markets for grains (Mandi), cloth/groceries (Sarai-i-Adl), and cattle/horses/slaves, supervised by superintendents called Shahna-i-Mandi, Barids (intelligence officers), and Munhiyan (spies).",
    "trap": "Market regulations were Alauddin Khilji's hallmark. Token currency was Muhammad bin Tughlaq.",
    "periodId": "khilji-dynasty"
  },
  {
    "id": "q9",
    "category": "medieval",
    "categoryLabel": "Medieval India",
    "yearRef": "UPSC CSE Pattern",
    "question": "With reference to the administration of the Chola Empire, consider the following statements:\n\n1. The village assembly of a brahmadeya (tax-free Brahmin settlement) was called 'Sabha' or 'Mahasabha'.\n2. The election of committee (variyam) members through the 'Kudavolai' (pot-ticket) system is detailed in the Uttaramerur Inscriptions of Parantaka I.\n3. The royal navy of Rajendra Chola I successfully conducted an expedition across the Bay of Bengal against the Srivijaya kingdom.",
    "options": [
      "1 and 2 only",
      "2 and 3 only",
      "1 and 3 only",
      "1, 2 and 3"
    ],
    "correctIndex": 3,
    "explanation": "All three statements are correct. The Cholas had sophisticated local self-government. The 'Ur' was the general village assembly, while 'Sabha' or 'Mahasabha' was the assembly of Brahmadeya villages. The Uttaramerur inscriptions of Parantaka I (919 and 921 CE) outline the Kudavolai election system, qualifications, and disqualifications. Rajendra Chola I sent naval expeditions across the Bay of Bengal to conquer Srivijaya (Sumatra/Malaya) in 1025 CE.",
    "trap": "Ur = non-Brahmadeya general assembly; Sabha = Brahmadeya assembly.",
    "periodId": "kingdoms-of-south"
  },
  {
    "id": "q10",
    "category": "medieval",
    "categoryLabel": "Medieval India",
    "yearRef": "UPSC CSE Pattern",
    "question": "In the context of the Mughal administrative system under Akbar, what do the terms 'Zat' and 'Sawar' denote in the Mansabdari system?",
    "options": [
      "Zat denoted the personal rank and salary status of the mansabdar, while Sawar indicated the number of cavalrymen and horses he was required to maintain.",
      "Zat denoted revenue collected from crown lands (Khalisa), while Sawar denoted the revenue from Jagir assignments.",
      "Zat was an honorific title awarded only to Rajput nobility, while Sawar was awarded to Turani nobles.",
      "Zat indicated the rank in the civil bureaucracy, while Sawar was purely for hereditary naval commanders."
    ],
    "correctIndex": 0,
    "explanation": "In Akbar's Mansabdari system, every mansabdar was assigned a dual numerical rank: 'Zat' (personal rank determining precedence, status, and salary scale) and 'Sawar' (contingent rank dictating the exact number of mounted cavalrymen and armed horses the noble was obligated to maintain for imperial service).",
    "trap": "Zat = personal status/pay scale; Sawar = actual cavalry obligation.",
    "periodId": "akbar-the-great"
  },
  {
    "id": "q11",
    "category": "medieval",
    "categoryLabel": "Medieval India",
    "yearRef": "UPSC CSE Pattern",
    "question": "With reference to the Vijayanagara Empire, consider the following statements:\n\n1. The kingdom was founded in 1336 CE by Harihara I and Bukka Raya I of the Sangama Dynasty.\n2. The Portuguese traveler Domingo Paes visited Vijayanagara during the reign of Krishnadeva Raya.\n3. The Battle of Talikota (1565) was fought during the reign of the Tuluva Dynasty emperor Krishnadeva Raya.",
    "options": [
      "1 and 2 only",
      "2 and 3 only",
      "1 and 3 only",
      "1, 2 and 3"
    ],
    "correctIndex": 0,
    "explanation": "Statements 1 and 2 are correct. Statement 3 is incorrect: Krishnadeva Raya died in 1529 CE. The catastrophic Battle of Talikota occurred in 1565 CE during the reign of Sadashiva Raya under the de-facto regency of Aliya Rama Raya (Aravidu dynasty).",
    "trap": "Krishnadeva Raya had passed away 36 years before the Battle of Talikota (1565)!",
    "periodId": "vijayanagara-empire"
  },
  {
    "id": "q12",
    "category": "medieval",
    "categoryLabel": "Medieval India",
    "yearRef": "UPSC CSE Pattern",
    "question": "Which medieval Indian ruler built the Grand Trunk Road (Sadak-e-Azam), introduced the standard silver coin called 'Rupiya', and established an efficient postal relay system (Sarai)?",
    "options": [
      "Alauddin Khilji",
      "Sher Shah Suri",
      "Akbar the Great",
      "Firoz Shah Tughlaq"
    ],
    "correctIndex": 1,
    "explanation": "Sher Shah Suri (1540\u20131545) was a visionary administrator who introduced the silver 'Rupiya' (178 grains) which survived through British rule, built the Sadak-e-Azam (Grand Trunk Road from Sonargaon to Attock) with 1,700 Sarais spaced every two kos with shaded trees and wells, and reformed the land revenue assessment system (Zabt).",
    "trap": "Akbar adopted and refined Sher Shah's administrative currency and revenue templates.",
    "periodId": "sur-interregnum"
  },
  {
    "id": "q13",
    "category": "medieval",
    "categoryLabel": "Medieval India",
    "yearRef": "UPSC CSE Pattern",
    "question": "With reference to the Bhakti movement, which of the following statements is/are correct?\n\n1. Kabir rejected all forms of institutionalized religion, polytheism, caste discrimination, and ritualism, composing verses in Sakhis and Dohas.\n2. Guru Nanak advocated 'Nirguna' Bhakti and established the institution of 'Langar' (community kitchen).\n3. Mirabai was a contemporary of Shankaracharya and propagated Advaita philosophy.",
    "options": [
      "1 and 2 only",
      "2 only",
      "1 and 3 only",
      "1, 2 and 3"
    ],
    "correctIndex": 0,
    "explanation": "Statements 1 and 2 are correct. Statement 3 is historically absurd: Shankaracharya lived in the 8th century CE promoting Advaita Vedanta, whereas Mirabai lived in the 16th century CE (c. 1498\u20131546) and was a passionate devotee of Krishna representing 'Saguna' Bhakti.",
    "trap": "Chronological mismatch: Shankaracharya (8th century) vs Mirabai (16th century, contemporary of Akbar).",
    "periodId": "delhi-sultanate"
  },
  {
    "id": "q14",
    "category": "modern",
    "categoryLabel": "Modern India",
    "yearRef": "UPSC CSE Pattern",
    "question": "The Regulating Act of 1773 was a landmark British statute because:\n\n1. It brought the East India Company's administrative affairs under the supervision of the British Parliament for the first time.\n2. It elevated the Governor of Bengal to the status of 'Governor-General of Bengal' assisted by a 4-member council.\n3. It provided for the establishment of a Supreme Court of Judicature at Fort William, Calcutta.",
    "options": [
      "1 and 2 only",
      "2 and 3 only",
      "1 and 3 only",
      "1, 2 and 3"
    ],
    "correctIndex": 3,
    "explanation": "All three statements are correct. The Regulating Act of 1773 was the first step by the British government to regulate the affairs of the East India Company. Warren Hastings was appointed the first Governor-General of Bengal. The Supreme Court at Calcutta was established in 1774 with Sir Elijah Impey as its first Chief Justice.",
    "trap": "Governor of Bengal became Governor-General of Bengal in 1773; he became Governor-General of INDIA only in the Charter Act of 1833 (Lord William Bentinck).",
    "periodId": "british-administration"
  },
  {
    "id": "q15",
    "category": "modern",
    "categoryLabel": "Modern India",
    "yearRef": "UPSC CSE Pattern",
    "question": "With reference to the British colonial land revenue settlements, consider the following statements:\n\n1. Permanent Settlement was introduced by Lord Cornwallis in 1793 in Bengal, Bihar, and Orissa, recognizing zamindars as owners of land with fixed revenue demands.\n2. Ryotwari System was devised by Thomas Munro and Alexander Read, where revenue settlement was made directly with the individual cultivator (Ryot).\n3. Mahalwari System was introduced by Holt Mackenzie in the North-Western Provinces and Punjab, where the village community (Mahal) was held collectively responsible for revenue payment.",
    "options": [
      "1 and 2 only",
      "2 and 3 only",
      "1 and 3 only",
      "1, 2 and 3"
    ],
    "correctIndex": 3,
    "explanation": "All three statements correctly characterize the three major colonial land revenue systems in India: Permanent Settlement (19% of British India, Zamindari ownership), Ryotwari (51% of British India, direct ryot liability), and Mahalwari (30% of British India, collective village community liability).",
    "trap": "Permanent = Cornwallis (1793); Ryotwari = Munro & Read; Mahalwari = Holt Mackenzie.",
    "periodId": "british-colonial-rule"
  },
  {
    "id": "q16",
    "category": "modern",
    "categoryLabel": "Modern India",
    "yearRef": "UPSC CSE Pattern",
    "question": "Which of the following was the immediate spark that ignited the Great Revolt of 1857?",
    "options": [
      "The annexation of the state of Awadh on the pretext of 'misgovernance' by Lord Dalhousie in 1856",
      "The introduction of the new Enfield rifle cartridge lubricated with beef and pork fat",
      "The abolition of the practice of Sati and legalization of widow remarriage",
      "The passage of the General Service Enlistment Act of 1856 requiring sepoys to serve overseas"
    ],
    "correctIndex": 1,
    "explanation": "While the annexation of Awadh (1856), General Service Enlistment Act, and Christian missionary activities provided deep underlying grievances, the IMMEDIATE trigger was the introduction of the Enfield P-53 rifle cartridges greased with cow and pig fat, which violated both Hindu and Muslim religious dietary laws as soldiers had to bite the cartridge open before loading.",
    "trap": "Distinguish between underlying causes (Awadh annexation, Doctrine of Lapse) and the IMMEDIATE spark (Enfield greased cartridges).",
    "periodId": "indian-freedom-struggle"
  },
  {
    "id": "q17",
    "category": "modern",
    "categoryLabel": "Modern India",
    "yearRef": "UPSC CSE Pattern",
    "question": "Consider the following socio-religious reform organizations and their founders:\n\n1. Brahmo Samaj \u2014 Raja Ram Mohan Roy\n2. Arya Samaj \u2014 Swami Dayananda Saraswati\n3. Satyashodhak Samaj \u2014 Jyotirao Phule\n4. Ramakrishna Mission \u2014 Swami Vivekananda\n\nWhich of the above are correctly matched?",
    "options": [
      "1, 2 and 3 only",
      "2, 3 and 4 only",
      "1 and 4 only",
      "1, 2, 3 and 4"
    ],
    "correctIndex": 3,
    "explanation": "All four pairs are correctly matched. Brahmo Samaj (1828, Calcutta) by Raja Ram Mohan Roy; Arya Samaj (1875, Bombay) by Swami Dayananda Saraswati ('Go back to the Vedas'); Satyashodhak Samaj (1873, Maharashtra) by Jyotirao Phule for lower-caste emancipation; Ramakrishna Mission (1897, Belur Math) by Swami Vivekananda.",
    "trap": "Phule founded Satyashodhak Samaj and wrote Gulamgiri; Dayananda Saraswati authored Satyarth Prakash.",
    "periodId": "socio-religious-reforms"
  },
  {
    "id": "q18",
    "category": "modern",
    "categoryLabel": "Modern India",
    "yearRef": "UPSC CSE Pattern",
    "question": "With reference to the Swadeshi Movement (1905\u20131908), consider the following statements:\n\n1. It erupted in reaction to Lord Curzon's partition of Bengal in 1905.\n2. The day partition took effect (16 October 1905) was observed as a day of national mourning and Raksha Bandhan.\n3. The movement remained strictly confined to Bengal and did not spread to any other part of India.",
    "options": [
      "1 and 2 only",
      "2 and 3 only",
      "1 only",
      "1, 2 and 3"
    ],
    "correctIndex": 0,
    "explanation": "Statements 1 and 2 are correct. Statement 3 is incorrect: The Swadeshi movement rapidly spread beyond Bengal across India under the leadership of Bal Gangadhar Tilak (Bombay/Pune), Lala Lajpat Rai (Punjab), Syed Haider Raza (Delhi), and Chidambaram Pillai (Madras/Tuticorin).",
    "trap": "Swadeshi was the first movement to spread nationwide, led by the Lal-Bal-Pal triumvirate.",
    "periodId": "indian-freedom-struggle"
  },
  {
    "id": "q19",
    "category": "modern",
    "categoryLabel": "Modern India",
    "yearRef": "UPSC CSE Pattern",
    "question": "What was the significance of the Lahore Session of the Indian National Congress held in December 1929 under the presidency of Jawaharlal Nehru?",
    "options": [
      "Adoption of the 'Purna Swaraj' (Complete Independence) resolution",
      "Reunion of the Moderates and Extremists after the Surat split",
      "Decision to cooperate with the Simon Commission",
      "Acceptance of the Communal Award"
    ],
    "correctIndex": 0,
    "explanation": "At the historic Lahore Congress (December 1929), the INC officially adopted 'Purna Swaraj' (Complete Independence) as its ultimate goal, unfurled the tricolour flag on the banks of the Ravi River on 31 December 1929, and declared that 26 January 1930 would be celebrated across India as 'Independence Day'.",
    "trap": "Purna Swaraj was adopted at Lahore (1929), NOT Karachi (1931, which adopted Fundamental Rights).",
    "periodId": "indian-freedom-struggle"
  },
  {
    "id": "q20",
    "category": "modern",
    "categoryLabel": "Modern India",
    "yearRef": "UPSC CSE Pattern",
    "question": "During the Quit India Movement (1942), 'parallel governments' (Prati Sarkar) were established in several parts of India. Which of the following locations witnessed these parallel administrations?\n\n1. Ballia (Uttar Pradesh) under Chittu Pandey\n2. Tamluk / Midnapore (Bengal) known as Jatiya Sarkar\n3. Satara (Maharashtra) under Nana Patil",
    "options": [
      "1 and 2 only",
      "2 and 3 only",
      "1 and 3 only",
      "1, 2 and 3"
    ],
    "correctIndex": 3,
    "explanation": "All three locations saw famous parallel governments during the 1942 Quit India rebellion: 1. Ballia (UP) under Chittu Pandey (declared independent for a week, released prisoners); 2. Tamluk (Bengal) where Jatiya Sarkar operated Vidyut Vahinis; 3. Satara (Maharashtra) under Nana Patil and Y.B. Chavan (longest-running Prati Sarkar).",
    "trap": "All three are high-yield UPSC examples of popular parallel governments during Quit India.",
    "periodId": "independence-of-india"
  },
  {
    "id": "q21",
    "category": "art",
    "categoryLabel": "Art & Culture",
    "yearRef": "UPSC CSE Pattern",
    "question": "Regarding the classical styles of Indian temple architecture, consider the following statements:\n\n1. In the Nagara style, the temple tower is known as 'Shikhara', whereas in the Dravida style, the tower over the sanctum is called 'Vimana'.\n2. Dravida style temples are characterized by monumental gateway towers called 'Gopurams' and a temple water tank (Kalyani/Pushkarini).\n3. The Vesara style represents a hybridization of Nagara and Dravida styles, seen predominantly in the temples of the Hoysalas and Chalukyas.",
    "options": [
      "1 and 2 only",
      "2 and 3 only",
      "1 and 3 only",
      "1, 2 and 3"
    ],
    "correctIndex": 3,
    "explanation": "All three statements are correct. Nagara style (North India) features curvilinear Shikhara over the Garbhagriha without boundary walls. Dravida style (South India) features stepped pyramidal Vimana, large pillared halls (Mandapa), high boundary walls with monumental Gopurams, and a water reservoir. Vesara (Deccan) is a composite blend patronized by Badami Chalukyas, Rashtrakutas, and Hoysalas.",
    "trap": "Vimana = tower directly over sanctum in South India; Gopuram = gateway tower.",
    "periodId": "kingdoms-of-south"
  },
  {
    "id": "q22",
    "category": "art",
    "categoryLabel": "Art & Culture",
    "yearRef": "UPSC CSE Pattern",
    "question": "With reference to the schools of ancient Indian sculpture, consider the following statements:\n\n1. Gandhara School was deeply influenced by Greco-Roman artistic idioms and predominantly utilized grey/blue schist stone.\n2. Mathura School developed completely indigenously using spotted red sandstone and produced images of Buddha, Mahavira, and Hindu deities.\n3. Amaravati School was patronized primarily by the Satavahanas and Ikshvakus, utilizing white marble-like limestone.",
    "options": [
      "1 and 2 only",
      "2 and 3 only",
      "1 and 3 only",
      "1, 2 and 3"
    ],
    "correctIndex": 3,
    "explanation": "All three statements are accurate: Gandhara (Northwest, Kushan period, grey schist/stucco, wavy Greek hair, Hellenistic drapery); Mathura (Upper Gangetic plain, indigenous, mottled red sandstone, fleshy cheerful transparent drapery); Amaravati (Krishna-Godavari basin, white limestone, narrative dynamic panels of Jatakas).",
    "trap": "Gandhara = Greco-Roman influence; Mathura = Indigenous development; Amaravati = Narrative relief carving.",
    "periodId": "post-mauryan-period"
  },
  {
    "id": "q23",
    "category": "uppsc",
    "categoryLabel": "Uttar Pradesh History (UPPSC)",
    "yearRef": "UPPSC GS Paper-I Pattern",
    "question": "Out of the sixteen Mahajanapadas mentioned in ancient Buddhist texts like the Anguttara Nikaya, how many were situated within the geographic boundaries of present-day Uttar Pradesh?",
    "options": [
      "4",
      "6",
      "8",
      "10"
    ],
    "correctIndex": 2,
    "explanation": "Exactly 8 of the 16 Mahajanapadas were located in modern Uttar Pradesh: 1. Kashi (Varanasi), 2. Kosala (Ayodhya/Shravasti), 3. Vatsa (Kaushambi), 4. Malla (Kushinagar/Pawa), 5. Kuru (Meerut/Hastinapur), 6. Panchala (Ahichchhatra/Kampilya), 7. Surasena (Mathura), and 8. Chedi (Bundelkhand/Shuktimati).",
    "trap": "A staple UPPSC question! Exactly 8 out of 16 Mahajanapadas were in Uttar Pradesh.",
    "periodId": "up-mahajanpadas"
  },
  {
    "id": "q24",
    "category": "uppsc",
    "categoryLabel": "Uttar Pradesh History (UPPSC)",
    "yearRef": "UPPSC GS Paper-I Pattern",
    "question": "Consider the following leaders of the Revolt of 1857 in Uttar Pradesh and their respective centers of rebellion:\n\n1. Nana Saheb and Tatya Tope \u2014 Kanpur\n2. Begum Hazrat Mahal \u2014 Lucknow (Awadh)\n3. Maulvi Ahmadullah Shah \u2014 Faizabad\n4. Khan Bahadur Khan \u2014 Bareilly (Rohilkhand)\n\nWhich of the pairs given above are correctly matched?",
    "options": [
      "1 and 2 only",
      "2, 3 and 4 only",
      "1, 3 and 4 only",
      "1, 2, 3 and 4"
    ],
    "correctIndex": 3,
    "explanation": "All four pairs are correctly matched. Kanpur: Nana Saheb, Azimullah Khan, Tatya Tope; Lucknow: Begum Hazrat Mahal and Birjis Qadir; Faizabad: Maulvi Ahmadullah Shah (who led stiff resistance against Colin Campbell); Bareilly: Khan Bahadur Khan (grandson of Hafiz Rahmat Khan).",
    "trap": "Every single pairing is a frequent UPPSC Prelims matching question.",
    "periodId": "up-revolt-of-1857"
  }
];
  const MAINS_QUESTIONS = [
  {
    "id": "m1",
    "title": "Town Planning and Civic Engineering in the Indus Valley Civilisation",
    "category": "ancient",
    "question": "To what extent can the urban planning and drainage architecture of the Indus Valley Civilisation offer practical insights for solving contemporary civic and sanitation challenges in modern Indian cities? (250 Words, 15 Marks)",
    "framework": {
      "intro": "The Indus Valley Civilisation (c. 2600\u20131900 BCE) represents South Asia's first urbanization, distinguished not by monumental palaces or mortuary grandeur, but by unprecedented civic hygiene, standardized brick masonry, and egalitarian urban architecture.",
      "dimensions": [
        "<b>Gridiron Layout & Zoning:</b> Segregation of residential sectors from administrative/craft zones; streets aligned along cardinal directions to utilize natural wind circulation for street cleaning.",
        "<b>Sanitation & Underground Drainage:</b> Soak pits, inspection manholes with removable covers, covered terracotta drains running beneath sidewalks\u2014a direct contrast to open gutters causing urban flooding today.",
        "<b>Water Resource Management:</b> Dholavira's cascading stone reservoirs and bunds harvesting monsoon runoff exemplify decentralized water conservation amidst climate stress.",
        "<b>Standardization & Quality Control:</b> Strict 4:2:1 brick proportion and standardized weights/measures reflecting accountable municipal governance."
      ],
      "conclusion": "Modern initiatives like the Smart Cities Mission and Swachh Bharat Abhiyan essentially strive to recreate the civic priorities that Harappan municipal planners mastered over four millennia ago."
    }
  },
  {
    "id": "m2",
    "title": "Bhakti Movement as an Instrument of Socio-Cultural Integration",
    "category": "medieval",
    "question": "Evaluate the role of the medieval Bhakti movement in breaking social hierarchies and facilitating the growth of regional vernacular languages. (250 Words, 15 Marks)",
    "framework": {
      "intro": "Originating in South India with the Alvars and Nayanars (6th\u20139th century CE) and sweeping across North India between the 14th and 17th centuries, the Bhakti movement was both a devotional renaissance and a profound socio-cultural rebellion against feudal rigidity.",
      "dimensions": [
        "<b>Democratic Spiritual Accessibility:</b> Emphasized intense personal devotion (prema/bhakti) over priestly mediation, costly Vedic sacrifices, and Sanskrit monopolies.",
        "<b>Erosion of Caste and Gender Barriers:</b> Welcomed marginalized castes and women (e.g. Kabir the weaver, Ravidas the leatherworker, Sena the barber, Mirabai, Akka Mahadevi, Andal).",
        "<b>Vibrant Flourishing of Regional Vernaculars:</b> Replaced classical Sanskrit with people's dialects\u2014Awadhi (Tulsidas), Braj Bhasha (Surdas), Bengali (Chaitanya), Marathi (Tukaram, Namdev), Assamese (Sankardev), and Punjabi (Guru Nanak).",
        "<b>Syncretic Hindu-Muslim Cultural Convergence:</b> Mutual philosophical interpenetration with Sufism (Wahdat-ul-Wujud), rejecting dogmatic orthodoxy."
      ],
      "conclusion": "The Bhakti movement laid the foundation for India's composite culture (Ganga-Jamuni Tehzeeb) and democratized religious knowledge into everyday vernacular literature."
    }
  },
  {
    "id": "m3",
    "title": "Economic Critique of Colonial Rule and the Freedom Movement",
    "category": "modern",
    "question": "Analyze how the 'Drain of Wealth' theory formulated by early nationalist thinkers dismantled the moral justification of British rule and laid the ideological groundwork for mass nationalism. (250 Words, 15 Marks)",
    "framework": {
      "intro": "In the late 19th century, moderate leaders like Dadabhai Naoroji ('Poverty and Un-British Rule in India', 1871), R.C. Dutt ('Economic History of India'), and M.G. Ranade pioneered the economic analysis of colonialism, exposing the systemic exploitation underlying the facade of the 'civilizing mission'.",
      "dimensions": [
        "<b>Anatomy of the Drain:</b> Naoroji exposed unrequited exports\u2014wealth siphoned off as Home Charges, pensions, guaranteed 5% railway dividends, and interest on external public debt without any economic return.",
        "<b>De-industrialization & Ruralization:</b> Ruin of traditional handicraft artisans due to discriminatory one-way tariff policies, forcing millions onto subsistence agriculture and causing catastrophic recurring famines.",
        "<b>Moral De-legitimization of the Raj:</b> Demolished the paternalistic British claim of providing 'benevolent peace and good governance', proving the British administration was bleeding India white.",
        "<b>Unifying Catalyst for Mass Movements:</b> Linked the day-to-day poverty of peasants and workers directly to imperial rule, equipping Tilak, Gandhi, and the Congress with an incontrovertible anti-colonial rationale."
      ],
      "conclusion": "The economic critique transformed nationalist resistance from a polite quest for administrative concessions into an existential battle for economic and political sovereignty (Swaraj)."
    }
  }
];

  let activeCategory = 'all';
  let activeMode = 'prelims'; // 'prelims' or 'mains'
  let userAnswers = {}; // questionId -> selectedIndex
  let stats = { attempted: 0, correct: 0 };

  const CATEGORIES = [
    { id: 'all', label: 'All Subjects', icon: '🎯' },
    { id: 'ancient', label: 'Ancient India', icon: '🏺' },
    { id: 'medieval', label: 'Medieval India', icon: '⚔️' },
    { id: 'modern', label: 'Modern India', icon: '🇮🇳' },
    { id: 'art', label: 'Art & Culture', icon: '🛕' },
    { id: 'uppsc', label: 'UPPSC Special', icon: '🏛️' }
  ];

  function getQuestions() {
    return QUESTIONS;
  }

  function getFilteredQuestions() {
    if (activeCategory === 'all') return QUESTIONS;
    return QUESTIONS.filter(q => q.category === activeCategory);
  }

  function getFilteredMains() {
    if (activeCategory === 'all') return MAINS_QUESTIONS;
    return MAINS_QUESTIONS.filter(m => m.category === activeCategory);
  }

  function setCategory(catId) {
    activeCategory = catId;
    render();
  }

  function setMode(mode) {
    activeMode = mode;
    render();
  }

  function submitAnswer(questionId, selectedIdx) {
    if (userAnswers[questionId] !== undefined) return; // already answered

    userAnswers[questionId] = selectedIdx;
    const q = QUESTIONS.find(item => item.id === questionId);
    if (!q) return;

    stats.attempted++;
    if (selectedIdx === q.correctIndex) {
      stats.correct++;
    }

    renderScoreboard();
    renderQuestionCard(questionId);
  }

  function resetQuiz() {
    userAnswers = {};
    stats = { attempted: 0, correct: 0 };
    render();
  }

  function renderScoreboard() {
    const attemptedEl = document.getElementById('statAttempted');
    const correctEl = document.getElementById('statCorrect');
    const accuracyEl = document.getElementById('statAccuracy');
    if (!attemptedEl || !correctEl || !accuracyEl) return;

    attemptedEl.textContent = stats.attempted;
    correctEl.textContent = stats.correct;
    const accuracy = stats.attempted > 0 ? Math.round((stats.correct / stats.attempted) * 100) : 0;
    accuracyEl.textContent = `${accuracy}%`;
  }

  function renderCategoryChips() {
    const bar = document.getElementById('practiceCategoryBar');
    if (!bar) return;

    bar.innerHTML = CATEGORIES.map(c => `
      <button class="filter-chip ${activeCategory === c.id ? 'active' : ''}" 
              onclick="HistoryPractice.setCategory('${c.id}')">
        <span>${c.icon}</span> ${c.label}
      </button>`).join('');
  }

  function renderQuestionCard(questionId) {
    const cardEl = document.getElementById(`qcard-${questionId}`);
    if (!cardEl) return;

    const q = QUESTIONS.find(item => item.id === questionId);
    if (!q) return;

    const answered = userAnswers[questionId] !== undefined;
    const selectedIdx = userAnswers[questionId];
    const isCorrect = selectedIdx === q.correctIndex;

    cardEl.className = `practice-q-card tablet reveal in ${answered ? (isCorrect ? 'q-correct' : 'q-incorrect') : ''}`;

    const optionsHtml = q.options.map((opt, idx) => {
      let optClass = 'opt-btn';
      if (answered) {
        if (idx === q.correctIndex) optClass += ' opt-correct';
        else if (idx === selectedIdx) optClass += ' opt-wrong';
        else optClass += ' opt-disabled';
      }
      return `
        <button class="${optClass}" 
                ${answered ? 'disabled' : ''} 
                onclick="HistoryPractice.submitAnswer('${q.id}', ${idx})">
          <span class="opt-label">${String.fromCharCode(65 + idx)}</span>
          <span class="opt-text">${opt}</span>
        </button>`;
    }).join('');

    const explanationHtml = answered ? `
      <div class="q-explanation reveal in">
        <div class="exp-header">
          <span class="exp-badge ${isCorrect ? 'badge-correct' : 'badge-wrong'}">
            ${isCorrect ? '✓ Correct Answer' : '✗ Incorrect Attempt'}
          </span>
          <span class="exp-correct-tag">Correct Option: <b>(${String.fromCharCode(65 + q.correctIndex)})</b></span>
        </div>
        <p class="exp-text">${q.explanation}</p>
        <div class="upsc-panel" style="margin:10px 0 0; border-color:var(--seal); background:var(--seal-tint); padding:12px 16px;">
          <h4 style="color:var(--seal-strong); margin-bottom:4px; font-size:0.75rem;">💡 UPSC Elimination Trick &amp; Trap</h4>
          <p style="margin:0; font-size:0.84rem; color:var(--ink);">${q.trap}</p>
        </div>
        <div style="margin-top:10px; font-size:0.8rem;">
          <a href="period.html?id=${q.periodId}" style="color:var(--accent); text-decoration:none; font-weight:600;">
            Review topic in Period Chapter (${q.periodId}) &rarr;
          </a>
        </div>
      </div>` : '';

    cardEl.innerHTML = `
      <div class="q-head">
        <div class="q-meta">
          <span class="badge badge-site badge-${q.category}">${q.categoryLabel}</span>
          <span class="q-year">${q.yearRef}</span>
        </div>
        <span class="q-id">#${q.id.toUpperCase()}</span>
      </div>
      <div class="q-body">
        <p class="q-prompt">${q.question.replace(/\n/g, '<br>')}</p>
        <div class="q-options">${optionsHtml}</div>
        ${explanationHtml}
      </div>`;
  }

  function renderPrelims() {
    const container = document.getElementById('practiceContainer');
    if (!container) return;

    const filtered = getFilteredQuestions();
    if (!filtered.length) {
      container.innerHTML = '<p class="loading-note">No questions found in this category.</p>';
      return;
    }

    container.innerHTML = `
      <div class="q-list">
        ${filtered.map(q => `<div id="qcard-${q.id}"></div>`).join('')}
      </div>`;

    filtered.forEach(q => renderQuestionCard(q.id));
  }

  function renderMains() {
    const container = document.getElementById('practiceContainer');
    if (!container) return;

    const filtered = getFilteredMains();
    if (!filtered.length) {
      container.innerHTML = '<p class="loading-note">No Mains questions found in this category.</p>';
      return;
    }

    container.innerHTML = `
      <div class="mains-list">
        ${filtered.map(m => `
          <div class="tablet reveal in" style="margin-bottom:24px; padding:28px;">
            <span class="badge badge-site badge-${m.category}" style="margin-bottom:10px;">UPSC Mains GS Paper-I</span>
            <h3 style="font-size:1.35rem; margin-bottom:12px;">${m.title}</h3>
            <div class="mains-prompt" style="background:var(--bg-sunken); padding:16px 20px; border-left:4px solid var(--gold); border-radius:4px; font-weight:500; font-size:1rem; margin-bottom:20px;">
              ${m.question}
            </div>
            
            <div class="mains-framework">
              <h4 style="font-family:var(--font-mono); font-size:0.8rem; text-transform:uppercase; letter-spacing:0.08em; color:var(--ink-faint); margin-bottom:8px;">Model Answer Structuring Framework</h4>
              <div style="margin-bottom:12px;">
                <b style="font-size:0.88rem; color:var(--seal);">1. Context &amp; Introduction (30-40 words):</b>
                <p style="font-size:0.9rem; color:var(--ink-soft); margin:4px 0 10px;">${m.framework.intro}</p>
              </div>
              <div style="margin-bottom:12px;">
                <b style="font-size:0.88rem; color:var(--accent);">2. Analytical Core Dimensions:</b>
                <ul style="padding-left:1.3em; margin-top:6px; font-size:0.9rem; color:var(--ink-soft);">
                  ${m.framework.dimensions.map(d => `<li style="margin-bottom:6px;">${d}</li>`).join('')}
                </ul>
              </div>
              <div>
                <b style="font-size:0.88rem; color:var(--gold);">3. Balanced Conclusion &amp; Contemporary Resonance:</b>
                <p style="font-size:0.9rem; color:var(--ink-soft); margin:4px 0 0;">${m.framework.conclusion}</p>
              </div>
            </div>
          </div>
        `).join('')}
      </div>`;
  }

  function render() {
    renderCategoryChips();
    renderScoreboard();
    if (activeMode === 'prelims') {
      renderPrelims();
    } else {
      renderMains();
    }
  }

  function init() {
    renderNav('practice.html');
    renderBreadcrumb([{ label: 'Home', href: 'index.html' }, { label: 'UPSC Practice Hub' }]);
    render();
    renderFooter();
  }

  return { init, setCategory, setMode, submitAnswer, resetQuiz, getQuestions };
})();
