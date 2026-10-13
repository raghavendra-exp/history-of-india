import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Enrichment mapping for UP Specific (GS 5 & 6) and 3 remaining National periods
UP_AND_REMAINING_ENRICHMENTS = {
    'world-history-context': {
        'upsc': {
            'prelims': [
                'The doctrine of "Separation of Powers" among the executive, legislative, and judicial branches was propounded by French philosopher Montesquieu in The Spirit of the Laws.',
                'Jean-Jacques Rousseau enunciated the theory of "Popular Sovereignty" and the "General Will" in his landmark work The Social Contract (1762).',
                'John Locke\'s concept of "Natural Rights" (Life, Liberty, and Property) directly inspired Thomas Jefferson in drafting the American Declaration of Independence.',
                'The movable-type printing press was invented in Europe by Johannes Gutenberg in Mainz, Germany around 1440 CE, catalyzing the Protestant Reformation.',
                'Nicolaus Copernicus proposed the Heliocentric model (sun at the centre of the solar system) in his 1543 work De revolutionibus orbium coelestium.',
                'The Renaissance originated in the city-states of Northern Italy (Florence, Venice, Genoa) in the 14th century, championed by the Medici family.'
            ],
            'mains': [
                'Trace the influence of Enlightenment political philosophy (Locke, Montesquieu, Rousseau) on the constitutional frameworks of modern democratic republics.',
                'Analyze the transition from medieval feudalism to modern commercial capitalism in Europe, evaluating the roles of the Scientific Revolution and maritime trade.',
                'Examine the historical continuum from the 18th-century Atlantic Revolutions through 19th-century colonial imperialism to 20th-century globalization, highlighting the shifting centres of global economic power.'
            ]
        }
    },
    'early-medieval-india-750-1200': {
        'upsc': {
            'prelims': [
                'The Tripartite Struggle for Kannauj was waged between the Gurjara-Pratiharas, Palas, and Rashtrakutas for mastery over the fertile Ganga-Yamuna Doab.',
                'Dharmapala founded Vikramashila University and restored Nalanda University, granting 200 villages for its maintenance.',
                'The monolithic rock-cut Kailasanatha Temple at Ellora (Cave 16) was excavated by Rashtrakuta king Krishna I in the 8th century CE.',
                'The Chola local self-government system was regulated by the Uttaramerur Inscriptions of Parantaka I (919 and 921 CE).',
                'Arab traveler Al-Masudi visited India during the reign of Pratihara king Mahipala I and praised the power and cavalry of the empire.'
            ],
            'mains': [
                'Critically evaluate the "Indian Feudalism" debate formulated by R.S. Sharma against the "Lineage Integration Model" proposed by B.D. Chattopadhyaya.',
                'Analyze the geopolitical causes and consequences of the Tripartite Struggle among the Gurjara-Pratiharas, Palas, and Rashtrakutas for control of Kannauj.',
                'Examine the growth of regional identities, languages, and vernacular literatures in early medieval India between 750 and 1200 CE, assessing how regional states fostered distinct cultural traditions.'
            ]
        }
    },
    'eighteenth-century-transition-and-regional-states': {
        'upsc': {
            'prelims': [
                'Murshid Quli Khan was appointed Diwan of Bengal in 1700 and Governor in 1717, transferring the capital from Dacca to Murshidabad.',
                'Saadat Khan Burhan-ul-Mulk founded the autonomous principality of Awadh in 1722, succeeded by Safdarjung.',
                'Chin Qilich Khan (Nizam-ul-Mulk Asaf Jah) established the independent state of Hyderabad in 1724 following the Battle of Shakar Kheda.',
                'Hyder Ali established a modern arms arsenal at Dindigul with the assistance of French experts in 1755.',
                'Nadir Shah invaded Delhi in 1739 during the reign of Muhammad Shah Rangeela, carrying away the Peacock Throne and the Koh-i-Noor diamond.'
            ],
            'mains': [
                'Analyze the 18th-century debate in Indian historiography: was this era a "Dark Age" of political collapse and economic ruin, or a period of regional state formation and dynamic commercial growth?',
                'Examine the internal structure and agrarian policies of the regional successor states of Bengal, Awadh, and Hyderabad in the 18th century.',
                'Critically assess the "Dark Age" hypothesis versus the "Regional Prosperity" revisionist model of 18th-century Indian history, analyzing the economic vitality of Bengal, Awadh, and Mysore prior to British annexation.'
            ]
        }
    },
    'up-history-overview': {
        'aspects': {
            'Chronological Horizons of Uttar Pradesh': [
                'Deep Time & Prehistoric Archaeology: Belan Valley (Prayagraj) yielding Lower Palaeolithic to Neolithic stratigraphic sequences; Lahuradewa (Sant Kabir Nagar) yielding the earliest domesticated rice in South Asia (c. 7000–6000 BCE); Chopani Mando wild-to-settled transition; Sarai Nahar Rai, Damdama, and Mahadaha (Pratapgarh) showing Mesolithic microlithic cemeteries and bone ornaments.',
                'Vedic & Mahajanapada Era: Heartland of Later Vedic Kuru-Panchala culture; 8 of the 16 Mahajanapadas flourished in UP: Kuru, Panchala, Shurasena, Vatsa, Kosala, Malla, Chedi, and Kashi.',
                'Classical to Medieval Empires: Sarnath (Ashoka\'s Lion Capital, First Sermon); Mathura (Kushana second capital, Mathura school of red sandstone sculpture); Gupta masterpieces at Deogarh (Dashavatara temple) and Bhitargaon (brick temple); Kannauj under Harshavardhana, Pratiharas, and Gahadavalas; Jaunpur Sharqi Sultanate ("Shiraz of the East"); Mughal Agra and Fatehpur Sikri; Awadh Nawabi culture in Lucknow.',
                'Colonial Resistance & Modern Formation: Epicenter of the Revolt of 1857 (Mangal Pandey, Meerut, Lucknow, Kanpur, Jhansi, Bareilly, Allahabad); cradle of the mass freedom struggle (Chauri Chaura, Swaraj Party, Kakori Action, Azad martyrdom, Ballia parallel government); official evolution from North-Western Provinces (1836) to United Provinces of Agra & Oudh (1902) to Uttar Pradesh (24 January 1950).'
            ]
        },
        'upsc': {
            'prelims': [
                'Uttar Pradesh officially received its current name on 24 January 1950; 24 January is celebrated annually as "UP Diwas" (Uttar Pradesh Day).',
                'Eight of the sixteen ancient Mahajanapadas were located entirely or predominantly within the modern boundaries of Uttar Pradesh.',
                'Lahuradewa in Sant Kabir Nagar district of UP has yielded the oldest archaeological evidence of domesticated rice in South Asia, dating to c. 7000–6000 BCE.',
                'The National Emblem of India is adopted from the Lion Capital of Ashoka excavated at Sarnath near Varanasi.',
                'The Dashavatara Temple at Deogarh (Lalitpur district, UP) is the earliest surviving structural temple in India built on a complete Panchayatana layout.',
                'The First Spark of the 1857 Revolt erupted on 10 May 1857 at Meerut, initiated by sepoys of the 3rd Native Cavalry.',
                'Ballia was the first district in India to establish a parallel government (Prati Sarkar) during the Quit India Movement in August 1942 under Chittu Pandey.'
            ],
            'mains': [
                'Trace the historical evolution of Uttar Pradesh from the prehistoric settlements of the Belan Valley to the formation of the modern state in 1950.',
                'Evaluate the role of the Ganga-Yamuna Doab in shaping the political, agrarian, and urban history of Northern India from the ancient Mahajanapadas to the Mughal era.',
                'Discuss the contributions of Uttar Pradesh to India\'s national freedom struggle, highlighting the key revolutionary actions, mass movements, and peasant uprisings.'
            ]
        }
    },
    'up-prehistoric': {
        'aspects': {
            'Belan Valley & Gangetic Mesolithic Sites': [
                'Belan Valley Stratigraphy: Located in Prayagraj and Mirzapur districts; excavated by Prof. G.R. Sharma (University of Allahabad); rare site in South Asia revealing continuous stratigraphic sequence from Lower Palaeolithic through Middle and Upper Palaeolithic to Mesolithic and Neolithic; Lopamudra / Belan gravel beds yielded Acheulian handaxes, cleavers, and a famous Upper Palaeolithic carved bone female figurine (Mother Goddess) from Lohanda Nala.',
                'Sarai Nahar Rai (Pratapgarh): Earliest Mesolithic settlement in the Ganga plains (c. 8400 BCE); revealed 14 human burials (extended inhumation oriented west-east) with microlith grave goods and bone ornaments; earliest evidence of violent human conflict (skeleton with a stone microlith embedded in a lumbar vertebra).',
                'Mahadaha & Damdama (Pratapgarh): Damdama revealed 41 human burials, including double burials (joint male-female burials) and a unique triple burial; circular and oblong pit hearths; abundant animal bones (wild cattle, deer, pig, turtle, birds); bone arrowheads, points, and rings.'
            ],
            'Chopani Mando & Lahuradewa': [
                'Chopani Mando (Belan Valley): Shows transition from wild hunter-gatherer existence to semi-sedentary life; beehive-shaped huts with reed-plastered floors; earliest crude handmade cord-impressed pottery in North India.',
                'Lahuradewa (Sant Kabir Nagar): Breakthrough excavation by UP State Archaeology Department (Rakesh Tewari); yielded carbonized domesticated rice (Oryza sativa) grains and ceramic sherds dating back to c. 7000–6000 BCE, pushing back the origin of Asian rice farming by millennia.'
            ]
        },
        'upsc': {
            'prelims': [
                'The bone figurine of a Mother Goddess dating to the Upper Palaeolithic period was excavated from Lohanda Nala in the Belan Valley (Prayagraj).',
                'The earliest human skeletal remains and extended burials in the Gangetic plain were excavated at Sarai Nahar Rai, Mahadaha, and Damdama in Pratapgarh district, UP.',
                'Damdama (Pratapgarh) has yielded evidence of 41 human burials, including joint burials and a rare triple burial, alongside bone ornaments and microliths.',
                'Lahuradewa in Sant Kabir Nagar (UP) has yielded radiocarbon dates of c. 7000–6000 BCE for domesticated rice, revolutionizing ancient agricultural chronologies.',
                'Chopani Mando in the Belan Valley exhibits a continuous three-phase transition from food gathering to early pottery and circular hut settlements.',
                'The prehistoric rock art sites of Uttar Pradesh are concentrated in the Vindhyan sandstone caves of Mirzapur, Sonbhadra, and Prayagraj districts.',
                'Robert Bruce Foote and subsequent archaeologists confirmed that the Belan Valley holds a continuous stratified record from the Lower Palaeolithic to the Neolithic.'
            ],
            'mains': [
                'Critically examine the archaeological significance of the Belan Valley excavations in establishing the prehistoric cultural sequence of Northern India.',
                'Analyze the Mesolithic burial practices, skeletal morphology, and tool industries of Sarai Nahar Rai, Mahadaha, and Damdama in Uttar Pradesh.',
                'Evaluate the impact of the Lahuradewa excavations on the global understanding of the origin and antiquity of rice domestication in South Asia.'
            ]
        }
    },
    'up-vedic-age': {
        'aspects': {
            'Kuru-Panchala Cultural Heartland': [
                'Geographical epicentre: Western and Central Uttar Pradesh formed the core heartland of the Later Vedic civilization; Kuru realm spanned Meerut, Delhi, and Thaneshwar (capital: Asandivat, later Hastinapur); Panchala realm encompassed Bareilly, Badaun, and Farrukhabad (capitals: Ahichchhatra in Bareilly and Kampilya in Farrukhabad).',
                'Painted Grey Ware (PGW) Horizon: Archaeological excavations by B.B. Lal at Hastinapur, Atranjikhera (Etah), Alamgirpur (Meerut), and Jakhera (Kasganj) confirmed that PGW culture corresponds directly to the Later Vedic horizon; Jakhera yielded iron plowshares and early urban fortifications; flood layer at Hastinapur confirmed Puranic tradition of shifting the capital to Kaushambi.',
                'Philosophical debates in UP: King Pravahana Jaivali of Panchala hosted assemblies of Vedic scholars; royal court of King Janaka of Videha attracted scholars like sage Yajnavalkya, Gargi Vachaknavi, and Maitreyi.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Painted Grey Ware (PGW) culture, associated with the Later Vedic period, was prominently excavated at Hastinapur and Atranjikhera in Uttar Pradesh.',
                'Atranjikhera in Etah district (UP) has provided the earliest extensive evidence of regular iron tool usage (Krishna Ayas) in agriculture dating to c. 1000 BCE.',
                'The capital of the northern Panchala kingdom was Ahichchhatra (Ramnagar, Bareilly), while the southern capital was Kampilya (Farrukhabad).',
                'Excavations at Hastinapur conducted by Prof. B.B. Lal confirmed a massive flood layer in the Ganga, supporting Puranic records of capital relocation to Kaushambi.',
                'King Pravahana Jaivali, a prominent philosopher-king celebrated in the Chandogya Upanishad, ruled over the Panchala realm in Uttar Pradesh.',
                'Jakhera in Kasganj district (UP) yielded early iron sickles, hoes, and agricultural implements reflecting the transition to settled agrarian life.',
                'The sacred confluence (Sangam) of Ganga, Yamuna, and mythical Saraswati at Prayagraj was already venerated in Later Vedic literature.'
            ],
            'mains': [
                'Discuss the archaeological and literary evidence correlating the Painted Grey Ware (PGW) culture with the Later Vedic settlements in the Ganga-Yamuna Doab of Uttar Pradesh.',
                'Examine the political and cultural pre-eminence of the Kuru and Panchala kingdoms during the Later Vedic transformation.',
                'Analyze the role of iron technology (excavations at Atranjikhera and Jakhera) in facilitating agricultural clearing and urbanization in ancient Uttar Pradesh.'
            ]
        }
    },
    'up-mahajanapadas': {
        'aspects': {
            'Eight Mahajanapadas of Uttar Pradesh': [
                '1. Kuru: Western UP (Meerut, Hastinapur, Ghaziabad; capitals: Indraprastha / Hastinapur; later adopted republican constitution).',
                '2. Panchala: Rohilkhand and Central UP (Bareilly, Badaun, Farrukhabad; northern capital Ahichchhatra, southern capital Kampilya; famed for textile production).',
                '3. Shurasena: Braj region (Mathura on the Yamuna; capital Mathura; ruled by Yadava dynasty; Krishna associated with Shurasena; centre of Krishna / Bhagavata cult).',
                '4. Vatsa: Central Doab (Prayagraj, Kaushambi; capital Kaushambi on Yamuna; King Udayana was a contemporary of Buddha; central junction of Uttarapatha and Dakshinapatha trade routes).',
                '5. Kosala: Awadh region (Faizabad, Ayodhya, Shravasti; capital Shravasti / Sahet-Mahet on Rapti river; King Prasenjit was contemporary of Buddha; Buddha spent 25 rainy seasons / Vassa at Jetavana monastery in Shravasti).',
                '6. Malla: Eastern UP (Deoria, Gorakhpur, Kushinagar; republican Gana-Sangha; two branches: Kusinara / Kasia where Buddha attained Mahaparinirvana, and Pava where Mahavira attained Nirvana).',
                '7. Chedi: Bundelkhand region (Banda, Lalitpur, Ken river; capital Shuktimati / Sotthivati; King Shishupala).',
                '8. Kashi: Eastern UP (Varanasi; capital Varanasi between Varuna and Assi rivers; famed for cotton textiles, ivory crafts, and religious learning; annexed by Kosala and later Magadha).'
            ]
        },
        'upsc': {
            'prelims': [
                'Eight of the 16 ancient Mahajanapadas were situated in Uttar Pradesh: Kuru, Panchala, Shurasena, Vatsa, Kosala, Malla, Chedi, and Kashi.',
                'The capital of the Vatsa Mahajanapada was Kaushambi, situated on the Yamuna river near modern Prayagraj, ruled by King Udayana.',
                'Gautama Buddha spent the maximum number of rainy seasons (25 Varshavasas) at the Jetavana monastery in Shravasti (capital of Kosala).',
                'The capital of Shurasena was Mathura, located at the junction of Uttarapatha and Dakshinapatha, associated with the Yadava clan and Lord Krishna.',
                'Gautama Buddha attained Mahaparinirvana at Kusinara (Kushinagar), which was the capital of the Malla republican Mahajanapada in Eastern UP.',
                'Vardhamana Mahavira attained Nirvana at Pava, which was the second major centre of the Malla Mahajanapada in UP.',
                'The ancient city of Kaushambi features a massive fortified mud-brick rampart with burnt-brick revetment and the celebrated Ghoshitarama monastery.'
            ],
            'mains': [
                'Examine the geographical distribution and political characteristics of the eight Mahajanapadas located within Uttar Pradesh.',
                'Analyze the religious and historical significance of Uttar Pradesh in early Buddhism and Jainism with special reference to Sarnath, Shravasti, Kushinagar, and Pava.',
                'Discuss the urban and commercial prominence of Kaushambi and Mathura as nodal centres on the trans-subcontinental trade routes (Uttarapatha and Dakshinapatha).'
            ]
        }
    },
    'up-maurya-period': {
        'aspects': {
            'Ashokan Epigraphy & Architecture in UP': [
                'Lion Capital of Sarnath: Carved from polished Chunar sandstone; features four Asiatic lions back-to-back, an abacus with high-relief sculptures of an elephant, horse, bull, and lion separated by Dharmachakra wheels, resting on an inverted bell lotus; adopted as the National Emblem of India on 26 January 1950; Wheel of Law adopted on the National Flag.',
                'Ashokan Pillar Edicts in UP: 1. Prayagraj / Allahabad Pillar (inscribed with 6 Major Pillar Edicts of Ashoka, Queen\'s Edict regarding Karuvaki, and the Schism Edict warning monks; later inscribed with Samudragupta\'s Prayag Prashasti and Jahangir\'s genealogy), 2. Meerut Pillar (transported by Firuz Shah Tughlaq to Delhi Ridge in the 14th century), 3. Topra Pillar (transported from Haryana to Feroz Shah Kotla, Delhi), 4. Kaushambi Pillar.',
                'Buddhist Monasteries & Stupas: Dharmarajika Stupa and Dhamek Stupa at Sarnath commissioned by Ashoka; ancient brick monastic complexes at Shravasti (Jetavana) and Sankissa (Farrukhabad, where Buddha legendarily descended from heaven on a jeweled ladder; Ashokan elephant capital).'
            ]
        },
        'upsc': {
            'prelims': [
                'The Sarnath Lion Capital, sculpted from Chunar sandstone under Ashoka, was officially adopted as the National Emblem of India on 26 January 1950.',
                'The Allahabad / Prayagraj Pillar bears inscriptions of three distinct emperors: Ashoka (Pillar Edicts, Queen\'s Edict), Samudragupta (Prayag Prashasti), and Jahangir.',
                'The Queen\'s Edict on the Allahabad Pillar is the only Ashokan inscription that names a queen (Karuvaki, mother of Prince Tivara).',
                'Ashoka built the Dharmarajika Stupa at Sarnath to enshrine the sacred relics of Gautama Buddha.',
                'Sankissa in Farrukhabad district (UP) is celebrated in Buddhist tradition as the site of Buddha\'s descent from Trayastrimsa Heaven, marked by an Ashokan elephant capital.',
                'The Meerut Ashokan Pillar was transported and re-erected on the Delhi Ridge by Sultan Firuz Shah Tughlaq in the 14th century.',
                'The Schism Edict warning Buddhist monks against causing divisions in the Sangha is found on pillars at Sarnath and Kaushambi.'
            ],
            'mains': [
                'Critically evaluate the artistic, technological, and ideological features of the Mauryan sculptures and pillars in Uttar Pradesh, with specific reference to the Sarnath Lion Capital.',
                'Analyze the epigraphical significance of the Allahabad / Prayagraj Pillar Inscription as a multi-layered historical record spanning Ashoka, the Guptas, and the Mughals.',
                'Examine the spread of Buddhist monastic architecture under Mauryan patronage at Sarnath, Shravasti, and Sankissa.'
            ]
        }
    },
    'up-post-maurya-period': {
        'aspects': {
            'Kushanas at Mathura & Shunga Ayodhya': [
                'Mathura as Kushana Southern Capital: Mathura functioned as the premier political, administrative, and artistic metropolis of the Kushana Empire in India under Kanishka I, Huvishka, and Vasudeva; imperial portrait shrine (Devakula) excavated at Mat near Mathura, yielding the colossal headless standing statue of Kanishka I wearing a heavy nomadic coat and boots, holding a mace and sword, with the inscription "Maharaja Rajadhiraja Devaputra Kanishka".',
                'Mathura School of Sculpture: Flourished from 1st century BCE to 4th century CE; material: distinctive local mottled / spotted red sandstone from Karri/Sikri quarries; sculpted the earliest indigenous anthropomorphic images of Gautama Buddha (seated Katra Buddha under Bodhi tree with snail-shell curls, smiling countenance, and Abhayaprada gesture), 24 Jain Tirthankaras (Kankali Tila stupa and Ayagapattas votive slabs), and Hindu deities (four-armed Vishnu, Shiva-lingams, Kartikeya, Mahishasuramardini).',
                'Ayodhya Inscription of Dhanadeva: Inscribed stone slab found at Ayodhya recording that King Dhanadeva, the 6th descendant of Senapati Pushyamitra Shunga, performed two Ashvamedha sacrifices, establishing Shunga royal lineage and revival of Vedic rituals in UP.'
            ]
        },
        'upsc': {
            'prelims': [
                'Mathura served as the second imperial capital and primary commercial hub of the Kushana Empire in Northern India.',
                'The famous headless statue of Emperor Kanishka I wearing Central Asian boots and tunic was excavated from the royal portrait shrine (Devakula) at Mat near Mathura.',
                'The Mathura School of Art exclusively used mottled / spotted red sandstone quarried from nearby Sikri and Fatehpur.',
                'The earliest indigenous anthropomorphic images of the Buddha and Jain Tirthankaras in Indian art were crafted by the Mathura School of Sculpture.',
                'The Ayodhya Stone Inscription of King Dhanadeva confirms that Pushyamitra Shunga performed two Ashvamedha sacrifices.',
                'Kankali Tila in Mathura is a world-famous archaeological site renowned for the excavation of an ancient Jain stupa and beautifully carved Ayagapattas (votive tablets).',
                'The Greek ambassador Heliodorus visited Vidisha from Taxila, but Indo-Greek coins of Menander have been found in extensive hoards at Mathura and Rohilkhand.'
            ],
            'mains': [
                'Analyze the stylistic, iconographical, and material characteristics of the Mathura School of Art during the Kushana period, comparing it with the Gandhara School.',
                'Examine the political and commercial importance of Mathura as the Kushana imperial capital and meeting point of major trans-Indian trade routes.',
                'Discuss the significance of the Ayodhya Inscription of Dhanadeva in reconstructing the post-Mauryan Shunga history and religious revival in Uttar Pradesh.'
            ]
        }
    },
    'up-gupta-period': {
        'aspects': {
            'Gupta Architectural Zenith in UP': [
                'Dashavatara Temple at Deogarh (Lalitpur district): Consecrated c. 500 CE; earliest surviving Hindu temple built on a complete Panchayatana layout (central sanctum surrounded by four subsidiary corner shrines); soaring pyramidal shikhara (early Nagara style); monumental sculpted relief panels: Sheshashayi Vishnu (Vishnu reclining on cosmic serpent Ananta, surrounded by Lakshmi, Garuda, and the Pandavas), Gajendramoksha, and Nara-Narayana meditation; river goddesses Ganga (on Makara) and Yamuna (on Kurma tortoise) adorning sanctum doorjambs.',
                'Bhitargaon Brick Temple (Kanpur district): Earliest and largest surviving classical Hindu temple built entirely of terracotta and kiln-fired bricks; dating to the 5th century CE; prominent curvilinear shikhara rising over 70 feet; historic use of the "true arch" (semi-circular voussoir arch) centuries before Islamic architecture in India; adorned with terracotta panels of Shiva, Parvati, Ganesha, and Ramayana episodes.',
                'Sarnath Seated Buddha & Prayag Prashasti: Sarnath School achieved the classical apex of Buddhist art: the world-famous Sarnath Seated Buddha in Dharmachakrapravartana Mudra (carved in Chunar sandstone with transparent drapery, serene downcast eyes, and a lavishly carved halo featuring celestial gandharvas); Allahabad Pillar preserved Harishena\'s Prayag Prashasti detailing Samudragupta\'s conquests.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Dashavatara Temple at Deogarh (Lalitpur district, UP) is the earliest known temple featuring a complete Panchayatana plan and early Nagara shikhara.',
                'The monumental Sheshashayi Vishnu panel, depicting Vishnu reclining on the coils of serpent Sheshanaga, is sculpted on the wall of the Deogarh Temple.',
                'The Bhitargaon Temple in Kanpur district is the oldest surviving brick temple in India featuring a shikhara and true arch construction.',
                'The iconic Sarnath Seated Buddha image preaching the First Sermon in Dharmachakrapravartana Mudra is a masterwork of the 5th-century Gupta classical style.',
                'The Prayag Prashasti (composed by Harishena on the Allahabad Pillar) details Samudragupta\'s four-fold military strategy across Aryavarta and Dakshinapatha.',
                'The Bhitari Pillar Inscription in Ghazipur district (UP) records the heroic defense of the Gupta Empire against the invading White Hunas by Skandagupta.',
                'Eran inscription (MP) records the first dated evidence of Sati (510 CE), while Bhitari and Mankuwar inscriptions document Gupta royal land grants in UP.'
            ],
            'mains': [
                'Critically evaluate the architectural evolution of North Indian temples during the Gupta period with specific reference to the Deogarh Dashavatara Temple and Bhitargaon Brick Temple in Uttar Pradesh.',
                'Analyze the aesthetic and spiritual qualities of the Gupta sculpture school of Sarnath, contrasting it with the earlier Mathura School.',
                'Examine the historical and geographical significance of the Bhitari Pillar Inscription of Skandagupta in Ghazipur in documenting the Huna invasion.'
            ]
        }
    },
    'up-harsha-period': {
        'aspects': {
            'Kannauj as Imperial Capital & Assemblies': [
                'Rise of Kannauj (Mahodaya / Kanyakubja): Harsha shifted his capital from Thaneshwar to Kannauj in 606 CE following the death of Grahavarman Maukhari; Kannauj replaced Pataliputra as the premier political and imperial metropolis of Northern India, remaining the imperial prize for five centuries.',
                'Kannauj Assembly (643 CE): Grand multi-faith assembly convened by Harsha to honor Chinese pilgrim Xuanzang and demonstrate the supremacy of Mahayana Buddhism; attended by 20 tributary kings (including Bhaskaravarman of Kamarupa), 3,000 Buddhist monks, 3,000 Jains and orthodox Brahmanas; orthodox conspiracy: disgruntled Brahmanas set fire to the 100-foot temporary pavilion and attempted to assassinate Harsha; conspirators banished.',
                'Prayag Mahamokshaparishad (643 CE): Quinquennial assembly convened at the holy confluence of Ganga and Yamuna at Prayagraj; 75-day festival attended by 500,000 people; Harsha worshipped Buddha on the first day, Sun god on the second, and Shiva on the third; distributed all accumulated royal treasury riches, jewels, cloth, and even his personal royal robes in charity, begging a worn garment from his sister Rajyashri.'
            ]
        },
        'upsc': {
            'prelims': [
                'Harshavardhana transferred the imperial capital of his empire from Thaneshwar (Haryana) to Kannauj (Uttar Pradesh) in 606 CE.',
                'Harsha convened the famous religious assembly at Kannauj in 643 CE to honor the Chinese Buddhist scholar Xuanzang.',
                'The grand quinquennial charity festival known as the "Mahamokshaparishad" was convened by Harsha at the holy confluence in Prayag (Prayagraj).',
                'Banabhatta, the court poet of Harsha, was born near the banks of the Son river and composed the biographical classic Harshacharita and Kadambari.',
                'Xuanzang described Kannauj as a strongly fortified, prosperous city with over 100 Buddhist monasteries, 200 Hindu temples, and lavish gardens.',
                'Harsha\'s defeat on the Narmada river by Chalukya king Pulakeshin II is recorded in the Aihole Inscription authored by Ravikirti.',
                'Harsha authored three classical Sanskrit dramas: Ratnavali, Priyadarsika, and Nagananda.'
            ],
            'mains': [
                'Discuss the geopolitical and economic reasons for the emergence of Kannauj as the premier political capital of Northern India during the reign of Harshavardhana.',
                'Analyze the accounts of Chinese pilgrim Xuanzang regarding the religious assemblies of Kannauj and Prayag, evaluating Harsha\'s secular policy.',
                'Examine the political and cultural contributions of the Maukhari dynasty of Kannauj prior to its unification with Harsha\'s empire.'
            ]
        }
    },
    'up-gurjara-pratiharas': {
        'aspects': {
            'Pratihara Hegemony over Kannauj': [
                'Imperial consolidation: Nagabhata II captured Kannauj and made it the permanent imperial capital of the Gurjara-Pratiharas around 815 CE; celebrated as the bulwark of India for repelling early Arab invasions from Sindh.',
                'Mihira Bhoja (r. 836–885 CE): Most illustrious Pratihara emperor; consolidated an empire stretching from the foothills of the Himalayas to the Narmada and from Bengal to Gujarat; assumed the titles "Adivaraha" and "Prabhas"; struck silver and copper coins bearing the boar incarnation of Vishnu; patron of learning; praised by Arab traveler Sulaiman as possessing the finest cavalry in India.',
                'Culture & Rajasekhara: Mahendrapala I and Mahipala I patronized the great Sanskrit poet-playwright Rajasekhara, author of Kavyamimamsa, Karpuramanjari (written entirely in Sauraseni Prakrit), Balaramayana, and Viddhasalabhanjika; Arab geographer Al-Masudi visited Kannauj in 915 CE, calling the king "Baura" and describing his four vast armies guarding the four cardinal directions.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Gurjara-Pratihara emperor Mihira Bhoja assumed the title "Adivaraha" and minted silver coins depicting the Boar incarnation of Vishnu.',
                'Nagabhata II made Kannauj the permanent imperial capital of the Gurjara-Pratihara dynasty in the early 9th century CE.',
                'The celebrated Sanskrit poet and dramatist Rajasekhara was the court poet and guru of Pratihara king Mahendrapala I.',
                'Rajasekhara composed Karpuramanjari, the only classical Sanskrit drama written entirely in Sauraseni Prakrit.',
                'Arab traveler Al-Masudi visited Kannauj in 915 CE during the reign of Pratihara king Mahipala I, describing the kingdom as "al-Juzr" and the king as "Baura".',
                'Arab chronicler Sulaiman (851 CE) praised Mihira Bhoja as the greatest enemy of Islam possessing India\'s most formidable cavalry.',
                'Mahmud of Ghazni invaded and sacked Kannauj in 1018 CE, defeating the last major Pratihara ruler Rajyapala.'
            ],
            'mains': [
                'Analyze the political and military role of the Gurjara-Pratiharas of Kannauj as the "defenders of the northwestern frontiers" against early Arab invasions.',
                'Evaluate the reign and cultural achievements of Mihira Bhoja and Mahendrapala I, with specific reference to Rajasekhara\'s literary works.',
                'Discuss the decline of the Gurjara-Pratihara empire and explain how its collapse led to the rise of regional Rajput polities in Northern India.'
            ]
        }
    },
    'up-kalachuris-chandellas': {
        'aspects': {
            'Chandellas of Bundelkhand & Bundeli Valour': [
                'Chandellas of Jejakabhukti: Founded by Nannuka (9th cent); broke free from Pratihara suzerainty under Harsha and Yashovarman (built the Lakshmana Temple at Khajuraho); King Dhanga (built the Vishvanatha and Parshvanatha temples; shifted political capital to Mahoba while retaining Khajuraho as the sacred temple city); King Vidyadhara (1019–1022 CE; heroically resisted Mahmud of Ghazni twice at the impregnable Kalinjar Fort; built the soaring Kandariya Mahadeva Temple).',
                'Kalinjar & Mahoba Fortresses: Impregnable military strongholds in Bundelkhand; Kalinjar withstood sieges by Mahmud of Ghazni, Qutbuddin Aibak, and later Sher Shah Suri (who died there in 1545).',
                'Alha-Udal & Parmal: Reign of King Paramardideva (Parmal, r. 1165–1203 CE); defended Mahoba against Prithviraj Chauhan (1182 CE); celebrated in the heroic Bundeli folk ballad Alha-Khand (composed by court bard Jagnik), recounting the 52 epic battles of legendary warrior brothers Alha and Udal; Qutbuddin Aibak captured Kalinjar in 1203 CE.',
                'Kalachuris of Dahala & Sarayupara: Kalachuri branch of Gorakhpur (Sarayupara) and Tripuri; King Gangeyadeva (assumed title Vikramaditya, struck Lakshmi-type gold coins widely imitated across North India) and Lakshmi-Karna.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Chandella dynasty of Bundelkhand was anciently known as the rulers of "Jejakabhukti" (named after prince Jeja/Jayasakti).',
                'The world-famous temples of Khajuraho were built between 950 and 1050 CE under the patronage of Chandella kings, notably Dhanga and Vidyadhara.',
                'Chandella King Vidyadhara successfully resisted the invasions of Mahmud of Ghazni at the formidable Kalinjar Fort in 1019 and 1022 CE.',
                'The folk ballad Alha-Khand, celebrating the martial exploits of warrior brothers Alha and Udal of Mahoba, was composed by court poet Jagnik.',
                'Kalinjar Fort in Banda district of UP is one of the oldest and most impregnable hill fortresses of India, where Sher Shah Suri died in 1545.',
                'The Kalachuri king Gangeyadeva issued gold coins bearing the seated image of Goddess Lakshmi, which became the standard coin type across Northern India.',
                'Qutbuddin Aibak invaded Bundelkhand and captured Kalinjar Fort from Chandella king Paramardideva in 1203 CE.'
            ],
            'mains': [
                'Trace the rise and political history of the Chandellas of Bundelkhand, analyzing their military resistance against Turkish invaders at Kalinjar.',
                'Examine the folk and cultural significance of the Alha-Udal ballad tradition in the regional identity of Bundelkhand in Uttar Pradesh.',
                'Analyze the architectural brilliance of the Khajuraho group of temples, focusing on temple layout, shikhara design, and sculptural iconography.'
            ]
        }
    },
    'up-gahadavalas': {
        'aspects': {
            'Gahadavala Hegemony & The Fall of Kannauj': [
                'Dynastic establishment: Founded by Chandradeva (c. 1090 CE) following the chaotic collapse of the Pratiharas and Kalachuris; established dual capitals at Kannauj (political) and Varanasi (religious/cultural); assumed the imperial title "Parama-bhattaraka Maharajadhiraja Parameshvara".',
                'Govindachandra (r. 1114–1155 CE): Greatest Gahadavala emperor; defended the Gangetic Doab against Ghaznavid invasions from Punjab; levied a specific defense war tax called "Turushkadanda" (tax to fight or tribute paid to the Turks); patron of learning: minister Lakshmidhara authored the monumental 14-volume legal compendium Krityakalpataru (defining medieval Hindu civil law and court procedure); Queen Kumaradevi (Buddhist princess of Pithi) built the Dharmachakra Jina Vihara at Sarnath.',
                'Jaichand & The Battle of Chandawar (1194 CE): Last great sovereign; contemporary and rival of Prithviraj Chauhan (legendary swayamvara of daughter Sanyogita recorded in Prithviraj Raso); Muhammad Ghori invaded the Doab in 1194 CE; Jaichand confronted Ghori at the Battle of Chandawar (near Firozabad on the Yamuna river); struck in the eye by an arrow, Jaichand fell from his elephant and died; Ghori plundered Kannauj and Varanasi, destroying temples and ending independent Hindu monarchical rule in central UP.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Gahadavala dynasty ruled over Kannauj and Varanasi from the late 11th century until their defeat in 1194 CE.',
                'The "Turushkadanda" was an extraordinary war tax levied by Gahadavala rulers like Govindachandra to maintain defenses against Ghaznavid Turkish invasions.',
                'Lakshmidhara, the chief minister of Gahadavala king Govindachandra, compiled the celebrated encyclopaedic legal digest Krityakalpataru.',
                'Queen Kumaradevi, the Buddhist wife of Gahadavala king Govindachandra, constructed the Dharmachakra Jina Vihara monastery at Sarnath.',
                'The Battle of Chandawar took place in 1194 CE near modern Firozabad, where Muhammad Ghori defeated and killed Gahadavala king Jaichand.',
                'The Gahadavala rulers were devout Vaishnavas and Shaivas who styled themselves protectors of holy shrines in Varanasi, Ayodhya, and Gaya.',
                'The romantic episode of the abduction of Jaichand\'s daughter Sanyogita by Prithviraj Chauhan is recounted in Chand Bardai\'s Prithviraj Raso.'
            ],
            'mains': [
                'Evaluate the political, military, and administrative achievements of King Govindachandra Gahadavala, with specific reference to the Turushkadanda tax and the Krityakalpataru.',
                'Analyze the geopolitical causes and consequences of the Battle of Chandawar (1194 CE) in sealing the fate of Turkish hegemony across Northern India.',
                'Examine the patronage extended by the Gahadavalas to both Brahmanical learning and Buddhism at Varanasi and Sarnath.'
            ]
        }
    },
    'up-foundation-of-cities-medieval': {
        'aspects': {
            'Medieval Urban Foundations in UP': [
                'Agra (1504 CE): Founded by Sultan Sikandar Lodi as a forward military outpost against Rajput rulers and to control trade routes through the Doab; transferred the capital from Delhi to Agra in 1506 CE; transformed into the grand imperial metropolis "Akbarabad" by Akbar, Jahangir, and Shah Jahan.',
                'Jaunpur (1359 CE): Founded by Sultan Firuz Shah Tughlaq along the Gomti river, named in loving memory of his cousin Muhammad bin Tughlaq (whose original name was Fakhruddin Jauna Khan); flourished as the capital of the Sharqi Sultanate (1394–1479 CE), celebrated as the "Shiraz of the East".',
                'Firozabad (1354 CE): Founded by Firuz Shah Tughlaq on the Yamuna; evolved into India\'s premier hub of glassmaking, bangles, and chandeliers ("Suhag Nagari").',
                'Fatehpur Sikri (1571 CE): Founded by Emperor Akbar atop a rocky ridge near Sikri village to honor Sufi saint Shaikh Salim Chishti; planned imperial capital with red sandstone palaces, public halls, and Buland Darwaza.',
                'Other major medieval foundations: Sambhal, Badaun (cultural and administrative centre under Iltutmish and Sayyid kings), and Shahjahanpur (founded in 1647 by Diler Khan and Bahadur Khan under Shah Jahan).'
            ]
        },
        'upsc': {
            'prelims': [
                'Sikandar Lodi founded the city of Agra in 1504 CE and shifted his imperial capital there in 1506 CE.',
                'The city of Jaunpur was founded on the banks of the Gomti river in 1359 CE by Firuz Shah Tughlaq in memory of his cousin Jauna Khan (Muhammad bin Tughlaq).',
                'Firozabad was established by Firuz Shah Tughlaq and is historically renowned as India\'s glassmaking and bangle manufacturing capital ("Suhag Nagari").',
                'Akbar founded his planned capital city of Fatehpur Sikri in 1571 CE in gratitude to the Sufi saint Shaikh Salim Chishti.',
                'Badaun was an illustrious medieval administrative centre where Iltutmish served as governor before becoming Sultan of Delhi.',
                'Jaunpur was renowned throughout the medieval Islamic world as the "Shiraz-i-Hind" (Shiraz of the East) for its Islamic colleges and architecture.',
                'The historic Grand Trunk Road (Sadak-e-Azam) rebuilt by Sher Shah Suri traversed through major medieval urban hubs in UP including Chunar, Varanasi, and Agra.'
            ],
            'mains': [
                'Analyze the strategic, geopolitical, and commercial reasons behind the foundation of medieval cities in Uttar Pradesh, with special focus on Agra and Jaunpur.',
                'Examine the urban planning, water architecture, and cultural significance of Fatehpur Sikri as Akbar\'s planned capital.',
                'Discuss how urban foundations during the Delhi Sultanate and Mughal era reshaped trade routes and regional craft production across the Ganga-Yamuna Doab.'
            ]
        }
    },
    'up-delhi-sultanate': {
        'aspects': {
            'The Doab as Fiscal Core & Rebellions': [
                'Geopolitical significance: Uttar Pradesh and the fertile Ganga-Yamuna Doab formed the economic backbone of the Delhi Sultanate; prime source of agrarian land revenue (Kharaj).',
                'Administrative centres: Kara-Manikpur (on the Ganga near Prayagraj) served as the vital strategic provincial headquarters where Alauddin Khalji governed and murdered Jalaluddin; Badaun, Sambhal, Koil (Aligarh), Kannauj, and Baran (Bulandshahr) were major Iqta centres.',
                'Agrarian resistance: Rebellions of the Hindu agrarian gentry (Khuts and Muqaddams) in the Doab were crushed ruthlessly by Balban (who cleared the Mewat and Katehr forests) and Alauddin Khalji (who confiscated tax-free lands and raised revenue to 50%); severe famine in the Doab under Muhammad bin Tughlaq triggered wide peasant flight and uprisings.'
            ]
        },
        'upsc': {
            'prelims': [
                'Kara-Manikpur (near Prayagraj, UP) was the strategic provincial governorship from where Alauddin Khalji launched his raid on Devagiri and murdered Sultan Jalaluddin in 1296 CE.',
                'Badaun in Western UP was one of the most prestigious governorships in the Delhi Sultanate; Iltutmish served as its governor before ascending the throne.',
                'Balban deployed his "Blood and Iron" policy to ruthlessly suppress rural uprisings and bandits in the forests of Katehr (Rohilkhand) and the Doab.',
                'The famous Jama Masjid of Badaun (Shamsi Jama Masjid) was constructed by Shamsuddin Iltutmish in 1223 CE.',
                'Muhammad bin Tughlaq introduced agricultural relief measures (Diwan-i-Kohi and Takkavi loans) following devastating famines and rebellions in the Ganga-Yamuna Doab.',
                'Ziauddin Barani, the author of Tarikh-i-Firuz Shahi, hailed from Baran (modern Bulandshahr in Western Uttar Pradesh).',
                'Firuz Shah Tughlaq excavated canals from the Yamuna to irrigate agricultural tracts in the upper Doab and Haryana.'
            ],
            'mains': [
                'Examine the strategic, fiscal, and agrarian importance of the Ganga-Yamuna Doab for the sultans of Delhi from Iltutmish to Muhammad bin Tughlaq.',
                'Analyze the role of Kara-Manikpur as a nodal military base for Sultanate expansion into Central and Southern India.',
                'Discuss the peasant unrest in the Doab during the reign of Muhammad bin Tughlaq and evaluate the state\'s agricultural response through the Diwan-i-Kohi.'
            ]
        }
    },
    'up-jaunpur-sultanate': {
        'aspects': {
            'The Sharqi Dynasty & Shiraz of the East': [
                'Foundation (1394 CE): Malik Sarwar, a noble of Firuz Shah Tughlaq, appointed "Sultan-us-Sharq" (Ruler of the East) by Nasiruddin Mahmud Tughlaq; established the independent Sharqi Sultanate of Jaunpur; spanned modern Eastern UP and Western Bihar (Kanpur to Tirhut).',
                'Golden Age under Ibrahim Shah Sharqi (r. 1402–1440 CE): Promoted Islamic scholarship, literature, and arts; attracted celebrated scholars, theologians, and Sufis fleeing Timur\'s devastation of Delhi, earning Jaunpur the title "Shiraz-i-Hind" (Shiraz of the East).',
                'Sharqi Architectural Style: Distinctive monumental style discarding the traditional minaret; characterized by massive, steeply sloping propylons (screen walls with central arched pylon) fronting the central dome; blend of Hindu beam-and-bracket construction with Islamic arches; prominent monuments: Atala Masjid (built 1408 on site of Atala Devi temple), Jami Masjid (built 1478 by Husain Shah Sharqi), Lal Darwaza Masjid (built 1450 by Bibi Raji), and the historic Shahi Bridge (Akbari Bridge over Gomti built by Munim Khan in 1568).',
                'Fall of Dynasty: Perpetual wars with the Lodi Sultans of Delhi; Sultan Bahlul Lodi annexed Jaunpur in 1479 CE, defeating the last Sharqi Sultan Husain Shah Sharqi, though Sharqi culture and Hindustani classical music (Jaunpuri Todi, Khayal) endured.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Sharqi dynasty of Jaunpur was founded in 1394 CE by Malik Sarwar, who assumed the title "Sultan-us-Sharq" (King of the East).',
                'Jaunpur was hailed across medieval Asia as "Shiraz-i-Hind" (Shiraz of the East) due to its flourishing colleges, arts, and Islamic scholarship.',
                'The Atala Masjid at Jaunpur, completed in 1408 CE by Ibrahim Shah Sharqi, is famous for its massive central sloping pylon and absence of minarets.',
                'Sharqi architecture is unique for using towering screen facades (propylons) in front of domes and combining Hindu trabeate brackets with arcuate arches.',
                'The Shahi Bridge (Akbari Bridge) across the Gomti river in Jaunpur was built by Mughal governor Munim Khan in 1568 CE.',
                'Husain Shah Sharqi, the last ruler of Jaunpur, was a master composer of Hindustani classical music who created the Raga Jaunpuri and popularized Khayal singing.',
                'Bahlul Lodi annexed the Jaunpur Sultanate into the Delhi Sultanate in 1479 CE, ending the Sharqi dynasty.'
            ],
            'mains': [
                'Critically evaluate the architectural innovations of the Sharqi style of Jaunpur, with specific reference to the Atala Masjid and Jami Masjid.',
                'Analyze the cultural and intellectual flourishment that earned Jaunpur the moniker "Shiraz-i-Hind" during the 15th century.',
                'Examine the geopolitical conflict between the Sharqi rulers of Jaunpur and the Lodi Sultans of Delhi leading to the annexation of Jaunpur in 1479.'
            ]
        }
    },
    'up-sayyid-lodi-dynasty': {
        'aspects': {
            'Lodis in UP & The Foundation of Agra': [
                'Sayyid retirement in Badaun: Last Sayyid Sultan Alauddin Alam Shah voluntarily abdicated Delhi in 1451 CE and retired to Badaun (UP), where he lived peacefully until his death in 1478 CE.',
                'Sikandar Lodi & Agra Capital: Sikandar Lodi recognized that controlling the central Doab and neutralizing hostile Rajput chiefs required moving imperial headquarters south; founded Agra in 1504 CE and officially shifted the imperial capital there in 1506 CE; introduced Gaz-i-Sikandari; laid layout of modern Agra city.',
                'End of Sultanate: Ibrahim Lodi ruled from Agra; after his death at the First Battle of Panipat (1526), Babur dispatched Humayun directly to secure the royal treasury and palaces of Agra.'
            ]
        },
        'upsc': {
            'prelims': [
                'The city of Agra was established in 1504 CE by Sikandar Lodi to maintain strategic control over the Rajput borders and the Doab.',
                'Sikandar Lodi shifted the imperial capital of the Delhi Sultanate from Delhi to Agra in 1506 CE.',
                'The last Sayyid ruler, Alauddin Alam Shah, surrendered the throne of Delhi to Bahlul Lodi in 1451 CE and lived out his life in Badaun, UP.',
                'The standard land measurement rod "Gaz-i-Sikandari" of 32 units was introduced in Uttar Pradesh by Sikandar Lodi.',
                'Following the First Battle of Panipat (1526), Babur immediately dispatched Prince Humayun to seize the imperial treasury at Agra Fort.',
                'Sikandar Lodi constructed the Baradari building at Sikandra near Agra, which was later converted into the burial site of Akbar.',
                'Ibrahim Lodi resided primarily at Agra during his confrontation with rebellious Afghan sardars and Rana Sanga of Mewar.'
            ],
            'mains': [
                'Examine the strategic and political considerations that prompted Sikandar Lodi to found Agra in 1504 and make it the imperial capital.',
                'Analyze the transition of power from the Sayyids to the Lodis in Uttar Pradesh, focusing on the regional roles of Badaun and Jaunpur.',
                'Examine the administrative, agrarian, and architectural contributions of the Lodi dynasty in Uttar Pradesh with special reference to the Gaz-i-Sikandari and the Sikandra Baradari.'
            ]
        }
    },
    'up-mughal-period': {
        'aspects': {
            'Uttar Pradesh as Imperial Mughal Epicentre': [
                'Agra as the Mughal Capital (Akbarabad): Served as the primary imperial seat for Babur, Akbar, Jahangir, and Shah Jahan; Babur created Aram Bagh (1526); Akbar rebuilt Agra Fort in red sandstone (1565–1573 with over 500 stone structures including Jahangiri Mahal); Shah Jahan added the white marble Moti Masjid, Khas Mahal, Diwan-i-Aam, and Musamman Burj.',
                'Fatehpur Sikri: Built by Akbar (1571–1585) in Agra district; unique fusion of Rajput and Persian architectural traditions: Buland Darwaza (176 ft gateway), Jodha Bai Palace, Panch Mahal, Diwan-i-Khas with ornate central lotus bracket, Tomb of Shaikh Salim Chishti with white marble jali screens.',
                'The Taj Mahal (Agra): Built by Shah Jahan (1631–1648) on the Yamuna bank; peak of Mughal architecture using Makrana white marble, Pietra Dura inlay, double dome, and four minarets; world heritage monument.',
                'Other monumental heritage in UP: Akbar\'s Tomb at Sikandra (unique 5-tier open-air top pavilion without a dome), Tomb of Itmad-ud-Daula at Agra (built by Nur Jahan, "Baby Taj"), Allahabad Fort built by Akbar at the Sangam (1583 CE, housing the Ashoka Pillar and Patalpuri temple).'
            ]
        },
        'upsc': {
            'prelims': [
                'Akbar founded his imperial capital at Fatehpur Sikri in Agra district in 1571 CE to honor Sufi saint Shaikh Salim Chishti.',
                'The Buland Darwaza at Fatehpur Sikri was constructed by Akbar in 1601 CE to celebrate his victorious conquest of Gujarat.',
                'The Taj Mahal in Agra was commissioned by Shah Jahan in 1631 CE as a mausoleum for Mumtaz Mahal and designed by chief architect Ustad Ahmad Lahori.',
                'The tomb of Itmad-ud-Daula in Agra, constructed by Nur Jahan between 1622 and 1628 CE, is the earliest Mughal monument featuring extensive Pietra Dura on white marble.',
                'Akbar constructed the massive red sandstone Allahabad Fort at the confluence of the Ganga and Yamuna in 1583 CE.',
                'Akbar\'s tomb at Sikandra near Agra was planned by Akbar and completed by Jahangir in 1613 CE, notable for its tier-stacked design without a central dome.',
                'The Ram Bagh (originally Aram Bagh) in Agra is the oldest surviving Mughal garden in India, laid out by Babur in 1526 CE.'
            ],
            'mains': [
                'Critically evaluate the architectural evolution of Mughal monuments in Uttar Pradesh from Akbar\'s red sandstone at Fatehpur Sikri to Shah Jahan\'s white marble at the Taj Mahal.',
                'Analyze the planning, symbolic geometry, and defensive engineering of the Allahabad Fort built by Akbar at the holy confluence (Sangam).',
                'Examine the influence of Rajput architectural elements in the palaces of Fatehpur Sikri and the Agra Fort.'
            ]
        }
    },
    'up-later-mughals': {
        'aspects': {
            'Nawabs of Awadh & Lucknow Composite Culture': [
                'Rise of the Awadh Nawabi: Saadat Khan Burhan-ul-Mulk appointed Subahdar of Awadh in 1722 by Muhammad Shah; founded autonomous dynasty; succeeded by Safdarjung (1739–1754, who also served as imperial Wazir).',
                'Shuja-ud-Daula (r. 1754–1775): Fought alongside Ahmad Shah Abdali at Third Battle of Panipat (1761); formed confederacy with Mir Qasim and Shah Alam II against the British, defeated at Battle of Buxar (1764); signed Treaty of Allahabad (1765), paying 50 lakh indemnity and ceding Kora and Allahabad to the Company.',
                'Asaf-ud-Daula & Shift to Lucknow (1775): Shifted capital from Faizabad to Lucknow in 1775; commissioned the monumental Bara Imambara (Asafi Imambara, 1784) during a devastating famine as food-for-work relief; world\'s largest unsupported vaulted central hall without pillars or beams; built the Bhulbhulaiya (labyrinth) and Rumi Darwaza (modeled on the Sublime Porte of Istanbul).',
                'Wajid Ali Shah & The Twilight of Awadh: Last Nawab (r. 1847–1856); celebrated patron of music, dance, and poetry; developed Kathak dance and Thumri; authored Indar Sabha (first musical opera in Urdu); deposed by Lord Dalhousie in February 1856 on the pretext of misgovernance, and exiled to Metiabruz near Calcutta.'
            ]
        },
        'upsc': {
            'prelims': [
                'Saadat Khan Burhan-ul-Mulk founded the autonomous principality of Awadh in 1722 with its original capital at Faizabad.',
                'Nawab Asaf-ud-Daula shifted the capital of Awadh from Faizabad to Lucknow in 1775 CE.',
                'The Bara Imambara in Lucknow was built in 1784 CE by Nawab Asaf-ud-Daula as a famine relief project, renowned for its vaulted roof without supporting pillars and the Bhulbhulaiya labyrinth.',
                'The Rumi Darwaza in Lucknow was constructed by Asaf-ud-Daula in 1784 CE, modeled after the historic Bab-i-Humayun (Sublime Porte) gateway in Constantinople / Istanbul.',
                'The Treaty of Allahabad was signed in August 1765 between Robert Clive, Nawab Shuja-ud-Daula of Awadh, and Mughal Emperor Shah Alam II.',
                'Nawab Wajid Ali Shah was a celebrated patron of the Lucknow Gharana of Kathak dance, under whose patronage classical Thumri blossomed.',
                'Lord Dalhousie annexed the Kingdom of Awadh on 7 February 1856 on the pretext of "gross maladministration" based on the Outram report, exiling Wajid Ali Shah to Calcutta.'
            ],
            'mains': [
                'Analyze the political, diplomatic, and territorial consequences of the Treaty of Allahabad (1765) for the Nawab of Awadh and the British East India Company.',
                'Examine the distinctive architectural and cultural features of the Nawabs of Awadh in Lucknow, with special reference to the Bara Imambara, Rumi Darwaza, and Chhota Imambara.',
                'Discuss the development of the "Ganga-Jamuni Tehzeeb" (composite culture), Urdu poetry, and Kathak dance under the patronage of the Nawabs of Awadh.'
            ]
        }
    },
    'up-british-rule-administration': {
        'aspects': {
            'Colonial Administrative Evolution in UP': [
                'Ceded and Conquered Provinces (1801–1803): Awadh Nawab ceded Rohilkhand, Gorakhpur, and the lower Doab in 1801; Second Anglo-Maratha War (1803) yielded upper Doab, Agra, and Delhi to the British; annexed into the Bengal Presidency.',
                'North-Western Provinces (NWP, 1836): Carved out as a separate administrative territory under a Lieutenant-Governor with headquarters at Agra (Sir Charles Metcalfe as first Lt. Governor); shifted capital to Allahabad in 1858.',
                'United Provinces Formations: Oudh added to NWP in 1877; renamed the "United Provinces of Agra and Oudh" in 1902; capital shifted from Allahabad to Lucknow in 1920 (formalized 1935); renamed simply the "United Provinces" (UP) in 1937 under the Government of India Act 1935.',
                'Judiciary & Infrastructure: Allahabad High Court established in 1866 (originally seated at Agra, shifted to Allahabad in 1869); first railway line in UP ran between Allahabad and Kanpur on 3 March 1859; Upper Ganga Canal engineered by Sir Proby Cautley (1854); Roorkee Engineering College founded in 1847 (oldest technical institution in Asia, now IIT Roorkee).'
            ]
        },
        'upsc': {
            'prelims': [
                'The North-Western Provinces (NWP) was established in 1836 with its administrative headquarters at Agra, headed by Sir Charles Metcalfe.',
                'The headquarters of the North-Western Provinces was shifted from Agra to Allahabad in 1858 following the suppression of the 1857 Revolt.',
                'The High Court of Judicature for the North-Western Provinces was established at Agra in 1866 and relocated to Allahabad in 1869.',
                'The first railway line in Uttar Pradesh began operations on 3 March 1859 between Allahabad and Kanpur.',
                'The Upper Ganga Canal, one of the greatest colonial hydraulic engineering works in the world, was designed by Sir Proby Cautley and opened in 1854.',
                'The province was renamed the "United Provinces of Agra and Oudh" in 1902 and shortened to "United Provinces" in 1937.',
                'The Thomason College of Civil Engineering at Roorkee, founded in 1847, was the first engineering college established in the British Empire.'
            ],
            'mains': [
                'Trace the administrative and territorial evolution of Uttar Pradesh under British colonial rule from the Ceded Provinces (1801) to the United Provinces (1937).',
                'Evaluate the hydraulic and agricultural impact of the Upper Ganga Canal constructed in 19th-century Western Uttar Pradesh.',
                'Discuss the establishment and historical contributions of the Allahabad High Court to Indian jurisprudence and the freedom movement.'
            ]
        }
    },
    'up-revolt-of-1857': {
        'aspects': {
            'Uttar Pradesh as the Epicentre of 1857': [
                'First Sparks: Sepoy Mangal Pandey (34th Bengal Native Infantry, native of Nagwa village, Ballia, UP) revolted at Barrackpore on 29 March 1857; mutiny erupted at Meerut on 10 May 1857 when 85 sepoys of the 3rd Native Cavalry broke jail and marched to Delhi.',
                'Awadh & Lucknow: Begum Hazrat Mahal crowned her 11-year-old son Birjis Qadr as Nawab; seized Lucknow with support of taluqdars and sepoys; besieged the British Residency for 87 days (killing British Chief Commissioner Sir Henry Lawrence); Colin Campbell relieved the Residency in March 1858; Begum refused surrender and retreated to Nepal.',
                'Kanpur: Nana Saheb (adopted son of Peshwa Baji Rao II) led the uprising aided by military genius Tatya Tope and Azimullah Khan; captured Kanpur (massacre at Sati Chaura Ghat and Bibighar); recaptured by Colin Campbell; Tatya Tope fled to Gwalior to join Rani Lakshmibai.',
                'Jhansi: Rani Lakshmibai ("Khoob Ladi Mardani") revolted after Dalhousie annexed Jhansi under Doctrine of Lapse; defended Jhansi fort against Sir Hugh Rose; escaped on horse Sarangi with adopted son Damodar Rao; captured Gwalior fort; martyred in battle at Kotah-ki-Serai, Gwalior (18 June 1858); Hugh Rose eulogized: "Here lay the woman who was the only man among the rebels."',
                'Other Centres: Bareilly under Khan Bahadur Khan; Allahabad under Maulvi Liyaqat Ali; Faizabad under fiery patriot Maulvi Ahmadullah Shah; Mathura under Devi Singh; Kalpi.'
            ]
        },
        'upsc': {
            'prelims': [
                'Mangal Pandey, who fired the first shot of the 1857 uprising at Barrackpore, hailed from Nagwa village in Ballia district of Uttar Pradesh.',
                'The 1857 Revolt officially broke out at Meerut on 10 May 1857, initiated by sepoys of the 3rd Native Cavalry.',
                'Begum Hazrat Mahal led the revolt in Lucknow, proclaiming her minor son Birjis Qadr as the Nawab of Awadh.',
                'Sir Henry Lawrence, the British Chief Commissioner of Awadh, was killed during the siege of the British Residency in Lucknow in July 1857.',
                'Nana Saheb and his general Tatya Tope led the revolt in Kanpur, assisted by Azimullah Khan.',
                'Maulvi Ahmadullah Shah, celebrated as the "Danka Shah" for his fiery speeches, led the anti-British revolt in Faizabad.',
                'Sir Hugh Rose commanded the British forces that captured Jhansi and praised Rani Lakshmibai as "the bravest and best military leader of the rebels".'
            ],
            'mains': [
                'Critically analyze why Uttar Pradesh (specifically Awadh and the Doab) became the principal storm-centre and military battleground of the Revolt of 1857.',
                'Evaluate the leadership, military resistance, and tragic heroism of Rani Lakshmibai of Jhansi and Begum Hazrat Mahal of Lucknow during the 1857 uprising.',
                'Examine the role of the Taluqdars and peasants of Awadh in transforming the 1857 sepoy mutiny into a popular war of liberation.',
                'Discuss the administrative changes implemented in Uttar Pradesh following Queen Victoria\'s Proclamation of 1858 and the abolition of the East India Company.'
            ]
        }
    },
    'up-freedom-struggle': {
        'aspects': {
            'Landmark Milestones of UP Nationalism': [
                'INC Sessions in UP: Allahabad hosted three historic sessions (1888 under George Yule, 1892 under W.C. Bonnerjee, 1910 under William Wedderburn); Lucknow hosted three sessions (1899 under R.C. Dutt, 1916 under A.C. Majumdar - Lucknow Pact, 1936 under Jawaharlal Nehru); Benaras hosted 1905 session under G.K. Gokhale; Kanpur hosted 1925 session under Sarojini Naidu (first Indian woman INC president); Meerut hosted 1946 session under J.B. Kripalani.',
                'Chauri Chaura Incident (4 February 1922): Gorakhpur district; police fired on peaceful Non-Cooperation protestors; crowd burned police station killing 22 policemen; Gandhi suspended the nationwide Non-Cooperation Movement on 12 February 1922.',
                'Swaraj Party & HRA: Swaraj Party formed on 1 January 1923 at Anand Bhavan, Allahabad by Motilal Nehru and C.R. Das; Hindustan Republican Association (HRA) established in Kanpur (1924); Kakori Train Action executed on 9 August 1925 near Lucknow; Chandra Shekhar Azad martyred at Alfred Park, Allahabad on 27 February 1931.',
                'Peasant Mobilization: Awadh Kisan Sabha formed in October 1920 at Pratapgarh by Baba Ramchandra, Jawaharlal Nehru, and Gauri Shankar Mishra; Eka Movement (1921) led by Madari Pasi across Hardoi, Bahraich, and Sitapur; All India Kisan Sabha established at Lucknow in 1936 (Swami Sahajanand Saraswati as President, N.G. Ranga as Secretary).',
                'Parallel Government in Ballia (1942): Quit India Movement; Chittu Pandey ("Sher-e-Ballia") established a parallel independent government (Prati Sarkar) in Ballia in August 1942, taking over civil administration and releasing all political prisoners from jail.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Chauri Chaura incident occurred on 4 February 1922 in Gorakhpur district of UP, prompting Mahatma Gandhi to call off the Non-Cooperation Movement.',
                'The Swaraj Party was founded on 1 January 1923 at Anand Bhavan in Allahabad by Motilal Nehru and Deshbandhu Chittaranjan Das.',
                'Sarojini Naidu became the first Indian woman to preside over the Indian National Congress at the Kanpur Session in 1925.',
                'Chandra Shekhar Azad sacrificed his life fighting British police at Alfred Park (now Chandrashekhar Azad Park) in Allahabad on 27 February 1931.',
                'The Awadh Kisan Sabha was formed in October 1920 in Pratapgarh under the leadership of Baba Ramchandra and Jawaharlal Nehru.',
                'The Eka Movement (Unity Movement) of peasants was launched in 1921 across Hardoi, Bahraich, and Sitapur under the leadership of Madari Pasi.',
                'Chittu Pandey ("Sher-e-Ballia") formed the first parallel independent government during the Quit India Movement in Ballia in August 1942.'
            ],
            'mains': [
                'Examine the contribution of Uttar Pradesh to the peasant movements of modern India with specific reference to the Awadh Kisan Sabha and the Eka Movement.',
                'Analyze the significance of the Chauri Chaura incident (1922) and critically evaluate Mahatma Gandhi\'s decision to suspend the Non-Cooperation Movement.',
                'Discuss the role of revolutionary nationalist organizations in Uttar Pradesh (HRA, HSRA, and Kakori Action) in radicalizing the freedom struggle.',
                'Evaluate the Quit India Movement of 1942 in Uttar Pradesh, with special focus on the parallel government established by Chittu Pandey in Ballia.'
            ]
        }
    },
    'up-socio-religious-movement': {
        'aspects': {
            'Renaissance & Reform Institutions in UP': [
                'Aligarh Movement: Founded by Sir Syed Ahmad Khan; established the Scientific Society (1864 at Ghazipur, shifted to Aligarh); founded the Mohammedan Anglo-Oriental (MAO) College at Aligarh in 1875 (elevated to Aligarh Muslim University in 1920); championed modern Western scientific education and Urdu journalism (Tahzib-ul-Akhlaq).',
                'Islamic Seminaries: Darul Uloom Deoband founded in 1866 in Saharanpur district by Muhammad Qasim Nanautavi and Rashid Ahmad Gangohi; revivalist orthodox school firmly opposed to British colonial rule and pro-nationalist; Nadwatul Ulama established at Lucknow in 1894 by Maulana Shibli Nomani.',
                'Hindu & Vedic Reforms: Swami Dayananda established Arya Samaj branches across UP; Gurukul Kangri established at Haridwar (then UP) in 1902 by Swami Shraddhanand to revive ancient Vedic pedagogy; Radhasoami Satsang founded at Agra in 1861 by Shiv Dayal Singh (Soami Ji Maharaj).',
                'Theosophical Society & BHU: Theosophical Society established national headquarters at Varanasi; Annie Besant founded Central Hindu College at Kamachha, Varanasi in 1898; Pandit Madan Mohan Malaviya integrated it to establish Banaras Hindu University (BHU) in 1916 with foundation stone laid by Lord Hardinge; Bharat Dharma Mahamandal founded at Varanasi in 1902 by Pandit Din Dayalu Sharma.'
            ]
        },
        'upsc': {
            'prelims': [
                'Sir Syed Ahmad Khan established the Scientific Society at Ghazipur in 1864 and founded the MAO College at Aligarh in 1875.',
                'The Darul Uloom seminary at Deoband (Saharanpur district, UP) was established in 1866 by Muhammad Qasim Nanautavi and Rashid Ahmad Gangohi.',
                'Banaras Hindu University (BHU) was founded in Varanasi in 1916 by Pandit Madan Mohan Malaviya with the support of Annie Besant and Maharaja Rameshwar Singh of Darbhanga.',
                'The Radhasoami spiritual movement was founded in Agra in 1861 by Shiv Dayal Singh (known as Soami Ji Maharaj).',
                'Annie Besant founded the Central Hindu College at Varanasi in 1898, which later formed the nucleus of Banaras Hindu University.',
                'Nadwatul Ulama, an Islamic seminary balancing traditional theology with modern subjects, was established at Lucknow in 1894 by Shibli Nomani.',
                'Bharat Ratna Pandit Madan Mohan Malaviya was conferred the title of "Mahamana" by Mahatma Gandhi.'
            ],
            'mains': [
                'Critically evaluate the socio-religious and educational impact of the Aligarh Movement under Sir Syed Ahmad Khan on the modernization of Indian Muslims.',
                'Compare and contrast the political and ideological stances of the Aligarh Movement and the Deoband Movement toward the Indian national freedom struggle.',
                'Discuss the vision and contributions of Pandit Madan Mohan Malaviya and Annie Besant in the establishment and growth of Banaras Hindu University (BHU).'
            ]
        }
    },
    'up-united-provinces-modern': {
        'aspects': {
            'Provincial Autonomy & First Congress Ministry': [
                'Government of India Act 1935: Replaced Dyarchy with Provincial Autonomy; United Provinces established a bicameral legislature (Legislative Assembly with 228 seats and Legislative Council with 52 seats).',
                '1937 Elections & Pant Ministry: Provincial elections held in February 1937; Indian National Congress won an overwhelming absolute majority in UP (133 of 228 seats); Premier Govind Ballabh Pant formed the first Congress ministry in UP on 17 July 1937; Rafi Ahmad Kidwai served as Revenue Minister, K.N. Katju as Law Minister, and Vijaya Lakshmi Pandit as Minister of Local Self-Government and Health (first woman cabinet minister in Indian history); enacted the UP Tenancy Act 1939 to protect tenant farmers against eviction.',
                '1939 Resignation: Entire Congress ministry in UP resigned in October 1939 in protest against Viceroy Lord Linlithgow unilaterally declaring India a party to World War II without consulting provincial ministries.'
            ]
        },
        'upsc': {
            'prelims': [
                'Govind Ballabh Pant served as the first Premier (Chief Minister) of the United Provinces following the 1937 provincial elections.',
                'Vijaya Lakshmi Pandit became the first woman cabinet minister in India when she was appointed Minister of Local Self-Government and Health in the UP Ministry in 1937.',
                'The United Provinces Tenancy Act of 1939 was passed by the Pant ministry to provide security of tenure and eliminate arbitrary peasant evictions.',
                'Rafi Ahmad Kidwai served as the Revenue Minister in the first Congress government in the United Provinces in 1937.',
                'The Congress ministry in the United Provinces resigned in October 1939 over Britain\'s unilateral entry of India into World War II without legislative consent.',
                'Under the Government of India Act 1935, the official name of the province was simplified from "United Provinces of Agra and Oudh" to "United Provinces" in 1937.',
                'Purushottam Das Tandon served as the first Speaker of the United Provinces Legislative Assembly from 1937 to 1950.'
            ],
            'mains': [
                'Examine the functioning, legislative achievements, and agrarian reforms of the first Congress Ministry in the United Provinces headed by Govind Ballabh Pant (1937–1939).',
                'Discuss the constitutional significance of the 1937 provincial elections in the United Provinces under the Government of India Act 1935.',
                'Analyze the historical role of Vijaya Lakshmi Pandit and Purushottam Das Tandon in the legislative politics of the United Provinces.'
            ]
        }
    },
    'up-formation': {
        'aspects': {
            'Nomenclature & Constitutional Transition': [
                'Historical Chronology of Naming: 1836: North-Western Provinces (Agra capital) -> 1877: North-Western Provinces & Oudh -> 1902: United Provinces of Agra & Oudh -> 1937: United Provinces -> 24 January 1950: officially named "Uttar Pradesh".',
                'United Provinces Alteration of Name Order 1950: Issued by Governor-General C. Rajagopalachari on 24 January 1950 under Section 290A of the Government of India Act 1935; renamed the province "Uttar Pradesh"; state constitutionally became a Part A state of the Indian Union on 26 January 1950; capital permanently established at Lucknow; 24 January declared official "UP Diwas" in 2018.',
                'First Leaders: Sir Hormasji Peroshaw Mody served as first Governor of Uttar Pradesh; Govind Ballabh Pant took oath as first Chief Minister of Uttar Pradesh on 26 January 1950.'
            ]
        },
        'upsc': {
            'prelims': [
                'The United Provinces was officially rechristened as "Uttar Pradesh" on 24 January 1950 through the United Provinces (Alteration of Name) Order.',
                'Uttar Pradesh celebrates its official State Foundation Day ("UP Diwas") on 24 January every year.',
                'Pandit Govind Ballabh Pant was the first Chief Minister of Uttar Pradesh after its renaming in 1950.',
                'Sir Hormasji Peroshaw Mody (H.P. Mody) served as the first Governor of Uttar Pradesh following its constitutional formation.',
                'Sucheta Kripalani became the first female Chief Minister of Uttar Pradesh (and of any Indian state) in October 1963.',
                'Sarojini Naidu served as the first Governor of the United Provinces (1947–1949), becoming the first woman governor of an Indian state.',
                'The state symbol of Uttar Pradesh depicts the sacred confluence of the Ganga and Yamuna, a pair of fish (Matsya), and a bow and arrow (Dhanush-Baan).'
            ],
            'mains': [
                'Trace the chronological and constitutional evolution of Uttar Pradesh from the colonial British administrative divisions to the naming of the state on 24 January 1950.',
                'Analyze the contributions of Pandit Govind Ballabh Pant and Sucheta Kripalani in laying the administrative and agrarian foundations of post-independence Uttar Pradesh.',
                'Discuss the state symbols, geographical boundaries, and constitutional status of Uttar Pradesh under Part A of the Constitution of India.'
            ]
        }
    },
    'up-political-developments': {
        'aspects': {
            'Political Heartland of the Indian Republic': [
                'Electoral weight: Largest legislative state in India: 80 Lok Sabha seats (out of 543) and 31 Rajya Sabha seats; 403 Vidhan Sabha (Legislative Assembly) seats and 100 Vidhan Parishad (Legislative Council) seats; political adage: "The road to Delhi passes through Lucknow."',
                'Nine Prime Ministers from UP: Uttar Pradesh has sent 9 Prime Ministers to India: Jawaharlal Nehru (Phulpur), Lal Bahadur Shastri (Allahabad), Indira Gandhi (Rae Bareli), Charan Singh (Baghpat), Rajiv Gandhi (Amethi), V.P. Singh (Fatehpur), Chandra Shekhar (Ballia), Atal Bihari Vajpayee (Lucknow), and Narendra Modi (Varanasi).',
                'Era of Coalition Politics & Social Justice: Dominated by Congress until 1967; rise of peasant politics under Chaudhary Charan Singh (Bharatiya Kranti Dal / Lok Dal); emergence of coalition governments (Samyukta Vidhayak Dal 1967); rise of subaltern and social justice empowerment in 1990s: Samajwadi Party (Mulayam Singh Yadav) and Bahujan Samaj Party (Kanshi Ram and Mayawati - first Dalit woman Chief Minister of an Indian state in 1995); single-party majority mandates restored in 2007, 2012, 2017, and 2022.'
            ]
        },
        'upsc': {
            'prelims': [
                'Uttar Pradesh has the largest legislative representation in India: 80 Lok Sabha seats, 31 Rajya Sabha seats, 403 Legislative Assembly seats, and 100 Legislative Council seats.',
                'Nine Prime Ministers of India have represented parliamentary constituencies in Uttar Pradesh, including Jawaharlal Nehru, Indira Gandhi, and Narendra Modi.',
                'Chaudhary Charan Singh founded the Bharatiya Kranti Dal (BKD) and became the first non-Congress Chief Minister of Uttar Pradesh in April 1967.',
                'Mayawati became the first Dalit woman Chief Minister of an Indian state when she assumed office in Uttar Pradesh in June 1995.',
                'Sucheta Kripalani was the first woman Chief Minister in Indian history, heading the Uttar Pradesh government from 1963 to 1967.',
                'The first Speaker of the Legislative Assembly of Uttar Pradesh was Purushottam Das Tandon.',
                'The bicameral legislature of Uttar Pradesh was first created under the Government of India Act 1935 and held its first sitting in 1937.'
            ],
            'mains': [
                'Critically evaluate the political dominance of Uttar Pradesh in national Indian politics, analyzing why the state has produced nine Prime Ministers.',
                'Trace the rise of social justice, subaltern empowerment, and coalition politics in Uttar Pradesh from the 1960s to the 1990s (Charan Singh, Kanshi Ram, Mulayam Singh Yadav, Mayawati).',
                'Analyze the working and federal significance of the bicameral legislature (Vidhan Sabha and Vidhan Parishad) in Uttar Pradesh.'
            ]
        }
    },
    'up-reorganisation': {
        'aspects': {
            'Creation of Uttarakhand & Administrative Map': [
                'Uttarakhand Statehood Movement: Decades of peaceful and militant regional protests by the Uttarakhand Kranti Dal (UKD) demanding statehood for Himalayan hill districts; tragic police firings at Khatima, Mussoorie, and Rampur Tiraha (Muzaffarnagar, October 1994); Parliament enacted the Uttar Pradesh Reorganisation Act 2000.',
                'Bifurcation of 9 November 2000: 13 hill districts of Garhwal and Kumaon were bifurcated from Uttar Pradesh to form the 27th state of India, initially named "Uttaranchal" (renamed Uttarakhand in 2007); reduced UP\'s territorial area by 53,483 sq km (approx 17.5%), shifting UP\'s northern boundary to the Himalayan foothills.',
                'Current Administrative Structure: Uttar Pradesh is divided into 18 Administrative Divisions, 75 Districts, 351 Tehsils, 826 Development Blocks, and over 58,000 Gram Panchayats; four major socio-economic regions: Western UP (Paschim Pradesh), Central UP (Awadh), Eastern UP (Purvanchal), and Southern UP (Bundelkhand).'
            ]
        },
        'upsc': {
            'prelims': [
                'The state of Uttarakhand (originally Uttaranchal) was carved out of 13 hill districts of Uttar Pradesh on 9 November 2000 under the UP Reorganisation Act 2000.',
                'Uttar Pradesh currently has 75 districts grouped into 18 administrative divisions, with 351 tehsils and 826 community development blocks.',
                'The largest district of Uttar Pradesh by geographical area is Lakhimpur Kheri (7,680 sq km).',
                'The smallest district of Uttar Pradesh by geographical area is Hapur (approx 660 sq km).',
                'The most populous district of Uttar Pradesh according to the 2011 Census is Prayagraj (Allahabad).',
                'The least populous district of Uttar Pradesh according to the 2011 Census is Mahoba in Bundelkhand.',
                'Sonbhadra is the only district in India that shares interstate borders with four states: Madhya Pradesh, Chhattisgarh, Jharkhand, and Bihar.'
            ],
            'mains': [
                'Analyze the administrative, economic, and ecological consequences of the creation of Uttarakhand (2000) for Uttar Pradesh.',
                'Examine the recurring political demands for the further division of Uttar Pradesh into four smaller states (Harit Pradesh, Purvanchal, Bundelkhand, Awadh).',
                'Discuss the administrative tier architecture of Uttar Pradesh across Divisions, Districts, Tehsils, Blocks, and Gram Panchayats.'
            ]
        }
    },
    'up-economic-social-progress': {
        'aspects': {
            'Agrarian Base, Industrial Clusters & ODOP': [
                'Agricultural Powerhouse: India\'s leading producer of food grains, sugarcane, wheat, potatoes, and milk; irrigated by extensive canal networks (Sharda Canal, Upper Ganga Canal, Lower Ganga Canal) and groundwater tube-wells; Western UP characterized by high productivity cash-crop farming.',
                'Specialized Industrial Clusters: 1. Leather & Footwear: Kanpur and Agra, 2. Textile & Handloom: Varanasi (Banarasi Silk), Mau, Kanpur ("Manchester of the East"), 3. Brassware & Metal: Moradabad ("Peetal Nagari"), 4. Glassware: Firozabad ("Suhag Nagari"), 5. Locks & Hardware: Aligarh, 6. Wooden Carvings: Saharanpur, 7. Handmade Carpets: Bhadohi and Mirzapur, 8. Chikan Embroidery & Zardozi: Lucknow, 9. Perfume (Ittar): Kannauj ("Perfume Capital of India").',
                'One District One Product (ODOP): Pioneering state flagship scheme launched in January 2018; promotes, finances, brands, and exports distinct indigenous artisanal crafts and agro-products across all 75 districts; adopted as a national model by the Government of India.'
            ]
        },
        'upsc': {
            'prelims': [
                'The One District One Product (ODOP) scheme was first conceptualized and launched by the Government of Uttar Pradesh in January 2018.',
                'Uttar Pradesh ranks first in India in the production of wheat, sugarcane, potatoes, and milk.',
                'Kanpur was historically acclaimed as the "Manchester of the East" due to its flourishing textile mills and leather tanneries.',
                'Kannauj in Uttar Pradesh is celebrated as the "Perfume Capital of India" (Ittar Nagari) for its traditional hydro-distilled floral fragrances.',
                'Bhadohi district in Uttar Pradesh is globally renowned as the "Carpet City" of South Asia, holding a registered GI tag for handmade carpets.',
                'Moradabad is internationally famous as the "Brass City" (Peetal Nagari) for its brass handicraft exports.',
                'The Sharda Canal, commissioned in 1928, is the longest canal network in Uttar Pradesh, irrigating the Rohilkhand and Awadh plains.'
            ],
            'mains': [
                'Evaluate the achievements, institutional design, and export impact of the One District One Product (ODOP) initiative in reviving traditional handicrafts in Uttar Pradesh.',
                'Analyze the regional economic disparities between Western Uttar Pradesh, Purvanchal, and Bundelkhand, recommending policy interventions for balanced regional development.',
                'Discuss the challenges facing agriculture in Uttar Pradesh with specific reference to land fragmentation, sugarcane pricing, and groundwater depletion.'
            ]
        }
    },
    'up-21st-century': {
        'aspects': {
            'Expressways, Defense Corridor & 1 Trillion Dollar Vision': [
                'Expressway State of India: UP has built India\'s largest high-speed expressway network: 1. Yamuna Expressway (165 km, Greater Noida to Agra), 2. Agra-Lucknow Expressway (302 km, features an airstrip for fighter jet emergency landings), 3. Purvanchal Expressway (341 km, Lucknow to Ghazipur), 4. Bundelkhand Expressway (296 km, Etawah to Chitrakoot), 5. Ganga Expressway (594 km, Meerut to Prayagraj - under construction).',
                'Defense Industrial Corridor (UP DIC): Set up across 6 strategic nodes: Aligarh, Agra, Jhansi, Chitrakoot, Kanpur, and Lucknow; developing indigenous aerospace manufacturing, BrahMos supersonic cruise missile production unit in Lucknow, artillery shell manufacturing in Kanpur.',
                'Aviation & Megaprojects: Jewar / Noida International Airport (poised to be India\'s largest international airport with 5–6 runways); Maryada Purushottam Shri Ram International Airport at Ayodhya; dedicated industrial freight corridors (EDFC and WDFC intersecting at Dadri Multi-Modal Logistics Hub).',
                'Vision for 1 Trillion Dollar GSDP: Ambitious target to scale UP\'s Gross State Domestic Product to 1 trillion US dollars by 2027–2030, anchored by infrastructure investments, tourism corridors (Kashi Vishwanath Corridor, Ayodhya Dham, Braj Teerth Vikas), and green energy.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Uttar Pradesh Defense Industrial Corridor (UP DIC) comprises six dedicated nodes: Agra, Aligarh, Chitrakoot, Jhansi, Kanpur, and Lucknow.',
                'The BrahMos aerospace integration facility producing next-generation cruise missiles is situated in Lucknow, Uttar Pradesh.',
                'The Purvanchal Expressway connects Chand Sarai (Lucknow district) to Haidaria (Ghazipur district) spanning 341 kilometres.',
                'The Ganga Expressway, spanning 594 km from Meerut to Prayagraj, is under construction as the longest expressway in Uttar Pradesh.',
                'Noida International Airport at Jewar (Gautam Buddha Nagar) is designed to be the largest greenfield international airport in South Asia.',
                'The Eastern Dedicated Freight Corridor (EDFC) and Western Dedicated Freight Corridor (WDFC) intersect at Dadri in Uttar Pradesh.',
                'The Kashi Vishwanath Dham Corridor connecting the temple directly to the Ganga riverfront at Varanasi was inaugurated in December 2021.'
            ],
            'mains': [
                'Critically evaluate the infrastructure-led development model of Uttar Pradesh with specific focus on the operational and upcoming expressway networks.',
                'Analyze the strategic and economic significance of the Uttar Pradesh Defense Industrial Corridor in promoting indigenization and manufacturing under "Make in India".',
                'Discuss the roadmap, sectoral opportunities, and structural challenges in realizing Uttar Pradesh\'s target of becoming a One Trillion Dollar Economy.'
            ]
        }
    },
    'up-important-personalities': {
        'aspects': {
            'Luminaries of Uttar Pradesh': [
                'Spiritual & Literary Giants: Sage Valmiki (Bithoor on Ganga); Ved Vyasa; Goswami Tulsidas (Rajapur / Varanasi - Ramcharitmanas, Vinaya Patrika); Sant Kabir (Varanasi - Bijak; Maghar nirvana); Surdas (Runkata, Agra - Sursagar); Amir Khusrau (Patiyali, Kasganj - inventor of Sitar, Qawwali, Hindavi poet); Malik Muhammad Jayasi (Jais, Amethi - Padmavat); Bharatendu Harishchandra (Varanasi - "Father of Modern Hindi Literature"); Munshi Premchand (Lamhi, Varanasi - Godan, Gaban, Idgah); Suryakant Tripathi Nirala; Jaishankar Prasad; Mahadevi Verma; Harivansh Rai Bachchan.',
                'Mughal Courtiers & Artists: Raja Todar Mal (Laharpur, Sitapur - creator of Dahsala revenue system); Raja Birbal (Mahesh Das, Kalpi - Navaratna court wit); Ustad Bismillah Khan (Varanasi - Shehnai maestro, Bharat Ratna 2001); Pandit Ravi Shankar (Varanasi - Sitar maestro, Bharat Ratna 1999); Begum Akhtar (Faizabad - Queen of Ghazals).',
                'Patriots & Statesmen: Mangal Pandey (Ballia); Rani Lakshmibai (Jhansi); Begum Hazrat Mahal (Lucknow); Chandra Shekhar Azad (Unnao/Allahabad); Ram Prasad Bismil (Shahjahanpur); Ashfaqulla Khan (Shahjahanpur); Motilal Nehru & Jawaharlal Nehru (Allahabad); Madan Mohan Malaviya (Prayagraj); Purushottam Das Tandon; Rafi Ahmad Kidwai; Chaudhary Charan Singh (Meerut/Baghpat - Champion of Indian Kisans); Atal Bihari Vajpayee (Bateshwar, Agra / Lucknow).'
            ]
        },
        'upsc': {
            'prelims': [
                'Amir Khusrau was born in Patiyali (Kasganj district, UP) in 1253 CE, and was celebrated as the "Tuti-i-Hind" (Parrot of India).',
                'Munshi Premchand, the greatest novelist of modern Hindi and Urdu literature (author of Godan and Gaban), was born in Lamhi village near Varanasi.',
                'Raja Todar Mal, the architect of Akbar\'s Dahsala land revenue system, hailed from Laharpur in Sitapur district of Uttar Pradesh.',
                'Raja Birbal (original name Mahesh Das), one of Akbar\'s Nine Gems, was born in Kalpi in Jalaun district of Uttar Pradesh.',
                'Shehnai virtuoso Ustad Bismillah Khan, who performed on the ramparts of Red Fort on India\'s Independence Day in 1947, was based in Varanasi and awarded the Bharat Ratna in 2001.',
                'Ram Prasad Bismil, Ashfaqulla Khan, and Roshan Singh, legendary martyrs of the Kakori Action (1925), all hailed from Shahjahanpur district, UP.',
                'Mahadevi Verma, the celebrated Hindi Chhayavadi poetess and Jnanpith laureate, was born in Farrukhabad, Uttar Pradesh.'
            ],
            'mains': [
                'Examine the literary and cultural contributions of Uttar Pradesh to the development of Hindi and Urdu literature, highlighting Munshi Premchand, Bharatendu Harishchandra, and Amir Khusrau.',
                'Analyze the revolutionary sacrifices of Shahjahanpur martyrs (Ram Prasad Bismil, Ashfaqulla Khan) and Chandra Shekhar Azad in India\'s freedom struggle.',
                'Discuss the contributions of Chaudhary Charan Singh to peasant mobilization, agrarian reforms, and democratic politics in Northern India.'
            ]
        }
    }
}

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

count = 0
for p in d['periods']:
    pid = p['id']
    if pid in UP_AND_REMAINING_ENRICHMENTS:
        enr = UP_AND_REMAINING_ENRICHMENTS[pid]
        if 'aspects' in enr:
            p.setdefault('aspects', {})
            for k, v in enr['aspects'].items():
                p['aspects'][k] = v
        if 'upsc' in enr:
            p['upsc'] = enr['upsc']
        count += 1
        print(f"Successfully enriched UP / Remaining period: {pid}")

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Total UP / remaining periods enriched: {count}")
