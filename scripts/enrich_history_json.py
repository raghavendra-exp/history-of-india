import json
import os

with open('data/history.json', 'r', encoding='utf-8') as f:
    hdata = json.load(f)

periods = hdata['periods']
print(f"Loaded {len(periods)} periods.")

period_map = {p['id']: p for p in periods}

# 1. Enrich prehistoric-age with Harari's Sapiens insights
p_pre = period_map.get('prehistoric-age')
if p_pre:
    p_pre.setdefault('aspects', {})
    p_pre['aspects']['Cognitive & Agricultural Revolutions (Sapiens Insights)'] = [
        "The Cognitive Revolution (c. 70,000 BCE): Genetic mutations enabled Homo sapiens to communicate abstract fictions, collective myths (gods, laws, money, and imagined communities), allowing cooperative hunting and social cohesion in bands far exceeding Dunbar's number (150 individuals).",
        "Paleolithic Foraging Economy: Hunter-gatherers in the Indian subcontinent (Bhimbetka rock shelters, Attirampakkam, Hunsgi) led physically diverse lifestyles with broad-spectrum wild diets, superior micronutrient profiles compared to early agriculturalists, and animistic belief systems reflected in cave paintings.",
        "The Agricultural Revolution (c. 10,000–7,000 BCE): Described by modern anthropologists as 'history's biggest fraud' — rather than humans domesticating crops, wheat, barley, and rice domesticated humans, tying nomadic bands to permanent mud-brick hamlets (demonstrated at Mehrgarh in the Bolan Pass).",
        "Demographic Explosion vs. Nutritional Stress: Sedentary agriculture caused exponential population growth and permanent settlements, but at the cost of repetitive back-breaking labor (slipped discs, arthritis), infectious epidemics from zoonotic livestock contact, vulnerability to famines, and emerging socio-economic stratification."
    ]
    p_pre.setdefault('upsc', {}).setdefault('prelims', []).append("Sapiens Historiographical Paradigm: The shift from hunting-gathering to Neolithic farming at Mehrgarh represented an irreversible metabolic and social transformation towards state formation.")
    p_pre.setdefault('upsc', {}).setdefault('mains', []).append("Critically evaluate the Neolithic transition in the Indian subcontinent. Was the 'Agricultural Revolution' an unambiguous leap forward in human welfare, or did it introduce structural vulnerabilities and inequality?")
    print("Enriched prehistoric-age")

# 2. Enrich kingdoms-of-north with Col. James Tod's Annals of Rajasthan insights
p_kn = period_map.get('kingdoms-of-north')
if p_kn:
    p_kn.setdefault('aspects', {})
    p_kn.setdefault('people', [])
    p_kn['aspects']['Rajput Polity & Chivalry (James Tod: Annals of Rajasthan)'] = [
        "Agnikula vs. Solar-Lunar Dynastic Origins: Col. James Tod recorded the classic Agnikula fire-pit legend on Mount Abu, where the sage Vashistha created four warrior clans (Pratiharas, Paramaras, Chalukyas/Solankis, and Chauhans) to protect dharma; alongside the solar (Suryavanshi: Guhilas/Sisodias of Mewar, Rathores of Marwar, Kachwahas of Amber) and lunar (Chandravanshi: Bhattis of Jaisalmer) lineages.",
        "Mewar's Unbroken Chivalric Ethos: The Guhila-Sisodia dynasty of Mewar established by Bappa Rawal maintained stubborn independence against Delhi. Rana Kumbha erected 32 formidable hill fortresses across Mewar, including the iconic Kumbhalgarh and the victory tower Vijay Stambha at Chittor.",
        "Feudal Hierarchy & Military Tenure: Rajput states operated on clan-based feudal ties (Patta and Jagir tenures) where feudal thakurs and sardars owed hereditary military allegiance (Chhatri chivalric code) rather than bureaucratic submission to the monarch.",
        "Jauhar and Saka Traditions: In moments of inevitable defeat against overwhelming imperial armies, Rajput fortresses enacted the supreme sacrifice — women and children performed Jauhar (collective self-immolation into ritual pyres to protect honor), while warriors donned saffron robes (Kesariya) and rode out in Saka (death-charge) to fight to the last man (exemplified in the sieges of Chittorgarh in 1303, 1535, and 1568)."
    ]
    p_kn['people'].append({
        "name": "Col. James Tod",
        "role": "British Political Agent & Chronicler of Rajasthan",
        "note": "Author of 'Annals and Antiquities of Rajasthan' (1829-32), the foundational monumental historical chronicle of Rajput genealogies, feudal chivalry, and regional resistance."
    })
    print("Enriched kingdoms-of-north")

