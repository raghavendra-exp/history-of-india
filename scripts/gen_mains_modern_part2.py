# scripts/gen_mains_modern_part2.py
import json

def get_modern_part2():
    # 20 Modern Mains Questions (mains_mod_041 to mains_mod_060)
    items = [
        {
            "id": "mains_mod_041", "periodId": "socio-religious-reform", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2018 GS-1", "bookRef": "Spectrum Modern India; Gail Omvedt",
            "question": "Dr. B.R. Ambedkar's crusade was not merely for political representation, but for the moral annihilation of caste and social democracy. Examine his philosophy and key movements.",
            "framework": {
                "intro": "Dr. Bhimrao Ramji Ambedkar (1891-1956) was the preeminent architect of modern Indian social democracy, who maintained that political liberty without social and economic equality is a contradiction in terms.",
                "body": [
                    {"heading": "Institutional Foundations for Dalit Mobilization", "points": [
                        "Founded the 'Bahishkrit Hitakarini Sabha' (1924) with the historic motto: 'Educate, Agitate, Organise'.",
                        "Started Marathi periodicals 'Mooknayak' (Leader of the Silent, 1920) and 'Bahishkrit Bharat' to voice subaltern grievances.",
                        "Founded the Independent Labour Party (1936) and the All India Scheduled Castes Federation (1942)."
                    ]},
                    {"heading": "Direct Action Movements for Civil Rights", "points": [
                        "Mahad Satyagraha (March 1927): Led thousands of Dalits to drink water from the public Chavadar Tank in Mahad, asserting basic human dignity against ritual untouchability.",
                        "Manusmriti Dahan (25 December 1927): Publicly burned the Manusmriti as a symbolic rejection of divinely ordained caste hierarchy.",
                        "Kalaram Temple Entry Satyagraha (Nashik, 1930): Demanded equal right of worship for untouchables."
                    ]},
                    {"heading": "Philosophical Climax: 'Annihilation of Caste' and Constitutional Secularism", "points": [
                        "In his undelivered 1936 address 'Annihilation of Caste', argued that caste is not a division of labour, but a 'division of labourers' based on birth.",
                        "As Chairman of the Drafting Committee of the Indian Constitution, enshrined Fundamental Rights prohibiting discrimination (Article 15), abolishing untouchability (Article 17), and providing affirmative reservations.",
                        "Converted to Buddhism alongside 500,000 followers at Nagpur (1956), choosing a rationalist, egalitarian spiritual path."
                    ]}
                ],
                "diagramMapIdea": "Triad of Ambedkar's Crusade: Socio-Civic Rights (Mahad 1927) + Intellectual Deconstruction (Annihilation of Caste) + Constitutional Guarantees (Articles 15, 17).",
                "conclusion": "Ambedkar bequeathed a revolutionary vision of social democracy where every citizen enjoys equality not as a patronizing gift, but as an inalienable constitutional right."
            }
        },
        {
            "id": "mains_mod_042", "periodId": "left-movement", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2019 GS-1", "bookRef": "Bipan Chandra, Ch. 19; Spectrum",
            "question": "The rise of the Left and Socialist movements in the 1920s and 1930s radicalized the Indian National Congress from within. Critically analyze.",
            "framework": {
                "intro": "Inspired by the 1917 Bolshevik Revolution in Russia and disillusioned by Gandhian compromises, the Indian Left emerged in the 1920s as a potent intellectual force that infused the freedom struggle with socio-economic radicalism.",
                "body": [
                    {"heading": "Emergence of Communist and Socialist Parties", "points": [
                        "M.N. Roy founded the Communist Party of India (CPI) at Tashkent in 1920; formalized on Indian soil at Kanpur (1925) under Satyabhakta and S.A. Dange.",
                        "Young Congress socialists founded the 'Congress Socialist Party' (CSP) in 1934 within the INC, led by Jayaprakash Narayan, Acharya Narendra Dev, Ram Manohar Lohia, and Minoo Masani.",
                        "Aimed to work within Congress to radicalize its bourgeois leadership and orient national policy towards the working class."
                    ]},
                    {"heading": "Transforming the Congress Ideological Agenda", "points": [
                        "Jawaharlal Nehru (Presidential Address, Lucknow 1936) declared: 'I see no way of ending the poverty, the vast unemployment, the degradation of the Indian people except through Socialism.'",
                        "Subhash Chandra Bose established the National Planning Committee (1938) under Nehru to formulate a state-directed industrial economy.",
                        "Karachi Congress Resolution on Fundamental Rights (1931): Enshrined state ownership of key industries, universal franchise, and labour welfare rights."
                    ]},
                    {"heading": "Organizing Working-Class and Peasant Fronts", "points": [
                        "Formed the All India Trade Union Congress (AITUC, 1920 - Lala Lajpat Rai first president, Dewan Chaman Lall general secretary).",
                        "Formed the All India Kisan Sabha (AIKS, 1936) under Swami Sahajanand Saraswati and N.G. Ranga, organizing millions of peasants against landlordism."
                    ]}
                ],
                "diagramMapIdea": "Influence vector: 1917 Russian Revolution -> CPI (1925) & CSP (1934) -> Radicalization of Congress (Karachi 1931, Planning Committee 1938, AIKS 1936).",
                "conclusion": "The Left ensured that Indian independence was not merely a transfer of power from British bureaucrats to Indian capitalists, but a commitment to an egalitarian welfare republic."
            }
        },
        {
            "id": "mains_mod_043", "periodId": "peasant-movements", "marks": 15, "wordLimit": 250, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Bipan Chandra, Ch. 27; Spectrum",
            "question": "Peasant movements in the 1920s-1940s evolved from spontaneous local uprisings into organized class-conscious anti-feudal struggles. Discuss with examples from UP, Gujarat, and Bengal.",
            "framework": {
                "intro": "The interwar period witnessed a qualitative transformation in Indian peasant mobilization, evolving from localized defensive protests into powerful, organized class movements demanding the total abolition of landlordism.",
                "body": [
                    {"heading": "1. Uttar Pradesh: Kisan Sabha and Eka Movement (1920-1922)", "points": [
                        "Awadh Kisan Sabha (1920): Led by Baba Ramchandra, Gauri Shankar Mishra, and Jawaharlal Nehru, protesting against illegal bedakhli (eviction) and high rents.",
                        "Eka (Unity) Movement (1921-1922): Led by lower-caste leader Madari Pasi across Hardoi, Bahraich, and Sitapur; peasants took religious oaths to pay only recorded rents, refuse forced labour (begar), and remain united against eviction."
                    ]},
                    {"heading": "2. Gujarat: Bardoli Satyagraha (1928)", "points": [
                        "Led by Vallabhbhai Patel against a 22% arbitrary increase in land revenue by the Bombay government amidst falling cotton prices.",
                        "Peasants organized disciplined 'Chhavanis' (camps) and refused to pay revenue despite cattle confiscation and land forfeiture.",
                        "Forced the government to appoint Maxwell-Broomfield Commission, which slashed the tax hike to 6.03%. Patel was conferred the title 'Sardar' by the women of Bardoli."
                    ]},
                    {"heading": "3. Bengal: The Tebhaga Movement (1946-1947)", "points": [
                        "Led by Bengal Provincial Kisan Sabha (BPKS); sharecroppers ('Bargadars') demanded two-thirds ('Tebhaga') share of the harvest instead of half from the exploitative landlords ('Jotedars').",
                        "Slogan: 'Nij khamare dhan tolo' (Take paddy to your own threshing floor), representing militant agrarian class assertion on the eve of independence."
                    ]}
                ],
                "diagramMapIdea": "Comparative regional matrix: UP (Eka: Madari Pasi) | Gujarat (Bardoli: Sardar Patel) | Bengal (Tebhaga: 2/3rd share).",
                "conclusion": "The peasant struggles transformed the rural masses from passive subjects into militant citizens, forcing independent India to enact landmark Zamindari Abolition acts."
            }
        },
        {
            "id": "mains_mod_044", "periodId": "women-in-freedom-struggle", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2017 GS-1", "bookRef": "Spectrum Modern India; Bipan Chandra",
            "question": "The Indian National Movement facilitated the largest mass entry of women into the public and political sphere in modern history. Analyze with key personalities across phases.",
            "framework": {
                "intro": "From the armed revolt of 1857 to the Quit India Movement of 1942, women transcended traditional domestic seclusion to become commanders, organizers, journalists, and martyrs in India's struggle for liberation.",
                "body": [
                    {"heading": "Early Martial and International Leadership", "points": [
                        "Rani Lakshmibai of Jhansi and Begum Hazrat Mahal of Awadh: Symbolized unyielding martial resistance in 1857.",
                        "Madam Bhikaiji Cama: Unfurled the first version of the Indian National Flag at the International Socialist Congress in Stuttgart, Germany (1907), internationalizing India's demand for freedom.",
                        "Sarojini Naidu: First Indian woman President of INC (Kanpur session, 1925); led the heroic raid on Dharasana Salt Works (1930)."
                    ]},
                    {"heading": "Mass Participation in Gandhian Movements", "points": [
                        "Non-Cooperation & Civil Disobedience: Millions of ordinary women courted arrest, picketed foreign cloth and liquor shops, and manufactured illegal salt.",
                        "Kamaladevi Chattopadhyay: Persuaded Gandhi to allow women to participate in the Salt Satyagraha; organized underground resistance.",
                        "Kasturba Gandhi and Basanti Devi (wife of C.R. Das) led demonstrations on the front lines."
                    ]},
                    {"heading": "Revolutionary Armed Actions and Underground Leadership", "points": [
                        "Chittagong Armoury Raid (1930): Pritilata Waddedar led the armed assault on the European Club in Pahartali, consuming cyanide to avoid capture; Kalpana Datta fought alongside Surya Sen.",
                        "Bina Das: Shot at Bengal Governor Stanley Jackson during her university convocation (1932).",
                        "Quit India (1942): Aruna Asaf Ali hoisted the tricolour at Gowalia Tank; Usha Mehta operated the underground secret radio; Matangini Hazra (73-year-old) was shot dead holding the tricolour high at Tamluk."
                    ]},
                    {"heading": "Netaji's INA: The Rani of Jhansi Regiment", "points": [
                        "Formed in Singapore (1943) under Captain Lakshmi Sahgal—Asia's first all-women combat infantry regiment."
                    ]}
                ],
                "diagramMapIdea": "Spectrum of Women's Participation: Mass Gandhian picketing (Sarojini, Kamaladevi) + Underground Radio (Usha Mehta) + Armed combat (Pritilata, Captain Lakshmi Sahgal).",
                "conclusion": "Women's participation in the freedom struggle was transformative: it simultaneously liberated the nation from British rule and broke the centuries-old shackles of domestic patriarchy."
            }
        },
        {
            "id": "mains_mod_045", "periodId": "press-and-education", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Bipan Chandra, Ch. 8; Spectrum",
            "question": "The vernacular press in 19th-century colonial India was a powerful engine of nationalist awakening. How did the Vernacular Press Act 1878 attempt to gag it?",
            "framework": {
                "intro": "The Indian nationalist press was not a commercial business, but a sacred national mission. Newspapers in regional languages awakened mass consciousness, prompting Viceroy Lord Lytton to enact the notorious Vernacular Press Act 1878 ('Gagging Act').",
                "body": [
                    {"heading": "Provisions of the 'Gagging Act' (1878)", "points": [
                        "Empowered District Magistrates to call upon printer/publisher of any vernacular paper to enter into a bond not to publish anything likely to excite disaffection against the government.",
                        "Magistrate's decision was final with no right of appeal to a court of law.",
                        "Racial Discrimination: The law applied EXCLUSIVELY to vernacular language papers, leaving English-language papers untouched."
                    ]},
                    {"heading": "Nationalist Ingenuity and Defiance", "points": [
                        "The 'Amrita Bazar Patrika' (edited by Sisir Kumar Ghosh and Motilal Ghosh) overnight converted into an English-language weekly to escape the Act's clutches.",
                        "Bal Gangadhar Tilak used 'Kesari' (Marathi) and 'Mahratta' (English) to boldly attack colonial policies, facing sedition trials (1897 and 1908) with heroic defiance: 'Sedition has become my religion.'"
                    ]},
                    {"heading": "Repeal", "points": [
                        "Widespread outrage forced liberal Viceroy Lord Ripon to unconditionally repeal the Act in 1882."
                    ]}
                ],
                "diagramMapIdea": "Flowchart: Vernacular Press growth -> Lytton's 1878 Gagging Act -> Amrita Bazar Patrika overnight English switch -> Tilak's trials -> Ripon's 1882 repeal.",
                "conclusion": "The battle for press freedom was India's earliest constitutional crusade, establishing the press as the indispensable fourth pillar of Indian democracy."
            }
        },
        {
            "id": "mains_mod_046", "periodId": "press-and-education", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2016 GS-1", "bookRef": "Spectrum Modern India",
            "question": "Colonial educational policy in India aimed at creating 'a class of persons, Indian in blood and colour, but English in taste'. Analyze Macaulay's Minute (1835) and Wood's Despatch (1854).",
            "framework": {
                "intro": "British educational policy was designed not to enlighten the Indian masses, but to train cheap subordinate clerks for colonial bureaucracy while indoctrinating the native elite with Western intellectual superiority.",
                "body": [
                    {"heading": "The Orientalist-Anglicist Controversy and Macaulay's Minute (1835)", "points": [
                        "Orientalists (H.T. Prinsep) favoured classical Sanskrit and Persian learning; Anglicists (Charles Trevelyan) demanded English education.",
                        "T.B. Macaulay resolved the debate in his infamous 1835 Minute, declaring with racist arrogance: 'A single shelf of a good European library was worth the whole native literature of India and Arabia.'",
                        "Objective: Explicitly aimed to create 'a class of persons, Indian in blood and colour, but English in taste, in opinions, in morals, and in intellect.'",
                        "Downward Filtration Theory: Educate only the upper aristocratic classes in English; modern ideas would allegedly 'filter down' to the masses (a theory that failed completely)."
                    ]},
                    {"heading": "Wood's Despatch (1854): The 'Magna Carta of English Education'", "points": [
                        "Authored by Sir Charles Wood; established a structured hierarchy of education across British India.",
                        "Pioneered Primary education in vernaculars, High Schools in Anglo-vernacular, and Universities in English at the apex.",
                        "Recommended establishment of universities on the model of London University at Calcutta, Bombay, and Madras (established in 1857).",
                        "Introduced Grants-in-Aid to encourage private educational enterprises, secular education, and teacher training."
                    ]},
                    {"heading": "Nationalist Reversal of Colonial Intent", "points": [
                        "Instead of becoming loyal colonial subjects, English-educated Indians used Western liberal philosophies (Mill, Rousseau, Voltaire) to deconstruct British tyranny and demand self-rule."
                    ]}
                ],
                "diagramMapIdea": "Educational hierarchy under Wood's Despatch: Universities (English) -> High Schools (Anglo-Vernacular) -> Primary Schools (Vernacular) supported by Grants-in-Aid.",
                "conclusion": "Though engineered to create loyal imperial clerks, English education paradoxically forged a pan-Indian intelligentsia that mobilized modern nationalism to overthrow the empire."
            }
        },
        {
            "id": "mains_mod_047", "periodId": "communalism-and-partition", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2018 GS-1", "bookRef": "Bipan Chandra, Communalism in Modern India",
            "question": "Trace the growth of communalism in modern India from elite competitive politics to mass communal hysteria, leading to the Two-Nation Theory.",
            "framework": {
                "intro": "Bipan Chandra defines communalism as the false belief that people following the same religion share identical political, economic, and social interests distinct from other religious groups. It evolved across three distinct stages in colonial India.",
                "body": [
                    {"heading": "Stage 1: Communal Consciousness and Elite Rivalry (Late 19th c.)", "points": [
                        "Rooted in unequal modernization: Muslim elite lagged behind Hindu elite in English education and government jobs.",
                        "Sir Syed Ahmad Khan and the Aligarh movement initially advocated modern education, but later advised Muslims to remain aloof from the Congress, viewing British rule as a safeguard against Hindu majority dominance.",
                        "Colonial government weaponized this through 'Divide and Rule', actively encouraging the formation of the All-India Muslim League in 1906."
                    ]},
                    {"heading": "Stage 2: Liberal / Institutional Communalism (1909-1937)", "points": [
                        "Morley-Minto Reforms (1909) institutionalized separate electorates; reinforced by Lucknow Pact (1916) and 1919/1935 Acts.",
                        "Rise of religious revivalist mobilization: Shuddhi and Sangathan movements (Hindu Mahasabha) countered by Tabligh and Tanzim.",
                        "Elite horse-trading: Communal leaders bargained for reserved legislative seats and government job quotas rather than addressing peasant poverty."
                    ]},
                    {"heading": "Stage 3: Extreme / Fascist Communalism and Two-Nation Theory (1937-1947)", "points": [
                        "Following crushing defeat in the 1937 elections, Jinnah and the League radicalized politics, claiming that 'Islam is in danger' under Hindu Congress Raj.",
                        "Lahore Resolution (March 1940): Officially demanded sovereign 'Pakistan', articulating the Two-Nation Theory that Hindus and Muslims were two separate civilizations.",
                        "Direct Action Day (1946) unleashed mass street violence, transforming elite constitutional bargaining into uncontrollable communal slaughter."
                    ]}
                ],
                "diagramMapIdea": "Three-Stage Staircase of Communalism: Stage 1: Elite Job Rivalry (1880s) -> Stage 2: Separate Electorates & Bargaining (1909-37) -> Stage 3: Two-Nation Theory & Direct Action (1940-47).",
                "conclusion": "Communalism was neither ancient nor theological, but a modern socio-political pathology engineered by elite vested interests and nurtured by colonial divide-and-rule."
            }
        },
        {
            "id": "mains_mod_048", "periodId": "freedom-struggle-climax", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Spectrum Modern India",
            "question": "Evaluate the 'August Offer' (1940) and the 'Cripps Mission' (1942). Why were both rejected by the Indian National Congress?",
            "framework": {
                "intro": "During World War II, facing Axis advances, Britain made two desperate constitutional overtures—the August Offer (1940) and Cripps Mission (1942)—both of which collapsed due to Indian rejection.",
                "body": [
                    {"heading": "The August Offer (1940 - Lord Linlithgow)", "points": [
                        "Proposed: Dominion Status at an unspecified future date; expansion of Viceroy's Executive Council; Constituent Assembly after the war.",
                        "Fatal Minority Veto: Explicitly guaranteed that Britain would not transfer power to any system whose authority is denied by powerful minority elements (giving Jinnah a veto on constitutional progress).",
                        "Rejected: Nehru famously retorted: 'Dominion status concept is dead as a doornail.' Gandhi launched Individual Satyagraha (Vinoba Bhave first satyagrahi)."
                    ]},
                    {"heading": "The Cripps Mission (March 1942 - Sir Stafford Cripps)", "points": [
                        "Dispatched under American pressure as Japanese forces reached the Andaman Islands.",
                        "Proposed: Dominion Status after the war; Constituent Assembly; right of any province not willing to accept the constitution to secede and form a separate union.",
                        "Rejected: Congress rejected the right of provinces to secede as a blueprint for balkanization. Gandhi called it a 'Post-dated cheque on a crashing bank.'",
                        "Directly led to the launch of the Quit India Movement in August 1942."
                    ]}
                ],
                "diagramMapIdea": "Failure timeline: August Offer 1940 (Minority Veto) -> Cripps Mission 1942 (Secession clause) -> Quit India Movement (Aug 1942).",
                "conclusion": "Both offers came too late with too little: when Britain offered Dominion Status, India was already prepared to accept nothing less than complete Purna Swaraj."
            }
        },
        {
            "id": "mains_mod_049", "periodId": "freedom-struggle-climax", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Spectrum Modern India",
            "question": "Explain why the Shimla Conference (1945) and the Wavell Plan collapsed over the issue of communal representation.",
            "framework": {
                "intro": "Convened by Viceroy Lord Wavell in June 1945 at Shimla, the Shimla Conference sought to reconstitute the Executive Council with Indian leaders to resolve the wartime constitutional deadlock.",
                "body": [
                    {"heading": "Proposals of the Wavell Plan", "points": [
                        "Reconstruction of the Governor-General's Executive Council, with all members being Indians except the Viceroy and Commander-in-Chief.",
                        "Equal representation for Caste Hindus and Muslims (parity in the council).",
                        "Governor-General to retain veto power, but promised to use it sparingly."
                    ]},
                    {"heading": "The Irreconcilable Stumbling Block", "points": [
                        "Jinnah insisted that the Muslim League held the exclusive monopoly to nominate all Muslim members to the council.",
                        "Congress (led by Congress President Maulana Abul Kalam Azad) vehemently rejected this claim, maintaining that Congress was a secular pan-Indian national body that included Muslims, Christians, and Sikhs, refusing to be reduced to a purely 'Hindu' party.",
                        "Wavell allowed Jinnah a virtual veto, summarily abandoning the conference."
                    ]},
                    {"heading": "Historical Consequence", "points": [
                        "Strengthened Jinnah's political standing, demonstrating that the British government would not finalize any settlement without League approval."
                    ]}
                ],
                "diagramMapIdea": "Deadlock vector: Wavell Plan (Hindu-Muslim Parity) -> Jinnah demands total Muslim nomination monopoly -> Congress defends secular status -> Conference collapse.",
                "conclusion": "Wavell's capitulation to Jinnah's veto at Shimla emboldened the League to take an uncompromising stance, making partition the inevitable outcome."
            }
        },
        {
            "id": "mains_mod_050", "periodId": "freedom-struggle-climax", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Bipan Chandra; Sugata Bose",
            "question": "The Tripuri Crisis of 1939 highlighted deep ideological cleavages between Gandhian gradualism and Left-wing radicalism within the Indian National Congress. Discuss.",
            "framework": {
                "intro": "The 1939 Tripuri session of the INC witnessed an unprecedented internal crisis between Subhash Chandra Bose and Mahatma Gandhi, exposing profound philosophical differences over the future of the freedom struggle.",
                "body": [
                    {"heading": "The Presidential Election of 1939", "points": [
                        "Bose stood for re-election as Congress President on an anti-imperial, radical Left socialist platform, defying the conservative 'Old Guard'.",
                        "Gandhi sponsored Pattabhi Sitaramayya. Bose won a stunning victory by 1,580 to 1,377 votes.",
                        "Gandhi publicly declared: 'Pattabhi's defeat is my defeat.'",
                        "Thirteen members of the Congress Working Committee resigned, creating a total administrative paralysis."
                    ]},
                    {"heading": "The Pant Resolution and Bose's Resignation", "points": [
                        "Govind Ballabh Pant moved a resolution mandating that the President must appoint the Working Committee in accordance with Gandhi's wishes.",
                        "Gandhi refused to nominate members, leaving Bose without an executive team.",
                        "Unwilling to divide the national movement on the eve of World War II, Bose resigned the Presidency in April 1939 and formed the 'Forward Bloc' within the Congress."
                    ]},
                    {"heading": "Underlying Ideological Divide", "points": [
                        "Gandhi believed in non-violent moral conversion and gradual mass mobilization; Bose believed in seizing international wartime opportunities for armed revolutionary assault."
                    ]}
                ],
                "diagramMapIdea": "Tripuri Crisis timeline: Bose re-elected (1939) -> Gandhi's 'My defeat' statement -> Pant Resolution -> Bose resigns -> Foundation of Forward Bloc.",
                "conclusion": "Though parting ways politically, both leaders shared supreme mutual respect: Bose was the first to address Gandhi as 'Father of the Nation' (1944), while Gandhi hailed Bose as the 'Patriot of Patriots'."
            }
        },
        {
            "id": "mains_mod_051", "periodId": "freedom-struggle-climax", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Sugata Bose; Spectrum",
            "question": "Examine the significance of the Rani of Jhansi Regiment of the Azad Hind Fauj in revolutionizing women's combat roles in Asian military history.",
            "framework": {
                "intro": "Formed in Singapore in July 1943 by Netaji Subhash Chandra Bose and commanded by Captain Lakshmi Sahgal (Swaminathan), the Rani of Jhansi Regiment was Asia's first all-female combat infantry unit.",
                "body": [
                    {"heading": "Recruitment and Military Training", "points": [
                        "Composed of over 1,000 young Indian women from the South Indian diaspora working on rubber plantations in Malaya, Burma, and Singapore.",
                        "Underwent rigorous infantry training: bayonet fighting, tactical maneuvers, machine guns, grenades, and jungle warfare under the same conditions as male soldiers."
                    ]},
                    {"heading": "Frontline Service in Burma", "points": [
                        "Deployed to Burma during the Imphal-Kohima offensive; served under air bombardments, providing combat defense, nursing wounded soldiers, and guarding retreats."
                    ]},
                    {"heading": "Socio-Political Legacy", "points": [
                        "Shattered traditional gender orthodoxies that relegated women to domestic supportive roles.",
                        "Presented a radical egalitarian image of Indian womanhood to the world, proving that women were ready to shed blood on the battlefield for national sovereignty."
                    ]}
                ],
                "diagramMapIdea": "Concept map: Diaspora women volunteers -> Rigorous military infantry training -> Frontline deployment in Burma -> Pioneer of women in combat.",
                "conclusion": "The Rani of Jhansi Regiment stands as a glorious testament to female valour, inspiring generations of Indian women to claim their rightful place in national defense."
            }
        },
        {
            "id": "mains_mod_052", "periodId": "peasant-movements", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Bipan Chandra; Ramachandra Guha",
            "question": "The Telangana Peasant Armed Struggle (1946-1951) was India's largest anti-feudal guerrilla insurrection. Discuss its causes, achievements, and impact on land reforms.",
            "framework": {
                "intro": "Erupting in July 1946 against the brutal feudal landlordism of the Nizam of Hyderabad and the Razakars, the Telangana movement was a massive communist-led armed agrarian revolt covering 3,000 villages.",
                "body": [
                    {"heading": "Causes of the Uprising", "points": [
                        "Vetti Chakiri: Widespread forced unpaid labour extracted from lower-caste peasants by oppressive feudal landlords ('Deshmukhs' and 'Jagirdars').",
                        "Illegal land evictions (Bedakhli) and exorbitant grain levies amidst post-war inflation.",
                        "The martyrdom of peasant Doddi Komarayya in July 1946 sparked the armed explosion."
                    ]},
                    {"heading": "Gains and Achievements of the Guerrillas", "points": [
                        "Liberated 3,000 villages, distributing over 1 million acres of landlord land to landless agricultural labourers.",
                        "Formed village soviets ('Gram Rajyams'), abolished Vetti, fixed agricultural wages, and instituted women's self-defense squads.",
                        "Fought a heroic guerrilla resistance against Kasim Razvi's brutal fascist Razakar militia."
                    ]},
                    {"heading": "Impact on Modern Land Reforms", "points": [
                        "Directly inspired Acharya Vinoba Bhave to launch the 'Bhoodan Movement' (1951) from Pochampally (Telangana).",
                        "Forced the Indian government to accelerate tenancy protection and land ceiling legislations across independent India."
                    ]}
                ],
                "diagramMapIdea": "Flowchart: Vetti exploitation -> Peasant uprising (1946) -> 1 million acres distributed -> Inspiration for Bhoodan Movement (1951).",
                "conclusion": "Telangana was India's historic peasant revolution: an armed strike against landlordism that placed radical agrarian reform at the heart of free India's political agenda."
            }
        },
        {
            "id": "mains_mod_053", "periodId": "peasant-movements", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Bipan Chandra, Ch. 27",
            "question": "Examine the demands, methods, and significance of the Tebhaga Movement (1946-1947) in Bengal.",
            "framework": {
                "intro": "On the eve of independence in 1946-47, North and East Bengal witnessed the historic 'Tebhaga Movement' launched by the Bengal Provincial Kisan Sabha, mobilizing sharecroppers against landlord exploitation.",
                "body": [
                    {"heading": "Core Demand: Two-Thirds Share ('Tebhaga')", "points": [
                        "Traditionally, sharecroppers ('Bargadars') surrendered 50% of the harvest to the non-cultivating landlord ('Jotedar'), despite bearing all costs of seeds, ploughs, and fertilizer.",
                        "Bargadars demanded the implementation of the Flood Commission Recommendation: two-thirds (2/3rd) share of the crop for the tiller, and only one-third (1/3rd) for the landlord."
                    ]},
                    {"heading": "Methods and Women's Active Role", "points": [
                        "Peasants refused to store harvested paddy in Jotedars' granaries, taking it directly to their own threshing floors under the battle cry: 'Tebhaga Chai!' (We want two-thirds!).",
                        "Peasant women formed 'Nari Bahinis' armed with broomsticks and rolling pins, standing guard against police raids and defending grain stores."
                    ]},
                    {"heading": "Significance", "points": [
                        "Maintained complete communal harmony between Hindu, Muslim, and Rajbanshi sharecroppers at the height of partition communal riots in Calcutta.",
                        "Laid the agrarian foundation for the post-independence Bargadar tenancy reforms (Operation Barga in West Bengal)."
                    ]}
                ],
                "diagramMapIdea": "Sharecropper crop-split diagram: Traditional 50:50 vs Tebhaga 2/3rd (Tiller) : 1/3rd (Landlord).",
                "conclusion": "The Tebhaga movement proved that economic class solidarity could transcend religious fanaticism even during the darkest hours of communal frenzy."
            }
        },
        {
            "id": "mains_mod_054", "periodId": "tribal-and-peasant-uprisings", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Spectrum Modern India",
            "question": "The Warli Adivasi Revolt (1945-1947) in Maharashtra was a struggle against debt slavery and sexual exploitation. Elucidate with reference to Godavari Parulekar.",
            "framework": {
                "intro": "Led by communist leader Godavari Parulekar and the Kisan Sabha in the Thane district of Maharashtra, the Warli Adivasi Revolt (1945) was an epic struggle against debt bondage, serfdom, and landlord violence.",
                "body": [
                    {"heading": "System of Inhuman Exploitation", "points": [
                        "Warlis were trapped in perpetual debt-slavery ('Vethbigar') by forest contractors and landlords, working generation after generation without wages for a small ancestral grain loan.",
                        "Landlords claimed feudal rights over Adivasi women ('Lagangadi' system)."
                    ]},
                    {"heading": "Godavari Parulekar's Leadership and Resistance", "points": [
                        "Godavari Parulekar (affectionately called 'Godutai') mobilized thousands of illiterate tribal men and women.",
                        "Adivasis struck work: refused to cut timber for contractors, stopped bonded labour, and demanded minimum daily cash wages.",
                        "When police opened fire killing several Warlis at Talwada, the Adivasis remained non-violent and completely unified."
                    ]},
                    {"heading": "Historic Gains", "points": [
                        "Abolished Vethbigar debt-slavery across the Thane forest belt, enforced minimum wages, and restored human dignity to an ancient indigenous community."
                    ]}
                ],
                "diagramMapIdea": "Flowchart: Vethbigar debt serfdom -> Godavari Parulekar's mobilization -> Warli timber strike -> Abolition of bonded labour.",
                "conclusion": "The Warli revolt demonstrated that subaltern indigenous communities, when organized around class consciousness, can shatter centuries of feudal bondage."
            }
        },
        {
            "id": "mains_mod_055", "periodId": "economic-nationalism", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Bipan Chandra; Spectrum",
            "question": "Analyze the complex relationship between Indian industrial capitalists and the national movement. Discuss the vision of the Bombay Plan (1944).",
            "framework": {
                "intro": "Unlike the comprador bourgeoisie in other colonial societies, Indian indigenous capitalists (G.D. Birla, Jamnalal Bajaj, Purshottamdas Thakurdas) maintained a complex relationship of financial support and tactical caution toward the national movement.",
                "body": [
                    {"heading": "Financial Support and Nationalist Sympathy", "points": [
                        "Indian capitalists financed Congress activities, khadi institutions, and supported the Swadeshi boycott of foreign goods, which directly protected domestic cotton mills from Manchester competition.",
                        "However, they feared radical mass movements and strikes that threatened private property, consistently advising Gandhi to compromise (e.g., Gandhi-Irwin Pact 1931)."
                    ]},
                    {"heading": "The Bombay Plan (1944): Blueprint for National Industrialization", "points": [
                        "Drafted in 1944 by 8 leading industrialists (including J.R.D. Tata, G.D. Birla, Kasturbhai Lalbhai, and John Mathai).",
                        "Key Vision: Advocated massive state intervention and public sector investment in heavy infrastructure (steel, power, transport) where private capital was inadequate.",
                        "Called for central economic planning, land reform, and social welfare programs to create a vibrant domestic consumer market."
                    ]},
                    {"heading": "Convergence with Post-Independence Policy", "points": [
                        "Prefigured the 'Mixed Economy' model adopted in Nehru's Five-Year Plans, where the state built heavy industry while leaving consumer goods to private enterprise."
                    ]}
                ],
                "diagramMapIdea": "Triangle of Indian Capitalist strategy: Support Swadeshi & Congress -> Resist Communist radicalism -> Demand State Infrastructure (Bombay Plan).",
                "conclusion": "The Indian capitalist class astutely utilized nationalism to break foreign monopolies, laying the framework for independent India's planned mixed economy."
            }
        },
        {
            "id": "mains_mod_056", "periodId": "british-economic-impact", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Daniel Thorner; Bipan Chandra",
            "question": "The construction of railways in colonial India was 'private enterprise at public risk'. Critically analyze.",
            "framework": {
                "intro": "Introduced in 1853 under Lord Dalhousie, the Indian railways were hailed by colonialists as modernizing wonders, but economic historian Daniel Thorner characterized their financial construction as 'private enterprise at public risk'.",
                "body": [
                    {"heading": "The Guarantee System: Risk-Free British Profiteering", "points": [
                        "British railway companies were guaranteed a fixed 5% return on capital investments paid out of Indian tax revenues, regardless of operating losses.",
                        "Encouraged reckless waste and corruption: British companies built railways at astronomical costs (nearly £18,000 per mile compared to £4,000 in Australia or USA), knowing that the Indian peasant would fund any deficit."
                    ]},
                    {"heading": "Colonial-Imperial Design over National Needs", "points": [
                        "Rail lines connected inland agricultural heartlands directly to coastal export ports (Bombay, Calcutta, Madras) to siphon off raw materials (cotton, food grains) to Britain.",
                        "Freight rates discriminated against Indian indigenous manufacturers: shipping imported goods from ports to hinterlands was cheaper than shipping Indian manufactured goods between two domestic cities."
                    ]},
                    {"heading": "Military Imperative", "points": [
                        "Designed primarily for rapid military troop deployment to northwestern frontiers and internal suppression of rebellions."
                    ]}
                ],
                "diagramMapIdea": "Colonial Railway Routing map: Raw materials drawn from Hinterlands -> Ports -> London; Finished goods distributed backwards.",
                "conclusion": "Karl Marx famously remarked that the British laid railways in India not to develop the country, but to facilitate imperial exploitation: a modernization subsidized by Indian sweat for British imperial profit."
            }
        },
        {
            "id": "mains_mod_057", "periodId": "cultural-nationalism", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "NCERT Class 10; Bipan Chandra",
            "question": "Examine the role of vernacular literature and patriotic poetry in inspiring anti-colonial consciousness in 19th and 20th-century India.",
            "framework": {
                "intro": "Indian nationalism found its soul in vernacular literature, where novelists, bards, and playwrights forged an emotional anti-colonial consciousness across regional linguistic communities.",
                "body": [
                    {"heading": "Bengali: Bankim Chandra and Rabindranath Tagore", "points": [
                        "Bankim Chandra Chattopadhyay: In his political novel 'Anandamath' (1882), composed the immortal national hymn 'Vande Mataram', elevating the motherland to divine status as Bharat Mata.",
                        "Rabindranath Tagore: Composed patriotic songs during Swadeshi ('Amar Sonar Bangla', 'Jana Gana Mana'), awakening cultural pride."
                    ]},
                    {"heading": "Tamil: Mahakavi Subramania Bharati", "points": [
                        "Wrote fiery nationalist poems in vernacular Tamil ('Achamillai, Achamillai' - We Fear Nothing), calling for freedom, caste abolition, and women's liberation."
                    ]},
                    {"heading": "Hindi and Urdu: Munshi Premchand and Iqbal", "points": [
                        "Munshi Premchand: In short stories and novels ('Godan', 'Kafan', 'Rangbhoomi'), laid bare the brutal exploitation of the peasant by British collectors, zamindars, and moneylenders.",
                        "Allama Iqbal: Composed the enduring anthem of communal fraternity: 'Saare Jahan Se Achha Hindostan Hamara' (1904)."
                    ]}
                ],
                "diagramMapIdea": "Regional literary web: Bankim (Vande Mataram - Bengal) <--> Bharati (Achamillai - Tamil Nadu) <--> Premchand (Peasant realism - Hindi Heartlands).",
                "conclusion": "Vernacular literature democratized the freedom struggle: it translated abstract constitutional ideas into the poetic heartbeat of ordinary peasants, inspiring fearless sacrifice."
            }
        },
        {
            "id": "mains_mod_058", "periodId": "princely-states-movement", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Bipan Chandra, Ch. 28",
            "question": "The Praja Mandal movements bridged the artificial divide between British India and the Princely States. Discuss their objectives and struggles.",
            "framework": {
                "intro": "While British India was aflame with anti-colonial agitations, nearly two-fifths of India's land was ruled by autocratic princes. The 'Praja Mandals' (States People's Conferences) organized mass movements for democratic rights within princely domains.",
                "body": [
                    {"heading": "The All-India States People's Conference (AISPC, 1927)", "points": [
                        "Founded in Bombay (1927) to coordinate democratic struggles across hundreds of princely states.",
                        "Demanded: Responsible representative government, civil liberties, abolition of forced labour (Veth), and merger of princely revenues with state budgets.",
                        "Jawaharlal Nehru was elected President of AISPC in 1939, officially cementing the organic alliance between the Congress and the people of princely states."
                    ]},
                    {"heading": "Heroic Struggles against Royal Autocracy", "points": [
                        "Mysore, Travancore, Kashmir, and Hyderabad: Massive protests against autocratic royal misrule and police brutality.",
                        "In Travancore, C.P. Ramaswamy Aiyar attempted an 'American Model' of autocracy; crushed by the militant Punnapra-Vayalar communist uprising (1946)."
                    ]},
                    {"heading": "Crucial Role in National Integration", "points": [
                        "When Sardar Patel initiated integration in 1947, the surging democratic unrest organized by Praja Mandals made it impossible for princes to stay independent."
                    ]}
                ],
                "diagramMapIdea": "Integration axis: AISPC (Praja Mandals) -> Democratic agitation within Princely States -> Convergence with Congress -> Facilitating Sardar Patel's Integration.",
                "conclusion": "The Praja Mandal movements ensured that Indian independence was not just the liberation of British provinces, but the democratic emancipation of all subjects across princely India."
            }
        },
        {
            "id": "mains_mod_059", "periodId": "post-independence", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2015 GS-1", "bookRef": "Bipan Chandra, India Since Independence; Ramachandra Guha",
            "question": "Jawaharlal Nehru's policy of Non-Alignment was not passive neutrality, but an assertive, moral foreign policy rooted in India's anti-colonial heritage. Critically analyze.",
            "framework": {
                "intro": "Emerging into independence amidst the ideological hostility of the Cold War (USA vs USSR), Prime Minister Jawaharlal Nehru pioneered the Non-Aligned Movement (NAM), charting an independent, sovereign path for newly liberated post-colonial nations.",
                "body": [
                    {"heading": "Non-Alignment vs Neutrality", "points": [
                        "Nehru explicitly clarified: 'Where freedom is menaced or justice threatened or where aggression takes place, we cannot and shall not be neutral.'",
                        "Non-alignment was not passive isolationism; it meant the sovereign prerogative to judge every international issue independently on its merits, without being tethered to military bloc dictates (NATO or Warsaw Pact)."
                    ]},
                    {"heading": "The Panchsheel Principles (1954)", "points": [
                        "Codified in the Sino-Indian Agreement of 1954: 1. Mutual respect for territorial integrity and sovereignty; 2. Mutual non-aggression; 3. Mutual non-interference in internal affairs; 4. Equality and mutual benefit; 5. Peaceful coexistence.",
                        "Became the moral template for the 1955 Bandung Conference and the formal launch of NAM at Belgrade in 1961 (alongside Tito, Nasser, Sukarno, Nkrumah)."
                    ]},
                    {"heading": "Active Peacemaking and Global Mediations", "points": [
                        "Mediated the Korean War armistice (1953), with India chairing the Neutral Nations Repatriation Commission (NNRC).",
                        "Active diplomacy during the Suez Crisis (1956), denouncing Anglo-French aggression, and mediating the Congo crisis."
                    ]},
                    {"heading": "Strategic Challenges and Criticisms", "points": [
                        "Critics highlighted ideological idealism over hard realpolitik, culminating in military vulnerability during the 1962 Sino-Indian War.",
                        "However, NAM allowed India to receive economic and military assistance from both superpowers while retaining sovereign foreign policy autonomy."
                    ]}
                ],
                "diagramMapIdea": "Panchsheel pentagon diagram showing the five foundational principles of peaceful coexistence.",
                "conclusion": "Nehru's Non-Alignment gave the global South a united collective voice, transforming post-colonial nations from pawns in superpower chess into active architects of world peace."
            }
        },
        {
            "id": "mains_mod_060", "periodId": "post-independence", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2020 GS-1", "bookRef": "Bipan Chandra, India Since Independence",
            "question": "Analyze the ideological rationale and socio-economic outcomes of the Nehru-Mahalanobis strategy of heavy industrialization in early post-independence India.",
            "framework": {
                "intro": "Facing mass poverty, de-industrialization, and structural stagnation at independence, India under Jawaharlal Nehru adopted democratic planned development, crystallized in the landmark Second Five-Year Plan (1956-1961) based on the Nehru-Mahalanobis Model.",
                "body": [
                    {"heading": "Core Rationale of the Mahalanobis Model", "points": [
                        "Formulated by statistician P.C. Mahalanobis; prioritized massive public sector investments in heavy, capital-goods industries ('Machines to make machines') rather than consumer goods.",
                        "Rationale: True national economic sovereignty required breaking dependency on foreign capital goods for steel, heavy machinery, power generation, and chemicals.",
                        "Public Sector commanding the 'Commanding Heights of the Economy': private capital was too weak, risk-averse, and small to finance multi-crore infrastructure projects."
                    ]},
                    {"heading": "Creation of the 'Temples of Modern India'", "points": [
                        "Construction of colossal multipurpose river valley projects: Bhakra Nangal, Damodar Valley Corporation (DVC), and Hirakud.",
                        "Establishment of world-class public sector steel plants: Rourkela (German aid), Bhilai (Soviet aid), and Durgapur (British aid).",
                        "Creation of scientific and technical institutions: Indian Institutes of Technology (IITs), Atomic Energy Commission under Homi Bhabha, and CSIR laboratories."
                    ]},
                    {"heading": "Achievements and Structural Pitfalls", "points": [
                        "Achievements: Built a self-reliant industrial and technological foundation that shielded India from foreign economic blackmail.",
                        "Pitfalls: Neglected agriculture and rural irrigation, leading to severe food deficits and humiliating dependency on US PL-480 wheat imports in the 1960s; bureaucratic licensing ('License-Permit Raj') bred inefficiencies."
                    ]}
                ],
                "diagramMapIdea": "Mahalanobis Model Flowchart: Public Investment in Capital Goods (Steel, Power) -> Domestic Heavy Machinery -> Long-term Industrial Self-Reliance.",
                "conclusion": "Despite agrarian imbalances, the Nehru-Mahalanobis vision created the indispensable scientific, metallurgical, and technological steel frame that made India a modern industrial power."
            }
        }
    ]

    return items
