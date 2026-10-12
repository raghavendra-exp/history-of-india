import json

with open('data/mains-questions.json', 'r', encoding='utf-8') as f:
    mains = json.load(f)

print(f"Current Mains count: {len(mains)}")

new_mains = [
    {
        "id": "mains-pn-001",
        "question": "Lord Dalhousie is celebrated by imperial historians as the 'maker of modern India' but regarded by nationalists as the aggressive liquidator of Indian sovereignty. Critically examine his policies and dual legacy.",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Pratik Nayak HFS5P4; B.L. Grover, Ch. 12; Spectrum Modern India",
        "framework": {
            "intro": "Lord Dalhousie (Governor-General 1848–1856) occupies a paradoxically dual position in Indian historiography: as an energetic utilitarian modernizer who introduced railways, telegraphs, and postal systems, and as an aggressive imperial expansionist whose Doctrine of Lapse and annexationist drive dismantled native sovereignty and provoked the explosion of 1857.",
            "body": [
                {
                    "heading": "The Expansionist Destroyer of Sovereignty",
                    "points": [
                        "Doctrine of Lapse: Denied the traditional Hindu right of adopted heirs to inherit governance in subordinate states, annexing Satara (1848), Sambalpur (1849), Jhansi (1853), and Nagpur (1854).",
                        "Military Conquests: Annexed Punjab after the 2nd Anglo-Sikh War (1849) and Lower Burma (Pegu) after the 2nd Burmese War (1852).",
                        "Annexation of Awadh (1856): Deposed Nawab Wajid Ali Shah on the subjective pretext of 'misgovernance' based on Outram's report, alienating the Company's sepoy army (sepoys in Awadh were called 'peasants in uniform').",
                        "Abolition of Titles & Pensions: Withdrew titles and pensions of Nana Sahib (adopted son of Peshwa Baji Rao II), the Nawab of Carnatic, and the Raja of Tanjore, creating deep discontent among traditional elites."
                    ]
                },
                {
                    "heading": "The Utilitarian 'Maker of Modern India' & Imperial Infrastructure",
                    "points": [
                        "Railway Revolution: Authored the landmark Railway Minute of 1853; opened the first railway line from Bombay to Thane (1853), accelerating commercial integration.",
                        "Electric Telegraph & Postal System: Laid over 4,000 miles of telegraph lines under O'Shaughnessy; passed the Post Office Act of 1854 introducing uniform 2-pice postage across India.",
                        "Public Works Department (PWD): Established a separate central and provincial PWD, undertaking construction of the Grand Trunk Road and the Ganges Canal (opened 1854 under Proby Cautley).",
                        "Social & Educational Reforms: Enacted the Hindu Widows' Remarriage Act (1856) championed by Ishwar Chandra Vidyasagar; implemented Wood's Educational Despatch (1854) laying the architecture for Indian university education."
                    ]
                },
                {
                    "heading": "Historiographical Critique & Dual Purpose",
                    "points": [
                        "Marxist & Nationalist Critique: Modernizing infrastructure was designed to serve British metropolitan capitalism — extracting raw materials, opening markets for Manchester textiles, and enabling rapid troop mobility.",
                        "Direct Catalyst to 1857: His ruthless disregard for native political treaties and religious sensibilities directly ignited the widespread civil, peasant, and military rebellion of 1857."
                    ]
                }
            ],
            "conclusion": "Dalhousie did not build modern institutions for the welfare of Indians, but to forge an integrated, administratively coherent British imperial apparatus. In doing so, he ironically forged the material and communicative infrastructure that enabled Indians to build a unified nationwide anti-colonial national movement.",
            "diagramMapIdea": "Dual Flowchart: Left column showing Annexationist Policies (Doctrine of Lapse, Awadh) leading to 1857; Right column showing Infrastructure Modernization (Railways, Telegraph, PWD, Wood's Despatch) leading to National Unification."
        }
    },
    {
        "id": "mains-pn-002",
        "question": "Analyze the 'Safety Valve' theory regarding the origin of the Indian National Congress. How does modern historiography refute this myth in favor of the 'Lightning Conductor' perspective?",
        "marks": 10,
        "wordLimit": 150,
        "bookRef": "Pratik Nayak HFS7P1; Bipan Chandra, Ch. 4; B.L. Grover",
        "framework": {
            "intro": "The foundation of the Indian National Congress (INC) in December 1885 at Bombay has been the subject of intense historiographical debate, centered on whether it was a British-engineered 'Safety Valve' to preempt peasant rebellion or the conscious culmination of nascent Indian political consciousness.",
            "body": [
                {
                    "heading": "The 'Safety Valve' Myth & Its Proponents",
                    "points": [
                        "Origin of the Theory: Propounded by Extremist leader Lala Lajpat Rai (1916) in 'Young India' and Marxist historian R. Palme Dutt ('India Today').",
                        "The Argument: Claimed that retired British civil servant Allan Octavian Hume acted as a tool of Viceroy Lord Dufferin to create a harmless debating forum that would vent boiling Indian peasant discontent, purportedly documented in seven secret CID volume reports.",
                        "Flaws in the Theory: Modern archival research by Bipan Chandra revealed that Dufferin had never sanctioned Hume's political scheme, and the mysterious 'seven volumes of secret police reports' existed nowhere in the official archives."
                    ]
                },
                {
                    "heading": "The 'Lightning Conductor' Reality of Early Nationalists",
                    "points": [
                        "Gokhale's Clarification: Gopal Krishna Gokhale remarked in 1913 that if an Indian had initiated an all-India political movement in 1885, the colonial state would have suppressed it instantly; Hume was consciously utilized as a 'lightning conductor' to deflect imperial hostility.",
                        "Dufferin's Rapid Estrangement: Within three years, Dufferin grew openly hostile, ridiculing the Congress at the 1888 St. Andrew's Day dinner as a 'microscopic minority' of babus and barring government servants from attending."
                    ]
                }
            ],
            "conclusion": "The INC was not the conspiratorial byproduct of British statecraft but the natural convergence of earlier political associations (Indian Association, Poona Sarvajanik Sabha, Madras Mahajana Sabha). Hume was the catalyst, but Indian political maturity was the substance.",
            "diagramMapIdea": "Comparative Diagram: Left side 'Safety Valve Myth' (British Bureaucracy -> Hume -> Congress -> Dissipation of Peasant Anger); Right side 'Lightning Conductor Reality' (Pre-Congress Associations -> Nationalist Leaders using Hume to deflect State Wrath -> All-India Organization)."
        }
    },
    {
        "id": "mains-pn-003",
        "question": "Examine the economic critique of British rule propounded by early nationalists. How did the 'Drain of Wealth' theory awaken national consciousness and dismantle the moral legitimacy of the colonial Raj?",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Pratik Nayak HFS4P1; Dadabhai Naoroji; Bipan Chandra, Ch. 7",
        "framework": {
            "intro": "The early Moderate nationalists (1885–1905), led by Dadabhai Naoroji, Romesh Chunder Dutt, M.G. Ranade, and G.V. Joshi, pioneered a devastating, statistically grounded economic critique of British colonialism. By formulating the 'Drain of Wealth' theory, they laid the intellectual foundation of modern Indian anti-imperialist nationalism.",
            "body": [
                {
                    "heading": "Conceptual Architecture of the 'Drain of Wealth'",
                    "points": [
                        "Dadabhai Naoroji's Formulation: In 'Poverty and Un-British Rule in India' (1867 paper 'England's Debt to India'), Naoroji conceptualized the drain as the unrequited export of India's national product for which India received no financial or economic returns.",
                        "Components of the Drain: Home Charges (salaries/pensions of India Office officials, interest on public debt, guaranteed 5% return on railways), remittance of private profits by British merchants, and foreign military expenditure.",
                        "R.C. Dutt's Agrarian Analysis: In 'Economic History of India', Dutt calculated that over one-third of India's annual net revenues flowed out to Britain, bleeding India's capital formation dry.",
                        "Mechanisms of Impoverishment: The drain prevented internal capital reinvestment, destroyed indigenous handicraft industries (de-industrialization), forced commercialization of agriculture, and precipitated catastrophic recurring famines."
                    ]
                },
                {
                    "heading": "Political Impact: Awakening National Consciousness",
                    "points": [
                        "Dismantling the 'Benevolent Despotism' Myth: The British claimed their rule was bringing civilizing peace, good governance, and development. The economic critique exposed that the Raj was fundamentally an extractive colonial vampire ('bleeding India white').",
                        "Unifying Pan-Indian Sentiment: Economic exploitation affected peasants, artisans, middle classes, and native merchants alike, providing an all-India material commonality that transcended caste, religious, and linguistic fault lines.",
                        "Shifting Nationalist Demands: Transformed politics from early piecemeal petitions into structural demands for fiscal autonomy, protectionist tariffs, and Swaraj (self-rule declared by Naoroji at Calcutta in 1906)."
                    ]
                }
            ],
            "conclusion": "The economic critique was the early nationalists' greatest contribution. Though the Moderates lacked a mass agitation strategy, their economic exposure destroyed the moral hegemony of the British Raj and provided the ideological ammunition for the Gandhian mass movements that followed.",
            "diagramMapIdea": "Concentric Flowchart: Central Hub 'Indian Agrarian & Craft Production' -> Three Drainage Pipes (Home Charges, Guaranteed Railway Interest, Commodity Surplus) -> Outflow to London Metropolis -> Consequence Hub (Pauperization, Famines, De-industrialization) -> Catalyst to National Awaking."
        }
    },
    {
        "id": "mains-pn-004",
        "question": "Compare and contrast the ideological orientations, operational methods, and social base of Revolutionary Terrorism in Phase I (1907–1917) and Revolutionary Socialism in Phase II (1920s–1930s).",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Pratik Nayak HFS10P2; B.L. Grover; Bipan Chandra, Ch. 12 & 20",
        "framework": {
            "intro": "The Indian revolutionary movement erupted in two distinct temporal waves: Phase I (1907–1917) following the partition of Bengal, and Phase II (1920s–1930s) following the suspension of the Non-Cooperation Movement. While both shared supreme patriotism and self-sacrifice, they differed fundamentally in ideology, social program, and operational strategy.",
            "body": [
                {
                    "heading": "Ideological Divergence: Revivalist Patriotism vs. Scientific Socialism",
                    "points": [
                        "Phase I Ideology: Strongly influenced by religious nationalism and heroic self-immolation. Secret societies (Anushilan Samiti, Abhinav Bharat) drew inspiration from the Bhagavad Gita, Bankim Chandra's Anandamath, and Kali worship, occasionally alienating non-Hindu minorities.",
                        "Phase II Ideology: Embraced Marxist-Leninist scientific socialism, working-class solidarity, and internationalism. Bhagat Singh's essay 'Why I Am an Atheist' (1930) broke decisively with religious symbolism. HRA was renamed HSRA (1928) to declare the goal of ending all forms of human exploitation (man by man, nation by nation)."
                    ]
                },
                {
                    "heading": "Operational Strategy: Individual Assassination vs. Mass Consciousness",
                    "points": [
                        "Phase I Methods: Secret conspiracies, bomb manufacturing, targeted assassination of oppressive British officials (Kingsford, Curzon Wyllie, Jackson), and dacoities (Swadeshi dacoities) to fund weapons; overseas international ties (Ghadar Party in US/Canada, Berlin Committee).",
                        "Phase II Methods: Propagandist actions designed to awaken the masses. Central Assembly Bombing (1929) used harmless smoke bombs and leaflets 'to make the deaf hear'. Court trials were utilized as national political rostrums to propagate socialist manifestos. Mass mobilization of youth, workers, and peasants through organizations like the Naujawan Bharat Sabha and Kirti Kisan Party."
                    ]
                },
                {
                    "heading": "Role of Women Revolutionaries",
                    "points": [
                        "Phase I: Women largely played auxiliary roles (sheltering absconders, carrying secret couriers, e.g., Sarala Devi Chaudhurani, Madam Bhikaji Cama).",
                        "Phase II: Women actively participated in direct combat and guerrilla raids (Pritilata Waddedar leading the Pahartali Club raid, Kalpana Datta, Bina Das shooting Governor Jackson, Suniti Choudhury and Santi Ghosh)."
                    ]
                }
            ],
            "conclusion": "Phase I demonstrated that Indians were prepared to die for freedom, shattering the myth of passive submissiveness; Phase II infused the national consciousness with a vision of sovereign socio-economic equality, fundamentally shaping the socialist orientation of the post-independence Indian Republic.",
            "diagramMapIdea": "Comparative Table Matrix contrasting Phase I vs Phase II across: Ideology (Religious Nationalism vs Scientific Socialism), Primary Target (Tyrannical Officials vs Imperialist System), Role of Religion, Role of Women, and Mass Outreach."
        }
    },
    {
        "id": "mains-pn-005",
        "question": "Discuss the strategy of the Swarajists within the Indian National Congress. Were they mere constitutional obstructionists, or did they effectively bridge the political vacuum between mass movements?",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Pratik Nayak HFS10P1; Bipan Chandra, Ch. 19; Spectrum Modern India",
        "framework": {
            "intro": "Following Mahatma Gandhi's sudden withdrawal of the Non-Cooperation Movement in February 1922 and his subsequent imprisonment, the nationalist movement faced acute demoralization and a political vacuum. In this context, C.R. Das and Motilal Nehru formed the Congress-Khilafat Swarajya Party (1923) to carry the struggle into legislative councils.",
            "body": [
                {
                    "heading": "The Swarajist Rationale: 'End or Mend' the Councils",
                    "points": [
                        "Boycott of Boycott: Swarajists argued that council boycott during an ebb of mass movement allowed loyalist and communal elements to capture legislative power unchallenged.",
                        "Wrecking from Within: Proposed entering the councils under the 1919 Act to throw out budgets, obstruct reactionary bills, expose the sham nature of dyarchy, and transform councils into rostrums of anti-colonial agitation."
                    ]
                },
                {
                    "heading": "Major Achievements of the Swaraj Party",
                    "points": [
                        "Legislative Deadlocks: Repeatedly outvoted the government on budget demands, rejected repressive bills (Public Safety Bill), and appointed the Muddiman Committee (1924) to expose dyarchy's administrative failures.",
                        "Symbolic Parliamentary Triumph: Elected Vithalbhai J. Patel as the first Indian President (Speaker) of the Central Legislative Assembly in 1925, asserting parliamentary dignity.",
                        "Keeping National Agitation Alive: Kept public enthusiasm, press debate, and political confrontation burning at a time when the masses were exhausted and incapable of immediate civil disobedience."
                    ]
                },
                {
                    "heading": "Inherent Limitations & Degeneration",
                    "points": [
                        "Inability to Sustain Total Obstruction: Parliamentary rules and bureaucratic vetoes limited disruption; without an active mass movement outside, parliamentary politics became an end in itself.",
                        "Rise of Responsivism: Internal splits emerged with leaders like N.C. Kelkar, M.R. Jayakar, and Madan Mohan Malaviya forming the Responsivist faction to accept government offices and defend Hindu communal interests."
                    ]
                }
            ],
            "conclusion": "The Swarajists were far more than obstructionists; they functioned as an indispensable tactical rearguard. By carrying the anti-colonial banner into the legislative arena, they prevented apathy, sustained political momentum, and paved the way for the radical resurgence of the Simon Commission boycott and Civil Disobedience.",
            "diagramMapIdea": "Cycle Diagram showing: Ebb of Mass Struggle (1922) -> Political Vacuum -> Swarajist Council Entry Strategy -> Exposing Dyarchy & Defeating Official Bills -> Sustaining Momentum until Simon Commission Boycott (1927) & Purna Swaraj."
        }
    },
    {
        "id": "mains-pn-006",
        "question": "The Karachi Resolution of 1931 was a defining milestone that transitioned the Indian national movement from a purely political struggle for transfer of power into a radical socio-economic program. Elaborate.",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Pratik Nayak HFS10P4; B.L. Grover; Bipan Chandra, Ch. 22",
        "framework": {
            "intro": "The Karachi Session of the Indian National Congress (March 1931), presided over by Sardar Vallabhbhai Patel in the immediate shadow of Bhagat Singh's martyrdom and the Gandhi-Irwin Pact, is universally acknowledged as the ideological watershed of modern Indian constitutionalism, articulating for the first time what 'Swaraj' would mean for the starving millions.",
            "body": [
                {
                    "heading": "Socio-Economic Commitments of the Karachi Resolution",
                    "points": [
                        "Pioneered by Jawaharlal Nehru: Drafted by Nehru in consultation with Gandhi, the Resolution on Fundamental Rights and Economic Programme gave concrete socio-economic flesh to political independence.",
                        "Charter of Fundamental Rights: Free speech, free press, freedom of assembly, universal adult franchise, equality before law irrespective of caste, creed, or sex, and religious neutrality of the State (secularism).",
                        "Labor Rights & Welfare: Legal protection of trade unions, living wages, limitation of working hours, healthy working conditions, abolition of child labor, and state protection against old age and unemployment.",
                        "Agrarian Relief: Substantial reduction in land revenue and agricultural rent, exemption of uneconomic holdings from rent, abolition of feudal levies, and relief from rural agricultural indebtedness."
                    ]
                },
                {
                    "heading": "Economic Vision & Foundation of Independent India's Constitution",
                    "points": [
                        "State Ownership of Key Resources: Mandated that the state shall own or control key industries, mines, railways, waterways, shipping, and mineral resources (laying the blueprint for the post-1947 Mixed Economy and Five-Year Plans).",
                        "Precursor to the Indian Constitution: The Karachi Resolution formed the direct foundational draft for both Part III (Fundamental Rights) and Part IV (Directive Principles of State Policy) of the Constitution of India."
                    ]
                }
            ],
            "conclusion": "Karachi 1931 redefined the freedom struggle from a transfer-of-power arrangement between British and Indian elites into a transformative social contract. It assured peasants and workers that Swaraj would mean the eradication of hunger, inequality, and exploitation.",
            "diagramMapIdea": "Mind Map connecting 'Karachi Resolution 1931' to three pillars: Civil Liberties (Part III Fundamental Rights), Agrarian/Labor Welfare (Part IV Directive Principles), and State Economic Control (Mixed Economy & Planning Commission)."
        }
    },
    {
        "id": "mains-pn-007",
        "question": "Why did the nationwide rebellion of 1857 fail to overthrow British power, whereas the Quit India Movement of 1942, despite the arrest of its top leadership within hours, shattered the foundations of the colonial state?",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Pratik Nayak HFS6P2 & HFS11P1; B.L. Grover; Bipan Chandra",
        "framework": {
            "intro": "Both the Revolt of 1857 and the Quit India Movement of 1942 represented monumental, spontaneous mass uprisings that shook the British Empire to its core. Yet while 1857 was crushed by colonial military forces, 1942 inflicted an irreparable structural blow that compelled the British to depart within five years.",
            "body": [
                {
                    "heading": "Structural Weaknesses of 1857",
                    "points": [
                        "Lack of All-India Scope & Social Unity: Confined largely to North and Central India; Bengal, Bombay, Madras, and Punjab remained passive or actively assisted the British (Sikh and Gurkha regiments).",
                        "Traditional Backward-Looking Leadership: Led by deposed feudal princes and taluqdars looking backward to restore past feudal privileges, lacking a unified forward-looking socio-political vision.",
                        "Modern Intelligentsia's Alienation: The newly educated Indian middle class viewed the rebels as feudal reactionaries and supported the British, believing the Raj was modernizing India.",
                        "Military & Technological Asymmetry: Rebels were equipped with archaic weapons, lacked telegraph coordination, unified command, and logistical depth compared to British reinforcements."
                    ]
                },
                {
                    "heading": "Transformative Strengths of Quit India 1942",
                    "points": [
                        "Pan-Indian Nationalist Consciousness: Decades of Gandhian mass mobilization (Non-Cooperation, Civil Disobedience) had forged an irreversible all-India national consciousness across urban and rural masses.",
                        "Decentralized Organic Leadership: Operation Zero Hour arrested Gandhi and the Congress Working Committee overnight, but the masses took the initiative, operating under local leadership, socialist youth (Aruna Asaf Ali, JP, Lohia), and parallel governments (Ballia, Tamluk, Satara).",
                        "Erosion of the State's Coercive Loyalty: The police, civil bureaucracy, and Indian army began demonstrating sympathy for the nationalists, culminating in the 1946 INA trials and RIN Mutiny.",
                        "Global Geopolitical Weakness: Britain was economically ruined by World War II, international pressure from the US mounted, and post-war Britain lacked the military willpower or financial resources to hold 400 million hostile subjects by force."
                    ]
                }
            ],
            "conclusion": "1857 was a heroic but fragmented revolt of a dying feudal order against an advancing colonial power; 1942 was the conscious, unstoppable rebellion of an awakened modern nation against a fatally weakened imperial master.",
            "diagramMapIdea": "Comparative Flowchart contrasting 1857 (Feudal leadership, regional fragmentation, technological inferiority -> Military suppression) vs 1942 (Modern national consciousness, decentralized masses, post-WWII imperial exhaustion -> Transfer of power)."
        }
    },
    {
        "id": "mains-tod-001",
        "question": "Col. James Tod's 'Annals and Antiquities of Rajasthan' immortalized the Rajput chivalric ethos, yet modern historians note the limitations of clan-based feudal polities. Critically analyze the nature of Rajput statecraft and resistance.",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Col. James Tod, Annals and Antiquities of Rajasthan; Satish Chandra, Ch. 12; Upinder Singh",
        "framework": {
            "intro": "Lieut.-Col. James Tod's monumental work 'Annals and Antiquities of Rajasthan' (1829–1832) romanticized the Rajput clans as knights of chivalry, immortalizing the resistance of Mewar under Maharana Pratap against imperial hegemony. However, modern historical scholarship critically unpacks both the strengths of their martial ethos and the structural vulnerabilities of clan-based feudal statecraft.",
            "body": [
                {
                    "heading": "The Heroic Dimensions: Martial Ethos & Resistance",
                    "points": [
                        "Uncompromising Independence of Mewar: Under Bappa Rawal, Rana Kumbha, Rana Sanga, and Maharana Pratap, the Guhila-Sisodias maintained heroic resistance against Delhi Sultanate and Mughal dominance.",
                        "Rituals of Honor: The traditions of Jauhar (collective female self-immolation) and Saka (saffron death-charge) in sieges of Chittorgarh (1303, 1535, 1568) symbolized a cultural code that prioritized honor over subjugation.",
                        "Architectural & Defensive Masterpieces: Rana Kumbha's fortification of 32 hill forts (Kumbhalgarh's impenetrable 36-km wall, Chittor's Vijay Stambha) provided strategic depth against imperial cavalry."
                    ]
                },
                {
                    "heading": "Structural Vulnerabilities: Clan Fractures & Feudal Instability",
                    "points": [
                        "Clan Particularism: Rajput states were based on bloodline clans (Guhila, Rathore, Kachwaha, Chauhan) rather than a centralized territorial state. Intense inter-clan rivalry and blood feuds prevented the formation of a permanent unified Rajput confederacy.",
                        "Feudal Independence of Thakurs: The Patta land tenure granted near-autonomous power to feudal barons, weakening royal central authority and preventing cohesive military modernizations (such as infantry discipline and field artillery).",
                        "Mughal Integration vs. Rajput Disunity: Akbar capitalized on these fractures by offering mansabdari alliances to the Kachwahas of Amber, Rathores of Marwar, and Bhattis, isolating Mewar and deploying Rajput generals (Raja Man Singh) against fellow Rajputs (Maharana Pratap at Haldighati)."
                    ]
                }
            ],
            "conclusion": "Tod's chronicle rightfully celebrated the unmatched individual valour and moral integrity of Rajput warriors. Yet their inability to transcend clan particularism and institutionalize modern bureaucratic and military structures ultimately rendered their feudal polities subordinate to centralized imperial powers.",
            "diagramMapIdea": "Structural Matrix: Upper quadrant showing Martial Strengths (Heroic Chivalry, Mountain Fortresses, Mewar Ideology); Lower quadrant showing Feudal Flaws (Clan Rivalries, Decentralized Patta system, Lack of Artillery integration -> Imperial Vassalage)."
        }
    },
    {
        "id": "mains-har-001",
        "question": "In his work 'Sapiens', Yuval Noah Harari characterizes the Agricultural Revolution as 'history's biggest fraud'. Evaluate this assessment in the context of the Neolithic transition in South Asia, drawing on archaeological evidence from Mehrgarh.",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Yuval Noah Harari, Sapiens; Upinder Singh, Ch. 3; R.S. Sharma, Ch. 6",
        "framework": {
            "intro": "In 'Sapiens: A Brief History of Humankind', Yuval Noah Harari provokes conventional wisdom by describing the Agricultural Revolution (c. 10,000 BCE) as 'history's biggest fraud' — arguing that while it drastically expanded the collective biomass and population of Homo sapiens, it severely degraded the physical health, dietary variety, and individual liberty of the average farmer compared to the Paleolithic forager.",
            "body": [
                {
                    "heading": "The 'Fraud' Argument: Nutritional & Social Costs",
                    "points": [
                        "Monotonous Diet & Health Degradation: Foragers consumed dozens of diverse wild plants, berries, and game; early farmers subsisted predominantly on a single carbohydrate crop (wheat, barley, or rice), resulting in nutritional deficiencies, rickets, and tooth decay.",
                        "Back-breaking Repetitive Labor: Skeletal analysis of Neolithic populations demonstrates spinal degeneration, arthritis, and slipped discs caused by constant bending, tilling, weeding, and pestle-grinding.",
                        "Zoonotic Diseases & Vulnerability: Living in permanent crowded mud-brick settlements adjacent to domesticated livestock exposed humans to zoonotic epidemics (smallpox, tuberculosis, malaria), while monsoonal crop failures caused catastrophic famines.",
                        "Emergence of Inequality: Private ownership of land, granaries, and cattle generated rigid socio-economic stratification, patriarchy, and predatory ruling elites extracting surpluses from impoverished cultivators."
                    ]
                },
                {
                    "heading": "Archaeological Evidence from Mehrgarh (Balochistan)",
                    "points": [
                        "Earliest South Asian Neolithic (c. 7000 BCE): Excavations at Mehrgarh by Jarrige demonstrate the transition from hunting wild gazelle to domesticating humped cattle (Bos indicus), sheep, and cultivating six-row barley and einkorn wheat.",
                        "Technological Specialization: Multi-room mud-brick granaries, bone tools, ground-stone axes, and turquoise/steatite bead manufacture emerged, confirming permanent sedentism.",
                        "The Demographic Trade-off: Mehrgarh provided the economic surplus, demographic density, and craft specialization that made state formation and the subsequent urban flowering of the Indus Valley Civilization possible."
                    ]
                }
            ],
            "conclusion": "While the Neolithic transition was an existential trap for the individual peasant, it was the non-negotiable springboard for human civilization. Without the agrarian surplus established at sites like Mehrgarh, complex societies, epigraphy, mathematics, philosophy, and cities could never have arisen.",
            "diagramMapIdea": "Comparative Balance Sheet: Left Side 'Individual Costs' (Dietary Narrowing, Spinal Strain, Zoonotic Epidemics, Emergence of Inequality); Right Side 'Civilizational Gains' (Demographic Expansion, Permanent Granaries, Craft Specialization -> Indus Urbanization)."
        }
    },
    {
        "id": "mains-gan-001",
        "question": "Distinguish between Mahatma Gandhi's concept of 'Satyagraha' and Western 'Passive Resistance'. How did Gandhi's constructive programme serve as the non-violent bedrock of moral nation-building?",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "M.K. Gandhi, The Story of My Experiments with Truth; Bipan Chandra, Ch. 14; Pratik Nayak HFS9",
        "framework": {
            "intro": "In his autobiography 'The Story of My Experiments with Truth' and 'Satyagraha in South Africa', Mahatma Gandhi drew a fundamental, non-negotiable distinction between Western 'Passive Resistance' and his philosophy of 'Satyagraha' (Truth-Force). For Gandhi, political freedom (Swaraj) was meaningless without moral regeneration through the Constructive Programme.",
            "body": [
                {
                    "heading": "Philosophical Distinction: Satyagraha vs. Passive Resistance",
                    "points": [
                        "Moral Basis & Inner Motive: Passive resistance is a weapon of the weak that permits malice, internal hatred, and tactical violence if arms become available; Satyagraha is a weapon of the morally courageous based on absolute Ahimsa (non-violence) and love for the adversary.",
                        "Method of Conflict Resolution: Passive resistance aims to coerce or embarrass the opponent into surrender; Satyagraha aims to convert the conscience of the opponent through voluntary self-suffering (Tapasya).",
                        "Compromise and Truth: A Satyagrahi never compromises on truth or moral principles, yet is always ready for honorable dialogue, distinguishing between the evil system (which must be destroyed) and the evil-doer (who must be redeemed)."
                    ]
                },
                {
                    "heading": "The Constructive Programme: Bedrock of Mass Struggle",
                    "points": [
                        "Sustaining Energy During Truce Phases: In the 'Struggle-Truce-Struggle' (S-T-S) strategy of the Gandhian movement, mass civil disobedience could not continue indefinitely. The Constructive Programme mobilized millions during inactive phases.",
                        "Economic Decentralization (Khadi & Charkha): The spinning wheel was not merely cotton production, but economic independence from Manchester, self-reliance for impoverished rural households, and the physical symbol of national unity.",
                        "Social Reformation: Eradication of Untouchability (Harijan upliftment, temple entry) and Hindu-Muslim unity aimed to dismantle internal social hierarchies, preventing the colonial state from exploiting communal divisions.",
                        "Nai Talim (Basic Education): Promoted vocational, mother-tongue education rooted in rural handicrafts rather than colonial clerk-producing rote literacy."
                    ]
                }
            ],
            "conclusion": "Satyagraha was not merely an anti-imperialist political tactic, but an ethical philosophy of living. The Constructive Programme ensured that while the national movement was fighting the British Raj outwardly, it was building an egalitarian, self-reliant, and spiritually resilient Indian nation inwardly.",
            "diagramMapIdea": "Dual Pillar Diagram: Left Pillar 'Political Agitation' (Non-Cooperation, Civil Disobedience, Quit India); Right Pillar 'Constructive Programme' (Khadi, Removal of Untouchability, Communal Unity, Nai Talim); Both anchored on the Foundation of 'Satya & Ahimsa'."
        }
    }
]

existing_ids = set(m['id'] for m in mains)
added_count = 0
for nm in new_mains:
    if nm['id'] not in existing_ids:
        mains.append(nm)
        existing_ids.add(nm['id'])
        added_count += 1

with open('data/mains-questions.json', 'w', encoding='utf-8') as f:
    json.dump(mains, f, ensure_ascii=False, indent=2)

print(f"Added {added_count} new Mains model questions. Total now: {len(mains)}")