# 3. Enrich establishment-of-british-power with Pratik Nayak & B.L. Grover insights
p_est = period_map.get('establishment-of-british-power')
if p_est:
    p_est.setdefault('aspects', {})
    p_est['aspects']['Stages of Colonial Penetration & Diplomatic Treaties (B.L. Grover & Pratik Nayak)'] = [
        "Mercantile Conquest & Elimination of Rivals: The British East India Company methodically eliminated European competitors — defeating the Portuguese (Battle of Swally 1612), the Dutch (Battle of Bedara/Chinsurah 1759), and the French in three Carnatic Wars (culminating in the Battle of Wandiwash 1760 and Treaty of Paris 1763).",
        "The Bengal Lever & Treaty of Allahabad (1765): Following Plassey (1757) and Buxar (1764), Robert Clive secured the Diwani (civil and revenue administration) of Bengal, Bihar, and Orissa from Mughal Emperor Shah Alam II for an annual tribute of 26 lakh rupees, introducing the predatory Dual System of Government (1765-1772) where the Company wielded power without responsibility.",
        "The Ring Fence Policy (Warren Hastings, 1772-1785): Created buffer zones around Company territories to defend frontiers against Marathas and Afghans, famously turning Awadh into a dependent buffer state whose defense costs were borne by the Nawab.",
        "Subsidiary Alliance Framework (Lord Wellesley, 1798-1805): Codified Dupleix's pioneer mercenary mechanism into a four-stage imperial subjugation tool: Company promised troops -> Stationed permanent subsidiary force inside native territory -> Demanded territorial cessions or cash subsidies -> Controlled external relations and stationed a British Resident, stripping native rulers of external sovereignty (Hyderabad 1798, Mysore 1799, Tanjore 1799, Awadh 1801, Peshwa Baji Rao II Treaty of Bassein 1802)."
    ]
    print("Enriched establishment-of-british-power")

# 4. Enrich british-colonial-rule with R. Palme Dutt's 3 Stages & Drain of Wealth
p_bcr = period_map.get('british-colonial-rule')
if p_bcr:
    p_bcr.setdefault('aspects', {})
    p_bcr['aspects']['Marxist Paradigm: 3 Stages of Colonialism (R. Palme Dutt)'] = [
        "Stage I: Mercantile Capitalist Phase (1757–1813): Direct plunder and monopolistic trade. The Company used territorial land revenues of Bengal to buy Indian textiles and spices ('investment') for export to Europe without any inflow of bullion into India, draining raw wealth at the point of origin.",
        "Stage II: Industrial Capitalist Phase (1813–1858): Post-Charter Act of 1813, the Company's trade monopoly was abolished. India was systematically converted into an agrarian appendage of the British metropolis — an exporter of raw materials (cotton, jute, indigo, opium, tea) and an open market for Manchester machine-made cotton goods, precipitating catastrophic deindustrialization and the collapse of urban artisan guild centers (Dhaka, Murshidabad, Surat).",
        "Stage III: Financial Capitalist Phase (Post-1858): Export of British surplus capital into India under state-guaranteed returns. British capitalists invested in Indian railways (with a guaranteed 5% return paid from Indian tax revenues, termed 'private enterprise at public risk'), public debt, tea plantations, mining, and managing agency houses."
    ]
    p_bcr['aspects']['The Drain of Wealth & Famine Policy Matrix'] = [
        "Mechanisms of Economic Drain: Conceptualized by Dadabhai Naoroji ('Poverty and Un-British Rule in India'), Romesh Chunder Dutt ('Economic History of India'), and M.G. Ranade. The drain comprised Home Charges (pensions and salaries of India Office officials, interest on Indian public debt, guaranteed railway interest, military procurement abroad) and unrequited commodity exports.",
        "Commercialization of Agriculture: Forced shift from subsistence foodgrains to cash crops (indigo, cotton, opium, sugarcane) driven by rigid, monetized land revenue demands. This severed the traditional village famine cushion, rendering the peasantry defenseless during monsoonal droughts.",
        "Evolution of Famine Policy & Commissions: Campbell Commission (1866 Orissa Famine - recommended government responsibility for famine relief); Strachey Commission (1880 - formulated the Provisional Famine Code, creation of Famine Insurance Fund); Lyall Commission (1897); MacDonnell Commission (1901 - recommended 'moral strategy' of advance loans, agricultural banks, and irrigation development)."
    ]
    print("Enriched british-colonial-rule")

