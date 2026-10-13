import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Comprehensive enrichment mapping for Modern Indian History
MODERN_ENRICHMENTS = {
    'establishment-of-british-power': {
        'aspects': {
            'Anglo-French Carnatic Rivalry': [
                'Commercial duel in South India: Austrian War of Succession and Seven Years\' War triggered three Carnatic Wars (1746–1763) between the British (Robert Clive, Stringer Lawrence) and French (Dupleix, Bussy, Lally).',
                'Decisive Battles: Battle of St. Thome (1746; tiny disciplined French force routed the large army of Nawab Anwaruddin, proving the superiority of European military drill); Clive\'s daring siege and defense of Arcot (1751); Battle of Wandiwash (22 January 1760; British General Sir Eyre Coote crushed French General Count de Lally, ending French imperial ambitions in India).'
            ],
            'Conquest of Bengal: Plassey to Buxar': [
                'Battle of Plassey (23 June 1757): Siraj-ud-Daulah clashed with Clive over fortification of Calcutta (Fort William) and alleged Black Hole tragedy; Mir Jafar (Commander-in-Chief), Rai Durlabh, Yar Lutuf Khan, and banker Jagat Seth betrayed Siraj; Clive achieved victory with minimal fighting, installing Mir Jafar as puppet Nawab; East India Company received 24 Parganas zamindari.',
                'Battle of Buxar (22 October 1764): Most decisive battle in modern Indian history; Major Hector Munro defeated the combined confederate army of Mir Qasim (deposed Nawab of Bengal), Shuja-ud-Daula (Nawab of Awadh), and Mughal Emperor Shah Alam II; demonstrated outright battlefield superiority of the Company army over Indian imperial powers.',
                'Treaty of Allahabad (August 1765) & Dual Government: Robert Clive secured the Diwani (right to collect revenue) of Bengal, Bihar, and Orissa from Mughal Emperor Shah Alam II in exchange for an annual tribute of 26 lakh rupees and the districts of Kora and Allahabad; instituted the "Dual System of Government" in Bengal (1765–1772): Company controlled Diwani (revenue and military defence) without administrative responsibility, while puppet Nawab held Nizamat (criminal justice and civil administration) without financial resources, causing the devastating Great Bengal Famine of 1770 (killing one-third of the population).'
            ]
        },
        'upsc': {
            'prelims': [
                'The Battle of Wandiwash (1760) ended French imperial ambitions in India, in which British General Eyre Coote decisively defeated Count de Lally.',
                'The Battle of Plassey was fought on 23 June 1757 on the banks of the Bhagirathi river, where Robert Clive defeated Siraj-ud-Daulah through the betrayal of Mir Jafar and Jagat Seth.',
                'Major Hector Munro commanded the victorious British East India Company forces at the decisive Battle of Buxar on 22 October 1764.',
                'Under the Treaty of Allahabad (1765), Mughal Emperor Shah Alam II granted the Diwani rights of Bengal, Bihar, and Orissa to the British East India Company.',
                'Robert Clive introduced the Dual System of Government in Bengal in 1765, which was abolished by Warren Hastings in 1772.',
                'The disastrous Great Bengal Famine of 1770 occurred under the Dual Government, resulting in the death of an estimated 10 million people (one-third of Bengal\'s population).'
            ],
            'mains': [
                'Compare and contrast the political, military, and historical significance of the Battle of Plassey (1757) and the Battle of Buxar (1764). Why is Buxar considered far more decisive than Plassey?',
                'Critically examine the working and economic consequences of Robert Clive\'s Dual System of Government in Bengal (1765–1772).',
                'Analyze the causes of the failure of the French East India Company under Dupleix against the British in the Carnatic Wars.'
            ]
        }
    },
    'colonial-economy-and-drain-of-wealth': {
        'aspects': {
            'Three Land Revenue Systems': [
                '1. Permanent Settlement / Zamindari (1793): Introduced by Lord Cornwallis and Sir John Shore in Bengal, Bihar, Orissa, Northern Carnatic, and Banaras (19% of British India); Zamindars recognized as absolute hereditary owners of the soil; state revenue demand fixed in perpetuity at 10/11th of total rent, with Zamindar retaining 1/11th; "Sunset Law" mandated auctioning of estates if revenue was not deposited by sunset on specified date; created an artificial class of loyal aristocratic absentee landlords, rack-renting tenant cultivators.',
                '2. Ryotwari System (1820): Devised by Thomas Munro and Alexander Read in Madras, Bombay, parts of Assam and Coorg (51% of British India); settlement made directly with the individual peasant cultivator (Ryot); revenue fixed for 20 to 30 years after soil survey, demanding 45% to 55% of gross produce; failure of harvest led to ruthless land confiscation and peasant indebtedness to moneylenders (Sahukars).',
                '3. Mahalwari System (1822 / 1833): Formulated by Holt Mackenzie (1822) and reformed by Merttins Bird ("Father of Land Revenue Settlement in North India", 1833) in the Ganga Valley, North-Western Provinces (UP), Central Provinces, and Punjab (30% of British India); settlement made with the entire village community (Mahal) represented by the village headman (Lambardar) who was collectively responsible for payment.'
            ],
            'De-Industrialization & Commercialization': [
                'Ruin of Traditional Indian Handicrafts: One-way free trade imposed after the Charter Act of 1813; high British tariffs on Indian textiles entering Britain, while machine-made Manchester cottons flooded India duty-free; collapse of urban artisanal centres (Dacca, Murshidabad, Surat); artisan millions thrown back onto overcrowded agriculture, turning India from an exporter of textiles into an exporter of raw cotton, jute, and food grains; Governor-General Lord William Bentinck lamented in 1834: "The bones of the cotton weavers are bleaching the plains of India."',
                'Forced Commercialization of Agriculture: Peasantry compelled to cultivate cash crops for British industries (indigo, opium, tea, raw cotton, jute) instead of subsistence food grains; Tinkathia system in Champaran forced peasants to grow indigo on 3/20th of land; induced chronic famines (Orissa 1866, Great Famine 1876–78, Bengal 1943).'
            ],
            'The Drain of Wealth Theory': [
                'Economic Critique of Imperialism: Unilateral transfer of Indian economic surplus to Britain without any equivalent commercial or material return.',
                'Dadabhai Naoroji ("Grand Old Man of India"): Formulated the Drain theory in his 1867 paper "England\'s Debt to India" and book Poverty and Un-British Rule in India (1901); identified the drain through Home Charges (interest on public debt, railway guarantees, civil/military pensions, India Office expenses), remittances of British officers, and profits of foreign shipping/banking.',
                'R.C. Dutt (Economic History of India) and Dinshaw Wacha: Demonstrated that nearly 20 to 30 million pounds were drained annually from India, suffocating domestic capital formation and turning the country into an impoverished colonial dependency.'
            ]
        },
        'upsc': {
            'prelims': [
                'Lord Cornwallis introduced the Permanent Settlement in Bengal and Bihar in 1793 based on the recommendations of Sir John Shore.',
                'Under the Sunset Law of the Permanent Settlement, if the Zamindar failed to pay the fixed revenue by sunset of the specified date, his estate was confiscated and auctioned.',
                'The Ryotwari system was introduced in the Madras and Bombay Presidencies by Sir Thomas Munro and Captain Alexander Read.',
                'Holt Mackenzie devised the Mahalwari system in 1822, which was later overhauled by Merttins Bird in 1833 in the North-Western Provinces.',
                'Dadabhai Naoroji articulated the "Drain of Wealth" theory in his seminal book Poverty and Un-British Rule in India (1901).',
                'Romesh Chunder Dutt (R.C. Dutt) authored the monumental two-volume Economic History of India, systematically exposing colonial de-industrialization.',
                'The Tinkathia system in Bihar legally bound tenant farmers to cultivate indigo on 3/20th of their total landholdings for European planters.'
            ],
            'mains': [
                'Critically examine the institutional features and socio-economic consequences of the Permanent Settlement, Ryotwari, and Mahalwari systems in colonial India.',
                'Evaluate the "Drain of Wealth" thesis formulated by Dadabhai Naoroji and R.C. Dutt, analyzing its contribution to the rise of modern Indian economic nationalism.',
                'Discuss the phenomenon of "De-industrialization" in 19th-century India, examining how British tariff policies and mechanized manufacturing crippled indigenous artisans.',
                'Analyze the commercialization of agriculture during British rule and evaluate its linkage with recurrent catastrophic famines in the late 19th and early 20th centuries.'
            ]
        }
    },
    'tribal-movements-colonial-india': {
        'aspects': {
            'Causes of Tribal & Peasant Resentment': [
                'Colonial forest encroachments: Forest Acts of 1865 and 1878 transformed traditional tribal communal forests into state-reserved property, criminalizing shifting cultivation (Jhum), grazing, and collection of minor forest produce.',
                'Infiltration of Dikus (Outsiders): Money-lenders (Mahajans), zamindars, traders, and European contractors supported by British police seized ancestral tribal land through fraudulent debt mortgages, turning free adivasis into bonded agricultural laborers (Kamia / Beth-begari).'
            ],
            'Major Tribal Uprisings': [
                'Santhal Hool (1855–1856): Led by four brothers (Sidho, Kanhu, Chand, and Bhairav) in the Damin-i-Koh region (Rajmahal Hills, Bihar/Jharkhand) against British revenue officers, Bengali Mahajans, and railway contractors; mobilized 60,000 Santhals; brutally suppressed with martial law; led to creation of the separate non-regulation Santhal Parganas district.',
                'Munda Ulgulan / The Great Tumult (1899–1900): Led by charismatic religious leader Birsa Munda ("Dharti Aaba" / Father of the Earth) in the Chotanagpur plateau; fought against the destruction of the ancestral Khuntkatti joint-landholding system by Thikadars and Christian missionaries; Birsa declared an independent Munda Raj; captured and died in Ranchi jail (1900); prompted enactment of the Chotanagpur Tenancy Act (1908) banning transfer of tribal land to non-tribals.',
                'Other key uprisings: Kol Mutiny (1831–32 under Buddho Bhagat in Chotanagpur); Khasi Uprising (1829–33 led by U Tirot Sing in Meghalaya against road construction); Rampa Rebellion (1922–24 in Andhra Pradesh led by Alluri Sitarama Raju using guerrilla warfare against Madras Forest Act); Chenchu tribal revolt.'
            ],
            'Major Peasant Movements': [
                'Indigo Revolt / Nil Bidroho (1859–1860): Led by Digambar Biswas and Bishnu Biswas in Nadia (Bengal); peasants took solemn oath refusing to cultivate indigo; popularized by Dinabandhu Mitra\'s Bengali play Nil Darpan (translated into English by Michael Madhusudan Dutta); led to appointment of Indigo Commission (1860) declaring indigo cultivation cannot be forced.',
                'Pabna Agrarian League (1873 in East Bengal, resisting rent hikes via legal litigation) and Deccan Riots (1875 in Pune/Ahmednagar, burning debt bonds of Gujarati/Marwari moneylenders; led to Deccan Agriculturists\' Relief Act 1879).'
            ]
        },
        'upsc': {
            'prelims': [
                'The Santhal Hool (1855–56) in the Rajmahal Hills was led by brothers Sidho, Kanhu, Chand, and Bhairav.',
                'Birsa Munda led the Munda Ulgulan (Great Tumult) in Chotanagpur, championing the restoration of the traditional "Khuntkatti" collective landholding system.',
                'The Chotanagpur Tenancy Act of 1908 was enacted following the Munda uprising, prohibiting the alienation of tribal land to non-tribals.',
                'The Indigo Revolt (Nil Bidroho) of 1859–60 began in Govindpur village (Nadia district, Bengal) under the leadership of Digambar Biswas and Bishnu Biswas.',
                'The play Nil Darpan, depicting the atrocities of British indigo planters, was written in Bengali by Dinabandhu Mitra.',
                'The Rampa Rebellion (1922–24) in the Godavari agency hills was led by Alluri Sitarama Raju.',
                'The Deccan Riots of 1875 broke out in the villages of Pune and Ahmednagar, where peasants attacked moneylenders and burned debt bonds and mortgage deeds.'
            ],
            'mains': [
                'Analyze the underlying socio-economic and ecological causes of tribal uprisings in colonial India, highlighting how British forest and revenue policies transformed the tribal habitat.',
                'Examine the leadership, religious ideology, and agrarian objectives of Birsa Munda\'s Ulgulan in Chotanagpur.',
                'Evaluate the nature and significance of the Indigo Revolt (1859–1860) as a model of non-violent peasant resistance supported by the urban intelligentsia.',
                'Discuss how tribal rebellions differed from peasant movements in 19th-century India in terms of leadership, mobilization, and methods of protest.'
            ]
        }
    },
    'socio-religious-reforms': {
        'aspects': {
            'Raja Ram Mohan Roy & Brahmo Samaj': [
                'Father of Modern Indian Renaissance: Polyglot scholar; established Atmiya Sabha (1815) and Brahmo Samaj (1828); preached monotheism based on the Upanishads; vehemently campaigned against Sati, child marriage, polygamy, and caste rigidity; persuaded Lord William Bentinck to pass Regulation XVII (December 1829) declaring Sati illegal and punishable as culpable homicide.',
                'Pioneered Indian Journalism: Published Sambad Kaumudi (Bengali weekly) and Mirat-ul-Akhbar (Persian journal); supported Western scientific education (founded Hindu College in 1817 with David Hare, and Vedanta College in 1825); passed away at Bristol, England (1833).',
                'Evolution of Brahmo Samaj: Debendranath Tagore joined in 1842, establishing the Tattvabodhini Sabha (and journal Tattvabodhini Patrika); Keshub Chandra Sen expanded movement pan-India; schisms: Brahmo Samaj of India (1866 under Keshub) and Adi Brahmo Samaj (under Debendranath); second schism into Sadharan Brahmo Samaj (1878) led by Anand Mohan Bose and Sivanath Sastri.'
            ],
            'Ishwar Chandra Vidyasagar & Widow Remarriage': [
                'Crusade for Women\'s Emancipation: Principal of Sanskrit College, Calcutta (opened admissions to non-Brahmin students); cited Parashara Smriti to prove Vedic sanction for widow remarriage; submitted mass petitions to government; secured passage of the Hindu Widows\' Remarriage Act (Act XV of 1856) enacted by Lord Dalhousie and Lord Canning; served as secretary of Bethune School (founded 1849 by J.E.D. Bethune), pioneering female education in Bengal.'
            ],
            'Lower-Caste Movements: Jyotirao Phule & Periyar': [
                'Jyotirao Govindrao Phule: Pioneered non-Brahmin anti-caste movement in Maharashtra; opened first school for Untouchable girls at Bhidewada, Pune (1848) with wife Savitribai Phule; founded Satyashodhak Samaj (Truth Seekers\' Society, 1873) to liberate Shudras and Ati-Shudras; authored Gulamgiri (Slavery, 1873 - dedicated to the American abolitionist movement) and Sarvajanik Satya Dharma.',
                'E.V. Ramasamy Periyar: Launched the Self-Respect Movement (1925) in Tamil Nadu; rejected Brahminical dominance, Manusmriti, and theistic rituals; advocate of rationalism and women\'s rights; founded Dravidar Kazhagam (1944).'
            ],
            'Revivalist & Reformist Movements': [
                'Arya Samaj (1875): Founded at Bombay by Swami Dayananda Saraswati (Mulshankar); slogan: "Go Back to the Vedas"; rejected Puranas, idol worship, polytheism, child marriage, and hereditary caste; authored Satyarth Prakash; initiated Shuddhi movement (re-conversion); founded DAV College network at Lahore (1886) and Gurukul Kangri at Haridwar (1902 by Swami Shraddhanand).',
                'Ramakrishna Mission (1897): Founded at Belur Math by Swami Vivekananda (Narendranath Datta) to institutionalize the humanitarian teachings of Ramakrishna Paramahamsa; world-renowned speech at the Chicago Parliament of Religions (11 September 1893); preached Neo-Vedanta and Practical Vedanta: "Service to Jiva is worship of Shiva".',
                'Muslim Reform: Aligarh Movement led by Sir Syed Ahmad Khan (founded MAO College at Aligarh in 1875, later AMU; journal Tahzib-ul-Akhlaq advocating modern Western science); Deoband School (1866 by Muhammad Qasim Nanautavi and Rashid Ahmad Gangohi, revivalist anti-British orthodoxy).'
            ]
        },
        'upsc': {
            'prelims': [
                'The abolition of Sati was enacted through Regulation XVII of 1829 by Governor-General Lord William Bentinck, championed by Raja Ram Mohan Roy.',
                'The Hindu Widows\' Remarriage Act (Act XV of 1856) was passed largely due to the sustained crusade of Ishwar Chandra Vidyasagar.',
                'Raja Ram Mohan Roy published the weekly journal Sambad Kaumudi in Bengali and Mirat-ul-Akhbar in Persian.',
                'Jyotirao Phule established the Satyashodhak Samaj in 1873 and authored the famous anti-caste manifesto Gulamgiri (Slavery).',
                'Swami Dayananda Saraswati founded the Arya Samaj in 1875 at Bombay and gave the clarion call "Go Back to the Vedas", authoring Satyarth Prakash.',
                'Swami Vivekananda delivered his historic address on Hinduism and universal tolerance at the Parliament of Religions in Chicago on 11 September 1893.',
                'Sir Syed Ahmad Khan founded the Mohammedan Anglo-Oriental (MAO) College at Aligarh in 1875 and published the reformist journal Tahzib-ul-Akhlaq.'
            ],
            'mains': [
                'Compare and contrast the reformist approach of the Brahmo Samaj with the revivalist ideology of the Arya Samaj, analyzing their respective attitudes toward the Vedas and social reform.',
                'Critically evaluate the contribution of Ishwar Chandra Vidyasagar to the cause of women\'s education and widow remarriage in 19th-century India.',
                'Examine the non-Brahmin social justice movements in Western and Southern India with specific reference to Jyotirao Phule\'s Satyashodhak Samaj and Periyar\'s Self-Respect Movement.',
                'Analyze the role of the Aligarh Movement under Sir Syed Ahmad Khan in modernizing Indian Muslim society and education.'
            ]
        }
    },
    'revolutionary-nationalism-and-ina': {
        'aspects': {
            'First Phase of Revolutionary Nationalism (1905–1917)': [
                'Bengal: Anushilan Samiti (founded 1902 by Pramathanath Mitra, Jatindranath Banerjee, Barindra Ghosh); Yugantar weekly; Muzaffarpur bombing (1908 by Khudiram Bose and Prafulla Chaki targeting magistrate Kingsford); Alipore Conspiracy Case (Aurobindo Ghose defended by C.R. Das); Bagha Jatin (Jatindranath Mukherjee) heroic last stand at Burhabalang river, Balasore (1915).',
                'Maharashtra & Abroad: Chapekar Brothers (Damodar and Balkrishna, assassinated Plague Commissioner Rand in Pune 1897); V.D. Savarkar founded Abhinav Bharat (1904) and Mitra Mela; India House in London (founded by Shyamji Krishna Varma; Madan Lal Dhingra assassinated Curzon Wyllie in 1909); Madam Bhikaji Cama hoisted first Indian national tricolour flag at Stuttgart International Socialist Congress (Germany, 1907); Ghadar Party (founded 1913 at San Francisco by Lala Har Dayal, Sohan Singh Bhakna, Kartar Singh Sarabha; Komagata Maru incident 1914).'
            ],
            'Second Phase: HRA, HSRA & Bhagat Singh (1920s)': [
                'Hindustan Republican Association (HRA, 1924): Founded at Kanpur by Ram Prasad Bismil, Sachindra Nath Sanyal (author of Bandi Jiwan), and Jogesh Chandra Chatterjee; goal: armed revolution to establish the Federal Republic of the United States of India; Kakori Train Action (9 August 1925; looted British government railway treasury near Lucknow; Bismil, Ashfaqulla Khan, Roshan Singh, and Rajendra Lahiri hanged).',
                'Hindustan Socialist Republican Association (HSRA, 1928): Reorganized at Feroz Shah Kotla, Delhi under Chandra Shekhar Azad, Bhagat Singh, Sukhdev, and Bhagwati Charan Vohra (author of Philosophy of the Bomb); adopted explicit Marxist-socialist objective of ending human exploitation.',
                'Saunders Assassination & Central Assembly Bomb: Assassinated police officer J.P. Saunders at Lahore (December 1928) to avenge the fatal lathi-charge on Lala Lajpat Rai; Bhagat Singh and Batukeshwar Dutt threw smoke bombs in the Central Legislative Assembly, Delhi (8 April 1929) against the Public Safety Bill and Trade Disputes Bill ("To make the deaf hear"); Jatin Das died following a 63-day hunger strike in Lahore jail; Bhagat Singh, Sukhdev, and Rajguru executed at Lahore Central Jail on 23 March 1931; Chandra Shekhar Azad martyred at Alfred Park, Allahabad (27 Feb 1931).',
                'Chittagong Armoury Raid (April 1930): Masterda Surya Sen led the Indian Republican Army, raiding police armouries in Chittagong (Bengal); heroic participation of young women: Pritilata Waddedar (attack on Pahartali European Club, martyred) and Kalpana Datta.'
            ],
            'Subhas Chandra Bose, INA & RIN Mutiny': [
                'Subhas Chandra Bose\'s Ascent: Congress President at Haripura (1938) and Tripuri (1939, defeating Gandhi\'s candidate Pattabhi Sitaramayya); resigned over ideological differences with Gandhi, founding the Forward Bloc (1939); escaped house arrest in Calcutta (Great Escape, January 1941), traveling via Kabul and Moscow to Berlin (Free India Centre, "Jai Hind" greeting, Tiger Legion).',
                'Indian National Army (Azad Hind Fauj): Conceptualized by Mohan Singh and Rash Behari Bose from Indian POWs in Malaya; Subhas Bose took command in Singapore (July 1943); formed the Provisional Government of Free India (Arzi Hukumat-i-Azad Hind) on 21 October 1943; recognized by Axis powers; created Rani of Jhansi Regiment (women\'s combat regiment commanded by Captain Lakshmi Sahgal); proclaimed slogans: "Chalo Delhi" and "Give me blood, and I will give you freedom"; fought in Imphal and Kohima campaigns (1944).',
                'INA Trials & Royal Indian Navy Mutiny (1945–1946): Red Fort Trials of Prem Sahgal, Gurbaksh Singh Dhillon, and Shah Nawaz Khan sparked massive nationwide mass protests; defended by legal team headed by Bhulabhai Desai, Tej Bahadur Sapru, and Jawaharlal Nehru; RIN Mutiny (18 February 1946; ratings of HMIS Talwar struck work in Bombay over racial discrimination, spreading to 78 naval ships and 20,000 ratings; persuaded to surrender by Sardar Patel and Jinnah), delivering the mortal blow to British imperial control over Indian armed forces.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Hindustan Republican Association (HRA) was founded in 1924 at Kanpur by Ram Prasad Bismil, Sachindra Nath Sanyal, and Jogesh Chandra Chatterjee.',
                'The Kakori Train Action took place on 9 August 1925 near Lucknow, leading to the hanging of Ram Prasad Bismil, Ashfaqulla Khan, Roshan Singh, and Rajendra Lahiri.',
                'Bhagat Singh and Batukeshwar Dutt threw harmless smoke bombs into the Central Legislative Assembly on 8 April 1929 to protest against the Public Safety Bill and Trade Disputes Bill.',
                'Madam Bhikaji Cama unfurled the first design of the Indian national flag at the International Socialist Congress at Stuttgart, Germany, in 1907.',
                'The Chittagong Armoury Raid of 18 April 1930 was planned and executed by the Indian Republican Army under the leadership of "Masterda" Surya Sen.',
                'The Provisional Government of Free India (Arzi Hukumat-i-Azad Hind) was proclaimed by Netaji Subhas Chandra Bose in Singapore on 21 October 1943.',
                'The Royal Indian Navy (RIN) Mutiny began on 18 February 1946 on the naval training ship HMIS Talwar in Bombay harbor.'
            ],
            'mains': [
                'Trace the ideological and strategic evolution of the revolutionary nationalist movement from early romantic individualism to the scientific socialism of Bhagat Singh and the HSRA.',
                'Critically evaluate the contribution of Netaji Subhas Chandra Bose and the Indian National Army (Azad Hind Fauj) to India\'s struggle for independence.',
                'Analyze the historical significance of the INA Red Fort Trials (1945) and the Royal Indian Navy (RIN) Mutiny (1946) in hastening the British decision to transfer power to India.',
                'Discuss the role of women in the revolutionary movement with special reference to Pritilata Waddedar, Kalpana Datta, Bina Das, and Captain Lakshmi Sahgal.'
            ]
        }
    }
}

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

count = 0
for p in d['periods']:
    pid = p['id']
    if pid in MODERN_ENRICHMENTS:
        enr = MODERN_ENRICHMENTS[pid]
        if 'aspects' in enr:
            p.setdefault('aspects', {})
            for k, v in enr['aspects'].items():
                p['aspects'][k] = v
        if 'upsc' in enr:
            p['upsc'] = enr['upsc']
        count += 1
        print(f"Successfully enriched Modern period: {pid}")

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Total modern periods enriched: {count}")
