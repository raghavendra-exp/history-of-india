import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Comprehensive enrichment mapping for Medieval Indian History
MEDIEVAL_ENRICHMENTS = {
    'early-medieval-period': {
        'aspects': {
            'Tripartite Struggle for Kannauj': [
                'Imperial triangle: Centuries-long contest (8th–10th centuries CE) among the Gurjara-Pratiharas of Malwa/Rajasthan, Palas of Bengal/Bihar, and Rashtrakutas of the Deccan for mastery over the fertile agrarian Doab and symbolic imperial capital of Kannauj.',
                'Major confrontations: Vatsaraja Pratihara defeated Pala ruler Dharmapala, but was routed by Rashtrakuta Dhruva; Nagabhata II defeated Dharmapala and captured Kannauj, before being humbled by Govinda III Rashtrakuta; Mihira Bhoja (r. 836–885 CE, title Adivaraha) finally secured lasting Pratihara control over Kannauj.'
            ],
            'Palas & Eastern Monasticism': [
                'Buddhist renaissance: Founded by Gopala (elected through popular consensus to end the anarchic condition of Matsyanyaya c. 750 CE); Dharmapala (revived Nalanda and founded Vikramashila University with 107 colleges; built Somapura Mahavihara in Bangladesh); Devapala (patronized Balaputradeva of Shailendra dynasty of Java/Sumatra, granting 5 villages for a monastery at Nalanda).',
                'Tibetan missions: Atisha Dipankara Srijnana journeyed to Tibet, propagating reformed Tantric Mahayana (Vajrayana) Buddhism.'
            ],
            'Rashtrakutas & Deccan Synthesis': [
                'Military and cultural zenith: Dantidurga established Rashtrakuta sovereignty by performing the Hiranyagarbha ritual at Ujjain; Krishna I excavated the monolithic rock-cut Kailasanatha Temple at Ellora (Cave 16) out of a single basalt cliff.',
                'Literary patrons: Amoghavarsha I Nrupatunga (r. 814–878 CE, "Ashoka of the South") authored Kavirajamarga (earliest landmark work on poetics in Kannada) and Prashnottara Ratnamalika in Sanskrit; Arab chronicler Sulaiman (851 CE) described the Rashtrakuta emperor (Balhara / Vallabharaja) as one of the four great emperors of the world alongside the Caliph of Baghdad, Emperor of China, and Emperor of Constantinople.'
            ],
            'Feudalism Debate (R.S. Sharma vs Revisionists)': [
                'Feudal fragmentation model: R.S. Sharma, D.N. Jha, and B.N.S. Yadava argue that royal land grants (Samanta system) led to parcellized sovereignty, economic ruralization, decline of urban centres, and decay of artisanal trade.',
                'Integration Model: B.D. Chattopadhyaya and Hermann Kulke argue that the period witnessed progressive agrarian expansion, transformation of tribes into peasant castes (Jatis), and integration of local lineage deities into regional state cults (e.g., Jagannatha cult of Odisha).'
            ]
        },
        'upsc': {
            'prelims': [
                'Gopala founded the Pala dynasty around 750 CE, chosen by local chieftains to eliminate "Matsyanyaya" (law of the jungle / anarchy).',
                'Vikramashila University was founded by Pala king Dharmapala; its most illustrious scholar, Atisha Dipankara, spearheaded the Buddhist mission to Tibet.',
                'The monolithic rock-cut Kailasanatha Temple at Ellora (Cave 16) was excavated top-down from basalt rock by Rashtrakuta king Krishna I.',
                'Kavirajamarga, the earliest extant monumental work on Kannada rhetoric and poetics, was composed during the reign of Rashtrakuta king Amoghavarsha I.',
                'Arab traveler Sulaiman visited India in the 9th century and hailed the Rashtrakuta ruler ("Balhara") as one of the four greatest sovereigns of the world.',
                'Pratihara king Mihira Bhoja assumed the title "Adivaraha", dedicated coins with the Boar incarnation of Vishnu, and was referred to as "King Baura" by Arab traveler Al-Masudi.',
                'The Shailendra king of Java, Balaputradeva, built a Buddhist monastery at Nalanda with the permission of Pala ruler Devapala, who granted 5 villages for its upkeep.'
            ],
            'mains': [
                'Critically analyze the geopolitical causes, trajectory, and consequences of the Tripartite Struggle among the Pratiharas, Palas, and Rashtrakutas for control over Kannauj.',
                'Examine the Indian Feudalism debate with reference to early medieval land grants, subinfeudation, and urban decay, comparing R.S. Sharma\'s thesis with B.D. Chattopadhyaya\'s "Integration Model".',
                'Evaluate the architectural, artistic, and literary achievements of the Rashtrakutas with special focus on Ellora Cave 16 and the development of Kannada literature.',
                'Discuss the contributions of the Pala dynasty to the patronization and dissemination of Vajrayana Buddhism across Eastern India and Tibet.'
            ]
        }
    },
    'kingdoms-of-south': {
        'aspects': {
            'Imperial Cholas & Maritime Empire': [
                'Dynastic revival: Vijayalaya revived the Chola line by capturing Thanjavur (850 CE); Parantaka I conquered Madurai (title "Maduraikonda") and issued the historic Uttaramerur inscriptions.',
                'Rajaraja I (r. 985–1014 CE): Conquered Anuradhapura in northern Sri Lanka, Maldives; built the monumental Brihadisvara (Rajarajesvara) Temple at Thanjavur (consecrated 1010 CE; 216-foot granite Vimana topped by an 80-tonne monolithic cupola); initiated systematic land cadastral surveys.',
                'Rajendra I (r. 1012–1044 CE): Subjugated complete island of Sri Lanka; marched across Eastern India up to the Ganga, assuming title "Gangaikondachola" and establishing a new capital at Gangaikondacholapuram with an artificial reservoir (Cholaganga); dispatched an armada across the Bay of Bengal, sacking the maritime Srivijaya empire (Sumatra/Malaya) and Kadaram to protect Indian trade with Song China.'
            ],
            'Local Self-Government & Democratic Assemblies': [
                'Village administrative tiers: Ur (general assembly of tax-paying village landholders) and Sabha / Mahasabha (assembly of Brahmin proprietors in Brahmadeya villages); Nagaram (assembly of merchants and traders in commercial towns).',
                'Uttaramerur Inscription of Parantaka I (919 and 921 CE): Outlines detailed constitutional procedures for election to village executive committees (Variyams): Samvatsara-variyam (annual committee), Eri-variyam (lake/irrigation tank committee), Totta-variyam (garden committee), and Pon-variyam (gold/currency committee).',
                'Kudavolai (Pot-ticket lottery) system: Names of qualified candidates written on palm leaves (Olais), placed into an earthen pot (Kuda), and picked by a young innocent boy; qualifications: owning land (at least 1/4th Veli), having a house on one\'s own site, age between 35 and 70, mastery of Vedic hymns and Dharma-Shastras; disqualifications: financial default, criminal conduct, failing to submit accounts of previous committee.'
            ],
            'Chola Art, Bronzes & Temple Economy': [
                'Lost-wax bronze casting zenith: World-renowned Chola bronzes depicting Nataraja (Shiva as Cosmic Dancer: upper right hand holding Damaru drum of creation, upper left holding Agni fire of destruction, lower right in Abhayaprada gesture of protection, lower left pointing to uplifted foot representing grace/liberation, trampling Apasmara Purusha demon of ignorance within a circle of flames Prabhamandala).',
                'Temple as socio-economic hub: Temples operated as major landowners, employers, banking institutions lending capital at interest, patrons of classical music, Bharatnatyam (Devadasi institution), education (Ghatikas), and grain storehouses during famine.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Uttaramerur Inscriptions of Chola King Parantaka I (919 and 921 CE) provide minute details of democratic village self-government, committee functions (Variyams), and election disqualifications.',
                'The Kudavolai system was an ancient Chola democratic lottery method using palm-leaf tickets drawn from an earthen pot by a boy to elect village committee members.',
                'Rajaraja I built the great Brihadisvara Temple at Thanjavur, entirely made of granite, with a 216-foot soaring Vimana.',
                'Rajendra I assumed the title "Gangaikondachola" after defeating Mahipala of Bengal, and founded the capital Gangaikondacholapuram and the massive Cholaganga lake.',
                'Chola naval expeditions under Rajendra I crossed the Bay of Bengal and conquered ports of the Srivijaya Empire (Sumatra, Malaya) to secure maritime trading routes to China.',
                'The iconic bronze Nataraja sculpture shows Shiva dancing within a halo of flames (Prabhamandala), crushing the dwarf demon Apasmara (representing spiritual ignorance).',
                'In Chola local administration, the assembly of Brahmins in a Brahmadeya village was called "Sabha" or "Mahasabha", while the merchant assembly in trade towns was called "Nagaram".'
            ],
            'mains': [
                'Evaluate the unique features of the village autonomy and local self-government under the Imperial Cholas on the basis of the Uttaramerur inscriptions.',
                'Analyze the geopolitical, economic, and maritime strategies that transformed the Bay of Bengal into a "Chola Lake" under Rajaraja I and Rajendra I.',
                'Discuss the artistic, iconographical, and metaphysical significance of Chola bronze sculptures, with particular reference to the cosmic symbolism of Nataraja.',
                'Examine the role of the temple as a pivotal socio-economic institution and employer in early medieval South Indian agrarian society.'
            ]
        }
    },
    'delhi-sultanate': {
        'aspects': {
            'Centralized Imperial Bureaucracy': [
                'Four pillars of sultanate administration: 1. Diwan-i-Wizarat (finance and revenue department headed by the Wazir/Prime Minister), 2. Diwan-i-Arz (military recruitment, inspection, and logistics department headed by the Ariz-i-Mamalik), 3. Diwan-i-Insha (state correspondence and royal chancery headed by Dabir-i-Khas), 4. Diwan-i-Risalat (religious affairs, endowments, and appeals headed by the Chief Sadr/Qazi-ul-Quzat).',
                'Intelligence and judicial apparatus: Barid-i-Mamalik (head of intelligence and news reporters / spies); Amir-i-Hajib (master of royal ceremonies in court); Muhtasib (censor of public morals and overseer of market weights).'
            ],
            'Iqta System & Agrarian Taxation': [
                'Iqta institutional mechanics: Revenue assignment of a defined tract of land granted to nobles/military commanders (Iqtadars / Muqtis / Walis); tasked with maintaining a designated quota of troops, collecting land revenue (Kharaj), maintaining local law and order, and remitting the fiscal surplus (Fawazil) to the royal central exchequer.',
                'Evolution under Balban and Alauddin: Balban appointed a royal Khwaja (accountant) to audit Muqti accounts; Alauddin Khalji converted large tracts of crown lands (Khalisa) into directly administered zones and confiscated hereditary tax privileges of rural intermediaries (Khuts, Muqaddams, Chaudhuris).'
            ],
            'Indo-Islamic Architecture & Cultural Confluence': [
                'Architectural innovations: Introduction of true arch (Mehrab), true dome (Gumbad), and lime-mortar cementing technology; Qutb Minar complex (Quwwat-ul-Islam mosque, Alai Darwaza built by Alauddin featuring the earliest horseshoe arch and white marble squinches).',
                'Amir Khusrau (Tuti-i-Hind / Parrot of India): Court poet across 7 sultans; pioneer of Qawwali music, invented the Sitar and Tabla; created the Hindavi dialect; authored historical masnavis: Qiran-us-Sa\'dain, Miftah-ul-Futuh, Ashiqa, Nuh Sipihr, and Tughlaq Nama.'
            ]
        },
        'upsc': {
            'prelims': [
                'In the Delhi Sultanate administration, Diwan-i-Wizarat dealt with revenue/finance, Diwan-i-Arz with military affairs, Diwan-i-Insha with royal correspondence, and Diwan-i-Risalat with religious appeals.',
                'The revenue officer responsible for auditing the accounts of Iqtadars and calculating "Fawazil" (surplus revenue due to the state) was the Khwaja.',
                'Alai Darwaza, built by Alauddin Khalji at the Qutb complex in 1311 CE, is considered the earliest monument in India employing the true horseshoe arch and squinch dome technique.',
                'Amir Khusrau is credited with inventing the Sitar, standardizing Qawwali singing, and introducing the Khayal style into Hindustani classical music.',
                'Ziauddin Barani authored the famous political treatises Tarikh-i-Firuz Shahi and Fatawa-i-Jahandari on Islamic statecraft.',
                'The hereditary village headmen in the Sultanate period were termed Khuts, Muqaddams, and Chaudhuris.',
                'Ibn Battuta, the Moroccan traveler, visited India during the reign of Muhammad bin Tughlaq and was appointed the Chief Qazi of Delhi for eight years, authoring the travelogue Rihla.'
            ],
            'mains': [
                'Critically evaluate the administrative and fiscal mechanics of the Iqta system in the Delhi Sultanate, tracing its evolution from Iltutmish to Firuz Shah Tughlaq.',
                'Examine the architectural evolution of the Delhi Sultanate from the Mamluk period to the Lodis, highlighting the structural adoption of the true arch, dome, and beam-and-bracket styles.',
                'Analyze the role of Amir Khusrau in the composite cultural, musical, and linguistic synthesis of medieval North India.',
                'Discuss the centralization of royal authority under the Delhi Sultans and assess how the Wizarat balanced bureaucratic control with military imperatives.'
            ]
        }
    },
    'mamluk-dynasty': {
        'aspects': {
            'Establishment & Consolidation (Iltutmish)': [
                'Qutbuddin Aibak (r. 1206–1210 CE): Governor of Muhammad Ghori; ruled from Lahore; styled "Lakhbaksh" (giver of lakhs) for immense generosity; started construction of Qutb Minar (dedicated to Sufi saint Qutbuddin Bakhtiyar Kaki); died playing Chaugan (polo).',
                'Shamsuddin Iltutmish (r. 1211–1236 CE): Regarded as the true consolidator of the Sultanate; shifted capital to Delhi; obtained formal investiture (Mansur) from the Abbasid Caliph of Baghdad (1229 CE); averted Mongol invasion by diplomatically refusing asylum to Jalaluddin Mangbarani pursued by Genghis Khan (1221 CE); completed Qutb Minar; instituted Turkan-i-Chihalgani (The Corpse of Forty Turkish slave-oligarchs); introduced pure silver Tanka (175 grains) and copper Jital.',
                'Razia Sultan (r. 1236–1240 CE): First and only woman sovereign of the Delhi Sultanate; nominated by Iltutmish over incompetent sons; discarded purdah, donned male attire (Qaba and Kulah), rode elephants in battle; appointed Abyssinian slave Jamaluddin Yaqut as master of the royal stables (Amir-i-Akhur); provoked rebellion of Turkish Chihalgani nobles led by Altunia of Bhatinda; killed near Kaithal.'
            ],
            'Ghiyasuddin Balban: Autocracy & Blood-and-Iron': [
                'Theory of Divine Kingship: Claimed descent from the mythical Persian hero Afrasiyab; proclaimed the Sultan to be the "Zill-i-Ilahi" (Shadow of God on Earth) and recipient of "Niyabat-i-Khudai" (Viceregency of God); introduced rigid Persian court etiquette: Sajda (prostration before the Sultan) and Paibos (kissing the Sultan\'s feet); celebrated the Persian spring festival of Nauroz.',
                'Destruction of Chihalgani & Espionage: Systematically liquidated the treacherous "Forty" (Turkan-i-Chihalgani) nobles to eliminate rivals; instituted an omnipresent spy network (Barids) reporting directly to the Sultan.',
                'Blood and Iron Policy: Mercilessly crushed Meo / Mewati dacoits around Delhi, clearing the forests and establishing police military outposts (Thanas); suppressed the rebellion of Tughril Khan in Bengal, impaling rebels on stakes along the market of Lakhnauti; created Diwan-i-Arz under Imad-ul-Mulk to check recurring Mongol incursions.'
            ]
        },
        'upsc': {
            'prelims': [
                'Iltutmish introduced the standard silver "Tanka" (175 grains) and copper "Jital" coinage of the Delhi Sultanate.',
                'The elite aristocratic council of 40 Turkish slave nobles, known as Turkan-i-Chihalgani or "The Forty", was created by Iltutmish and later broken by Balban.',
                'Razia Sultan was the daughter of Iltutmish and ruled from 1236 to 1240 CE, adopting the title "Sultan" and riding horses uncovered.',
                'Balban enunciated the theory of divine kingship, claiming to be "Zill-i-Ilahi" (Shadow of God) and instituting the Persian court customs of Sajda (prostration) and Paibos (feet-kissing).',
                'Balban created a separate military department called Diwan-i-Arz under Imad-ul-Mulk to strengthen the defense against Mongol raids.',
                'Qutbuddin Aibak died in 1210 CE after falling from his horse while playing Chaugan (early form of polo) in Lahore.',
                'The Mongol conqueror Genghis Khan reached the Indus river in 1221 CE in pursuit of Khwarizm prince Jalaluddin Mangbarani, but Iltutmish prudently denied refuge, saving Delhi.'
            ],
            'mains': [
                'Evaluate the contributions of Shamsuddin Iltutmish as the "real founder and consolidator" of the Delhi Sultanate.',
                'Analyze the political factors that led to the rise and tragic fall of Razia Sultan, highlighting the gender dynamics and the resistance of the Turkish nobility (Chihalgani).',
                'Critically examine Ghiyasuddin Balban\'s Theory of Kingship, court ceremonies, and "Blood and Iron" policy in strengthening the prestige and authority of the Crown.',
                'Examine the internal and external security challenges faced by the Mamluk sultans, with particular reference to the Mongol threat on the northwestern frontier.'
            ]
        }
    },
    'khilji-dynasty': {
        'aspects': {
            'Imperial Expansion & Deccan Campaigns': [
                'Imperialist drive: Alauddin Khalji (r. 1296–1316 CE) murdered his uncle Jalaluddin at Kara (Prayagraj); assumed title "Sikandar-i-Sani" (Second Alexander); conquered Gujarat (1299; where eunuch military genius Malik Kafur was acquired for 1,000 dinars - Hazar Dinari), Ranthambore (1301; Jauhar of Rajput women led by Rani Ranga Devi described by Amir Khusrau), Chittor (1303; Rani Padmini legend recorded later in Malik Muhammad Jayasi\'s Padmavat), Malwa, and Jalor.',
                'Deccan & Far South Expeditions: Malik Kafur led four lightning southern expeditions: Devagiri (Yadavas under Ramachandra), Warangal (Kakatiyas under Prataparudra, who surrendered the Koh-i-Noor diamond), Dvarasamudra (Hoysalas under Vira Ballala III), and Madurai (Pandyas); southern kingdoms were not directly annexed, but converted into tributary vassal states paying colossal war indemnities and annual tribute.'
            ],
            'Economic Market Control & Price Fixation': [
                'Strategic rationale: Alauddin required a colossal, permanent standing army to defend against massive Mongol invasions (Qutlugh Khwaja, Targhi) and expand across India without exhausting state treasury funds; fixed retail prices of every commodity in Delhi.',
                'Four specialized markets in Delhi: 1. Mandi (Grain market), 2. Sarai-i-Adl (Cloth, sugar, herbs, dry fruits, and manufactured goods), 3. Horses, cattle, and slaves market, 4. Miscellaneous general goods.',
                'Market regulatory bureaucracy: Diwan-i-Riyasat (Commerce ministry headed by Malik Yaqut); Shahna-i-Mandi (Market Superintendent maintaining registers of merchants); Barids (intelligence officers) and Munhiyas (undercover child spies testing shopkeepers\' weights); brutal punishments: flesh carved out of shopkeepers caught giving short weights.',
                'Agrarian reforms: First Sultan to measure agricultural land (Masahat) using the Biswa standard; state revenue share fixed at 50% (half) of gross produce (Kharaj); direct tax collection eliminating village middlemen (Khuts, Muqaddams); imposed grazing tax (Charai) and house tax (Ghari).'
            ],
            'Military Reforms': [
                'Standing army & direct cash pay: Paid soldiers directly in cash (Naqd) from royal treasury (234 Tankas annually for a regular cavalryman, plus 78 Tankas for a second horse - Do-Aspa).',
                'Anti-corruption controls: Dagh system (branding royal marks on horses to prevent substitution with inferior ponies) and Chehra / Huliya system (detailed descriptive physical register of each soldier to prevent fraudulent proxy muster-rolls).'
            ]
        },
        'upsc': {
            'prelims': [
                'Alauddin Khalji assumed the title "Sikandar-i-Sani" (Second Alexander) and struck coins bearing this epithet.',
                'Alauddin Khalji was the first ruler of the Delhi Sultanate to introduce the Dagh (branding of horses) and Chehra (descriptive roll of soldiers) systems in the army.',
                'In Alauddin\'s market control policy, the specialized central cloth and luxury goods market was called the "Sarai-i-Adl".',
                'The market control machinery was overseen by the Shahna-i-Mandi (superintendent) and monitored by child secret spies called "Munhiyas".',
                'Alauddin measured cultivable agricultural land based on the "Biswa" unit (Masahat system) and fixed the land revenue at 50% of the produce.',
                'Malik Kafur (Hazar Dinari) led Alauddin\'s military expeditions into South India, defeating the Yadavas of Devagiri, Kakatiyas of Warangal, Hoysalas of Dwarasamudra, and Pandyas of Madurai.',
                'The famous Persian epic poem Padmavat, recounting the siege of Chittor and Rani Padmini\'s Jauhar, was composed in Awadhi by Malik Muhammad Jayasi during the reign of Sher Shah Suri (1540 CE).'
            ],
            'mains': [
                'Critically analyze the economic and market control measures introduced by Alauddin Khalji. Was it an egalitarian socialist experiment or a ruthless fiscal mechanism to sustain a massive standing army?',
                'Examine Alauddin Khalji\'s agrarian policy with specific reference to land measurement (Masahat), revenue extraction, and the curtailment of hereditary rural intermediaries (Khuts and Muqaddams).',
                'Discuss the geopolitical strategy behind Alauddin Khalji\'s southern campaigns led by Malik Kafur, analyzing why he chose indirect tributary vassalage rather than direct territorial annexation.',
                'Evaluate the military reforms of Alauddin Khalji (Dagh, Chehra, cash salaries) in successfully repelling the repeated Mongol invasions of India.'
            ]
        }
    },
    'tughlaq-dynasty': {
        'aspects': {
            'Muhammad bin Tughlaq\'s Controversial Experiments': [
                'Intellectual contradictions: Highly erudite scholar of Arabic, Persian, mathematics, astronomy, philosophy, and medicine; described by contemporaries (Barani, Ibn Battuta) as a "mixture of opposites" and visionary ahead of his times.',
                'Transfer of capital (1327 CE): Ordered shifting of royal court and population from Delhi to Devagiri (renamed Daulatabad in Maharashtra) to rule South India more centrally and secure defense against Mongols; immense human suffering along the 1500 km march; failure forced him to order the populace back to Delhi.',
                'Token Currency Experiment (1329–1330 CE): Introduced brass and bronze coins (token currency) pegged at par with silver Tankas to address global silver shortages; failed catastrophically because the state failed to establish a monopoly over minting; every Hindu and Muslim house turned into a counterfeit mint; forced to redeem all worthless token coins with pure gold and silver coins from treasury.',
                'Khurasan & Qarachil Expeditions: Recruited an army of 370,000 men paid one year\'s salary in advance for the Khurasan expedition, which was cancelled when Central Asian alliances collapsed; Qarachil expedition into the Kumaon Himalayas resulted in devastating army destruction due to monsoon landslides and guerrilla warfare.',
                'Doab Taxation & Diwan-i-Kohi: Drastically hiked land revenue in the fertile Ganga-Yamuna Doab during a severe famine, causing peasant rebellion; later pioneered agricultural relief: established Diwan-i-Kohi (agricultural development department), provided state crop loans (Sondhar / Takkavi), and dug wells.'
            ],
            'Firuz Shah Tughlaq\'s Welfare & Orthodoxy': [
                'Appeasement of Nobility & Ulema: Made the Iqta system and administrative offices hereditary; restored confiscated land endowments to Ulema; banned un-Islamic court practices; imposed Jizya on Brahmins for the first time as a separate tax.',
                'Canal Networks & Agricultural Boom: Constructed 5 major irrigation canals (including Western Yamuna Canal and Satluj canal), irrigating extensive agricultural tracts in Haryana and Punjab; levied Haqq-i-Sharb (irrigation water cess at 1/10th of produce); planted 1,200 royal fruit orchards around Delhi.',
                'Welfare Institutions & Urban Foundations: Established Diwan-i-Khairat (charity department for poor girls\' marriages and orphans), Diwan-i-Bandagan (department for managing 180,000 royal slaves / Ghulam), and Dar-ul-Shafa (free state hospital in Delhi); founded new cities: Firozabad, Jaunpur (named after Muhammad bin Tughlaq / Jauna Khan), Hisar-Firoza, and Fatehabad; brought two Ashokan pillars from Topra (Haryana) and Meerut to Delhi.'
            ]
        },
        'upsc': {
            'prelims': [
                'Muhammad bin Tughlaq established a separate department of agriculture called "Diwan-i-Amir-Kohi" to encourage state-assisted cultivation and disburse Takkavi crop loans.',
                'Muhammad bin Tughlaq issued token currency made of copper and brass, minted at parity with silver Tankas, between 1329 and 1330 CE.',
                'Firuz Shah Tughlaq was the first Sultan of Delhi to impose Jizya on Brahmins as a distinct tax.',
                'Firuz Shah Tughlaq created a specialized department called "Diwan-i-Bandagan" to look after the welfare and training of over 180,000 state slaves.',
                'Firuz Shah Tughlaq constructed extensive canal networks in North India and levied an irrigation tax called "Haqq-i-Sharb" (10% of produce).',
                'The two Ashokan monolithic pillars from Topra (Haryana) and Meerut (UP) were transported and re-erected in Delhi by Firuz Shah Tughlaq.',
                'The Moroccan traveler Ibn Battuta visited India in 1334 CE during the reign of Muhammad bin Tughlaq, served as Qazi of Delhi, and wrote the travelogue Kitab-ur-Rihla.'
            ],
            'mains': [
                'Critically evaluate the five administrative and economic experiments of Muhammad bin Tughlaq, assessing whether their failure was due to conceptual flaws or defective execution.',
                'Compare and contrast the religious and administrative policies of Muhammad bin Tughlaq and Firuz Shah Tughlaq, with specific reference to their relations with the Ulema and the nobility.',
                'Examine Firuz Shah Tughlaq\'s public works infrastructure (canals, urban foundations, hospitals, and charity departments), evaluating its long-term impact on the agrarian economy of North India.',
                'Analyze the accounts of Ibn Battuta and Ziauddin Barani as primary sources for reconstructing the political psychology and administrative dynamics of the Tughlaq era.'
            ]
        }
    },
    'sayyid-dynasty': {
        'aspects': {
            'Origins & Timur\'s Shadow': [
                'Invasion of Timur (1398 CE): Timur\'s devastating sack of Delhi broke the backbone of the Tughlaq empire; appointed Khizr Khan (governor of Multan) as his viceroy in Punjab.',
                'Foundation: Khizr Khan (r. 1414–1421 CE) occupied Delhi, founding the Sayyid Dynasty; claimed direct descent from Prophet Muhammad; ruled not as independent Sultan but as "Rayat-i-Ala" (Vassal of Timur and his successor Shah Rukh).'
            ],
            'Political Instability & Decline': [
                'Successors: Mubarak Shah (r. 1421–1434 CE) suppressed rebellions in Mewat, Gwalior, and the Doab; founded the city of Mubarakabad on the Yamuna; patronized Yahya bin Ahmad Sirhindi, who authored the invaluable dynastic history Tarikh-i-Mubarak Shahi.',
                'End of Dynasty: Succeeded by Muhammad Shah and Alauddin Alam Shah; Alam Shah voluntarily abdicated the throne in 1451 CE in favor of Bahlul Lodi, retiring peacefully to Badaun, enabling the peaceful transition to the Afghan Lodi dynasty.'
            ]
        },
        'upsc': {
            'prelims': [
                'Khizr Khan founded the Sayyid dynasty in 1414 CE, ruling under the subordinate title "Rayat-i-Ala" acknowledging Timur and Shah Rukh.',
                'The historical chronicle Tarikh-i-Mubarak Shahi, an essential contemporary source for the Sayyid period, was authored by Yahya bin Ahmad Sirhindi.',
                'The last ruler of the Sayyid dynasty, Alauddin Alam Shah, peacefully abdicated the throne of Delhi in 1451 CE and retired to Badaun.',
                'The Sayyid dynasty rulers claimed direct biological descent from the Prophet Muhammad, hence the name "Sayyid".',
                'Mubarak Shah Sayyid founded the city of Mubarakabad along the banks of the Yamuna river.'
            ],
            'mains': [
                'Assess the political condition of Northern India following Timur\'s invasion (1398 CE) and analyze how Khizr Khan established the Sayyid dynasty amidst regional fragmentation.',
                'Evaluate the historical significance of Yahya Sirhindi\'s Tarikh-i-Mubarak Shahi in understanding the transition from the Tughlaqs to the Afghan Lodis.'
            ]
        }
    },
    'lodi-dynasty': {
        'aspects': {
            'First Afghan Empire in India': [
                'Afghan tribal confederacy ethos: Bahlul Lodi (r. 1451–1489 CE) established the First Afghan Empire in India; ruled on the principle of primus inter pares (first among equals), refusing to sit on an elevated throne in front of his Afghan tribal sardars; annexed the rival Sharqi Sultanate of Jaunpur (1479 CE), reuniting the central Gangetic plains with Delhi; issued the Bahloli copper coin.',
                'Sikandar Lodi (r. 1489–1517 CE): Greatest Lodi ruler; transformed tribal Afghan monarchy into a centralized imperial despotism; founded the city of Agra (1504 CE) as his second capital and military headquarters against Rajput confederacies.',
                'Measurement & Cultural patronage: Introduced standard measurement rod Gaz-i-Sikandari (32 digits / 39 inches) used up to Akbar\'s reign; composed Persian poetry under the pen-name "Gulrukhi"; had medical treatise Arghya-Roga translated from Sanskrit into Persian under the title Farhang-i-Sikandari; patron of classical music (Lahjat-i-Sikandar Shahi).'
            ],
            'Ibrahim Lodi & The Battle of Panipat (1526)': [
                'Despotic clash with Afghan Sardars: Ibrahim Lodi (r. 1517–1526 CE) asserted unbending royal absolutism, humiliating senior Afghan grandees (asserting "a king has no relatives or clan"); provoked rebellions by his uncle Alam Khan Lodi and Daulat Khan Lodi (Governor of Punjab), who invited Babur (ruler of Kabul) to invade India.',
                'First Battle of Panipat (21 April 1526): Babur\'s disciplined force of 12,000 men defeated Ibrahim Lodi\'s army of 100,000 soldiers and 1,000 elephants; Babur utilized field artillery (cannons under Ustad Ali and Mustafa) and the Ottoman Tulghuma tactical flanking system; Ibrahim Lodi died fighting on the battlefield (the only Delhi Sultan to perish in combat); marked the demise of the Delhi Sultanate and foundation of the Mughal Empire.'
            ]
        },
        'upsc': {
            'prelims': [
                'The First Afghan Empire in India was established by Bahlul Lodi in 1451 CE.',
                'Sikandar Lodi founded the city of Agra in 1504 CE and made it his capital in 1506 CE.',
                'The standard land measurement rod "Gaz-i-Sikandari" of 32 units was introduced by Sikandar Lodi and continued into the Mughal era.',
                'Sikandar Lodi composed Persian poems under the pen-name "Gulrukhi".',
                'The Sanskrit musical treatise Lahjat-i-Sikandar Shahi and medical treatise Farhang-i-Sikandari were compiled under Sikandar Lodi\'s patronage.',
                'The First Battle of Panipat took place on 21 April 1526, where Babur defeated Ibrahim Lodi using firearms and the Tulghuma flanking strategy.',
                'Ibrahim Lodi is the only Sultan of Delhi who died fighting on the battlefield.'
            ],
            'mains': [
                'Analyze the transition of Afghan political theory of kingship from Bahlul Lodi\'s tribal egalitarianism ("first among equals") to Sikandar and Ibrahim Lodi\'s centralized absolutism.',
                'Examine the political and administrative contributions of Sikandar Lodi, with specific reference to the foundation of Agra, the Gaz-i-Sikandari, and his cultural patronages.',
                'Discuss the tactical, technological, and political factors that enabled Babur to defeat Ibrahim Lodi at the First Battle of Panipat (1526).'
            ]
        }
    },
    'vijayanagara-empire': {
        'aspects': {
            'Genesis & Four Dynasties': [
                'Foundation (1336 CE): Founded on the banks of Tungabhadra by brothers Harihara I and Bukka I of the Sangama dynasty, under the spiritual guidance of sage Vidyaranya of the Sringeri Matha; four successive dynasties: 1. Sangama (1336–1485), 2. Saluva (1485–1505, founded by Saluva Narasimha), 3. Tuluva (1505–1570), 4. Aravidu (1570–1646, founded by Tirumala).',
                'Krishnadevaraya (r. 1509–1529 CE): Pinnacle of Tuluva glory; defeated Sultan of Bijapur (conquered Raichur Doab 1520), subjugated Gajapatis of Odisha (conquered Udayagiri, Kondavidu); styled "Andhra Bhoja", "Abhinava Bhoja", and "Yavana-rajya-sthapana-acharya"; friendly ties with Portuguese Governor Albuquerque (secured monopoly over Arabian war-horses).'
            ],
            'Administrative Institutions: Nayankara & Ayagar': [
                'Nayankara System: Provincial military-feudal organization; territories assigned to military commanders termed Amara-Nayakas; in exchange for revenue extraction, Nayakas maintained a fixed quota of foot-soldiers, cavalry, and war-elephants for the King and remitted an annual cash tribute to the royal treasury; maintained substantial local administrative autonomy.',
                'Ayagar System: Village self-governance; each village managed by a body of 12 hereditary village functionaries (Ayagars: headman/Gaunda, accountant/Karnam, blacksmith, carpenter, watchman, etc.); paid through tax-free land plots (Manyam) or a share of agricultural crops; eroded traditional Chola-style autonomous village assemblies.'
            ],
            'Art, Architecture & Mahanavami Festival': [
                'Vijayanagara Architectural Style: Monumental Raya Gopurams (soaring entrance towers); Kalyana Mandapas (intricately carved marriage halls with monolithic musical pillars); hippogryph / yali rearing horse pillars; monuments at Hampi: Hazara Rama Temple (carved with continuous narrative Ramayana bas-reliefs), Vitthala Temple (famous stone chariot and 56 musical pillars).',
                'Mahanavami Dibba: Massive stone stepped ceremonial platform; focal point of the 10-day state Mahanavami (Dussehra) festival where feudatory Nayakas paid annual homage, military parades were inspected, and animal sacrifices were performed.',
                'Foreign Chroniclers: Nicolo de Conti (Italian, visited 1420 under Devaraya I); Abdur Razzaq (Persian envoy of Shah Rukh, 1443 under Devaraya II: "The city is such that eyes have not seen, nor ears heard of any place to equal it on earth"); Duarte Barbosa (1518); Domingo Paes (1520–22 under Krishnadevaraya); Fernao Nuniz (1535–37 under Achyuta Raya).'
            ],
            'Battle of Talikota (1565) & Fall of Hampi': [
                'Rakshasi-Tangadi catastrophe: Regent Aliya Rama Raya played balance-of-power diplomacy among the Deccan Sultanates; provoked a united confederacy of four Deccan Sultanates (Bijapur, Golconda, Ahmednagar, Bidar); Rama Raya was captured and beheaded; the imperial metropolis of Hampi was systematically sacked, looted, and burned for six months; capital shifted south to Penukonda and Chandragiri under the Aravidu dynasty.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Vijayanagara Empire was founded in 1336 CE on the southern banks of the Tungabhadra river by Harihara and Bukka under the inspiration of sage Vidyaranya.',
                'Krishnadevaraya composed the epic Telugu treatise on statecraft, Amuktamalyada (story of Andal), and the Sanskrit drama Jambavati Kalyanam.',
                'Krishnadevaraya\'s royal court was adorned by the "Ashtadiggajas" (eight great Telugu poets), including Allasani Peddana (Andhra Kavita Pitamaha) and Tenali Ramakrishna.',
                'The Nayankara system in Vijayanagara was a military-feudal system where officers called Amara-Nayakas held land assignments in exchange for maintaining troops.',
                'The Ayagar system was an administrative system where 12 hereditary officials governed village affairs in the Vijayanagara Empire.',
                'The Persian ambassador Abdur Razzaq visited Vijayanagara in 1443 CE during the reign of Devaraya II, describing the seven concentric fortified rings of the city.',
                'The Battle of Talikota (also known as the Battle of Rakshasi-Tangadi) took place on 23 January 1565, in which the combined armies of Bijapur, Ahmednagar, Golconda, and Bidar destroyed Vijayanagara power.'
            ],
            'mains': [
                'Analyze the Nayankara and Ayagar administrative systems of the Vijayanagara Empire, comparing them with the Delhi Sultanate\'s Iqta system.',
                'Examine the political, military, and cultural achievements of Krishnadevaraya, evaluating why his reign is considered the Golden Age of South Indian history.',
                'Discuss the unique architectural and urban planning features of Hampi, with specific reference to the Vitthala Temple, Hazara Rama Temple, and the Mahanavami Dibba.',
                'Evaluate the accounts of foreign travelers (Abdur Razzaq, Domingo Paes, Fernao Nuniz) in reconstructing the urban wealth, military pageantry, and society of Vijayanagara.'
            ]
        }
    },
    'deccan-sultanate': {
        'aspects': {
            'Bahmani Empire & Mahmud Gawan': [
                'Foundation (1347 CE): Alauddin Hasan Bahman Shah (Zafar Khan) revolted against Muhammad bin Tughlaq, founding the Bahmani Kingdom (capitals: Gulbarga, later Bidar); perpetual geopolitical conflict with Vijayanagara over the fertile Krishna-Tungabhadra (Raichur) Doab and Marathwada ports (Goa).',
                'Mahmud Gawan (r. 1463–1481 CE as Prime Minister / Khwaja Jahan): Persian merchant-administrator; streamlined provincial governance by dividing the 4 bloated provinces (Tarafs) into 8 manageable districts; secured royal monopoly over artillery; constructed the world-famous three-storey Mahmud Gawan Madrasa at Bidar (Islamic college adorned with Persian tilework and 3,000-volume library); executed due to a forged treason letter planted by jealous rival Deccani nobles, leading to the collapse of Bahmani unity.'
            ],
            'The Five Deccan Sultanates & Architecture': [
                'Five successor sultanates: 1. Bijapur (Adil Shahi dynasty, 1490–1686, founded by Yusuf Adil Shah), 2. Golconda (Qutb Shahi dynasty, 1512–1687, founded by Quli Qutb Shah), 3. Ahmednagar (Nizam Shahi dynasty, 1490–1633, founded by Malik Ahmad), 4. Berar (Imad Shahi dynasty, 1490–1574), 5. Bidar (Barid Shahi dynasty, 1492–1619).',
                'Bijapur\'s architectural zenith: Gol Gumbaz (mausoleum of Muhammad Adil Shah) boasting the world\'s second largest dome (144-foot diameter) unsupported by pillars, and a legendary acoustic "Whispering Gallery" where soft murmurs echo 11 times; Ibrahim Rauza (tomb of Ibrahim Adil Shah II, "Jagadguru Badshah", author of musical treatise Kitab-i-Navras in Dakhani Urdu).',
                'Golconda & Hyderabad: Founded by Muhammad Quli Qutb Shah, who built the iconic Charminar in 1591 CE in Hyderabad to commemorate the eradication of plague; Golconda diamond mines (Kollur mine yielding the Koh-i-Noor, Hope, and Darya-i-Noor diamonds).',
                'Malik Ambar of Ahmednagar: Abyssinian prime minister; introduced guerrilla warfare (Bargir-giri) against Mughal armies; conducted scientific land revenue settlement based on actual crop measurement inspired by Todar Mal.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Bahmani Kingdom was founded in 1347 CE by Alauddin Hasan Bahman Shah (Zafar Khan), with its initial capital at Gulbarga (Ahsanabad).',
                'Mahmud Gawan, prime minister of the Bahmani Kingdom, built the monumental three-storey theological college (Madrasa) at Bidar in 1472 CE.',
                'The Gol Gumbaz in Bijapur is the mausoleum of Muhammad Adil Shah, renowned for its massive single dome and acoustic Whispering Gallery.',
                'Ibrahim Adil Shah II of Bijapur was titled "Jagadguru Badshah" and "Abla Baba" (friend of the poor) for his religious syncretism, authoring the musical classic Kitab-i-Navras.',
                'The Charminar in Hyderabad was built in 1591 CE by Muhammad Quli Qutb Shah to commemorate the cessation of a devastating plague epidemic.',
                'Malik Ambar, the prime minister of Ahmednagar, pioneered the "Bargir-giri" guerrilla warfare technique against the Mughals and reformed land revenue administration.',
                'The legendary diamond mines that produced the Koh-i-Noor diamond were situated in the Golconda Sultanate (Kollur mines).'
            ],
            'mains': [
                'Examine the administrative reforms and military modernization spearheaded by Mahmud Gawan in the Bahmani Sultanate, analyzing why his execution precipitated its disintegration.',
                'Trace the rise and architectural contributions of the Five Deccan Sultanates, with special focus on Gol Gumbaz in Bijapur and the Charminar in Hyderabad.',
                'Evaluate the political and military role of Malik Ambar in organizing Deccani resistance against Mughal imperial expansion in the 17th century.',
                'Analyze the cultural and literary synthesis achieved under the Deccan Sultanates, specifically the development of Dakhani language and miniature painting traditions.'
            ]
        }
    },
    'bhakti-sufi-movements': {
        'aspects': {
            'South Indian Origins: Alvars & Nayanars': [
                'Bhakti genesis in Tamilakam (6th–9th centuries CE): Rejection of orthodox caste hierarchies and austere Jain/Buddhist asceticism in favour of passionate emotional devotion (Bhakti) to a personal god.',
                'Alvars (12 Vaishnavite saints): Composed devotional hymns in Tamil compiled by Nathamuni into the 4,000-hymn compendium Nalayira Divya Prabandham (termed the "Tamil Veda"); prominent Alvars include Nammalvar, Periyalvar, and Andal (Kodhai - only female Alvar, worshipping Krishna as her divine husband).',
                'Nayanars (63 Shaivite saints): Composed hymns compiled by Nambiyandar Nambi into the 12-volume Tirumurai (first 7 volumes being Tevaram by Appar, Sambandar, Sundarar; Tiruvachakam by Manikkavacakar); female saint Karaikkal Ammaiyar (ascetic demoness form).'
            ],
            'Philosophical Acharyas: Vedanta Systems': [
                'Adi Shankara (9th cent): Advaita Vedanta (Absolute Non-Dualism); Brahman alone is real, the material world is an illusion (Maya); individual soul (Atman) is identical to Brahman ("Aham Brahmasmi"); established 4 monastic mathas (Badrinath in North, Puri in East, Sringeri in South, Dwarka in West).',
                'Ramanuja (11th–12th cent): Vishishtadvaita (Qualified Non-Dualism); Brahman possesses auspicious attributes; the world and souls are real modes of God; path of Prapatti (complete surrender) and Bhakti to Narayana.',
                'Madhvacharya (13th cent): Dvaita Vedanta (Strict Dualism); absolute eternal separation between God (Vishnu), individual souls, and matter.',
                'Nimbarka (Dvaitadvaita - Dualistic Non-Dualism) and Vallabhacharya (Shuddhadvaita - Pure Non-Dualism, Pushtimarga path of grace).'
            ],
            'North Indian Bhakti: Nirguna vs Saguna': [
                'Nirguna Tradition (Formless, Non-Anthropomorphic God): Ramananda brought Bhakti from South to North; Sant Kabir (disciple of Ramananda, weaver of Varanasi; rejected institutional rituals, temples, mosques, caste, and scriptures; expressed in Doha couplets compiled in the Bijak); Guru Nanak (1469–1539; founded Sikhism; emphasized "Ek Onkar", Langar communal kitchen, Pangat sitting together, Nam-Simran; hymns compiled in Guru Granth Sahib); Dadu Dayal (Dadu Panth).',
                'Saguna Tradition (God with Attributes & Incarnation): Tulsidas (Ramcharitmanas in Awadhi vernacular, making Valmiki\'s epic accessible to masses); Surdas (blind poet of Braj, Sursagar celebrating child Krishna); Mirabai (Rajput princess of Mewar, passionate Pada hymns to Giridhar Gopal); Chaitanya Mahaprabhu (1486–1534; Gaudiya Vaishnavism in Bengal; popularised collective Sankirtana congregational singing and chanting of Hare Krishna).'
            ],
            'Sufi Silsilas & Composite Culture': [
                'Core Sufi concepts: Wahdat-ul-Wujud (Unity of Being / pantheism proposed by Ibn Arabi); Khanqah (hospice / monastery); Pir / Murshid (spiritual master) and Murid (disciple); Zikr (remembrance of God) and Sama (musical assemblies).',
                'Chishti Silsila: Most popular liberal order; founded in India by Khwaja Moinuddin Chishti (Gharib Nawaz, settled at Ajmer 1192); prominent Chishti masters: Qutbuddin Bakhtiyar Kaki, Baba Farid (Fariduddin Ganj-i-Shakar, whose Punjabi verses are included in Guru Granth Sahib), Nizamuddin Auliya (Mehboob-i-Ilahi of Delhi; embraced voluntary poverty, refused royal court patronage; lived through 7 sultans), Nasiruddin Chirag-i-Dehlavi.',
                'Other major orders: Suhrawardi (Bahauddin Zakariya, Multan; accepted state patronage and royal gifts), Qadiri (orthodox), Naqshbandi (orthodox, militant revivalist led by Khwaja Baqi Billah and Shaikh Ahmad Sirhindi "Mujaddid Alif Sani", who fiercely opposed Akbar\'s Sulh-i-Kul).'
            ]
        },
        'upsc': {
            'prelims': [
                'Nalayira Divya Prabandham is the sacred Tamil hymn collection of the 12 Alvars, compiled by Nathamuni and known as the Tamil Veda.',
                'Andal was the only woman Alvar saint, celebrated for her devotional poetic works Thiruppavai and Nachiyar Thirumozhi.',
                'Adi Shankara propounded the Advaita (Non-Dualism) Vedanta philosophy and established four cardinal Mathas at Sringeri, Badrinath, Puri, and Dwarka.',
                'Ramanuja propounded Vishishtadvaita (Qualified Non-Dualism) and advocated that devotion (Bhakti) to Vishnu is the path to liberation.',
                'Kabir was a Nirguna Bhakti saint whose philosophical couplets are preserved in the Bijak, Sakhi Granth, and the Sikh Adi Granth.',
                'Baba Farid\'s devotional Punjabi verses were incorporated into the Sikh holy scripture, the Guru Granth Sahib.',
                'Shaikh Ahmad Sirhindi (Mujaddid Alif Sani) was a prominent Naqshbandi Sufi saint who opposed Akbar\'s liberal religious policies and the doctrine of Wahdat-ul-Wujud.'
            ],
            'mains': [
                'Examine the socio-religious revolt represented by the Bhakti and Sufi movements against ritualistic orthodoxy, social hierarchies, and caste discrimination in medieval India.',
                'Compare and contrast the Nirguna and Saguna Bhakti traditions with specific reference to Kabir, Guru Nanak, Tulsidas, and Mirabai.',
                'Analyze the Chishti Sufi silsila\'s integration into Indian society, assessing the role of Khanqahs, voluntary poverty, and Sama musical gatherings.',
                'Discuss the philosophical debate between Advaita Vedanta of Adi Shankara and Vishishtadvaita of Ramanuja, explaining their respective approaches to reality and devotion.'
            ]
        }
    }
}

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

count = 0
for p in d['periods']:
    pid = p['id']
    if pid in MEDIEVAL_ENRICHMENTS:
        enr = MEDIEVAL_ENRICHMENTS[pid]
        # Merge aspects
        if 'aspects' in enr:
            p.setdefault('aspects', {})
            for k, v in enr['aspects'].items():
                p['aspects'][k] = v
        # Replace / enhance upsc
        if 'upsc' in enr:
            p['upsc'] = enr['upsc']
        count += 1
        print(f"Successfully enriched Medieval period: {pid}")

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Total medieval periods enriched: {count}")
