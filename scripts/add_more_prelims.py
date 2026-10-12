import json

with open('data/prelims-questions.json', 'r', encoding='utf-8') as f:
    prelims = json.load(f)

more_questions = [
    {
        "id": "prelims-pn-021",
        "question": "Regarding the 'Home Charges' that formed a prominent component of the economic Drain of Wealth from India to Britain, which of the following items were included?\n1. Salaries and pensions of officials of the India Office in London\n2. Guaranteed interest on British private capital invested in Indian railways\n3. Dividends payable to the East India Company stockholders\n4. Cost of British military expeditions and army stores purchased in England\nSelect the correct answer using the code below:",
        "options": [
            "1, 2 and 3 only",
            "1, 2 and 4 only",
            "2, 3 and 4 only",
            "1, 2, 3 and 4"
        ],
        "correctIndex": 3,
        "explanation": "Home Charges represented the annual payments made by the Government of India in London. Dadabhai Naoroji and R.C. Dutt showed that it encompassed: 1) Salaries, pensions, and allowances of the Secretary of State and India Office staff; 2) Guaranteed 5% return on capital invested in railways and public works; 3) Dividends on EIC stock (paid till 1874); 4) Military charges, furloughs, and purchase of British stores for imperial defense.",
        "bookRef": "Pratik Nayak HFS4P1; B.L. Grover; Dadabhai Naoroji, Poverty and Un-British Rule in India"
    },
    {
        "id": "prelims-pn-022",
        "question": "Which British constitutional statute established the 'Board of Control' of six commissioners in Great Britain to guide and supervise the civil, military, and revenue affairs of the East India Company, creating a 'Double Government' system?",
        "options": [
            "Regulating Act of 1773",
            "Pitt's India Act of 1784",
            "Charter Act of 1793",
            "Charter Act of 1813"
        ],
        "correctIndex": 1,
        "explanation": "Pitt's India Act of 1784 established the Board of Control (consisting of the Chancellor of the Exchequer, a Secretary of State, and four Privy Councillors) to supervise political, military, and revenue affairs, while commercial affairs remained with the Court of Directors. This system of Dual Control persisted until 1858.",
        "bookRef": "B.L. Grover, Ch. 4; Pratik Nayak HFS2P1"
    },
    {
        "id": "prelims-pn-023",
        "question": "Following the Jallianwala Bagh massacre (13 April 1919), the Indian National Congress appointed an independent Non-Official Inquiry Committee. Who among the following drafted the main report of this Congress committee?",
        "options": [
            "Motilal Nehru",
            "Mahatma Gandhi",
            "C.R. Das",
            "Madan Mohan Malaviya"
        ],
        "correctIndex": 1,
        "explanation": "The Congress appointed its own inquiry committee comprising Motilal Nehru (president), Mahatma Gandhi, C.R. Das, Abbas Tyabji, and M.R. Jayakar. Mahatma Gandhi collected witness testimonies and drafted the comprehensive report, which condemned General Dyer's brutality and exposed the atrocities of martial law under Michael O'Dwyer in Punjab.",
        "bookRef": "Pratik Nayak HFS9; Bipan Chandra, Ch. 15"
    },
    {
        "id": "prelims-pn-024",
        "question": "The Simon Commission (Indian Statutory Commission), appointed in November 1927, had seven British members of Parliament. Who among the following members later became the Prime Minister of the United Kingdom and oversaw the transfer of power to India in 1947?",
        "options": [
            "Lord Halifax",
            "Winston Churchill",
            "Clement Attlee",
            "Ramsay MacDonald"
        ],
        "correctIndex": 2,
        "explanation": "Clement Attlee (then a Labour MP) served as one of the seven members of the Simon Commission under Sir John Simon. Two decades later, as the Labour Prime Minister of Britain (1945–1951), Attlee announced Britain's decision to grant independence to India by June 1948.",
        "bookRef": "Pratik Nayak HFS10P3; Spectrum Modern India"
    },
    {
        "id": "prelims-pn-025",
        "question": "Prior to launching the Civil Disobedience Movement in 1930, Mahatma Gandhi presented an Eleven-Point Ultimatum to Viceroy Lord Irwin. Which of the following demands were included in Gandhi's 11 points?\n1. 50% reduction in land revenue and abolition of the salt tax\n2. 50% reduction in military expenditure and civil service salaries\n3. Total prohibition of intoxicants (alcohol)\n4. Immediate grant of Purna Swaraj (Complete Independence)\nSelect the correct answer using the code below:",
        "options": [
            "1, 2 and 3 only",
            "2, 3 and 4 only",
            "1, 3 and 4 only",
            "1, 2, 3 and 4"
        ],
        "correctIndex": 0,
        "explanation": "Gandhi's 11 Demands published in 'Young India' in January 1930 did NOT include immediate Purna Swaraj; instead, they addressed concrete economic and civil grievances: 50% reduction in land revenue, abolition of salt tax and government salt monopoly, 50% cut in military and civil salaries, total prohibition, release of political prisoners, protective tariff on foreign cloth, and reform of the CID.",
        "bookRef": "Pratik Nayak HFS10P3; Bipan Chandra, Ch. 21"
    },
    {
        "id": "prelims-pn-026",
        "question": "Following his resignation as Congress President in April 1939 due to ideological rifts with the Old Guard, Subhash Chandra Bose founded which political organisation within the Congress in May 1939?",
        "options": [
            "Congress Socialist Party",
            "Forward Bloc",
            "Independence for India League",
            "Revolutionary Socialist Party"
        ],
        "correctIndex": 1,
        "explanation": "Subhash Chandra Bose resigned as Congress President after the Tripuri crisis (where Govind Ballabh Pant moved a resolution binding Bose to Gandhi's nominated Working Committee) and founded the 'Forward Bloc' at Makur (Unnao, UP) in May 1939 as a radical, left-wing faction within the Congress to prepare India for a mass anti-imperialist struggle during the impending world war.",
        "bookRef": "Pratik Nayak HFS11P1; B.L. Grover"
    },
    {
        "id": "prelims-pn-027",
        "question": "With reference to the Rajagopalachari Formula (C.R. Formula) of 1944 designed to resolve the Congress-League deadlock, which of the following was proposed?",
        "options": [
            "Immediate creation of Pakistan prior to British departure",
            "Muslim League to endorse Congress demand for independence and cooperate in forming an interim government, with a post-war plebiscite in contiguous Muslim-majority districts",
            "Parity of Hindu and Muslim representation in the Viceroy's Executive Council without any plebiscite",
            "Division of India into three independent sovereign states: Hindustan, Pakistan, and Princely States"
        ],
        "correctIndex": 1,
        "explanation": "The C.R. Formula (drafted by C. Rajagopalachari and approved by Gandhi in March 1944) proposed that the Muslim League should endorse the demand for immediate independence and cooperate with the Congress in forming a provisional interim government. After the war, a commission would demarcate contiguous Muslim-majority districts in NW and NE India, where a plebiscite of all inhabitants (not just Muslims) would decide on separation, with common agreements on defence, commerce, and communications. Jinnah rejected it as offering a 'maimed, mutilated, and moth-eaten Pakistan'.",
        "bookRef": "Pratik Nayak HFS12P1; Bipan Chandra, Ch. 34"
    },
    {
        "id": "prelims-pn-028",
        "question": "The Cabinet Mission (March–May 1946) comprising Lord Pethick-Lawrence, Sir Stafford Cripps, and A.V. Alexander proposed which of the following constitutional arrangements?",
        "options": [
            "Acceptance of Jinnah's demand for a sovereign Pakistan",
            "A three-tier Union of India with limited central powers (Foreign Affairs, Defence, Communications) and grouping of provincial assemblies into Sections A, B, and C",
            "A unitary centralized government with no provincial autonomy",
            "Immediate partition of Bengal and Punjab under British supervision"
        ],
        "correctIndex": 1,
        "explanation": "The Cabinet Mission Plan rejected the demand for Pakistan and proposed a three-tier federation: a weak Union Government controlling Defence, Foreign Affairs, and Communications; three provincial groups (Section A: Hindu-majority provinces; Section B: Punjab, NWFP, Sind; Section C: Bengal and Assam); and an elected Constituent Assembly to frame the Constitution.",
        "bookRef": "Pratik Nayak HFS12P1; B.L. Grover"
    },
    {
        "id": "prelims-pn-029",
        "question": "On August 16, 1946, the All-India Muslim League under Muhammad Ali Jinnah called for 'Direct Action Day' to achieve Pakistan, leading to catastrophic communal killings known as the 'Great Calcutta Killings' in Bengal, where which politician was the Premier (Chief Minister)?",
        "options": [
            "A.K. Fazlul Huq",
            "Huseyn Shaheed Suhrawardy",
            "Khawaja Nazimuddin",
            "Liaquat Ali Khan"
        ],
        "correctIndex": 1,
        "explanation": "Huseyn Shaheed Suhrawardy was the Premier of the Muslim League ministry in Bengal during Direct Action Day on 16 August 1946. Widespread communal riots erupted in Calcutta, claiming an estimated 5,000 to 10,000 lives within 72 hours, triggering retaliatory violence in Noakhali, Bihar, and Punjab.",
        "bookRef": "Pratik Nayak HFS12P1; Sekhar Bandyopadhyay, Ch. 8"
    },
    {
        "id": "prelims-pn-030",
        "question": "In the Battle of Haldighati (18 June 1576), who was the commander-in-chief of Maharana Pratap's vanguard artillery and Afghan cavalry fighting valiantly against the Mughal imperial army under Man Singh of Amber?",
        "options": [
            "Hakim Khan Sur",
            "Rana Punja Bhil",
            "Bhim Singh",
            "Amar Singh"
        ],
        "correctIndex": 0,
        "explanation": "In the Battle of Haldighati (1576), Afghan warrior Hakim Khan Sur commanded Maharana Pratap's vanguard cavalry against Akbar's imperial army (ironically commanded by Rajput ruler Raja Man Singh of Amber). Punja Bhil commanded the Bhil archers defending the mountain passes. Maharana Pratap's horse Chetaka became immortalized for carrying his wounded master to safety.",
        "bookRef": "Col. James Tod, Annals and Antiquities of Rajasthan; Satish Chandra, Ch. 12"
    },
    {
        "id": "prelims-wh-004",
        "question": "Which Prussian statesman orchestrated the Unification of Germany through his strategy of 'Blood and Iron' (Blut und Eisen) and three planned wars against Denmark (1864), Austria (1866), and France (1870–71)?",
        "options": [
            "Klemens von Metternich",
            "Otto von Bismarck",
            "Kaiser Wilhelm II",
            "Helmut von Moltke"
        ],
        "correctIndex": 1,
        "explanation": "Otto von Bismarck, Minister President of Prussia (1862–1890), united Germany through Realpolitik and three decisive wars: the Danish War (1864 - seizing Schleswig-Holstein), the Austro-Prussian Seven Weeks' War (1866 - Battle of Sadowa), and the Franco-Prussian War (1870-71 - Battle of Sedan). The German Empire was proclaimed in the Hall of Mirrors at Versailles on 18 January 1871 under Kaiser Wilhelm I.",
        "bookRef": "Pratik Nayak WH_Vienna_Congress; Norman Lowe, Ch. 2"
    },
    {
        "id": "prelims-wh-005",
        "question": "During the Unification of Italy (Risorgimento), who were famously celebrated as the 'Soul', the 'Brain', and the 'Sword' of Italian unification respectively?",
        "options": [
            "Mazzini, Cavour, and Garibaldi",
            "Garibaldi, Mazzini, and Cavour",
            "Cavour, Garibaldi, and Victor Emmanuel",
            "Mazzini, Victor Emmanuel, and Cavour"
        ],
        "correctIndex": 0,
        "explanation": "Giuseppe Mazzini (founder of Young Italy in 1831) provided the revolutionary republican philosophy ('The Soul'); Count Camillo di Cavour (Prime Minister of Piedmont-Sardinia) orchestrated the master diplomatic alliances ('The Brain'); and Giuseppe Garibaldi (leader of the Red Shirts in the Expedition of the Thousand) led the military conquests ('The Sword'), uniting Italy under King Victor Emmanuel II.",
        "bookRef": "Pratik Nayak WH_Vienna_Congress; Norman Lowe, Ch. 2"
    }
]

existing_ids = set(q['id'] for q in prelims)
added_count = 0
for nq in more_questions:
    if nq['id'] not in existing_ids:
        prelims.append(nq)
        existing_ids.add(nq['id'])
        added_count += 1

with open('data/prelims-questions.json', 'w', encoding='utf-8') as f:
    json.dump(prelims, f, ensure_ascii=False, indent=2)

print(f"Added {added_count} more Prelims questions. Total now: {len(prelims)}")
