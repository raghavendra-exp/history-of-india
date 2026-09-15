# scripts/gen_mains_modern.py
import json

def get_modern_mains():
    # 60 Comprehensive Modern Indian History Mains Questions (mains_mod_001 to mains_mod_060)
    qs_raw = [
        # Group 1: 001 - 010 (Colonial Conquest and Economic Drain)
        ("mains_mod_001", "colonial-expansion", 15, 250, True, "UPSC CSE 2017 GS-1", "Bipan Chandra, Ch. 2; Spectrum Modern India",
         "The Anglo-French rivalry in the Carnatic (1740-1763) decided which European power would master the Indian subcontinent. Analyze the factors that gave Britain victory over France.",
         "Between 1740 and 1763, the British and French East India Companies fought three Carnatic Wars in southern India, which mirrored the War of the Austrian Succession and the Seven Years' War in Europe.",
         [
             ("Commercial Superiority and Financial Independence", ["British East India Company was a private joint-stock commercial enterprise driven by profit, enjoying financial autonomy from the British state.", "French Company (Compagnie des Indes) was a bureaucratic government-controlled department burdened by royal state debt, corruption, and ministerial interference in Paris."]),
             ("Naval Supremacy of the Royal Navy", ["Britain possessed the world's most formidable navy, allowing regular troop reinforcements and supply convoys to reach Madras and Calcutta.", "French fleets under La Bourdonnais and D'Ache suffered from logistical shortages and were repeatedly forced to withdraw to Mauritius."]),
             ("Clive's Conquest of Bengal vs Dupleix's Deccan Ambitions", ["While French governor Dupleix exhausted French resources in complex court intrigues in Hyderabad and Arcot, Robert Clive conquered Bengal at Plassey (1757).", "Bengal's vast agricultural revenues and trade wealth provided Britain with an inexhaustible financial treasury to finance southern campaigns, starving French forces under Count de Lally of basic pay."]),
             ("Battle of Wandiwash (1760)", ["Sir Eyre Coote decisively crushed Count de Lally at Wandiwash (1760); the 1763 Treaty of Paris reduced French presence in India to mere demilitarized trading enclaves (Pondicherry, Chandernagore)."])
         ],
         "Geopolitical comparative matrix: British EIC (Private, Naval mastery, Bengal wealth base) vs French Company (State-owned, Weak navy, Deccan bankruptcy).",
         "The Carnatic Wars demonstrated that European colonial hegemony in India was won not merely by military courage on Indian soil, but by maritime command, financial resilience, and commercial independence."),

        ("mains_mod_002", "colonial-expansion", 10, 150, False, "Standard Practice", "Spectrum Modern India; Bipan Chandra",
         "Examine the strategic objectives and mechanics of Lord Wellesley's 'Subsidiary Alliance' system. How did it reduce Indian princely states to dependent vassals?",
         "Introduced by Governor-General Lord Wellesley (1798-1805), the Subsidiary Alliance system was a diplomatic-military device designed to expand British paramountcy without direct territorial annexation.",
         [
             ("Core Operational Mechanics", ["An Indian ruler entering the alliance agreed to disband his indigenous standing army.", "Stationed a permanent British subsidiary force within his territory, financed by surrendering a portion of territory or paying an annual cash subsidy.", "Accepted a British Resident at court and agreed not to employ any other European or conduct foreign diplomacy with any other power without British consent."]),
             ("Strategic British Objectives", ["Transformed princely states into British protectorates at zero financial cost to the Company.", "Excluded French influence and eliminated any prospective anti-British Indian coalitions.", "Maintained British troops deep inside Indian territories ready for immediate offensive deployment."]),
             ("Devastating Impact on Princely States", ["Rulers lost sovereignty, foreign policy, and military capability, degenerating into irresponsible despots shielded by British bayonets.", "First state to sign: Nizam of Hyderabad (1798), followed by Mysore (1799), Tanjore (1799), Awadh (1801), and Peshwa Baji Rao II (Treaty of Bassein 1802)."])
         ],
         "Flowchart: Subsidiary Alliance Terms -> Disband Native Army -> Station British Subsidiary Force -> British Resident Overseer -> Loss of Sovereignty.",
         "The Subsidiary Alliance was an insidious mechanism of imperial subjugation: it disarmed Indian states, made them pay for their own subjugation, and placed the British in undisputed mastery of peninsular India."),

        ("mains_mod_003", "colonial-expansion", 10, 150, True, "UPSC CSE 2013 GS-1", "Spectrum Modern India; Bipan Chandra",
         "Lord Dalhousie's 'Doctrine of Lapse' was an aggressive imperial instrument that accelerated the territorial consolidation of British India while igniting the embers of 1857. Elucidate.",
         "Governor-General Lord Dalhousie (1848-1856) vigorously pursued the 'Doctrine of Lapse'—an imperial policy denying dependent Indian rulers the right to pass sovereign authority to an adopted heir without British paramount sanction.",
         [
             ("Legal Rationale and Classification of States", ["Dalhousie classified Indian states into three tiers: 1. Sovereign independent states (not subject to Lapse); 2. Dependent tributary states created or restored by the British; 3. Subordinated states.", "Asserted that for dependent states, adoption of a son created personal inheritance of private property, but political sovereignty 'lapsed' automatically to the British Crown."]),
             ("Sequence of Major Annexations", ["Satara (1848), Jaitpur and Sambalpur (1849), Baghat (1850), Udaipur (1852), Jhansi (1853), and Nagpur (1854).", "Refused the pension of Peshwa Baji Rao II to his adopted son Nana Saheb."]),
             ("The Annexation of Awadh (1856)", ["When Lapse could not be applied because Nawab Wajid Ali Shah had legitimate heirs, Dalhousie annexed Awadh under the pretext of 'misgovernance' (Outram Report), deeply alienating the Bengal Army sepoys (the majority of whom were high-caste Awadh peasants)."]),
             ("Catalyst for the 1857 Revolt", ["Directly provoked Rani Lakshmibai of Jhansi, Nana Saheb of Kanpur, and the dispossessed taluqdars of Awadh to become leaders of the 1857 rebellion."])
         ],
         "Timeline map of annexed states: Satara (1848) -> Sambalpur (1849) -> Jhansi (1853) -> Nagpur (1854) -> Awadh annexation (1856) -> 1857 Uprising.",
         "While Dalhousie physically unified the map of British India, his ruthless disregard for indigenous feudal treaties transformed princes, peasants, and sepoys into revolutionary allies in 1857."),

        ("mains_mod_004", "british-economic-impact", 15, 250, True, "UPSC CSE 2014 GS-1", "Bipan Chandra; Dadabhai Naoroji",
         "Dadabhai Naoroji's 'Drain of Wealth' theory unmasked the predatory nature of British colonial exploitation. Discuss its mechanisms and profound influence on early Indian nationalism.",
         "In his pioneering 1901 work 'Poverty and Un-British Rule in India', Dadabhai Naoroji (the Grand Old Man of India) formulated the 'Drain of Wealth' theory, mathematically demonstrating that India was systematically bled of its capital without any commercial or material return.",
         [
             ("Mechanisms of the Drain", ["1. Home Charges: Expenses incurred in Britain on behalf of India, paid from Indian tax revenues. Included pensions and furloughs of civil/military officials, interest on guaranteed Indian public debt, and office expenses of the India Office in London.", "2. Guaranteed Interest on Railway Investments: British private investors were guaranteed a risk-free 5% return on capital investments in Indian railways, subsidized entirely by Indian taxpayers.", "3. Remittances by British Officials: Salaries, savings, and fortunes remitted home to Britain by British administrators, soldiers, and professionals.", "4. Profits of Foreign Capital: Repatriation of dividends and profits from British-dominated shipping, banking, tea plantations, and jute industries.", "5. Financing British Colonial Wars: Indian revenues financed British imperial expeditions in Afghanistan, Burma, China, and Africa."]),
             ("Destructive Socio-Economic Consequences", ["Depleted India of domestic investment capital, preventing indigenous industrial modernization and capital formation.", "R.C. Dutt in 'Economic History of India' calculated that nearly one-fourth of India's annual state revenue was drained abroad.", "Starved public services: negligible spending on irrigation, public health, and technical education, generating chronic agrarian famines."]),
             ("Catalyst for Early Nationalist Consciousness", ["Shattered the colonial myth of the 'White Man's Burden' and benevolent British paternalism.", "United diverse regional groups around a shared economic grievance, transforming intellectual discontent into the demand for 'Swaraj' (Self-Rule)."])
         ],
         "Flowchart of Drain: Indian Agrarian Revenues -> Home Charges / Remittances / Guaranteed Railway Dividends -> London -> Depletion of Indian Capital Formation.",
         "The Drain of Wealth theory was early nationalism's most devastating intellectual weapon, laying bare the parasitic economic architecture that impoverished an ancient civilization."),

        ("mains_mod_005", "british-economic-impact", 15, 250, True, "UPSC CSE 2018 GS-1", "Bipan Chandra, Ch. 7; NCERT Themes Theme 10",
         "Critically analyze the phenomenon of 'De-industrialization' in 19th-century colonial India. How did it lead to the 'ruralization' of the Indian economy?",
         "Before the advent of British rule, India was the world's workshop, supplying over a quarter of global textile manufacturing. The 19th century witnessed 'De-industrialization'—the catastrophic collapse of traditional urban handicrafts and handloom weaving without compensating modern industrialization.",
         [
             ("Causes of De-industrialization", ["1. Disappearance of Indigenous Royal Courts: British annexation of princely states eliminated royal courts and aristocratic nobles who were the primary patrons of luxury handicrafts (e.g., Dacca muslin, Murshidabad silk, Kashmir shawls).", "2. Asymmetric One-Way Free Trade: Following the Charter Act of 1813 (which abolished the Company's trade monopoly), British machine-made factory textiles from Manchester and Lancashire flooded India duty-free, while heavy import duties were imposed on Indian handloom exports entering Britain.", "3. Penetration of Indian Railways: The railway network penetrated deep into the rural hinterland, distributing cheap imported British manufactured goods to rural bazaars, decimating village artisans.", "4. Export of Raw Materials: India was systematically coerced into an exporter of agricultural raw materials (raw cotton, silk, jute) and an importer of finished British manufactured goods."]),
             ("Consequence: The 'Ruralization' of the Indian Economy", ["Millions of ruined urban weavers, spinners, dyers, blacksmiths, and potters lost their livelihoods and were forced onto the agrarian countryside.", "Created excessive, unsustainable pressure on agricultural land: the proportion of population dependent on agriculture rose from ~55% in the early 19th century to over 73% by 1901.", "Fragmented landholdings into uneconomic slivers, lowered agricultural wages, boosted rack-renting, and caused recurrent devastating famines."]),
             ("William Bentinck's Famous Observation", ["Governor-General Lord William Bentinck reported in 1834: 'The misery hardly finds a parallel in the history of commerce. The bones of the cotton-weavers are bleaching the plains of India.'"])
         ],
         "Flowchart: Factory Goods from Manchester -> Destruction of Urban Handlooms -> Artisan Flight to Villages -> Overcrowding on Land -> Ruralization & Famines.",
         "De-industrialization transformed India from a premier global manufacturing exporter into a destitute, de-urbanized agrarian colony subservient to British industrial capital."),

        ("mains_mod_006", "british-economic-impact", 15, 250, True, "UPSC CSE 2016 GS-1", "Bipan Chandra; Spectrum",
         "The 'Commercialization of Agriculture' in colonial India was not an organic economic modernization, but a forced process that intensified rural indebtedness and famines. Discuss.",
         "Beginning in the second half of the 19th century, Indian agriculture underwent 'Commercialization'—a shift from subsistence food crops (millets, pulses, wheat) to cash crops produced for global commodity markets (indigo, opium, cotton, jute, sugarcane, tea).",
         [
             ("Forced and Artificial Character of Commercialization", ["Peasants did not commercialize voluntarily out of agricultural profit; they were compelled by the state's exorbitant, inflexible cash land revenue demands.", "To pay cash taxes before official sunset deadlines, peasants were forced to take advance loans ('Dadan' system in indigo) from merchants and plant cash crops on their fertile food-growing plots."]),
             ("Vulnerability to Global Price Fluctuations", ["Integrated Indian peasants into volatile global capitalist markets without state buffer support.", "The American Civil War (1861-1865) sparked a speculative boom in Deccan raw cotton; when the war ended, American cotton flooded world markets, cotton prices crashed, but British colonial revenue was raised by 50%, triggering the historic Deccan Riots of 1875."]),
             ("Food Insecurity and Catastrophic Famines", ["Fertile lands diverted from food grains to cash crops caused localized food shortages.", "Even during catastrophic famines, British authorities continued exporting millions of tonnes of wheat and rice from India to Britain to preserve free-market orthodoxy (e.g., Orissa Famine 1866, Great Madras Famine 1876-78 under Lytton)."]),
             ("Grip of Village Moneylenders ('Mahajans')", ["Commercialization monetized rural transactions, empowering usurious moneylenders who charged 25% to 50% compound interest, using British courts and mortgage laws to seize mortgaged peasant lands."])
         ],
         "Cycle of Peasant Ruin: Fixed Cash Taxes -> Moneylender Advance -> Forced Cash Crops -> Global Market Crash -> Land Alienation & Famine.",
         "Far from generating agricultural prosperity, colonial commercialization was an extractive distortion that enriched British mercantile cartels while condemning Indian peasantry to chronic starvation and debt bondage."),

        ("mains_mod_007", "british-economic-impact", 15, 250, True, "UPSC CSE 2019 GS-1", "NCERT Themes Theme 10; Bipan Chandra",
         "Compare and contrast the Permanent Settlement (Zamindari), Ryotwari, and Mahalwari land revenue systems introduced by the British in India.",
         "To extract maximum agrarian wealth, the British instituted three distinct land revenue settlements across different geographic regions of colonial India, fundamentally restructuring agrarian property relations.",
         [
             ("1. Permanent Settlement of Bengal (1793 - Lord Cornwallis)", ["Geography: Bengal, Bihar, Orissa, parts of Northern Karnataka and Varanasi (~19% of British India).", "Mechanism: Recognized hereditary Zamindars as absolute proprietary owners of the soil, provided they paid a fixed revenue to the Company (10/11th to Company, 1/11th retained by Zamindar).", "Fixed Revenue & Sunset Law: State revenue was fixed permanently in perpetuity; if a Zamindar failed to pay by sunset on the appointed date, his estate was publicly auctioned.", "Social Impact: Created a loyal parasitic class of absentee landlords living in Calcutta who rack-rented and evicted helpless tenant-tillers."]),
             ("2. Ryotwari System (1820 - Thomas Munro and Captain Read)", ["Geography: Madras Presidency, Bombay Presidency, parts of Assam and Coorg (~51% of British India).", "Mechanism: Made settlement directly with individual peasant cultivators ('Ryots') without landed intermediaries.", "Features: Land surveyed and revenue fixed for 20-30 years (usually 50% to 60% of gross produce).", "Social Impact: Eliminated feudal Zamindars, but the colonial state itself emerged as a ruthless supreme landlord, resorting to coercive torture to extract exorbitant dues."]),
             ("3. Mahalwari System (1822/1833 - Holt Mackenzie and Robert Merttins Bird)", ["Geography: Gangetic Valley, North-Western Provinces (UP), Punjab, and parts of Central India (~30% of British India).", "Mechanism: Settlement made with the entire village community or estate ('Mahal') represented by the village headman (Lambardar/Taluqdar) who collected revenue jointly.", "Social Impact: High assessment pauperized communal villages, encouraging rural usury and leading to large-scale land sales to urban moneylenders."])
         ],
         "Three-column comparative matrix: Feature, Permanent Settlement, Ryotwari, Mahalwari (Coverage, Property Owner, Assessment Period, Exploitation Mechanism).",
         "Though different in form, all three British land revenue systems shared a common predatory objective: extracting maximum agrarian surplus, breaking traditional community safety nets, and impoverishing the Indian peasantry."),

        ("mains_mod_008", "tribal-and-peasant-uprisings", 15, 250, True, "UPSC CSE 2020 GS-1", "Bipan Chandra, Ch. 3; Spectrum",
         "Tribal uprisings in 19th-century colonial India were rooted in the disruption of their traditional socio-economic life by British forest laws and outsider exploitation ('Dikus'). Discuss with special reference to the Santhal Hool (1855-56) and Birsa Munda's Ulgulan (1899-1900).",
         "Isolated within forested habitats, India's indigenous tribal communities (Adivasis) enjoyed communal autonomy until British colonial expansion aggressively penetrated their domains, transforming forest commons into private commercial commodities and sparking violent uprisings.",
         [
             ("Core Drivers of Tribal Resistance", ["1. Influx of 'Dikus': British revenue systems introduced non-tribal moneylenders, traders, and revenue contractors who usurped tribal lands through fraud and usury.", "2. Colonial Forest Enactments: Indian Forest Acts (1865, 1878) categorized forests into 'Reserved' and 'Protected', criminalizing traditional tribal shifting cultivation (Jhum), cattle grazing, and collection of minor forest produce (Mahua, timber).", "3. Beth-Begari (Forced Unpaid Labour): Extraction of forced labour for building colonial roads, bridges, and railways."]),
             ("The Santhal Hool (1855-1856): Revolt in the Damin-i-Koh", ["Led by brothers Sidhu and Kanhu Murmu in the Rajmahal hills (Jharkhand/Bengal).", "Rebelled against the ruthless exploitation by Bengali moneylenders (Mahajans), zamindars, and corrupt police officials.", "Over 30,000 Santhals armed with bows, poisoned arrows, and battle-axes declared self-rule; crushed by British martial law, leading to the creation of the separate 'Santhal Parganas' district."]),
             ("Birsa Munda and the 'Ulgulan' (The Great Tumult, 1899-1900)", ["Erupted in the Chotanagpur plateau to protect the traditional communal landholding system ('Khuntkatti') against British zamindari encroachments.", "Birsa declared himself a divine messenger ('Bhagwan') and envisioned a 'Munda Raj' free of British rule, Christian missionaries, and Dikus.", "Fought guerrilla actions against colonial forces; Birsa died in Ranchi jail in 1900.", "Consequence: British enacted the Chotanagpur Tenancy Act (1908), legally banning the transfer of tribal lands to non-tribals."])
         ],
         "Flowchart: Colonial Forest Laws + Diku Influx -> Destruction of Khuntkatti & Jhum -> Tribal Alienation -> Armed Resistance (Santhal Hool, Birsa's Ulgulan) -> Tenancy Protection Acts.",
         "Tribal uprisings were the fiercest anti-colonial resistances of the 19th century: unyielding struggles to protect ancestral cultural identity, communal ecology, and sacred freedom against imperial dispossession.")
    ]

    # Let's generate items 9 to 60 systematically
    # We will append the remaining 52 questions covering all topics listed above
    more_mod = [
        ("mains_mod_009", "revolt-of-1857", 15, 250, True, "UPSC CSE 2015 GS-1", "Bipan Chandra, Ch. 4; NCERT Themes Theme 10",
         "The Revolt of 1857 was the culmination of a century of brewing discontent against British colonial rule. Analyze its political, economic, military, and socio-religious causes.",
         "The rebellion of 1857 was not a sudden unprovoked mutiny over greased cartridges, but the violent explosion of deep-seated grievances accumulated over a century of British misrule.",
         [
             ("Political Grievances", ["Dalhousie's Doctrine of Lapse annexed ancient dynasties (Satara, Jhansi, Nagpur) and stopped Nana Saheb's pension.", "The annexation of Awadh in 1856 on charges of misgovernance disgraced the Nawab and dispossessed 21,000 taluqdars."]),
             ("Economic Exploitation", ["Exorbitant land revenue settlements ruined peasants; moneylenders foreclosed on ancestral holdings.", "De-industrialization annihilated artisanal livelihoods, throwing millions into poverty."]),
             ("Military Discontent in the Bengal Army", ["High-caste sepoys (Brahmanas and Rajputs) deeply resented service overseas across the 'Kala Pani' (General Service Enlistment Act 1856), which breached caste purity.", "Severe racial discrimination: Indian soldiers were paid meager wages, denied officer promotions (highest rank open was Subedar), and subjected to racial slurs."]),
             ("Socio-Religious Fears and the Greased Cartridges", ["Enactments like the Religious Disabilities Act (1850), Widow Remarriage Act (1856), and activities of Christian missionaries stoked fears of forced conversion.", "The immediate trigger: Enfield rifle paper cartridges greased with animal fat (beef and pork fat), violating religious taboos of Hindu and Muslim sepoys."])
         ],
         "Fishbone diagram of 1857 causes: Political (Lapse, Awadh) + Economic (Taxes, De-industrialization) + Military (Kala Pani, Racial bias) + Immediate trigger (Enfield cartridges).",
         "The Revolt of 1857 brought diverse disaffected segments of Indian society together in an unprecedented, heroic bid to expel foreign colonial masters."),

        ("mains_mod_010", "revolt-of-1857", 15, 250, True, "UPSC CSE 2016 GS-1", "Bipan Chandra; V.D. Savarkar",
         "Critically examine the historiographical debate regarding the nature of the Revolt of 1857. Was it a mere 'Sepoy Mutiny' or India's 'First War of Independence'?",
         "The historical character of the Revolt of 1857 remains intensely contested across colonial, nationalist, Marxist, and revisionist paradigms.",
         [
             ("Colonial Historiography: The 'Sepoy Mutiny' Thesis", ["Sir John Lawrence and Sir John Kaye portrayed it as a 'wholly unpatriotic and selfish Sepoy Mutiny with no native leadership and no popular support.'", "Argued that the rebellion was confined to disgruntled soldiers over religious cartridges, minimizing popular civil participation in Awadh and Bihar."]),
             ("Nationalist Perspective: The 'First War of Independence'", ["V.D. Savarkar in 1909 christened it 'The Indian War of Independence of 1857'.", "Argued that sepoys were the vanguard of an all-India liberation war; highlighted remarkable Hindu-Muslim unity (Bahadur Shah Zafar declared Emperor; cow slaughter banned during the uprising in Delhi and Awadh)."]),
             ("Marxist and Subaltern Reinterpretation", ["Marxist historians (K.M. Panikkar, R.C. Majumdar) argued that the leaders (Nana Saheb, Lakshmibai, Begum Hazrat Mahal, Kunwar Singh) were dying feudal aristocrats fighting to regain lost personal privileges ('a dying groan of an obsolete aristocracy').", "Subaltern historians emphasize massive grassroots peasant and artisan participation: in Awadh, over 100,000 civilians died fighting alongside the sepoys."])
         ],
         "Spectrum chart: Colonial view (Selfish sepoy mutiny) <---> Marxist view (Feudal reaction) <---> Nationalist view (First War of National Independence).",
         "While lacking modern democratic nationalism, the 1857 uprising was far more than a military mutiny: it was India's first collective subcontinental anti-colonial armed insurrection."),

        ("mains_mod_011", "socio-religious-reform", 15, 250, True, "UPSC CSE 2019 GS-1", "Bipan Chandra, Ch. 6; Spectrum",
         "Raja Ram Mohan Roy is rightfully acclaimed as the 'Father of Modern Indian Renaissance'. Examine his multifaceted contributions to social reform, rationalism, and free press.",
         "Raja Ram Mohan Roy (1772-1833) inaugurated the modern era in India by synthesizing Western rational enlightenment with pristine Upanishadic monotheism, launching a multi-front assault on dogma.",
         [
             ("Crusade for Women's Rights and Abolition of Sati", ["Citing ancient Hindu scriptures, proved that Sati (widow burning) had no Vedic sanction.", "Persuaded Governor-General Lord William Bentinck to pass the historic Regulation XVII of 1829, criminalizing Sati as culpable homicide.", "Advocated widow remarriage, denounced polygamy, and demanded inheritance and property rights for women."]),
             ("Rationalism and Monotheism: The Brahmo Samaj", ["Authored 'Tuhfat-ul-Muwahhidin' (A Gift to Monotheists) in Persian, attacking idolatry, priestcraft, and superstition.", "Founded the 'Atmiya Sabha' (1815) and 'Brahmo Samaj' (1828) dedicated to the worship of the one formless supreme reality ('Brahman')."]),
             ("Educational Modernization and Free Press", ["Supported Western scientific education, assisting David Hare to establish the Hindu College at Calcutta (1817) and founding the Vedanta College (1825).", "Pioneer of Indian journalism: edited 'Sambad Kaumudi' (Bengali) and 'Mirat-ul-Akhbar' (Persian); petitioned the Supreme Court against the Press Regulations of 1823, defending free speech as the lifeblood of progress."])
         ],
         "Pillars of Roy's Renaissance: Sati Abolition (1829), Brahmo Samaj Monotheism (1828), Western Scientific Education, Freedom of the Press.",
         "Raja Ram Mohan Roy laid the intellectual bridge from medieval religious scholasticism to modern humanistic rationalism, awakening the conscience of modern India."),

        ("mains_mod_012", "socio-religious-reform", 15, 250, True, "UPSC CSE 2021 GS-1", "Spectrum Modern India; Gail Omvedt",
         "Jyotirao Phule and Savitribai Phule pioneered a radical anti-caste and feminist revolution in 19th-century Maharashtra. Analyze their legacy with reference to the Satyashodhak Samaj.",
         "Jyotirao Govindrao Phule (1827-1890) and his wife Savitribai Phule launched South Asia's first subaltern social revolution, dismantling Brahminical hegemony and pioneering education for untouchables and women.",
         [
             ("Educational Pioneers for Dalits and Women", ["In 1848, Jyotirao and Savitribai opened India's first school for girls from untouchable castes at Bhide Wada in Pune.", "Savitribai, despite severe verbal and physical abuse from orthodox conservatives (who hurled mud and cow-dung at her), persevered to educate thousands of low-caste girls."]),
             ("Critique of Brahminical Hegemony: 'Gulamgiri'", ["In his seminal treatise 'Gulamgiri' (Slavery, 1873), Phule dedicated the book to the American abolitionist movement fighting Negro slavery.", "Deconstructed Hindu mythology: reinterpreted the avatar of Vamana not as a divine hero, but as an Aryan invader who deceitfully murdered the indigenous righteous king Raja Bali."]),
             ("The Satyashodhak Samaj (Truth-Seekers' Society)", ["Founded in 1873 to liberate Shudras and Ati-Shudras from priestly exploitation and religious deception.", "Conducted marriages without Brahmin priests, reciting simple Marathi oaths of mutual respect and equality.", "Founded the 'Balhatya Pratibandhak Griha' (Infanticide Prohibition Home) in 1863 to provide sanctuary and care for pregnant Brahmin widows and their children."])
         ],
         "Triad of Phule's Revolution: Female Education (Bhide Wada 1848) + Anti-Caste Theory (Gulamgiri) + Institutional Counter-Hegemony (Satyashodhak Samaj).",
         "The Phules ignited India's modern anti-caste movement, inspiring Dr. B.R. Ambedkar and enshrining universal education as the supreme instrument of human emancipation."),

        ("mains_mod_013", "socio-religious-reform", 10, 150, False, "Standard Practice", "Spectrum; NCERT",
         "Differentiate between the reformist and revivalist socio-religious movements of 19th-century India with suitable examples.",
         "The socio-religious ferment of 19th-century India manifested in two distinct currents: reformist movements seeking structural modernization and revivalist movements seeking ideological rejuvenation from ancient roots.",
         [
             ("Reformist Movements (Embracing Modern Rationalism)", ["Approach: Looked outward and forward, synthesizing Indian philosophy with Western liberal rationalism, scientific humanism, and secular education.", "Key Examples: Brahmo Samaj (Raja Ram Mohan Roy), Prarthana Samaj (Atmaram Pandurang, M.G. Ranade), and Young Bengal Movement (Henry Vivian Derozio).", "Major Focus: Abolition of Sati, promotion of widow remarriage, modern English education, and women's legal rights."]),
             ("Revivalist Movements (Reclaiming Ancient Purity)", ["Approach: Looked inward and backward to ancient scriptural golden ages, seeking to purge medieval degeneration and defend indigenous culture against Western Christian missionary encroachment.", "Key Examples: Arya Samaj (Swami Dayananda Saraswati: 'Go Back to the Vedas'), Deoband Movement (orthodox Islamic revival), and Ramakrishna Mission.", "Major Focus: Dayananda rejected Puranic idol-worship and caste-by-birth while defending the infallibility of the Vedas and launching the Shuddhi movement (re-conversion)."])
         ],
         "Comparative spectrum: Reformist (Brahmo Samaj, Modern synthesis, Rationalism) vs Revivalist (Arya Samaj, Vedic purity, Cultural defense).",
         "Despite differing ideological postures, both reformist and revivalist currents shared a common nationalist mission: rejuvenating Indian society to resist colonial subjugation."),

        ("mains_mod_014", "early-nationalism", 15, 250, True, "UPSC CSE 2017 GS-1", "Bipan Chandra, Ch. 5; Spectrum",
         "The 'Safety Valve' theory regarding the formation of the Indian National Congress in 1885 is historically untenable. Critically analyze in the light of the 'Lightning Conductor' hypothesis.",
         "The foundation of the Indian National Congress (INC) in Bombay in December 1885 by retired British civil servant Allan Octavian Hume sparked the long-standing 'Safety Valve' debate.",
         [
             ("The 'Safety Valve' Theory and Its Flaws", ["Propounded initially by Lala Lajpat Rai (Young India) and later adopted by Marxist historian R.P. Dutt.", "Argued that Viceroy Lord Dufferin and Hume orchestrated the Congress as a political safety-valve to release growing popular peasant discontent, pre-empting another armed explosion like 1857.", "Historical Refutation: Bipan Chandra demonstrated that Dufferin did not support Hume's political scheme and subsequently ridiculed the Congress as representing only a 'microscopic minority' of the educated elite."]),
             ("Gokhale's 'Lightning Conductor' Hypothesis", ["Gopal Krishna Gokhale articulated that early Indian nationalists intentionally used Hume as a 'Lightning Conductor'.", "Had an Indian founded the Congress in 1885, the suspicious British colonial government would have banned and suppressed the organization immediately.", "Hume's European background shielded the nascent political body from state suppression, giving early nationalists crucial time to build an all-India platform."]),
             ("Organic Evolution of Subcontinental Political Awakening", ["The Congress was not born overnight in a vacuum; it was the natural culmination of earlier provincial political associations: Poona Sarvajanik Sabha (1870), Indian Association of Calcutta (Surendranath Banerjee, 1876), Madras Mahajana Sabha (1884), and Bombay Presidency Association (1885)."])
         ],
         "Historical debate diagram: Safety Valve Theory (Colonial conspiracy to defuse mass unrest) vs Lightning Conductor Reality (Nationalist strategy utilizing Hume to evade suppression).",
         "The creation of the Congress was the organic fruit of emerging subcontinental national consciousness, astutely employing Hume to establish a permanent political bridge for freedom."),

        ("mains_mod_015", "early-nationalism", 15, 250, True, "UPSC CSE 2018 GS-1", "Bipan Chandra, Ch. 8; Spectrum",
         "Assess the contributions and limitations of the Moderate phase of the Indian National Congress (1885-1905). Did their 'politics of mendicancy' fail the Indian people?",
         "Led by luminaries such as Dadabhai Naoroji, Pherozeshah Mehta, Gopal Krishna Gokhale, and Surendranath Banerjee, the Moderate phase laid the ideological and institutional foundations of Indian nationalism.",
         [
             ("Substantive Contributions of the Moderates", ["1. Comprehensive Economic Critique: Naoroji, R.C. Dutt, and G.V. Joshi formulated the drain of wealth and de-industrialization critiques, proving that British rule was the root cause of Indian poverty.", "2. Constitutional Agitation & Institution Building: Believed in legal constitutional methods: Public meetings, Petitions, Memoranda, and Press ('3 Ps: Prayer, Petition, Protest').", "3. Expansion of Legislative Councils: Achieved the Indian Councils Act of 1892, securing the right to discuss the budget and question the executive.", "4. Democratic Consciousness: Nurtured subcontinental political unity, training citizens in modern democratic debate and public life."]),
             ("Inherent Limitations: The 'Politics of Mendicancy'", ["Extremists (Tilak, Bipin Chandra Pal) criticized their methods as 'Political Mendicancy' (begging for constitutional crumbs).", "Narrow Social Base: Confined strictly to English-educated urban lawyers, journalists, and zamindars; lacked mass contact with peasants, industrial workers, and the rural masses.", "Naive Faith in British Justice: Believed that British rule was basically providential and benevolent, and that British democracy would grant self-rule once properly informed of Indian grievances."])
         ],
         "Balance matrix: Historic Achievements (Economic critique, Pan-Indian unity, Councils Act 1892) vs Flaws (Narrow elitist base, Begging petitions, Fear of mass action).",
         "While the Moderates failed to mobilize the masses, they sowed the seeds of national consciousness and created the political apparatus without which the subsequent Gandhian mass movements would have been impossible."),

        ("mains_mod_016", "swadeshi-movement", 15, 250, True, "UPSC CSE 2014 GS-1", "Bipan Chandra, Ch. 10; Sumit Sarkar",
         "The Swadeshi Movement (1905-1908) was a watershed epoch that witnessed the birth of modern mass political techniques in India. Discuss.",
         "Announced by Lord Curzon in July 1905 to divide Bengal along communal lines (Muslim East Bengal vs Hindu West Bengal) and crush the nerve-center of nationalism, the Partition of Bengal ignited the historic Swadeshi and Boycott Movement.",
         [
             ("Evolution of Novel Political Techniques", ["1. Boycott of Foreign Goods: Public bonfires of Manchester cloth, foreign salt, and sugar; picketing of shops by students and women.", "2. Passive Resistance and Non-Cooperation: Aurobindo Ghosh and Bal Gangadhar Tilak articulated the doctrine of boycotting British schools, courts, and civil offices—prefiguring Gandhi's Non-Cooperation.", "3. Mass Processions and Cultural Symbolism: Rabindranath Tagore composed 'Amar Sonar Bangla' and introduced the 'Raksha Bandhan' festival, where Hindus and Muslims tied rakhis on each other's wrists in hundreds of thousands to symbolize indivisible brotherhood."]),
             ("Constructive Swadeshi and National Institutions", ["National Education: Founded the National Council of Education (1906) and Bengal National College under Aurobindo Ghosh to replace colonial government schools.", "Swadeshi Enterprises: Established indigenous textile mills, national banks, soap and match factories (Prafulla Chandra Ray founded Bengal Chemical and Pharmaceutical Works).", "Samitis for Grassroots Mobilization: Ashwini Kumar Dutta's Swadesh Bandhab Samiti in Barisal mobilized hundreds of thousands of villagers, providing famine relief, arbitration courts, and patriotic physical training."]),
             ("Internal Limitations and Communal Rift", ["The movement failed to draw in the Muslim peasantry of East Bengal on a permanent basis, as colonial administrators successfully wooed conservative Muslim elites, culminating in the founding of the All-India Muslim League at Dacca in 1906."])
         ],
         "Multi-dimensional map of Swadeshi: Economic Boycott + Constructive Enterprises + National Education + Cultural Renaissance (Tagore, Abanindranath) = Precursor to Gandhian Era.",
         "The Swadeshi Movement transformed Indian politics forever: it shattered the politics of prayer, brought students and women onto the streets, and made 'Swaraj' the non-negotiable goal of the freedom struggle.")
    ]

    # Let's add remaining 44 questions in structured format
    # Topics 17 to 60
    # Let's generate them programmatically to ensure complete coverage up to 60 items
    topics_44 = [
        ("mains_mod_017", "swadeshi-movement", 10, 150, True, "UPSC CSE 2015 GS-1", "Bipan Chandra, Ch. 11",
         "Analyze the causes and disastrous consequences of the Surat Split of 1907 for the Indian national movement.",
         "The Surat session of the INC in December 1907 witnessed an irreparable schism between Moderates and Extremists, crippling the nationalist movement for nearly a decade.",
         [("Ideological and Tactical Fault-Lines", ["Extremists (Tilak, Lala Lajpat Rai) demanded extending the Swadeshi and Boycott movement across all of India and boycotting all colonial institutions.", "Moderates (Gokhale, Pherozeshah Mehta) insisted on confining boycott strictly to Bengal and foreign goods, fearing government suppression and council disqualifications."]),
          ("The Clash at Surat", ["Disputes erupted over the Congress presidency (Lajpat Rai vs Rash Behari Ghosh); session descended into violent chaos with flying chairs and shoes."]),
          ("Disastrous Consequences", ["The British government unleashed severe repression: Tilak was sentenced to 6 years imprisonment in Mandalay (Burma); Aurobindo retreated to Pondicherry.", "The truncated Moderate Congress became an ineffective political body, while the absence of open agitation encouraged underground revolutionary terrorism."])],
         "Flowchart: Moderate vs Extremist rift -> Surat Split (1907) -> British repression (Tilak jailed) -> 10-year political paralysis.",
         "The Surat Split was a pyrrhic blunder that temporarily paralyzed the national movement, only resolved a decade later at the 1916 Lucknow session."),

        ("mains_mod_018", "revolutionary-nationalism", 10, 150, False, "Standard Practice", "Bipan Chandra, Ch. 12",
         "Examine the ideology, methods, and limitations of the first phase of Revolutionary Terrorism (1897-1915).",
         "Frustrated by Moderate mendicancy and brutal government suppression of Swadeshi, educated youth turned to heroic individual assassination to intimidate colonial administrators.",
         [("Secret Societies and Assassinations", ["Anushilan Samiti (Calcutta and Dacca) and Jugantar: Barindra Kumar Ghosh and Bhupendranath Dutta.", "Abhinav Bharat (Maharashtra): Founded by V.D. Savarkar in 1904.", "Targeted assassinations of notorious colonial officials: Chapekar brothers shot Rand (1897); Khudiram Bose and Prafulla Chaki threw bombs at Kingsford (1908); Madan Lal Dhingra assassinated Curzon Wyllie in London (1909)."]),
          ("Underlying Ideology", ["Inspired by Russian nihilists and Italian Carbonari; aimed at striking terror into British rulers and arousing national pride through personal martyrdom."]),
          ("Structural Limitations", ["Completely lacked mass peasant and worker involvement; operated as isolated middle-class intellectual conspiracies.", "Failed to counter heavy state surveillance and colonial treason trials (Alipore Bomb Conspiracy)."])],
         "Network map: Maharashtra (Chapekar/Savarkar) <--> Bengal (Anushilan/Jugantar) <--> Punjab (Ajit Singh) <--> London (India House).",
         "Though incapable of overthrowing British rule by force, early revolutionaries infused the national movement with supreme courage, self-sacrifice, and patriotic romanticism."),

        ("mains_mod_019", "early-nationalism", 10, 150, True, "UPSC CSE 2020 GS-1", "Spectrum Modern India",
         "The Morley-Minto Reforms (1909) introduced the poison of communal electorates into Indian politics. Discuss.",
         "Enacted as the Indian Councils Act 1909, the Morley-Minto Reforms expanded legislative councils but introduced the insidious principle of separate communal electorates.",
         [("Separate Electorates for Muslims", ["Created exclusive Muslim constituencies where only Muslim voters could vote for Muslim candidates, legally codifying religious identity as the basis of political franchise.", "Conferred disproportionate weightage to Muslims relative to their population proportion."]),
          ("Imperial Objective: Divide and Rule", ["Designed to drive an institutional wedge between Hindus and Muslims, isolating the Congress from the newly established Muslim League (1906).", "Lord Minto confessed: 'We are sowing dragon's teeth, and the harvest will be bitter.'"]),
          ("Tragic Long-Term Ramifications", ["Prevented inter-communal political convergence, institutionalizing communal separatism that culminated 38 years later in the tragic Partition of India."])],
         "Vector diagram: Morley-Minto Separate Electorates (1909) -> Communal Polarization -> Two-Nation Theory -> Partition (1947).",
         "The 1909 reforms were an imperial act of constitutional sabotage that sacrificed India's organic communal harmony to preserve colonial longevity."),

        ("mains_mod_020", "revolutionary-nationalism", 10, 150, False, "Standard Practice", "Bipan Chandra, Ch. 13",
         "Evaluate the contributions of the Ghadar Movement (1913) to India's freedom struggle. Why did its armed rebellion fail?",
         "Founded in 1913 in San Francisco by Lala Har Dayal, Sohan Singh Bhakna, and Kartar Singh Sarabha, the Ghadar Party was a revolutionary secular organization of overseas Indian immigrants.",
         [("Ideology and Global Revolutionary Mobilization", ["Published the weekly journal 'Ghadar' (Revolt) preaching armed revolution: 'Wanted: Enthusiastic and heroic soldiers for the Ghadar in India; Pay: Death; Price: Martyrdom; Field: India.'", "Stood for complete secularism: united Punjabi Sikhs, Muslims, and Hindus against British imperialism.", "The Komagata Maru tragedy (1914) radicalized thousands of immigrant Sikhs to return to India to launch an armed insurrection."]),
          ("Failure of the February 1915 Rebellion", ["Rushed returnees were infiltrated by British spies and informers (e.g., Kirpal Singh).", "Rash Behari Ghosh and Sachin Sanyal coordinated the mutiny plan, but British authorities arrested top leaders in pre-emptive strikes.", "Crushed under the Defense of India Act 1915, leading to Lahore Conspiracy trials and executions."])],
         "Global route map: San Francisco / Vancouver -> Komagata Maru journey -> Budge Budge clash -> Punjab rebellion aborted.",
         "The Ghadarites were secular internationalist martyrs whose courage proved that expatriate Indians across the globe were united in the struggle for Indian freedom.")
    ]

    # Combine into qs
    all_raw = qs_raw + more_mod + topics_44

    # Let's generate up to mains_mod_060
    # Let's build a dedicated generator function that adds items up to 60
    items = []
    for item in all_raw:
        items.append({
            "id": item[0],
            "category": "modern",
            "categoryLabel": "Modern India",
            "periodId": item[1],
            "marks": item[2],
            "wordLimit": item[3],
            "isPyq": item[4],
            "yearSource": item[5],
            "bookRef": item[6],
            "question": item[7],
            "framework": {
                "intro": item[8],
                "body": [{"heading": b[0], "points": b[1]} for b in item[9]],
                "diagramMapIdea": item[10],
                "conclusion": item[11]
            }
        })

    # Now let's add questions mains_mod_021 to mains_mod_060 (40 questions)
    modern_40 = [
        ("mains_mod_021", "Home Rule League Movement (Tilak and Annie Besant)", "early-nationalism", 10, 150, "Bipan Chandra, Ch. 14",
         "The Home Rule League movement (1916) revitalized Indian nationalism and created the popular organizational base for subsequent Gandhian mass movements. Discuss.",
         "Launched during World War I by Bal Gangadhar Tilak and Annie Besant, the Home Rule movement revived Indian political momentum after the post-Surat depression.",
         [("Two Distinct Spheres of Mobilization", ["Tilak's League: Operated in Maharashtra (excluding Bombay city), Karnataka, Central Provinces, and Berar with 6 branches.", "Besant's League: Covered the rest of India with over 200 branches.", "Propagated self-government ('Home Rule') using libraries, reading rooms, political leaflets, and vernacular tours."]),
          ("Tilak's Famous Proclamation and Methods", ["Proclaimed: 'Swaraj is my birthright and I shall have it.'", "Popularized vernacular education and linguistic reorganization of provinces."]),
          ("Catalyst for Unity and Institutional Transformation", ["Pressured Congress to reunite Moderates and Extremists at Lucknow (1916).", "Trained a cadre of young organizers (Jawaharlal Nehru, Motilal Nehru, B.P. Wadia, Shankarlal Banker) who formed the vanguard of Gandhi's Non-Cooperation Movement."])],
         "Map of Home Rule jurisdictions: Tilak's domain (Maharashtra, Karnataka, CP/Berar) vs Besant's pan-India domain.",
         "The Home Rule movement was the bridge between elite constitutionalism and mass agitation, awakening political consciousness across towns and villages."),

        ("mains_mod_022", "Lucknow Pact (1916): Significance and Structural Flaws", "early-nationalism", 10, 150, "Spectrum; Bipan Chandra",
         "The Lucknow Pact (1916) marked the zenith of Congress-League rapprochement, but conceded fatal communal principles. Critically evaluate.",
         "At Lucknow in 1916, the Indian National Congress and the All-India Muslim League concluded the historic 'Lucknow Pact', jointly presenting constitutional demands to the British government.",
         [("Historic Achievements of Unity", ["Facilitated the reunion of Moderates and Extremists after a nine-year rupture since Surat (1907).", "Forged a united Hindu-Muslim political front demanding Dominion Status and elected majorities in legislative councils."]),
          ("The Fatal Flaw: Legitimizing Separate Electorates", ["Congress officially accepted separate communal electorates for Muslims, conceding that Hindus and Muslims formed separate political entities with divergent interests.", "Agreed to weighted Muslim representation in provincial councils where they were in minority, without reciprocal safeguards in majority provinces (Bengal, Punjab)."]),
          ("Long-Term Repercussions", ["Conferred elite institutional legitimacy on communal bargaining, paving the way for escalating communal demands rather than secular joint citizenship."])],
         "Balance diagram: Immediate Strength (United anti-colonial front) vs Fatal Legacy (Official Congress legitimization of Separate Electorates).",
         "The Lucknow Pact was a tactical triumph of short-term anti-imperial unity, but a strategic surrender to communal separatism."),

        ("mains_mod_023", "Montagu-Chelmsford Reforms (1919) and Provincial Dyarchy", "early-nationalism", 10, 150, "Spectrum Modern India",
         "Explain the structural mechanics of 'Dyarchy' introduced by the Government of India Act 1919 and discuss why it failed in operation.",
         "Enacted under the Montagu-Chelmsford Reforms, the Government of India Act 1919 introduced 'Dyarchy' (rule by two authorities) in the provincial executive.",
         [("The Bifurcated Provincial Executive", ["Transferred Subjects: Administered by Indian Ministers responsible to the elected provincial legislative council (e.g., Education, Public Health, Agriculture, Local Self-Government).", "Reserved Subjects: Administered by the Governor and his non-responsible bureaucratic Executive Council (e.g., Law and Order, Police, Justice, Finance, Land Revenue)."]),
          ("Why Dyarchy Failed in Practice", ["Ministers had administrative responsibility without financial purse-strings: the finance portfolio was kept under the Governor's reserved council.", "Governor held overriding veto powers over ministerial legislation and appointments.", "Permanent civil servants (ICS) bypassed Indian ministers, taking orders directly from the Governor."])],
         "Dyarchy structural diagram: Governor -> Reserved Subjects (Police/Finance: Autocratic) vs Transferred Subjects (Education/Health: Responsible to Assembly).",
         "Dyarchy was an unworkable constitutional gimmick that granted the shadow of responsibility while withholding the substance of power."),

        ("mains_mod_024", "Gandhi's Early Satyagrahas: Champaran, Kheda, and Ahmedabad", "gandhian-era", 15, 250, "Bipan Chandra, Ch. 15",
         "Champaran (1917), Ahmedabad (1918), and Kheda (1918) served as the experimental laboratory for Mahatma Gandhi's techniques of Satyagraha. Elucidate.",
         "Upon returning from South Africa in 1915, Mahatma Gandhi spent his first years studying Indian realities on Gokhale's advice, applying his techniques of truth (Satya) and non-violence (Ahimsa) in three localized agrarian and labour struggles.",
         [("Champaran Satyagraha (1917): Civil Disobedience Against Tinkathia", ["Peasants were forced by European planters to cultivate indigo on 3/20th ('Tinkathia') of their holdings.", "Invited by Rajkumar Shukla, Gandhi arrived in Champaran. When ordered to leave by the British magistrate, he refused, pioneering civil disobedience on Indian soil.", "Government appointed an inquiry committee with Gandhi as a member; Tinkathia was abolished and planters refunded 25% of extorted money."]),
          ("Ahmedabad Mill Strike (1918): Non-Violent Fasting for Labour Rights", ["Dispute between textile mill owners and workers over the withdrawal of the Plague Bonus.", "Gandhi guided workers to demand a 35% wage hike and undertook his first hunger strike unto death.", "Mill owners conceded, establishing the principle of collective arbitration."]),
          ("Kheda Satyagraha (1918): Non-Cooperation and Peasant Solidarity", ["Severe crop failure in Gujarat entitled peasants to revenue remission under the revenue code, but authorities demanded full collection.", "Gandhi and Vallabhbhai Patel advised peasants to withhold revenue ('No-Tax Satyagraha').", "Government issued secret orders to collect taxes only from those who could pay."])],
         "Triangular matrix: Champaran (First Civil Disobedience), Ahmedabad (First Hunger Strike), Kheda (First Non-Cooperation).",
         "These three victories demonstrated that non-violent Satyagraha was practically viable on Indian soil, forging Gandhi's organic connection with peasants and working masses."),

        ("mains_mod_025", "Rowlatt Act and Jallianwala Bagh Massacre (1919)", "gandhian-era", 15, 250, "Bipan Chandra, Ch. 16",
         "The Rowlatt Satyagraha and the Jallianwala Bagh massacre shattered India's faith in British constitutional justice. Analyze their historical significance.",
         "In early 1919, the imperial government passed the Anarchical and Revolutionary Crimes Act (Rowlatt Act), authorizing detention of political suspects without trial for two years, famously denounced as 'No Dalil, No Vakil, No Appeal'.",
         [("The Rowlatt Satyagraha: India's First Pan-Indian Hartal", ["Gandhi launched the 'Rowlatt Satyagraha Sabha', organizing a nationwide non-violent general strike ('Hartal') on 6 April 1919.", "Marked Gandhi's transformation from a local reformer into the unquestioned leader of pan-Indian mass nationalism."]),
          ("The Jallianwala Bagh Massacre (13 April 1919)", ["Protesting the arrest of beloved Punjab leaders Dr. Saifuddin Kitchlew and Dr. Satyapal on Baisakhi day in Amritsar.", "Brigadier-General Reginald Dyer blocked the only narrow exit of Jallianwala Bagh and ordered troops to fire without warning on an unarmed crowd of 20,000 men, women, and children for 10 minutes until ammunition was exhausted.", "Hunter Commission white-washed Dyer's war crime, while the British House of Lords hailed him as the 'Saviour of the Punjab'."]),
          ("Historic Watershed in Indo-British Relations", ["Rabindranath Tagore renounced his British Knighthood in moral protest ('The time has come when badges of honour make our shame glaring').", "Gandhi returned his Kaiser-i-Hind gold medal, proclaiming that 'cooperation with this satanic government is impossible', paving the way for the Non-Cooperation Movement."])],
         "Flowchart: Rowlatt Act -> Nationwide Hartal -> Dyer's Jallianwala Massacre -> Hunter Commission whitewash -> Launch of Non-Cooperation Movement (1920).",
         "Jallianwala Bagh permanently tore away the moral mask of British benevolence, convincing millions of Indians that complete liberation was the only honourable path."),

        ("mains_mod_026", "Non-Cooperation Movement (1920-1922) and Chauri Chaura", "gandhian-era", 15, 250, "Bipan Chandra, Ch. 16-17",
         "Examine the socio-political dynamics of the Non-Cooperation Movement. Why did Mahatma Gandhi abruptly withdraw the movement following the Chauri Chaura incident?",
         "Launched at the Special Calcutta Congress (September 1920) and ratified at Nagpur (December 1920), the Non-Cooperation and Khilafat Movement was India's first genuine mass anti-colonial upheaval.",
         [("Multi-Layered Tactics of Non-Cooperation", ["1. Surrender of titles, honours, and honorary offices.", "2. Boycott of government schools, colleges, and law courts (lawyers like C.R. Das, Motilal Nehru, Rajendra Prasad suspended lucrative practices).", "3. Boycott of foreign cloth: Value of foreign cloth imports dropped from Rs 102 crore to Rs 57 crore.", "4. Promotion of Charkha, Khadi, and national educational institutions (Kashi Vidyapith, Jamia Millia Islamia, Gujarat Vidyapith)."]),
          ("Mass Social Base and Subaltern Mobilization", ["Brought together peasants (Awadh Kisan Sabha), tribal forest protestors (Alluri Sitarama Raju in Andhra), students, and urban working classes.", "Achieved unprecedented Hindu-Muslim solidarity under the joint banner of Non-Cooperation and the Khilafat cause."]),
          ("The Chauri Chaura Tragedy (4 February 1922) and Withdrawal", ["In Gorakhpur district (UP), police fired on a peaceful peasant procession; an infuriated mob attacked and burnt the police station, killing 22 policemen.", "Gandhi immediately called a meeting of the Congress Working Committee at Bardoli on 12 February 1922 and unconditionally withdrew the entire national movement."]),
          ("Strategic Rationale Behind Withdrawal", ["Subhash Chandra Bose and young leaders condemned the withdrawal as a 'national calamity'.", "However, Gandhi understood that an unarmed mass movement cannot remain peaceful once the state has moral justification to unleash brutal violent retaliation. He wanted to preserve the movement's moral discipline."])],
         "Crisis timeline: Nagpur Congress (1920) -> Nationwide boycott & Khadi -> Chauri Chaura violence (Feb 1922) -> Bardoli Resolution of withdrawal.",
         "Though suspended abruptly, Non-Cooperation transformed the Congress from an elite debating club into a mass revolutionary movement that permanently shattered the fear of British colonial authority."),

        ("mains_mod_027", "Swarajists vs No-Changers (1922-1924)", "gandhian-era", 10, 150, "Bipan Chandra, Ch. 18",
         "Differentiate between the political strategies of the 'Swarajists' and the 'No-Changers' following the suspension of the Non-Cooperation Movement.",
         "The sudden withdrawal of Non-Cooperation in 1922 and Gandhi's subsequent imprisonment caused deep demoralization, splitting Congress into Swarajists and No-Changers.",
         [("Swarajists: Council Entry and 'Wrecking from Within'", ["Led by Chittaranjan Das and Motilal Nehru; founded the Congress-Khilafat Swarajya Party in January 1923.", "Strategy: End the boycott of legislative councils. Enter the councils to 'wreck the reforms from within', expose the autocratic nature of colonial dyarchy, and obstruct government budgets.", "Achievements: Voted down official budgets; Vithalbhai Patel was elected President (Speaker) of the Central Legislative Assembly in 1925."]),
          ("No-Changers: Constructive Grassroots Work", ["Led by C. Rajagopalachari, Vallabhbhai Patel, Rajendra Prasad, and M.A. Ansari.", "Strategy: Opposed council entry as an illusion that would co-opt leaders into colonial parliamentarism.", "Focused on Gandhi's constructive program: spinning Khadi, eradicating untouchability, national schools, and Hindu-Muslim unity, quietly preparing the grassroots for the next mass struggle."])],
         "Bifurcation chart: Post-1922 Impasse -> Swarajists (Council entry, Parliamentary obstruction) vs No-Changers (Constructive village work, Anti-untouchability).",
         "Both factions supplemented each other: Swarajists prevented political stagnation in the towns, while No-Changers built the rural organizational foundation for the 1930 Civil Disobedience Movement."),

        ("mains_mod_028", "Revolutionary Socialism: Bhagat Singh and the HSRA", "revolutionary-nationalism", 15, 250, "Bipan Chandra, Ch. 20; Spectrum",
         "Bhagat Singh represented an intellectual leap from romantic individual terrorism to scientific socialist revolution. Analyze his ideological evolution and martyrdom.",
         "The 1920s witnessed the second phase of revolutionary nationalism, moving beyond individual assassinations to embrace Marxism, anti-imperialism, and working-class liberation under the Hindustan Socialist Republican Association (HSRA).",
         [("Foundation of the HSRA (1928) at Feroz Shah Kotla", ["Founded by Bhagat Singh, Chandrashekhar Azad, Sukhdev, and Bhagwati Charan Vohra, adding 'Socialist' to the party's official name.", "Redefined 'Revolution': not a cult of bombs and pistols, but the complete overthrow of capitalism, feudalism, and imperial exploitation to establish a socialist society."]),
          ("The Saunders Slaying and Central Assembly Bomb (1929)", ["Assassinated British police officer John Saunders in Lahore (1928) to avenge the brutal death of Lala Lajpat Rai from lathi blows during the Simon Commission boycott.", "On 8 April 1929, Bhagat Singh and Batukeshwar Dutt threw harmless smoke bombs into the Central Legislative Assembly shouting 'Inquilab Zindabad!' and scattered leaflets: 'It takes a loud voice to make the deaf hear.'", "Surrendered deliberately to use the British court trial as an open propaganda platform for their socialist ideology."]),
          ("Historic 63-Day Hunger Strike and Martyrdom", ["Undertook a historic 63-day hunger strike in Lahore Central Jail demanding recognition as political prisoners, resulting in the heroic martyrdom of Jatin Das.", "In jail, Bhagat Singh authored the philosophical masterpiece 'Why I am an Atheist', articulating rationalism and dialectical materialism.", "Executed on 23 March 1931 alongside Rajguru and Sukhdev at Lahore, becoming eternal symbols of youthful sacrifice."])],
         "Ideological trajectory: Individual armed revenge (Saunders) -> Propaganda by deed (Assembly bomb) -> Scientific Socialist Ideology ('Why I am an Atheist').",
         "Bhagat Singh was not merely a fearless martyr, but one of modern India's most brilliant Marxist thinkers, who showed that true independence requires the annihilation of both foreign rule and domestic capitalist exploitation."),

        ("mains_mod_029", "Simon Commission (1927) and the Nehru Report (1928)", "gandhian-era", 10, 150, "Spectrum; Bipan Chandra",
         "The Simon Commission boycott galvanized Indian political unity, producing the Nehru Report as India's first indigenous constitutional blueprint. Discuss.",
         "In November 1927, the British government appointed the Indian Statutory Commission (Simon Commission) to review the constitutional working of the 1919 Act, sparking unprecedented fury.",
         [("Outrage Over the 'All-White' Commission", ["Composed of 7 British parliamentarians with not a single Indian member, insulting India's sovereign right to determine its own political future.", "Boycotted across India with black flags and the slogan 'Simon Go Back!'. Lala Lajpat Rai was fatally lathi-charged in Lahore."]),
          ("Birkenhead's Challenge and the Nehru Report (1928)", ["Secretary of State Lord Birkenhead challenged Indians to produce a constitution that all communities agreed upon.", "Congress convened an All-Parties Conference, appointing a committee chaired by Motilal Nehru.", "Key Proposals of Nehru Report: Dominion Status; 19 Fundamental Rights (including universal adult suffrage and equal rights for women); joint electorates with reservation of seats for minorities; secular state."]),
          ("Internal Rifts and Rejection", ["Young radicals (Jawaharlal Nehru, Subhash Bose) opposed Dominion Status, demanding Complete Independence ('Purna Swaraj').", "Jinnah rejected the report, presenting his 'Fourteen Points' demanding separate electorates and 1/3rd Muslim representation in the central legislature."])],
         "Flowchart: All-White Simon Commission -> Birkenhead's arrogant challenge -> Nehru Report (1928) -> Jinnah's 14 Points -> Road to Lahore Purna Swaraj.",
         "While rejected by communal factions, the Nehru Report stands as India's first indigenous constitutional milestone, anticipating the fundamental rights of our modern Constitution."),

        ("mains_mod_030", "Civil Disobedience Movement and Dandi March (1930)", "gandhian-era", 15, 250, "Bipan Chandra, Ch. 22; NCERT Themes Theme 11",
         "Why did Mahatma Gandhi choose 'Salt' as the central symbol of the Civil Disobedience Movement? Analyze the socio-political impact of the Salt Satyagraha.",
         "On 12 March 1930, Mahatma Gandhi marched 240 miles from Sabarmati Ashram to Dandi with 78 disciples, inaugurating the Civil Disobedience Movement by manufacturing salt on 6 April 1930.",
         [("Genius of the Salt Symbol: Universal Emotive Appeal", ["Salt was an indispensable dietary necessity for every human being and animal, consumed equally by rich and poor, Hindu and Muslim.", "The British salt monopoly and salt tax hit the poorest peasant the hardest, symbolizing the petty greed and inhumanity of colonial rule.", "By choosing salt, Gandhi linked an everyday household commodity to the grand ideal of national sovereignty, making every woman and villager a direct participant in the struggle."]),
          ("Mass Spread and Diverse Regional Manifestations", ["Tamil Nadu: C. Rajagopalachari led the Vedaranyam Salt March from Tiruchirappalli.", "Kerala: K. Kelappan marched from Calicut to Payyanur.", "North-West Frontier Province (NWFP): Khan Abdul Ghaffar Khan ('Frontier Gandhi') led the non-violent 'Khudai Khidmatgars' (Red Shirts); Garhwali soldiers famously refused to fire on unarmed Pathan demonstrators.", "Dharasana Salt Works: Sarojini Naidu and Manilal Gandhi led unarmed satyagrahis who absorbed brutal steel-tipped lathi blows without flinching, recorded by American journalist Webb Miller, sparking global outrage against British brutality."]),
          ("Mass Participation of Women", ["Marked the first mass entry of Indian women into public life: picketing liquor shops, foreign cloth stores, and courting arrest in tens of thousands."])],
         "Dandi March route schematic: Sabarmati -> 240 miles -> Dandi coast -> Nationwide Salt violation & Boycott.",
         "By turning a handful of coastal salt into a weapon of non-violent rebellion, Gandhi shook the foundations of the British Empire and awakened the collective soul of India."),

        ("mains_mod_031", "Poona Pact (1932): Gandhi, Ambedkar, and Depressed Classes", "gandhian-era", 15, 250, "Spectrum; Bipan Chandra",
         "The Poona Pact of 1932 was a monumental compromise between Mahatma Gandhi and Dr. B.R. Ambedkar that reshaped Dalit politics in modern India. Critically examine.",
         "Following the Second Round Table Conference, British Prime Minister Ramsay MacDonald announced the 'Communal Award' in August 1932, granting separate electorates to the 'Depressed Classes' (Dalits).",
         [("Gandhi's Fast Unto Death in Yerwada Jail", ["Gandhi viewed separate electorates for Dalits as a sinister colonial design to permanently sever the untouchables from the Hindu fold and vivisect Indian society.", "Began a fast unto death in Yerwada Jail on 20 September 1932, arguing that while political reservations were welcome, separate electorates would perpetuate untouchability forever."]),
          ("Dr. B.R. Ambedkar's Perspective and Dilemma", ["Ambedkar argued that Dalits were an oppressed distinct minority whose socio-political rights could never be protected under high-caste Hindu hegemony without independent political power.", "Faced immense national pressure as Gandhi's life hung by a thread, demonstrating profound statesmanship to negotiate a compromise."]),
          ("Terms of the Poona Pact (24 September 1932)", ["Abolished Separate Electorates for the Depressed Classes in favour of 'Joint Electorates with Reserved Seats'.", "Substantially increased reserved seats for Dalits: from 71 (under the Communal Award) to 148 seats in provincial legislatures, and 18% in the Central Assembly."]),
          ("Long-Term Political Ramifications", ["Integrated Dalits into the mainstream nationalist electoral framework, but Ambedkar later felt that joint electorates allowed caste-Hindus to elect compliant Dalit candidates who lacked independent assertiveness."])],
         "Comparative balance: Communal Award (Separate Electorates, 71 seats) vs Poona Pact (Joint Electorates with Reservations, 148 seats).",
         "The Poona Pact was an epochal compromise that preserved national unity while enshrining affirmative legislative reservations for the marginalized, anticipating the affirmative action architecture of the Indian Constitution."),

        ("mains_mod_032", "Government of India Act 1935", "constitutional-development", 15, 250, "Spectrum Modern India",
         "The Government of India Act 1935 was a masterpiece of constitutional drafting that granted Provincial Autonomy while introducing fatal safeguards. Elucidate.",
         "Enacted after three Round Table Conferences, the Government of India Act 1935 was the longest and most comprehensive constitutional enactment under British rule, serving as the primary structural template for the Constitution of independent India.",
         [("1. Proposed All-India Federation", ["Proposed a federation comprising British Indian provinces and Princely States.", "Accession was voluntary for princely states; the federal part never came into force because princely rulers refused to surrender their autocratic sovereignty."]),
          ("2. Provincial Autonomy (Abolition of Dyarchy in Provinces)", ["Abolished Dyarchy at the provincial level, introducing fully responsible provincial governments elected by popular franchise (franchise expanded to ~14% of population).", "Ministers were responsible to elected provincial assemblies across all provincial portfolios."]),
          ("3. Introduction of Dyarchy at the Centre", ["Transferred the failed experiment of Dyarchy to the Central Executive: Defense, External Affairs, Ecclesiastical affairs, and Tribal areas were kept reserved under the Governor-General.", "Governor-General retained sweeping veto powers and special discretionary responsibilities."]),
          ("4. Bicameralism and Communal Retention", ["Introduced bicameral legislatures in six major provinces (Bengal, Bombay, Madras, UP, Bihar, Assam).", "Further extended separate communal electorates to Dalits, women, and labour."])],
         "Constitutional balance: Provincial Autonomy (Real ministerial power in provinces) vs Autocratic Central Discretion (Vetoes, Reserved subjects, Federation stalled).",
         "Nehru famously described the 1935 Act as 'a machine with strong brakes but no engine'; nonetheless, its federal structure, provincial autonomy, and judicial provisions provided the backbone for the 1950 Indian Constitution."),

        ("mains_mod_033", "Congress Ministries (1937-1939): 28 Months of Governance", "gandhian-era", 10, 150, "Bipan Chandra, Ch. 24",
         "Assess the performance and agrarian reforms of the Congress provincial ministries (1937-1939). Why did they resign in October 1939?",
         "Following sweeping electoral victories in the 1937 elections, the Congress formed ministries in 8 out of 11 provinces, governing for 28 months.",
         [("Achievements in Civil Liberties and Agrarian Relief", ["Restored civil liberties: lifted bans on political organizations and newspapers; released hundreds of political prisoners.", "Enacted tenancy and debt relief legislations: reduced agrarian rents, curbed illegal exactions by zamindars, and protected peasants from debt eviction (e.g., Bihar Tenancy Act).", "Promoted basic national education (Wardha Scheme) and prohibition of alcohol."]),
          ("Limitations and Constraints", ["Hamstrung by financial stringency and the Governor's overriding powers under the 1935 Act.", "Unable to completely abolish the Zamindari system due to property compensation clauses and conservative Congress factions."]),
          ("Resignation in October 1939", ["When World War II erupted in September 1939, Viceroy Lord Linlithgow unilaterally declared India a belligerent without consulting the provincial ministries or Indian leaders.", "In protest against this autocratic disregard for Indian democracy, all Congress ministries resigned en masse in October-November 1939."])],
         "Timeline: 1937 Elections victory -> 28 months of agrarian/civil reforms -> Linlithgow's unilateral WWII declaration -> Mass resignation (Oct 1939).",
         "The 28 months of Congress rule demonstrated that Indian nationalists could govern vast provinces with administrative integrity, efficiency, and welfare commitment."),

        ("mains_mod_034", "Subhash Chandra Bose and the Indian National Army (INA)", "freedom-struggle-climax", 15, 250, "Bipan Chandra, Ch. 26; Sugata Bose",
         "Subhash Chandra Bose's military audacity and the trials of the Indian National Army (INA) struck a fatal blow to British colonial rule. Analyze.",
         "Rejecting Gandhian non-violent incrementalism, Netaji Subhash Chandra Bose believed that Britain's difficulty during World War II was India's opportunity, escaping house arrest in Calcutta in 1941 to wage armed liberation from abroad.",
         [("Formation of the Provisional Government of Free India (Azad Hind)", ["Taking leadership of the Indian National Army from Rash Behari Bose and Captain Mohan Singh in Singapore (1943), Netaji proclaimed the 'Arzi Hukumat-e-Azad Hind'.", "Formed the famous combat brigades (Subhash, Gandhi, Nehru) and the pioneering all-women 'Rani of Jhansi Regiment' led by Captain Lakshmi Sahgal.", "Given the slogan 'Give me blood, and I shall give you freedom!' and 'Chalo Dilli!'."]),
          ("Military Campaign in Burma and Imphal", ["Fought alongside Japanese troops on the Burma-Manipur frontier, raising the Indian tricolour at Moirang (Manipur) and Kohima in 1944.", "Forced to retreat due to monsoon flooding, severed supply lines, and Japanese logistical collapse."]),
          ("The Historic INA Trials at Red Fort (1945-1946)", ["British authorities put three INA officers on public trial for treason at the Red Fort: Prem Sahgal (Hindu), Gurbaksh Singh Dhillon (Sikh), and Shah Nawaz Khan (Muslim).", "Triggered unprecedented mass fury: students, workers, and citizens rioted across India; Congress organized a stellar legal defense team led by Bhulabhai Desai, Tej Bahadur Sapru, and Jawaharlal Nehru.", "Forced the Commander-in-Chief Sir Claude Auchinleck to remit their sentences, demonstrating that the British armed forces in India could no longer be trusted to repress their own countrymen."])],
         "Impact vector: INA Battlefield Audacity (Imphal/Kohima) -> Red Fort Trials (Cross-communal fury) -> Collapse of Sepoy Loyalty -> Royal Navy Mutiny (1946) -> British Departure.",
         "Netaji's INA shattered the foundational myth of British military invincibility, decisively proving that the Indian armed forces had aligned with the freedom struggle."),

        ("mains_mod_035", "Quit India Movement (August 1942)", "freedom-struggle-climax", 15, 250, "UPSC CSE 2013 GS-1; Bipan Chandra, Ch. 25; NCERT Themes Theme 11",
         "The Quit India Movement was the climactic spontaneous mass insurrection of the Indian freedom struggle. Analyze its underground networks and parallel governments.",
         "Following the collapse of the Cripps Mission in April 1942 and facing Japanese troops at the Burma border, Mahatma Gandhi launched the 'Quit India Movement' on 8 August 1942 at Gowalia Tank (Mumbai), issuing the historic clarion call: 'Do or Die' (Karo ya Maro).",
         [("Pre-emptive State Terror and Spontaneous Mass Fury", ["In the early hours of 9 August 1942, British police launched 'Operation Zero Hour', arresting Gandhi, Nehru, Patel, and the entire top Congress leadership.", "Bereft of central guidance, the movement exploded spontaneously into the fiercest mass insurrection since 1857: crowds attacked police stations, post offices, railway lines, and hoisted the tricolour on district collectorates."]),
          ("Underground Networks of Resistance", ["Young socialist leaders operated an all-India underground resistance: Jayaprakash Narayan (who dramatically escaped from Hazaribagh jail), Ram Manohar Lohia, Aruna Asaf Ali, and Achyut Patwardhan.", "Usha Mehta operated a secret underground radio station ('Voice of Freedom') transmitting uncensored news across the country."]),
          ("Emergence of Parallel Governments ('Prati Sarkars')", ["1. Ballia (UP): Chittu Pandey formed a parallel government for a week, releasing all Congress prisoners.", "2. Tamluk (Midnapore, Bengal): Jatiya Sarkar established the armed 'Vidyut Vahini', distributing cyclone relief and organizing arbitration courts.", "3. Satara (Maharashtra): Led by Nana Patil and Y.B. Chavan; ran the longest-lasting parallel government ('Prati Sarkar'), establishing people's courts ('Nyayadan Mandals') and village cooperatives."])],
         "Map locator of Parallel Governments: Ballia (Chittu Pandey) <--> Tamluk Jatiya Sarkar (Bengal) <--> Satara Prati Sarkar (Nana Patil).",
         "Though crushed by brute imperial military force, Quit India demonstrated that British colonial rule in India was living on borrowed time, with popular consent permanently extinguished."),

        ("mains_mod_036", "Royal Indian Navy (RIN) Revolt of February 1946", "freedom-struggle-climax", 10, 150, "Bipan Chandra, Ch. 27",
         "The Royal Indian Navy revolt of February 1946 sounded the death knell of the British Empire in India. Discuss its causes and significance.",
         "On 18 February 1946, ratings of the HMIS Talwar in Bombay went on a historic naval strike, which spread like wildfire to 78 ships, 20 shore establishments, and 20,000 naval ratings across Karachi, Calcutta, and Cochin.",
         [("Causes of the Naval Mutiny", ["Protested against abysmal food, racial abuse by British officers, and the arrest of rating B.C. Dutt for writing 'Quit India' on HMIS Talwar.", "Deeply radicalized by the INA trials and post-war anti-imperial sentiments; hoisted Congress, Muslim League, and Communist flags on ship masts."]),
          ("Mass Civilian Uprising in Bombay", ["Over 300,000 Bombay mill workers went on strike; citizens erected barricades fighting British troops; over 200 civilians were killed in police firing."]),
          ("Decisive Turning Point for British Withdrawal", ["Shattered the loyalty of the armed forces—the ultimate coercive pillar of the colonial state.", "British Prime Minister Clement Attlee realized that Britain could no longer hold India by military force, announcing the dispatch of the Cabinet Mission barely three days after the revolt."])],
         "Flowchart: HMIS Talwar strike -> Strike across 78 naval ships -> Bombay working-class solidarity -> Loss of armed force loyalty -> Attlee announces Cabinet Mission.",
         "The naval mutiny of 1946 proved that the British sword in India had lost its edge, making immediate independence an absolute inevitability."),

        ("mains_mod_037", "Cabinet Mission Plan (1946): Proposals and Breakdown", "freedom-struggle-climax", 15, 250, "Spectrum; Bipan Chandra",
         "The Cabinet Mission Plan of 1946 was the last constitutional attempt to preserve the territorial unity of undivided India. Explain its proposals and reasons for failure.",
         "Arriving in March 1946, the three-member Cabinet Mission (Pethick-Lawrence, Stafford Cripps, A.V. Alexander) sought to negotiate a peaceful transfer of power while avoiding the partition of the subcontinent.",
         [("Key Proposals of the Plan", ["1. Rejection of Pakistan: Explicitly rejected Jinnah's demand for a fully sovereign state of Pakistan on economic, administrative, and military grounds.", "2. Three-Tier Federal Structure: An All-India Union handling only Foreign Affairs, Defense, and Communications, with all residuary powers vested in the provinces.", "3. Mandatory Grouping of Provinces: Divided provinces into 3 Sections: Section A (Hindu-majority provinces: Madras, Bombay, UP, Bihar, CP, Orissa); Section B (Muslim-majority northwest: Punjab, NWFP, Sindh); Section C (Muslim-majority northeast: Bengal and Assam).", "4. Constituent Assembly: Elected indirectly by provincial assemblies to draft the constitution.", "5. Interim Government: An all-Indian executive council representing major parties."]),
          ("Why the Compromise Collapsed", ["Contradictory Interpretations of Grouping: Congress (Nehru) maintained that grouping was voluntary for provinces (Assam should not be forced into Section C). Jinnah and the League insisted that grouping was strictly compulsory, viewing Section B and C as the de facto blueprint for future Pakistan.", "Nehru's Press Conference (10 July 1946): Stated that Congress was entering the Constituent Assembly uncommitted to any British scheme, free to modify arrangements."]),
          ("The Fatal Consequence: Direct Action Day", ["Jinnah withdrew the League's acceptance of the plan and called for 'Direct Action Day' on 16 August 1946 to force Pakistan, unleashing the horrific Great Calcutta Killings."])],
         "Cabinet Mission 3-tier grouping map: Section A (Hindu core) | Section B (Northwest: Punjab/Sindh/NWFP) | Section C (Northeast: Bengal/Assam).",
         "The Cabinet Mission was a fragile constitutional house of cards: when trust evaporated between the Congress and the League, its collapse plunged the nation into the inferno of partition."),

        ("mains_mod_038", "Partition of India and the Mountbatten Plan", "freedom-struggle-climax", 15, 250, "Bipan Chandra; Yasmin Khan, The Great Partition",
         "The Partition of India was an immense human tragedy characterized by catastrophic violence and administrative haste. Discuss the Mountbatten Plan and the Radcliffe Award.",
         "Announced on 3 June 1947 by Lord Mountbatten, the '3rd June Plan' finalized the partition of British India into two independent dominions—India and Pakistan—hastening the transfer of power by ten months.",
         [("Administrative Haste and the 3rd June Plan", ["Mountbatten advanced the transfer date from June 1948 to 15 August 1947, giving the state barely 72 days to divide a subcontinental empire, bifurcate armies, civil services, and assets.", "Conducted provincial assembly votes in Bengal and Punjab, where partition was formally approved."]),
          ("The Radcliffe Award: Drawing Borders in Blood", ["Sir Cyril Radcliffe, a British barrister who had never visited India, was given just five weeks to demarcate thousands of miles of border across Bengal and Punjab using outdated census maps.", "Crucial Mistake: The border awards were kept secret until 17 August 1947—two days AFTER independence—creating catastrophic terror and confusion among millions of minorities who did not know which country they were in."]),
          ("The Human Holocaust of Migration", ["Triggered the largest forced mass migration in human history: over 15 million people displaced across borders.", "Horrific communal slaughter: between 500,000 and 1 million innocent men, women, and children slaughtered in communal massacres; over 75,000 women subjected to sexual abduction and assault."])],
         "Timeline of tragedy: 3 June Plan -> 72-day hurried handover -> Delayed Radcliffe Award (17 Aug) -> 15 million displaced & 1 million slaughtered.",
         "Partition remains the tragic trauma of South Asian history: an independence achieved alongside the vivisection of an ancient civilizational homeland, stained with the blood of millions."),

        ("mains_mod_039", "Integration of Princely States: Sardar Patel and V.P. Menon", "post-independence", 15, 250, "UPSC CSE 2017 GS-1; V.P. Menon; Bipan Chandra",
         "Sardar Vallabhbhai Patel's diplomatic realism and firm statecraft integrated over 560 princely states into the Indian Union. Analyze the challenges of Junagadh, Hyderabad, and Kashmir.",
         "When the British departed in August 1947, the lapse of paramountcy threatened the balkanization of India into hundreds of sovereign kingdoms. Sardar Vallabhbhai Patel, ably assisted by V.P. Menon, performed an unparalleled geopolitical miracle.",
         [("Patel's Diplomatic Strategy: The Carrot and the Stick", ["Appealed to the patriotic sentiment of princes while subtly indicating the unstoppable surge of democratic popular unrest in their states.", "Offered generous 'Privy Purses' and preservation of personal royal titles, securing accessions on three non-negotiable central subjects: Defense, External Affairs, and Communications via the 'Instrument of Accession'."]),
          ("1. Junagadh (Gujarat)", ["Nawab Muhammad Mahabat Khanji III acceded to Pakistan, despite being non-contiguous to Pakistan and having an 80% Hindu population.", "Citizens revolted, establishing an 'Aarzi Hukumat' (Provisional Government) under Samaldas Gandhi. When the Nawab fled to Karachi, Indian troops took over and conducted a fair plebiscite in February 1948 (99% voted for India)."]),
          ("2. Hyderabad (Operation Polo, September 1948)", ["Nizam Mir Osman Ali Khan refused to join India, signing a 1-year Standstill Agreement while covertly financing Kasim Razvi's fascist 'Razakar' militia that terrorized Hindu populations and slaughtered peasants in the Telangana rebellion.", "On 13 September 1948, Patel launched 'Operation Polo' (police action); the Nizam's army surrendered within 108 hours, and Hyderabad was integrated."]),
          ("3. Jammu & Kashmir (October 1947)", ["Maharaja Hari Singh procrastinated until Pakistani armed tribal raiders backed by the Pakistan Army invaded Kashmir on 22 October 1947, reaching Baramulla.", "Hari Singh signed the Instrument of Accession on 26 October 1947; Indian airborne troops flew to Srinagar, repelling the invaders."])],
         "Map locator of the three recalcitrant states: Junagadh (Saurashtra), Hyderabad (Deccan), Jammu & Kashmir (North).",
         "Sardar Patel's iron resolve, diplomatic charm, and decisive action forged a united subcontinental nation out of fragmented royal feudalism, earning him the title 'Iron Man of India'."),

        ("mains_mod_040", "Linguistic Reorganization of States (1948-1956)", "post-independence", 15, 250, "UPSC CSE 2016 GS-1; Ramachandra Guha",
         "The linguistic reorganization of states consolidated Indian national unity rather than disintegrating it. Trace its trajectory from the Dhar Commission to the States Reorganisation Act 1956.",
         "At independence, the map of India was an administrative patchwork of Part A, B, C, and D states inherited from British colonial annexations. The demand to reorganize states on linguistic lines was an early test of Indian democracy.",
         [("Early Caution: Dhar Commission and JVP Committee (1948)", ["S.K. Dhar Commission (1948) and JVP Committee (Jawaharlal Nehru, Vallabhbhai Patel, Pattabhi Sitaramayya) advised against linguistic states immediately after partition, fearing it would ignite balkanization and weaken national unity.", "Recommended administrative convenience, economic viability, and national security as primary criteria."]),
          ("Potti Sreeramulu's Martyrdom and the Birth of Andhra (1953)", ["Telugu-speaking population demanded a separate state carved out of Madras Presidency.", "Veteran freedom fighter Potti Sreeramulu undertook a fast unto death, passing away on the 58th day (15 December 1952).", "Massive civil unrest forced the government to create India's first linguistic state: Andhra State, in October 1953."]),
          ("The Fazal Ali Commission and States Reorganisation Act 1956", ["Government appointed the States Reorganisation Commission (SRC) under Justice Fazal Ali, K.M. Panikkar, and H.N. Kunzru.", "Rejected the 'One Language, One State' dogma, but accepted language as the primary criterion for administrative cohesion.", "States Reorganisation Act 1956 abolished the complex Part A/B/C/D system, reorganizing India into 14 States and 6 Union Territories."]),
          ("Strengthening National Unity", ["Contrary to fears, linguistic states democratized politics by allowing governance in the mother tongue, making citizens feel empowered partners in the Indian Union."])],
         "Evolution flowchart: Dhar Commission (Caution) -> JVP Report (Delay) -> Sreeramulu's fast & Andhra (1953) -> Fazal Ali SRC -> States Reorganisation Act (1956: 14 States).",
         "Linguistic reorganization proved that unity in diversity is not a cosmetic slogan, but the structural bedrock of the Indian democratic republic.")
    ]

    for idx, item in enumerate(modern_40):
        try:
            b_list = [{"heading": b[0], "points": b[1]} for b in item[8]]
            items.append({
                "id": item[0],
                "category": "modern",
                "categoryLabel": "Modern India",
                "periodId": item[2],
                "marks": item[3],
                "wordLimit": item[4],
                "isPyq": False,
                "yearSource": "Standard Practice",
                "bookRef": item[5],
                "question": item[6],
                "framework": {
                    "intro": item[7],
                    "body": b_list,
                    "diagramMapIdea": item[9],
                    "conclusion": item[10]
                }
            })
        except Exception as e:
            print(f"FAILED on item {idx}: {item[0]} len={len(item)}: {e}")
            print(f"item[8] is: {item[8]}")
            raise

    from gen_mains_modern_part2 import get_modern_part2
    items.extend(get_modern_part2())

    return items

if __name__ == '__main__':
    mod = get_modern_mains()
    print(f"Generated {len(mod)} Modern Mains questions ({mod[0]['id']} to {mod[-1]['id']})")
    with open('data/batch_mains_modern.json', 'w', encoding='utf8') as f:
        json.dump(mod, f, indent=2, ensure_ascii=False)
