import json

with open('data/prelims-questions.json', 'r', encoding='utf-8') as f:
    prelims = json.load(f)

print(f"Current Prelims count: {len(prelims)}")

new_questions = [
    # B.L. Grover & Pratik Nayak: British Doctrines & Early Conquest
    {
        "id": "prelims-blg-001",
        "question": "Which of the following is the correct chronological sequence of Indian states entering into Lord Wellesley's Subsidiary Alliance system?",
        "options": [
            "Hyderabad — Mysore — Tanjore — Awadh — Peshwa (Marathas)",
            "Mysore — Hyderabad — Awadh — Tanjore — Peshwa",
            "Awadh — Hyderabad — Mysore — Peshwa — Tanjore",
            "Hyderabad — Awadh — Mysore — Peshwa — Tanjore"
        ],
        "correctIndex": 0,
        "explanation": "According to B.L. Grover and Pratik Nayak, Lord Wellesley codified the Subsidiary Alliance in 1798. The chronological order of states entering the alliance is: Nizam of Hyderabad (1798), Mysore (1799, following Tipu Sultan's defeat in the 4th Anglo-Mysore War), Tanjore (October 1799), Awadh (1801, forced to cede half its territory), and the Maratha Peshwa Baji Rao II (1802, Treaty of Bassein).",
        "bookRef": "B.L. Grover, A New Look at Modern Indian History; Pratik Nayak Freedom Struggle Compendium"
    },
    {
        "id": "prelims-blg-002",
        "question": "Consider the following princely states annexed by Lord Dalhousie under the 'Doctrine of Lapse':\n1. Satara\n2. Jhansi\n3. Sambalpur\n4. Nagpur\nWhat is the correct chronological order of their annexation?",
        "options": [
            "1 — 3 — 2 — 4",
            "1 — 2 — 3 — 4",
            "3 — 1 — 4 — 2",
            "1 — 4 — 3 — 2"
        ],
        "correctIndex": 0,
        "explanation": "Lord Dalhousie applied the Doctrine of Lapse to annex dependent native states where the ruler died without a natural male heir: Satara (1848 - first state annexed), Jaitpur and Sambalpur (1849), Baghat (1850), Udaipur (1852), Jhansi (1853), and Nagpur (1854). Awadh was annexed in 1856, but on the pretext of 'misgovernance' rather than the Doctrine of Lapse.",
        "bookRef": "B.L. Grover, Ch. 12; Pratik Nayak HFS5P4"
    },
    {
        "id": "prelims-blg-003",
        "question": "Regarding British land revenue systems, consider the following statements:\n1. The Permanent Settlement covered approximately 19% of British India, while the Ryotwari system covered about 51%.\n2. Under the Permanent Settlement, the state demand was fixed at 10/11th for the government and 1/11th for the Zamindar.\n3. The Mahalwari system was formulated by Holt Mackenzie and settled revenue with village communities through headmen (Lambardars).\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 3,
        "explanation": "All three statements are historically accurate: Permanent Settlement covered ~19% of British India (Bengal, Bihar, Orissa, Northern Circars) with state share at 10/11th; Ryotwari covered ~51% (Madras, Bombay, Assam); Mahalwari (Holt Mackenzie, Regulation VII of 1822) covered ~30% (NWFP, Punjab, Central Provinces) where revenue was settled with the Mahal collectively through Lambardars.",
        "bookRef": "B.L. Grover; Pratik Nayak HFS3P4"
    },
    {
        "id": "prelims-blg-004",
        "question": "Which British Governor-General is famously known as the 'Liberator of the Indian Press' for repealing the restrictive 1823 Licensing Regulations?",
        "options": [
            "Lord William Bentinck",
            "Sir Charles Metcalfe",
            "Lord Macaulay",
            "Lord Ripon"
        ],
        "correctIndex": 1,
        "explanation": "Sir Charles Metcalfe (acting Governor-General 1835-36) passed the Press Act of 1835, which repealed John Adams' draconian 1823 Licensing Regulations (which had banned Raja Rammohan Roy's Mirat-ul-Akhbar). For restoring press freedom, Metcalfe is celebrated as the 'Liberator of the Indian Press'.",
        "bookRef": "B.L. Grover; Pratik Nayak HFS3P2"
    },
    {
        "id": "prelims-blg-005",
        "question": "With reference to the Vernacular Press Act of 1878, which of the following statements is INCORRECT?",
        "options": [
            "It was enacted during the viceroyalty of Lord Lytton.",
            "It required vernacular newspaper publishers to enter into a bond not to publish anything likely to excite disaffection against the government.",
            "The magistrate's action under the Act was subject to an appeal in a civil court of law.",
            "The Amrita Bazar Patrika overnight converted itself into an English-language weekly to escape the Act's provisions."
        ],
        "correctIndex": 2,
        "explanation": "Statement 3 is incorrect because the magistrate's action under the Vernacular Press Act was final and no appeal could be made in a court of law. It was nicknamed the 'Gagging Act'. The Amrita Bazar Patrika (edited by Sisir Kumar Ghosh and Motilal Ghosh) famously morphed overnight from Bengali to English to circumvent the Act. It was eventually repealed by Lord Ripon in 1882.",
        "bookRef": "B.L. Grover; Pratik Nayak HFS3P2"
    },
    {
        "id": "prelims-blg-006",
        "question": "Which of the following British famine commissions was the FIRST to recommend that relief of the distressed during famines should be recognized as a paramount obligation of the State, leading to the formulation of the Provisional Famine Code?",
        "options": [
            "Campbell Commission (1866)",
            "Strachey Commission (1880)",
            "Lyall Commission (1897)",
            "MacDonnell Commission (1901)"
        ],
        "correctIndex": 1,
        "explanation": "The Richard Strachey Commission (1880), appointed after the Great Famine of 1876-78 under Lord Lytton, formulated the principles of famine relief: state obligation to provide employment to able-bodied, gratuitous relief to destitute, suspension and remission of land revenue, and creating a permanent Famine Insurance Fund. Its recommendations formed the bedrock of the 1883 Provisional Famine Code.",
        "bookRef": "B.L. Grover; Pratik Nayak HFS4P1"
    },
    {
        "id": "prelims-blg-007",
        "question": "With reference to educational policy in British India, Wood's Educational Despatch of 1854 recommended which of the following?\n1. Downward Filtration Theory to educate only the upper classes\n2. Establishment of universities on the model of London University in Calcutta, Bombay, and Madras\n3. English as the medium of instruction for higher education and vernaculars for school education\n4. Promotion of female education and grant-in-aid system for private schools\nSelect the correct answer using the code below:",
        "options": [
            "1 and 2 only",
            "2, 3 and 4 only",
            "1, 3 and 4 only",
            "1, 2, 3 and 4"
        ],
        "correctIndex": 1,
        "explanation": "Wood's Despatch of 1854 explicitly repudiated Macaulay's 'Downward Filtration Theory', emphasizing mass education. It recommended establishing universities at Calcutta, Bombay, and Madras (set up in 1857), vernaculars as medium for primary education, English for collegiate education, female education, and a system of grants-in-aid. It is known as the 'Magna Carta of English Education in India'.",
        "bookRef": "B.L. Grover; Pratik Nayak HFS3P1"
    },
    {
        "id": "prelims-blg-008",
        "question": "Who among the following was the FIRST Indian to qualify for the prestigious Indian Civil Service (ICS) examination in London?",
        "options": [
            "Surendranath Banerjea",
            "Satyendranath Tagore",
            "Romesh Chunder Dutt",
            "Subhash Chandra Bose"
        ],
        "correctIndex": 1,
        "explanation": "Satyendranath Tagore (elder brother of Rabindranath Tagore) was the first Indian to qualify for the Indian Civil Service exam held in London, clearing it in 1863 and being posted in Bombay Presidency. Surendranath Banerjea cleared it in 1869.",
        "bookRef": "B.L. Grover; Pratik Nayak HFS3P2"
    },
    {
        "id": "prelims-blg-009",
        "question": "The Lee Commission, appointed by the British Government in 1923, dealt primarily with which of the following subjects?",
        "options": [
            "Reorganization of Indian Currency and Exchange",
            "Condition and Indianization of Superior Civil Services",
            "Development of Agricultural Marketing and Cooperatives",
            "Frontier Defense and Military Reorganization"
        ],
        "correctIndex": 1,
        "explanation": "The Royal Commission on Superior Civil Services in India (Lee Commission, 1923-24 under Lord Lee of Fareham) recommended rapid Indianization of civil services: 50:50 parity between Europeans and Indians in the ICS within 15 years, and immediate establishment of a statutory Public Service Commission (which was established in 1926).",
        "bookRef": "B.L. Grover; Pratik Nayak HFS3P2"
    },
    {
        "id": "prelims-blg-010",
        "question": "Which of the following early political associations was established in London in 1866 by Dadabhai Naoroji to present Indian viewpoints directly before the British public and Parliament?",
        "options": [
            "British Indian Association",
            "East India Association",
            "Indian National Association",
            "London Indian Society"
        ],
        "correctIndex": 1,
        "explanation": "Dadabhai Naoroji founded the East India Association in London in 1866. Its primary objective was to discuss the Indian question and influence British public opinion and members of Parliament in favor of Indian political and economic welfare.",
        "bookRef": "B.L. Grover; Pratik Nayak HFS7P1"
    },

    # Freedom Struggle & Revolutionary Movements (Pratik Nayak)
    {
        "id": "prelims-pn-001",
        "question": "Regarding the Swadeshi Movement (1905–1908), consider the following statements:\n1. The formal proclamation of the Swadeshi Movement and the Boycott Resolution was made at the Calcutta Town Hall on August 7, 1905.\n2. The National Council of Education was set up in 1906 with Aurobindo Ghosh as its principal.\n3. V.O. Chidambaram Pillai launched the Swadeshi Steam Navigation Company at Tuticorin to challenge the British shipping monopoly.\nWhich of the statements given above are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 3,
        "explanation": "All three statements are correct: The boycott resolution was passed at Calcutta Town Hall on 7 August 1905; National Council of Education was founded on 15 August 1906 with Aurobindo Ghosh as principal of Bengal National College; V.O. Chidambaram Pillai established the Swadeshi Steam Navigation Company in Tamil Nadu, sailing ships between Tuticorin and Colombo.",
        "bookRef": "Pratik Nayak HFS7P6; Bipan Chandra, Ch. 10"
    },
    {
        "id": "prelims-pn-002",
        "question": "Who among the following presided over the historic 1907 Surat Session of the Indian National Congress, where the split between Moderates and Extremists occurred?",
        "options": [
            "Dadabhai Naoroji",
            "Rash Behari Ghosh",
            "Gopal Krishna Gokhale",
            "Bal Gangadhar Tilak"
        ],
        "correctIndex": 1,
        "explanation": "Dr. Rash Behari Ghosh was elected president of the 1907 Surat Congress session. The Extremists wanted Lala Lajpat Rai or Bal Gangadhar Tilak as president and sought reaffirmation of the 1906 Calcutta resolutions on Swadeshi, Boycott, National Education, and Swaraj, leading to chaotic clashes and the suspension of the session.",
        "bookRef": "Pratik Nayak HFS7P6; B.L. Grover"
    },
    {
        "id": "prelims-pn-003",
        "question": "Regarding the Home Rule League Movement (1916), which of the following is correct regarding the territorial division between Tilak's League and Annie Besant's League?",
        "options": [
            "Tilak's League was confined to Maharashtra (excluding Bombay city), Karnataka, Central Provinces, and Berar, while Besant's League covered the rest of India.",
            "Besant's League was confined to Madras Presidency and Bombay city, while Tilak's League covered all of North India.",
            "Tilak's League covered Bengal and Punjab, while Besant's League operated exclusively in South India.",
            "Both Leagues operated throughout the entire country with overlapping branches and no territorial demarcation."
        ],
        "correctIndex": 0,
        "explanation": "To prevent friction, Tilak and Annie Besant demarcated their spheres of work in 1916: Tilak's League operated in Maharashtra (excluding Bombay city), Karnataka, Central Provinces, and Berar with 6 branches; Annie Besant's League operated in the rest of India (including Bombay city) with 200 branches.",
        "bookRef": "Pratik Nayak HFS8P3; Spectrum Modern India"
    },
    {
        "id": "prelims-pn-004",
        "question": "The Komagata Maru incident (1914), which galvanized the Ghadar Movement, involved a Japanese steamship carrying Indian immigrants that was refused entry by the government of which country?",
        "options": [
            "United States of America",
            "Canada",
            "Australia",
            "United Kingdom"
        ],
        "correctIndex": 1,
        "explanation": "The Komagata Maru was a Japanese steamship chartered by Gurdit Singh carrying 376 passengers (mostly Punjabi Sikhs and Muslims) to Vancouver, Canada. Canadian authorities refused entry under strict Asiatic exclusion laws. Forced to return, the ship docked at Budge Budge (Calcutta) in September 1914, where British police opened fire, killing over 20 passengers and triggering Ghadarite uprisings.",
        "bookRef": "Pratik Nayak HFS8P1; Bipan Chandra, Ch. 12"
    },
    {
        "id": "prelims-pn-005",
        "question": "Who among the following was the founder of the 'Hindustan Republican Association' (HRA) established at Kanpur in October 1924?",
        "options": [
            "Sachindra Nath Sanyal, Ram Prasad Bismil, and Jogesh Chandra Chatterjee",
            "Bhagat Singh, Sukhdev, and Chandrashekhar Azad",
            "Surya Sen, Pritilata Waddedar, and Ganesh Ghosh",
            "Lala Har Dayal and Sohan Singh Bhakna"
        ],
        "correctIndex": 0,
        "explanation": "The Hindustan Republican Association (HRA) was founded in October 1924 at Kanpur by Sachindra Nath Sanyal (author of Bandi Jiwan), Ram Prasad Bismil, and Jogesh Chandra Chatterjee to organize armed revolution to establish the Federal Republic of the United States of India. It was later reorganized as the Hindustan Socialist Republican Association (HSRA) in 1928 under Bhagat Singh and Chandrashekhar Azad.",
        "bookRef": "Pratik Nayak HFS10P2; B.L. Grover"
    },
    {
        "id": "prelims-pn-006",
        "question": "On April 8, 1929, Bhagat Singh and Batukeshwar Dutt threw smoke bombs and leaflets into the Central Legislative Assembly in Delhi to protest against the passage of which two reactionary bills?",
        "options": [
            "The Rowlatt Bill and the Arms Act",
            "The Public Safety Bill and the Trade Disputes Bill",
            "The Vernacular Press Bill and the Sedition Bill",
            "The Ilbert Bill and the Defence of India Bill"
        ],
        "correctIndex": 1,
        "explanation": "Bhagat Singh and Batukeshwar Dutt threw non-lethal bombs and distributed leaflets in the Central Legislative Assembly on 8 April 1929 to protest against the passage of the Public Safety Bill (which allowed detention of foreign socialists helping Indian trade unions) and the Trade Disputes Bill (which curbed the right to strike). Their stated aim was 'to make the deaf hear'.",
        "bookRef": "Pratik Nayak HFS10P2; Bipan Chandra, Ch. 20"
    },
    {
        "id": "prelims-pn-007",
        "question": "The legendary Chittagong Armoury Raid of April 1930 was planned and executed under the leadership of which revolutionary leader, affectionately known as 'Masterda'?",
        "options": [
            "Rash Behari Bose",
            "Jatin Das",
            "Surya Sen",
            "Sachindra Nath Sanyal"
        ],
        "correctIndex": 2,
        "explanation": "Surya Sen ('Masterda'), a schoolteacher in Chittagong (now Bangladesh), led the Indian Republican Army (Chittagong Branch) on 18 April 1930 in raiding two government armouries, cutting railway and telegraph lines, and declaring a provisional revolutionary government. Women revolutionaries like Pritilata Waddedar and Kalpana Datta played active operational roles.",
        "bookRef": "Pratik Nayak HFS10P2; Spectrum Modern India"
    },
    {
        "id": "prelims-pn-008",
        "question": "Which Congress session is uniquely famous for being the ONLY session presided over by Mahatma Gandhi?",
        "options": [
            "Nagpur Session, 1920",
            "Ahmedabad Session, 1921",
            "Belgaum Session, 1924",
            "Karachi Session, 1931"
        ],
        "correctIndex": 2,
        "explanation": "The Belgaum Session of December 1924 was the only session of the Indian National Congress presided over by Mahatma Gandhi. At this session, Gandhi endorsed the Swarajist agreement, allowing Swarajists to work within legislative councils while Congress workers focused on constructive programmes.",
        "bookRef": "Pratik Nayak HFS10P1; B.L. Grover"
    },
    {
        "id": "prelims-pn-009",
        "question": "With reference to the Swaraj Party formed in January 1923, who among the following leaders were known as 'No-Changers' who opposed council entry?",
        "options": [
            "C.R. Das and Motilal Nehru",
            "Vallabhbhai Patel, C. Rajagopalachari, and Rajendra Prasad",
            "Hakim Ajmal Khan and Vithalbhai Patel",
            "Subhash Chandra Bose and Jawaharlal Nehru"
        ],
        "correctIndex": 1,
        "explanation": "After the withdrawal of Non-Cooperation, Congress split into Swarajists (Pro-Changers like C.R. Das and Motilal Nehru, who advocated entering legislative councils to wreck the 1919 reforms from within) and No-Changers (Vallabhbhai Patel, C. Rajagopalachari, Rajendra Prasad, M.A. Ansari, who opposed council entry and advocated constructive grassroots work).",
        "bookRef": "Pratik Nayak HFS10P1; Bipan Chandra, Ch. 19"
    },
    {
        "id": "prelims-pn-010",
        "question": "Who was the FIRST Indian to be elected as the President (Speaker) of the Central Legislative Assembly in 1925, representing a crowning triumph for the Swarajists?",
        "options": [
            "Motilal Nehru",
            "Vithalbhai J. Patel",
            "C.R. Das",
            "Srinivasa Iyengar"
        ],
        "correctIndex": 1,
        "explanation": "Vithalbhai J. Patel (elder brother of Vallabhbhai Patel) was elected President (Speaker) of the Central Legislative Assembly in August 1925, defeating the government's official candidate T. Rangachariar by two votes. This was a monumental parliamentary victory for the Swaraj Party.",
        "bookRef": "Pratik Nayak HFS10P1; B.L. Grover"
    },
    {
        "id": "prelims-pn-011",
        "question": "The Nehru Report of 1928, drafted under the chairmanship of Motilal Nehru, recommended which of the following?\n1. Complete independence (Purna Swaraj) immediately\n2. Rejection of separate communal electorates in favor of joint electorates with reservation of seats for minorities\n3. Fundamental Rights including universal adult suffrage and equal rights for women\n4. Reorganization of provinces on a linguistic basis\nSelect the correct answer using the code below:",
        "options": [
            "1 and 2 only",
            "2, 3 and 4 only",
            "1, 3 and 4 only",
            "1, 2, 3 and 4"
        ],
        "correctIndex": 1,
        "explanation": "The Nehru Report (1928) recommended Dominion Status (not complete independence, which caused young leaders Jawaharlal Nehru and Subhash Bose to form the Independence for India League), joint electorates with reserved minority seats where in a minority, Fundamental Rights (19 rights including universal adult suffrage), and linguistic reorganization of provinces.",
        "bookRef": "Pratik Nayak HFS10P3; B.L. Grover"
    },
    {
        "id": "prelims-pn-012",
        "question": "During the Civil Disobedience Movement of 1930, C. Rajagopalachari organized a famous salt march from Tiruchirappalli to break the salt law at which coastal town?",
        "options": [
            "Dharasana",
            "Vedaranyam",
            "Payyanur",
            "Tuticorin"
        ],
        "correctIndex": 1,
        "explanation": "In Tamil Nadu, C. Rajagopalachari organized the Vedaranyam Salt March in April 1930, marching from Tiruchirappalli to the coastal town of Vedaranyam on the Coromandel coast to harvest contraband salt, mirroring Gandhi's Dandi March. In Malabar (Kerala), K. Kelappan marched from Calicut to Payyanur.",
        "bookRef": "Pratik Nayak HFS10P3; Bipan Chandra, Ch. 21"
    },
    {
        "id": "prelims-pn-013",
        "question": "At which landmark Congress session was the historic Resolution on Fundamental Rights and the National Economic Programme (drafted by Jawaharlal Nehru) formally adopted?",
        "options": [
            "Lahore Session, 1929",
            "Karachi Session, 1931",
            "Faizpur Session, 1937",
            "Haripura Session, 1938"
        ],
        "correctIndex": 1,
        "explanation": "The Karachi Session of March 1931, presided over by Sardar Vallabhbhai Patel (held days after the execution of Bhagat Singh and the Gandhi-Irwin Pact), passed the historic Resolution on Fundamental Rights and the National Economic Programme drafted by Jawaharlal Nehru. It committed the Congress to basic civil liberties, adult suffrage, free primary education, living wages, and state ownership of key industries and transport.",
        "bookRef": "Pratik Nayak HFS10P4; B.L. Grover"
    },
    {
        "id": "prelims-pn-014",
        "question": "Under the Poona Pact of September 1932 signed between Dr. B.R. Ambedkar and representatives of caste Hindus on behalf of Mahatma Gandhi, the number of reserved seats for the Depressed Classes in provincial legislatures was:",
        "options": [
            "Kept unchanged at 71 as granted by the Communal Award",
            "Increased from 71 to 147 in joint electorates",
            "Reduced from 71 to 50 in separate electorates",
            "Abolished entirely in favor of an open merit system"
        ],
        "correctIndex": 1,
        "explanation": "The Poona Pact (signed on 24 September 1932 at Yerwada Central Jail in Poona) abandoned separate electorates for the Depressed Classes in favor of joint electorates with reservation of seats, more than doubling their reserved representation in provincial legislatures from 71 (in Ramsay MacDonald's Communal Award) to 147 seats, and granting 18% of general seats in the Central Legislature.",
        "bookRef": "Pratik Nayak HFS10P4; B.L. Grover"
    },
    {
        "id": "prelims-pn-015",
        "question": "Who among the following was chosen by Mahatma Gandhi as the FIRST Individual Satyagrahi to launch the Individual Civil Disobedience movement in October 1940?",
        "options": [
            "Jawaharlal Nehru",
            "Acharya Vinoba Bhave",
            "Brahma Dutt",
            "Sardar Vallabhbhai Patel"
        ],
        "correctIndex": 1,
        "explanation": "In October 1940, Gandhi launched Individual Satyagraha to affirm the right of free speech against India's forced participation in WWII. Acharya Vinoba Bhave was chosen as the 1st Satyagrahi, Jawaharlal Nehru as the 2nd Satyagrahi, and Brahma Dutt as the 3rd Satyagrahi. They offered arrest after making anti-war speeches.",
        "bookRef": "Pratik Nayak HFS11P1; Spectrum Modern India"
    },
    {
        "id": "prelims-pn-016",
        "question": "During the Quit India Movement of 1942, in which of the following regions were 'Parallel Governments' (Prati Sarkar / Jatiya Sarkar) established?\n1. Ballia in Uttar Pradesh under Chittu Pandey\n2. Tamluk in Midnapore (Bengal) with Vidyut Vahinis\n3. Satara in Maharashtra under Nana Patil and Y.B. Chavan\nSelect the correct answer using the code below:",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 3,
        "explanation": "All three regions established heroic parallel governments during the Quit India Movement: Ballia (August 1942) for a week under Chittu Pandey; Tamluk (Midnapore, Dec 1942 - Sept 1944) as Jatiya Sarkar with cyclone relief and an armed Vidyut Vahini, where 73-year-old Matangini Hazra was martyred; and Satara (1943-45) as Prati Sarkar under Nana Patil and Y.B. Chavan, running Nyayadan Mandals and people's courts.",
        "bookRef": "Pratik Nayak HFS11P1; Bipan Chandra, Ch. 35"
    },
    {
        "id": "prelims-pn-017",
        "question": "Who among the following operated an underground, clandestine 'Congress Radio' broadcasting patriotic speeches and uncensored news during the Quit India Movement?",
        "options": [
            "Aruna Asaf Ali",
            "Usha Mehta",
            "Sucheta Kripalani",
            "Kalpana Datta"
        ],
        "correctIndex": 1,
        "explanation": "Usha Mehta, a 22-year-old student, along with associates like Babubhai Prasad, set up the secret Congress Radio that broadcast from varying locations across Bombay during August-November 1942, broadcasting recorded messages of Gandhi, Ram Manohar Lohia, and revolutionary news until the police raided their transmitter.",
        "bookRef": "Pratik Nayak HFS11P1; Spectrum Modern India"
    },
    {
        "id": "prelims-pn-018",
        "question": "The historic Red Fort trials of November 1945 were held against which of the following officers of the Indian National Army (INA)?",
        "options": [
            "Prem Kumar Sahgal, Gurbaksh Singh Dhillon, and Shah Nawaz Khan",
            "Mohan Singh, Niranjan Singh Gill, and Rash Behari Bose",
            "Lakshmi Sahgal, Pritilata Waddedar, and Bina Das",
            "Kartar Singh Sarabha, Sohan Singh Bhakna, and Gurdit Singh"
        ],
        "correctIndex": 0,
        "explanation": "The first and most famous INA court-martial was held at the Red Fort in Delhi against three senior officers together: a Hindu (Prem Kumar Sahgal), a Sikh (Gurbaksh Singh Dhillon), and a Muslim (Shah Nawaz Khan). Defended by the INA Defence Committee (Bhulabhai Desai, Tej Bahadur Sapru, Jawaharlal Nehru, Asaf Ali), their trial sparked massive all-India popular demonstrations, forcing Commander-in-Chief Claude Auchinleck to remit their prison sentences.",
        "bookRef": "Pratik Nayak HFS12P1; B.L. Grover"
    },
    {
        "id": "prelims-pn-019",
        "question": "The Royal Indian Navy (RIN) Mutiny of February 18, 1946 began on which British naval ship stationed in Bombay harbor?",
        "options": [
            "HMIS Vikrant",
            "HMIS Talwar",
            "HMIS Shivaji",
            "HMIS Rajput"
        ],
        "correctIndex": 1,
        "explanation": "The RIN Mutiny began on 18 February 1946 when 1,100 naval ratings on the signals training ship HMIS Talwar went on strike over racial insults, unpalatable food, and the arrest of rating B.C. Dutt (who had written 'Quit India' on the ship's walls). The mutiny spread across 78 ships, 20 shore establishments, and 20,000 ratings in Bombay, Karachi, and Calcutta.",
        "bookRef": "Pratik Nayak HFS12P1; Bipan Chandra, Ch. 36"
    },
    {
        "id": "prelims-pn-020",
        "question": "Which plan announced on June 3, 1947 laid down the procedural mechanism for the partition of British India and the immediate transfer of Dominion Status power to India and Pakistan?",
        "options": [
            "Wavell Plan",
            "Cabinet Mission Plan",
            "Dickie Bird Plan",
            "Mountbatten Plan"
        ],
        "correctIndex": 3,
        "explanation": "Lord Mountbatten announced the Mountbatten Plan (3rd June Plan) on 3 June 1947. It proposed the partition of India into two dominions (India and Pakistan), partition of Punjab and Bengal based on legislative voting, referendums in NWFP and Sylhet, a Boundary Commission (headed by Cyril Radcliffe), and advancing the transfer of power from June 1948 to 15 August 1947. It was enacted as the Indian Independence Act, 1947.",
        "bookRef": "Pratik Nayak HFS12P1; B.L. Grover"
    },

    # James Tod: Annals and Antiquities of Rajasthan
    {
        "id": "prelims-tod-001",
        "question": "According to the classical Agnikula origin myth documented by Col. James Tod, which four Rajput clans were created out of the sacrificial fire-pit on Mount Abu by the sage Vashistha?",
        "options": [
            "Pratihara, Paramara, Chalukya (Solanki), and Chahamana (Chauhan)",
            "Guhila, Rathore, Kachwaha, and Bhatti",
            "Sisodia, Tomara, Chandella, and Kalachuri",
            "Rashtrakuta, Sena, Pala, and Yadava"
        ],
        "correctIndex": 0,
        "explanation": "As recorded in the Prithviraj Raso and detailed by Col. James Tod in 'Annals and Antiquities of Rajasthan', the four Agnikula (fire-born) clans emerged from the sacrificial pit (homa-kunda) of sage Vashistha atop Mount Abu: Pratiharas (Parihars), Paramaras (Pawars), Chalukyas (Solankis), and Chahamanas (Chauhans). The Guhilas/Sisodias, Rathores, and Kachwahas trace their lineages to the Sun (Suryavansha).",
        "bookRef": "Col. James Tod, Annals and Antiquities of Rajasthan; Upinder Singh, Ch. 10"
    },
    {
        "id": "prelims-tod-002",
        "question": "The celebrated victory tower 'Vijay Stambha' (Tower of Victory) at Chittorgarh was erected by which ruler of Mewar to commemorate his triumph over the combined armies of Malwa and Gujarat?",
        "options": [
            "Bappa Rawal",
            "Rana Kumbha",
            "Rana Sanga",
            "Maharana Pratap"
        ],
        "correctIndex": 1,
        "explanation": "Rana Kumbha (reigned 1433–1468) of Mewar constructed the 9-storeyed, 37-metre-tall Vijay Stambha at Chittorgarh between 1440 and 1448 to commemorate his resounding victory over Sultan Mahmud Khalji of Malwa at the Battle of Sarangpur (1437). Rana Kumbha was also a master musicologist (author of Sangita-raja) and fortified 32 of Mewar's 84 forts.",
        "bookRef": "Col. James Tod, Annals and Antiquities of Rajasthan; Satish Chandra, Ch. 5"
    },
    {
        "id": "prelims-tod-003",
        "question": "In the medieval feudal system of Rajput states documented by James Tod, the hereditary land tenure granted to Rajput nobles (Thakurs) in exchange for feudal military service was known as:",
        "options": [
            "Iqta",
            "Patta (or Jagir)",
            "Watandar",
            "Polaj"
        ],
        "correctIndex": 1,
        "explanation": "In Rajput polities, the Patta (or Jagir) was the feudal title deed granted by the Maharana or Raja to clan chieftains and sardars (Thakurs). Pattayats enjoyed revenue rights over assigned villages in return for maintaining specified cavalry quotas (Chhatri chivalric obligation) for royal defense.",
        "bookRef": "Col. James Tod, Annals and Antiquities of Rajasthan; Satish Chandra"
    },

    # Yuval Noah Harari: Sapiens & Prehistory
    {
        "id": "prelims-har-001",
        "question": "In anthropological history, the 'Cognitive Revolution' (c. 70,000 BCE) is primarily distinguished by which evolutionary breakthrough of Homo sapiens?",
        "options": [
            "The mastery of fire and iron smelting",
            "The emergence of fictional language enabling cooperation based on shared collective myths",
            "The transition from hunting to commercial crop rotation",
            "The invention of the wheel and written cuneiform script"
        ],
        "correctIndex": 1,
        "explanation": "According to Yuval Noah Harari ('Sapiens') and evolutionary anthropologists, the Cognitive Revolution (around 70,000 years ago) was marked by neural mutations that allowed Homo sapiens to communicate about entities that do not physically exist (fictions, spirits, myths, and social rules). This enabled thousands of unrelated individuals to cooperate flexibly, unlike any other animal species.",
        "bookRef": "Yuval Noah Harari, Sapiens: A Brief History of Humankind; NCERT Themes in World History"
    },
    {
        "id": "prelims-har-002",
        "question": "Which Neolithic archaeological site situated in the Bolan Pass (Balochistan) provides the earliest evidence in the Indian subcontinent of the Agricultural Revolution, demonstrating mud-brick houses and cultivation of barley and wheat around 7000 BCE?",
        "options": [
            "Burzahom",
            "Mehrgarh",
            "Chirand",
            "Inamgaon"
        ],
        "correctIndex": 1,
        "explanation": "Mehrgarh, located on the Kachi plain near the Bolan Pass in Balochistan, is the premier early farming and pastoral site in South Asia (c. 7000–2500 BCE). Excavated by Jean-François Jarrige, it shows the earliest evidence of barley and wheat cultivation, sheep/goat domestication, and multi-room mud-brick granaries, marking the subcontinent's Neolithic transition.",
        "bookRef": "Yuval Noah Harari, Sapiens; Upinder Singh, Ch. 3; R.S. Sharma, Ch. 6"
    },

    # Mahatma Gandhi: An Autobiography (Experiments with Truth)
    {
        "id": "prelims-gan-001",
        "question": "Which book by John Ruskin exerted a profound transformation on Mahatma Gandhi in South Africa, leading him to establish the Phoenix Settlement in 1904 based on the principle of 'Sarvodaya'?",
        "options": [
            "The Kingdom of God Is Within You",
            "Unto This Last",
            "Civil Disobedience",
            "The Social Contract"
        ],
        "correctIndex": 1,
        "explanation": "In his autobiography 'The Story of My Experiments with Truth', Gandhi recounts reading John Ruskin's 'Unto This Last' during a 24-hour train ride from Johannesburg to Durban in 1904. It taught him three life principles: that the good of the individual is contained in the good of all; that a lawyer's work has the same value as the barber's (dignity of labor); and that the life of the tiller/craftsman is the life worth living. He immediately founded Phoenix Settlement.",
        "bookRef": "M.K. Gandhi, The Story of My Experiments with Truth; Bipan Chandra, Ch. 14"
    },
    {
        "id": "prelims-gan-002",
        "question": "What was the fundamental distinction that Mahatma Gandhi made between 'Passive Resistance' and 'Satyagraha'?",
        "options": [
            "Passive Resistance was meant only for political leaders, whereas Satyagraha was meant for religious ascetics.",
            "Passive Resistance was a weapon of the weak that permitted hatred and internal violence, whereas Satyagraha was a weapon of the morally courageous based on pure love and non-violence.",
            "Passive Resistance involved breaking constitutional laws, whereas Satyagraha remained strictly within judicial litigation.",
            "There was no conceptual difference; they were identical terms in Gujarati and English."
        ],
        "correctIndex": 1,
        "explanation": "Gandhi emphasized that Passive Resistance as practiced in the West was regarded as a weapon of the weak, which admitted of harassment and could embrace physical violence if circumstances allowed. Satyagraha ('holding firmly to truth' or 'soul-force'), by contrast, is a weapon of the strongest, excludes every form of hatred or malice, and aims to convert the opponent through voluntary self-suffering.",
        "bookRef": "M.K. Gandhi, Satyagraha in South Africa; Pratik Nayak HFS9"
    },
    {
        "id": "prelims-gan-003",
        "question": "In which mass agitation did Mahatma Gandhi employ a 'Hunger Strike' for the FIRST time in India?",
        "options": [
            "Champaran Satyagraha (1917)",
            "Ahmedabad Mill Strike (1918)",
            "Kheda Satyagraha (1918)",
            "Rowlatt Satyagraha (1919)"
        ],
        "correctIndex": 1,
        "explanation": "Gandhi undertook his first fast unto death (hunger strike) in India during the Ahmedabad Mill Strike in March 1918. Cotton mill owners sought to withdraw the plague bonus while workers demanded a 50% wage hike; Gandhi advised workers to strike peacefully for a 35% wage hike and fasted to prevent them from wavering. The dispute was submitted to an arbitration tribunal, which awarded the full 35% hike.",
        "bookRef": "M.K. Gandhi, Experiments with Truth; Bipan Chandra, Ch. 14"
    },

    # World History: Revolutions & Constitutions (Pratik Nayak & Norman Lowe)
    {
        "id": "prelims-wh-001",
        "question": "With reference to the French Revolution, the direct land tax levied on the Third Estate (commoners) in pre-revolutionary France was known as the:",
        "options": [
            "Tithe",
            "Taille",
            "Gabelle",
            "Corvée"
        ],
        "correctIndex": 1,
        "explanation": "In Ancien Régime France, the 'Taille' was the direct royal land tax levied primarily on peasants and commoners (the Third Estate), from which the First Estate (Clergy) and Second Estate (Nobility) were exempted. The 'Tithe' was the 10% agricultural tax collected by the Church; the 'Gabelle' was the state salt monopoly tax; and the 'Corvée' was unpaid forced road labor.",
        "bookRef": "Pratik Nayak WH_Fr; Norman Lowe, Ch. 1"
    },
    {
        "id": "prelims-wh-002",
        "question": "Regarding comparative constitutional law between the United States of America and India, consider the following statements:\n1. The American Federation is an 'indestructible union of indestructible states', whereas India is an 'indestructible union of destructible states'.\n2. The American Constitution provides for 'Due Process of Law', whereas Article 21 of the Indian Constitution originally provided for 'Procedure Established by Law'.\n3. Both the US President and the Indian President are directly elected by universal adult franchise.\nWhich of the statements given above is/are correct?",
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correctIndex": 0,
        "explanation": "Statements 1 and 2 are correct. In the US, states cannot be altered or seceded without state consent, whereas under Article 3 of the Indian Constitution, Parliament can reorganize state boundaries without state consent. In the US, 5th and 14th Amendments guarantee 'Due Process of Law' (substantive and procedural fairness), whereas Article 21 originally adopted the British concept of 'Procedure Established by Law'. Statement 3 is incorrect: the US President is elected via an Electoral College, and the Indian President is elected indirectly by an electoral college of elected MPs and MLAs.",
        "bookRef": "Pratik Nayak CmC_P1&2; Norman Lowe"
    },
    {
        "id": "prelims-wh-003",
        "question": "In his famous 'April Theses' of 1917, Vladimir Lenin outlined which of the following three radical slogans for the Bolshevik Party?",
        "options": [
            "Liberty, Equality, Fraternity",
            "Peace, Land, and Bread",
            "Blood and Iron",
            "One People, One Empire, One Leader"
        ],
        "correctIndex": 1,
        "explanation": "Upon returning to Petrograd from exile in April 1917, Vladimir Lenin issued his 'April Theses' with the core demands summarized in the slogan 'Peace, Land, and Bread' — immediate withdrawal from the imperialist World War I (Peace), transfer of all landed estates to the peasantry (Land), and food supplies for hungry industrial workers (Bread), paired with 'All Power to the Soviets!'.",
        "bookRef": "Pratik Nayak WH_Russian_Revolution; Norman Lowe, Ch. 14"
    }
]

# Append new questions ensuring unique IDs
existing_ids = set(q['id'] for q in prelims)
added_count = 0
for nq in new_questions:
    if nq['id'] not in existing_ids:
        prelims.append(nq)
        existing_ids.add(nq['id'])
        added_count += 1

with open('data/prelims-questions.json', 'w', encoding='utf-8') as f:
    json.dump(prelims, f, ensure_ascii=False, indent=2)

print(f"Added {added_count} new Prelims questions. Total now: {len(prelims)}")