# 5. Enrich british-administration with Land Revenue, Press, Civil Services & Education
p_ba = period_map.get('british-administration')
if p_ba:
    p_ba.setdefault('aspects', {})
    p_ba['aspects']['Land Revenue Systems Matrix (Pratik Nayak Compendium)'] = [
        "Permanent Settlement / Zamindari System (1793): Introduced by Lord Cornwallis and John Shore across Bengal, Bihar, Orissa, Northern Carnatic (covering ~19% of British India). Zamindars recognized as absolute proprietors of land with hereditary rights. State demand fixed permanently at 10/11th for the Company and 1/11th for the Zamindar. Sunset Law dictated auction of estates if revenue was not deposited by sunset of the specified day. Resulted in rampant absentee landlordism, sub-infeudation, and pauperization of the ryots.",
        "Ryotwari System (1820): Devised by Thomas Munro and Alexander Read across Madras, Bombay Presidency, parts of Assam and Coorg (~51% of British India). Direct settlement with the individual peasant (ryot). Land surveyed and classified; revenue demand revised periodically (every 20–30 years), often reaching 45%–55% of gross produce. Led to direct state extortion and widespread indebtedness to moneylenders.",
        "Mahalwari System (1822/1833): Formulated by Holt Mackenzie (Regulation VII of 1822) and reformed by Merttins Bird and James Thomason (1833) across North-Western Provinces, Central Provinces, and Punjab (~30% of British India). Revenue settled with the village community or estate (Mahal) collectively through the village headman (Lambardar). Revenue demand initially set at 66% (later reduced to 50% under William Bentinck)."
    ]
    p_ba['aspects']['Civil Services, Police & Judiciary Evolution'] = [
        "Civil Services: Lord Cornwallis ('Father of Civil Services in India') separated revenue collection from commercial functions, established high European salaries to combat corruption, and instituted the Cornwallis Code (1793). Charter Act of 1853 introduced open competitive exams. Satyendranath Tagore became the first Indian to qualify for the ICS (1863). Aitchison Commission (1886) classified services into Imperial, Provincial, and Subordinate. Lee Commission (1924) recommended establishing a Public Service Commission (created 1926).",
        "Press Policy Chronology: Censorship of Press Act 1799 (Wellesley); Licensing Regulations 1823 (John Adams, forced closure of Raja Rammohan Roy's Mirat-ul-Akhbar); Press Act of 1835 (Charles Metcalfe - 'Liberator of the Indian Press', repealed 1823 regulations); Vernacular Press Act 1878 (Lord Lytton - 'The Gagging Act', discriminated against vernacular papers, repealed by Lord Ripon in 1882); Newspaper (Incitement to Offences) Act 1908 and Indian Press Act 1910.",
        "Educational Commissions Pipeline: Charter Act 1813 (1 lakh education grant); Orientalist-Anglicist Controversy (H.T. Prinsep vs Macaulay); Macaulay's Minute 1835 (Infiltration Theory - creating 'a class of persons Indian in blood and colour, but English in taste, in opinions, in morals and in intellect'); Wood's Despatch 1854 ('Magna Carta of English Education in India', recommended female education, vernacular primary schools, Anglo-vernacular high schools, and affiliating universities in Calcutta, Bombay, Madras 1857); Hunter Commission 1882 (primary & secondary education); Raleigh Commission & Indian Universities Act 1904 (Curzon); Sadler Commission 1917 (Calcutta University, secondary board reforms); Hartog Committee 1929 (consolidation against hasty expansion); Wardha Scheme of Basic Education 1937 (Zakir Husain Committee, learning through craft); Sargent Plan of Education 1944."
    ]
    print("Enriched british-administration")

