# -*- coding: utf-8 -*-
import json
import os

with open('data/history.json', 'r', encoding='utf-8') as f:
    history = json.load(f)

existing_ids = {p['id'] for p in history['periods']}

new_periods = [
    # 1. Deccan Sultanates
    {
        "id": "deccan-sultanate",
        "title": "The Deccan Sultanates",
        "dateRange": "1490 – 1686 CE",
        "category": "medieval",
        "tagline": "Five Successor Sultanates of the Bahmani Kingdom — Ahmednagar, Bijapur, Berar, Golconda, and Bidar: Centers of Deccani Art, Architecture & Trade",
        "heroImg": "vijayanagara_empire.png",
        "sourceImages": ["vijayanagara_empire.png"],
        "overview": "Following the disintegration of the Bahmani Kingdom around 1490 CE, five independent sultanates emerged in the Deccan plateau: the Nizam Shahis of Ahmednagar, the Adil Shahis of Bijapur, the Imad Shahis of Berar, the Qutb Shahis of Golconda, and the Barid Shahis of Bidar. Despite frequent internecine wars and shifting alliances, the Deccan Sultanates formed a united front to defeat Vijayanagara at the pivotal Battle of Talikota (1565). They fostered a distinct Deccani culture synthesizing Persian, Turkish, and local Telugu, Kannada, and Marathi elements, creating architectural wonders like the Gol Gumbaz and Charminar before being annexed into the Mughal Empire under Aurangzeb.",
        "phases": [
            {
                "name": "Disintegration of Bahmani Kingdom & Emergence of Five Sultanates",
                "range": "1490 – 1520 CE",
                "points": [
                    "Malik Ahmad declared independence in Ahmednagar (Nizam Shahi dynasty) in 1490.",
                    "Yusuf Adil Shah established the Adil Shahi dynasty at Bijapur (1490).",
                    "Fathullah Imad-ul-Mulk founded the Imad Shahi dynasty in Berar (1490).",
                    "Sultan Quli Qutb-ul-Mulk proclaimed independence in Golconda (Qutb Shahi dynasty, 1512).",
                    "Qasim Barid founded the Barid Shahi dynasty in Bidar (1492–1528)."
                ]
            },
            {
                "name": "Deccan Alliance & The Battle of Talikota",
                "range": "1565 CE",
                "points": [
                    "The Sultanates of Bijapur, Ahmednagar, Golconda, and Bidar forged a historic alliance against Vijayanagara ruler Aliya Rama Raya.",
                    "Battle of Talikota (Rakshasi-Tangadi, January 1565): The combined Sultanate artillery and cavalry decisively crushed Vijayanagara, leading to the destruction of Hampi.",
                    "Berar was subsequently annexed by Ahmednagar in 1574; Bidar was annexed by Bijapur in 1619."
                ]
            },
            {
                "name": "The Era of Malik Ambar & Cultural Flourishing",
                "range": "1580 – 1630 CE",
                "points": [
                    "Regency of Chand Bibi defending Ahmednagar and Bijapur against Mughal incursions.",
                    "Malik Ambar (an Ethiopian / Habshi military genius and Prime Minister of Ahmednagar) pioneered guerrilla warfare (Bargir-giri) and the revenue assessment system (Ain-i-Dahsala equivalent).",
                    "Ibrahim Adil Shah II of Bijapur ('Jagadguru Badshah') composed the musical treatise Kitab-i-Navras in Dakhani Urdu, honoring Saraswati and Ganesha.",
                    "Muhammad Quli Qutb Shah built the iconic Charminar in Hyderabad (1591) to commemorate the eradication of plague."
                ]
            },
            {
                "name": "Mughal Conquest & Annexation",
                "range": "1636 – 1687 CE",
                "points": [
                    "Shah Jahan's Treaties of 1636 forced Bijapur and Golconda to accept Mughal suzerainty and pay tributes.",
                    "Aurangzeb personally led imperial armies to conquer Bijapur (1686, capturing Sikandar Adil Shah) and Golconda (1687, capturing Abul Hasan Tana Shah after 8-month siege of Golconda Fort)."
                ]
            }
        ],
        "aspects": {
            "Administration & Military Innovations": [
                "Pioneered guerilla cavalry tactics (Bargir-giri / Ganimi Kava), later mastered by Chhatrapati Shivaji Maharaj.",
                "Recruitment of Habshis (African elite soldiers/administrators like Malik Ambar) alongside Persian (Afaqi) and local Deccani nobles.",
                "Extensive employment of Maratha revenue officers and cavalry commanders, laying the administrative groundwork for the Maratha state."
            ],
            "Deccani Art & Architecture": [
                "Gol Gumbaz (Bijapur): Mausoleum of Muhammad Adil Shah featuring the world's second-largest dome (unsupported by pillars) and acoustic whispering gallery.",
                "Charminar & Mecca Masjid (Hyderabad): Grand Qutb Shahi granite and stucco monuments with minarets and arcades.",
                "Mahmud Gawan Madrasa (Bidar): Three-storey Persian college with glazed tiles, minarets, and a 3,000-manuscript library.",
                "Deccani Miniature Painting: Brilliant jewel-like colors, elongated figures, and Persian-Turkish-Vijayanagara fusion."
            ],
            "Economy & Trade": [
                "World-renowned diamond mining in Golconda (Kollur Mines produced Koh-i-Noor, Hope, and Darya-i-Noor diamonds).",
                "Vibrant maritime trade through port of Machilipatnam and Konkan ports (Dabhol, Chaul) with Persian Gulf, Southeast Asia, and Europe (Dutch and English East India Companies)."
            ]
        },
        "women": [
            {
                "name": "Chand Bibi",
                "role": "Regent of Bijapur & Warrior Queen of Ahmednagar",
                "note": "Famous for defending Ahmednagar fort against Mughal imperial armies under Prince Murad in 1595, wearing armor and personally overseeing defensive artillery."
            },
            {
                "name": "Hayat Bakshi Begum",
                "role": "Queen Mother & Diplomat of Golconda",
                "note": "Influential Qutb Shahi diplomat and patron of mosques, caravanserais, and charitable institutions in Hyderabad; negotiated peace with Aurangzeb."
            }
        ],
        "events": [
            {
                "year": "1490 CE",
                "title": "Tripartite Breakup of Bahmani Kingdom",
                "desc": "Ahmednagar, Bijapur, and Berar simultaneously declare independence from the Bahmani Sultanate.",
                "theme": "polity"
            },
            {
                "year": "1565 CE",
                "title": "Battle of Talikota (Rakshasi-Tangadi)",
                "desc": "The alliance of Bijapur, Ahmednagar, Golconda, and Bidar decisively defeats the Vijayanagara Empire.",
                "theme": "war"
            },
            {
                "year": "1591 CE",
                "title": "Foundation of Hyderabad & Construction of Charminar",
                "desc": "Muhammad Quli Qutb Shah founds Hyderabad and constructs the four-minaret monument.",
                "theme": "art"
            },
            {
                "year": "1686–1687 CE",
                "title": "Mughal Annexation of Bijapur and Golconda",
                "desc": "Emperor Aurangzeb besieges and annexes Bijapur (1686) and Golconda (1687), ending Sultanate rule.",
                "theme": "war"
            }
        ],
        "people": [
            {
                "name": "Malik Ambar",
                "role": "Prime Minister & Military Commander of Ahmednagar",
                "note": "Ethiopian-born statesman who introduced land revenue surveys, built modern Aurangabad (Fatehnagar), and repeatedly thwarted Mughal expansion."
            },
            {
                "name": "Ibrahim Adil Shah II",
                "role": "King of Bijapur, Scholar & Musician",
                "note": "Author of Kitab-i-Navras, patron of arts and architecture (Ibrahim Rauza), renowned for secular governance and syncretism."
            }
        ],
        "themes": ["polity", "war", "art", "economy", "society"],
        "upsc": {
            "prelims": [
                "Identify the 5 Deccan Sultanates and their dynasties: Ahmednagar (Nizam Shahi), Bijapur (Adil Shahi), Berar (Imad Shahi), Golconda (Qutb Shahi), Bidar (Barid Shahi).",
                "Ibrahim Adil Shah II was titled 'Jagadguru Badshah' and wrote 'Kitab-i-Navras' in Dakhani Urdu.",
                "Malik Ambar introduced the Bargir-giri guerrilla warfare technique in the Deccan.",
                "Gol Gumbaz at Bijapur is celebrated for its acoustic whispering gallery and massive unsupported circular dome."
            ],
            "mains": [
                "Evaluate the socio-political impact of the Battle of Talikota (1565) on peninsular India and the subsequent rise of Maratha power.",
                "Discuss the architectural and artistic contributions of the Deccan Sultanates, contrasting them with contemporary Mughal architecture."
            ]
        },
        "quickFacts": [
            ["Dynasties", "5 Successor Sultanates (1490–1687 CE)"],
            ["Decisive Battle", "Talikota / Rakshasi-Tangadi (1565 CE)"],
            ["Key Architectural Wonders", "Gol Gumbaz (Bijapur), Charminar (Hyderabad), Ibrahim Rauza"],
            ["Diamond Capital", "Golconda (Kollur Mines - source of Koh-i-Noor)"],
            ["Military Genius", "Malik Ambar (Pioneered Bargir-giri guerilla tactics)"]
        ]
    },

    # 2. Maratha Empire
    {
        "id": "maratha-empire",
        "title": "The Maratha Empire & Confederacy",
        "dateRange": "1674 – 1818 CE",
        "category": "regional",
        "tagline": "Hindavi Swarajya under Chhatrapati Shivaji Maharaj, the Ashtapradhan, Peshwa Ascendancy, Panipat III & Resistance to British Colonialism",
        "heroImg": "birtish_establishment.png",
        "sourceImages": ["birtish_establishment.png"],
        "overview": "Founded by Chhatrapati Shivaji Maharaj in 1674 amidst the rugged Sahyadri terrain of the Western Ghats, the Maratha state transformed from a regional kingdom into the supreme military power of 18th-century India. Resisting Mughal onslaughts under Aurangzeb through prolonged guerrilla resistance (under Sambhaji, Rajaram, and Maharani Tarabai), the Marathas rose to pan-Indian hegemony under the hereditary Peshwas (Balaji Vishwanath, Baji Rao I, and Balaji Baji Rao). Operating as a vast confederacy (Scindias, Holkars, Gaekwads, Bhonsles), the Marathas collected Chauth and Sardeshmukhi across the subcontinent until the catastrophic Third Battle of Panipat (1761) and eventual defeat in the three Anglo-Maratha Wars (1775–1818).",
        "phases": [
            {
                "name": "Chhatrapati Shivaji & The Founding of Hindavi Swarajya",
                "range": "1645 – 1680 CE",
                "points": [
                    "Shivaji captured Torna Fort (1646), killed Afzal Khan at Pratapgad (1659), and raided Shaista Khan's camp in Pune (1663).",
                    "Treaty of Purandar (1665) signed with Jai Singh; Shivaji's daring escape from Aurangzeb's captivity in Agra (1666).",
                    "Coronation (Rajyabhisheka) at Raigad Fort in 1674; assumed title of Chhatrapati and established sovereign coinage (Shivrai and Hon)."
                ]
            },
            {
                "name": "The War of 27 Years & Regency of Maharani Tarabai",
                "range": "1681 – 1707 CE",
                "points": [
                    "Aurangzeb personally moved his imperial court to the Deccan to crush the Marathas.",
                    "Execution of Chhatrapati Sambhaji (1689); Rajaram established capital at Jinji (Tamil Nadu) during an 8-year siege.",
                    "Maharani Tarabai took leadership in 1700, rallying Maratha sardars and launching counter-invasions into Mughal Malwa and Gujarat, wearing down Aurangzeb until his death in 1707."
                ]
            },
            {
                "name": "Peshwa Ascendancy & Pan-Indian Expansion",
                "range": "1713 – 1761 CE",
                "points": [
                    "Chhatrapati Shahu appointed Balaji Vishwanath as Peshwa (1713), establishing hereditary ministerial power centered at Shaniwar Wada, Pune.",
                    "Peshwa Baji Rao I (1720–1740) led 41 victorious military campaigns ('Strike at the trunk of the withering Mughal tree'), defeating the Nizam at Palkhed (1728) and Bhopal (1737).",
                    "Balaji Baji Rao (Nana Saheb) expanded the empire to its territorial zenith, planting the saffron flag (Bhagwa Dhwaj) on the banks of the Indus at Attock (1758)."
                ]
            },
            {
                "name": "Panipat III, The Confederacy & Anglo-Maratha Wars",
                "range": "1761 – 1818 CE",
                "points": [
                    "Third Battle of Panipat (14 January 1761): Ahmad Shah Abdali crushed the Maratha army under Sadashivrao Bhau and Vishwasrao.",
                    "Maratha Resurrection under Peshwa Madhavrao I and Mahadji Scindia, restoring Mughal Emperor Shah Alam II to the Delhi throne.",
                    "Internal factionalism after Nana Fadnavis led to the Maratha Confederacy (Peshwa, Scindia of Gwalior, Holkar of Indore, Gaekwad of Baroda, Bhonsle of Nagpur).",
                    "Three Anglo-Maratha Wars (1775–1818) ended in the dissolution of the Peshwaship and British annexation of Maharashtra."
                ]
            }
        ],
        "aspects": {
            "Ashtapradhan Administrative Council": [
                "Peshwa (Prime Minister / general supervision).",
                "Amatya / Mazumdar (Finance and revenue minister).",
                "Waqia-Navis / Mantri (Internal affairs, records, intelligence).",
                "Samant / Dabir (Foreign affairs).",
                "Sachiv / Shurnavis (Royal correspondence).",
                "Panditrao (Religious disputes and charity).",
                "Nyayadhish (Chief Justice).",
                "Senapati / Sari-Naubat (Commander-in-Chief)."
            ],
            "Revenue System: Chauth & Sardeshmukhi": [
                "Chauth: 1/4th (25%) of land revenue levied on non-Maratha territories as protection money against Maratha raids.",
                "Sardeshmukhi: An additional 1/10th (10%) levy claimed by the Maratha ruler as hereditary supreme head (Sardeshmukh) of the land.",
                "Kathi system: Shivaji measured agricultural land using a standardized rod (Kathi) and eliminated oppressive Zamindari intermediaries (Deshmukhs and Kulkarnis)."
            ],
            "Military System & Fort Architecture": [
                "Ganimi Kava: Masterful guerrilla warfare utilizing hill forts, rapid light cavalry, and deep knowledge of Sahyadri geography.",
                "Extensive network of over 300 hill and coastal forts (Raigad, Rajgad, Pratapgad, Sinhagad, Sindhudurg sea fort, Vijaydurg).",
                "Pioneering Maratha Navy (Armada) organized under Admiral Kanhoji Angre, dominating the western coastline against Portuguese, Dutch, and English fleets."
            ]
        },
        "women": [
            {
                "name": "Jijabai (Rajmata)",
                "role": "Mother, Mentor & Political Guide of Shivaji",
                "note": "Instilled principles of swarajya, dharma, and righteous governance in Shivaji; managed the Pune Jagir with exceptional judicial acumen."
            },
            {
                "name": "Maharani Tarabai",
                "role": "Queen Regent & Military Commander",
                "note": "Led the Maratha resistance (1700–1707) after husband Rajaram's death; personally planned offensive campaigns against Aurangzeb's grand army."
            },
            {
                "name": "Ahilyabai Holkar",
                "role": "Philosopher Queen of Malwa (Maheshwar)",
                "note": "Revered administrator who transformed Indore, defended her state against invaders, and rebuilt major Hindu temples across India (Kashi Vishwanath, Somnath, Gaya)."
            }
        ],
        "events": [
            {
                "year": "1674 CE",
                "title": "Coronation of Chhatrapati Shivaji Maharaj",
                "desc": "Shivaji is crowned Chhatrapati at Raigad Fort by Pandit Gaga Bhatt, establishing sovereign Hindavi Swarajya.",
                "theme": "polity"
            },
            {
                "year": "1728 CE",
                "title": "Battle of Palkhed",
                "desc": "Peshwa Baji Rao I defeats Nizam-ul-Mulk of Hyderabad using brilliant mobile cavalry maneuvers.",
                "theme": "war"
            },
            {
                "year": "1758 CE",
                "title": "Maratha Conquest of Attock",
                "desc": "Raghunathrao and Malhar Rao Holkar capture Attock, expanding Maratha boundaries to the Khyber Pass.",
                "theme": "war"
            },
            {
                "year": "1761 CE",
                "title": "Third Battle of Panipat",
                "desc": "Ahmad Shah Durrani defeats the Marathas in one of the bloodiest single-day battles of the 18th century.",
                "theme": "war"
            },
            {
                "year": "1818 CE",
                "title": "End of Maratha Power (Third Anglo-Maratha War)",
                "desc": "Battle of Koregaon and defeat of Peshwa Baji Rao II; British abolish the Peshwaship.",
                "theme": "colonial"
            }
        ],
        "people": [
            {
                "name": "Chhatrapati Shivaji Maharaj",
                "role": "Founder of the Maratha Empire",
                "note": "Strategic genius who established Hindavi Swarajya, built a powerful navy and fort system, and formulated the Ashtapradhan administration."
            },
            {
                "name": "Peshwa Baji Rao I",
                "role": "Peshwa & Military Strategist",
                "note": "Undefeated general in 41 battles; transformed the Maratha state into a pan-Indian empire through blitzkrieg cavalry maneuvers."
            },
            {
                "name": "Mahadji Scindia",
                "role": "Ruler of Gwalior & Regent of Delhi",
                "note": "Modernized the Maratha army with European discipline (under Benoit de Boigne) and dominated North Indian politics."
            },
            {
                "name": "Nana Fadnavis",
                "role": "Statesman & Chief Minister of the Confederacy",
                "note": "Known as the 'Maratha Machiavelli' for holding together the Maratha Confederacy against internal intrigues and British diplomacy."
            }
        ],
        "themes": ["polity", "war", "economy", "society", "women"],
        "upsc": {
            "prelims": [
                "Explain the Ashtapradhan council: All members except Panditrao and Nyayadhish were required to command military forces.",
                "Differentiate Chauth (25% protection levy on neighbouring states) from Sardeshmukhi (additional 10% hereditary claim).",
                "Kanhoji Angre was the supreme admiral of the Maratha naval armada guarding the Konkan coast.",
                "Ahilyabai Holkar rebuilt the sacred Kashi Vishwanath temple at Varanasi in 1780."
            ],
            "mains": [
                "Analyze the factors responsible for the rise of the Marathas in the 17th century and examine the administrative innovations introduced by Shivaji.",
                "Critically evaluate the strategic and political consequences of the Third Battle of Panipat (1761) on the fate of India and British expansion."
            ]
        },
        "quickFacts": [
            ["Founder", "Chhatrapati Shivaji Maharaj (Coronation 1674 at Raigad)"],
            ["Administrative Council", "Ashtapradhan (8 Ministers)"],
            ["Key Taxes", "Chauth (25%) & Sardeshmukhi (10%)"],
            ["Turning Point", "Third Battle of Panipat (14 January 1761)"],
            ["Confederacy Houses", "Peshwa (Pune), Scindia (Gwalior), Holkar (Indore), Gaekwad (Baroda), Bhonsle (Nagpur)"]
        ]
    },

    # 3. Industrial Revolution & Rise of Capitalism
    {
        "id": "industrial-revolution-and-capitalism",
        "title": "The Industrial Revolution & Rise of Capitalism",
        "dateRange": "1750 – 1900 CE",
        "category": "world",
        "tagline": "Steam Power, Mechanization, Factory Systems, Rise of Industrial Capitalism & The Re-shaping of World Economies",
        "heroImg": "world_history.png",
        "sourceImages": ["world_history.png"],
        "overview": "Beginning in Great Britain during the mid-18th century, the Industrial Revolution fundamentally transformed human civilization from an agrarian, handicraft-based economy into an industrial society powered by machines, fossil fuels (coal), and mass production in factories. Driven by agricultural enclosures, colonial capital accumulation, scientific innovations (James Watt's steam engine, Hargreaves' spinning jenny, Arkwright's water frame), and abundant coal-iron deposits, industrialization gave birth to modern Industrial Capitalism, rapid urbanization, and a sharp polarization between the capitalist bourgeoisie and the industrial proletariat. The hunger for cheap raw materials and captive consumer markets fueled 19th-century imperialist conquest and precipitated the systematic de-industrialization of traditional artisanal economies in colonized nations like India.",
        "phases": [
            {
                "name": "First Industrial Revolution (Britain)",
                "range": "1750 – 1840 CE",
                "points": [
                    "Mechanization of textile production: Kay's flying shuttle, Hargreaves' spinning jenny, and Crompton's mule.",
                    "James Watt perfected the commercial steam engine (1769–1776), liberating factories from reliance on river water power.",
                    "Railway revolution: Stephenson's Rocket (1829) ignited national rail networks, compressing transport time and freight costs."
                ]
            },
            {
                "name": "Social Impact & Working-Class Resistance",
                "range": "1800 – 1850 CE",
                "points": [
                    "Unprecedented rapid urbanization: Cities like Manchester, Birmingham, and Leeds swelled into squalid, disease-ridden urban slums without sanitation.",
                    "Exploitation of women and children in coal mines and cotton textile mills with 14-16 hour workdays and hazardous conditions.",
                    "Luddite Movement (machine wreckers) and the Chartist Movement demanding universal male suffrage and workers' political rights."
                ]
            },
            {
                "name": "Second Industrial Revolution & Global Spread",
                "range": "1870 – 1914 CE",
                "points": [
                    "Spread to Germany, the United States, and Japan (Meiji Industrialization).",
                    "Technological shifts: Steel production (Bessemer process), chemical industry, electricity (Edison, Tesla), and internal combustion engines (petroleum).",
                    "Rise of giant corporate trusts, monopolies, and finance capitalism."
                ]
            },
            {
                "name": "Colonial Exploitation & De-Industrialization of India",
                "range": "1800 – 1900 CE",
                "points": [
                    "British one-way free trade: Machine-made Manchester textiles flooded Indian markets while heavy tariffs blocked Indian exports.",
                    "De-industrialization: Ruin of millions of Indian handloom weavers ('The bones of the cotton weavers are bleaching the plains of India' — Lord William Bentinck).",
                    "India was reduced from the world's premier textile exporter to an agrarian supplier of raw cotton, jute, tea, and indigo."
                ]
            }
        ],
        "aspects": {
            "Core Technological Inventions": [
                "Spinning Jenny (James Hargreaves, 1764) and Water Frame (Richard Arkwright, 1769).",
                "Steam Engine (James Watt, 1769) enabling mechanized mining, manufacturing, and transport.",
                "Locomotives and Steamships (George Stephenson, Robert Fulton) enabling global freight mobility.",
                "Bessemer Process (1856) enabling mass, cheap steel production for infrastructure."
            ],
            "Rise of Industrial Capitalism & Ideologies": [
                "Adam Smith's The Wealth of Nations (1776) articulated laissez-faire, market competition, and the 'invisible hand'.",
                "Emergence of the Industrial Bourgeoisie (factory owners, bankers) eclipsing landed aristocracy in political influence.",
                "Proletarianization: Masses of dispossessed peasants becoming wage-dependent industrial workers.",
                "Critique by Karl Marx & Friedrich Engels (The Communist Manifesto 1848, Das Kapital) analyzing class conflict and surplus value extraction."
            ],
            "Social & Environmental Repercussions": [
                "Extreme urban degradation: Typhus, cholera outbreaks, air pollution from coal smog, and absence of public health infrastructure.",
                "Passage of Factory Acts (1833, 1847) gradually limiting child labor and enforcing 10-hour workdays in Britain.",
                "Global environmental shifts: Accelerated carbon emissions initiating modern anthropogenic climate change."
            ]
        },
        "events": [
            {
                "year": "1769 CE",
                "title": "James Watt Patents the Steam Engine",
                "desc": "Watt develops a separate condenser steam engine, unlocking continuous mechanical energy.",
                "theme": "science"
            },
            {
                "year": "1811–1816 CE",
                "title": "The Luddite Uprisings",
                "desc": "British textile artisans smash mechanized looms in protest against wage cuts and job destruction.",
                "theme": "society"
            },
            {
                "year": "1830 CE",
                "title": "Liverpool and Manchester Railway Opens",
                "desc": "First twin-track inter-city passenger and goods railway opens, signaling the railway age.",
                "theme": "economy"
            },
            {
                "year": "1848 CE",
                "title": "Publication of The Communist Manifesto",
                "desc": "Karl Marx and Friedrich Engels formulate scientific socialism as a critique of industrial capitalism.",
                "theme": "polity"
            }
        ],
        "people": [
            {
                "name": "James Watt",
                "role": "Scottish Inventor & Mechanical Engineer",
                "note": "Perfected the steam engine, transforming manufacturing, mining, and transport globally."
            },
            {
                "name": "Adam Smith",
                "role": "Scottish Economist & Philosopher",
                "note": "Father of modern capitalism; formulated free market principles, division of labor, and laissez-faire economics."
            },
            {
                "name": "Robert Owen",
                "role": "Utopian Socialist & Industrialist",
                "note": "Pioneered cooperative communities and humane factory conditions at New Lanark mills in Scotland."
            }
        ],
        "themes": ["economy", "science", "society", "polity", "foreign"],
        "upsc": {
            "prelims": [
                "Why did the Industrial Revolution begin first in Britain? Availability of coal and iron, agricultural surplus, rule of law, colonial capital accumulation, and strong naval merchant fleet.",
                "The Luddite movement was an anti-mechanization rebellion by British skilled handloom weavers.",
                "The Bessemer process enabled the mass, low-cost production of steel during the Second Industrial Revolution."
            ],
            "mains": [
                "Examine the socio-economic conditions in 18th-century Britain that catalyzed the Industrial Revolution.",
                "'The Industrial Revolution in Britain was subsidized by the de-industrialization of India.' Critically evaluate this statement."
            ]
        },
        "quickFacts": [
            ["Origin", "Great Britain (c. 1750–1850 CE)"],
            ["Key Power Source", "Coal and Steam Engine (James Watt)"],
            ["Primary Early Sector", "Cotton Textiles"],
            ["Key Political Philosophy", "Classical Capitalism (Adam Smith) & Marxist Socialism (Karl Marx)"],
            ["Impact on India", "Systematic De-industrialization & Conversion into Raw Material Exporter"]
        ]
    },

    # 4. American Revolution & US Civil War
    {
        "id": "american-revolution-and-civil-war",
        "title": "The American Revolution, US Civil War & Global Impacts",
        "dateRange": "1775 – 1865 CE",
        "category": "world",
        "tagline": "Colonial Independence, Constitutional Democracy, Lincoln, the Abolition of Slavery & Global Repercussions on India",
        "heroImg": "french_revolution.png",
        "sourceImages": ["french_revolution.png"],
        "overview": "The American War of Independence (1775–1783) resulted in the world's first modern constitutional democratic republic. Rebelling against British mercantilist taxation ('No taxation without representation') and colonial restrictions, thirteen American colonies declared independence on 4 July 1776, defeated British imperial forces under George Washington, and enacted the US Constitution with a Bill of Rights. Less than a century later, the structural contradiction between the industrializing, free-labor North and the plantation, slave-owning South triggered the bloody American Civil War (1861–1865). Led by President Abraham Lincoln, the Union was preserved and slavery abolished (13th Amendment). The disruption of American cotton exports during the Civil War triggered a massive 'Cotton Boom' in western India, fundamentally altering Indian agrarian relations and setting off the Deccan Riots of 1875.",
        "phases": [
            {
                "name": "Causes of the American Revolution",
                "range": "1763 – 1775 CE",
                "points": [
                    "British victory in the Seven Years' War (1756–1763) left Britain in debt, prompting Parliament to levy taxes on the American colonies.",
                    "Controversial enactments: Stamp Act (1765), Townshend Acts (1767), and Tea Act (1773).",
                    "Colonial resistance: Boston Massacre (1770), Boston Tea Party (1773), and Continental Congress meeting at Philadelphia (1774)."
                ]
            },
            {
                "name": "War of Independence & Constitutional Founding",
                "range": "1775 – 1789 CE",
                "points": [
                    "Outbreak of war at Lexington and Concord (April 1775); George Washington appointed Commander-in-Chief.",
                    "Declaration of Independence adopted on 4 July 1776, drafted by Thomas Jefferson ('All men are created equal... Life, Liberty and the pursuit of Happiness').",
                    "French military and financial alliance (Lafayette, Rochambeau) tipped the balance; British surrender at Yorktown (1781) and Treaty of Paris (1783).",
                    "US Constitution drafted at Philadelphia Convention (1787); established federalism, separation of powers, and the Bill of Rights (1791)."
                ]
            },
            {
                "name": "The American Civil War & Abolition of Slavery",
                "range": "1861 – 1865 CE",
                "points": [
                    "Deep polarization between the industrial Northern states and the Southern agrarian plantation economy dependent on chattel slavery.",
                    "Election of Abraham Lincoln (1860) led 11 Southern states to secede and form the Confederate States of America under Jefferson Davis.",
                    "Bloody military campaigns: Battle of Antietam (1862), Battle of Gettysburg (1863 - Turning point).",
                    "Lincoln issued the Emancipation Proclamation (1 January 1863), declaring all enslaved people in Confederate territory free.",
                    "Surrender of Confederate General Robert E. Lee at Appomattox (April 1865); passage of the 13th Amendment abolishing slavery."
                ]
            },
            {
                "name": "Global Impact & The Cotton Boom in India",
                "range": "1861 – 1875 CE",
                "points": [
                    "Union naval blockade cut off Southern cotton exports to Lancashire mills in Britain ('Cotton Famine').",
                    "Britain turned to India: Bombay presidency witnessed an unprecedented 'Cotton Boom' (1861–1865) as raw cotton prices soared.",
                    "Indian peasants borrowed heavily from Sahukars (moneylenders) to expand cotton cultivation.",
                    "Civil War end (1865) brought sudden collapse of cotton prices; peasants were trapped in unpayable debt, sparking the violent Deccan Riots of 1875 and passage of the Deccan Agriculturists' Relief Act 1879."
                ]
            }
        ],
        "aspects": {
            "Ideological Pillars of the American Revolution": [
                "Enlightenment philosophy: John Locke's natural rights (life, liberty, property) and social contract theory.",
                "Montesquieu's doctrine of Separation of Powers (Executive, Legislature, Judiciary) and checks and balances.",
                "Inspiration for global anti-colonial movements and the 1789 French Revolution."
            ],
            "US Civil War Significance": [
                "Preservation of the democratic Union and confirmation of federal supremacy over state secession rights.",
                "Abolition of human chattel slavery via the 13th Amendment (1865), and citizenship rights via 14th Amendment (1868).",
                "Transformation of the United States into a unified continental industrial powerhouse."
            ],
            "Impact on Indian Economy & Society": [
                "Demonstrated the hyper-vulnerability of Indian colonial agriculture to distant global geopolitical shocks.",
                "Commercialization of agriculture without institutional credit forced ryots into hereditary debt bondage.",
                "Catalyzed early Indian nationalist economic thinking (Dadabhai Naoroji, M.G. Ranade) on rural indebtedness and market distortion."
            ]
        },
        "events": [
            {
                "year": "1773 CE",
                "title": "The Boston Tea Party",
                "desc": "American colonists dump 342 chests of British East India Company tea into Boston harbor to protest taxation without representation.",
                "theme": "polity"
            },
            {
                "year": "1776 CE",
                "title": "US Declaration of Independence",
                "desc": "Continental Congress adopts the Declaration drafted by Thomas Jefferson on 4 July 1776.",
                "theme": "polity"
            },
            {
                "year": "1863 CE",
                "title": "Emancipation Proclamation & Gettysburg Address",
                "desc": "President Abraham Lincoln declares slaves in rebel states free and delivers the Gettysburg Address.",
                "theme": "society"
            },
            {
                "year": "1861–1865 CE",
                "title": "Bombay Cotton Boom in India",
                "desc": "American Civil War cuts global cotton supply, triggering a 4-year speculative boom in Indian cotton export.",
                "theme": "economy"
            },
            {
                "year": "1875 CE",
                "title": "The Deccan Riots in India",
                "desc": "Post-Civil War cotton crash traps Ryots in debt; peasants revolt against Marwari and Gujarati moneylenders in Pune and Ahmednagar.",
                "theme": "society"
            }
        ],
        "people": [
            {
                "name": "George Washington",
                "role": "General & First US President",
                "note": "Led the Continental Army to victory over Britain; presided over the drafting of the US Constitution."
            },
            {
                "name": "Thomas Jefferson",
                "role": "Founding Father & 3rd US President",
                "note": "Principal author of the Declaration of Independence; championed individual liberty and republicanism."
            },
            {
                "name": "Abraham Lincoln",
                "role": "16th US President",
                "note": "Preserved the Union through the Civil War, issued the Emancipation Proclamation, and abolished slavery."
            }
        ],
        "themes": ["polity", "war", "economy", "society", "foreign"],
        "upsc": {
            "prelims": [
                "The phrase 'No taxation without representation' was the rallying slogan of the American Revolution.",
                "The Treaty of Paris (1783) formally recognized American independence from Great Britain.",
                "The American Civil War directly caused the Bombay Cotton Boom (1861-1865) and subsequent Deccan Riots of 1875 in India."
            ],
            "mains": [
                "Examine how the American War of Independence was an economic conflict disguised in constitutional rhetoric.",
                "Discuss the ripple effects of the American Civil War on Indian agriculture and colonial agrarian unrest in the late 19th century."
            ]
        },
        "quickFacts": [
            ["Declaration of Independence", "4 July 1776 (Philadelphia)"],
            ["Key Leaders", "George Washington, Thomas Jefferson, Benjamin Franklin"],
            ["Civil War Duration", "1861 – 1865 CE"],
            ["Constitutional Landmark", "13th Amendment (Abolition of Slavery)"],
            ["Direct Impact on India", "Bombay Cotton Boom (1861–65) & Deccan Riots (1875)"]
        ]
    },

    # 5. Cold War, Decolonisation & Political Philosophies
    {
        "id": "cold-war-and-decolonisation",
        "title": "The Cold War, Decolonisation & Political Philosophies",
        "dateRange": "1945 – 1991 CE",
        "category": "world",
        "tagline": "Bipolar Hegemony, Nuclear Brinkmanship, Third World Decolonisation, Collapse of USSR & Competing Ideologies (Communism, Capitalism, Socialism)",
        "heroImg": "world_war_II.png",
        "sourceImages": ["world_war_II.png"],
        "overview": "The post-World War II global order was defined by the ideological, geopolitical, and military confrontation between two nuclear superpowers: the capitalist United States and the communist Soviet Union. Characterized by proxy wars (Korean War, Vietnam War), nuclear arms race (MAD doctrine), and intelligence contests rather than direct military clash, the Cold War spanned from the division of Europe (Iron Curtain) to the fall of the Berlin Wall (1989) and the dissolution of the USSR (1991). Concurrently, a historic wave of Decolonization swept Asia and Africa, leading newly liberated nations to pioneer the Non-Aligned Movement (NAM). The era tested and transformed the three dominant political philosophies of modernity: Communism, Capitalism, and Socialism.",
        "phases": [
            {
                "name": "Origins of Cold War & Division of Europe",
                "range": "1945 – 1953 CE",
                "points": [
                    "Yalta and Potsdam Conferences divided Germany and Berlin into Allied and Soviet occupation zones.",
                    "Churchill's 'Iron Curtain' speech (1946); US Truman Doctrine of Containment and Marshall Plan economic aid.",
                    "Formation of opposing military blocs: NATO (1949) vs Warsaw Pact (1955); Berlin Blockade and Airlift (1948–49)."
                ]
            },
            {
                "name": "Decolonisation & Rise of Asia and Africa",
                "range": "1947 – 1965 CE",
                "points": [
                    "Wave of independence: India and Pakistan (1947), Burma and Ceylon (1948), Indonesia (1949), Ghana (1957), Algeria (1962).",
                    "Bandung Asian-African Conference (1955) in Indonesia articulated Third World solidarity against neo-colonialism.",
                    "Founding of the Non-Aligned Movement (NAM) at Belgrade (1961) led by Nehru (India), Tito (Yugoslavia), Nasser (Egypt), Sukarno (Indonesia), and Nkrumah (Ghana)."
                ]
            },
            {
                "name": "Hot Wars of the Cold War & Nuclear Crises",
                "range": "1950 – 1979 CE",
                "points": [
                    "Korean War (1950–1953): North Korea (backed by USSR/China) vs South Korea (backed by UN/US); ended in armistice at 38th parallel.",
                    "Cuban Missile Crisis (October 1962): Closest world came to full-scale nuclear war; Kennedy and Khrushchev negotiated Soviet missile withdrawal from Cuba.",
                    "Vietnam War (1955–1975): US military intervention defeated by Viet Cong and North Vietnam under Ho Chi Minh; reunification of Vietnam.",
                    "Developments in West Asia: Arab-Israeli Wars (1948, 1967 Six-Day War, 1973 Yom Kippur War), 1956 Suez Crisis, and 1979 Iranian Islamic Revolution."
                ]
            },
            {
                "name": "Soviet Stagnation, Gorbachev & Collapse of USSR",
                "range": "1979 – 1991 CE",
                "points": [
                    "Soviet invasion of Afghanistan (1979–1989) drained Soviet military and economic resources.",
                    "Mikhail Gorbachev launched Glasnost (political openness) and Perestroika (economic restructuring).",
                    "Fall of the Berlin Wall (November 1989) and German reunification (1990).",
                    "Dissolution of the Soviet Union (December 1991) into 15 independent republics, ending the bipolar Cold War and ushering in a unipolar US-dominated world."
                ]
            }
        ],
        "aspects": {
            "Political Philosophy 1: Communism": [
                "Philosophical Core: Formulated by Karl Marx and Friedrich Engels. Dialectical and Historical Materialism; class struggle between Bourgeoisie and Proletariat; surplus value extraction; dictatorship of the proletariat leading to a stateless, classless society.",
                "Evolution & Forms: Leninism (vanguard party, democratic centralism), Stalinism (command economy, forced collectivization, industrialization, totalitarian purges), Maoism (peasant-led guerilla revolution).",
                "Social Impact: Abolished hereditary feudal aristocracy, achieved near-universal literacy and healthcare; however, led to severe suppression of civil liberties, forced labor camps (Gulags), economic stagnation, and totalitarian terror."
            ],
            "Political Philosophy 2: Capitalism": [
                "Philosophical Core: Formulated by Adam Smith (The Wealth of Nations 1776). Private property rights, profit incentive, market competition, division of labor, and laissez-faire non-interference.",
                "Evolution & Forms: Merchant Capitalism -> Industrial Capitalism -> Monopoly / Finance Capitalism -> Post-WWII Keynesian Welfare Capitalism -> Neoliberalism (Hayek, Friedman, Reagan, Thatcher).",
                "Social Impact: Unmatched technological innovation, consumer choice, and wealth generation; however, produces sharp wealth inequality, corporate monopolies, labor precarity, economic boom-bust cycles, and environmental crisis."
            ],
            "Political Philosophy 3: Socialism": [
                "Philosophical Core: Rejection of unfettered free-market inequality in favor of collective social ownership or democratic regulation of essential economic means.",
                "Evolution & Forms: Utopian Socialism (Robert Owen, Saint-Simon) -> Fabian Socialism (gradual reformist democracy - Sidney & Beatrice Webb, influencing Nehruvian India) -> Democratic Socialism / Social Democracy (Nordic Model combining high taxation, private enterprise, and comprehensive cradle-to-grave welfare states).",
                "Social Impact: Balanced individual freedom with social justice, providing universal healthcare, public education, labor unions, and social safety nets."
            ]
        },
        "events": [
            {
                "year": "1949 CE",
                "title": "Formation of NATO & Chinese Communist Revolution",
                "desc": "North Atlantic Treaty signed in Washington; Mao Zedong proclaims the People's Republic of China in Beijing.",
                "theme": "polity"
            },
            {
                "year": "1955 CE",
                "title": "Bandung Conference",
                "desc": "29 Asian and African states meet in Indonesia to oppose colonialism and promote economic cooperation.",
                "theme": "foreign"
            },
            {
                "year": "1962 CE",
                "title": "The Cuban Missile Crisis",
                "desc": "13-day nuclear standoff between the US and USSR over Soviet ballistic missiles stationed in Cuba.",
                "theme": "war"
            },
            {
                "year": "1989 CE",
                "title": "Fall of the Berlin Wall",
                "desc": "East German citizens tear down the wall separating East and West Berlin, symbolizing the collapse of Soviet control.",
                "theme": "polity"
            },
            {
                "year": "1991 CE",
                "title": "Dissolution of the Soviet Union",
                "desc": "The USSR is officially dissolved, ending the Cold War and establishing a unipolar geopolitical order.",
                "theme": "polity"
            }
        ],
        "people": [
            {
                "name": "Jawaharlal Nehru",
                "role": "First Prime Minister of India & NAM Co-Founder",
                "note": "Championed Non-Alignment to keep newly independent nations from becoming pawns in superpower Cold War blocs."
            },
            {
                "name": "Mikhail Gorbachev",
                "role": "Last General Secretary of the CPSU",
                "note": "Introduced Glasnost and Perestroika reforms that inadvertently led to the collapse of the Soviet Union."
            },
            {
                "name": "Ho Chi Minh",
                "role": "Vietnamese Communist Revolutionary Leader",
                "note": "Led North Vietnam through anti-colonial resistance against France and the United States, achieving national reunification."
            }
        ],
        "themes": ["polity", "war", "foreign", "economy", "society"],
        "upsc": {
            "prelims": [
                "NAM was officially established at the 1st Belgrade Summit (1961) based on the 10 principles of the 1955 Bandung Conference.",
                "The 38th parallel divides North and South Korea following the 1953 armistice.",
                "Glasnost signified political openness/transparency, whereas Perestroika referred to economic restructuring in the USSR."
            ],
            "mains": [
                "'Non-Alignment was not a policy of neutrality or opportunism, but a positive assertion of national sovereignty.' Analyze in the context of India's Cold War foreign policy.",
                "Compare and contrast the political philosophies of Communism, Capitalism, and Democratic Socialism with respect to their social outcomes in the 20th century."
            ]
        },
        "quickFacts": [
            ["Era", "1945 – 1991 CE"],
            ["Opposing Blocs", "NATO (US-led) vs Warsaw Pact (USSR-led)"],
            ["Third World Response", "Non-Aligned Movement (NAM Belgrade 1961)"],
            ["Climax Crises", "Cuban Missile Crisis (1962), Vietnam War (1955-75), Afghanistan (1979-89)"],
            ["End Event", "Dissolution of the USSR (December 1991)"]
        ]
    }
]

