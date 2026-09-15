# scripts/gen_mains.py
import json

def get_ancient_mains():
    qs = []
    # 40 Ancient Mains Questions
    ancient_data = [
        ("mains_anc_001", "indus-valley-civilization", 15, 250, True, "UPSC CSE 2020 GS-1", "Upinder Singh, Ch. 4; NCERT Class 12 Themes Theme 1",
         "To what extent can the urban planning and drainage architecture of the Indus Valley Civilisation offer practical insights for solving contemporary civic and sanitation challenges in modern Indian cities?",
         "The Indus Valley Civilisation (c. 2600-1900 BCE) represents South Asia's first urbanization, distinguished not by monumental palaces or mortuary grandeur, but by civic hygiene, standardized brick masonry, and egalitarian urban architecture.",
         [
             ("Gridiron Layout & Functional Zoning", ["Segregation of residential quarters from public administrative/craft zones (Citadel vs Lower Town).", "Streets aligned along cardinal directions (North-South, East-West) to utilize natural wind circulation for street cleaning and aeration.", "Relevance: Offers lessons for modern urban master-planning to curb unplanned sprawl and congested ghettos."]),
             ("Underground Drainage & Waste Management", ["Covered masonry wastewater drains running along streets with gradient slopes to prevent stagnation.", "Inspection manholes with removable limestone covers, terracotta soak pits, and grease traps at household outlets.", "Relevance: Contrasts with contemporary open storm gutters prone to clogging, vector-borne epidemics, and urban flooding (e.g., Chennai, Delhi, Mumbai)."]),
             ("Decentralized Water Harvesting & Management", ["Dholavira's cascading stone-cut reservoirs and stormwater bundling systems harvesting seasonal hill runoffs from Manhar and Mansar channels.", "Deep brick-lined public and private wells (over 700 in Mohenjo-daro alone).", "Relevance: Direct blueprint for Jal Jeevan Mission and decentralized rainwater harvesting in climate-stressed arid zones."]),
             ("Standardization & Building Regulations", ["Strict adherence to 4:2:1 brick proportion across thousands of kilometers.", "House entrances opening onto secondary alleys rather than main arterial roads, minimizing noise and vehicular dust."], "Relevance: Demonstrates enforcement of municipal building bye-laws lacking in rapidly urbanizing Indian peri-urban corridors.")
         ],
         "Schematic sketch of Dholavira's tripartite zoning (Castle, Bailey, Middle Town, Lower Town) with encircling reservoir tanks; flowchart of Harappan household soak-pit to municipal street drain system.",
         "Modern initiatives like the Smart Cities Mission and Swachh Bharat Abhiyan essentially strive to recreate the civic priorities and sustainable urban sanitation that Harappan municipal engineers mastered over four millennia ago."),

        ("mains_anc_002", "indus-valley-civilization", 10, 150, True, "UPSC CSE 2018 GS-1", "Upinder Singh, Ch. 4; R.S. Sharma, Ch. 6",
         "The decline of the Harappan civilization was not an abrupt cataclysm but a gradual process of de-urbanization caused by multiple ecological and economic factors. Critically discuss.",
         "Recent archaeological excavations and palaeoclimatic studies have challenged the 20th-century 'Aryan invasion' catastrophe theory, demonstrating that the collapse of Mature Harappa (c. 1900 BCE) was a complex transition termed the 'Late Harappan / Post-Urban phase'.",
         [
             ("Ecological & Climate Shifts", ["Weakening of the Indian Summer Monsoon and progressive desiccation of the Saraswati/Ghaggar-Hakra river system.", "Shifting of river courses and recurrent catastrophic tectonic shifts causing flash floods (evidenced by silt layers at Mohenjo-daro).", "Palaeobotanical evidence indicates deforestation caused by centuries of baking millions of mud bricks and fuelling pottery kilns."]),
             ("Breakdown of Long-Distance Trade Networks", ["Mesopotamian cuneiform records show abrupt cessation of trade references to 'Meluhha' after the reign of Hammurabi.", "Disruption of central procurement of lapis lazuli (Badakhshan), copper (Khetri), and tin severed the economic arteries sustaining urban specialist craft elites."]),
             ("Ruralization & Regional Reorientation", ["De-urbanization did not mean extinction of people; populations migrated eastwards and southwards into the Ganga-Yamuna Doab (Cemetery H, Ochre Coloured Pottery) and Gujarat (Rangpur, Rojdi).", "Loss of the Indus script, standardized weights, and baked bricks, transitioning into decentralized agrarian agro-pastoral village cultures."])
         ],
         "Timeline arrow: Early Harappan (3300-2600 BCE) -> Mature Urban Harappan (2600-1900 BCE) -> Late Harappan Degenerative Phase (1900-1300 BCE) -> Rural Settlements.",
         "Thus, the 'fall' of Harappa is best understood as systemic urban devolution under multi-causal ecological stresses, which reshaped the demographic contours of North India rather than causing a sudden demographic void."),

        ("mains_anc_003", "vedic-age", 15, 250, False, "UPSC CSE Standard Practice", "R.S. Sharma, Ch. 11-12; NCERT Class 11",
         "Examine the profound socio-economic and political transformations between the Early Vedic (Rigvedic) and Later Vedic societies, highlighting how the discovery and use of iron altered the historical trajectory.",
         "The transition from the Early Vedic period (c. 1500-1000 BCE in the Saptasindhu) to the Later Vedic period (c. 1000-600 BCE in the Ganga-Yamuna Doab) marks India's transition from an egalitarian pastoral tribal society to a territorial, stratified, and agrarian polity.",
         [
             ("Agrarian Transformation and the Role of Iron", ["Early Vedic economy was predominantly pastoral; wealth was counted in cattle (Gomat, Gavishti). Agriculture was marginal.", "In the Later Vedic period, the advent of iron ('Shyama Ayas' / 'Krishna Ayas') around 1000 BCE at Atranjikhera enabled deep clearing of dense Gangetic monsoon forests and the manufacture of iron ploughshares.", "Resulted in agricultural surplus, transitioning from shifting pastoralism to sedentary settled village life ('Janapada')."]),
             ("Polity: From Tribal Chiefdoms to Territorial Monarchies", ["Rajan evolved from a pastoral war-chief ('Gopati') without territorial claims into a territorial ruler ('Bhupapati').", "Tribal popular assemblies (Sabha and Samiti), which included women in the Rigveda, lost power to royal lineage and nobility; Vidatha disappeared.", "Introduction of grand legitimizing Vedic sacrifices: Rajasuya (consecration), Ashvamedha (imperial sovereignty), and Vajapeya (chariot race).", "Emergence of embryonic tax collection: Voluntary 'Bali' transformed into compulsory tribute collected by 'Bhagadugha'."]),
             ("Social Stratification and Varna Hierarchy", ["Rigvedic society possessed flexible occupational divisions with egalitarian elements (Purusha Sukta 10th Mandala being a late addition).", "Later Vedic period witnessed the ossification of the fourfold Varna system (Brahmana, Kshatriya, Vaishya, Shudra) governed by strict ritual purity.", "Degradation of the status of women: Loss of Upanayana rites, exclusion from assemblies, and emergence of child marriage and Gotra exogamy."])
         ],
         "Comparative structural table: Early Vedic vs Later Vedic (Polity, Economy, Social Stratification, Role of Women).",
         "The Later Vedic transformations, catalysed by iron metallurgy and agrarian surplus, laid the structural foundations for the emergence of Mahajanapadas and the Second Urbanization in the 6th century BCE."),

        ("mains_anc_004", "age-of-mahajanapadas", 15, 250, True, "UPSC CSE 2016 GS-1", "R.S. Sharma, Ch. 13; Upinder Singh, Ch. 6",
         "The 6th century BCE in northern India witnessed an intense philosophical churning and the rise of heterodox movements. Analyse the socio-economic conditions that facilitated the emergence and popularity of Buddhism and Jainism.",
         "The 6th century BCE represents a pivotal epoch in Indian history characterized by the 'Second Urbanization', the rise of territorial Mahajanapadas, and a profound intellectual revolt against Brahmanical sacrificial orthodoxy, crystallizing in the Shramana traditions of Gautama Buddha and Vardhamana Mahavira.",
         [
             ("Expansion of the Iron Economy and Need for Draught Cattle", ["The clearing of the middle Gangetic plains created intensive plough agriculture demanding heavy animal labour.", "Vedic animal sacrifices (Pashubandha / Gomedha) depleted draught cattle, directly hurting peasant productivity.", "Both Buddhism and Jainism preached Ahimsa (non-injury), directly protecting agrarian livestock assets."]),
             ("Rise of the Mercantile Class (Vaishyas) and Coinage", ["The growth of craft guilds (Shrenis) and trade routes (Uttarapatha) produced a prosperous Vaishya class (Setthis, Gahapatis).", "Brahmanical Dharmasutras condemned sea voyages and denounced money-lending (usury) as sinful.", "Heterodox sects welcomed traders without social stigma, did not condemn usury, and accommodated wealth accumulation based on righteous conduct."]),
             ("Reaction Against Varna Hegemony and Ritual Costs", ["Kshatriya rulers resented the ritual and social superiority claimed by the Brahmana priestly class.", "Both Buddha and Mahavira hailed from Kshatriya aristocratic lineages (Gautama and Jnatrika clans) and challenged the divine origin of Varna based on birth.", "Brahmana rituals were prohibitively expensive and conducted in obscure Sanskrit, whereas Shramana teachers preached in the vernacular (Pali and Ardhamagadhi), democratizing spiritual salvation."]),
             ("Alienation Caused by Urban Life and Material Greed", ["Rapid urbanization, private property disputes, and state coercion in kingdoms generated social alienation and psychological distress.", "The Buddhist Sangha and Jain monastic rules modeled after primitive tribal republics (Ganasanghas) provided a sanctuary of simplicity, communal equality, and detachment."])
         ],
         "Concept map: Socio-Economic Pressures (Agrarian surplus, Cattle preservation, Mercantile wealth, Urban alienation) -> Religious Response (Ahimsa, Vernacular preaching, Sangha equality) -> Rise of Buddhism & Jainism.",
         "Buddhism and Jainism were thus not merely theological movements, but profound socio-economic responses to the material realities of the Second Urbanization, establishing ethical humanism at the core of Indian thought."),

        ("mains_anc_005", "age-of-mahajanapadas", 10, 150, False, "UPSC CSE Standard Practice", "Upinder Singh, Ch. 6; R.S. Sharma, Ch. 12",
         "Differentiate between the monarchical kingdoms (Rajyas) and the non-monarchical republican states (Ganasanghas) of the 6th century BCE in ancient India.",
         "The 6th century BCE witnessed two distinct forms of political organization among the sixteen Mahajanapadas: hereditary monarchies (e.g., Magadha, Kosala, Vatsa) and oligarchic clan republics known as Ganasanghas (e.g., Vrijji confederacy, Licchavis of Vaishali, Shakyas of Kapilavastu).",
         [
             ("Locus of Sovereign Power", ["Rajyas: Power was centralized in a single hereditary monarch whose authority was legitimized by divine ritual consecration (Brahmanical rites).", "Ganasanghas: Sovereignty resided collectively in an assembly of clan oligarchs (Rajas). Decisions were taken through consensus, debate, and majority voting (Chhanda) in the Santhagara."]),
             ("Social Structure and Role of Brahmanism", ["Rajyas: Strictly adhered to the orthodox fourfold Varna hierarchy, giving paramount privilege to Brahmanas and Kshatriyas.", "Ganasanghas: Dominated by a single ruling Kshatriya clan; Brahmanas held minimal political clout. Society was bifurcated into ruling clan members and servile labourers (Dasa-kammakaras)."]),
             ("Military and Fiscal Administration", ["Rajyas: Maintained a permanent standing army (Senabal) paid directly from regular imperial land taxation (Bhaga, Bali) collected by royal officers.", "Ganasanghas: Relied on a militia of armed clan members led by clan chiefs; lacked a bureaucratic standing army, rendering them vulnerable to sustained monarchical siegecraft (as seen in Ajatashatru's 16-year campaign against Vaishali)."])
         ],
         "Venn diagram / Comparative matrix contrasting Rajyas (Monarchy, standing army, Varna orthodoxy) with Ganasanghas (Oligarchy, Santhagara voting, clan militia).",
         "Though the republican Ganasanghas eventually succumbed to the superior centralized resources of Magadha, they bequeathed invaluable democratic and consultative traditions that deeply influenced early Buddhist Sangha governance."),

        ("mains_anc_006", "ashoka-the-great", 15, 250, True, "UPSC CSE 2019 GS-1", "Romila Thapar, Ashoka; Upinder Singh, Ch. 7",
         "Ashoka's policy of 'Dhamma' was neither a sectarian Buddhist doctrine nor a royal whim, but an astute political and moral ideology designed to preserve the unity of a vast, multi-ethnic empire. Critically evaluate.",
         "Following the catastrophic carnage of the Kalinga War (c. 261 BCE), Emperor Ashoka propounded the policy of 'Dhamma' (Dharma). Historian Romila Thapar argues that Ashoka's Dhamma was a universal political philosophy tailored to integrate the heterogenous cultural, linguistic, and religious fault-lines of the sprawling Mauryan subcontinent.",
         [
             ("Universal Ethical Core vs Sectarian Dogma", ["Ashokan Dhamma did not emphasize specific Buddhist dogmatic tenets like the Four Noble Truths, the Eightfold Path, or Nirvana.", "Instead, Major Rock Edicts emphasize universal ethical civic values: filial obedience (Sushrusa), kindness to slaves and servants (Dasa-Bhataka), non-injury to living beings (Ahimsa), and truthfulness.", "Rock Edict XII specifically commands tolerance towards all religious sects (Samavaya - concourse of faiths) and forbids unprovoked slander of other religions."]),
             ("Administrative Integration of a Heterogeneous Empire", ["The Mauryan empire stretched from Kandahar (Greek/Aramaic) to Karnataka (Prakrit) and Bengal, comprising tribal forest populations, agrarian plains, and urban merchants.", "Dhamma served as a secular, overarching civic glue transcending regional dialects and theological dogmas, fostering imperial unity without coercive military suppression.", "Created the cadre of 'Dhamma Mahamattas' (Major Rock Edict V) to inspect royal officials, redress grievances, propagate moral harmony, and supervise welfare among frontier tribes."]),
             ("Foreign Policy: From Bherighosha to Dhammaghosha", ["Major Rock Edict XIII proclaims the abandonment of military aggression (Bherighosha) in favour of cultural and moral conquest (Dhammaghosha).", "Dispatched peace embassies to contemporary Hellenistic kings: Antiochus II of Syria, Ptolemy II of Egypt, Antigonus of Macedonia, and Magas of Cyrene, transforming imperial foreign policy into cultural diplomacy."]),
             ("Limitations and Historical Critiques", ["Scholars like Raychaudhuri argued that pacifism weakened the Mauryan martial apparatus, rendering frontiers vulnerable to Greco-Bactrian invasions.", "However, Ashoka warned forest tribes that the Emperor possessed the power to punish if they transgressed (Major Rock Edict XIII), showing Dhamma was supported by sovereign state authority."])
         ],
         "Flowchart linking Ashokan Dhamma components: Core Ethics (Ahimsa, Tolerance) + Administrative machinery (Dhamma Mahamattas) + Universal outreach (Prakrit/Greek edicts) = Multi-ethnic Subcontinental Imperial Unity.",
         "Ashoka's Dhamma represents an enduring civilizational breakthrough: the pioneering transformation of imperial statecraft from brute conquest into moral governance and pluralistic coexistence."),

        ("mains_anc_007", "mauryan-empire", 15, 250, False, "UPSC CSE Standard Practice", "Upinder Singh, Ch. 7; R.S. Sharma, Ch. 15",
         "Compare the bureaucratic centralization and socio-political apparatus described in Kautilya's Arthashastra with the observations recorded in Megasthenes' Indica.",
         "The Mauryan Empire (c. 322-185 BCE) is one of the best-documented periods in ancient India, with domestic political theory codified in Kautilya's 'Arthashastra' and external eyewitness observations preserved in Megasthenes' 'Indica'.",
         [
             ("Bureaucracy and State Control", ["Arthashastra: Depicts an intensely centralized administrative apparatus. Details 27 'Adhyakshas' (superintendents) regulating everything from agriculture (Sitadhyaksha), mining (Akaradhyaksha), to weights and measures (Pautavadhyaksha). Supported by an omnipresent espionage network (Gudhapurushas).", "Indica: Megasthenes corroborates sophisticated administration by describing a 30-member municipal commission divided into 6 boards of five members each (industries, foreigners, births/deaths, trade, manufacturing, and tax collection) administering Pataliputra, and a similar 30-member board for the military."]),
             ("Social Stratification and Caste Structure", ["Arthashastra: Adheres strictly to orthodox Brahmanical Varna classification (Brahmana, Kshatriya, Vaishya, Shudra) and prescribes legal penalties based on Varna rank.", "Indica: Megasthenes mistakenly identified 7 distinct occupational classes rather than 4 Varnas: Philosophers, Farmers (the largest group), Herdsmen, Artisans/Traders, Soldiers, Overseers/Inspectors, and Councillors/Magistrates. This reflected functional occupational divisions rather than scriptural endogamous Varnas."]),
             ("Condition of Slavery and Exploitation", ["Arthashastra: Recognizes slavery ('Dasa') and specifies detailed legal codes ('Dasa-Kalpa') governing their treatment, rights, manumission, and prohibitions against enslaving free Aryas.", "Indica: Megasthenes famously asserted that 'All Indians are free, and not even one of them is a slave.' He was likely misled because Indian domestic slavery was far less brutal than the dehumanizing Greco-Roman chattel slavery with which he was familiar."]),
             ("Land Ownership and Agrarian Revenue", ["Arthashastra: Recognizes both crown lands managed directly by the state ('Sita') and private peasant holdings assessed for revenue ('Bhaga', typically 1/6th to 1/4th).", "Indica: Megasthenes recorded that all land belonged exclusively to the King, and cultivators worked it for a payment of 1/4th produce, reflecting royal eminent domain."])
         ],
         "Comparative synthesis table: Arthashastra vs Indica on Administration, Class/Varna, Slavery, and Land Rights.",
         "While Kautilya provides the theoretical normative blueprint of a powerful centralized state, Megasthenes offers an external empirical snapshot, together revealing the sophisticated governance of the Mauryan Empire."),

        ("mains_anc_008", "post-mauryan-period", 15, 250, True, "UPSC CSE 2017 GS-1", "Upinder Singh, Ch. 8; R.S. Sharma, Ch. 18",
         "The Post-Mauryan era (c. 200 BCE - 300 CE) was marked by unprecedented integration with the global economy and flourishing internal craft guilds. Evaluate the economic and urban manifestations of this phase.",
         "Often mischaracterized as a period of political fragmentation following the fall of the Mauryas, the Post-Mauryan epoch witnessed a vibrant economic boom, prolific urbanization, thriving craft guilds (Shrenis), and lucrative Indo-Roman maritime and overland trade across the Silk Road.",
         [
             ("Monetization and Proliferation of Coinage", ["Witnessed the highest level of currency monetization in ancient India.", "Indo-Greeks introduced die-struck gold, silver, and copper coins bearing portraits and bilingual legends.", "Kushanas issued magnificent high-purity gold dinaras, while Satavahanas issued lead, potin, and copper coins, facilitating petty daily bazaar transactions."]),
             ("Autonomy and Sophistication of Craft Guilds (Shrenis)", ["Inscriptions at Nasik, Karle, and Junnar reveal guilds operating as autonomous commercial corporations with their own customary laws (Shreni-dharma).", "Guilds acted as primitive commercial banks, accepting fixed interest-bearing deposits (Akshaya-nivi) from royalty and commoners to finance religious endowments and social works.", "Specialized craft production: Ujjain (agate/carnelian beads), Mathura (sculpture and Shataka textiles), Madurai (pearls and muslin)."]),
             ("Maritime Indo-Roman Trade and Balance of Payments", ["Described vividly in the anonymous 1st-century CE Greek navigational guide 'Periplus of the Erythraean Sea' and Pliny's 'Naturalis Historia'.", "Indian ports: Barygaza (Bharuch), Muziris (Kodungallur), Sopara, and Arikamedu (Poduke).", "Exports: Black pepper ('Yavanapriya'), fine muslin, malabathrum, ivory, pearls, and wild animals.", "Imports: Roman gold and silver denarii, amphorae containing wine, and Italian Arretine pottery.", "Roman senator Pliny famously lamented that Rome was drained of over 100 million sesterces annually to satisfy luxury Indian imports."]),
             ("Urban Growth and Thriving Trading Hubs", ["Archaeological excavations demonstrate the zenith of urban habitation (Mathura, Taxila, Ujjain, Paithan, Kaveripattinam, Shishupalgarh) with multi-storeyed burnt-brick buildings, terracotta ring-wells, and soak pits."])
         ],
         "Trade map sketch showing ports (Barygaza, Muziris, Arikamedu), overland Uttarapatha and Dakshinapatha routes, and the monsoon navigation corridor across the Arabian Sea.",
         "The Post-Mauryan economic vitality demonstrated that political decentralization is fully compatible with commercial expansion, cultural cosmopolitanism, and high artistic achievement."),

        ("mains_anc_009", "gupta-empire", 15, 250, True, "UPSC CSE 2021 GS-1", "R.S. Sharma, Ch. 20; Upinder Singh, Ch. 9",
         "The Gupta period has traditionally been hailed as the 'Golden Age' of ancient India. In the light of recent historiography, assess the validity of this characterization.",
         "Colonial and nationalist historians christened the Gupta period (c. 319-550 CE) as the 'Golden Age' or 'Classical Age' of India, pointing to classical Sanskrit literature, artistic achievements, and scientific breakthroughs. Modern critical historiography (e.g., R.S. Sharma, D.N. Jha), however, reveals profound socio-economic contradictions beneath this cultural elite facade.",
         [
             ("Arguments Supporting the 'Golden Age' Paradigm", ["Literary Zenith: Flourishing of classical Sanskrit drama and poetry under Kalidasa (Abhijnanashakuntalam, Meghadutam), Vishakhadatta, and Sudraka.", "Scientific Breakthroughs: Aryabhata's 'Aryabhatiya' (heliocentric hints, calculation of pi, zero/decimal notation, cause of solar/lunar eclipses) and Varahamihira's 'Brihatsamhita' and 'Panchasiddhantika'.", "Metallurgical and Artistic Mastery: The rustless Iron Pillar of Mehrauli; rock-cut cave paintings at Ajanta (Caves 16, 17, 19); sublime Sarnath seated Buddha sculpture reflecting spiritual inwardness.", "Numismatic Splendour: High artistic purity of Gupta gold coins (Dinaras) depicting monarchs playing veena, performing Ashvamedha, and hunting."]),
             ("Contradictions and the Dark Underbelly: Revisionist Historiography", ["Emergence of Feudalism and Subinfeudation: Widespread royal land grants (Agraharas and Brahmadeyas) transferred judicial and administrative rights to priestly donees, weakening central authority and subjecting peasants to forced unpaid labour ('Vishti').", "Decline of Urban Centres and Trade: Excavations show decay in urban centres (Hastinapur, Kaushambi, Shravasti) and cessation of Indo-Roman maritime commerce; minting of poor-quality copper coins reflected reduced monetization for the common populace.", "Social Degradation of Lower Castes: Rigidification of the Varna-Jati framework. Chinese traveller Faxian documented that Chandalas (untouchables) had to strike a wooden clapper when entering city gates to alert caste-Hindus to avoid pollution.", "Subordination of Women: Proliferation of patriarchal restrictions; epigraphic evidence of Sati appears for the first time in the Eran stone pillar inscription of Bhanugupta (510 CE); child marriage and denial of property rights (except Stridhana)."])
         ],
         "Balance scale diagram: Elite Cultural Zenith (Sanskrit, Aryabhata, Ajanta, Gold coins) vs Subaltern Social Realities (Vishti forced labour, Urban decay, Untouchability, Eran Sati).",
         "The Gupta era was undeniably a 'Golden Age' for courtly literature, science, and the artistic elite, but for women, peasants, and the lower Varnas, it marked an era of creeping feudal subjugation and social rigidity."),

        ("mains_anc_010", "harsha-and-his-times", 10, 150, False, "UPSC CSE Standard Practice", "Upinder Singh, Ch. 9; R.S. Sharma, Ch. 21",
         "Harshavardhana's reign (606-647 CE) reflects both the sunset of classical imperial unity and the dawn of early medieval feudal decentralization. Elucidate.",
         "Harshavardhana of Pushyabhuti dynasty united northern India following the Hun invasions, ruling from Kannauj. His reign constitutes a watershed transition from the classical pan-Indian empire to regionalized early medieval feudal polities.",
         [
             ("Sunset of Imperial Authority", ["Harsha revived imperial grandeur through extensive military campaigns across northern India ('Sakalottarapathanatha').", "Patronized literature (composed Ratnavali, Priyadarsika, Nagananda) and convened magnificent grand assemblies at Kannauj and the quinquennial Prayaga assembly observed by Xuanzang.", "Patronized Nalanda Mahavihara, funding it through revenue grants from over 100 villages."]),
             ("Dawn of Feudalization and Decentralization", ["Inability to forge a permanent all-India empire: Decisively defeated on the Narmada banks by Chalukya monarch Pulakeshin II (recorded in Ravikirti's Aihole Prashasti).", "State officials were no longer paid in cash salaries but in assignments of land revenues and villages, accelerating the growth of autonomous 'Samantas' (feudatories).", "Xuanzang observed that law and order was far more precarious than under the Guptas; he was robbed multiple times on imperial highways.", "The empire disintegrated immediately upon Harsha's death (647 CE), giving way to the fragmented Tripartite Struggle."])
         ],
         "Timeline / Conceptual bridge diagram: Centralized Imperial Guptas -> Harsha (Hybrid Transition) -> Early Medieval Feudal Polities (Tripartite Struggle).",
         "Harsha stood as the last great emperor of classical North India; his reliance on feudatory Samantas prefigured the decentralized political landscape of the medieval era."),

        ("mains_anc_011", "sangam-age", 15, 250, True, "UPSC CSE 2015 GS-1", "Upinder Singh, Ch. 8; Nitin Singhania",
         "Sangam literature provides an authentic window into the socio-economic life, ecological diversity, and political contours of early South India. Discuss with reference to the concept of 'Thinai'.",
         "The Sangam corpus (c. 300 BCE - 300 CE), compiled across three literary academies under Pandyan patronage, represents the earliest secular poetic literature of South India, categorized into Akam (internal, love poetry) and Puram (external, heroism and polity).",
         [
             ("The Five Eco-zones ('Ainthinai') and Economic Adaptation", ["The unique concept of 'Thinai' reflects acute ecological consciousness where geographical landscape determined economic subsistence and social habits:", "1. Kurinji (Hilly/Forest): Hunting and honey collection; deity Murugan.", "2. Mullai (Pastoral Scrubland): Animal husbandry and shifting millets; deity Mayon (Krishna).", "3. Marudam (Fertile River Plains): Intensive wet-rice agriculture, tank irrigation; deity Ventan (Indra). Highest social stratification.", "4. Neydal (Coastal/Littoral): Fishing and salt manufacturing (Umanar traders); deity Varunan.", "5. Palai (Parched Arid Wasteland): Highway raiding and banditry; deity Korravai (goddess of war)."]),
             ("Polity: The Muvendar and Heroic Chieftaincies", ["Identifies the three crowned monarchs ('Muvendar'): Cheras (Vanji), Cholas (Uraiyur/Puhar), and Pandyas (Madurai), alongside independent chieftains (Velirs).", "Warfare was endemic, primarily driven by cattle-raids ('Vetchi'). Fallen warriors were consecrated with inscribed Hero Stones ('Nadukal' / 'Virakkal').", "Rulers maintained legitimacy by lavishly redistributing captured booty and gifts to bards (Panar) and poets."]),
             ("Lively Commercial Life and Urban Trading Centres", ["Puhar (Kaveripattinam) is vividly described in 'Silappadikaram' with bustling foreign merchants (Yavanas), harbour docks, and warehouses.", "Flourishing long-distance spice and muslin trade with the Roman Empire; Roman coin hoards discovered at Coimbatore and Madurai."]),
             ("Social Structure: Non-Vedic Roots", ["Absence of rigid North Indian fourfold Varna hierarchy. Status was determined by clan kinship, ecology, and occupation (e.g., Enadi for military chiefs, Vellalas for land-owning farmers, Paraiyar for agricultural labourers).", "Women enjoyed literary freedom; over 30 female poets (notably Avvaiyar, Velli Vithiyar) contributed to the Sangam anthologies."])
         ],
         "Five-column schematic showing the 5 Thinais: Landscape, Subsistence, Deity, and Literary Mood.",
         "Sangam literature stands as a timeless masterpiece of ecological determinism and cultural realism, capturing the vibrant dawn of peninsular Indian civilization."),

        ("mains_anc_012", "kingdoms-of-south", 15, 250, False, "UPSC CSE Standard Practice", "Upinder Singh, Ch. 10; Nitin Singhania, Ch. 1",
         "Analyse the architectural evolution from rock-cut cave shrines to monolithic rathas and structural stone temples under the Pallavas of Kanchi.",
         "The Pallavas of Kanchipuram (c. 6th - 9th centuries CE) laid the foundational architectural vocabulary of South Indian Dravidian temple architecture, progressing sequentially through four distinct evolutionary phases.",
         [
             ("1. Mahendra Style (600-630 CE) - Rock-Cut Excavation", ["Initiated by king Mahendravarman I, proud bearer of the title 'Vichitrachitta' (curious-minded).", "Directly excavated pillared cave temples ('Mandapas') out of living granite bedrock without using brick, mortar, or timber (e.g., Mandagapattu inscription: temple to Brahma, Shiva, and Vishnu).", "Features: Plain massive octagonal pillars with square blocks, simple corbels, and guardian dvarapalas flanking sanctums (e.g., Trichy, Bhairavakonda)."]),
             ("2. Mamalla Style (630-668 CE) - Monolithic Rathas and Open-Air Bas-Reliefs", ["Developed by Narasimhavarman I (Mamalla) at the port city of Mamallapuram (Mahabalipuram).", "Monolithic Free-Standing Sculptured Temples ('Rathas' or Seven Pagodas): Carved top-down from single granite boulders (Dharmaraja, Bhima, Arjuna, Draupadi, Nakula-Sahadeva).", "Features: Slender fluted pillars resting on seated lion bases; embryonic Dravidian tiered Shikharas.", "Grand Open-Air Rock Relief: 'Descent of the Ganga' (or Arjuna's Penance) carved on two massive boulders, celebrating naturalistic animal sculpting (cleft as Ganga with Nagas, elephants, ascetics)."]),
             ("3. Rajasimha Style (700-728 CE) - Advent of Free-Standing Structural Stone Masonry", ["Pioneered by Narasimhavarman II (Rajasimha).", "Shifted definitively from cave excavation to assembling structural stone blocks of granite and sandstone.", "Masterpieces: Shore Temple at Mahabalipuram (facing the Bay of Bengal with tiered vimana) and the Kailasanatha Temple at Kanchipuram.", "Features: Enclosure walls (Prakara), early Gopurams, pyramidal stepped vimanas, and rampart lion pilasters."]),
             ("4. Nandivarman Style (728-900 CE) - Declining Scale and Ornamentation", ["Represented by later Pallavas (Nandivarman II, Aparajita). Small, compact structural temples (e.g., Vaikuntha Perumal at Kanchipuram, Mukteshwara temple).", "Paved the way for the imperial monumentalism of the Cholas."])
         ],
         "Evolutionary timeline flowchart: Mahendra style (Rock-cut Caves) -> Mamalla style (Monolithic Rathas) -> Rajasimha style (Structural Shore/Kailasanatha) -> Imperial Chola Vimanas.",
         "The Pallavas decisively transformed Indian rock into living architectural hymns, establishing the structural DNA that culminated in the colossal temples of Thanjavur and Hampi."),

        ("mains_anc_013", "ancient-religion", 10, 150, False, "UPSC CSE Standard Practice", "Upinder Singh, Ch. 6; NCERT Class 12 Themes Theme 2",
         "Differentiate between the philosophical tenets and monastic codes of early Buddhism (Theravada/Hinayana) and Jainism (Digambara/Svetambara).",
         "Originating in the 6th century BCE Shramana ferment, Buddhism and Jainism rejected Vedic sacrificial ritualism and Varna supremacy, yet diverged fundamentally in their metaphysical doctrines and ascetic rigor.",
         [
             ("Concept of Soul and Material Reality", ["Jainism: Extreme pan-psychic animism. Believes in eternal souls ('Jiva') possessing consciousness present not just in humans and animals, but also in plants, water, fire, and rocks. Matter ('Ajiva') binds the soul through karmic inflow ('Asrava').", "Buddhism: Radical doctrine of 'Anatta' (No-Soul / Non-Self) and 'Anicca' (Impermanence). The self is merely a changing bundle of 5 aggregates (Skandhas). Rebirth occurs through psychological continuity without an immutable transmigrating soul."]),
             ("Ascetic Practice: Extreme Mortification vs Middle Path", ["Jainism: Espouses rigorous self-mortification, extreme penance, and bodily denial to purge accumulated karmic dust ('Nirjara'). Climaxed in Sallekhana (peaceful fasting unto death). Digambara monks renounce even clothing.", "Buddhism: Rejects both hedonistic indulgence and brutal self-torture, championing the 'Majjhima Patipada' (Middle Path) and the Eightfold Path (Ashtangika Marga)."]),
             ("Ahimsa (Non-Violence)", ["Jainism: Absolute, uncompromising Ahimsa. Monks wear mouth-cloths (Muhapatti) and sweep paths with feather whisks to avoid injuring microbes; forbidden from farming due to injury to earthworms.", "Buddhism: Practical and pragmatic Ahimsa; emphasizes compassionate intention (Karuna/Metta). Lay followers and monks were allowed to consume meat if not slaughtered specifically for them."])
         ],
         "Side-by-side comparative table: Metaphysics (Jiva vs Anatta), Ascetic path (Severe Tapas vs Middle Path), Epistemology (Syadvada vs Pratityasamutpada).",
         "While Jainism's absolute asceticism kept it largely concentrated within India's mercantile heartland, Buddhism's pragmatic Middle Path facilitated its rapid pan-Asian transcontinental expansion."),

        ("mains_anc_014", "ancient-science", 10, 150, True, "UPSC CSE 2014 GS-1", "A.L. Basham, The Wonder That Was India; NCERT",
         "Highlight the pioneering contributions of ancient India in the fields of mathematics, astronomy, and medicine.",
         "Ancient Indian scientific enquiry was empirical, rational, and deeply integrated into daily astronomical, architectural, and medicinal needs, generating foundational concepts that influenced global civilization via Arab transmissions.",
         [
             ("Mathematics: The Zero and Decimal System", ["Invention of the symbol Zero ('Shunya') and the base-10 positional place-value decimal system, described by Laplace as an invention of profound genius.", "Aryabhata (5th c. CE): Calculated the value of Pi to 3.1416, solved indeterminate equations, and formulated rules for calculating areas of triangles and volumes of spheres.", "Brahmagupta (7th c. CE): In 'Brahmasphutasiddhanta', codified mathematical arithmetic operations involving zero and negative numbers."]),
             ("Astronomy: Celestial Mechanics", ["Aryabhata posited that the Earth is spherical and rotates on its own axis daily, correctly explaining that solar and lunar eclipses are caused by planetary shadows rather than Rahu/Ketu demons.", "Varahamihira (6th c. CE): Authored 'Panchasiddhantika' and 'Brihatsamhita', synthesizing indigenous knowledge with Greco-Roman (Romaka and Paulisa) astronomical principles."]),
             ("Medicine: Ayurveda and Surgery", ["Charaka Samhita (Charaka): Foundational compendium on internal medicine, pathology, and therapeutics based on the equilibrium of the three humours ('Tridosha': Vata, Pitta, Kapha).", "Sushruta Samhita (Sushruta - Father of Surgery): Detailed over 300 surgical procedures, including rhinoplasty (plastic surgery), cataract removal, lithotomy, and documented 121 surgical instruments."])
         ],
         "Triangular flowchart: Math (Zero, Decimal, Pi) + Astronomy (Earth's rotation, Eclipses) + Medicine (Charaka, Sushruta's surgery) -> Global transmission via Arab scholars (Al-Khwarizmi).",
         "These breakthroughs underline that ancient Indian intellect was as profoundly invested in rational secular sciences as it was in metaphysical philosophy."),

        ("mains_anc_015", "prehistoric-india", 10, 150, False, "UPSC CSE Standard Practice", "Upinder Singh, Ch. 3; NCERT Class 11 An Introduction to Indian Art",
         "Rock art of Bhimbetka offers an authentic visual narrative of the daily life, ecological consciousness, and cognitive evolution of prehistoric humans. Elucidate.",
         "The rock shelters of Bhimbetka (Madhya Pradesh, discovered by V.S. Wakankar in 1957), a UNESCO World Heritage site, preserve continuous artistic strata spanning the Upper Palaeolithic, Mesolithic, and Chalcolithic periods.",
         [
             ("Visual Archive of Daily Subsistence and Economy", ["Mesolithic paintings (the most numerous) depict collective hunting scenes: hunters armed with barbed spears, bows, arrows, and sticks chasing wild beasts.", "Women are depicted gathering wild roots, honeycombing, carrying children in skin baskets, and preparing food, revealing egalitarian gender division of labour.", "Depiction of domestic pastoralism and riding horses/elephants in later Chalcolithic layers."]),
             ("Cognitive and Socio-Cultural Evolution", ["Depiction of communal group dances in synchronized lines holding hands accompanied by drums, marking the birth of ritual celebration and proto-social cohesion.", "Masked human figures, 'horned sorcerers', and funeral rituals indicate emerging spiritual consciousness and shamanistic animism."]),
             ("Artistic Technique and Ecological Palette", ["Natural mineral pigments: Haematite/ochre (Geru) for red, limestone/gypsum for white, copper ore for green, bound using animal fat and tree resins.", "Dynamic stick-like kinetic figures capturing movement with acute anatomical observation of 29 animal species (bison, boars, tigers, rhinos)."])
         ],
         "Sketch diagram representing Mesolithic stick-figure community dancing line and dynamic hunter with bow and arrow.",
         "Bhimbetka's rock art serves not merely as primitive aesthetic expression, but as humanity's earliest visual encyclopedia of survival, social bonding, and artistic impulse.")
    ]

    # Generate additional 25 systematic ancient mains questions (mains_anc_016 to mains_anc_040)
    extra_anc_topics = [
        ("Chalcolithic Cultures of India (Jorwe, Malwa, Ahar-Banas)", "prehistoric-india", 10, 150, False, "NCERT Class 11",
         "Examine the socio-economic characteristics and limitations of non-Harappan Chalcolithic village settlements in Central and Western India.",
         "Non-Harappan Chalcolithic cultures (c. 2000-700 BCE) like Ahar-Banas (Rajasthan), Malwa (Central India), and Jorwe (Maharashtra) represented farming communities using copper and stone simultaneously.",
         [("Subsistence and Settlement Pattern", ["Cultivated wheat, barley, rice, and pulses; domesticated cattle, sheep, and pigs.", "Settlements comprised rectangular or circular wattle-and-daub huts with thatched roofs; Inamgaon featured fortified enclosures and granaries."]),
          ("Crafts and Ceramic Culture", ["Prolific Black-and-Red Ware (BRW) pottery painted with white geometric designs.", "Copper metallurgy practiced using local ores (Khetri for Ahar culture)."]),
          ("Structural Limitations and Demise", ["Inability to smelt iron or produce bronze on a large scale; continued reliance on brittle stone microliths.", "High infant mortality (evidenced by hundreds of children buried in urns under house floors in Jorwe sites) and soil exhaustion led to abandonment around 700 BCE."])],
         "Map locator of key Chalcolithic clusters: Ahar-Banas (Ahar, Balathal), Malwa (Navdatoli), Jorwe (Jorwe, Inamgaon).",
         "Chalcolithic cultures bridged Neolithic agrarianism and the Iron Age, representing rich regional rural traditions alongside the declining Indus valley."),

        ("Ashoka's Pillar Inscriptions vs Rock Edicts", "ashoka-the-great", 10, 150, True, "UPSC CSE 2022 GS-1", "Nitin Singhania, Ch. 1",
         "Differentiate between Ashoka's monolithic stone pillars and Achaemenid (Persian) pillars in terms of design, execution, and ideological purpose.",
         "Ashoka's monolithic pillars represent the zenith of Mauryan court art. While early European scholars posited Persian imitation, critical analysis reveals distinctive indigenous craftsmanship.",
         [("Material and Monolithic Construction", ["Ashokan pillars: Monolithic shafts quarried and chiselled out of a single block of Chunar sandstone.", "Achaemenid pillars: Constructed in multiple segments or drums joined by lead clamps (e.g., Persepolis)."]),
          ("Surface Finish and Bell Capital", ["Ashokan pillars exhibit the lustrous, glass-like 'Mauryan Polish' and stand freely without structural temple supports.", "Achaemenid capitals support palace ceilings; Ashokan capitals support independent sacred animal emblems (Lion, Bull, Elephant, Horse)."]),
          ("Ideological Intent", ["Persian pillars glorified the monarch's autocratic grandeur and military triumphs.", "Ashokan pillars served as moral instruments to propagate ethical Dhamma and civic duty to ordinary subjects across highways."])],
         "Side-by-side structural sketch: Monolithic Ashokan Pillar (Shaft, inverted lotus, abacus, animal crowning capital) vs Achaemenid Segmented Column.",
         "Ashokan pillars synthesized available West Asian decorative idioms into a sovereign, indigenous medium of ethical statecraft."),

        ("Satavahana Dynasty: Bridge between North and South", "post-mauryan-period", 15, 250, False, "Upinder Singh, Ch. 8",
         "Assess the political, agrarian, and cultural contributions of the Satavahana dynasty in peninsular India.",
         "The Satavahanas (c. 1st c. BCE - 3rd c. CE), ruling the Deccan from Pratishthana (Paithan) and Amaravati, acted as the vital geographic and cultural bridge between the Indo-Gangetic plain and the southern peninsula.",
         [("Pioneering Royal Land Grants (Brahmadeya)", ["First rulers in Indian history to issue epigraphically recorded tax-exempt land grants to Buddhist monks and Brahmanas (Nanaghat inscription of Nayanika).", "Inaugurated the process of agrarian expansion into Deccan forests, laying foundations for early Indian feudalism."]),
          ("Matronymics and Social Structure", ["Kings bore names derived from mothers (Gautamiputra Satakarni, Vashishtiputra Pulumayi), reflecting elevated matriarchal respect, though royal succession remained strictly patrilineal.", "Claimed to be 'Ekabrahmana' (peerless Brahmana) who curbed Kshatriya pride while actively patronizing Buddhist rock-cut Chaityas."]),
          ("Trade and Architectural Splendour", ["Controlled lucrative west coast ports (Kalyan, Sopara) and eastern Coromandel trade.", "Patronized the magnificent Amaravati and Guntupalli stupas, and excavated splendid rock-cut Chaityas and Viharas at Karle, Bhaja, and Kanheri."])],
         "Map of Satavahana realm showing Godavari-Krishna basin, trade routes connecting Ujjain to Paithan, and ports.",
         "The Satavahanas integrated peninsular India into subcontinental political and cultural currents, leaving an enduring legacy in art, epigraphy, and agrarian expansion.")
    ]

    # Fill up to 40
    for idx, item in enumerate(ancient_data):
        qs.append({
            "id": item[0],
            "category": "ancient",
            "categoryLabel": "Ancient India",
            "periodId": item[1],
            "marks": item[2],
            "wordLimit": item[3],
            "isPyq": item[4],
            "yearSource": item[5],
            "bookRef": item[6],
            "question": item[7],
            "framework": {
                "intro": item[8],
                "body": [{"heading": h, "points": pts} if isinstance(h, str) else {"heading": h[0], "points": h[1]} for h, pts in (item[9] if isinstance(item[9][0], tuple) else [(b[0], b[1]) for b in item[9]])],
                "diagramMapIdea": item[10],
                "conclusion": item[11]
            }
        })

    # Add systematic remaining to reach 40
    base_ancient_remaining = [
        ("mains_anc_016", "Gupta Golden Age Debate: Agrarian and Subaltern Perspectives", "gupta-empire", 15, 250, True, "UPSC CSE 2021 GS-1", "R.S. Sharma, Ch. 20",
         "Critically examine whether the Gupta period can be justified as a 'Golden Age' from the perspective of agrarian labour and subaltern classes.",
         "While courtly Sanskrit literature and metallurgical mastery flourished, the subaltern classes faced increasing feudal subjugation.",
         [("Proliferation of Vishti (Forced Labour)", ["Peasants were subjected to unpaid labour for royal officials, army movements, and local grantees.", "Agrahara grants alienated royal judicial authority, leaving tillers at the mercy of landed religious donees."]),
          ("Depreciation of Peasant Status", ["Free communal cultivators were reduced to semi-serfs tied to the soil as sharecroppers.", "Increased variety of fiscal levies: Udranga (water/land tax), Uparikara (extra imposts), and Hiranya."]),
          ("Untouchability and Social Exclusion", ["Faxian's observations on Chandalas living outside city gates and striking wooden clappers.", "Codification of rigid caste endogamy and outcaste penalties in Smritis (Narada, Katyayana)."])],
         "Diagram contrasting Courtly Wealth vs Rural Feudal Exploitation.",
         "The golden hue of the Guptas was largely confined to courtly and priestly elites, masking the deepening socio-economic disempowerment of the subaltern peasantry."),

        ("mains_anc_017", "Evolution of Stupa Architecture: From Relic Mound to Monumental Cosmic Symbol", "ancient-religion", 15, 250, True, "UPSC CSE 2013 GS-1", "Nitin Singhania, Ch. 1; NCERT Class 11",
         "Trace the architectural evolution of the Buddhist Stupa from a simple earthen funeral tumulus to a complex cosmic cosmological monument.",
         "Originating as Vedic earthen burial mounds over bodily relics, the Stupa evolved under Buddhist patronage into an elaborate cosmic architectural symbol of the Buddha's Mahaparinirvana.",
         [("Core Structural Components and Symbolism", ["Anda: The semi-spherical dome symbolizing the cosmic egg and the universe.", "Harmika: The square railed balcony atop the Anda representing the abode of the gods.", "Chhatra: Triple umbrella disc representing the Three Jewels (Buddha, Dhamma, Sangha) and spiritual sovereignty.", "Yasti: Central cosmic axis uniting earth and heaven."]),
          ("Circumambulation and Ritual Architecture", ["Pradakshina Patha: Elevated and lower ambulatory pathways for clockwise ritual circumambulation.", "Vedika: Elaborate stone boundary railings demarcating sacred space from the profane world."]),
          ("Decorative Gates: Toranas", ["Four monumental Toranas facing cardinal directions carved with narrative Jataka tales, Yakshas, and floral motifs (Sanchi Stupa 1).", "Transition from Mauryan plain stone to Sunga-Satavahana high-relief narrative carvings."])],
         "Detailed cross-section diagram of a classical Stupa labelling: Anda, Harmika, Chhatra, Yasti, Medhi, Pradakshina Patha, Vedika, and Torana.",
         "The Stupa evolved from a humble mortuary cairn into an enduring architectural synthesis of Buddhist cosmology, artistic narrative, and spiritual contemplation."),

        ("mains_anc_018", "Schools of Ancient Indian Sculpture: Gandhara, Mathura, and Amaravati", "post-mauryan-period", 15, 250, True, "UPSC CSE 2014 GS-1", "Nitin Singhania, Ch. 1; Upinder Singh, Ch. 8",
         "Compare and contrast the Gandhara, Mathura, and Amaravati schools of sculpture with reference to their materials, thematic focus, and philosophical outlook.",
         "The Post-Mauryan era witnessed the flowering of three distinct sculptural idioms that shaped Indian sacred art across the subcontinent.",
         [("Material and Geographic Realm", ["Gandhara: Northwestern frontier (Taxila, Peshawar); utilized grey/blue schist stone and stucco.", "Mathura: Upper Gangetic heartland; used indigenous white-spotted red sandstone.", "Amaravati: Krishna-Godavari basin (Andhra); utilized white marble-like limestone."]),
          ("Stylistic Influences and Iconography", ["Gandhara: Heavy Greco-Roman Hellenistic influence; Buddha depicted with Apollo-like facial features, wavy hair, and heavy folded drapery.", "Mathura: Completely indigenous idiom; Buddha depicted with robust, muscular physique, shaven head, transparent clinging drapery, and peaceful spiritual smile.", "Amaravati: Focus on dynamic narrative panels rather than individual statues; masterly crowd scenes depicting Jataka stories with fluid, sensual human movement."]),
          ("Religious Scope and Patronage", ["Gandhara: Exclusively Mahayana Buddhist; patronized by Kushana monarchs (Kanishka).", "Mathura: Eclectic patronage; produced images of Buddha, Jain Tirthankaras, and Brahmanical deities (Vishnu, Shiva, Kartikeya, Surya).", "Amaravati: Primarily Buddhist; patronized by Satavahanas, Ikshvakus, and wealthy merchant guilds."])],
         "Three-way comparative table across 6 parameters: Stone material, Foreign influence, Buddha facial styling, Drapery, Narrative vs Iconic, Religious patronage.",
         "While Gandhara achieved Hellenistic anatomical realism and Amaravati mastered dynamic narrative composition, Mathura provided the authentic spiritual archetype for pan-Indian classical iconography."),

        ("mains_anc_019", "Nagara vs Dravida Temple Styles", "ancient-art", 15, 250, True, "UPSC CSE 2019 GS-1", "Nitin Singhania, Ch. 2; NCERT Class 11",
         "The Nagara and Dravida styles of temple architecture reflect distinct regional geographical, ritual, and aesthetic traditions. Examine their distinguishing architectural features.",
         "From the 6th century CE onwards, temple architecture in India crystallized into two major classical styles: Nagara in North India and Dravida in South India, with Vesara developing as a hybrid in the Deccan.",
         [("Tower Over Sanctum: Shikhara vs Vimana", ["Nagara: Curvilinear beehive-shaped tower ('Shikhara') that slopes gently inward towards the top, crowned by an Amalaka (stone disc) and Kalasha.", "Dravida: Stepped pyramidal tower ('Vimana') rising geometrically in receding storeys (talas), crowned by an octagonal or circular domical cupola ('Shikhara/Kumbam')."]),
          ("Gateway Architecture and Enclosure Walls", ["Nagara: Generally lacks monumental enclosure walls or elaborate entrance gates; the main temple stands prominently on an elevated stone plinth (Jagati).", "Dravida: Enclosed within colossal boundary walls (Prakara) entered through soaring, ornate gateway towers ('Gopurams') that often dwarf the central Vimana."]),
          ("Water Tanks and Mandapas", ["Nagara: Water reservoirs (Kunds) are typically located outside the sanctum compound or absent.", "Dravida: A sacred water tank (Kalyani / Teerthakulam) inside the temple courtyard is an indispensable ritual component.", "Mandapas: Dravida temples feature pillared halls ('Kalyana Mandapa', 'Nandi Mandapa') and 1000-pillared corridors (Chidambaram, Madurai)."])],
         "Comparative architectural drawing showing Nagara curvilinear Shikhara with Amalaka vs Dravida stepped pyramidal Vimana with Gopuram gateway.",
         "Nagara style emphasizes soaring upward verticality towards heaven, whereas Dravida style creates a self-contained cosmic fortress reflecting institutional temple sovereignty."),

        ("mains_anc_020", "Megasthenes' Observations on Indian Society", "mauryan-empire", 10, 150, False, "UPSC CSE Standard Practice", "Upinder Singh, Ch. 7",
         "Evaluate Megasthenes' account of Mauryan society and state administration. How far does modern archaeology corroborate his assertions?",
         "Megasthenes, the Seleucid ambassador to Chandragupta Maurya's court at Pataliputra, left a detailed memoir 'Indica', preserving invaluable Greek perspectives on 4th-century BCE India.",
         [("Administrative Organization", ["Indica's description of Pataliputra's 30-member municipal commission and military boards is corroborated by the complex bureaucracy described in Kautilya's Arthashastra and Ashokan edicts.", "Excavations at Kumrahar and Bulandibagh revealed massive wooden palisades, ramparts, and an 80-pillared hypostyle hall, verifying Megasthenes' account of Pataliputra's wooden fort."]),
          ("Misunderstandings: Seven Castes and Absence of Slavery", ["Megasthenes categorized society into seven classes based on functional occupation rather than endogamous birth-based Varnas.", "His assertion that slavery was absent in India reflected his familiarity with brutal Greco-Roman chattel slavery; Indian domestic 'Dasa' slavery was more legally protected and socially integrated, making it invisible to him."]),
          ("Absence of Writing and Famine", ["Asserted that Indians did not know the art of writing and that famines never occurred; both refuted by Ashokan rock inscriptions in Brahmi and the Sohgaura copper plate inscription dealing with famine relief."])],
         "Balance chart: Corroborated facts (Wooden palisades, Municipal boards, Army size) vs Foreign Misconceptions (Absence of slavery, 7 castes, no writing).",
         "Despite observational filters of a foreign traveller, Megasthenes provides an indispensable empirical foundation for reconstructing the vibrancy of Mauryan urban civilization.")
    ]

    for item in base_ancient_remaining:
        qs.append({
            "id": item[0],
            "category": "ancient",
            "categoryLabel": "Ancient India",
            "periodId": item[2],
            "marks": item[3],
            "wordLimit": item[4],
            "isPyq": item[5],
            "yearSource": item[6],
            "bookRef": item[7],
            "question": item[1],
            "framework": {
                "intro": item[8],
                "body": [{"heading": b[0], "points": b[1]} for b in item[9]],
                "diagramMapIdea": item[10],
                "conclusion": item[11]
            }
        })

    # Generate questions anc_021 to anc_040 to reach exactly 40 Ancient Mains questions
    anc_topics_list = [
        ("mains_anc_021", "Neolithic Revolution in the Indian Subcontinent (Mehrgarh to Burzahom)", "prehistoric-india", 10, 150, "Upinder Singh, Ch. 3",
         "The Neolithic phase represented a fundamental technological and socio-economic transformation in human prehistory. Discuss with examples from Mehrgarh and Burzahom.",
         "V. Gordon Childe termed the Neolithic transition the 'Neolithic Revolution' because humanity shifted from predatory food gathering to proactive food production, enabling sedentary settlements.",
         [("Mehrgarh: The Pioneer Agrarian Settlement", ["Located on the Bolan River in Balochistan; earliest evidence of settled agriculture (c. 7000 BCE) with multi-room mud-brick granaries.", "Cultivated wheat and barley; domesticated sheep, goats, and zebu cattle."]),
          ("Burzahom: Himalayan Pit-Dwellings and Unique Burials", ["Kashmir valley Neolithic site characterized by subterranean circular pit-dwellings to protect against freezing alpine winds.", "Unique burial practices: Humans buried alongside domesticated dogs and wolves, with grave goods of polished bone and stone tools."]),
          ("Technological Hallmarks", ["Invention of the potter's wheel producing sturdy storage vessels for grain surpluses.", "Polished, ground stone celts and axes for efficient wood-cutting and soil tilling."])],
         "Comparative sketch: Mehrgarh mud-brick granary vs Burzahom pit-dwelling.",
         "The Neolithic revolution established the domestic agrarian foundations that eventually nurtured South Asia's first bronze age urbanization."),

        ("mains_anc_022", "Maritime Trade Networks of the Harappan Civilisation", "indus-valley-civilization", 10, 150, "Upinder Singh, Ch. 4",
         "Assess the archaeological evidence of external maritime trade between the Indus Valley Civilisation and contemporary West Asian civilizations.",
         "The Harappan civilization was not an isolated cultural enclave; it operated extensive maritime trading networks across the Persian Gulf and Arabian Sea connecting to Dilmun, Magan, and Meluhha.",
         [("Lothal: The First Maritime Port", ["Excavation of a massive trapezoidal burnt-brick dockyard (214 m x 36 m) connected via a spillway channel to the tidal waters of the Sabarmati River.", "Presence of an extensive warehouse (bonded storehouse) with seal impressions, and Persian Gulf round button seals."]),
          ("Mesopotamian Epigraphic Corroboration", ["Cuneiform tablets of Sargon of Akkad (c. 2350 BCE) boast of ships from 'Meluhha' (Indus region), 'Magan' (Oman), and 'Dilmun' (Bahrain) mooring at his quays.", "Exports from Meluhha: Carnelian beads, lapis lazuli, timber, copper, and ivory; imports into India: Wool, olive oil, and silver."]),
          ("Archaeological Artefact Distribution", ["Harappan seals, etched carnelian beads, and chert cubical weights discovered at Ur, Kish, Nippur, Susa, and Failaka island."])],
         "Map of ancient maritime trade route: Lothal/Dholavira -> Magan (Oman) -> Dilmun (Bahrain) -> Ur (Mesopotamia).",
         "Harappan maritime mastery demonstrates that ancient India was an early commercial powerhouse integrated into global supply chains."),

        ("mains_anc_023", "Rigvedic Religion: Naturalistic Polytheism to Henotheism", "vedic-age", 10, 150, "R.S. Sharma, Ch. 11",
         "Analyze the evolution of religious thought in the Rigveda from the worship of anthropomorphic forces of nature to embryonic philosophical monism.",
         "Rigvedic religion mirrored the pastoral pastoralist lifestyle of early Aryans, initially deifying dynamic cosmic forces before synthesizing toward philosophical monism.",
         [("Deification of Natural Elements (Naturalistic Polytheism)", ["Indra (Purandara - Breaker of Forts): Rain god and supreme warrior hero, commanding 250 hymns.", "Agni (Fire): Intermediary messenger transmitting offerings from mortals to the celestials, commanding 200 hymns.", "Varuna: Moral guardian of the cosmic order ('Rta') and sovereign of waters."]),
          ("Henotheism (Kathenotheism)", ["Max Müller coined 'Henotheism' to describe the Vedic practice of elevating whichever deity is being addressed to supreme cosmic status at that moment."]),
          ("Evolution into Monism: Nasadiya Sukta", ["The 10th Mandala contains the profound 'Creation Hymn' (Nasadiya Sukta) and Purusha Sukta.", "Proclaims the philosophical climax: 'Ekam Sat Vipra Bahudha Vadanti' (Truth is One, the wise call It by many names), laying the seeds of Upanishadic Vedanta."])],
         "Flowchart: Anthropomorphic Nature Gods -> Henotheism -> Nasadiya Sukta / Upanishadic Monism ('Ekam Sat').",
         "Rigvedic spiritual thought progressed from wonder-filled propitiation of external nature to profound introspection on the unified nature of reality."),

        ("mains_anc_024", "Significance of the Upanishads in Indian Philosophy", "vedic-age", 10, 150, "NCERT Class 12 Themes Theme 2",
         "The Upanishads represent a decisive intellectual revolt against ritualistic Brahmanism. Discuss their central philosophical concepts.",
         "Compiled towards the close of the Later Vedic era (c. 800-500 BCE), the Upanishads ('Vedanta' - end of the Vedas) shifted the focus of religion from external sacrificial rituals to internal spiritual contemplation.",
         [("Rejection of Sacrificial Efficacy", ["The Mundaka Upanishad famously decries Vedic animal sacrifices and rituals as 'frail rafts' (Adridha Naavah) incapable of liberating humans from the cycle of rebirth."]),
          ("Atman and Brahman: Non-Dual Ontology", ["Central identity of the individual soul ('Atman') with the supreme universal cosmic consciousness ('Brahman').", "Expressed in the Mahavakyas: 'Tat Tvam Asi' (That Thou Art - Chandogya) and 'Aham Brahmasmi' (I am Brahman - Brihadaranyaka)."]),
          ("Doctrine of Karma, Samsara, and Moksha", ["Codified the causal theory of Karma: one's actions dictate the nature of future reincarnations ('Samsara').", "Moksha (spiritual liberation) is achieved not through priestly rituals, but through Jnana (self-realization and experiential wisdom)."])],
         "Conceptual triangle: Brahman (Macrocosm) <-> Atman (Microcosm) united through Jnana leading to Moksha.",
         "The Upanishads provided the intellectual backbone of Indian philosophy, inspiring Adi Shankara, Ramanuja, and modern global philosophical thought."),

        ("mains_anc_025", "Factors Responsible for the Rise of Magadha", "age-of-mahajanapadas", 15, 250, "R.S. Sharma, Ch. 12",
         "Explain the geographical, economic, and military factors that enabled the kingdom of Magadha to establish subcontinental hegemony among the sixteen Mahajanapadas.",
         "Between the 6th and 4th centuries BCE, Magadha (under the Haryanka, Shishunaga, Nanda, and Maurya dynasties) outstripped all rival Mahajanapadas to establish India's first subcontinental empire.",
         [("Geographical and Strategic Location of Capitals", ["Rajagriha (Old capital): Impregnably fortified, surrounded by a natural ring of five rocky hills.", "Pataliputra (New capital): Founded at the confluence of the Ganga, Son, and Gandak rivers, functioning as an unassailable water fortress ('Jaladurga') commanding Gangetic riverine communication and commercial tolls."]),
          ("Rich Mineral and Forest Resources", ["Proximity to rich iron-ore deposits in Chotanagpur and Rajgir enabled Magadha to forge superior iron weapons and sturdy forest-clearing implements.", "Dense forests provided heavy timber for fortifications and a plentiful supply of wild war elephants."]),
          ("Pioneering Military Innovations: Elephants and Siege Engines", ["Magadha was the first Indian state to deploy trained war elephants on a massive scale, battering enemy forts and infantry formations.", "Ajatashatru introduced novel military technology against Vaishali: the 'Mahashilakantaka' (catapult launching giant stones) and 'Rathamusala' (scythed chariot with spinning blades)."]),
          ("Fertile Alluvial Soil and Agrarian Surplus", ["Located in the fertile middle Gangetic basin receiving heavy rainfall, yielding rich multiple crop harvests and steady land revenues ('Bhaga') to sustain large standing armies."]),
          ("Dynamic and Ruthless Leadership", ["Visionary and ambitious monarchs: Bimbisara (matrimonial alliances), Ajatashatru (military conquest), and Mahapadma Nanda (eliminating all Kshatriya dynasties as 'Ekarat')."])],
         "Mind map linking 5 Magadhan Pillars: Strategic Capitals, Iron Ore, War Elephants, Gangetic Agriculture, and Ruthless Rulers.",
         "Magadha's physical geography, military technology, and iron resources combined synergistically to transform a regional janapada into India's first subcontinental empire."),

        ("mains_anc_026", "Impact of Alexander's Invasion on India", "age-of-mahajanapadas", 10, 150, "Upinder Singh, Ch. 6",
         "Critically examine the political, economic, and cultural consequences of Alexander the Great's invasion of northwestern India (326 BCE).",
         "Alexander's campaign in the Punjab and Indus valleys in 326 BCE lasted barely nineteen months, yet its historical reverberations influenced Indian politics, trade, and art.",
         [("Political Impact: Paving the Way for Mauryan Imperialism", ["Alexander destroyed the small, fractious tribal principalities and oligarchies in the Punjab (Aspasioi, Assakenoi, Porus' realm).", "This created a political vacuum that Chandragupta Maurya and Chanakya capitalized upon, easily absorbing northwestern India into the unified Mauryan Empire."]),
          ("Direct Overland and Maritime Contact", ["Alexander opened four distinct trade routes by land and sea between Greece and India.", "His admiral Nearchus explored the coastal sea route from the Indus delta to the Persian Gulf, boosting maritime navigation."]),
          ("Cultural Synthesis and Historiography", ["Greek historians accompanying Alexander (Aristobulus, Onesicritus, Nearchus) recorded precise dates and geographical descriptions, providing Indian history with its first verifiable chronological anchor.", "Laid the foundation for long-term Hellenistic cultural interaction, later culminating in Indo-Greek coin portraiture and the Gandhara school of Buddhist sculpture."])],
         "Flowchart: Alexander's campaign -> Subjugation of Punjab chiefdoms -> Political vacuum -> Mauryan territorial consolidation + Hellenistic trade routes.",
         "While Alexander's invasion was a fleeting military storm, it permanently bridged the commercial and artistic worlds of the Mediterranean and the Indian subcontinent."),

        ("mains_anc_027", "Ashoka's Dhamma: Nature, Spread, and Relevance", "ashoka-the-great", 15, 250, "Romila Thapar; NCERT Themes Theme 2",
         "Analyze the institutional mechanism devised by Ashoka to propagate his Dhamma and discuss its contemporary relevance to modern secular and pluralistic governance.",
         "Ashoka's policy of Dhamma was not a mere passive ethical sermon, but an active public policy implemented through specialized administrative machinery and innovative communication.",
         [("Institutional Machinery: The Dhamma Mahamattas", ["Major Rock Edict V records the creation of a brand-new administrative cadre called 'Dhamma Mahamattas' 14 years after his coronation.", "Entrusted with touring the empire, checking high-handedness of district officials, ensuring humane treatment of prisoners, distributing royal charities, and fostering inter-sectarian harmony."]),
          ("Subcontinental Communication in the Vernacular", ["Carved edicts on permanent public rocks, polished pillars, and cave walls along major trade highways and pilgrimage routes.", "Demonstrated acute linguistic sensitivity: used Prakrit in Brahmi script across core territories, Kharosthi in the northwest (Shahbazgarhi), and bilingual Greek and Aramaic in Kandahar."]),
          ("Public Welfare and Animal Care ('Sarvajanahita')", ["Major Rock Edict II details the establishment of botanical hospitals and medicinal herbs for both humans and animals across India and neighbouring Hellenistic kingdoms.", "Banned animal slaughter in the imperial kitchen (Major Rock Edict I) and prohibited the burning of forests."]),
          ("Contemporary Relevance to Democratic Governance", ["Constitutional Secularism (Article 25-28): Resonates with Major Rock Edict XII's call for religious restraint and mutual respect.", "Panchsheel and Peaceful Diplomacy: Direct predecessor of India's non-alignment and ethical foreign policy.", "Animal Welfare & Environmental Ethics (Article 48A / 51A): Precursor of modern environmental conservation and bio-ethics."])],
         "Relevance Matrix: Ashokan Inscription Principle <--> Modern Indian Constitutional / Governance Counterpart.",
         "Ashoka's Dhamma remains one of humanity's finest historic triumphs: an emperor employing sovereign power not to conquer lands, but to conquer hatred, intolerance, and suffering."),

        ("mains_anc_028", "Agrarian Economy under the Mauryan Empire", "mauryan-empire", 10, 150, "R.S. Sharma, Ch. 15",
         "How did the Mauryan state expand and regulate the agrarian frontier? Discuss the role of the 'Sitadhyaksha'.",
         "The Mauryan state was fundamentally an agrarian empire whose colossal military and bureaucratic expenditures were sustained by aggressive state-directed agrarian colonization.",
         [("State Colonization of Virgin Lands ('Janapadanivesha')", ["Kautilya's Arthashastra describes the establishment of new rural settlements by deporting captive populations and inducing Shudra cultivators with tax holidays, cattle, and seeds.", "Clearing state forests to create organized village settlements ('Gramas') under the oversight of royal superintendents."]),
          ("Crown Lands Managed by the 'Sitadhyaksha'", ["Crown lands ('Sita') were managed directly by the Superintendent of Agriculture (Sitadhyaksha).", "Cultivated using state slaves ('Dasa'), hired agricultural labourers ('Karmakaras'), and convicts, generating direct agricultural revenue for the royal treasury."]),
          ("Irrigation and the Sudarshana Lake", ["State constructed and maintained irrigation reservoirs and canals, levying an irrigation cess ('Udaka-bhaga', 1/5th to 1/3rd).", "Pushyagupta, Chandragupta Maurya's governor in Kathiawar (Saurashtra), constructed the famous Sudarshana Lake, later repaired by Ashoka, Rudradaman, and Skandagupta."])],
         "Flowchart: State forest clearance -> Settlement of Shudra peasants -> Sitadhyaksha supervision + Sudarshana irrigation -> Bumper agrarian tax collection.",
         "Through deliberate colonization, public irrigation, and bureaucratic oversight, the Mauryans turned the subcontinent's agrarian potential into imperial strength."),

        ("mains_anc_029", "Shungas and Kanvas: The Brahmanical Revival", "post-mauryan-period", 10, 150, "Upinder Singh, Ch. 8",
         "Examine the socio-political significance of the Shunga and Kanva dynasties following the collapse of the Mauryas.",
         "In 185 BCE, Pushyamitra Shunga assassinated the last Mauryan king Brihadratha, founding the Shunga dynasty and inaugurating a political and cultural revival of Brahmanical traditions.",
         [("Revival of Vedic Sacrifices and Royal Consecration", ["Pushyamitra Shunga, a staunch Brahmana general, performed two grand Ashvamedha (horse sacrifices) at Ayodhya to celebrate victories over Indo-Greek invaders (attested by the Ayodhya inscription of Dhanadeva and Patanjali's Mahabhashya).", "Marked the royal resurgence of sacrificial Brahmanism after over a century of Ashokan heterodox patronage."]),
          ("Artistic Patronage: The Sunga Stupa Enhancements", ["Despite later Buddhist legends portraying Pushyamitra as a persecutor of monks, archaeological evidence shows that major Buddhist stupas (Bharhut, Sanchi) underwent substantial architectural expansion under Shunga rule.", "The plain wooden railings of Sanchi Stupa 1 were replaced with ornate stone railings (Vedikas) and Bharhut's narrative relief sculpture flourished."]),
          ("Codification of Classical Dharmashastras", ["The Shunga-Kanva period is widely regarded as the formative epoch for the redaction of the 'Manusmriti' (Manava Dharmashastra), which codified conservative Brahmanical social norms and Varna hierarchy."])],
         "Timeline: 185 BCE Pushyamitra's coup -> Ayodhya Ashvamedha -> Sanchi/Bharhut stone railings -> Kanva rule.",
         "The Shunga-Kanva era was not an anti-Buddhist dark age, but a dynamic synthesis where Vedic monarchical legitimization coexisted with popular Buddhist artistic patronage."),

        ("mains_anc_030", "Indo-Greeks and Their Cultural Impact on India", "post-mauryan-period", 10, 150, "Upinder Singh, Ch. 8",
         "The Indo-Greek presence in northwestern India catalyzed significant innovations in coinage, literature, and art. Discuss with special reference to King Menander.",
         "Descending from Bactria in the 2nd century BCE, the Indo-Greeks (Yavanas) ruled parts of northwestern India, establishing an enduring legacy of Hellenistic-Indian syncretism.",
         [("King Menander and the Milinda Panha", ["Menander I (Milinda, c. 165-145 BCE), ruling from Sagala (Sialkot), converted to Buddhism after deep philosophical debates with Buddhist sage Nagasena.", "Their dialogues, compiled in the famous Pali text 'Milinda Panha' (Questions of King Milinda), represent an intellectual masterpiece reconciling Greek rationalism with Buddhist metaphysics."]),
          ("Revolution in Indian Coinage", ["Indo-Greeks were the FIRST rulers in Indian history to issue coins that can be definitively attributed to specific kings.", "Introduced die-cast round coins bearing realistic royal portraiture, dynamic action figures, and bilingual inscriptions (Greek on obverse, Prakrit in Kharosthi on reverse)."]),
          ("Origins of Gandhara Art and Astronomy", ["Introduced Hellenistic sculptural techniques, paving the way for the anthropomorphic depiction of the Buddha in Gandhara art.", "Enriched Indian astronomy with astrological concepts (the Greek origin of Sanskrit terms like 'Horashastra' from 'Hora')."])],
         "Coin sketch: Obverse with helmeted portrait of Menander in Greek; Reverse with Athena Alkidemos in Kharosthi script.",
         "The Indo-Greeks exemplified successful cultural assimilation, adopting Indian faiths while enriching Indian artistic and monetary standards."),

        ("mains_anc_031", "Kanishka and the Fourth Buddhist Council", "post-mauryan-period", 10, 150, "Upinder Singh, Ch. 8",
         "Assess the historical significance of Emperor Kanishka I's reign with special focus on the Fourth Buddhist Council and the crystallisation of Mahayana Buddhism.",
         "Kanishka I (c. 78 CE - 120 CE), the greatest Kushana monarch ruling an empire stretching from Central Asia to Pataliputra, played a transformative role in the global spread of Buddhism.",
         [("The Fourth Buddhist Council at Kundalvana (Kashmir)", ["Convened under the presidency of Vasumitra, with scholar-poet Ashvaghosha as vice-president.", "Tasked with codifying authentic Buddhist scriptures, resulting in the monumental commentaries known as the 'Mahavibhasha Sastra' inscribed on copper sheets and deposited in a stupa."]),
          ("The Definitive Schism: Birth of Mahayana Buddhism", ["The Council formalized the theological division between Hinayana (Theravada - orthodox elder tradition) and Mahayana (Great Vehicle).", "Mahayana introduced: Deification of the Buddha as an eternal saviour god, worship of Bodhisattvas (Avalokiteshvara, Manjushri) postponing Nirvana to save humanity, idol-worship, and adoption of Sanskrit instead of Pali."]),
          ("Literary and Cultural Renaissance", ["Kanishka patronized literary giants: Ashvaghosha (composed 'Buddhacharita' and 'Saundarananda'), Nagarjuna (propounded Madhyamaka/Sunyavada philosophy), and Charaka (court physician).", "Erected the colossal 13-storey relic tower at Shah-ji-ki-Dheri in Peshawar."])],
         "Conceptual divide: Theravada (Pali, Individual Arahat, Non-theistic) vs Mahayana (Sanskrit, Compassionate Bodhisattva, Buddha deified).",
         "Kanishka's patronage transformed Buddhism from an Indian monastic movement into a world religion spanning China, Central Asia, and East Asia."),

        ("mains_anc_032", "Samudragupta: The 'Napoleon of India' and His Allahabad Inscription", "gupta-empire", 15, 250, "R.S. Sharma, Ch. 20; Upinder Singh, Ch. 9",
         "Critically examine Samudragupta's military campaigns and imperial policy as recorded in Harishena's Prayag Prashasti (Allahabad Pillar Inscription).",
         "Historian V.A. Smith christened Samudragupta (c. 335-375 CE) the 'Napoleon of India' for his uninterrupted military triumphs recorded with poetic panache by his court poet Harishena on the Ashokan pillar at Prayagraj.",
         [("The Prayag Prashasti: Epigraphic Masterpiece", ["Composed in classical Sanskrit using the 'Champu' style (alternating prose and verse) in Brahmi script.", "Portrays Samudragupta as a warrior bearing the marks of a hundred battle scars, but equally as a poet ('Kaviraja') and skilled Veena musician."]),
          ("Four-Fold Pragmatic Military Policies across Regions", ["1. Aryavarta (Northern India): Policy of 'Prasabhoddharana' (violent extermination and direct territorial annexation); uprooted 9 kings including Nagasena and Achyuta to create a centralized Gupta core.", "2. Dakshinapatha (South India): Policy of 'Grahana-Mokshanugraha' (capture, liberation, and reinstatement as tributary feudatories); defeated 12 kings (including Vishnugopa of Kanchi) but restored their thrones after extracting submission and annual tribute, recognizing the logistical impossibility of administering the Deccan from Pataliputra.", "3. Atavika Rajyas (Forest Kingdoms of Central India): Policy of 'Paricharakikrita' (reduced to bonded servants and pacified).", "4. Frontier States & Foreign Rulers (Samatata, Kamarupa, Shakas, Kushanas): Policy of 'Sarvakaradana-Agyakarana' (paying all tributes and obeying imperial commands) and 'Atmanivedana' (offering personal attendance and daughters in marriage)."]),
          ("Comparison with Napoleon", ["Unlike Napoleon whose career ended in disastrous defeats at Leipzig and Waterloo, Samudragupta was never defeated in battle and celebrated his subcontinental sovereignty with the revival of the Vedic Ashvamedha sacrifice."])],
         "Map schematic of India showing Samudragupta's 4 territorial strategies: Annexed Core (Aryavarta), Tributary Vassals (Dakshinapatha), Border Protectors, and Frontier Allies.",
         "Samudragupta's genius lay in his geopolitical realism: blending direct annexation in the Gangetic plains with autonomous tributary suzerainty in peninsular India."),

        ("mains_anc_033", "Chandragupta II Vikramaditya: Zenith of Gupta Power", "gupta-empire", 10, 150, "Upinder Singh, Ch. 9",
         "Assess the political, matrimonial, and cultural achievements of Chandragupta II 'Vikramaditya'.",
         "Chandragupta II (c. 376-415 CE), assuming the legendary title 'Vikramaditya', brought the Gupta Empire to the zenith of territorial expansion, commercial affluence, and cultural brilliance.",
         [("Strategic Matrimonial Alliances", ["Married princess Kuberanaga of the powerful Naga dynasty of North India.", "Married his daughter Prabhavatigupta to Rudrasena II of the Vakataka dynasty of the Deccan. When Rudrasena died prematurely, Prabhavatigupta served as regent, bringing the Vakataka realm under indirect Gupta hegemony."]),
          ("Conquest of the Western Kshatrapas (Shakas)", ["Annihilated the Western Kshatrapas of Malwa, Gujarat, and Saurashtra (defeating Rudrasimha III).", "Annexed rich western sea ports (Barygaza/Bharuch, Cambay, Sopara), opening lucrative maritime trade with the Western world and issuing silver coins for the first time."]),
          ("The 'Navaratnas' and Cultural Zenith", ["Patronized the legendary 'Nine Gems' (Navaratnas) in his court at Ujjain, including Kalidasa, Varahamihira, Amarasimha, and Dhanvantari.", "Chinese pilgrim Faxian visited during his reign, noting mild criminal punishments, absence of capital punishment, and general prosperity."])],
         "Map of Gupta Empire at its peak showing core northern territory, Vakataka alliance in Deccan, and newly conquered Gujarati ports.",
         "Through military audacity and astute matrimonial diplomacy, Chandragupta II established the golden age of classical Indian imperial statecraft."),

        ("mains_anc_034", "Indian Feudalism: The Historiographical Debate", "early-medieval-period", 15, 250, True, "UPSC CSE 2016 GS-1", "R.S. Sharma, Indian Feudalism; B.D. Chattopadhyaya",
         "Critically examine the 'Indian Feudalism' model propounded by R.S. Sharma. Contrast it with the 'Segmentary State' and 'Integrative' models of the early medieval period.",
         "The nature of the early medieval Indian socio-political order (c. 600-1200 CE) remains one of the most vibrant debates in subcontinental historiography, contested between the Feudalism, Segmentary, and Integrative paradigms.",
         [("R.S. Sharma's 'Indian Feudalism' Paradigm", ["Argues that widespread royal land grants (Brahmadeya and Devadana) from the Gupta period onwards transferred fiscal, judicial, and administrative rights to private beneficiaries.", "Triggered: 1. Political fragmentation and rise of hereditary Samantas; 2. Peasant subjection and forced labour ('Vishti'); 3. Demonetization, urban decay, and decline of foreign trade leading to a self-sufficient, closed village economy."]),
          ("Critiques of the Feudal Model: B.D. Chattopadhyaya's 'Integrative Model'", ["Rejects the thesis of sudden collapse and urban decay.", "Argues that early medieval India witnessed 'lineage-to-state' integration: local tribal chieftains were absorbed into the Kshatriya fold via Rajputization and Agnicula myths.", "Land grants were not instruments of state breakdown, but dynamic mechanisms of agrarian expansion into virgin peripheral forests, generating new rural trade hubs (Mandapikas)."]),
          ("Burton Stein's 'Segmentary State' Model (South India)", ["Borrowed from Aidan Southall's African anthropology and applied to the Chola state.", "Posits that political authority was dual: ritual sovereignty remained with the Chola King at the center, while actual political-administrative power was decentralized across autonomous agrarian localities ('Nadus')."])],
         "Conceptual triangle comparing the three models: Feudalism (Fragmentation & Decay) vs Integrative (Agrarian Expansion & Regional State Formation) vs Segmentary (Ritual Sovereignty & Autonomous Nadus).",
         "Modern scholarship largely views the early medieval era not as a dark age of feudal degeneration, but as a dynamic period of regional agrarian integration, state formation, and cultural proliferation."),

        ("mains_anc_035", "Chola Local Self-Government: Uttaramerur Inscriptions", "imperial-cholas", 15, 250, True, "UPSC CSE 2018 GS-1", "Satish Chandra, Ch. 2; Upinder Singh, Ch. 10",
         "The local self-government institutions under the Imperial Cholas represent a pioneering democratic experiment in ancient India. Analyze with reference to the Uttaramerur inscriptions of Parantaka I.",
         "The Imperial Cholas (9th-12th centuries CE) established a sophisticated system of rural local self-governance, documented in minute operational detail in the two Uttaramerur inscriptions (919 and 921 CE) of Parantaka I in Tamil Nadu.",
         [("Types of Village Assemblies", ["Ur: The general village assembly of tax-paying non-Brahmana landowners.", "Sabha or Mahasabha: The exclusive assembly of Brahmana landowners in tax-free Agrahara/Brahmadeya villages, enjoying sovereign local autonomy.", "Nagaram: Specialized corporate assembly of merchants and artisans regulating marketplace commerce."]),
          ("The Committee System ('Variyams')", ["The Sabha conducted administrative, judicial, and infrastructural work through specialized executive committees called 'Variyams':", "1. Eri-Variyam: Tank and irrigation committee (regulating sluices, water distribution, desilting).", "2. Thotta-Variyam: Garden and horticulture committee.", "3. Pon-Variyam: Gold and fiscal audit committee.", "4. Samvatsara-Variyam: Annual general administrative committee."]),
          ("Democratic Kudavolai Election System and Strict Qualifications", ["Kudavolai (Pot-Ticket) System: Names of qualified candidates were written on palm-leaf tickets, placed inside an earthen pot, and drawn blindly by a young boy.", "Strict Eligibility Criteria: Age (35-70 years), ownership of at least 1/4th Veli of taxable land, residence on own property, and proficiency in Vedic texts and virtuous conduct.", "Disqualifications (Anti-Corruption Norms): Anyone who had served on a committee in the previous 3 years without submitting audited accounts was disqualified, alongside those convicted of heinous crimes, theft, or bribery."])],
         "Flowchart of Chola Sabha governance: Kudavolai drawing -> Selection to 5 Variyams -> Supervised by Royal Amuktamalyada officers.",
         "The Chola Uttaramerur model stands as South Asia's earliest codified constitutional democracy, balancing merit, civic accountability, and decentralized administrative autonomy."),

        ("mains_anc_036", "The Tripartite Struggle: Causes and Consequences", "early-medieval-period", 10, 150, "Satish Chandra, Ch. 1",
         "Analyze the causes and long-term geopolitical consequences of the Tripartite Struggle over Kannauj between the Gurjara-Pratiharas, Palas, and Rashtrakutas.",
         "From the late 8th to the 10th century CE, three major contemporary powers—the Gurjara-Pratiharas (North/West), Palas (Bengal/Bihar), and Rashtrakutas (Deccan)—engaged in a protracted two-hundred-year war for hegemony over Kannauj.",
         [("Symbolic and Geopolitical Value of Kannauj", ["Kannauj, the imperial capital of Harsha, was regarded as the premier seat of subcontinental imperial sovereignty ('Mahodaya-shri'). Whoever held Kannauj claimed the status of Chakravartin.", "Located in the heart of the upper Gangetic plain, commanding fertile agricultural revenues and lucrative commercial trade tolls along the Uttarapatha."]),
          ("Key Phases of the Struggle", ["Vatsaraja (Pratihara) defeated Dharmapala (Pala), only to be routed by Dhruva (Rashtrakuta).", "Later, Nagabhata II and Mihir Bhoja consolidated Pratihara control over Kannauj, but Rashtrakuta raids under Krishna III repeatedly shattered northern stability."]),
          ("Disastrous Long-Term Geopolitical Consequences", ["Exhausted the military, financial, and manpower resources of all three grand empires, accelerating their mutual internal disintegration.", "Left the northwestern gates of India politically fractured and militarily defenseless, paving the way for the devastating invasions of Mahmud of Ghazni in the early 11th century."])],
         "Triangular geopolitical map: Gurjara-Pratiharas (West) <--> Palas (East) <--> Rashtrakutas (Deccan), all arrows pointing at Kannauj.",
         "The Tripartite Struggle proved to be a pyrrhic subcontinental conflict: in their obsession with the prestige of Kannauj, India's three greatest dynasties bled each other to death, inviting foreign conquests."),

        ("mains_anc_037", "Bhakti Movements in South India: Alvars and Nayanars", "ancient-religion", 15, 250, True, "UPSC CSE 2013 GS-1", "NCERT Themes Theme 6; Nitin Singhania",
         "The Alvars and Nayanars of South India transformed medieval Indian religious sensibilities by pioneering emotional egalitarian devotion. Discuss their socio-religious impact.",
         "Between the 6th and 9th centuries CE in Tamil Nadu, the Alvars (12 Vaishnavite saints) and Nayanars (63 Shaivite saints) initiated the historic Bhakti movement, subverting rigid ritualism with intense emotional personal devotion to god.",
         [("Egalitarian Ethos and Defiance of Caste Hierarchy", ["Welcomed saints from every social stratum, including untouchables, hunters, potters, merchants, and kings (e.g., Nayanar saint Nandanar, an outcaste Pulaiya; Tiruppan Alvar, an outcaste musician).", "Challenged the religious exclusivity of Sanskrit-educated Brahmanas, asserting that sincere devotion ('Anbu') transcended birth and Varna rank."]),
          ("Promotion of the Vernacular and Sacred Canons", ["Composed impassioned hymns in vernacular Tamil set to music rather than classical Sanskrit.", "Alvars: Hymns anthologized in the 'Divya Prabandham' (termed the Tamil Veda) by Nathamuni.", "Nayanars: Hymns compiled in the 'Tevaram' (by Nambi Andar Nambi) and the 'Tirumurai', featuring Appar, Sambandar, and Sundarar."]),
          ("Inclusion and Empowerment of Women", ["Female saints broke societal patriarchal shackles: Andal (the only female Alvar) expressed intense bridal mysticism towards Lord Ranganatha.", "Karaikkal Ammeiyar (Nayanar) renounced physical beauty, assumed a skeletal ascetic form, and composed ecstatic hymns to Shiva dancing in cremation grounds."]),
          ("Subversion of Jainism and Buddhism", ["Aggressively displaced the prevailing influence of Jainism and Buddhism in the Tamil country through public debates, miracles, and royal conversions (e.g., Appar converted Pallava king Mahendravarman I from Jainism to Shaivism)."])],
         "Concept web: Alvars/Nayanars -> Vernacular Tamil + Anti-Caste Inclusivity + Women Saints (Andal, Karaikkal) -> Divine Royal Patronage & Temple Culture.",
         "The Alvars and Nayanars democratized divine salvation, birthing the emotional devotional paradigm that subsequently swept northward across medieval India."),

        ("mains_anc_038", "Chalukyas of Badami: Art and Political Legacy", "kingdoms-of-south", 10, 150, "Upinder Singh, Ch. 10",
         "Examine the military and architectural legacy of the Early Chalukyas of Badami (Vatapi), with special reference to Aihole as the 'cradle of temple architecture'.",
         "Ruling the Deccan from Vatapi (Badami) in Karnataka (6th-8th century CE), the Chalukyas forged a powerful trans-peninsular empire and developed the innovative hybrid Vesara architectural style.",
         [("Pulakeshin II and Military Hegemony", ["Greatest monarch Pulakeshin II (610-642 CE); checked the southward march of Harshavardhana on the Narmada banks, assuming the title 'Parameshvara'.", "His court poet Ravikirti authored the poetic Sanskrit Aihole Prashasti on the Meguti Jain temple, recording his military campaigns across the subcontinent."]),
          ("Aihole: The Experimental Cradle of Indian Temple Architecture", ["Aihole hosts over 120 stone temples exhibiting radical experimentation with floor-plans and shikhara profiles.", "Lad Khan Temple: Early cave-like flat-roofed stone hall with pillared porch.", "Durga Temple: Unique apsidal plan derived from Buddhist chaityas with a proto-Nagara curvilinear shikhara and circumambulatory colonnade.", "Huchimalli Gudi: Early temple introducing an antarala (vestibule) connecting sanctum and mandapa."]),
          ("Badami Rock Caves and Pattadakal", ["Badami: Four magnificently sculpted rock-cut cave temples (Cave 3 dedicated to Vishnu featuring cosmic Varaha and Narasimha).", "Pattadakal (UNESCO site): Represents the synthesis of Nagara (Papanatha) and Dravida (Virupaksha built by Queen Lokamahadevi) architectural styles."])],
         "Floor plan sketch of Aihole Durga Temple showing apsidal sanctum and peristyle colonnade.",
         "The Chalukyas established the Deccan as a creative crucible where northern and southern architectural streams converged into majestic stone monuments."),

        ("mains_anc_039", "Rashtrakutas and the Kailasanatha Temple at Ellora", "kingdoms-of-south", 15, 250, True, "UPSC CSE 2020 GS-1", "Nitin Singhania, Ch. 1; Satish Chandra, Ch. 1",
         "The Kailasanatha Temple at Ellora represents an unsurpassed pinnacle of rock-cut monolithic engineering in world art history. Analyze its architectural and sculptural significance.",
         "Commissioned by Rashtrakuta monarch Krishna I (c. 756-773 CE) at Ellora (Cave 16), Maharashtra, the Kailasanatha (Kailash) temple is the world's largest monolithic rock-cut monument, excavated entirely out of a single vertical basalt cliff.",
         [("Monolithic Engineering Feat: Top-Down Excavation", ["Unlike structural temples built bottom-up from stones, Kailasanatha was scooped out 'top-down' from the basalt cliff face using only hammers and chisels.", "Engineers removed an estimated 200,000 tonnes of basalt rock to excavate a pit 100 feet deep, leaving behind a complete free-standing Dravidian multi-storeyed temple."]),
          ("Architectural Components of a Full-Fledged Dravidian Complex", ["Monolithic double-storeyed Gopuram gateway leading into an expansive courtyard.", "Nandi Mandapa connected to the main Vimana via stone rock-cut overhead bridges.", "Soaring Dravidian Vimana rising 96 feet, surrounded by five secondary shrines and circumambulatory cloistered pillared galleries.", "Two life-size monolithic elephants and two monumental 50-foot victory pillars ('Dhwajastambhas') carved directly in the courtyard."]),
          ("Sculptural Grandeur and Narrative Power", ["'Ravana Shaking Mount Kailash': A sculptural masterpiece capturing dramatic kinetic tension. Multi-armed Ravana strains beneath the mountain while Shiva remains unperturbed, soothing Parvati and pinning Ravana with his toe.", "Epic narrative relief panels of the Mahabharata, Ramayana, and Krishna Leela carved along the temple plinth, supported by a colossal frieze of sculpted elephants appearing to carry the entire cosmic temple on their backs."])],
         "Elevation sketch of Kailasanatha Cave 16 showing top-down trench cut, central Vimana, bridge, and Nandi Mandapa.",
         "The Kailasanatha temple remains an incomparable engineering marvel: a monument where royal ambition, religious ecstasy, and geological mastery coalesced into timeless rock."),

        ("mains_anc_040", "Decline of Buddhism in the Land of Its Birth", "ancient-religion", 10, 150, "R.S. Sharma, Ch. 22; Upinder Singh",
         "Analyze the socio-religious and political factors that contributed to the gradual decline and disappearance of Buddhism in early medieval India.",
         "Though Buddhism was born in India and spread across Asia, it experienced a precipitous decline in its subcontinental homeland between the 8th and 12th centuries CE.",
         [("Internal Corruption and Degeneration of Monasteries", ["Monasteries (Mahaviharas) amassed enormous wealth through land grants, disconnecting monks from the common populace.", "Emergence of esoteric Tantric practices (Vajrayana Buddhism) involving occult rituals and esoteric ceremonies eroded its original ethical appeal."]),
          ("Assimilation into Reformed Brahmanism / Hinduism", ["Reformed Hinduism incorporated core Buddhist principles: adopting Ahimsa, building monasteries (Mathas by Adi Shankara), and assimilating the Buddha as the 9th avatar of Lord Vishnu.", "Adi Shankara and Kumarila Bhatta philosophically outmanoeuvred Buddhist scholars in public theological disputations."]),
          ("Loss of Royal Patronage", ["Following the fall of the Palas of Bengal (the last great Buddhist patrons), newly emerging Rajput dynasties favoured martial Shaivism, Vaishnavism, and Brahmanical sacrificial legitimacy."]),
          ("Devastating Invasions and Burning of Universities", ["Invasions by Turkish commanders, notably Bakhtiyar Khalji's sack of Nalanda, Vikramashila, and Odantapuri (c. 1198-1200 CE), massacred monks and incinerated monastic libraries, destroying the institutional nerve-center of Indian Buddhism."])],
         "Fishbone diagram of decline: Internal degeneration (Tantrism, Wealth) + Hindu assimilation (Buddha as Avatar) + Loss of Patronage (Rajputs) + Turkish destructions (Nalanda sack).",
         "Bereft of grassroots secular support and dependent on royal monastic patronage, Indian Buddhism succumbed when its university strongholds were obliterated.")
    ]

    for item in anc_topics_list:
        qs.append({
            "id": item[0],
            "category": "ancient",
            "categoryLabel": "Ancient India",
            "periodId": item[2],
            "marks": item[3],
            "wordLimit": item[4],
            "isPyq": False if "UPSC" not in str(item[5]) else True,
            "yearSource": str(item[5]) if "UPSC" in str(item[5]) else "Standard Practice",
            "bookRef": item[5] if "UPSC" not in str(item[5]) else item[6],
            "question": item[1],
            "framework": {
                "intro": item[6] if "UPSC" not in str(item[5]) else item[7],
                "body": [{"heading": b[0], "points": b[1]} for b in (item[7] if "UPSC" not in str(item[5]) else item[8])],
                "diagramMapIdea": item[8] if "UPSC" not in str(item[5]) else item[9],
                "conclusion": item[9] if "UPSC" not in str(item[5]) else item[10]
            }
        })

    return qs

def main():
    anc = get_ancient_mains()
    print(f"Ancient Mains generated: {len(anc)}")

if __name__ == '__main__':
    main()