# 6. Enrich foundation-of-indian-national-congress with Political Associations & Ideological Debates
p_inc = period_map.get('foundation-of-indian-national-congress')
if p_inc:
    p_inc.setdefault('aspects', {})
    p_inc['aspects']['Pre-Congress Political Organizations (1836–1885 Chronology)'] = [
        "Bangabhasha Prakasika Sabha (1836): Early association in Bengal formed by associates of Raja Rammohan Roy to discuss government policies.",
        "Landholders' Society / Zamindari Association (1838): Founded by Dwarkanath Tagore and Radhakanta Deb to protect landlord interests through constitutional agitation.",
        "Bengal British India Society (1843) and British Indian Association (1851): Amalgamation under Radhakanta Deb and Debendranath Tagore, petitioning the British Parliament for separate legislatures and reduction of salt duties.",
        "East India Association (1866, London): Founded by Dadabhai Naoroji to lobby British Parliament and educate the British public on Indian grievances.",
        "Poona Sarvajanik Sabha (1870): Founded by M.G. Ranade, G.V. Joshi, and S.H. Chiplunkar to serve as a bridge between the government and the rural public, vigorously mobilizing famine relief.",
        "Indian Association of Calcutta (1876): Founded by Surendranath Banerjea and Ananda Mohan Bose; organized the nationwide Civil Service agitation and convened the Indian National Conference (1883 & 1885), the direct dress-rehearsal for the Congress.",
        "Madras Mahajana Sabha (1884) & Bombay Presidency Association (1885): Founded by M. Veeraraghavachariar, G. Subramania Iyer, P. Anandacharlu; and Pherozeshah Mehta, K.T. Telang, Badruddin Tyabji, providing nationwide political momentum."
    ]
    p_inc['aspects']['Foundational Historiographical Debates: Safety Valve vs. Lightning Conductor'] = [
        "The 'Safety Valve' Myth: Propounded by Extremist leader Lala Lajpat Rai (in 'Young India', 1916) and Marxist historian R. Palme Dutt ('India Today'), alleging that retired civil servant Allan Octavian Hume founded the Congress with Viceroy Dufferin's blessings to provide a safe, harmless outlet for boiling peasant discontent following seven secret CID volume reports.",
        "The 'Lightning Conductor' Historiographical Reality: Bipan Chandra and modern historians established that early nationalist leaders (Gokhale, W.C. Bonnerjee) consciously used A.O. Hume as a 'lightning conductor' to prevent the colonial state from crushing the infant all-India political organization at its inception; Dufferin soon grew fiercely hostile, deriding the Congress as a 'microscopic minority'."
    ]
    print("Enriched foundation-of-indian-national-congress")

