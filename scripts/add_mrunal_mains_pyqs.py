import json

with open('data/mains-questions.json', 'r', encoding='utf-8') as f:
    mains_questions = json.load(f)

existing_ids = set(q['id'] for q in mains_questions)
print(f"Current Mains count: {len(mains_questions)}")

MRUNAL_MAINS_PYQS = [
    # 2023 GS-1 QUESTIONS
    {
        "id": "mains_pyq_2023_01",
        "periodId": "vedic-age",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2023 GS-1",
        "bookRef": "R.S. Sharma, Ch. 14 & 15; NCERT Class 11 Themes Theme 2",
        "question": "What are the main features of Vedic society and religion? Do you think some of the features are still prevailing in Indian society?",
        "framework": {
            "intro": "Vedic society (c. 1500–600 BCE) evolved across two distinct epochs—the early pastoral, egalitarian Rigvedic phase and the later sedentary, stratified Gangetic phase—bequeathing foundational sociological and religious paradigms that continue to permeate contemporary Indian life.",
            "body": [
                {
                    "heading": "Core Features of Vedic Society & Religion",
                    "points": [
                        "Social Structure: Evolution from kinship-based pastoral clans (Kula, Grama, Vis, Jana) to the institutionalized fourfold Varna hierarchy (Purusha Sukta) and patrilineal patriarchal family (Kula).",
                        "Religious Weltanschauung: Henotheism (polytheism centering on one chosen deity like Indra, Agni, Varuna), cosmic order (Rita), sacrificial rituals (Yajnas, Homa), and eventual Upanishadic philosophical monism (Brahman-Atman).",
                        "Position of Women: High status in Rigvedic era (Brahmavadinis like Gargi, Apala; Upanayana rights) followed by subordination in Later Vedic texts (prohibition of assemblies, dowry roots)."
                    ]
                },
                {
                    "heading": "Continuities in Contemporary Indian Society",
                    "points": [
                        "Ritualistic & Sacrificial Rites: Domestic Samskaras (Vivaha, Upanayana, Antyeshti) still commence with sacred fire (Agni) invocations and Vedic Mantras (Gayatri Mantra).",
                        "Enduring Social Stratification: Persistence of caste endogamy (Jati-Varna consciousness) and patriarchal family norms, alongside Gotra lineage taboos in matrimonial alliances.",
                        "Philosophical Monism: The Upanishadic philosophy of Advaita, Karma, and Moksha continues to form the ethical bedrock of Indian metaphysics.",
                        "Evolving Transformations: Constitutional guarantees (Articles 14, 15, 17) and social reform laws have actively dismantled untouchability, while universal education has restored women's leadership."
                    ]
                }
            ],
            "conclusion": "Vedic traditions demonstrate remarkable civilizational resilience, surviving not as frozen antiquities but as dynamic spiritual practices actively democratized and harmonized with modern constitutional values.",
            "microDiagram": "Vedic Seeds (Rita, Yajna, Varna, Samskaras) ──▶ Modern Continuities (Homa rituals, Gotra endogamy, Upanishadic Ethics, Constitutional Re-calibration)",
            "historiographicalDebate": "R.S. Sharma emphasizes the material shift from Rigvedic pastoral redistribution to Later Vedic sacrificial surplus extraction by Brahmins; A.L. Basham highlights the unbroken thread of domestic ritual continuity."
        }
    },
    {
        "id": "mains_pyq_2023_02",
        "periodId": "delhi-sultanate",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2023 GS-1",
        "bookRef": "Irfan Habib, Technology in Medieval India; Satish Chandra, Ch. 6",
        "question": "What were the major technological changes introduced during the Sultanate period? How did those technological changes influence the Indian society?",
        "framework": {
            "intro": "The establishment of the Delhi Sultanate (13th–14th century CE) catalyzed a profound technological resurgence in India, characterized by Irfan Habib as the 'Medieval Indian Technological Revolution', which revolutionized artisan manufacturing, agrarian irrigation, and architectural engineering.",
            "body": [
                {
                    "heading": "Major Technological Innovations Introduced",
                    "points": [
                        "Agrarian Irrigation: Introduction of the geared water-lifting wheel with pot-chain (Persian Wheel / Saqiya / Rahat) and lime-mortar lined canals (Firoz Tughlaq).",
                        "Textile Manufacturing: The Spinning Wheel (Charkha, first mentioned in Isami's Futuh-us-Salatin 1350 CE) increasing yarn output sixfold; cotton-carder's bow (Dhuniya/Kaman); and treadle loom.",
                        "Paper Technology: Introduction of paper manufacturing (Kagaz-sazi) replacing fragile palm-leaf and birch-bark manuscripts.",
                        "Architectural Engineering: The Arcuate system (true arch with keystone, dome, and squinch) utilizing high-strength gypsum-lime mortar.",
                        "Military Technology: Iron stirrup (Rikab) enhancing cavalry archer stability; horseshoeing (Na'lbandi); and counterweight catapults (Manjaniq/Kashkanjir)."
                    ]
                },
                {
                    "heading": "Socio-Economic Impacts on Indian Society",
                    "points": [
                        "Urban Crafts & Caste Proliferation: Expansion of specialized Muslim and Hindu artisan groups (weaver/Julaha, carder/Dhuniya, paper-maker/Kagzi), integrating lower-caste shudras into urban guild crafts.",
                        "Diffusion of Knowledge: Inexpensive paper facilitated the democratized recording of regional Bhakti-Sufi literature, astronomical texts, and commercial bookkeeping (Bahi-Khata).",
                        "Agrarian Surplus & Urbanization: The Persian wheel enabled double-cropping in semi-arid Punjab and Haryana, expanding urban food supplies to imperial garrisons."
                    ]
                }
            ],
            "conclusion": "The technological infusions of the Sultanate era transformed India's material culture, fostering a composite urban craft economy that laid the manufacturing foundation for the subsequent Mughal proto-industrial boom.",
            "microDiagram": "Sultanate Inventions (Charkha, Persian Wheel, Paper, True Arch) ──▶ Socio-Economic Results (Urban Artisan Boom, Mass Bhakti Texts, Cavalry Dominance, Agrarian Surplus)",
            "historiographicalDebate": "Irfan Habib argues these technologies created a new class of urban artisans and shifted the varna composition; Harbans Mukhia points out that traditional rural tool kits coexisted with slow diffusion rates."
        }
    },
    {
        "id": "mains_pyq_2023_03",
        "periodId": "sources-and-historiography",
        "marks": 15,
        "wordLimit": 250,
        "isPyq": True,
        "yearSource": "UPSC CSE 2023 GS-1",
        "bookRef": "R.S. Sharma, India's Ancient Past, Ch. 4 & 5; Upinder Singh, Ch. 1",
        "question": "Explain the role of geographical factors towards the development of Ancient India.",
        "framework": {
            "intro": "Geography has served as the silent architect of Indian historical evolution. The physical topography of the Indian subcontinent—defined by the Himalayan mountain wall, monsoon circulation, perennial riverine basins, and peninsular mineral belts—directly governed settlement patterns, agrarian urbanization, and cultural frontiers.",
            "body": [
                {
                    "heading": "Himalayan Barrier & North-Western Passes",
                    "points": [
                        "Strategic Isolation & Cultural Diffusion: The Himalayas shielded the subcontinent from Arctic winds and northern invasions, while passes in the Hindu Kush (Khyber, Bolan, Gomal) functioned as conduits for traders, pilgrims, and invaders (Indo-Greeks, Shakas, Kushanas).",
                        "Riverine Genesis: Perennial Himalayan meltwater fed the Indus and Ganga river systems, providing silt-laden alluvial plains critical for sustained food production."
                    ]
                },
                {
                    "heading": "River Basins & The Trajectory of Two Urbanizations",
                    "points": [
                        "Indus Valley Alluvium: Semi-arid floodplains of the Indus and Ghaggar-Hakra enabled easy clearance and flood-retreat agriculture, facilitating the Bronze Age First Urbanization (Harappa, Mohenjo-daro).",
                        "Gangetic Basin & Iron Revolution: Dense mid-Gangetic sal-forests required heavy iron axes (mined from Chota Nagpur) for clearance. The fertile alluvium supported wet paddy transplantation (Shali), fueling the Second Urbanization and Magadhan imperialism.",
                        "Riverine Confluences as Capitals: Pataliputra at the confluence of Ganga, Son, Gandak, and Ghaghra was an impregnable 'Jaladurga' (water fortress) controlling trade routes."
                    ]
                },
                {
                    "heading": "Mineral Belts & Material State Formation",
                    "points": [
                        "Copper & Iron Deposits: Proximity of Magadha to the iron ores of Barabar and copper belts of Singhbhum provided an unmatched metallurgical edge in military weaponry and agrarian tools.",
                        "Khetri Mines: Fueled Harappan bronze and Chalcolithic OCP copper-hoard industries in Rajasthan."
                    ]
                },
                {
                    "heading": "Peninsular Geography & Regional Identity",
                    "points": [
                        "Vindhyan Divide: The Vindhya and Satpura ranges created a semi-permeable boundary between Aryavarta and Dakshinapatha, preserving Dravidian linguistics while allowing cultural acculturation.",
                        "Coastal Enclaves & Maritime Silk Road: Malabar (Muziris) and Coromandel (Arikamedu, Kaveripattinam) coasts utilized monsoon winds (Hippalus 45 CE) for lucrative spice trade with the Roman Empire and Southeast Asia."
                    ]
                }
            ],
            "conclusion": "As R.S. Sharma observes, ancient Indian history is essentially the chronicle of human interaction with diverse ecological zones, where geography determined whether a region became a nuclear center of empire or an isolated refuge zone.",
            "microDiagram": "Geographical Anchors ──▶ Historical Outcomes: [Hindu Kush Passes ──▶ Silk Route trade & invasions]; [Gangetic Alluvium + Chota Nagpur Iron ──▶ Magadhan Imperialism]; [Monsoon Winds ──▶ Roman-Southeast Asian Maritime Trade]",
            "historiographicalDebate": "Environmental determinists (Ellsworth Huntington) view geography as causative; modern cultural geographers (Subbarao, The Personality of India) emphasize the dynamic interaction between geography, ecology, and human technological intervention."
        }
    },
    {
        "id": "mains_pyq_2023_04",
        "periodId": "establishment-of-british-power",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2023 GS-1",
        "bookRef": "Sekhar Bandyopadhyay, Ch. 2; B.L. Grover, British Conquest",
        "question": "Why did the armies of the British East India Company – mostly comprising of Indian soldiers – win consistently against the more numerous and better equipped armies of the then Indian rulers? Give reasons.",
        "framework": {
            "intro": "The British conquest of India presents an extraordinary military paradox: a commercial trading company conquered a subcontinent of 300 million people using an army composed of over 85% native Indian sepoys. The Company's consistent military victories stemmed not from racial or technological superiority, but from superior institutional, financial, and organizational systems.",
            "body": [
                {
                    "heading": "Key Factors for British Military Supremacy",
                    "points": [
                        "Regular Fiscal-Military State: Unlike Indian rulers whose armies suffered from chronic salary arrears (leading to frequent mutinies and desertions), the EIC paid regular cash salaries on the first of every month, guaranteed by Bengal's land revenues.",
                        "Strict Discipline & Professional Drill: Modern European line infantry tactics, standardized musket volley-firing, and continuous tactical training rendered Company regiments cohesive under fire, contrasting with feudal Indian levies.",
                        "Institutional Meritocracy & Officer Cadre: Company officers were promoted based on merit and seniority through an institutional military bureaucracy, whereas Indian leadership was plagued by courtly factionalism, dynastic rivalries, and mercenary loyalties.",
                        "Absence of Pan-Indian National Consciousness: India was a mosaic of warring regional kingdoms (Marathas, Mysore, Nizam, Sikhs). Indian recruits (Purbiyas, Gurkhas, Telugus) identified with local clan loyalties or military 'namak' (salt fidelity), viewing the Company as a reliable military employer rather than an alien colonial oppressor.",
                        "Superior Artillery Logistics & Cartography: Advanced surveying (Great Trigonometrical Survey), standardized munitions, and naval supremacy along coastal supply lines ensured sustained logistical resilience."
                    ]
                }
            ],
            "conclusion": "The British did not conquer India with British soldiers; they harnessed India's own military labour market through regular pay, superior institutional discipline, and naval-financial power to defeat politically fractured regional polities.",
            "microDiagram": "Institutional Foundations: [Regular Cash Pay + Meritocratic Command + Standardized Drill] ──▶ Defeated: [Feudal Levies + Delayed Wages + Court Factionalism]",
            "historiographicalDebate": "Dirks and Bayly emphasize the Company as an aggressive 'fiscal-military state' backed by global capitalist credit; nationalist historians emphasize the tragic absence of political unity among 18th-century regional states."
        }
    },
    {
        "id": "mains_pyq_2023_05",
        "periodId": "mahatma-gandhi",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2023 GS-1",
        "bookRef": "Bipan Chandra, Ch. 18; Ramachandra Guha, Gandhi and Tagore",
        "question": "What was the difference between Mahatma Gandhi and Rabindranath Tagore in their approach towards education and nationalism?",
        "framework": {
            "intro": "Mahatma Gandhi and Rabindranath Tagore, two intellectual titans of modern India whom Romain Rolland called the 'two poles of the Indian mind', shared a deep mutual reverence ('Mahatma' given by Tagore, 'Gurudev' given by Gandhi) while holding profoundly contrasting philosophical visions on education and nationalism.",
            "body": [
                {
                    "heading": "Contrasting Visions on Nationalism",
                    "points": [
                        "Gandhi (Anti-Colonial Mass Nationalism): Viewed political nationalism and anti-colonial mobilization as indispensable to liberate Indian masses from British exploitation, emphasizing Swadeshi, non-cooperation, and boycotts.",
                        "Tagore (Cosmopolitan Humanism): Deeply suspicious of narrow political nationalism, calling it a 'cruel epidemic' of the West that breeds jingoism and xenophobia. Tagore advocated universal cosmopolitanism (Visva-Bharati motto: 'Where the world makes its home in a single nest') and vehemently opposed the burning of foreign cloth during Swadeshi."
                    ]
                },
                {
                    "heading": "Contrasting Pedagogical Philosophies (Education)",
                    "points": [
                        "Gandhi's Nai Talim (Basic Education): Rooted in village craft-based education (Wardha Scheme 1937); learning through physical labour (spinning, carpentry, farming) to eradicate caste prejudices and build self-reliant rural republics.",
                        "Tagore's Shantiniketan (Aesthetic Freedom): Emphasized open-air learning amidst nature, creative artistic expression (music, poetry, fine arts), and a synthesis of Eastern spiritualism with Western scientific enquiry, rejecting rigid disciplinary dogmatism."
                    ]
                }
            ],
            "conclusion": "Despite divergent pedagogical paths—Gandhi's utilitarian moral self-reliance vs. Tagore's aesthetic universal humanism—both fundamentally rejected rote British colonial education and aimed to restore authentic Indian civilizational self-respect.",
            "microDiagram": "Gandhi [Craft-based Nai Talim + Political Anti-Imperialism] ◀── Debate ──▶ Tagore [Nature Aesthetic Shantiniketan + Cosmopolitan Anti-Jingoism]",
            "historiographicalDebate": "Amartya Sen in 'The Argumentative Indian' notes that Tagore's critique saved Indian nationalism from parochial xenophobia, while Gandhi grounded Tagore's lofty idealism in the harsh material reality of the Indian peasantry."
        }
    },
    {
        "id": "mains_pyq_2023_06",
        "periodId": "french-revolution",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2023 GS-1",
        "bookRef": "Norman Lowe, Mastering Modern World History, Ch. 1 & 2; Pratik Nayak World History",
        "question": "Explain the consequences of the American and French Revolutions on the modern world.",
        "framework": {
            "intro": "The Atlantic Revolutions of the late 18th century—the American Revolution (1776) and the French Revolution (1789)—shattered the ancient regimes of feudal privilege and divine-right monarchies, inaugurating the modern political epoch of popular sovereignty, constitutionalism, and human rights.",
            "body": [
                {
                    "heading": "Consequences of the American Revolution (1776)",
                    "points": [
                        "Pioneered Written Constitutionalism: Established the world's first modern constitutional republic based on Montesquieu's separation of powers (Executive, Legislative, Judiciary) and a justiciable Bill of Rights.",
                        "Catalyst for Anti-Colonialism: The principle of 'No taxation without representation' inspired global decolonization movements across Latin America (Simon Bolivar) and Asia.",
                        "Federal Governance Model: Provided the institutional blueprint for federal democracies managing continental diversity."
                    ]
                },
                {
                    "heading": "Consequences of the French Revolution (1789)",
                    "points": [
                        "Tricolour Ideology: Universalized the revolutionary trinity of 'Liberty, Equality, Fraternity', inspiring radical movements worldwide.",
                        "Demolition of Feudalism & Secular Statehood: Abolished feudal manorial dues, codified the secular Napoleonic Code (1804), and separated church from state.",
                        "Birth of Modern Nationalism: Transformed subjects into citizens of a nation-state, catalyzing 19th-century European unifications (Italy, Germany) and anti-dynastic revolutions of 1848.",
                        "Inspiration for Indian Nationalists: Tipu Sultan planted the 'Tree of Liberty' at Seringapatam and joined the Jacobin Club; Raja Rammohan Roy celebrated the French Revolution as the dawn of human emancipation."
                    ]
                }
            ],
            "conclusion": "The American Revolution established the institutional architecture of constitutional democracy, while the French Revolution provided its social and egalitarian conscience, together shaping the Universal Declaration of Human Rights and modern democratic constitutions, including the Indian Constitution.",
            "microDiagram": "Atlantic Revolutions ──▶ Modern Heritage: [American: Federalism, Written Constitution, Separation of Powers] + [French: Liberty, Equality, Fraternity, Secularism, Citizen Sovereignty]",
            "historiographicalDebate": "R.R. Palmer characterized this as the single 'Age of the Democratic Revolution'; Marxist historians (Lefebvre) view the French Revolution as the definitive triumph of the bourgeoisie over feudal aristocracy."
        }
    },

    # 2022 GS-1 QUESTIONS
    {
        "id": "mains_pyq_2022_01",
        "periodId": "kingdoms-of-south",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2022 GS-1",
        "bookRef": "Upinder Singh, Ch. 10; NCERT Class 11 Fine Arts",
        "question": "How will you explain that medieval Indian temple sculptures represent the social life of those days?",
        "framework": {
            "intro": "Medieval Indian temples (c. 8th–14th century CE) were not merely sacred abodes of divinity; they functioned as dynamic civic complexes and stone chronicles that mirrored the full panorama of contemporary secular, social, and economic life.",
            "body": [
                {
                    "heading": "Temple Sculptures as Mirrors of Medieval Society",
                    "points": [
                        "Delineation of Occupations & Guilds: Sculptural friezes at Khajuraho and Konark depict stonemasons, carpenters, musicians, metalworkers, and agriculturalists plowing fields, recording the occupational specialization of medieval society.",
                        "Courtly Life & Royal Patronage: Narrative panels at Thanjavur (Brihadisvara) and Hampi depict royal processions, coronation ceremonies, war elephants, and royal hunts, reflecting the feudal court culture.",
                        "Gender Roles & Domestic Realities: Reliefs illustrate women applying makeup (Darpana-sundaris / Alasa kanyas), dancing, playing instruments (Vina, Mridangam), nursing infants, and participating in temple rituals.",
                        "Martial Culture & Warfare: Friezes at Hoysaleswara (Halebidu) and Sun Temple (Konark) document contemporary military technology, cavalry armor, archery stances, and battle formations.",
                        "Celebration of Kama & Esoteric Cults: Mithuna couples at Khajuraho and Konark reflect the integration of Tantric philosophical traditions and the holistic Hindu worldview recognizing Kama (desire) alongside Dharma, Artha, and Moksha."
                    ]
                }
            ],
            "conclusion": "Medieval temple sculptures democratized religious spaces by etching the secular rhythm of everyday human existence into sacred stone, providing historians with an invaluable visual ethnography of pre-modern India.",
            "microDiagram": "Temple Sculptural Reliefs ──▶ Social Dimensions: [Mithuna & Alasa Kanyas ──▶ Aesthetics & Tantra]; [Warrior Friezes ──▶ Feudal Military]; [Artisan Panels ──▶ Shreni Guild Economy]",
            "historiographicalDebate": "Stella Kramrisch viewed temple sculptures as pure metaphysical symbols; Devangana Desai demonstrates their sociological anchorage in feudal court patronage and tantric socio-religious networks."
        }
    },
    {
        "id": "mains_pyq_2022_02",
        "periodId": "gupta-age",
        "marks": 15,
        "wordLimit": 250,
        "isPyq": True,
        "yearSource": "UPSC CSE 2022 GS-1",
        "bookRef": "R.S. Sharma, Ch. 27; K.A. Nilakanta Sastri, The Colas",
        "question": "Discuss the main contributions of Gupta period and Chola period towards Indian heritage and culture.",
        "framework": {
            "intro": "The Imperial Guptas (c. 4th–6th c. CE) in the north and the Imperial Cholas (c. 9th–12th c. CE) in the south constitute the twin classical summits of Indian civilization, defining enduring standards in temple architecture, bronze sculpture, literature, and administrative innovation.",
            "body": [
                {
                    "heading": "Contributions of the Gupta Period (The Classical Zenith of the North)",
                    "points": [
                        "Structural Temple Architecture: Transitioned from rock-cut caves to free-standing stone temples in the Panchayatana layout (Dashavatara Temple at Deogarh, Bhitargaon brick temple).",
                        "Mastery of Classical Sculpture & Murals: Sarnath Seated Buddha in Dharmachakra Pravartana mudra; sublime Ajanta cave frescoes (Padmapani Bodhisattva); rust-free metallurgy of Mehrauli Iron Pillar.",
                        "Sanskrit Golden Age: Zenith of Classical Sanskrit drama and poetry under Kalidasa (Abhijnanashakuntalam, Meghadutam), Visakhadatta (Mudrarakshasa), and Sudraka.",
                        "Scientific Treatises: Aryabhata (Aryabhatiya: decimal zero, earth's diurnal rotation, eclipse science); Varahamihira (Brihatsamhita); metallurgy and medical compendia."
                    ]
                },
                {
                    "heading": "Contributions of the Chola Period (The Monumental & Maritime Zenith of the South)",
                    "points": [
                        "Monumental Dravida Temple Architecture: Reached perfection in the soaring vimanas of Rajaraja I's Brihadisvara Temple at Thanjavur (66m granite vimana) and Rajendra I's Gangaikondacholapuram.",
                        "Lost-Wax Bronze Sculpture (Cire Perdue): The iconic Chola Bronze Nataraja (Lord of Dance), hailed worldwide by Auguste Rodin as the supreme sculptural synthesis of cosmic science and religious art.",
                        "Democratic Local Self-Government: Decentralized rural administration via the Kudavolai (pot-ticket) system in the Brahmin Sabha, recorded in the Uttaramerur Inscriptions (919/921 CE).",
                        "Maritime Silk Route Dominance: Powerful blue-water navy conquering the Srivijaya Empire (Sumatra/Malaya) and establishing extensive diplomatic trade with Song Dynasty China.",
                        "Tamil Literary Flourishing: Kamban's Ramavataram (Kamba Ramayanam) and Sekkizhar's Periyapuranam."
                    ]
                }
            ],
            "conclusion": "While the Guptas formulated the canonical aesthetic, mathematical, and literary grammar of classical India, the Cholas scaled monumental architecture to cosmic proportions and projected Indian cultural genius across the maritime Indian Ocean world.",
            "microDiagram": "Classical Summits: [Guptas: Sarnath Buddha + Kalidasa Sanskrit + Aryabhata Science] ◀──▶ [Cholas: Brihadisvara Vimana + Nataraja Bronze + Uttaramerur Democracy + Maritime Navy]",
            "historiographicalDebate": "A.L. Basham celebrated the Gupta era as India's Renaissance; modern regional historians emphasize that the Chola maritime-agrarian empire exhibited equal organizational and artistic brilliance."
        }
    },
    {
        "id": "mains_pyq_2022_03",
        "periodId": "colonial-economy-and-drain-of-wealth",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2022 GS-1",
        "bookRef": "Bipan Chandra, Ch. 7; Spectrum, Ch. 28",
        "question": "Why was there a sudden spurt in famines in colonial India since the mid-eighteenth century? Give reasons.",
        "framework": {
            "intro": "Between 1770 (the devastating Great Bengal Famine which wiped out one-third of Bengal's population) and 1943 (the Bengal Famine), colonial India witnessed over 30 major famines. As Amartya Sen established, these famines were not natural acts of drought, but institutional man-made catastrophes created by British colonial economic policies.",
            "body": [
                {
                    "heading": "Structural Causes of Famines under Colonial Rule",
                    "points": [
                        "Rigid High Land Revenue Demands: Permanent Settlement, Ryotwari, and Mahalwari systems enforced inflexible cash assessments under the 'Sunset Law', forcing peasants to sell foodstocks to pay revenue even during droughts.",
                        "Forced Commercialization of Agriculture: Foodgrain cultivation (millets, pulses, coarse rice) was displaced by export cash crops (indigo, opium, cotton, jute) to feed British textile mills and imperial treasuries.",
                        "Deindustrialization & Rural Overcrowding: Collapse of traditional handloom and artisan industries threw millions of artisans back onto land as landless agricultural labourers with zero purchasing power.",
                        "Laissez-Faire Ideology & Foodgrain Exports: Rulers adhered dogmatically to Adam Smith's free-market dogma, refusing price controls or relief grain distribution; India continued exporting foodgrains to Britain even at the peak of famines (e.g., Famine of 1876–78 under Lord Lytton).",
                        "Inadequate Transportation as a Two-Edged Sword: Railways were used to suck foodgrains out of drought-hit rural hinterlands to ports for export, transforming local crop shortages into widespread regional starvations."
                    ]
                }
            ],
            "conclusion": "Colonial famines were fundamentally crises of 'entitlement' and purchasing power resulting from systemic economic drain, commodification of agriculture, and imperial indifference, culminating in the 1943 Churchill-era famine that killed 3 million people.",
            "microDiagram": "Colonial Policy Nexus: [Rigid Cash Taxes + Cash Crop Shift + Deindustrialization + Foodgrain Exports] ──▶ Famine Mortality Spurt (30+ Major Famines)",
            "historiographicalDebate": "Imperial administrators blamed tropical monsoon failure and Indian overpopulation; R.C. Dutt (Economic History of India) and Amartya Sen proved that structural poverty and entitlement failure drove famine mortality."
        }
    },
    {
        "id": "mains_pyq_2022_04",
        "periodId": "indian-freedom-struggle",
        "marks": 15,
        "wordLimit": 250,
        "isPyq": True,
        "yearSource": "UPSC CSE 2022 GS-1",
        "bookRef": "Bipan Chandra, Ch. 1 to 16; Sekhar Bandyopadhyay, Ch. 4 & 5",
        "question": "Trace the emergence of national consciousness in India from the late 19th century to the non-cooperation movement.",
        "framework": {
            "intro": "The emergence of modern Indian national consciousness was a transformative evolutionary process spanning six decades, progressing from elite constitutional prayer-and-petition associations to militant cultural self-assertion, and culminating in Mahatma Gandhi's mass multi-class Non-Cooperation Movement (1920–1922).",
            "body": [
                {
                    "heading": "1. Material & Institutional Catalysts (Late 19th Century)",
                    "points": [
                        "Colonial Modernity: Pan-Indian railway networks, postal-telegraph lines, and press created physical and informational connectivity.",
                        "The Economic Drain Critique: Early nationalist intellectuals (Dadabhai Naoroji, M.G. Ranade, R.C. Dutt) systematically dismantled the British 'civilizing mission' myth by proving colonial rule caused structural pauperization.",
                        "Pre-Congress Associations: East India Association (1866), Poona Sarvajanik Sabha (1870), Indian Association of Calcutta (Surendranath Banerjee, 1876) organizing all-India campaigns against the reduction of civil service age limits and the Vernacular Press Act 1878."
                    ]
                },
                {
                    "heading": "2. Moderate Phase of INC (1885–1905): The Secular Seedbed",
                    "points": [
                        "Constitutional Agitation: Used the 3Ps (Prayer, Petition, Protest) to cultivate a pan-Indian political fraternity, demand legislative representation (Indian Councils Act 1892), and train public opinion."
                    ]
                },
                {
                    "heading": "3. Extremist Surge & Swadeshi Movement (1905–1908)",
                    "points": [
                        "Curzon's Partition of Bengal (1905): Transformed elite politics into active popular protest; introduced boycott of foreign goods, national education, and mass cultural mobilizations (Vande Mataram, Raksha Bandhan).",
                        "Lal-Bal-Pal & Aurobindo Ghosh: Demanded Swaraj as an inalienable right, moving beyond colonial mendicancy."
                    ]
                },
                {
                    "heading": "4. First World War, Home Rule & The Lucknow Synthesis (1914–1919)",
                    "points": [
                        "Home Rule Leagues (Tilak & Besant 1916): Diffused political awareness into mofussil towns and rural areas.",
                        "Lucknow Pact (1916): Reunited Moderates and Extremists, and forged joint Congress-Muslim League anti-colonial front."
                    ]
                },
                {
                    "heading": "5. The Gandhian Watershed & Non-Cooperation (1919–1922)",
                    "points": [
                        "Catalysts: Rowlatt Act tyranny and the horrific Jallianwala Bagh massacre (13 April 1919).",
                        "Khilafat-Non-Cooperation Merger (1920): Gandhi united Hindu-Muslim masses, transforming the Congress at Nagpur (1920) into a fighting mass movement with 15-member Working Committee, village committees, and boycott of courts, schools, and foreign cloth."
                    ]
                }
            ],
            "conclusion": "Between 1885 and 1920, Indian nationalism transitioned from an elite urban intellectual club into an all-India mass anti-colonial movement, forging an unbreakable collective national consciousness across barriers of region, language, and caste.",
            "microDiagram": "Nationalism Evolution: [Pre-Congress / Drain Critique] ──▶ [Moderate Constitutionalism (1885-1905)] ──▶ [Swadeshi Mass Boycott (1905-08)] ──▶ [Home Rule (1916)] ──▶ [Gandhian Mass Non-Cooperation (1920-22)]",
            "historiographicalDebate": "Cambridge school (Seal, Gallagher) views early nationalism as factional elite competition for colonial patronage; Marxist & Nationalist historians demonstrate the genuine growth of anti-imperialist mass solidarity."
        }
    },

    # 2021 GS-1 QUESTIONS
    {
        "id": "mains_pyq_2021_01",
        "periodId": "bhakti-sufi-movements",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2021 GS-1",
        "bookRef": "Satish Chandra, Ch. 13; NCERT Class 12 Themes Theme 6",
        "question": "Evaluate the nature of the Bhakti literature and its contribution to Indian culture.",
        "framework": {
            "intro": "Bhakti literature (c. 6th–17th century CE) represents South Asia's greatest egalitarian cultural renaissance, which decentralized sacred knowledge from elite Sanskrit monopolies into vibrant regional vernaculars, transforming poetry into an instrument of social emancipation.",
            "body": [
                {
                    "heading": "Nature of Bhakti Literature",
                    "points": [
                        "Vernacular & Oral Idiom: Composed in the living languages of the common people (Awadhi, Brajbhasha, Marathi, Bengali, Tamil, Assamese, Punjabi), utilizing folk song meters (Padas, Dohe, Abhangas, Vachanas).",
                        "Nirguna vs. Saguna Polarities: Nirguna literature (Kabir's Bijak, Guru Nanak's hymns in Adi Granth) denounced idol worship and caste bigotry; Saguna literature (Tulsidas's Ramcharitmanas, Surdas's Sursagar, Mirabai's bhajans) celebrated personal emotional intimacy with divine incarnations (Rama, Krishna).",
                        "Feminine Agency & Defiance: Women saint-poets (Mirabai, Lal Ded, Akka Mahadevi, Andal) subverted patriarchal domesticity and caste structures through ecstatic devotional poetry."
                    ]
                },
                {
                    "heading": "Contributions to Indian Culture",
                    "points": [
                        "Linguistic Democratization: Gave birth to modern regional literatures; Sankaradeva founded Assamese literature; Chaitanya's followers enriched Bengali; Jnaneshwar and Tukaram shaped Marathi.",
                        "Musical Synthesis: Blended classical ragas with regional folk melodies; nurtured Dhrupad, Thumri, Haveli Sangeet, and the Kirtan choral tradition.",
                        "Socio-Religious Inclusivity: Dismantled varna discrimination by asserting that devotion, not birth or ritual purity, was the sole path to divine grace.",
                        "Syncretic Confluence: Blended seamlessly with Sufi poetry (Amir Khusrau, Bulleh Shah), fostering India's composite Ganga-Jamuni Tehzeeb."
                    ]
                }
            ],
            "conclusion": "Bhakti literature democratized spirituality and linguistic culture, humanizing religion and providing the secular, inclusive cultural bedrock upon which modern democratic India stands.",
            "microDiagram": "Bhakti Literature ──▶ Cultural Fruits: [Vernacular Languages Born] + [Feminine Agency Expressed] + [Caste Barriers Challenged] + [Kirtan/Bhajan Music Created]",
            "historiographicalDebate": "Max Weber saw Bhakti as other-worldly quietism; D.D. Kosambi and Krishna Sharma demonstrate its dynamic socio-economic role in integrating peasants and artisans into a common cultural fold."
        }
    },
    {
        "id": "mains_pyq_2021_02",
        "periodId": "colonial-economy-and-drain-of-wealth",
        "marks": 10,
        "wordLimit": 150,
        "isPyq": True,
        "yearSource": "UPSC CSE 2021 GS-1",
        "bookRef": "Bipan Chandra, Ch. 7; Spectrum, Ch. 28",
        "question": "Trace the technological and socioeconomic developments that led to the decline of traditional artisan industries in colonial India.",
        "framework": {
            "intro": "The catastrophic de-industrialization of India in the 19th century—which transformed a premier global manufacturing exporter of fine textiles into a primary raw material exporter—was driven by the aggressive convergence of British industrial technology, discriminatory tariff policies, and colonial administrative disruption.",
            "body": [
                {
                    "heading": "Technological & Industrial Developments",
                    "points": [
                        "British Industrial Mechanization: Inventions of the Flying Shuttle (Kay), Spinning Jenny (Hargreaves), and Steam Engine (Watt) enabled Manchester and Lancashire power-looms to produce cotton cloth at speeds and costs unmatched by handloom weavers.",
                        "Steamship & Railway Penetration: Railways (commencing 1853) pierced the rural Indian interior, flooding village bazaars with machine-made British textiles and ironware, while steam navigation drastically lowered transport costs from Liverpool to Indian ports."
                    ]
                },
                {
                    "heading": "Socio-Economic & Policy Factors",
                    "points": [
                        "One-Way Free Trade & Tariff Inequity: Under the pressure of British industrial lobbies, British goods entered India duty-free (or with nominal 2-3% tariffs), while Indian textiles faced punitive import duties in Britain (up to 70–80%).",
                        "Collapse of Indigenous Court Patronage: Annexation of princely states (Awadh, Carnatic, Marathas) destroyed the primary aristocratic market for luxury crafts (muslins of Dacca, metal inlays, Bidri ware, fine silks).",
                        "Oppressive EIC Agency System: EIC commercial agents forced weavers under the 'Dadni' advance system to supply cloth at unremunerative prices, driving hereditary weavers out of their trade.",
                        "Ruralization of the Economy: Displaced artisans migrated to agriculture, causing hyper-subdivision of land, tenancy exploitation, and agrarian stagnation."
                    ]
                }
            ],
            "conclusion": "De-industrialization was not an inevitable outcome of technological progress, but a conscious imperial policy designed to make India a colonial appendage: an agrarian feeder of raw cotton to Manchester and an uncompetitive captive market for British manufactured goods.",
            "microDiagram": "De-Industrialization Nexus: [British Power-Looms + Indian Railways + Punitive Tariffs + Court Collapse] ──▶ Destruction of Artisans ──▶ Agrarian Overcrowding",
            "historiographicalDebate": "Morris D. Morris argued handlooms survived by adapting to imported yarn; Amiya Kumar Bagchi and Bipan Chandra proved conclusively that artisan employment suffered an catastrophic absolute and relative collapse."
        }
    },
    {
        "id": "mains_pyq_2021_03",
        "periodId": "world-war-1",
        "marks": 15,
        "wordLimit": 250,
        "isPyq": True,
        "yearSource": "UPSC CSE 2021 GS-1",
        "bookRef": "Norman Lowe, Ch. 8 to 14 (Interwar Years)",
        "question": "There arose a serious challenge to the Democratic State System between the two World Wars. Evaluate the statement.",
        "framework": {
            "intro": "The interwar period (1919–1939), hailed at the 1919 Paris Peace Conference as the triumphant zenith of liberal democracy with the birth of the League of Nations and new European republics, degenerated within two decades into an acute systemic crisis that witnessed the rapid collapse of parliamentary democracies and the virulent ascendancy of totalitarian regimes.",
            "body": [
                {
                    "heading": "1. Flaws of the Versailles Settlement & Economic Devastation",
                    "points": [
                        "Treaty of Versailles (1919): The harsh 'War Guilt' clause (Article 231) and crushing reparations ($33 billion) imposed on Weimar Germany delegitimized parliamentary democracy as an instrument of national humiliation ('November Criminals').",
                        "The Great Depression (1929): Global economic collapse, 40% unemployment in Germany, and hyperinflation shattered middle-class faith in liberal capitalist democracies, driving masses toward extremist political movements."
                    ]
                },
                {
                    "heading": "2. Rise of Totalitarian Ideologies (Fascism & Nazism)",
                    "points": [
                        "Italian Fascism (Mussolini, 1922): Exploited Italy's 'mutilated victory', fear of communism, and parliamentary deadlock; established a one-party corporate totalitarian state ('Everything in the State, nothing outside the State').",
                        "German National Socialism (Hitler, 1933): Exploited racial pseudoscience, anti-Semitism, and economic distress; dismantled the Weimar Constitution through the Reichstag Fire Decree and Enabling Act 1933.",
                        "Totalitarian Characteristics: Total subjugation of individual rights, state terror (Gestapo, OVRA), personality cults, militaristic expansionism, and eradication of democratic opposition."
                    ]
                },
                {
                    "heading": "3. Paralysis of Democratic Institutions & The League of Nations",
                    "points": [
                        "Inability to Halt Aggression: The League of Nations was paralyzed by US absence and Anglo-French discord; failed to stop Japanese invasion of Manchuria (1931) and Italian invasion of Abyssinia (1935).",
                        "Policy of Appeasement: Britain (Neville Chamberlain) and France surrendered democratic Czechoslovakia at Munich (1938) to placate Hitler, fatally undermining democratic collective security."
                    ]
                },
                {
                    "heading": "4. Militarism in East Asia",
                    "points": [
                        "Imperial Japan: Assassination of democratic prime ministers (May 1932 Incident) led to military junta control, imperialist expansion into China, and alliance with Axis powers."
                    ]
                }
            ],
            "conclusion": "The interwar democratic crisis demonstrated that democratic institutions cannot survive without economic stability and courageous collective security. The failure of interwar democracies directly unleashed the catastrophic global violence of World War II.",
            "microDiagram": "Interwar Crisis: [Versailles Humiliation + 1929 Great Depression + Parliamentary Gridlock] ──▶ Totalitarian Ascent (Hitler & Mussolini) ──▶ Aggression Unchecked by Appeasement ──▶ World War II",
            "historiographicalDebate": "A.J.P. Taylor argued Hitler was an opportunist exploiting western democratic weakness; Eric Hobsbawm viewed the interwar years as the 'Age of Catastrophe' where liberal capitalism was caught in a mortal fight against fascist and communist alternatives."
        }
    }
]

# Append new questions
count_added = 0
for q in MRUNAL_MAINS_PYQS:
    if q['id'] not in existing_ids:
        mains_questions.append(q)
        existing_ids.add(q['id'])
        count_added += 1

print(f"Added {count_added} authentic UPSC CSE Mains PYQs. Total now: {len(mains_questions)}")

with open('data/mains-questions.json', 'w', encoding='utf-8') as f:
    json.dump(mains_questions, f, ensure_ascii=False, indent=2)

print("Saved mains-questions.json successfully!")