# Insert missing periods
added = 0
for np in new_periods:
    if np['id'] not in existing_ids:
        history['periods'].append(np)
        existing_ids.add(np['id'])
        added += 1
        print(f"Added period: {np['id']} - {np['title']}")
    else:
        print(f"Already exists: {np['id']}")

# Re-sort periods: national first by chronological sequence, then UP periods
def period_sort_key(p):
    is_up = 1 if p.get('region') == 'up' else 0
    # Custom chronological order for national periods
    order_map = {
        'prehistoric-age': 1,
        'indus-valley-civilization': 2,
        'vedic-age': 3,
        'age-of-mahajanapadas': 4,
        'mauryan-empire': 5,
        'ashoka-the-great': 6,
        'post-mauryan-period': 7,
        'gupta-age': 8,
        'post-gupta-age': 9,
        'early-medieval-period': 10,
        'kingdoms-of-north': 11,
        'kingdoms-of-south': 12,
        'delhi-sultanate': 13,
        'mamluk-dynasty': 14,
        'khilji-dynasty': 15,
        'tughlaq-dynasty': 16,
        'sayyid-dynasty': 17,
        'lodi-dynasty': 18,
        'vijayanagara-empire': 19,
        'deccan-sultanate': 20,
        'mughal-empire': 21,
        'babur': 22,
        'humayun': 23,
        'sur-interregnum': 24,
        'akbar-the-great': 25,
        'jahangir': 26,
        'shah-jahan': 27,
        'aurangzeb': 28,
        'maratha-empire': 29,
        'later-mughal-empire': 30,
        'establishment-of-british-power': 31,
        'sikh-empire': 32,
        'british-colonial-rule': 33,
        'british-administration': 34,
        'governors-general-and-viceroys': 35,
        'tribal-movements-colonial-india': 36,
        'socio-religious-reforms': 37,
        'foundation-of-indian-national-congress': 38,
        'indian-freedom-struggle': 39,
        'mahatma-gandhi': 40,
        'independence-of-india': 41,
        'independent-india-overview': 42,
        'india-1947-1964': 43,
        'india-1965-1980': 44,
        'india-1981-1991': 45,
        'india-1992-2000': 46,
        'india-2001-2010': 47,
        'india-2011-2020': 48,
        'india-2020-present': 49,
        'world-history-context': 50,
        'industrial-revolution-and-capitalism': 51,
        'american-revolution-and-civil-war': 52,
        'french-revolution': 53,
        'world-war-1': 54,
        'russian-revolution': 55,
        'world-war-2': 56,
        'cold-war-and-decolonisation': 57
    }
    if is_up:
        return (1, p.get('order', 999))
    return (0, order_map.get(p['id'], p.get('order', 999)))

history['periods'].sort(key=period_sort_key)

# Re-assign sequential order 1..N
for i, p in enumerate(history['periods']):
    p['order'] = i + 1

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(history, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully updated history.json! Total periods now: {len(history['periods'])}")