# 7. Enrich indian-freedom-struggle with Revolutionary Movements Phase I & II, Home Rule
p_ifs = period_map.get('indian-freedom-struggle')
if p_ifs:
    p_ifs.setdefault('aspects', {})
    p_ifs['aspects']['Revolutionary Movement: Phase I vs Phase II Comparative Matrix (Pratik Nayak)'] = [
        "Phase I (1907–1917) Characteristics: Individual heroic action, secret societies (Anushilan Samiti, Yugantar, Abhinav Bharat), assassination of unpopular British officials (Kingsford, Curzon Wyllie, Jackson), religious oaths (Gita, Kali worship), overseas networks (Ghadar Party in San Francisco, Berlin Committee, Komagata Maru incident 1914), aimed at striking terror into British bureaucracy.",
        "Phase II (1920s–1930s) Characteristics: Ideological shift towards scientific socialism and Marxism, mass mobilization of workers and peasants (Kirti Kisan Party, Naujawan Bharat Sabha), rejection of religious revivalism. HRA (Kanpur 1924: Bismil, Sachindranath Sanyal, Ashfaqulla Khan) evolved into HSRA (Feroz Shah Kotla 1928: Bhagat Singh, Chandrashekhar Azad), declaring the goal of establishing the Federal Republic of the United States of India.",
        "Iconic Landmark Actions: Kakori Train Action (1925), Saunders Assassination (1928 to avenge Lala Lajpat Rai), Central Legislative Assembly Bombing (8 April 1929 - Bhagat Singh & Batukeshwar Dutt threw leaflets stating 'to make the deaf hear' protesting Public Safety & Trade Disputes Bills), Lahore Conspiracy Case (Jatin Das 63-day hunger strike martyrdom), Chittagong Armoury Raid (1930 - Surya Sen / Masterda, Pritilata Waddedar, Kalpana Datta)."
    ]
    p_ifs['aspects']['Home Rule Movement & Lucknow Entente (1916)'] = [
        "Tilak's Home Rule League (April 1916): Launched at Belgaum, operated across Maharashtra (excluding Bombay city), Karnataka, Central Provinces, and Berar with 6 branches; newspapers Mahratta (English) and Kesari (Marathi); slogan 'Swaraj is my birthright and I shall have it'.",
        "Annie Besant's Home Rule League (September 1916): Headquartered at Adyar (Madras), covered rest of India with 200 branches; newspapers New India and Commonweal; organized by George Arundale and B.P. Wadia.",
        "Lucknow Session (1916, A.C. Majumdar): Readmission of Extremists into Congress; signing of the landmark Lucknow Pact between Congress and the Muslim League (joint demands for self-government, mutual acceptance of separate electorates)."
    ]
    print("Enriched indian-freedom-struggle")

# 8. Enrich mahatma-gandhi with South African experiments & core philosophy
p_mg = period_map.get('mahatma-gandhi')
if p_mg:
    p_mg.setdefault('aspects', {})
    p_mg['aspects']['South African Crucible & Philosophical Foundations (Experiments with Truth)'] = [
        "South African Crucible (1893–1914): Evolved non-violent passive resistance through the Natal Indian Congress (1894), Indian Opinion journal (1903), Phoenix Settlement (1904 - communal manual labor inspired by Ruskin's 'Unto This Last'), and Tolstoy Farm (1910 - funded by Hermann Kallenbach for satyagrahis). Fought against the Asiatic Registration Act (Black Act), poll tax on ex-indentured laborers, and invalidation of Indian marriages.",
        "Intellectual Mentors & Influences: Leo Tolstoy ('The Kingdom of God Is Within You' - doctrine of non-resistance to evil through violence), John Ruskin ('Unto This Last' - Sarvodaya, welfare of all), Henry David Thoreau ('Civil Disobedience' - moral duty to resist unjust state laws), and Shrimad Rajchandra (spiritual guide on Jain principles of Ahimsa and Aparigraha).",
        "The Satyagraha Paradigm: Fundamental distinction between Passive Resistance (a weapon of the weak, allowing tactical hatred and practical violence if opportunity permits) and Satyagraha (a weapon of the morally courageous, based on love, non-hatred, self-suffering, and aiming to convert the conscience of the adversary rather than defeating him).",
        "The Constructive Programme: Non-political pillars essential for Swaraj — Khadi and Village Industries (economic decentralization and self-reliance), removal of Untouchability (Harijan Sevak Sangh), Hindu-Muslim unity, prohibition of alcohol, Basic Education (Nai Talim), and Trusteeship (capitalists acting as moral trustees of wealth for the community)."
    ]
    print("Enriched mahatma-gandhi")

