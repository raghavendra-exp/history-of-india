import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Enrichment mapping for British administration, Viceroys, Later Mughals, Regional & Northern Kingdoms
ADMIN_REGIONAL_ENRICHMENTS = {
    'kingdoms-of-north': {
        'aspects': {
            'Rajput Clan Dynasties & Chahamans': [
                'Rajput lineage origin theories: Agnikula origin myth (derived from the sacrificial fire pit of sage Vashistha at Mount Abu: Pratiharas, Paramaras, Chalukyas/Solankis, Chahamanas) vs. foreign descent (Col. James Tod, V.A. Smith) and indigenous solar/lunar kshatriya origins (G.H. Ojha).',
                'Chahamanas / Chauhans of Shakambhari & Ajmer: Founded by Vasudeva; Ajayraja founded Ajayameru (Ajmer); Vigraharaja IV (Visaladeva) conquered Delhi from the Tomaras and composed the Sanskrit drama Harikeli Nataka; Prithviraj III (Prithviraj Chauhan, r. 1177–1192 CE): Celebrated hero of Chand Bardai\'s epic Prithviraj Raso; defeated Muhammad Ghori at the First Battle of Tarain (1191 CE); defeated and captured at the Second Battle of Tarain (1192 CE), which laid the foundations of Turkish rule in North India.'
            ],
            'Paramaras, Solankis & Chandellas': [
                'Paramaras of Malwa: Capital at Dhara; Raja Bhoja (r. 1010–1055 CE): Legendary polymath king who authored over 84 scholarly treatises across diverse disciplines including Samaranganasutradhara (treatise on architecture and mechanical flying devices), Yuktikalpataru (shipbuilding and statecraft), Sarasvatikanthabharana (poetics), and built the Bhojpur Shiva Temple and Bhojshala Sanskrit college at Dhar.',
                'Solankis / Chaulukyas of Gujarat: Founded by Mularaja (capital: Anhilwara); Bhima I (reign witnessed Mahmud of Ghazni\'s raid on Somnath Temple in 1026 CE; built the Sun Temple at Modhera; his queen Udayamati built the monumental subterranean stepwell Rani ki Vav in Patan, a UNESCO World Heritage site); patronized Jain polymath Hemachandra (author of Siddha-Hema-Shabdanushasana); Vimala Vasahi Dilwara Jain temple built at Mount Abu.',
                'Chandellas of Jejakabhukti (Bundelkhand): Capital at Khajuraho and Mahoba; built the world-renowned Khajuraho group of temples (Kandariya Mahadeva, Lakshmana, Vishvanatha; Nagara style with soaring curvilinear shikharas and sensuous mithuna erotic sculptures).'
            ]
        },
        'upsc': {
            'prelims': [
                'The First Battle of Tarain took place in 1191 CE, where Prithviraj Chauhan defeated Muhammad Ghori; in the Second Battle of Tarain (1192 CE), Ghori defeated Prithviraj.',
                'Raja Bhoja of the Paramara dynasty of Malwa authored the famous architectural treatise Samaranganasutradhara and the shipbuilding work Yuktikalpataru.',
                'The Rani ki Vav (Queen\'s Stepwell) at Patan was commissioned in the 11th century by Queen Udayamati in memory of Chaulukya king Bhima I.',
                'The Sun Temple at Modhera (Gujarat) was built in 1026 CE during the reign of Solanki king Bhima I.',
                'The Dilwara Jain temples at Mount Abu (Rajasthan) were built by Vimala Shah, a minister of the Chaulukya kings of Gujarat.',
                'Prithviraj Raso, the heroic Brajbhasha epic detailing the life of Prithviraj Chauhan, was composed by his court poet Chand Bardai.',
                'The Kandariya Mahadeva Temple at Khajuraho, the grandest of the Chandella temples, was dedicated to Lord Shiva and built around 1030 CE by King Vidyadhara.'
            ],
            'mains': [
                'Examine the political and military causes of the defeat of the Rajput confederacy under Prithviraj Chauhan against Muhammad Ghori at the Second Battle of Tarain (1192).',
                'Analyze the cultural, intellectual, and architectural patronages of Raja Bhoja of Dhar and the Chaulukyas of Gujarat in early medieval Western India.',
                'Critically evaluate the architectural and sculptural hallmarks of the Khajuraho group of temples built by the Chandellas of Bundelkhand.'
            ]
        }
    },
    'british-administration': {
        'aspects': {
            'Constitutional Acts: 1773 to 1853': [
                'Regulating Act of 1773: First step of British parliamentary control over East India Company; transformed Governor of Bengal into Governor-General of Bengal (Warren Hastings); established a 4-member Executive Council; created the Supreme Court of Judicature at Fort William, Calcutta (1774, Sir Elijah Impey as first Chief Justice); prohibited servants of the Company from engaging in private trade.',
                'Pitt\'s India Act of 1784: Instituted a "System of Double Government": Board of Control (6 commissioners appointed by Crown to supervise civil, military, and revenue affairs) and Court of Directors (managing commercial affairs); styled Company possessions for the first time as "British possessions in India".',
                'Charter Act of 1813: Abolished Company\'s commercial trade monopoly in India, opening Indian trade to all British subjects (except monopoly over tea trade and trade with China); allocated an annual sum of one lakh rupees for the promotion of literature and science in India; permitted Christian missionaries to enter India.',
                'Charter Act of 1833: Centralization climax: Governor-General of Bengal redesignated as the Governor-General of India (Lord William Bentinck); deprived Bombay and Madras governors of legislative powers; ended all remaining commercial activities of the Company; added a fourth member (Law Member, Lord Macaulay) to Governor-General\'s Executive Council, establishing the First Law Commission (which drafted the Indian Penal Code).',
                'Charter Act of 1853: Separated executive and legislative functions of the Council; introduced open competitive examinations for recruitment to the covenanted Indian Civil Service (ending patronage of Court of Directors); Macaulay Committee on Civil Services appointed in 1854.'
            ],
            'Administrative Pillars: Civil Service, Police & Judiciary': [
                'Civil Service: Lord Cornwallis regarded as the "Father of Civil Services in India"; separated commercial and administrative branches; banned private trade; Lord Wellesley established Fort William College at Calcutta (1800) to train young civil servants (later shifted to Haileybury College in England).',
                'Police Organization: Cornwallis relieved Zamindars of police duties, establishing a regular police force; divided districts into Thanas (circles of approx 20 miles) under a Daroga (police inspector); appointed District Superintendent of Police (SP); Police Act of 1861 created modern police organizational hierarchy.',
                'Judiciary: Cornwallis Code of 1793 separated revenue collection from judicial administration (depriving Collector of judicial powers); established a hierarchy of courts: Munsif Courts, District/Zilla Courts (headed by District Judge), Provincial Courts of Appeal, and Sadar Diwani Adalat (civil) / Sadar Nizamat Adalat (criminal); replaced Islamic criminal law with codified secular law.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Regulating Act of 1773 established the Supreme Court at Calcutta, with Sir Elijah Impey as its first Chief Justice.',
                'Pitt\'s India Act of 1784 established the Board of Control to supervise the civil, military, and revenue affairs of the East India Company.',
                'The Charter Act of 1813 earmarked an annual expenditure of Rs. 1,00,000 for education in India and ended the trade monopoly (except tea and China).',
                'The Charter Act of 1833 made Lord William Bentinck the first Governor-General of India and completely abolished the Company\'s commercial monopoly.',
                'Lord Cornwallis is regarded as the "Father of the Indian Civil Service" and separated judicial powers from executive revenue collectors.',
                'The Charter Act of 1853 introduced open competitive examination for the Indian Civil Service, ending the patronage of the Court of Directors.',
                'The Indian Penal Code (IPC) was drafted based on the recommendations of the First Law Commission headed by Lord Macaulay (appointed under Charter Act of 1833).'
            ],
            'mains': [
                'Trace the evolution of British parliamentary control over the East India Company from the Regulating Act of 1773 to the Charter Act of 1853.',
                'Critically evaluate the administrative, police, and judicial reforms introduced by Lord Cornwallis in colonial India.',
                'Analyze the introduction of open competition for the Indian Civil Services and examine the racial and institutional barriers faced by early Indian aspirants.'
            ]
        }
    },
    'governors-general-and-viceroys': {
        'aspects': {
            'Key Governors-General (1773–1858)': [
                'Warren Hastings (1772–1785): Abolished Dual Government in Bengal (1772); Asiatic Society of Bengal founded by Sir William Jones (1784); First Anglo-Maratha War (Treaty of Salbai 1782); Second Anglo-Mysore War; impeached in British Parliament on return to England (defended by Edmund Burke).',
                'Lord Cornwallis (1786–1793): Permanent Settlement of Bengal (1793); Cornwallis Code; Third Anglo-Mysore War (Treaty of Srirangapatna 1792); father of Indian Civil Service.',
                'Lord Wellesley (1798–1805): Subsidiary Alliance system; Fourth Anglo-Mysore War (1799); Treaty of Bassein (1802) and Second Anglo-Maratha War; styled himself "A Bengal Tiger".',
                'Lord William Bentinck (1828–1835): Abolition of Sati (1829); suppression of Thuggee by Colonel William Sleeman; English Education Act of 1835 based on Macaulay\'s Minute; first Governor-General of India.',
                'Lord Dalhousie (1848–1856): Doctrine of Lapse; Second Anglo-Sikh War and annexation of Punjab (1849); Annexation of Awadh (1856); First railway line (Bombay to Thane, 1853); First electric telegraph line (Calcutta to Agra, 1853); Post Office Act 1854; Wood\'s Despatch on Education (1854 - "Magna Carta of English Education in India"); Hindu Widows\' Remarriage Act (1856).'
            ],
            'Key Viceroys (1858–1947)': [
                'Lord Canning (1856–1862): Last Governor-General of Company and First Viceroy of Crown (Government of India Act 1858); Queen Victoria\'s Proclamation; Indian Councils Act 1861; Indian Penal Code (1860); Universities of Calcutta, Bombay, and Madras established (1857).',
                'Lord Lytton (1876–1880): Reactionary imperialist; Vernacular Press Act (1878 - "Gagging Act" targeting Amrita Bazar Patrika); Arms Act (1878); Delhi Durbar of 1877 amidst catastrophic famine (Queen Victoria proclaimed Kaiser-i-Hind); Second Anglo-Afghan War (1878–80); lowered maximum age for ICS exam from 21 to 19.',
                'Lord Ripon (1880–1884): Most popular and liberal Viceroy; repealed Vernacular Press Act (1882); First Factory Act of 1881 (child labour reform); Local Self-Government Resolution (1882 - "Father of Local Self-Government in India"); Hunter Commission on Education (1882); Ilbert Bill Controversy (1883 - proposed allowing Indian judges to try Europeans, provoking racist white mutiny).',
                'Lord Curzon (1899–1905): Indian Universities Act (1904); Ancient Monuments Preservation Act (1904); Partition of Bengal (1905); Younghusband Expedition to Tibet (1904).',
                'Lord Chelmsford (1916–1921): Montagu-Chelmsford Reforms / Government of India Act 1919 (introduced Dyarchy in provinces); Jallianwala Bagh Massacre (1919); Non-Cooperation and Khilafat Movements.',
                'Lord Irwin (1926–1931): Simon Commission boycott (1928); Nehru Report; Lahore Session (Purna Swaraj 1929); Civil Disobedience Movement and Dandi March (1930); Gandhi-Irwin Pact (1931).',
                'Lord Mountbatten (March–August 1947): Last Viceroy and first Governor-General of independent India; June 3rd Plan; oversaw partition and transfer of power.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Asiatic Society of Bengal was founded in Calcutta in 1784 by Sir William Jones during the governor-generalship of Warren Hastings.',
                'Colonel William Sleeman was commissioned by Lord William Bentinck to systematically eradicate the ritual murder cult of Thuggee across Central India.',
                'The first passenger train in India ran between Bombay (Bori Bunder) and Thane on 16 April 1853 during the tenure of Lord Dalhousie.',
                'Sir Charles Wood\'s Education Despatch of 1854 is celebrated as the "Magna Carta of English Education in India".',
                'Lord Ripon is hailed as the "Father of Local Self-Government in India" for his historic resolution of 1882.',
                'The Ilbert Bill Controversy of 1883 under Lord Ripon erupted over the proposal to permit Indian district magistrates to preside over trials of European British subjects.',
                'Lord Lytton enacted the Vernacular Press Act in 1878 to suppress critical Indian newspapers, which was repealed by Lord Ripon in 1882.'
            ],
            'mains': [
                'Critically compare the reactionary imperial policies of Lord Lytton (1876–1880) with the progressive reforms of Lord Ripon (1880–1884), analyzing their impact on Indian political awakening.',
                'Evaluate the tenure of Lord Dalhousie (1848–1856) as an imperial modernizer. Did railways, telegraphs, and postal systems serve Indian development or colonial exploitation?',
                'Analyze the administration of Lord Curzon (1899–1905), examining his administrative centralism and how the Partition of Bengal catalyzed militant nationalism.'
            ]
        }
    },
    'later-mughal-empire': {
        'aspects': {
            'Succession Anarchy & Kingmakers': [
                'Bahadur Shah I (Shah Alam I, r. 1707–1712): Son of Aurangzeb; assumed title "Shah-i-Bekhabar" (The Careless King); pacified Marathas by releasing Shahu; concluded peace with Guru Gobind Singh and Chhatrasal Bundela.',
                'Jahandar Shah & Farrukhsiyar: Jahandar Shah (r. 1712–1713, puppet of Zulfiqar Khan; abolished Jizya; introduced Ijarah tax-farming); Farrukhsiyar (r. 1713–1719; raised to throne by the Sayyid Brothers - Abdullah Khan and Husain Ali Khan, known as the "Kingmakers"); granted the fateful 1717 Royal Farman to the British East India Company (termed "Magna Carta of the Company" by John Surman, granting duty-free trade in Bengal in exchange for Rs. 3,000 annually and right to mint coins).',
                'Muhammad Shah "Rangeela" (r. 1719–1748): Overthrew the Sayyid Brothers with help of Nizam-ul-Mulk; reign witnessed complete disintegration of the empire as provincial governors declared de facto independence: Murshid Quli Khan in Bengal (1717), Saadat Khan Burhan-ul-Mulk in Awadh (1722), Nizam-ul-Mulk Asaf Jah in Hyderabad (1724).'
            ],
            'Foreign Cataclysms: Nadir Shah & Abdali': [
                'Nadir Shah\'s Sack of Delhi (1739): Persian conqueror routed imperial Mughal army at Battle of Karnal (February 1739); occupied Delhi; ordered the general massacre (Qatl-e-Aam) of 30,000 citizens in Chandni Chowk; plundered the imperial treasury, carrying away the Peacock Throne (Takht-i-Taus) and the priceless Koh-i-Noor diamond.',
                'Ahmad Shah Abdali (Durrani): Afghan ruler invaded India 8 times between 1748 and 1767; annexed Punjab; crushed the Marathas at the Third Battle of Panipat (1761); left Mughal Emperor Shah Alam II as a blind, helpless puppet ("The Empire of Shah Alam extends from Delhi to Palam").'
            ]
        },
        'upsc': {
            'prelims': [
                'The Sayyid Brothers (Abdullah Khan and Husain Ali Khan) were known as the "Kingmakers" of the Later Mughal era, making and unmaking four emperors.',
                'Mughal Emperor Farrukhsiyar granted the historic Farman of 1717 (the "Magna Carta of the Company") to the British East India Company delegation led by John Surman.',
                'Nadir Shah of Persia invaded India in 1739 during the reign of Muhammad Shah Rangeela, defeating the Mughals at the Battle of Karnal and looting the Peacock Throne.',
                'The regional state of Hyderabad was founded in 1724 by Chin Qilich Khan (Nizam-ul-Mulk Asaf Jah) following his victory at the Battle of Shakar Kheda.',
                'Saadat Khan Burhan-ul-Mulk founded the autonomous principality of Awadh in 1722.',
                'Murshid Quli Khan was appointed Governor of Bengal in 1717 and transferred the capital from Dacca to Murshidabad.',
                'Mughal Emperor Shah Alam II granted the Diwani of Bengal, Bihar, and Orissa to the British East India Company following the Battle of Buxar in 1765.'
            ],
            'mains': [
                'Analyze the internal political, agrarian, and structural factors that caused the rapid disintegration of the Mughal Empire in the first half of the 18th century.',
                'Examine the invasion of Nadir Shah in 1739 and evaluate its psychological, military, and financial impact on the prestige and authority of the Mughal Emperor.',
                'Discuss the emergence of regional successor states (Bengal, Awadh, Hyderabad) in 18th-century India, assessing whether this period was one of "anarchy and decline" or regional economic restructuring.'
            ]
        }
    },
    'sayyid-dynasty': {
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
                'Evaluate the historical significance of Yahya Sirhindi\'s Tarikh-i-Mubarak Shahi in understanding the transition from the Tughlaqs to the Afghan Lodis.',
                'Examine the internal rebellions in Mewat, the Doab, and Gwalior faced by the Sayyid rulers, explaining why the dynasty was unable to re-establish centralized Sultanate authority.'
            ]
        }
    }
}

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

count = 0
for p in d['periods']:
    pid = p['id']
    if pid in ADMIN_REGIONAL_ENRICHMENTS:
        enr = ADMIN_REGIONAL_ENRICHMENTS[pid]
        if 'aspects' in enr:
            p.setdefault('aspects', {})
            for k, v in enr['aspects'].items():
                p['aspects'][k] = v
        if 'upsc' in enr:
            p['upsc'] = enr['upsc']
        count += 1
        print(f"Successfully enriched Admin/Regional period: {pid}")

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Total admin/regional periods enriched: {count}")
