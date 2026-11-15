import json

with open('data/prelims-questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

existing_ids = set(q['id'] for q in questions)
print(f"Current count: {len(questions)}")

batch2 = [
    # Modern Freedom Movement
    {
        "id": "bipan_mod_001",
        "category": "modern",
        "categoryLabel": "Modern India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": True,
        "year": 2020,
        "bookRef": "Bipan Chandra, India's Struggle for Independence, Ch. 14",
        "question": "Which of the following was Mahatma Gandhi's first experiment with Satyagraha in India, undertaken to redress the grievances of indigo farmers bound by the oppressive Tinkathia system?",
        "options": [
            "Ahmedabad Mill Strike (1918)",
            "Champaran Satyagraha (1917)",
            "Kheda Satyagraha (1918)",
            "Rowlatt Satyagraha (1919)"
        ],
        "correctIndex": 1,
        "explanation": "Champaran Satyagraha (1917) in Bihar was Gandhi's first civil disobedience movement in India. Persuaded by local peasant Rajkumar Shukla, Gandhi investigated the plight of farmers forced under the Tinkathia system to cultivate indigo on 3/20th of their holdings, successfully securing an inquiry commission and 25% refund of illegal exactions.",
        "trap": "Champaran was First Civil Disobedience; Ahmedabad was First Hunger Strike; Kheda was First Non-Cooperation.",
        "topperTip": "Champaran 1917 (Tinkathia / Indigo) = First Civil Disobedience in India.",
        "periodId": "mahatma-gandhi",
        "examTag": "upsc"
    },
    {
        "id": "bipan_mod_002",
        "category": "modern",
        "categoryLabel": "Modern India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2023,
        "bookRef": "Bipan Chandra, Ch. 14; Spectrum, Ch. 15",
        "question": "In which movement did Mahatma Gandhi undertake his first hunger strike in India, mediating between mill owners and workers demanding a 35% plague bonus wage increase?",
        "options": [
            "Champaran Satyagraha (1917)",
            "Ahmedabad Mill Strike (1918)",
            "Kheda Satyagraha (1918)",
            "Non-Cooperation Movement (1920)"
        ],
        "correctIndex": 1,
        "explanation": "The Ahmedabad Mill Strike (March 1918) was Gandhi's first hunger strike in India. Supported by social worker Anasuya Sarabhai (sister of mill-owner Ambalal Sarabhai), Gandhi fasted to support workers demanding a 35% wage increase following the discontinuation of the plague bonus. The dispute was referred to a tribunal which granted the full 35% raise.",
        "trap": "Ahmedabad = First Hunger Strike. Kheda = First Non-Cooperation.",
        "topperTip": "Ahmedabad 1918 = First Hunger Strike + 35% wage hike (Anasuya Sarabhai).",
        "periodId": "mahatma-gandhi",
        "examTag": "upsc"
    },
    {
        "id": "bipan_mod_003",
        "category": "modern",
        "categoryLabel": "Modern India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "Bipan Chandra, Ch. 14; Spectrum, Ch. 15",
        "question": "In the Kheda Satyagraha (1918) in Gujarat, the primary demand of the Kunbi-Patidar peasants led by Gandhi and Vallabhbhai Patel was:",
        "options": [
            "The total abolition of the salt tax.",
            "The suspension and remission of land revenue under the Revenue Code because crops had yielded less than 25% (four annas) of normal output due to drought.",
            "The immediate withdrawal of British armed garrisons from Ahmedabad.",
            "The right to bear arms without a license."
        ],
        "correctIndex": 1,
        "explanation": "According to the colonial land revenue code, if the crop yield was less than 25% of normal, farmers were legally entitled to full remission of land revenue. When the British government refused remission despite severe crop failure, Gandhi launched the Kheda Satyagraha (his first true Non-Cooperation), where Sardar Patel mobilized the Patidar peasants to withhold revenue.",
        "trap": "Kheda demand was legal revenue remission due to crop failure under 25%, not complete independence.",
        "topperTip": "Kheda 1918 = First Non-Cooperation + Land revenue remission (Sardar Patel joined).",
        "periodId": "mahatma-gandhi",
        "examTag": "upsc"
    },
    {
        "id": "bipan_mod_004",
        "category": "modern",
        "categoryLabel": "Modern India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": True,
        "year": 2021,
        "bookRef": "Spectrum, Ch. 19; Bipan Chandra, Ch. 21",
        "question": "The 'Nehru Report' (1928), prepared by an All-Parties Conference committee headed by Motilal Nehru, recommended which constitutional status for India?",
        "options": [
            "Complete Independence (Purna Swaraj) outside the British Commonwealth.",
            "Dominion Status on the lines of Canada and Australia with universal adult suffrage and joint electorates.",
            "Continuation of Dyarchy with an expanded Governor-General's executive council.",
            "A separate state for minority communities in the north-west."
        ],
        "correctIndex": 1,
        "explanation": "Drafted as India's response to Lord Birkenhead's challenge, the Nehru Report (1928) outlined a democratic constitution based on: 1. Dominion Status for India; 2. Universal adult suffrage; 3. Rejection of separate electorates in favour of joint electorates with reservation for minorities only where they were in numerical minority; 4. Nineteen fundamental rights; 5. Responsible government at the centre and provinces.",
        "trap": "Nehru Report recommended Dominion Status; younger leaders (Jawaharlal Nehru & Subhas Bose) rebelled and demanded Purna Swaraj, which became official policy at Lahore in 1929.",
        "topperTip": "Nehru Report 1928 = Dominion Status + Joint electorates + 19 Fundamental Rights.",
        "periodId": "indian-freedom-struggle",
        "examTag": "upsc"
    },
    {
        "id": "bipan_mod_005",
        "category": "modern",
        "categoryLabel": "Modern India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": True,
        "year": 2022,
        "bookRef": "Spectrum, Ch. 20; Bipan Chandra, Ch. 23",
        "question": "The historic Poona Pact signed on 24 September 1932 between representatives of caste Hindus and Dr. B.R. Ambedkar resulted in:",
        "options": [
            "Acceptance of Ramsay MacDonald's Communal Award creating separate electorates for the Depressed Classes.",
            "Abandonment of separate electorates for the Depressed Classes in exchange for increased reserved seats in joint electorates (from 71 to 147 in provincial legislatures).",
            "The formation of the Independent Labour Party.",
            "The immediate entry of untouchables into all Vedic temples in Maharashtra."
        ],
        "correctIndex": 1,
        "explanation": "To prevent the political vivisection of Hindu society via separate electorates granted in Ramsay MacDonald's Communal Award (1932), Gandhi undertook a fast-unto-death in Yerwada Jail. The Poona Pact reconciled Ambedkar and Gandhi: separate electorates for the Depressed Classes were abandoned, but their reserved seats in provincial legislatures were more than doubled (from 71 under the Award to 147 under the Pact), with 18% reservation in the Central Assembly.",
        "trap": "Poona Pact ABOLISHED separate electorates for Depressed Classes and INCREASED their reserved seats within joint electorates.",
        "topperTip": "Poona Pact (Sept 1932) = Joint electorates retained + Reserved seats increased (71 → 147).",
        "periodId": "indian-freedom-struggle",
        "examTag": "upsc"
    },
    {
        "id": "bipan_mod_006",
        "category": "modern",
        "categoryLabel": "Modern India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": True,
        "year": 2021,
        "bookRef": "Spectrum, Ch. 22; Bipan Chandra, Ch. 27",
        "question": "Why did the Cripps Mission (March 1942) fail to secure the cooperation of Indian political parties during World War II?",
        "options": [
            "It proposed the immediate establishment of Pakistan without a referendum.",
            "It offered only post-war Dominion Status, retained British control over defense during wartime, and included a clause permitting provinces to opt out of the Indian Union.",
            "It insisted on making Persian the compulsory national language of India.",
            "It refused to grant amnesty to the leaders of the 1857 revolt."
        ],
        "correctIndex": 1,
        "explanation": "Sir Stafford Cripps' draft declaration failed because: 1. It offered Dominion Status only AFTER the war (Gandhi called it a 'post-dated cheque on a crashing bank'); 2. It gave provinces the right to secede from the Union, effectively granting Pakistan in embryo; 3. It kept defense strictly in British hands during the war; 4. Princely states were to be represented by nominated autocrats rather than elected people's representatives.",
        "trap": "Cripps offered Dominion status post-war with a provincial opt-out clause, which both Congress and Muslim League rejected for different reasons.",
        "topperTip": "Cripps Mission 1942 = 'Post-dated cheque on a crashing bank' (Gandhi).",
        "periodId": "indian-freedom-struggle",
        "examTag": "upsc"
    },
    {
        "id": "bipan_mod_007",
        "category": "modern",
        "categoryLabel": "Modern India",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "Spectrum, Ch. 24; Bipan Chandra, Ch. 28",
        "question": "The Royal Indian Navy (RIN) Mutiny of February 1946, which signaled the final collapse of British coercive authority in India, commenced on which naval ship in Bombay harbor?",
        "options": [
            "HMIS Vikrant",
            "HMIS Talwar",
            "HMIS Ganga",
            "HMIS Hindustan"
        ],
        "correctIndex": 1,
        "explanation": "On 18 February 1946, 1,100 naval ratings on the signal training ship HMIS Talwar in Bombay went on strike against racial discrimination, unpalatable food, and the arrest of B.C. Dutt (who had written 'Quit India' on the ship's walls). The mutiny spread to 78 ships, 20 shore establishments, and 20,000 ratings across Bombay, Karachi, and Calcutta.",
        "trap": "HMIS Talwar was the origin ship in Bombay; HMIS Hindustan was involved in intense gunfire in Karachi.",
        "topperTip": "RIN Mutiny 18 Feb 1946 = HMIS Talwar (Bombay) • B.C. Dutt & M.S. Khan.",
        "periodId": "independence-of-india",
        "examTag": "upsc"
    },

    # World History Questions (Norman Lowe)
    {
        "id": "world_lowe_003",
        "category": "world",
        "categoryLabel": "World History",
        "source": "UPSC CSE Mains/Prelims Standard",
        "isPyq": False,
        "year": 2023,
        "bookRef": "Norman Lowe, Ch. 4 (Unification of Italy)",
        "question": "In the Italian Risorgimento (Unification of Italy), which Italian patriot organized the volunteer military expedition of the 'Red Shirts' (Thousand / I Mille) in 1860, conquering the Kingdom of the Two Sicilies?",
        "options": [
            "Giuseppe Mazzini",
            "Count Camillo di Cavour",
            "Giuseppe Garibaldi",
            "Victor Emmanuel II"
        ],
        "correctIndex": 2,
        "explanation": "Giuseppe Garibaldi was the charismatic guerrilla leader of the Italian unification. In 1860, he led his volunteer army of 'Red Shirts' (Expedition of the Thousand) from Genoa to Sicily and Naples, overthrowing the Bourbon dynasty and handing over southern Italy to King Victor Emmanuel II of Piedmont-Sardinia to achieve a united Italy.",
        "trap": "Mazzini = Soul/Ideologue. Cavour = Brain/Diplomat. Garibaldi = Sword/Military hero. Victor Emmanuel II = Crown.",
        "topperTip": "Garibaldi = Red Shirts & Expedition of the Thousand (1860).",
        "periodId": "industrial-revolution-and-capitalism",
        "examTag": "upsc"
    },
    {
        "id": "world_lowe_004",
        "category": "world",
        "categoryLabel": "World History",
        "source": "UPSC CSE Mains/Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "Norman Lowe, Ch. 5 (Unification of Germany)",
        "question": "Otto von Bismarck unified Germany through his famous policy of 'Blood and Iron' (Blut und Eisen) by waging three calculated wars between 1864 and 1871. What was the correct chronological sequence of these three wars?",
        "options": [
            "Danish War (1864) → Austro-Prussian Seven Weeks' War (1866) → Franco-Prussian War (1870–71)",
            "Franco-Prussian War (1864) → Austro-Prussian War (1866) → Danish War (1870)",
            "Crimean War (1864) → Danish War (1866) → Austro-Prussian War (1870)",
            "Austro-Prussian War (1864) → Danish War (1866) → Franco-Prussian War (1870)"
        ],
        "correctIndex": 0,
        "explanation": "Bismarck orchestrated three swift wars: 1. Danish War (1864) alongside Austria over Schleswig-Holstein; 2. Austro-Prussian War (1866, Battle of Sadowa), expelling Austria from German affairs and forming the North German Confederation; 3. Franco-Prussian War (1870–71, Battle of Sedan), culminating in the proclamation of the German Empire at Versailles on 18 Jan 1871.",
        "trap": "Denmark (1864) → Austria (1866) → France (1870–71).",
        "topperTip": "Bismarck 3 Wars: Denmark (1864) → Austria (1866) → France (1870).",
        "periodId": "industrial-revolution-and-capitalism",
        "examTag": "upsc"
    },
    {
        "id": "world_lowe_005",
        "category": "world",
        "categoryLabel": "World History",
        "source": "UPSC CSE Mains/Prelims Standard",
        "isPyq": False,
        "year": 2023,
        "bookRef": "Norman Lowe, Ch. 16 (The Russian Revolution)",
        "question": "In the Russian Revolution of 1917, Vladimir Lenin issued his famous 'April Theses' upon returning from exile in Switzerland. Which of the following were the three primary slogans of the April Theses?",
        "options": [
            "'Liberty, Equality, Fraternity'",
            "'Peace, Land, and Bread' & 'All Power to the Soviets'",
            "'Blood, Toil, Tears, and Sweat'",
            "'Work, Family, Fatherland'"
        ],
        "correctIndex": 1,
        "explanation": "Lenin's April Theses (April 1917) called for: 1. Immediate withdrawal of Russia from World War I ('Peace'); 2. Confiscation of aristocratic landed estates and distribution to peasants ('Land'); 3. Control of food supply and factories by workers' committees ('Bread'); 4. Overthrow of the Provisional Government and transfer of state power ('All Power to the Soviets').",
        "trap": "'Peace, Land, Bread' addressed the three desperate needs of soldiers, peasants, and workers.",
        "topperTip": "Lenin's April Theses = 'Peace, Land, Bread' & 'All Power to the Soviets'.",
        "periodId": "russian-revolution",
        "examTag": "upsc"
    },
    {
        "id": "world_lowe_006",
        "category": "world",
        "categoryLabel": "World History",
        "source": "UPSC CSE Prelims Standard",
        "isPyq": False,
        "year": 2024,
        "bookRef": "Norman Lowe, Ch. 26 (Cold War & Non-Alignment)",
        "question": "The Afro-Asian Conference held at Bandung (Indonesia) in April 1955 was a landmark milestone that laid the foundations for which international diplomatic movement?",
        "options": [
            "The North Atlantic Treaty Organization (NATO)",
            "The Non-Aligned Movement (NAM)",
            "The Warsaw Pact",
            "The European Economic Community"
        ],
        "correctIndex": 1,
        "explanation": "The 1955 Bandung Conference, attended by 29 newly independent Asian and African nations (championed by Jawaharlal Nehru of India, Zhou Enlai of China, Sukarno of Indonesia, Gamal Abdel Nasser of Egypt, and Josip Broz Tito of Yugoslavia), formulated the 10 Bandung Principles of peaceful coexistence, leading directly to the founding of the Non-Aligned Movement (NAM) at Belgrade in 1961.",
        "trap": "Bandung 1955 laid the principles; Belgrade 1961 officially established the Non-Aligned Movement.",
        "topperTip": "Bandung Conference 1955 = Afro-Asian solidarity & foundation of NAM (Nehru, Nasser, Tito, Sukarno).",
        "periodId": "cold-war-and-decolonisation",
        "examTag": "upsc"
    }
]

# Append batch2 to questions
count_added = 0
for q in batch2:
    if q['id'] not in existing_ids:
        questions.append(q)
        existing_ids.add(q['id'])
        count_added += 1

print(f"Added {count_added} questions. Total prelims questions now: {len(questions)}")

with open('data/prelims-questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Saved prelims-questions.json successfully!")