# 9. Enrich independence-of-india with Swarajists, CDM, 1935 Act, Quit India & 1946-47 Pipeline
p_ind = period_map.get('independence-of-india')
if p_ind:
    p_ind.setdefault('aspects', {})
    p_ind['aspects']['The Interwar Political Pipeline: Swarajists to Poona Pact (1922–1935)'] = [
        "Swarajists vs. No-Changers (1922–1924): Following Non-Cooperation's withdrawal, C.R. Das and Motilal Nehru formed the Congress-Khilafat Swarajya Party (Gaya Session 1922) to enter legislative councils and 'end or mend' the 1919 Montford reforms from within; No-Changers (Patel, Rajagopalachari, Rajendra Prasad) focused on grassroots constructive work. Gandhi mediated unity at Belgaum (1924).",
        "Simon Commission & Nehru Report (1927–1928): Appointment of all-white Indian Statutory Commission sparked universal boycott ('Simon Go Back'). Birkenhead's challenge yielded the Nehru Report (Motilal Nehru) advocating Dominion Status, Fundamental Rights (universal adult suffrage), joint electorates, and linguistic provinces; countered by Jinnah's 14 Points.",
        "Civil Disobedience & Round Table Conferences (1930–1934): Dandi March (12 March – 6 April 1930, 240 miles to break Salt Law); nationwide mobilization at Vedaranyam (Rajagopalachari), Payyanur (K. Kelappan), Peshawar (Frontier Gandhi & Khudai Khidmatgars), and Dharsana Salt Works (Sarojini Naidu). First RTC boycotted; Gandhi-Irwin Pact (March 1931); Karachi Session (1931 - resolution on Fundamental Rights & National Economic Programme drafted by Nehru); Second RTC deadlock; Ramsay MacDonald's Communal Award (1932); Poona Pact (Sept 1932 - Ambedkar and Gandhi agreement in Yerwada Jail increasing reserved seats for Depressed Classes from 71 to 147 in joint electorates).",
        "Government of India Act 1935: Provided for an All-India Federation (never materialized), Provincial Autonomy with responsible ministries, abolition of dyarchy in provinces and its introduction at the Centre, bicameral legislatures in 6 provinces, and establishment of the Federal Court and Reserve Bank of India. Led to Congress forming ministries in 8 provinces in 1937."
    ]
    p_ind['aspects']['The Final Surge: Quit India, INA, RIN Mutiny & Transfer of Power (1942–1947)'] = [
        "Quit India Movement (August Kranti 1942): Cripps Mission failure led to Gowalia Tank resolution (8 August 1942) with Gandhi's call 'Do or Die'. Operation Zero Hour arrested the entire top leadership overnight. Unprecedented mass uprising ensued with underground radio (Usha Mehta), underground networks (Aruna Asaf Ali, Ram Manohar Lohia, JP), and parallel governments (Ballia under Chittu Pandey, Tamluk Jatiya Sarkar, Satara Prati Sarkar under Nana Patil).",
        "Indian National Army (Azad Hind Fauj): Reorganized by Netaji Subhash Chandra Bose in Singapore (1943), establishing the Provisional Government of Free India (Arzi Hukumat-e-Azad Hind) and Rani of Jhansi Regiment under Captain Lakshmi Sahgal. Red Fort INA Trials (Nov 1945 - Prem Sahgal, Gurbaksh Dhillon, Shah Nawaz Khan defended by Bhulabhai Desai, Sapru, Nehru) created unmatched anti-imperialist public fury.",
        "Royal Indian Navy (RIN) Mutiny (Feb 1946): Ratings of HMIS Talwar struck in Bombay over racial discrimination, substandard food, and INA trials. Spread across 78 ships, 20 shore establishments, and 20,000 ratings in Bombay, Karachi, and Calcutta, shattering the British military pillar of control.",
        "Constitutional Endgame (1946–1947): Cabinet Mission Plan (May 1946 - grouping of provinces, rejected Pakistan, Constituent Assembly election); Direct Action Day (16 August 1946 - communal carnage); Interim Government formed (September 1946); Attlee's Declaration (20 February 1947); Mountbatten Plan (3 June 1947); Indian Independence Act (passed July 1947); partition, partition refugee crisis, and historic integration of 565 Princely States orchestrated by Sardar Vallabhbhai Patel and V.P. Menon."
    ]
    print("Enriched independence-of-india")

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(hdata, f, ensure_ascii=False, indent=2)

print("Successfully enriched data/history.json!")
