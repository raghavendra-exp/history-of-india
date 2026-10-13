import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Enrichment mapping for British rule, INC, Gandhi, and Independence
FREEDOM_ENRICHMENTS = {
    'british-colonial-rule': {
        'aspects': {
            'Lord Wellesley & The Subsidiary Alliance (1798–1805)': [
                'Imperial annexation strategy: Designed to subjugate Indian princely states without British financial expenditure; princely state compelled to accept a permanent British subsidiary army stationed in its territory, pay a heavy annual subsidy (or cede fertile territory in perpetuity), expel all European advisors of non-British nationality, conduct external diplomacy only through the British Resident, and surrender sovereign foreign policy.',
                'Chronological accession of states: 1. Nizam of Hyderabad (1798 and 1800 - first state to enter alliance), 2. Mysore (1799, after Fourth Anglo-Mysore War and death of Tipu Sultan), 3. Tanjore (1799), 4. Awadh (1801, ceding Rohilkhand and the fertile Doab), 5. Peshwa Baji Rao II (Treaty of Bassein, 1802), 6. Bhonsle of Nagpur (1803), 7. Scindia of Gwalior (1804).'
            ],
            'Lord Dalhousie & The Doctrine of Lapse (1848–1856)': [
                'Annexation of childless principalities: Stated that if a dependent Indian princely state had no natural male biological heir, the adopted son could inherit the ruler\'s private personal property, but the state sovereignty lapsed automatically to the paramount British Crown.',
                'Annexed states in order: 1. Satara (1848 - first state annexed), 2. Jaitpur and Sambalpur (1849), 3. Baghat (1850), 4. Udaipur (1852), 5. Jhansi (1853 - Gangadhar Rao died, rejecting adopted son Damodar Rao, provoking Rani Lakshmibai\'s 1857 defiance), 6. Nagpur (1854 - royal jewels auctioned off in Calcutta bazaar).',
                'Annexation of Awadh (1856): Nawab Wajid Ali Shah had natural heirs; Dalhousie annexed Awadh on the pretext of "persistent gross misgovernance and maladministration" based on the exaggerated report of Resident Outram; deeply outraged the Bengal Army sepoys (75,000 of whom were recruited from peasant families of Awadh, "the nursery of the Bengal Army").'
            ]
        },
        'upsc': {
            'prelims': [
                'Lord Wellesley introduced the Subsidiary Alliance system in 1798; the Nizam of Hyderabad was the first Indian ruler to accept it.',
                'Under the Doctrine of Lapse introduced by Lord Dalhousie, Satara (1848) was the first princely state to be annexed, followed by Sambalpur, Jhansi (1853), and Nagpur (1854).',
                'Awadh was annexed by Lord Dalhousie in February 1856 on the grounds of "misgovernance" based on the report of British Resident James Outram.',
                'The Treaty of Bassein was signed on 31 December 1802 between Peshwa Baji Rao II and the British East India Company, triggering the Second Anglo-Maratha War.',
                'Tipu Sultan died defending his capital Srirangapatna on 4 May 1799 during the Fourth Anglo-Mysore War against Lord Wellesley.',
                'The Charter Act of 1833 ended all commercial trading monopolies of the East India Company (including tea and trade with China), transforming it purely into an administrative body.',
                'Lord Dalhousie introduced the first electric telegraph line in India in 1853 between Calcutta and Agra.'
            ],
            'mains': [
                'Compare and contrast Lord Wellesley\'s Subsidiary Alliance System and Lord Dalhousie\'s Doctrine of Lapse as instruments of British colonial territorial expansion in India.',
                'Critically examine the annexation of Awadh by Lord Dalhousie in 1856 and analyze its direct role in triggering the Revolt of 1857 among the Bengal Army sepoys.',
                'Discuss the four Anglo-Mysore Wars (1767–1799) and evaluate the military, technological, and diplomatic strategies of Hyder Ali and Tipu Sultan against the British.'
            ]
        }
    },
    'foundation-of-indian-national-congress': {
        'aspects': {
            'Formation & Early Sessions': [
                'Founding Conference (28–31 December 1885): Convened at Gokuldas Tejpal Sanskrit College, Bombay; attended by 72 delegates from across India; presided over by Womesh Chandra Bonnerjee; initiated by retired British civil servant Allan Octavian Hume (A.O. Hume) with the tacit blessing of Viceroy Lord Dufferin.',
                'Theories of origin: 1. "Safety Valve Theory" (advanced by early British observers and later adopted by Lala Lajpat Rai; argued that Hume established the Congress to release dangerous subterranean peasant discontent against British rule peacefully), 2. "Lightning Conductor Theory" (formulated by Gopal Krishna Gokhale; argued that Indian nationalists utilized Hume as an English figurehead to prevent the British government from crushing the infant national organization in its cradle).'
            ],
            'The Moderate Phase (1885–1905)': [
                'Methods of 3Ps (Prayer, Petition, Protest): Firm belief in British sense of justice, fair play, and gradual constitutional reform; leaders: Dadabhai Naoroji, Pherozeshah Mehta, Dinshaw Wacha, Gopal Krishna Gokhale, Surendranath Banerjea, Badruddin Tyabji, Anand Mohan Bose.',
                'Major Contributions & Legacy: Demanded Indianization of higher civil services, separation of judicial and executive powers, freedom of press, expansion of Legislative Councils (achieved in Indian Councils Act 1892), reduction of military expenditure; pioneered the systemic economic critique of colonialism (Drain of Wealth theory); created an all-India secular national consciousness.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Indian National Congress was founded in Bombay in December 1885 under the presidency of Womesh Chandra Bonnerjee, attended by 72 delegates.',
                'The "Safety Valve Theory" regarding the foundation of the Congress was propounded by Lala Lajpat Rai in his work Young India.',
                'Gopal Krishna Gokhale articulated the "Lightning Conductor Theory" regarding A.O. Hume\'s role in the formation of the Congress.',
                'Badruddin Tyabji was the first Muslim president of the Indian National Congress (Madras Session, 1887).',
                'George Yule was the first British president of the Indian National Congress (Allahabad Session, 1888).',
                'Kadambini Ganguly, the first female graduate of Calcutta University, addressed the INC session in 1890, symbolizing the participation of women.',
                'The Indian Councils Act of 1892 introduced indirect elections and the right of legislators to discuss the budget and ask questions.'
            ],
            'mains': [
                'Evaluate the "Safety Valve" and "Lightning Conductor" theories concerning the foundation of the Indian National Congress in 1885.',
                'Critically assess the political philosophy, constitutional methods, and historical achievements of the Moderate nationalists during 1885–1905.',
                'Analyze the economic critique of British imperialism formulated by the early Congress leadership (Dadabhai Naoroji, R.C. Dutt, M.G. Ranade).'
            ]
        }
    },
    'indian-freedom-struggle': {
        'aspects': {
            'Swadeshi & Boycott Movement (1905–1908)': [
                'Partition of Bengal: Announced on 20 July 1905 by Viceroy Lord Curzon; took effect on 16 October 1905 (observed as a day of national mourning, fasting, and Raksha Bandhan brotherly solidarity); intended to divide Bengal on communal lines (Hindu-majority West vs Muslim-majority East).',
                'Mass Mobilization & Methods: Boycott of British Manchester cloth, Liverpool salt, and foreign goods; bonfire of foreign textiles; picketing of shops; Swadeshi enterprises established (Acharya P.C. Ray\'s Bengal Chemical Swadeshi Stores, V.O. Chidambaram Pillai\'s Swadeshi Steam Navigation Company in Tuticorin); National Council of Education and Bengal National College founded (Aurobindo Ghose as principal); Rabindranath Tagore composed "Amar Sonar Bangla" (national anthem of Bangladesh).',
                'Surat Split (1907): Fierce ideological clash between Moderates (Gokhale, Pherozeshah Mehta, Rash Behari Ghosh) and Extremists (Lal-Bal-Pal: Lala Lajpat Rai, Bal Gangadhar Tilak, Bipin Chandra Pal, and Aurobindo Ghose) over extending the boycott movement pan-India; Congress split; Tilak arrested in 1908 and exiled to Mandalay jail for 6 years, composing Gita Rahasya.'
            ],
            'Home Rule League & Revolutionary Surge': [
                'Home Rule League Movement (1916): Launched to demand self-government (Swaraj) within the British Empire on the Irish model; Tilak founded his League at Belgaum (April 1916, operating in Maharashtra except Bombay, Karnataka, Central Provinces, and Berar; proclaimed: "Swaraj is my birthright and I shall have it"); Annie Besant founded her League at Madras (September 1916, covering the rest of India with George Arundale and B.P. Wadia; newspapers New India and Commonweal).',
                'Lucknow Session of INC (1916): Historic twin developments: 1. Re-unification of Moderates and Extremists through efforts of Tilak and Besant, 2. Signing of the Lucknow Pact between Congress and the All India Muslim League (endorsing separate electorates in exchange for joint constitutional demands).'
            ],
            'Rowlatt Act & Jallianwala Bagh Massacre (1919)': [
                'Rowlatt Act (Black Act, March 1919): Anarchical and Revolutionary Crimes Act empowered police to arrest any individual without warrant and detain them for up to 2 years without trial or right of legal appeal ("No Dalil, No Vakil, No Appeal"); Gandhi called for a nationwide Satyagraha Hartal on 6 April 1919.',
                'Jallianwala Bagh Massacre (13 April 1919, Baisakhi Day): Peaceful assembly of 20,000 citizens in an enclosed park in Amritsar protesting the arrest of popular leaders Dr. Saifuddin Kitchlew and Dr. Satyapal; Brigadier-General Reginald Dyer blocked the solitary narrow exit and ordered troops to open fire without warning; fired 1,650 rounds; over 1,000 innocents killed; Rabindranath Tagore renounced his British Knighthood in protest; Gandhi renounced the Kaiser-i-Hind medal; Hunter Commission whitewashed the atrocity.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Partition of Bengal took effect on 16 October 1905 under Lord Curzon, observed across Bengal as a day of mourning and Raksha Bandhan.',
                'The Indian National Congress split into Moderates and Extremists at the Surat Session in 1907, presided over by Rash Behari Ghosh.',
                'V.O. Chidambaram Pillai launched the Swadeshi Steam Navigation Company in 1906 in Tuticorin (Tamil Nadu) to break the British shipping monopoly.',
                'Bal Gangadhar Tilak authored the commentary Gita Rahasya during his six-year imprisonment (1908–1914) in Mandalay jail (Burma).',
                'The Lucknow Pact (1916) between the Congress and the Muslim League was negotiated primarily through the mediation of Bal Gangadhar Tilak and Muhammad Ali Jinnah.',
                'Rabindranath Tagore renounced his British Knighthood in May 1919 in protest against the Jallianwala Bagh massacre.',
                'The British government appointed the Disorders Inquiry Committee (headed by Lord William Hunter) in October 1919 to investigate the Punjab disturbances and Amritsar shootings.'
            ],
            'mains': [
                'Analyze the Swadeshi and Boycott Movement of 1905–1908 as a turning point in India\'s freedom struggle, examining its impact on indigenous industries, education, and literature.',
                'Evaluate the causes and consequences of the Surat Split of 1907 in the Indian National Congress, analyzing why the Moderates and Extremists were unable to maintain organizational unity.',
                'Discuss the objectives, organizational methods, and historical significance of the Home Rule League movements led by Bal Gangadhar Tilak and Annie Besant in 1916.',
                'Examine the events leading up to the Jallianwala Bagh Massacre (1919) and assess its transformative impact on Mahatma Gandhi\'s political strategy toward the British Empire.'
            ]
        }
    },
    'mahatma-gandhi': {
        'aspects': {
            'Early Experiments in South Africa & India': [
                'South African Crucible (1893–1914): Evolved the philosophy of Satyagraha (Soul Force / Truth-Force); established Natal Indian Congress (1894), Phoenix Settlement (1904 near Durban), and Tolstoy Farm (1910 near Johannesburg); published Indian Opinion; fought against the Asiatic Registration Act and poll tax on indentured labourers.',
                'Return to India & Three Local Triumphs: Arrived in India on 9 January 1915 (Pravasi Bharatiya Divas); guided by political mentor Gopal Krishna Gokhale; founded Sabarmati Ashram in Ahmedabad; three regional test-beds: 1. Champaran Satyagraha (1917, Bihar - First Civil Disobedience against Tinkathia indigo exploitation at the invitation of Rajkumar Shukla; secured 25% refund of extorted money), 2. Ahmedabad Mill Strike (1918, Gujarat - First Hunger Strike for 35% plague bonus wage hike for textile workers), 3. Kheda Satyagraha (1918, Gujarat - First Non-Cooperation against revenue collection during crop failure, assisted by Sardar Vallabhbhai Patel).'
            ],
            'Non-Cooperation & Khilafat Movement (1920–1922)': [
                'Mass mobilization: Nagpur Congress Session (December 1920) endorsed the Non-Cooperation resolution and reorganized PCCs on linguistic lines; combined with the Khilafat Movement (led by the Ali Brothers: Shaukat Ali and Mohammad Ali) against the dismemberment of the Ottoman Caliphate by Britain; surrender of British titles (Kaiser-i-Hind), boycott of government schools, law courts, foreign cloth, and elections; promotion of Charkha, Khadi, and Hindu-Muslim unity.',
                'Chauri Chaura Incident (4 February 1922): Violent clash near Gorakhpur (UP) where an agitated crowd locked 22 policemen inside a police station and set it on fire, killing all; Gandhi, asserting that the masses were not yet trained in non-violence, unilaterally suspended the nationwide Non-Cooperation Movement on 12 February 1922 (Bardoli Resolution), prompting severe shock and criticism from younger leaders like Subhas Bose and Nehru.'
            ],
            'Civil Disobedience Movement & Salt Satyagraha (1930–1934)': [
                'Eleven Demands & Dandi Salt March: Viceroy Lord Irwin ignored Gandhi\'s 11-point administrative ultimatum; Gandhi launched the Civil Disobedience Movement with the historic Dandi March (12 March – 6 April 1930) from Sabarmati Ashram to the coastal village of Dandi (240 miles with 78 chosen ashramites); broke the salt monopoly law by picking up a lump of natural sea salt on 6 April 1930.',
                'Pan-Indian Response: Dharasana Salt Works raid (21 May 1930) led by Sarojini Naidu, Imam Saheb, and Manilal Gandhi, brutally beaten by police (reported worldwide by American journalist Webb Miller); C. Rajagopalachari led Vedaranyam Salt March in Tamil Nadu; K. Kelappan led Vaikom to Payyanur march in Malabar; Khan Abdul Ghaffar Khan ("Frontier Gandhi") organized the Khudai Khidmatgars ("Red Shirts") in NWFP; Rani Gaidinliu led the Naga civil disobedience uprising.',
                'Gandhi-Irwin Pact & Poona Pact: Gandhi-Irwin Pact (5 March 1931; Congress suspended CDM to attend the Second Round Table Conference in London); British Prime Minister Ramsay MacDonald announced the Communal Award (August 1932), granting separate electorates for Depressed Classes; Gandhi began a fast unto death in Yerwada Jail; resolved through the Poona Pact (24 September 1932) signed by Dr. B.R. Ambedkar and Madan Mohan Malaviya, which abandoned separate electorates in exchange for reserved seats in provincial legislatures (increased from 71 to 147).'
            ],
            'Quit India Movement (1942)': [
                'Failure of Cripps Mission: Stafford Cripps brought proposals for post-war Dominion Status, termed by Gandhi as a "post-dated cheque on a crashing bank".',
                'Do or Die Ultimatum: All-India Congress Committee met at Gowalia Tank Maidan (August Kranti Maidan), Bombay, passing the historic Quit India Resolution on 8 August 1942; Gandhi declared: "Here is a mantra, a short one, that I give you. The mantra is: Do or Die. We shall either free India or die in the attempt."',
                'Operation Zero Hour & Underground Resistance: All top Congress leaders arrested in pre-dawn raids on 9 August 1942; spontaneous leaderless mass uprising: attacks on railway stations, telegraph lines, post offices; underground networks run by Aruna Asaf Ali, Jayaprakash Narayan, Ram Manohar Lohia, and Usha Mehta (Congress Secret Radio in Bombay); parallel governments (Prati Sarkar): Ballia (UP) under Chittu Pandey ("Sher-e-Ballia"), Tamluk (Midnapore, Bengal) Jatiya Sarkar under Satish Samanta, and Satara (Maharashtra) under Nana Patil.'
            ]
        },
        'upsc': {
            'prelims': [
                'Mahatma Gandhi established the Phoenix Settlement in 1904 near Durban and Tolstoy Farm in 1910 near Johannesburg in South Africa.',
                'Champaran Satyagraha (1917) was Mahatma Gandhi\'s first Civil Disobedience movement in India, organized to protest the Tinkathia system.',
                'Gandhi undertook his first hunger strike in India during the Ahmedabad Mill Strike of 1918 to demand a 35% wage increase for textile workers.',
                'The Bardoli Resolution passed by the Congress Working Committee on 12 February 1922 officially called off the Non-Cooperation Movement following the Chauri Chaura incident.',
                'Mahatma Gandhi embarked on the historic Dandi March on 12 March 1930 with 78 chosen companions, covering 240 miles from Sabarmati to Dandi.',
                'American journalist Webb Miller reported on the brutal British police lathi-charge on peaceful salt marchers at Dharasana Salt Works in May 1930.',
                'The Poona Pact was signed on 24 September 1932 between Dr. B.R. Ambedkar and Madan Mohan Malaviya (on behalf of Gandhi) in Yerwada Jail, abandoning separate electorates for Depressed Classes in favor of increased reserved seats.'
            ],
            'mains': [
                'Critically evaluate Mahatma Gandhi\'s philosophy of Satyagraha, Ahimsa, and Sarvodaya, analyzing how he transformed the Indian national movement into a mass mobilization.',
                'Trace the trajectory of the Civil Disobedience Movement (1930–1934), examining why the salt tax was chosen as the central rallying symbol and assessing its pan-Indian geographical reach.',
                'Analyze the circumstances leading to the Quit India Movement of 1942, evaluating the role of underground resistance networks and parallel governments in sustaining the revolt.',
                'Examine the debate and historical compromise between Mahatma Gandhi and Dr. B.R. Ambedkar leading to the Poona Pact of 1932 regarding political representation for the Depressed Classes.'
            ]
        }
    },
    'independence-of-india': {
        'aspects': {
            'Constitutional Proposals & Deadlocks (1942–1946)': [
                'Wavell Plan & Simla Conference (June 1945): Viceroy Lord Wavell proposed reconstituting the Executive Council with all Indian members (except Commander-in-Chief), maintaining equal representation for Caste Hindus and Muslims; broke down over Jinnah\'s demand that only the Muslim League could nominate Muslim members.',
                'Cabinet Mission Plan (March 1946): Pethick-Lawrence, Stafford Cripps, and A.V. Alexander; rejected full Pakistan; proposed a three-tier loose Union of India with limited central powers (Defence, Foreign Affairs, Communications) and grouping of provinces into Sections A, B, and C; Constituent Assembly to be elected indirectly by provincial assemblies; initially accepted by both Congress and League, but rejected by League after Nehru\'s press statement asserting Constituent Assembly sovereignty.'
            ],
            'Direct Action & The Partition Holocaust': [
                'Direct Action Day (16 August 1946): Muslim League declared Direct Action to enforce Pakistan; Great Calcutta Killings broke out, sparking horrific communal riots in Noakhali, Bihar, and Punjab; Interim Government formed on 2 September 1946 with Jawaharlal Nehru as Vice-President; Liaquat Ali Khan became Finance Minister, deliberately obstructing government work.',
                'Attlee\'s Statement (20 February 1947): British Prime Minister Clement Attlee declared Britain\'s definitive intention to transfer power to responsible Indian hands by June 1948 at the latest; replaced Lord Wavell with Lord Mountbatten as the final Viceroy.'
            ],
            'Mountbatten Plan & Indian Independence Act (1947)': [
                'June 3rd Plan (Mountbatten Plan, 1947): Advanced date of transfer of power to 15 August 1947; proposed partition of British India into two sovereign Dominions: India and Pakistan; legislative assemblies of Bengal and Punjab voted for partition; referendum in NWFP and Sylhet; princely states granted freedom to accede to either dominion or remain independent.',
                'Indian Independence Act 1947 (Enacted 18 July 1947 by British Parliament): Created two independent Dominions of India and Pakistan with effect from 15 August 1947; abolished the office of Viceroy (installing Governor-General) and Secretary of State for India; Boundary Commissions under Sir Cyril Radcliffe drew the boundaries (Radcliffe Line); India celebrated Independence on 15 August 1947 with Nehru\'s immortal "Tryst with Destiny" address.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Cabinet Mission arrived in India in March 1946, comprising Lord Pethick-Lawrence (Secretary of State), Sir Stafford Cripps, and A.V. Alexander.',
                'The Muslim League observed 16 August 1946 as "Direct Action Day", precipitating the communal riots known as the Great Calcutta Killings.',
                'The Interim Government of India was sworn in on 2 September 1946, headed by Jawaharlal Nehru as Vice-President of the Executive Council.',
                'British Prime Minister Clement Attlee announced on 20 February 1947 that the British would transfer power and quit India not later than June 1948.',
                'The Mountbatten Plan, proposing the partition of India into the Dominions of India and Pakistan, was announced on 3 June 1947.',
                'Sir Cyril Radcliffe chaired the two Boundary Commissions appointed to demarcate the boundaries between India and Pakistan in Bengal and Punjab.',
                'The Indian Independence Act was granted royal assent by the British Crown on 18 July 1947.'
            ],
            'mains': [
                'Critically examine the proposals of the Cabinet Mission Plan (1946) and analyze the factors that led to its ultimate rejection by the major political parties.',
                'Discuss the geopolitical and communal factors that made the Partition of India unavoidable by 1947, evaluating the role of the Mountbatten Plan.',
                'Analyze the tragic human consequences of the Radcliffe Line and the partition holocaust in Punjab and Bengal, evaluating the challenges of immediate refugee rehabilitation.'
            ]
        }
    }
}

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

count = 0
for p in d['periods']:
    pid = p['id']
    if pid in FREEDOM_ENRICHMENTS:
        enr = FREEDOM_ENRICHMENTS[pid]
        if 'aspects' in enr:
            p.setdefault('aspects', {})
            for k, v in enr['aspects'].items():
                p['aspects'][k] = v
        if 'upsc' in enr:
            p['upsc'] = enr['upsc']
        count += 1
        print(f"Successfully enriched Freedom Struggle period: {pid}")

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Total freedom struggle periods enriched: {count}")
