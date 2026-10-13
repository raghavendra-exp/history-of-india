import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Detailed enrichment mapping for Ancient Indian History & Archaeology
ANCIENT_ENRICHMENTS = {
    'sources-and-historiography': {
        'aspects': {
            'Archaeological Exploration & Stratigraphy': [
                'Methodological dichotomy: Sir Mortimer Wheeler introduced systematic vertical stratigraphic trenching to establish chronological cultural sequences, contrasting with horizontal excavations utilized to recover comprehensive town layouts (e.g., Harappa, Taxila).',
                'Ceramic horizons as chronological benchmarks: Ochre Coloured Pottery (OCP, c. 2000–1500 BCE; Copper Hoard culture); Black-and-Red Ware (BRW, late Harappan & Megalithic); Painted Grey Ware (PGW, c. 1100–600 BCE; associated with the Later Vedic Gangetic expansion); Northern Black Polished Ware (NBPW, c. 600–200 BCE; glossy luxurious ceramic marking the Second Urbanization and Mauryan empire).'
            ],
            'Epigraphy & Paleography': [
                'Decipherment breakthrough: James Prinsep in 1837 deciphered Ashokan Brahmi and Kharosthi using bilingual Indo-Greek coins, unlocking the Ashokan edicts across the subcontinent.',
                'Major Ashokan epigraphic corpora: 14 Major Rock Edicts (RE XIII detailing the Kalinga War remorse, RE XII preaching religious toleration); 7 Pillar Edicts; Minor Rock Edicts (Maski, Gujarra, Nittur, Udegolam directly naming Ashoka as Devanampiya Piyadassi).',
                'Imperial Prashastis: Harishena\'s Allahabad Pillar Inscription (Prayag Prashasti) in Sanskrit Champu kavya; Ravikirti\'s Aihole Inscription detailing Pulakeshin II\'s defeat of Harsha on the Narmada; Rudradaman I\'s Junagadh Rock Inscription (150 CE, earliest extensive classical Sanskrit inscription recording Sudarshana Lake repairs by governor Suvishakha).'
            ],
            'Numismatics & Economic Indicators': [
                'Punch-Marked Coins (PMC / Karshapana / Pana): 6th–2nd century BCE; silver and copper ingots stamped with solar, tree-in-railing, six-arm, and hill symbols; devoid of royal portraits or inscriptions; standard weight 32 ratis (approx 56 grains).',
                'Indo-Greek coinage: First to introduce portraits of sovereigns and bilingual, bi-scriptural legends (Greek on obverse, Kharosthi on reverse); pioneered gold, silver, and copper dynastic issues.',
                'Kushana & Gupta monetary standards: Vima Kadphises and Kanishka I established heavy gold Dinaras pegged to Roman denarii; Gupta coinage represented the aesthetic zenith with diverse types (Samudragupta\'s Lyrist, Ashvamedha; Chandragupta II\'s Archer, Lion-slayer); post-Gupta gold debasement and scarcity of small copper coinage serve as R.S. Sharma\'s primary index of early medieval monetary contraction and feudalization.'
            ],
            'Foreign Travel Accounts': [
                'Classical Graeco-Roman chronicles: Megasthenes\' Indica (Pataliputra municipal administration across 6 boards of 5 members each; 7-caste division of Indian society); Periplus of the Erythraean Sea (anonymous merchant guide to western and eastern ports: Barygaza/Bharuch, Muziris, Poduke/Arikamedu); Claudius Ptolemy\'s Geographia.',
                'Chinese Buddhist Pilgrims: Faxian (399–414 CE, reign of Chandragupta II; observed civil tranquility, vegetarianism, absence of corporal punishment, flourishing of Pataliputra); Xuanzang (629–645 CE, reign of Harsha; documented Nalanda Mahavihara curriculum under Silabhadra, Kannauj assembly, Prayag almsgiving); Yijing (671–695 CE; meticulous documentation of Buddhist Vinaya monastic rules and medical practices).',
                'Arab Travellers: Al-Biruni\'s Kitab-ul-Hind / Tahqiq-i-Hind (1017–1030 CE; objective analytical study of Indian astronomy, trigonometry, Hindu philosophy, social varna rules, and insular intellectual attitudes).'
            ],
            'Historiographical Schools': [
                'Colonial / Imperialist School: James Mill\'s The History of British India (1817) which instituted the communal tripartite division (Hindu, Muslim, British period); Vincent Smith\'s Early History of India advocating benevolent British despotism as necessary for an intrinsically fractured populace.',
                'Nationalist School: R.G. Bhandarkar, K.P. Jayaswal (Hindu Polity defending ancient Indian representative republics / Gana-Sanghas), R.C. Majumdar celebrating indigenous political resistance and civilizational achievements.',
                'Marxist & Socio-Economic School: D.D. Kosambi (An Introduction to the Study of Indian History, applying historical materialism), R.S. Sharma (Indian Feudalism, urban decay and land grant economy), Romila Thapar (Asoka and the Decline of the Mauryas, structural administrative analyses).',
                'Subaltern & Revisionist Schools: Ranajit Guha emphasizing autonomous peasant and tribal consciousness; B.D. Chattopadhyaya and Hermann Kulke proposing the "Integration Model" of early medieval state formation through local lineage emergence rather than sheer feudal collapse.'
            ]
        },
        'upsc': {
            'prelims': [
                'James Prinsep deciphered Ashokan Brahmi in 1837; Kharosthi is written right-to-left, Brahmi left-to-right; Aramaic and Greek edicts found at Kandahar/Taxila.',
                'Ashoka\'s personal name occurs in only four inscriptions: Maski, Gujarra, Nittur, and Udegolam (all others use "Devanampiya Piyadassi").',
                'Rudradaman I\'s Junagadh Rock Inscription (150 CE) in chaste Sanskrit records the history of Sudarshana Lake built under Chandragupta Maurya (Pushyagupta) and restored under Ashoka (Tushaspha) and Rudradaman (Suvishakha).',
                'Punch-Marked Coins (Pana/Karshapana) carried no ruler names or dates; Indo-Greeks introduced bilingual legends and royal portraits; Kushanas introduced regular high-purity gold dinaras.',
                'NBPW (Northern Black Polished Ware) with its mirror-like lustrous black glaze is the archaeological marker of the Second Urbanization (c. 6th–3rd century BCE).',
                'Megasthenes mentioned that Pataliputra administration was managed by 6 committees of 5 members each, and divided society into 7 occupational classes (philosophers, farmers, soldiers, herdsmen, artisans, magistrates, councillors).',
                'Al-Biruni accompanied Mahmud of Ghazni and authored Kitab-ul-Hind; translated Euclid\'s elements and Patanjali\'s Yoga-Sutra into Arabic.'
            ],
            'mains': [
                'Critically evaluate the significance of epigraphy and numismatics in reconstructing the socio-economic and political history of ancient India in the absence of continuous dynastic chronicles.',
                'Compare and contrast the Imperialist, Nationalist, and Marxist historiographical frameworks with specific reference to the concept of the "Golden Age" and the "Indian Feudalism" debate.',
                'Examine the accounts of Chinese Buddhist travellers (Faxian and Xuanzang) as comparative mirrors of Gupta and Post-Gupta socio-cultural, religious, and economic transitions.',
                'Discuss how advances in archaeological science (pottery typologies, radiocarbon dating, archaeo-metallurgy) have revised traditional textual chronologies of early Indian history.'
            ]
        }
    },
    'prehistoric-age': {
        'aspects': {
            'Palaeolithic Cultures (Pleistocene)': [
                'Lower Palaeolithic (Acheulian culture): Characterized by pebble tools, cleavers, and bifacial handaxes; key sites include Soan Valley (Punjab, Pakistan), Attirampakkam (Tamil Nadu, Robert Bruce Foote 1863), Hunsgi and Isampur (Karnataka), and Singi Talav (Didwana, Rajasthan). Subsistence based on big-game hunting and scavenging.',
                'Middle Palaeolithic (Nevasan industry): Transition to flake-tool industries based on fine-grained stones like chert, jasper, and chalcedony; Nevasa (Maharashtra), Belan Valley (UP), Kalpi (UP).',
                'Upper Palaeolithic: Emergence of blade, burin, and bone tools; ostrich eggshell beads discovered at Patne (Maharashtra); Bhimbetka rock shelters (MP) showing earliest red linear hunting depictions.'
            ],
            'Mesolithic Transition (Holocene)': [
                'Microlithic technology: Geometric stone tools (triangles, trapezes, lunates, scrapers, crescents) measuring 1 to 5 cm, hafted on bone or wood handles to create composite weapons (spears, sickles).',
                'Earliest animal domestication: Confirmed faunal osteological evidence from Bagor (on the Kothari river, Bhilwara, Rajasthan) and Adamgarh (Hoshangabad, MP) dating to c. 5000 BCE (sheep, goats, cattle).',
                'Sedentary burials: Middle Ganga valley sites of Sarai Nahar Rai, Mahadaha, and Damdama (Pratapgarh, UP) revealing extended human burials oriented west-east, microlith grave goods, bone jewellery, hearths, and micro-wear evidence of intensive wild plant foraging.'
            ],
            'Neolithic Revolution & Agriculture': [
                'Gordon Childe\'s concept of "Neolithic Revolution": Shift from food-gathering to food-producing economy; polished ground stone axes (celts), pottery manufacture, and sedentary village life.',
                'Northwestern Oasis: Mehrgarh (Bolan pass, Balochistan c. 7000 BCE) proves indigenous subcontinental transition: Period I (aceramic Neolithic) to Period II (mud-brick granaries, two-row barley, emmer wheat, zebu cattle, sheep domestication).',
                'Kashmir Valley: Burzahom and Gufkral characterized by subterranean pit dwellings, bone harpoons, scrapers, red ochre burials, and animal sacrifices (dogs buried with masters); absence of micro-blades.',
                'Gangetic Valley & Vindhyas: Lahuradewa (Sant Kabir Nagar, UP) yielding cultivated rice grains radiocarbon-dated to c. 7000–6000 BCE; Koldihwa (Belan valley) cord-impressed pottery; Chopani Mando wild-to-cultivated transition.',
                'South Indian Ashmounds: Utnur, Kupgal, Kudatini, Brahmagiri, Paiyampalli; accumulation of calcined cattle dung heaps reflecting seasonal pastoral encampments and cattle pennings; finger millet (ragi) cultivation.'
            ],
            'Chalcolithic Regional Complexes': [
                'Non-urban copper-stone cultures: Ahar-Banas culture (Rajasthan: Gilund, Balathal; copper metallurgy, lack of microliths, white-painted black-and-red ware); Kayatha culture (Chambal basin; sturdy red-slipped ware, cast copper axes); Malwa culture (Navdatoli on Narmada; richest painted ceramic repertoire, broad agricultural basket: wheat, barley, lentils).',
                'Jorwe Culture (Northern Deccan): Inamgaon and Daimabad (Pravara basin); mud-plastered rectangular houses, granaries, irrigation channels; bronze hoard at Daimabad (bronze chariot with driver, buffalo, rhino, elephant).',
                'Social limits & burial practices: North-south adult inhumations under house floors; infant urn burials indicating devastating infantile mortality; copper scarcity preventing hard bronze production; no script; periodic ecological collapses due to aridity.'
            ]
        },
        'upsc': {
            'prelims': [
                'Robert Bruce Foote discovered the first Palaeolithic implement in India (Acheulian handaxe) at Pallavaram / Attirampakkam near Madras in 1863.',
                'Bhimbetka (Madhya Pradesh) in the Vindhyan foothills was discovered by V.S. Wakankar (1957); contains over 700 rock shelters with Upper Palaeolithic, Mesolithic, and historic paintings in red and green pigments.',
                'Earliest archaeological evidence of animal domestication in India comes from Bagor (Rajasthan) and Adamgarh (Madhya Pradesh).',
                'Mehrgarh (Balochistan) presents the earliest evidence of agriculture (wheat and barley) and settled village life in South Asia, dating back to c. 7000 BCE.',
                'Lahuradewa (Sant Kabir Nagar, UP) has provided the earliest radiocarbon evidence of domesticated rice in South Asia (c. 7000–6000 BCE).',
                'Burzahom (Kashmir) is famous for subterranean pit-dwellings, bone tools, and the unique practice of burying domestic dogs with their masters in graves.',
                'The massive bronze chariot with bull, rhinoceros, elephant, and buffalo sculptures was excavated from the Chalcolithic site of Daimabad (Maharashtra).'
            ],
            'mains': [
                'Critically examine Gordon Childe\'s concept of the "Neolithic Revolution" in the light of recent excavations in the Gangetic valley (Lahuradewa) and Balochistan (Mehrgarh).',
                'Trace the evolution of prehistoric rock art in India from the Upper Palaeolithic to the Mesolithic era with special reference to Bhimbetka, highlighting what it reveals about hunting patterns and communal life.',
                'Discuss the regional distribution, socio-economic features, and technological constraints of the Chalcolithic cultures of Central and Western India, explaining why they failed to transition into an urban civilization.',
                'Analyse the ecological and technological factors that governed the transition from mobile hunter-forager bands to sedentary farming communities across the Indian subcontinent.'
            ]
        }
    },
    'indus-valley-civilization': {
        'aspects': {
            'Origins, Chronology & Extent': [
                'Phased developmental trajectory: Pre-Harappan formative stages at Kot Diji, Amri, Sothi-Siswal, and Mehrgarh Period VII; Mature Harappan phase (c. 2600–1900 BCE); Late/Post-Harappan degeneration (Cemetery H, Jhukar, Lustrous Red Ware). Carbon-14 calibrated chronology established by D.P. Agrawal.',
                'Geographical perimeter: Spanned over 1.25 million square kilometres: Sutkagendor (Dasht river, Makran coast, Balochistan) in the West; Alamgirpur (Hindon river, Meerut, UP) in the East; Manda (Chenab river, Akhnoor, Jammu) in the North; Daimabad (Pravara river, Ahmednagar, Maharashtra) in the South; trading outpost at Shortugai (Oxus river, Badakhshan, Afghanistan) for lapis lazuli.'
            ],
            'Town Planning & Hydraulic Engineering': [
                'Gridiron layout & Citadel dichotomy: Towns planned along North-South and East-West thoroughfares intersecting at right angles; Citadel (raised artificial mud-brick acropolis) housing monumental communal structures (Great Bath, Granary, Assembly Hall) and Lower Town containing residential blocks.',
                'Sanitation and drainage network: Underground brick-masonry conduits beneath street pavements, domestic wastewater connected via terracotta chutes and soak-pits, inspection sumps with removable limestone manhole covers for regular de-silting.',
                'Advanced hydraulic achievements: Dholavira (Khadir Bet, Kutch) featured 16 monumental rock-cut water reservoirs, check-dams across Manhar and Mansar channels, and a tripartite layout (Citadel, Middle Town, Lower Town); Lothal had a trapezoidal kiln-burnt brick tidal dockyard connected to the Bhogavo river with a water-sluice mechanism.'
            ],
            'Economy, Weights & Foreign Trade': [
                'Agricultural subsistence: Cultivated wheat, six-row barley, sesamum, mustard, dates, and cotton (termed "Sindon" by Greeks); ploughed field with criss-cross furrows excavated at Kalibangan; terracotta toy plough found at Banawali.',
                'Craft specialisation & metallurgy: Lost-wax casting (Cire-perdue) exemplified by the bronze Dancing Girl of Mohenjo-daro; bead manufacturing factories with specialized copper drills at Chanhudaro and Lothal; steatite micro-beads; shell-working at Balakot and Nageshwar.',
                'Binary-decimal weight system: Cubical chert weights following a binary ratio (1, 2, 4, 8, 16, 32, 64) for lower units (16th unit weighing 13.7 grams) and decimal increments (160, 200, 320, 640) for higher commercial transactions.',
                'Mesopotamian maritime links: Cuneiform inscriptions of King Sargon of Akkad (c. 2350 BCE) record voyages to "Meluhha" (Indus region), "Dilmun" (Bahrain), and "Makan" (Oman); Harappan circular seals and etched carnelian beads discovered at Ur, Kish, and Susa.'
            ],
            'Society, Religion & Script': [
                'Secular urban ethos: Absence of monumental palaces, royal tombs, or standing armies; social stratification evidenced by variable house sizes (single-room workmen barracks vs multi-room double-storey courtyards).',
                'Religious symbolism: Pashupati Seal (seated horned yogic figure surrounded by an elephant, tiger, rhino, buffalo, and twin deer beneath); terracotta female Mother Goddess figurines; phallic stone lingams and yoni rings; pipal tree and unicorn veneration; brick fire altars at Kalibangan and Lothal; dockyard burials with double-inhumation.',
                'Script characteristics: Pictographic script with approx 400 signs, written right-to-left in boustrophedon style (alternating directions); longest inscription (Dholavira signboard) contains 10 signs; remains undeciphered.'
            ],
            'Theories of De-Urbanization': [
                'Multi-causal scientific consensus: Mortimer Wheeler\'s "Aryan invasion" hypothesis (based on skeletons in Mohenjo-daro streets) is scientifically discredited due to chronological mismatch and lack of battlefield trauma.',
                'Ecological and hydrological collapse: Shifting of the monsoon belt and prolonged aridification (c. 2200 BCE 4.2k event); tectonic uplifting diverting the Ghaggar-Hakra (Saraswati) perennial flow into the Yamuna and Indus, causing desiccation of Cholistan and desertion of cities; repeated disastrous floods of the Indus; soil exhaustion and salinization; collapse of Mesopotamian trade networks causing urban de-clustering into rural Chalcolithic agrarian settlements.'
            ]
        },
        'upsc': {
            'prelims': [
                'Dholavira in Gujarat is unique for its tripartite city plan (Citadel, Middle Town, Lower Town), 16 rock-cut water reservoirs, and a 10-symbol wooden signboard.',
                'Lothal in Gujarat contains the world\'s oldest artificial brick tidal dockyard, bead-making kilns, and evidence of double burials.',
                'The ploughed field showing furrow marks at right angles (indicating double-cropping) was discovered at Kalibangan (Rajasthan).',
                'Bronze Dancing Girl from Mohenjo-daro was cast using the lost-wax technique (cire perdue); the Priest-King statue is carved from steatite.',
                'Harappans knew copper, bronze, gold, silver, and lead, but did NOT know iron; horses were generally absent in mature Harappan culture (horse tooth claim at Surkotada remains contested).',
                'In Mesopotamian cuneiform tablets, the Indus region is referred to as "Meluhha", with Bahrain as "Dilmun" and Oman as "Makan".',
                'The earliest evidence of silk in South Asia comes from Harappan beads excavated at Chanhudaro and Nevasa.'
            ],
            'mains': [
                'Analyse the town-planning, sanitation, and hydraulic engineering systems of the Indus Valley Civilization, examining what contemporary Indian cities can learn from their municipal design.',
                'Discuss the maritime and overland trade networks of the Harappan civilization with Mesopotamia and the Persian Gulf, assessing the role of standardized weights, measures, and seals.',
                'Evaluate the various hypotheses regarding the decline of the Indus Valley Civilization. Did the civilization "collapse" or undergo a process of ruralization and transformation?',
                'Examine the religious practices and social structure of the Harappan people in the absence of deciphered textual records, highlighting the significance of terracotta figurines, seals, and cemetery patterns.'
            ]
        }
    },
    'vedic-age': {
        'aspects': {
            'Early Vedic (Rigvedic) Society & Polity': [
                'Pastoral semi-nomadic structure: Pastoral economy centered on cattle (Gau); terms derived from cattle: Gaveshana (quest for cows / war), Godhuma (wheat), Gopa / Gopati (king / protector of cows), Duhitri (daughter / milker of cows). Wealth measured in cattle and horses, not land ownership.',
                'Tribal governance & popular assemblies: Tribal chief (Rajan) aided by the Purohita (priest), Senani (army commander), and Gramani (village head); authority checked by popular assemblies: Sabha (council of elders / elites), Samiti (general tribal assembly that elected the Rajan), Vidatha (tribal assembly with redistributive and religious functions in which women actively participated).',
                'Egalitarian kinship: Division into Kula (family), Grama (village), Vis (clan), and Jana (tribe); flexible occupational varna; women enjoyed high status (Upanayana investiture, participation in assemblies, composing hymns: Lopamudra, Ghosha, Sikata, Apala, Viswavara).'
            ],
            'Later Vedic Transformation & State Formation': [
                'Agrarian transition & Iron technology: Widespread adoption of iron (Krishna Ayas / Shyama Ayas) enabling clearing of thick Gangetic forest cover; expansion from the Sapta-Sindhu eastward into the Kuru-Panchala (Western UP) and Kosala-Videha realms; Painted Grey Ware (PGW) archaeological culture.',
                'Emergence of territorial monarchy: Transformation from tribal Jana to territorial Janapada; royal titles assumed: Samrat, Sarvabhauma, Virat; legitimacy reinforced through grandiose Vedic sacrifices: Ashvamedha (horse sacrifice for imperial sovereignty), Rajasuya (consecration sacrifice conferring supreme divine power), and Vajapeya (chariot race rejuvenating royal vigour).',
                'Bureaucracy & taxation: Regular revenue extraction: Bali (voluntary tribal tribute in Rigveda) became a mandatory tax; Bhaga (king\'s share of agricultural produce, usually 1/6th); collected by Bhagadugha (tax collector) and kept by Sangrahitri (treasurer); decline of Vidatha and exclusion of women from Sabha and Samiti.'
            ],
            'Varna Proliferation & Social Stratification': [
                'Rigid four-fold Varna system: Brahmanas (monopolizing sacrificial rituals), Kshatriyas (ruling nobility and warriors), Vaishyas (commoners, agriculturalists, sole tax-paying class: Anyasya Balikrit), Shudras (serving classes, deprived of Upanayana and Vedic study); Purusha Sukta (Rigveda Mandala X) mythologizing cosmic origin from the Purusha.',
                'Institutionalization of Ashramas: Brahmacharya (student life), Grihastha (householder), Vanaprastha (hermit), and Sannyasa (renunciant); first three mentioned in Chandogya Upanishad, all four fully articulated in Jabala Upanishad.',
                'Subordination of women: Loss of Upanayana rite, child marriage emergence, exclusion from inheritance, depiction as source of sorrow (Aitareya Brahmana); occasional female intellectual figures in philosophical debates (Gargi Vachaknavi and Maitreyi challenging Yajnavalkya in Brihadaranyaka Upanishad).'
            ],
            'Vedic Religion to Upanishadic Monism': [
                'Rigvedic polytheism & anthropomorphic personification: Indra (Purandara - breaker of forts, storm/war god, most hymns: 250), Agni (fire god, intermediary between gods and men: 200 hymns), Varuna (guardian of cosmic moral order - Rta), Soma (god of plants/intoxicating ritual drink), Mitra, Surya, Ushas.',
                'Later Vedic ritual complexity: Prominence of Prajapati (creator), Rudra (god of animals), and Vishnu (preserver); mechanical sacrificial rituals (Yajna) dominated by Brahmana priests demanding massive sacrificial fees (Dakshina).',
                'Upanishadic philosophical revolt: Transition from external animal sacrifice to internal knowledge (Jnana-Marga); central concepts: Brahman (ultimate cosmic reality), Atman (individual immortal soul), Moksha (liberation), Samsara (cycle of rebirth), and Karma; philosophical monism ("Tat Tvam Asi" - That Thou Art in Chandogya Upanishad).'
            ],
            'Vedic Literary Corpus': [
                'Shruti Literature: 4 Vedas (Rigveda - 1028 Suktas in 10 Mandalas; Samaveda - melodies/chants for Udgatri; Yajurveda - prose sacrificial formulas for Adhvaryu, divided into Shukla and Krishna recensions; Atharvaveda - magic spells, charms, and medical lore).',
                'Brahmanas & Aranyakas: Prose theological commentaries explaining ritual mechanics (Aitareya and Kaushitaki for Rigveda; Shatapatha for White Yajurveda; Gopatha for Atharvaveda); Aranyakas ("forest texts") bridging rituals and philosophy.',
                'Upanishads & Vedangas: 108 Upanishads (Mundaka Upanishad giving "Satyameva Jayate", Katha Upanishad dialogue between Nachiketa and Yama); 6 Vedangas (Shiksha - phonetics, Kalpa - ritual code, Vyakarana - grammar, Nirukta - etymology by Yaska, Chhanda - metrics, Jyotisha - astronomy).'
            ]
        },
        'upsc': {
            'prelims': [
                'In the Rigveda, the word "Gau" (cow) is mentioned 176 times; wars were termed "Gaveshana" (search for cows).',
                'The Battle of the Ten Kings (Dasarajna) took place on the banks of the river Parushni (modern Ravi), where King Sudas of the Bharata tribe defeated a confederacy of 10 tribes led by Vishvamitra.',
                '"Satyameva Jayate" (Truth alone triumphs) is taken from the Mundaka Upanishad.',
                'The dialogue between Nachiketa and Yama regarding the nature of the soul and life after death is in the Katha Upanishad.',
                'The Jabala Upanishad is the first text to mention all four Ashramas (Brahmacharya, Grihastha, Vanaprastha, Sannyasa).',
                'In the Later Vedic administration, the Sangrahitri was the royal treasurer and Bhagadugha was the tax collector.',
                'The famous philosophical debate between sage Yajnavalkya and the learned woman Gargi Vachaknavi is recorded in the Brihadaranyaka Upanishad.'
            ],
            'mains': [
                'Trace the socio-economic and political transformation from the Early Vedic pastoral society to the Later Vedic territorial and agrarian polity in the Gangetic basin.',
                'Examine the role of iron technology (Krishna Ayas) and the Painted Grey Ware (PGW) culture in catalyzing the Second Urbanization in ancient India.',
                'Evaluate the philosophical revolt initiated by the Upanishads against the rigid sacrificial ritualism of the Later Vedic Brahmanical religion.',
                'Critically assess the changes in the status, economic rights, and religious participation of women between the Early Vedic and Later Vedic periods.'
            ]
        }
    },
    'age-of-mahajanapadas': {
        'aspects': {
            '16 Mahajanapadas & Magadhan Hegemony': [
                'Geographical horizon: Anguttara Nikaya (Buddhist) and Bhagavati Sutra (Jain) list the 16 Mahajanapadas; stretched from Gandhara/Kamboja in the northwest to Anga in the east and Asmaka/Assaka (on the Godavari) in the south.',
                'Magadhan geographical advantages: Iron ore deposits of Rajgir/Singhbhum providing superior weapons and agricultural clearing tools; fertile alluvial soils of the Middle Ganga enabling immense agrarian surplus; natural water highways (Ganga, Son, Gandak) facilitating commercial and military transport; dense forests supplying wild war-elephants; natural defenses of capitals (Girivraja/Rajgir ringed by 5 hills, Pataliputra as a Jaladurga water fort).',
                'Dynastic expansion: Haryanka Dynasty: Bimbisara (matrimonial alliances with Kosala, Lichchhavis, Madra; conquest of Anga) and Ajatashatru (patron of 1st Buddhist council; invented Rathamusala scythed chariot and Mahashilakantaka catapult; annexed Kosala and Vaishali); Shishunaga Dynasty (annexed Avanti; 2nd Buddhist Council at Vaishali); Nanda Dynasty: Mahapadma Nanda ("Ekarat", "Sarvakshatrantaka" destroyer of Kshatriyas; standing army of 200,000 infantry and 6,000 war-elephants).'
            ],
            'Gana-Sanghas (Oligarchic Republics)': [
                'Structural mechanics of early republics: Gana-Sangha polities like the Vajji confederacy (Lichchhavis of Vaishali) and Mallas of Kusinara/Pava; ruled not by a hereditary monarch but by a clan oligarchic assembly (Santhagara).',
                'Deliberative governance: Decisions passed by voting (Chhanda) using wooden voting sticks (Salakas) overseen by a Salaka-gahapaka; procedural quorum rules; ideological cradle for non-Brahmanical heterodox thinkers (Mahavira was a Jnatrika kshatriya; Buddha was a Shakya prince of Kapilavastu).'
            ],
            'Second Urbanization & Guild Economy': [
                'Economic foundation: Northern Black Polished Ware (NBPW) ceramic horizon; iron share plows generating massive agricultural surplus; emergence of planned fortified cities: Varanasi, Rajgir, Kaushambi, Champa, Ujjain, Shravasti.',
                'Monetisation & merchant guilds: Introduction of silver punch-marked coins (Pana, Karshapana); emergence of wealthy merchant bankers (Sethis / Gahapatis); formation of autonomous craft and merchant guilds (Shrenis) with their own customary laws (Shreni-dharma) and executive heads (Jyetthaka / Pramukha).'
            ],
            'Buddhism: Philosophy & Expansion': [
                'Life of Gautama Buddha: Born at Lumbini (563 BCE), Enlightenment under Bodhi tree at Bodh Gaya, First Sermon (Dharmachakrapravartana) at Sarnath Dear Park, Mahaparinirvana at Kusinara (483 BCE).',
                'Core philosophical tenets: Four Noble Truths (Chatvari Arya Satyani: Dukkha, Samudaya, Nirodha, Magga); Noble Eightfold Path (Ashtangika Marga - Middle Path / Madhyama Pratipada); Pratityasamutpada (Dependent Origination - 12 nidanas / wheel of causal links); Anatta (no immortal soul); Anicca (impermanence); Nirvana (extinction of craving).',
                'Four Buddhist Councils: 1st (483 BCE, Rajgriha, Saptaparni cave, King Ajatashatru, President Mahakassapa; compiled Vinaya Pitaka by Upali, Sutta Pitaka by Ananda); 2nd (383 BCE, Vaishali, King Kalasoka, President Sabakami; schism into Sthaviravadins and Mahasanghikas); 3rd (250 BCE, Pataliputra, King Ashoka, President Moggaliputta Tissa; compiled Abhidhamma Pitaka and Kathavatthu); 4th (72 CE, Kundalvana Kashmir, King Kanishka, President Vasumitra, Vice-President Ashvaghosha; definitive division into Hinayana and Mahayana).'
            ],
            'Jainism: Tenets & Schism': [
                'Vardhamana Mahavira: 24th Tirthankara (born Kundagrama near Vaishali, 540 BCE; Kevala Jnana under Sal tree at Jimbhikagrama; Nirvana at Pavapuri, 468 BCE); incorporated Brahmacharya as the 5th great vow alongside Parshvanatha\'s 4 vows (Ahimsa, Satya, Asteya, Aparigraha).',
                'Epistemology & Metaphysics: Triratna (Right Faith, Right Knowledge, Right Conduct); Anekantavada (doctrine of manifold aspects of reality); Syadvada (theory of conditional / relative predication from 7 standpoints - Saptabhangi Naya); absolute Ahimsa (non-injury extending to all living beings, plants, elements).',
                'Great Schism & Councils: Famine in Magadha (c. 300 BCE) caused Bhadrabahu to migrate south to Shravanabelagola (Karnataka) with Chandragupta Maurya (preserving strict nudity - Digambaras), while Sthulabhadra remained in the North (wearing white robes - Svetambaras); 1st Council at Pataliputra (compiled 12 Angas under Sthulabhadra); 2nd Council at Vallabhi (Gujarat, 512 CE, led by Devardhi Kshamasramana, final canon recorded).'
            ]
        },
        'upsc': {
            'prelims': [
                'The Buddhist text Anguttara Nikaya and the Jain text Bhagavati Sutra provide the canonical list of the 16 Mahajanapadas.',
                'The only Mahajanapada situated south of the Vindhyas on the banks of the Godavari river was Asmaka / Assaka (capital: Potali/Podana).',
                'Ajatashatru used two innovative military siege engines against the Lichchhavis: the Mahashilakantaka (catapult) and Rathamusala (chariot with revolving scythes).',
                'Mahapadma Nanda assumed the titles "Ekarat" (sole sovereign) and "Sarvakshatrantaka" (destroyer of all Kshatriyas).',
                'The First Buddhist Council was held at Rajgriha (Saptaparni cave) immediately after Buddha\'s death, presided over by Mahakassapa and patronized by Ajatashatru.',
                'Pratityasamutpada (Dependent Origination) is the fundamental core of Buddhist philosophy, stating that all phenomena arise in dependence upon causes.',
                'Syadvada (doctrine of "may be" / conditional predication) and Anekantavada (non-absolutism) are distinctive philosophical hallmarks of Jainism.'
            ],
            'mains': [
                'Analyze the geopolitical, economic, and strategic factors that enabled Magadha to establish hegemony over all other Mahajanapadas.',
                'Examine the socio-economic conditions of the 6th century BCE that gave rise to heterodox religions like Buddhism and Jainism, assessing the role of the mercantile class (Sethis) in their patronage.',
                'Compare and contrast the political structure and decision-making processes of the monarchical Mahajanapadas with those of the Gana-Sangha oligarchic republics.',
                'Discuss the four Buddhist Councils in terms of their dates, venues, royal patrons, and ideological contributions to the development of the Buddhist canon and sectarian schisms.'
            ]
        }
    },
    'mauryan-empire': {
        'aspects': {
            'Foundation & Kautilyan Statecraft': [
                'Dynastic foundation: Chandragupta Maurya with Chanakya (Vishnugupta / Kautilya) overthrew Dhanananda (322 BCE); defeated Seleucus I Nicator (305 BCE), gaining the four satrapies of Aria (Herat), Arachosia (Kandahar), Paropamisadae (Kabul), and Gedrosia (Balochistan) in exchange for 500 war elephants; Megasthenes sent as Hellenistic ambassador.',
                'Arthashastra Saptanga State Theory: Organic view of state composed of 7 limbs: 1. Swami (King/Ruler), 2. Amatya (Ministers/Bureaucrats), 3. Janapada (Territory & Population), 4. Durga (Fortified Capital), 5. Kosha (Treasury), 6. Danda / Bala (Army/Coercive power), 7. Mitra (Allies).',
                'Centralized imperial machinery: Mantriparishad (Council of Ministers); Mahamatras (high executive officials); specialized superintendents (Adhyakshas) overseeing 27 state departments: Sitadhyaksha (crown agricultural lands), Pautavadhyaksha (weights and measures), Samsthadhyaksha (market & trade routes), Navadhyaksha (shipping and watercraft), Panyadhyaksha (commerce).'
            ],
            'Fiscal Administration & Taxation': [
                'Chief fiscal architects: Samaharta (Chief Collector-General of Revenue and budget overseer) and Sannidhata (Chief Treasury Officer and custodian of royal storehouses).',
                'Revenue categories: Bhaga (customary state share of agricultural produce, usually 1/6th); Bali (religious or additional levy); Kara (periodical tax on orchards); Visti (unpaid forced labour extracted from artisans and peasants); Shulka (customs toll on traded merchandise); Udakabhaga (water cess / irrigation tax ranging from 1/5th to 1/3rd).'
            ],
            'Pataliputra Municipal Governance (Megasthenes)': [
                'City commission: Municipal administration of Pataliputra governed by an urban council of 30 members divided into 6 boards of 5 members each: 1. Industrial arts & artisan welfare, 2. Foreigners\' registration and welfare, 3. Vital statistics (registration of births and deaths), 4. Trade and commerce (inspection of weights/measures), 5. Manufactured goods and quality control, 6. Tax collection (1/10th tax on sales prices; tax evasion punished with death).',
                'Military board: Army administration overseen by 30 commissioners across 6 military boards: Infantry, Cavalry, War-elephants, Chariots, Navy, and Military transport/logistics.'
            ],
            'Art, Architecture & Monumentality': [
                'Court Art vs Popular Folk Art: Court art sponsored by the imperial state: monolithic polished sandstone pillars (quarried at Chunar, UP) with bell-shaped lotus capitals, abacus, and animal sculptures (Sarnath Lion Capital with Dhammachakka); rock-cut caves for Ajivika monks in Barabar hills (Sudama, Lomas Rishi cave with horseshoe arch).',
                'Popular Folk Art: Individual initiative of local sculptors: colossal freestanding stone statues of Yakshas and Yakshis (Didarganj Yakshi with mirror-like Mauryan polish, Parkham Yaksha, Besnagar Yakshi) representing fertility and folk guardian cults; terracotta figurines.',
                'Monumental brick engineering: Wooden palisade of Pataliputra excavated at Kumrahar with 80-pillar pillared hall; original core of Sanchi Stupa built by Ashoka.'
            ],
            'Decline & Historiographical Explanations': [
                'Haraprasad Sastri\'s thesis: Brahmanical reaction against Ashoka\'s pro-Buddhist patronages and ban on animal sacrifices, culminating in the assassination of Brihadratha by his Senapati Pushyamitra Sunga (185 BCE).',
                'D.D. Kosambi\'s thesis: Severe financial crisis of the Mauryan state caused by maintaining an enormous standing army and top-heavy bureaucracy, evidenced by extensive debasement of late Mauryan punch-marked coins.',
                'Romila Thapar\'s thesis: Structural failure of administrative centralisation without adequate communication lines, absence of a concept of national allegiance, and top-heavy governance dependent entirely on the individual capability of the emperor.',
                'Hemchandra Raychaudhuri\'s thesis: Ashoka\'s pacifist policy of "Dhammavijaya" leading to martial demobilisation and inability to resist Bactrian Greek invasions.'
            ]
        },
        'upsc': {
            'prelims': [
                'According to Kautilya\'s Arthashastra, the Saptanga theory of state comprises Swami, Amatya, Janapada, Durga, Kosha, Danda, and Mitra.',
                'In Mauryan administration, the Sitadhyaksha was the superintendent of crown agricultural lands, Samaharta was the Collector-General of revenue, and Sannidhata was the Chief Treasury Officer.',
                'Megasthenes\' Indica records that the municipal administration of Pataliputra was conducted by 6 committees of 5 members each.',
                'Ashoka built the Lomas Rishi and Sudama rock-cut caves in the Barabar hills (Bihar) specifically for the monks of the Ajivika sect.',
                'The famous polished Didarganj Yakshi statue holding a chauri (fly-whisk) is a masterwork of Mauryan popular folk art.',
                'Pushyamitra Sunga, the Brahmin commander-in-chief, assassinated the last Mauryan ruler Brihadratha in 185 BCE, founding the Sunga dynasty.',
                'The Greek ambassador Heliodorus erected a Garuda pillar at Besnagar (Vidisha) in honour of Vasudeva during the reign of Sunga king Bhagabhadra.'
            ],
            'mains': [
                'Critically evaluate the administrative and fiscal apparatus of the Mauryan Empire as revealed by Kautilya\'s Arthashastra and Megasthenes\' Indica.',
                'Differentiate between Mauryan Court Art and Popular Folk Art with suitable examples, highlighting the technological significance of Chunar sandstone polishing.',
                'Examine the diverse historiographical perspectives on the decline of the Mauryan Empire, assessing whether Ashoka\'s religious policies were responsible for its disintegration.',
                'Discuss Kautilya\'s Saptanga Theory of State and analyze how it integrated territorial defense, economic sovereignty, and diplomatic intelligence.'
            ]
        }
    },
    'ashoka-the-great': {
        'aspects': {
            'Kalinga War & Spiritual Metamorphosis': [
                'Cataclysm of Kalinga (261 BCE): Major Rock Edict XIII explicitly records that 100,000 men were slain, 150,000 carried away captive, and many times that number perished; provoked intense remorse in Ashoka, prompting complete abandonment of Bherighosha (war drum conquest) in favour of Dhammaghosha (conquest by righteousness).',
                'Conversion to Buddhism: Influenced by Upagupta / Nigrodha; became an Upasaka (lay devotee) and later visited the Sangha; performed pilgrimage to Bodh Gaya (Sambodhi) and Lumbini (Rummindei pillar: reduced land revenue from 1/6th to 1/8th and exempted village from Bali in honor of Buddha\'s birthplace).'
            ],
            'Policy of Dhamma: Ethics & Social Harmony': [
                'Non-sectarian moral code: Dhamma was not a dogmatic religious doctrine or personal Buddhism forced on subjects, but an ethical civil code: Ahimsa (non-violence to humans and animals), Satya (truthfulness), Daya (compassion), Dana (generosity), Sushrusa (obedience to parents, teachers, and elders), and proper behaviour towards slaves and servants (Dasa-Bhataka).',
                'Religious toleration: Major Rock Edict XII champions concord among all religious sects (Samavaya eva sadhu), forbidding the praise of one\'s own sect and disparagement of others without genuine cause; state respect for Brahmanas, Sramanas, and Ajivikas alike.',
                'Welfare state measures: Major Rock Edict II records construction of medical facilities (Chikitsa) for humans and animals across India and neighbouring Hellenistic realms (Antiochus II, Ptolemy II, Antigonus Gonatas); planting of medicinal herbs, shade trees (banyan), and digging of wells along highways.'
            ],
            'Administrative Machinery of Dhamma': [
                'Dhamma Mahamattas: Appointed in the 14th regnal year (Major Rock Edict V) as a new cadre of ethical commissioners tasked with propagating Dhamma, mitigating arbitrary prison sentences, inspecting judicial conduct, and ensuring welfare across all communities.',
                'Rajukas & Yuktas: Judicial and revenue district officers; Major Rock Edict IV and Pillar Edict IV granted Rajukas autonomous judicial authority and judicial leniency (3-day reprieve for condemned convicts).',
                'Epigraphic transmission: Engraved across highways and frontiers in 4 distinct languages and scripts: Prakrit in Brahmi script (pan-India); Prakrit in Kharosthi script (Mansehra and Shahbazgarhi, NW); Aramaic and Greek bilingual inscriptions (Kandahar / Shar-i-Kuna, Afghanistan).'
            ],
            'Third Buddhist Council & Global Missions': [
                'Pataliputra Council (c. 250 BCE): Convened at Ashokarama under the presidency of Moggaliputta Tissa to purge heresy from the Sangha; compiled the Kathavatthu (heretical refutations in Abhidhamma Pitaka); promulgated the Schism Edicts (Kausambi, Sanchi, Sarnath) warning monks against splitting the order.',
                'International missionary diplomacy: Dispatched Dutas (envoys) abroad: son Mahendra and daughter Sanghamitra to Sri Lanka (carrying a sapling of the sacred Bodhi Tree); Majjhantika to Kashmir and Gandhara; Mahadharmaraksita to Maharashtra; Sona and Uttara to Suvarnabhumi (Southeast Asia).'
            ]
        },
        'upsc': {
            'prelims': [
                'Ashoka\'s remorse following the Kalinga War and his conversion from Bherighosha to Dhammaghosha is recorded in Major Rock Edict XIII.',
                'Major Rock Edict XII contains Ashoka\'s passionate plea for mutual religious tolerance, declaring that one who honors their own sect by disparaging others harms their own sect.',
                'The Rummindei Pillar Inscription in Nepal marks the exact birthplace of Gautama Buddha; Ashoka exempted Lumbini from Bali tax and reduced Bhaga to 1/8th.',
                'Dhamma Mahamattas were instituted as ethical welfare officers in Ashoka\'s 14th regnal year, as recorded in Major Rock Edict V.',
                'Ashoka\'s bilingual edicts in Greek and Aramaic were discovered at Kandahar (Shar-i-Kuna), Afghanistan.',
                'The Sarnath Lion Capital of Ashoka features four Asiatic lions back-to-back, with four animals on the circular abacus: elephant, galloping horse, bull, and lion separated by wheels (Dharmachakras).',
                'The Bhabru-Bairat rock edict (Rajasthan) explicitly states Ashoka\'s faith in the Buddha, Dhamma, and Sangha.'
            ],
            'mains': [
                'Evaluate the nature and objectives of Ashoka\'s policy of Dhamma. Was it an ethical state ideology aimed at political consolidation or the promotion of Buddhist sectarian faith?',
                'Analyse how Ashoka utilized the epigraphic medium (Rock and Pillar Edicts) across diverse scripts and regions to establish direct communication with his subjects.',
                'Discuss the administrative reforms introduced by Ashoka, specifically focusing on the roles of the Dhamma Mahamattas, Rajukas, and his public welfare infrastructure.',
                'Examine the significance of the Third Buddhist Council at Pataliputra and assess Ashoka\'s contributions to the global dissemination of Buddhism.'
            ]
        }
    },
    'post-mauryan-period': {
        'aspects': {
            'Indigenous Dynasties: Sungas, Kanvas, Satavahanas': [
                'Sunga & Kanva polities: Pushyamitra Sunga (185–151 BCE) revived Vedic sacrificial ceremonies (two Ashvamedha Yajnas celebrated by Patanjali, author of the Mahabhasya); Bharhut Stupa gateway and stone railings built under Sunga patronage; succeeded by Devabhuti and the brief Kanva dynasty (Vasudeva Kanva).',
                'Satavahanas of Deccan (Andhras): Founded by Simuka (capital: Pratishthana/Paithan on Godavari); Gautamiputra Satakarni (r. 106–130 CE) styled himself "Ekabrahmana" and "Kshatriya-darpa-man-mardana", defeating Western Kshatrapa Nahapana (evidenced by Jogalthambi coin hoard where Satakarni restamped Nahapana\'s silver coins); Queen Gautami Balashri\'s Nasik Prashasti.',
                'Nanaghat & Land grants: Queen Nayanika\'s Nanaghat Cave Inscription records the earliest epigraphic evidence in India of tax-exempt royal land grants (with administrative immunities) gifted to Buddhist monks and Brahmanas.'
            ],
            'Foreign Invasions: Indo-Greeks, Shakas, Parthians, Kushanas': [
                'Indo-Greek rulers: Demetrius and Menander I (Milinda, r. 165–145 BCE; capital: Shakala/Sialkot); converted to Buddhism following intellectual dialogue with monk Nagasena, recorded in the Pali text Milindapanha (Questions of King Menander); first rulers to issue gold coins in India and introduce realistic portraiture.',
                'Shakas (Scythians): Established 5 branches (Afghanistan, Punjab, Mathura, Western India, Upper Deccan); Western Kshatrapas: Rudradaman I (r. 130–150 CE; Junagadh inscription, champion of classical Sanskrit literature, repaired Sudarshana Lake without levying extra taxes).',
                'Kushana Empire: Yuezhi clan from Central Asia; Kujula Kadphises (issued copper coins imitating Roman coins); Vima Kadphises (introduced large-scale gold dinaras, devotee of Shiva / Mahesvara); Kanishka I (r. 78 CE, starting the Shaka Era; capitals: Purushapura/Peshawar and Mathura; controlled trans-Eurasian Silk Route extracting lucrative tolls).'
            ],
            'Three Sculptural Schools: Gandhara, Mathura, Amaravati': [
                'Gandhara School: Greco-Roman / Hellenistic influence in north-west (Taxila, Peshawar); material: grey sandstone / stucco; realistic anatomical musculature, curly wavy hair, heavy Greek drapery, wavy Apollo-like facial features, calm contemplative spiritual expression.',
                'Mathura School: Indigenous Indian aesthetic in Uttar Pradesh; material: mottled spotted red sandstone (Sikri); robust fleshy masculine forms, shaved head / ushnisha, transparent clinging drapery, dynamic smiling expression; crafted earliest indigenous images of Buddha, Mahavira, and Hindu deities (Vishnu, Shiva, Surya).',
                'Amaravati School: Indigenous style in Krishna-Godavari valley (Satavahanas and Ikshvakus); material: white marble-like limestone; dynamic narrative relief panels depicting Jataka tales, elongated graceful human limbs, complex crowded compositions full of movement and sensuous vitality.'
            ],
            'Trans-Continental Trade & Roman Commerce': [
                'Monsoon navigation & Indo-Roman trade: Discovery of monsoon trade winds by Hippalus (c. 45 CE) sparked direct voyages across the Arabian Sea; Periplus of the Erythraean Sea details major emporiums: Barygaza (Bharuch), Kalyan, Muziris (Kerala - pepper export), Poduke (Arikamedu near Puducherry, revealing Roman amphorae, Arretine pottery, Roman coins, and dyeing vats).',
                'Pliny\'s lament: Roman historian Pliny the Elder (Natural History) lamented the catastrophic drain of Roman gold to India, calculating that over 50 million sesterces flowed annually into India for luxury commodities like pepper ("black gold" / Yavanapriya), fine muslins, pearls, and tortoiseshell.'
            ],
            'Sangam Age in Deep South (Tamilakam)': [
                'Three crowned kings (Muventar): Cheras (Vanji; emblem: bow; king Senguttuvan / Red Chera founded Pattini cult / chaste Kannagi worship), Cholas (Uraiyur / Puhar-Kaveripattinam; emblem: tiger; Karikala built Grand Anicut / Kallanai on Kaveri), Pandyas (Madurai / Korkai; emblem: fish; patrons of the three Sangams).',
                'Five-fold eco-zones (Aintinai): Kurinji (hills - hunting/gathering; Murugan), Mullai (pastoral forests - herding; Mayon/Vishnu), Marudam (fertile river plains - rice farming; Vendan/Indra), Neydal (coastal sea - fishing/salt; Kadalon/Varuna), Palai (arid desert - robbery; Korravai).',
                'Sangam Literature: Tolkkappiyam (earliest Tamil grammar by Tolkkappiyar); Eight Anthologies (Ettuttokai); Ten Idylls (Pattuppattu); Twin Epics: Silappadikaram (by Ilango Adigal, story of Kovalan, Kannagi, and Madhavi) and Manimekalai (by Sittalai Sattanar, story of Manimekalai\'s renunciation and Buddhist pedagogy).'
            ]
        },
        'upsc': {
            'prelims': [
                'The Shaka Era was initiated by Kushana emperor Kanishka I in 78 CE, which is adopted as the Indian National Calendar.',
                'The Buddhist philosophical dialogue between Indo-Greek king Menander I and monk Nagasena is recorded in the Pali classic Milindapanha.',
                'The earliest epigraphic evidence of tax-free land grants to Brahmanas and Buddhist monks is found in the Nanaghat Cave Inscription of Satavahana Queen Nayanika.',
                'Arikamedu (identified as "Poduke" in the Periplus of the Erythraean Sea) near Puducherry yielded Roman amphorae, Arretine tableware, Roman glass, and rouletted ware.',
                'In Sangam poetry, Roman traders and Westerners were referred to as "Yavanas", and black pepper was termed "Yavanapriya" (dear to Yavanas).',
                'The Pattini cult (veneration of Kannagi as the ideal chaste wife) was established by Chera king Senguttuvan, who brought stone from the Himalayas to carve her idol.',
                'The Jogalthambi hoard discovered in Maharashtra contained over 13,000 silver coins of Western Kshatrapa ruler Nahapana restruck by Satavahana king Gautamiputra Satakarni.'
            ],
            'mains': [
                'Compare and contrast the stylistic, aesthetic, and iconographical features of the Gandhara, Mathura, and Amaravati schools of sculpture.',
                'Discuss the nature and volume of Indo-Roman maritime trade in the Post-Mauryan era, highlighting its impact on Indian monetization, port cities, and social structure.',
                'Analyze the Sangam socio-economic landscape through the prism of the five ecological zones (Tinai), highlighting the literary insights from Ettuttokai and Pattuppattu.',
                'Examine the political and cultural synthesis achieved under the Kushanas, assessing Kanishka\'s role in controlling the Silk Route and convening the Fourth Buddhist Council.'
            ]
        }
    },
    'gupta-age': {
        'aspects': {
            'Imperial Foundation & Military Triumphs': [
                'Rise of the Imperial Guptas: Chandragupta I (r. 319–335 CE) assumed title "Maharajadhiraja", married Lichchhavi princess Kumaradevi (issuing King-Queen coin type), and established the Gupta Era (319–320 CE).',
                'Samudragupta\'s conquests (Prayag Prashasti): Penned by court poet Harishena in ornate Sanskrit champu kavya on the Allahabad pillar; categorized military strategy into 4 distinct regional policies: 1. Prasabhoddharana (violent uprooting and direct annexation of 9 Aryavarta kings like Nagasena, Ganapatinaga), 2. Grahan-Mokshanugraha (capture, liberation, and reinstatement as tributary vassals of 12 Dakshinapatha kings like Mahendra of Kosala, Hastivarman of Vengi), 3. Paricharakikrita (reduction of Atavika / forest kings of central India to servitude), 4. Daivaputra-Shahanushahi, Shaka-Murundas and Simhala (Sri Lanka king Meghavarna sending gifts and tribute). Styled "Kaviraja", "Sarvarajochchetta", and "Napoleon of India" (V.A. Smith).',
                'Chandragupta II Vikramaditya (r. 376–415 CE): Annexed Western Kshatrapas (Shakas) of Malwa and Kathiawar, issuing first Gupta silver coins (Rupaka); matrimonial alliances with Nagas (married Kuberanaga) and Vakatakas (married daughter Prabhavatigupta to Rudrasena II); Navaratnas (Nine Gems) in court: Kalidasa, Amarasimha, Varahamihira, Dhanvantari, Ghatakarpara, Shanku, Kshapanaka, Vararuchi, Vetala Bhatta; visit of Faxian.'
            ],
            'Provincial & Local Administration': [
                'Hierarchical administrative tiers: Empire divided into provinces called Bhuktis (administered by royal governors called Uparikas); Bhuktis divided into districts called Vishayas (headed by Vishayapatis); Vishayas divided into sub-districts called Vithis; lowest administrative tier was the Grama (headed by Gramika and village elders / Grama-vriddhas).',
                'Urban Municipal Councils (Adhisthana-adhikarana): Damodarpur copper plate inscriptions reveal non-official merchant-artisan municipal boards in Bengal assisting the district magistrate: Nagarashreshthi (chief guild merchant of the town), Sarthavaha (leader of travelling merchant caravans), Prathamakulika (chief artisan), and Prathamakayastha (chief of scribe/clerk guild).'
            ],
            'Agrarian Economy, Land Grants & Feudalism Debate': [
                'Land classification: Kshetra (cultivable land), Khila (fallow/uncultivated land), Aprahata (jungle/forest land), Vastu (habitable land), Gapata-sarah (pasture land).',
                'Proliferation of Land Grants: Agrahara grants (perpetual, tax-free land gifted to Brahmana scholars) and Devagrahara (temple endowments); grants transferred not only revenue rights but also judicial jurisdiction (abhyantara-siddhi) and rights over minerals, salt, and peasants; growth of Vishti (unpaid forced labour) and serf-like tied peasantry.',
                'Feudalism Thesis: R.S. Sharma and D.N. Jha argue that royal land grants, combined with the decline of urban craft centres and decay of foreign trade (evidenced by debased late Gupta gold coinage and migration of silk weavers from Lata to Dashapura), laid the structural foundation for "Indian Feudalism" (Samanta system).'
            ],
            'Classical Art, Architecture & Murals': [
                'Nagara temple architecture dawn: Transition from flat-roofed shrines to shikhara temples: Dashavatara Temple at Deogarh (Jhansi/Lalitpur, UP) - earliest complete Panchayatana layout with sanctum, four subsidiary shrines, and monumental Sheshashayi Vishnu and Gajendramoksha relief panels; Bhitargaon brick temple (Kanpur, UP) - earliest preserved brick temple with true arches and curvilinear shikhara; Parvati temple at Nachna Kuthara; Shiva temple at Bhumara.',
                'Ajanta Murals & Sultanganj Buddha: Caves 16, 17, and 19 at Ajanta represent Gupta-Vakataka fresco-secco painting zenith (Dying Princess, Flying Gandharvas, Mother and Child before Buddha); 7.5-foot monumental Sultanganj bronze Buddha (cast via cire-perdue, now in Birmingham Museum); Sarnath seated Buddha preaching the first sermon.'
            ],
            'Golden Age of Literature & Sciences': [
                'Classical Sanskrit literature: Kalidasa (dramas: Abhijnanashakuntalam, Malavikagnimitram, Vikramorvasiyam; mahakavyas: Raghuvamsha, Kumarasambhava; lyric poetry: Meghaduta, Ritusamhara); Vishakhadatta (Mudrarakshasa political intrigue drama, Devichandraguptam); Sudraka (Mrichchhakatika - The Little Clay Cart); Bhasa (Svapnavasavadatta); Bharavi (Kiratarjuniya); Dandin (Kavyadarsha, Dashakumaracharita); Amarasimha (Amarakosha lexicon); Vishnu Sharma (Panchatantra).',
                'Astronomical & Mathematical breakthroughs: Aryabhata (Aryabhatiya, 499 CE; formulated rules for calculating area of triangle, approximation of Pi = 3.1416, Earth\'s diurnal axial rotation, accurate scientific explanation of solar and lunar eclipses); Varahamihira (Panchasiddhantika, Brihat Samhita - encyclopaedia of astronomy, weather, and flora); Brahmagupta (Brahmasphutasiddhanta - operations of zero, negative numbers, and gravity intuition); Vagbhata (Ashtangahridaya in medicine).'
            ]
        },
        'upsc': {
            'prelims': [
                'The Prayag Prashasti (Allahabad Pillar Inscription) was composed in chaste Sanskrit champu style by Harishena, court poet of Samudragupta.',
                'The Dashavatara Temple at Deogarh (Uttar Pradesh) is the earliest known structural temple built on a Panchayatana plan, famous for its Sheshashayi Vishnu sculpture.',
                'The Bhitargaon Temple in Kanpur is the earliest surviving classical brick temple in India featuring a shikhara and true arch construction.',
                'In the Gupta district administration, the municipal council (Adhisthana-adhikarana) included Nagarashreshthi (chief merchant), Sarthavaha (chief caravan merchant), Prathamakulika (chief artisan), and Prathamakayastha (chief scribe).',
                'Aryabhata authored the Aryabhatiya in 499 CE, explaining that the apparent daily motion of the heavens is caused by the rotation of the Earth on its axis.',
                'The iron pillar currently located in the Qutb Complex in Delhi bears an inscription of King Chandra (identified with Chandragupta II), remaining rust-free for over 1600 years.',
                'Prabhavatigupta, daughter of Chandragupta II, ruled as regent of the powerful Vakataka kingdom in the Deccan following the death of Rudrasena II.'
            ],
            'mains': [
                'Critically evaluate the characterisation of the Gupta period as the "Golden Age" of ancient India. Contrast the cultural and scientific achievements with the socio-economic realities of peasant subjection and feudalization.',
                'Analyze the military conquests and diplomatic strategies of Samudragupta as recorded in the Prayag Prashasti, highlighting his differing treatment of Aryavarta and Dakshinapatha rulers.',
                'Discuss the evolution of temple architecture during the Gupta era, tracing the transition from simple flat-roofed shrines to the Panchayatana shikhara temples at Deogarh and Bhitargaon.',
                'Examine the contributions of Aryabhata and Varahamihira to ancient Indian science and mathematics, evaluating their influence on the development of astronomy and scientific thought.'
            ]
        }
    },
    'post-gupta-age': {
        'aspects': {
            'Harshavardhana & The Pushyabhuti Empire': [
                'Ascent & Consolidation: Harsha (r. 606–647 CE) shifted capital from Thaneshwar to Kannauj (Kanyakubja) following the murder of his brother Rajyavardhana and brother-in-law Grahavarman Maukhari by Shashanka of Gauda and Devagupta of Malwa; unified Northern India from Punjab to Bengal.',
                'Defeat by Pulakeshin II: Harsha\'s southward imperial drive into the Deccan was decisively halted on the banks of the Narmada river (c. 618–619 CE) by Chalukya monarch Pulakeshin II, as recorded in the Aihole Inscription authored by court poet Ravikirti; Harsha retained title "Sakalottarapathnatha" (Lord of the Entire North).',
                'Royal assemblies & religious patronage: Patron of Mahayana Buddhism and Shaivism; convened the Kannauj Assembly (643 CE) to honour Xuanzang and celebrate Mahayana supremacy (opposed by disgruntled orthodox Brahmanas who set fire to the assembly tower); convened the quinquennial Prayag Mahamokshaparishad (confluence of Ganga and Yamuna) where he distributed all accumulated royal treasury riches in charity.',
                'Literary accomplishments: Harsha personally authored three classical Sanskrit dramas: Ratnavali, Priyadarsika, and Nagananda (embodying the Bodhisattva ideal of Jimutavahana); patronized Banabhatta (author of Harshacharita - earliest historical biography in Sanskrit, and Kadambari) and Mayura (Mayurashtaka).'
            ],
            'Early Medieval Regional Formations: Chalukyas & Pallavas': [
                'Badami Chalukyas: Founded by Pulakeshin I; zenith under Pulakeshin II (defeated Harsha, Mahendravarman I; exchanged diplomatic embassies with Sassanid Persian King Khosrow II); patrons of rock-cut and structural architecture at Badami, Aihole (temple town: Lad Khan, Durga temple), and Pattadakal (Virupaksha temple built by Queen Lokamahadevi in Dravidian style).',
                'Pallavas of Kanchi: Simhavishnu, Mahendravarman I (Vichitrachitta, author of satirical Sanskrit farce Mattavilasa Prahasana), and Narasimhavarman I Mahamalla (defeated Pulakeshin II, capturing Badami and assuming title "Vatapikonda"); built monolithic rock-cut cave shrines (Mandapas) and monolithic Rathas (Pancha Pandava Rathas) at Mamallapuram / Mahabalipuram, as well as the open-air relief "Descent of the Ganga / Arjuna\'s Penance"; Narasimhavarman II Rajasimha built the Shore Temple at Mahabalipuram and Kailasanatha Temple at Kanchipuram.'
            ],
            'Xuanzang\'s Accounts & Socio-Economic Shifts': [
                'Travelogue (Si-Yu-Ki): Xuanzang spent 16 years in India (629–645 CE); studied Buddhist logic and Yogacara philosophy at Nalanda Mahavihara for 5 years under venerable chancellor Silabhadra; described Nalanda as a residential university housing 10,000 scholars supported by revenues of 100 villages.',
                'Social observations: Observed strict enforcement of caste rules, rise of Untouchability (Chandalas forced to strike a wooden clapper when entering city gates), prevalence of ordeals in criminal justice, decay of historic cities (Pataliputra, Shravasti, Vaishali were largely in ruins), and the rise of Kannauj as the premier political and commercial metropolis of North India.'
            ]
        },
        'upsc': {
            'prelims': [
                'The decisive defeat of Harshavardhana on the banks of the Narmada river by Chalukya king Pulakeshin II is recorded in the Aihole Inscription composed by Ravikirti.',
                'Harshavardhana composed three famous Sanskrit plays: Ratnavali, Priyadarsika, and Nagananda.',
                'The Harshacharita, the earliest surviving formal historical biography in classical Sanskrit literature, was authored by Banabhatta.',
                'The Chinese pilgrim Xuanzang studied Yogacara philosophy at Nalanda University under the guidance of its chancellor, venerable Silabhadra.',
                'Pallava king Narasimhavarman I assumed the title "Vatapikonda" after defeating and killing Pulakeshin II and capturing the Chalukya capital of Vatapi/Badami.',
                'The famous rock-cut relief depicting the "Descent of the Ganga" (or "Arjuna\'s Penance") and the Pancha Rathas were sculpted at Mamallapuram under Pallava patronage.',
                'The Sanskrit satirical farce Mattavilasa Prahasana, mocking corrupt Kapalika, Pashupata, and Buddhist ascetics, was written by Pallava king Mahendravarman I.'
            ],
            'mains': [
                'Assess the political, religious, and literary contributions of Harshavardhana, evaluating whether his reign represented an Indian imperial culmination or a precursor to regional fragmentation.',
                'Trace the long-standing military and cultural rivalry between the Chalukyas of Badami and the Pallavas of Kanchi, analyzing its impact on South Indian temple architecture.',
                'Examine the educational, monastic, and architectural significance of Nalanda Mahavihara as documented in the travelogues of Xuanzang and Yijing.',
                'Discuss the transition of political power from Pataliputra to Kannauj in the post-Gupta era, analyzing the economic and geopolitical factors that made Kannauj the prize of northern India.'
            ]
        }
    }
}

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

count = 0
for p in d['periods']:
    pid = p['id']
    if pid in ANCIENT_ENRICHMENTS:
        enr = ANCIENT_ENRICHMENTS[pid]
        # Merge aspects
        if 'aspects' in enr:
            p.setdefault('aspects', {})
            for k, v in enr['aspects'].items():
                p['aspects'][k] = v
        # Replace / enhance upsc
        if 'upsc' in enr:
            p['upsc'] = enr['upsc']
        count += 1
        print(f"Successfully enriched Ancient period: {pid}")

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Total ancient periods enriched: {count}")
