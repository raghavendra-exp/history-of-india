import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Enrichment mapping for Post-Independence, World History, and Mughal Empire
POST_AND_WORLD_ENRICHMENTS = {
    'mughal-empire': {
        'aspects': {
            'Mughal Institutional Matrix & Composite Culture': [
                'Imperial state apparatus: Bureaucratic centralization balanced with regional diversity; royal sovereign as "Zill-i-Ilahi" (Shadow of God) governing under the moral ethos of Sulh-i-Kul (universal peace); administrative hierarchy from Subah (province) to Sarkar (district) and Pargana (sub-district).',
                'Mansabdari & Jagirdari interdependence: Civil and military administration integrated through the Mansabdari system; Mansabdars paid via temporary revenue assignments (Jagirs), preventing feudal landed entrenchment through periodic transfers every 3–4 years.',
                'Composite architectural and artistic heritage: Synthesis of Persian, Central Asian, and indigenous Indian traditions in architecture (Charbagh, red sandstone, white marble, double dome, pietra dura) and miniature painting (Mughal atelier fusing Persian delicacy with Indian vitality).'
            ]
        },
        'upsc': {
            'prelims': [
                'The Mughal administrative province was called a "Subah", headed by a Subahdar, while financial administration was independently directed by the provincial Diwan.',
                'Under the Mughal Jagirdari system, the land whose revenue was reserved directly for the imperial treasury was called "Khalisa", whereas land assigned to Mansabdars was termed "Jagir".',
                'The revenue assessment manual and administrative encyclopaedia of Akbar\'s empire, Ain-i-Akbari, was authored by Abul Fazl as the third volume of the Akbarnama.',
                'The bilingual silver coin carrying the Sanskrit translation "Avyaktamekam" alongside Arabic Kalima was minted by Mahmud of Ghazni, not the Mughals; the standard Mughal silver coin was the Rupiya.',
                'The custom of "Jharokha Darshan" (daily appearance on the palace balcony) was introduced by Akbar to build personal rapport with common subjects.',
                'Mughal miniature paintings reached their peak of naturalism and portraiture under Jahangir, while architectural monumentality peaked under Shah Jahan.',
                'The Battle of Tukaroi (1575) resulted in the annexation of Bengal and Bihar into the Mughal Empire by Akbar.'
            ],
            'mains': [
                'Critically evaluate the structural relationship between the Mansabdari system and the Jagirdari system in sustaining the fiscal and military power of the Mughal Empire.',
                'Analyze the evolution of the concept of sovereignty in the Mughal state from Babur to Akbar and Aurangzeb.',
                'Discuss the composite cultural synthesis (Ganga-Jamuni Tehzeeb) achieved under Mughal rule in the realms of language, music, painting, and architecture.'
            ]
        }
    },
    'independent-india-overview': {
        'aspects': {
            'Integration of Princely States & Sardar Patel': [
                'Integration miracle: 565 autonomous princely states covered 48% of Indian territory; Ministry of States created in June 1947 under Sardar Vallabhbhai Patel ("Iron Man of India") and Secretary V.P. Menon; persuaded rulers to sign the Instrument of Accession, ceding Defence, External Affairs, and Communications in exchange for guaranteed Privy Purses.',
                'Three recalcitrant states: 1. Junagadh (Nawab acceded to Pakistan despite 80% Hindu population; people revolted, Nawab fled to Karachi, plebiscite held in Feb 1948 voted 99% for India), 2. Hyderabad (Nizam wanted sovereign independence; Razakar paramilitary terrorized citizens; Government of India launched "Operation Polo" police action on 13 September 1948, forcing Nizam to surrender on 17 September), 3. Jammu & Kashmir (Maharaja Hari Singh signed Standstill Agreement; Pakistani tribal raiders invaded; Maharaja signed Instrument of Accession on 26 October 1947; Indian army airlifted to Srinagar).'
            ],
            'Framing the Republic & Planning Architecture': [
                'Constituent Assembly: Formed under Cabinet Mission Plan; first met on 9 December 1946 (Dr. Sachchidananda Sinha as temporary chairman; Dr. Rajendra Prasad elected permanent president on 11 Dec); Drafting Committee headed by Dr. B.R. Ambedkar; took 2 years, 11 months, and 18 days to draft the Constitution; adopted on 26 November 1949 (Constitution Day) and enacted on 26 January 1950 (commemorating 1930 Purna Swaraj day).',
                'Planning Commission & Scientific Infrastructure: Planning Commission established in March 1950 (Jawaharlal Nehru as chairman); launched First Five-Year Plan (1951–56, Harrod-Domar model focused on agriculture and irrigation dams: Bhakra Nangal, Hirakud, Damodar Valley); established Indian Institutes of Technology (IIT Kharagpur 1951), University Grants Commission (UGC), All India Institute of Medical Sciences (AIIMS 1956), and Atomic Energy Commission under Dr. Homi J. Bhabha.'
            ]
        },
        'upsc': {
            'prelims': [
                'Sardar Vallabhbhai Patel and V.P. Menon successfully integrated over 560 princely states into the Indian Union using the Instrument of Accession.',
                'Operation Polo was the military code name for the police action launched in September 1948 to integrate the princely state of Hyderabad into the Indian Union.',
                'The Constitution of India was adopted on 26 November 1949 and came into full legal effect on 26 January 1950.',
                'Dr. B.R. Ambedkar served as the Chairman of the seven-member Drafting Committee of the Constituent Assembly.',
                'The First Five-Year Plan (1951–1956) was based on the Harrod-Domar growth model and prioritized agriculture, dams, and irrigation.',
                'India\'s first Chief Election Commissioner, Sukumar Sen, conducted the historic First General Elections of 1951–1952 using universal adult suffrage.',
                'The Department of Atomic Energy was created in 1954 under the direct charge of the Prime Minister, led by Dr. Homi J. Bhabha.'
            ],
            'mains': [
                'Critically evaluate the diplomatic and administrative role of Sardar Vallabhbhai Patel and V.P. Menon in the political integration of the princely states into the Indian Union.',
                'Analyze the nation-building challenges faced by India immediately after Independence (1947–1952), with specific reference to refugee rehabilitation, communal peace, and food security.',
                'Discuss the vision and institutional architecture of the Nehruvian model of development, evaluating the roles of the Planning Commission and state-led industrialization.'
            ]
        }
    },
    'india-1947-1964': {
        'aspects': {
            'Linguistic Reorganisation of States': [
                'Demand for linguistic states: Dhar Commission (June 1948) and JVP Committee (Jawaharlal Nehru, Vallabhbhai Patel, Pattabhi Sitaramayya, Dec 1948) rejected linguistic states, prioritizing national unity and security.',
                'Potti Sreeramulu\'s fast (1952): Veteran Gandhian died on 15 December 1952 after a 58-day hunger strike demanding an Andhra state for Telugu speakers; sparked violent riots; government created the State of Andhra on 1 October 1953 (first linguistic state in India).',
                'States Reorganisation Commission (SRC, 1953): Headed by Justice Fazl Ali with H.N. Kunzru and K.M. Panikkar; recommended reorganizing states primarily on linguistic lines with administrative viability; Parliament enacted the States Reorganisation Act (November 1956), carving India into 14 States and 6 Union Territories.'
            ],
            'Mahalanobis Industrial Model & Panchayati Raj': [
                'Second Five-Year Plan (1956–1961): Formulated by statistician Prasanta Chandra Mahalanobis; prioritized rapid industrialization through heavy machine-building capital goods (socialistic pattern of society); established three monumental public sector steel plants with foreign collaboration: Bhilai (Soviet Union), Rourkela (West Germany), and Durgapur (United Kingdom); established Heavy Engineering Corporation (HEC) Ranchi.',
                'Panchayati Raj Dawn: Balwant Rai Mehta Committee (1957) recommended three-tier democratic decentralization (Gram Panchayat, Panchayat Samiti, Zilla Parishad); inaugurated by PM Nehru at Nagaur (Rajasthan) on 2 October 1959.'
            ],
            'Foreign Policy & The 1962 China War': [
                'Panchsheel & Non-Aligned Movement: Five Principles of Peaceful Coexistence (Panchsheel) signed with Chinese Premier Zhou Enlai on 29 April 1954; Afro-Asian Bandung Conference (1955) led to the founding of the Non-Aligned Movement (NAM) at the Belgrade Summit (1961) led by Nehru, Josip Broz Tito (Yugoslavia), Gamal Abdel Nasser (Egypt), Sukarno (Indonesia), and Kwame Nkrumah (Ghana).',
                'Sino-Indian War of 1962: Border disputes over the McMahon Line in Arunachal Pradesh (NEFA) and Aksai Chin in Ladakh; Chinese People\'s Liberation Army launched simultaneous surprise offensives on 20 October 1962, overrunning Indian positions; unilateral ceasefire declared by China in November; dealt a severe psychological and geopolitical blow to Nehru, forcing military modernization and defense budget expansion.'
            ]
        },
        'upsc': {
            'prelims': [
                'Andhra was the first state created on a linguistic basis in independent India on 1 October 1953, following the martyrdom of Potti Sreeramulu.',
                'The States Reorganisation Commission (SRC) appointed in 1953 was headed by Justice Fazl Ali, with H.N. Kunzru and K.M. Panikkar as members.',
                'The Second Five-Year Plan (1956–1961) was based on the Feldman-Mahalanobis model, prioritizing basic heavy industries and machine tools.',
                'The three public sector steel plants of Bhilai (USSR), Rourkela (Germany), and Durgapur (UK) were set up during the Second Five-Year Plan.',
                'Panchayati Raj was first inaugurated in India by Prime Minister Jawaharlal Nehru at Nagaur (Rajasthan) on 2 October 1959.',
                'The Five Principles of Peaceful Coexistence (Panchsheel) were first formally enunciated in the Sino-Indian Agreement on Tibet on 29 April 1954.',
                'The First Summit of the Non-Aligned Movement (NAM) was convened at Belgrade (Yugoslavia) in September 1961.'
            ],
            'mains': [
                'Trace the evolution of the linguistic reorganisation of states in India from the Dhar Commission to the States Reorganisation Act of 1956, analyzing how linguistic states strengthened Indian federalism.',
                'Evaluate the Nehru-Mahalanobis strategy of economic development during the Second Five-Year Plan, discussing its achievements and structural limitations.',
                'Critically analyze the geopolitical causes, military trajectory, and strategic consequences of the 1962 Sino-Indian War on India\'s foreign and defense policies.'
            ]
        }
    },
    'india-1965-1980': {
        'aspects': {
            'Shastri Era, Green Revolution & 1965 War': [
                'Lal Bahadur Shastri (1964–1966): Succeeded Nehru; confronted acute food shortages and Pakistani aggression with the slogan "Jai Jawan, Jai Kisan".',
                '1965 Indo-Pak War: Pakistan launched Operation Desert Hawk (Rann of Kutch) and Operation Gibraltar (infiltrating guerrillas into J&K); Indian army counter-attacked across the international border toward Lahore; UN ceasefire; Tashkent Declaration signed on 10 January 1966 mediated by Soviet Premier Alexei Kosygin; Shastri died suddenly at Tashkent hours after signing.',
                'Launch of Green Revolution (1966): Introduced High Yielding Variety (HYV) semi-dwarf wheat seeds (developed by Norman Borlaug in Mexico), chemical fertilizers, and assured tube-well irrigation in Punjab, Haryana, and Western UP; spearheaded by M.S. Swaminathan and Agriculture Minister C. Subramaniam, ending chronic reliance on American PL-480 food aid ("ship-to-mouth existence").'
            ],
            '1971 Bangladesh War & Structural Reforms': [
                'Bank Nationalization & Privy Purses: 14 major private commercial banks nationalized on 19 July 1969; Privy Purses and princely privileges abolished through the 26th Constitutional Amendment Act (1971).',
                '1971 Bangladesh Liberation War: Pakistan military junta under Yahya Khan launched Operation Searchlight (March 1971) committing genocide in East Pakistan; 10 million Bengali refugees flooded India; India trained the Mukti Bahini; war broke out on 3 December 1971; Indian Army (Gen. Sam Manekshaw) executed a brilliant 13-day blitzkrieg; Indian Navy executed Operation Trident (bombarding Karachi harbor); 93,000 Pakistani soldiers surrendered at Dhaka on 16 December 1971 under Lt. Gen. A.A.K. Niazi; birth of independent Bangladesh; Simla Agreement (July 1972) converted the ceasefire line into the Line of Control (LoC).',
                'Nuclear capability & Space: India conducted its first peaceful nuclear explosion ("Smiling Buddha") at Pokhran, Rajasthan on 18 May 1974; launched first indigenous satellite Aryabhata in 1975.'
            ],
            'JP Movement, The Emergency & Janata Government': [
                'The Emergency (25 June 1975 – 21 March 1977): Allahabad High Court Justice Jagmohanlal Sinha invalidated Indira Gandhi\'s 1971 election victory; Jayaprakash Narayan (JP) called for "Total Revolution" (Sampoorna Kranti); President Fakhruddin Ali Ahmed proclaimed National Emergency under Article 352 on grounds of "internal disturbance"; fundamental rights suspended, press censored, opposition leaders jailed.',
                '42nd Amendment & 1977 Transition: 42nd Amendment Act (1976 - "Mini-Constitution") inserted words "Socialist, Secular, Integrity" into the Preamble, added Fundamental Duties (Article 51A); March 1977 general elections brought the first non-Congress coalition government (Janata Party) to power under Morarji Desai; 44th Constitutional Amendment Act (1978) restored democratic liberties, replaced "internal disturbance" with "armed rebellion", and omitted Right to Property from Fundamental Rights.'
            ]
        },
        'upsc': {
            'prelims': [
                'Prime Minister Lal Bahadur Shastri coined the patriotic slogan "Jai Jawan, Jai Kisan" during the 1965 Indo-Pak War.',
                'The Tashkent Agreement was signed on 10 January 1966 between Prime Minister Lal Bahadur Shastri and Pakistani President Ayub Khan, mediated by the Soviet Union.',
                'Fourteen major private commercial banks were nationalized by the Indira Gandhi government on 19 July 1969.',
                'India conducted its first successful nuclear test, codenamed "Smiling Buddha", at Pokhran on 18 May 1974.',
                'The historic surrender of 93,000 Pakistani armed personnel took place in Dhaka on 16 December 1971, marking the creation of Bangladesh.',
                'The 42nd Constitutional Amendment Act of 1976 added the words "Socialist", "Secular", and "Integrity" to the Preamble of the Indian Constitution and introduced Fundamental Duties.',
                'The 44th Constitutional Amendment Act of 1978 substituted the term "internal disturbance" with "armed rebellion" for invoking national emergency under Article 352.'
            ],
            'mains': [
                'Analyze the geopolitical, humanitarian, and military dimensions of the 1971 Bangladesh Liberation War, evaluating India\'s strategic leadership and diplomatic maneuvering.',
                'Critically examine the causes, constitutional controversies, and socio-political fallout of the Internal Emergency (1975–1977) in India.',
                'Evaluate the economic, regional, and ecological impacts of the Green Revolution in India, discussing its role in achieving food self-sufficiency versus creating agrarian inequalities.',
                'Discuss the significant constitutional corrections enacted by the 44th Constitutional Amendment Act of 1978 to safeguard democracy and fundamental rights.'
            ]
        }
    },
    'india-1981-1991': {
        'aspects': {
            'Punjab Crisis & Operation Blue Star': [
                'Rise of militancy: Rise of Sikh militant separatism (demand for Khalistan) led by Jarnail Singh Bhindranwale, who fortified the Golden Temple complex in Amritsar.',
                'Operation Blue Star (June 1984): Military assault ordered by Indira Gandhi to clear armed militants from the Harmandir Sahib complex; resulted in heavy casualties and structural damage to the Akal Takht; provoked intense anguish among Sikhs; on 31 October 1984, Prime Minister Indira Gandhi was assassinated by her two Sikh bodyguards (Satwant Singh and Beant Singh), triggering horrific anti-Sikh riots in Delhi and other cities.'
            ],
            'Rajiv Gandhi Era Modernization & Pacts': [
                'Technological leap: Rajiv Gandhi (1984–1989) prioritized telecommunications modernization, computer technology, and digital networking spearheaded by Sam Pitroda (National Technology Missions); established C-DOT (Centre for Development of Telematics); launched Navodaya Vidyalayas.',
                'Constitutional reforms: 52nd Constitutional Amendment Act 1985 (Anti-Defection Law, Tenth Schedule); 61st Constitutional Amendment Act 1988 (lowered minimum voting age from 21 to 18 years); introduced bills for constitutional recognition of Panchayati Raj.',
                'Regional Accords: Punjab Accord (Rajiv-Longowal Accord 1985), Assam Accord (August 1985 ending the 6-year anti-foreigners agitation), and Mizo Accord (1986 ending Mizo insurgency under Laldenga); dispatched Indian Peace Keeping Force (IPKF - Operation Pawan 1987) to Sri Lanka following the Indo-Sri Lanka Accord, which became an intractable quagmire; Rajiv Gandhi was assassinated by an LTTE suicide bomber at Sriperumbudur (Tamil Nadu) on 21 May 1991.'
            ],
            '1991 Economic Crisis & The LPG Reforms': [
                'Balance of Payments (BoP) Emergency: Fiscal deficit reached 8.4% of GDP; Gulf War (1990–91) spiked crude oil prices and disrupted worker remittances; double-digit inflation; foreign exchange reserves plummeted to barely 1.2 billion dollars (scarcely enough to finance two weeks of essential imports); government airlifted 47 tonnes of gold reserves to the Bank of England and 20 tonnes to Union Bank of Switzerland as collateral for emergency loans.',
                'New Economic Policy (July 1991): Prime Minister P.V. Narasimha Rao and Finance Minister Dr. Manmohan Singh unveiled the revolutionary LPG (Liberalization, Privatization, Globalization) paradigm; dismantled the "License-Permit-Quota Raj"; devalued the rupee; abolished industrial licensing for most sectors; opened automatic approval for Foreign Direct Investment (FDI); rationalized peak customs tariffs from over 300% to competitive levels; transformed India into an open market economy.'
            ]
        },
        'upsc': {
            'prelims': [
                'The 52nd Constitutional Amendment Act of 1985 added the Tenth Schedule to the Constitution, providing for the disqualification of legislators on grounds of defection.',
                'The 61st Constitutional Amendment Act of 1988 reduced the voting age for Lok Sabha and Assembly elections from 21 years to 18 years.',
                'Operation Blue Star was conducted by the Indian Army in June 1984 to flush out armed militants from the Golden Temple complex in Amritsar.',
                'The Assam Accord was signed on 15 August 1985, setting 25 March 1971 as the cut-off date for the detection and deportation of illegal immigrants.',
                'In 1991, India faced an acute Balance of Payments (BoP) crisis with foreign exchange reserves dropping to just about two weeks of import cover.',
                'The New Economic Policy (LPG - Liberalisation, Privatisation, Globalisation) was initiated in July 1991 under Prime Minister P.V. Narasimha Rao and Finance Minister Dr. Manmohan Singh.',
                'Rajiv Gandhi was assassinated on 21 May 1991 at Sriperumbudur near Chennai by an LTTE suicide bomber.'
            ],
            'mains': [
                'Analyze the circumstances, structural factors, and policy measures that led to the Balance of Payments (BoP) crisis of 1991 in India.',
                'Critically evaluate the New Economic Policy of 1991 (LPG reforms), discussing how it dismantled the "License-Permit Raj" and transformed the Indian economy.',
                'Examine the regional peace accords concluded during the Rajiv Gandhi administration (Assam Accord, Punjab Accord, Mizo Accord), evaluating their success in resolving sub-national conflicts.',
                'Discuss the constitutional significance of the 52nd Amendment (Anti-Defection Law) and the 61st Amendment (voting age reduction) in Indian democratic governance.'
            ]
        }
    },
    'india-1992-2000': {
        'aspects': {
            'Democratic Decentralization & Social Mobilization': [
                '73rd & 74th Amendments (1992): Conferred constitutional status on Panchayati Raj Institutions (Part IX, Eleventh Schedule with 29 subjects) and Urban Local Bodies / Municipalities (Part IXA, Twelfth Schedule with 18 subjects); mandated regular five-year elections, mandatory State Finance Commissions, State Election Commissions, and 33% reservation of seats for women.',
                'Mandal Commission Implementation: V.P. Singh government implemented the Mandal Commission recommendation of 27% reservation for Other Backward Classes (OBCs) in central government jobs (upheld by Supreme Court in the landmark Indra Sawhney vs Union of India case 1992, introducing the Creamy Layer concept and 50% cap on total reservations).',
                'Communal Polarization: Demolition of the Babri Masjid in Ayodhya on 6 December 1992; triggered nationwide communal riots and March 1993 Bombay serial bomb blasts.'
            ],
            'Pokhran-II, Kargil War & Coalition Era': [
                'Pokhran-II Nuclear Tests ("Operation Shakti"): Conducted 5 underground nuclear tests (including a thermonuclear device) on 11 and 13 May 1998 at Pokhran under Prime Minister Atal Bihari Vajpayee and scientific advisor Dr. A.P.J. Abdul Kalam; declared India a responsible nuclear weapons state; adopted a nuclear doctrine based on "Credible Minimum Deterrence" and "No First Use" (NFU).',
                'Kargil Conflict (May–July 1999): Pakistani troops and paramilitaries covertly occupied strategic high-altitude bunker posts across the Line of Control in the Kargil, Dras, Batalik, and Mushkoh sectors (Operation Badr); Indian Armed Forces launched "Operation Vijay" (Army) and "Operation Safed Sagar" (Air Force); recaptured Tiger Hill and Tololing amidst extreme sub-zero mountain warfare; Pakistan forced to withdraw unconditionally; established the National Security Council and K. Subrahmanyam Kargil Review Committee.'
            ]
        },
        'upsc': {
            'prelims': [
                'The 73rd and 74th Constitutional Amendment Acts of 1992 added Parts IX and IXA to the Constitution, granting constitutional status to Panchayats and Municipalities.',
                'The Supreme Court upheld 27% reservation for OBCs in the landmark Indra Sawhney vs Union of India judgment (1992), while capping total reservations at 50% and introducing the Creamy Layer exclusion.',
                'India conducted five underground nuclear tests codenamed "Operation Shakti" (Pokhran-II) on 11 and 13 May 1998 under Prime Minister Atal Bihari Vajpayee.',
                'Operation Vijay was the code name of the military operation launched by the Indian Armed Forces to evict Pakistani intruders from the Kargil sector in 1999.',
                'Kargil Vijay Diwas is celebrated annually on 26 July to commemorate the successful culmination of Operation Vijay.',
                'The Information Technology Act (IT Act) was passed by Parliament in the year 2000 to provide legal recognition for electronic transactions and digital signatures.',
                'The K. Subrahmanyam Kargil Review Committee appointed in 1999 recommended a complete overhaul of the national security architecture, including the creation of the Chief of Defence Staff (CDS).'
            ],
            'mains': [
                'Analyze the features, institutional mechanisms, and transformative impact of the 73rd and 74th Constitutional Amendment Acts on grassroots democracy and women\'s empowerment in India.',
                'Critically evaluate the Indra Sawhney judgment (1992) and its implications for affirmative action, the creamy layer principle, and the 50% reservation ceiling.',
                'Discuss the strategic, diplomatic, and military significance of Operation Vijay (Kargil War 1999) and examine the national security reforms that followed.',
                'Examine India\'s Nuclear Doctrine formulated post-Pokhran-II, analyzing the principles of "No First Use" (NFU) and "Credible Minimum Deterrence".'
            ]
        }
    },
    'india-2001-2010': {
        'aspects': {
            'Rights-Based Legislative Architecture': [
                'Right to Information (RTI Act 2005): Enacted following grassroots advocacy by Mazdoor Kisan Shakti Sangathan (MKSS under Aruna Roy); empowered citizens to inspect government records, promoting transparency and accountability.',
                'MGNREGA (2005): Mahatma Gandhi National Rural Employment Guarantee Act guaranteed 100 days of wage employment per financial year to adult members of rural households willing to do unskilled manual work; largest rights-based social safety net program in the world.',
                'Right to Education (RTE Act 2009): Enacted pursuant to the 86th Constitutional Amendment Act 2002 (inserting Article 21A), guaranteeing free and compulsory elementary education to all children aged 6 to 14 years; mandated 25% quota in private schools for disadvantaged groups.',
                'Forest Rights Act 2006 (FRA): Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act vested individual and community forest rights over ancestral forest lands.'
            ],
            'Strategic Milestones & Global Integration': [
                'Indo-US Civil Nuclear Deal (123 Agreement, 2008): Ended India\'s nuclear isolation since 1974; separated civilian and military nuclear facilities, placing civilian reactors under IAEA safeguards while granting India access to global nuclear fuel and technology without signing the NPT.',
                'Space and Technology: ISRO successfully launched Chandrayaan-1 (October 2008), discovering water molecules on the lunar surface using the Moon Mineralogy Mapper (M3); UIDAI established in 2009 (chaired by Nandan Nilekani) to issue unique biometric Aadhaar identity numbers.',
                'National Highway Development Project (NHDP): Built the Golden Quadrilateral connecting Delhi, Mumbai, Chennai, and Kolkata, transforming domestic freight logistics.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Right to Information (RTI) Act came into force on 12 October 2005, repealing the earlier Freedom of Information Act 2002.',
                'The 86th Constitutional Amendment Act of 2002 inserted Article 21A, making free and compulsory education for children between 6 and 14 years a Fundamental Right.',
                'The Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA) was passed in 2005, legally guaranteeing 100 days of wage employment to rural households.',
                'India and the United States signed the historic Civil Nuclear Cooperation Agreement (123 Agreement) in October 2008.',
                'Chandrayaan-1, India\'s first lunar probe, was launched by ISRO in October 2008 using the PSLV-C11 rocket, confirming the presence of water molecules on the Moon.',
                'The Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act was passed in 2006.',
                'The Golden Quadrilateral highway project connecting Delhi, Mumbai, Chennai, and Kolkata was launched under Prime Minister Atal Bihari Vajpayee.'
            ],
            'mains': [
                'Critically analyze the "Rights-Based Approach" to governance that emerged in India during 2004–2014, evaluating the socio-economic impacts of RTI, MGNREGA, and RTE.',
                'Examine the strategic, geopolitical, and energy implications of the Indo-US Civil Nuclear Deal (2008) for India\'s foreign policy and atomic energy program.',
                'Evaluate the contribution of the Right to Information (RTI) Act in promoting administrative transparency and combating corruption, discussing its institutional challenges.',
                'Assess the role of infrastructure megaprojects (Golden Quadrilateral and NHDP) in integrating regional markets and accelerating GDP growth.'
            ]
        }
    },
    'india-2011-2020': {
        'aspects': {
            'Fiscal & Economic Structural Overhauls': [
                'Goods and Services Tax (GST, 2017): Enacted through the 101st Constitutional Amendment Act; subsumed 17 central and state indirect taxes into a unified destination-based tax system ("One Nation, One Tax, One Market"); governed by the constitutional GST Council (Article 279A).',
                'Insolvency and Bankruptcy Code (IBC 2016): Unified legal framework for time-bound resolution of stressed corporate assets (180 to 270 days) overseen by the Insolvency and Bankruptcy Board of India (IBBI) and NCLT, dismantling non-performing asset (NPA) cycles.',
                'JAM Trinity & Digital Public Infrastructure (DPI): Jan Dhan Yojana (universal financial inclusion) linked with Aadhaar biometric identity and Mobile connectivity (JAM); created Unified Payments Interface (UPI) developed by NPCI (2016), revolutionizing real-time cashless digital micropayments.'
            ],
            'Constitutional & Security Transitions': [
                'Abrogation of Special Status under Article 370 (5–6 August 2019): Parliament revoked the special semi-autonomous status of Jammu & Kashmir under Article 370 and Article 35A; enacted the Jammu and Kashmir Reorganisation Act 2019, bifurcating the state into two Union Territories: Jammu & Kashmir (with a legislature) and Ladakh (without a legislature); fully extended the Indian Constitution, reservations, and central laws to the region.',
                'National Security Actions: Uri surgical strikes (September 2016) and Balakot airstrikes (February 2019) demonstrating active counter-terror doctrine beyond the Line of Control; creation of the post of Chief of Defence Staff (CDS, General Bipin Rawat appointed first CDS in Dec 2019) to foster tri-service jointness.'
            ]
        },
        'upsc': {
            'prelims': [
                'The Goods and Services Tax (GST) was introduced through the 101st Constitutional Amendment Act and rolled out across India on 1 July 2017.',
                'Article 279A of the Constitution established the GST Council, chaired by the Union Finance Minister, with voting weights of 1/3rd for the Centre and 2/3rds for the States.',
                'The Insolvency and Bankruptcy Code (IBC) was enacted in 2016 to establish a time-bound mechanism for resolving corporate insolvency.',
                'On 5 August 2019, the President issued a Constitutional Order superseding the 1954 Order, effectively abrogating the special provisions of Article 370 regarding Jammu & Kashmir.',
                'The Jammu and Kashmir Reorganisation Act, 2019 bifurcated the erstwhile state into two Union Territories: Jammu & Kashmir and Ladakh, effective from 31 October 2019.',
                'General Bipin Rawat was appointed as India\'s first Chief of Defence Staff (CDS) on 30 December 2019.',
                'The Unified Payments Interface (UPI) was developed and launched by the National Payments Corporation of India (NPCI) in 2016.'
            ],
            'mains': [
                'Critically examine the institutional design, fiscal federalism challenges, and revenue implications of the Goods and Services Tax (GST) under the GST Council.',
                'Analyze the constitutional, legal, and security implications of the abrogation of Article 370 and the bifurcation of Jammu & Kashmir into two Union Territories.',
                'Evaluate the impact of the "JAM Trinity" (Jan Dhan, Aadhaar, Mobile) and Digital Public Infrastructure (UPI) on direct benefit transfers (DBT) and financial inclusion in India.',
                'Discuss the creation of the Chief of Defence Staff (CDS) and the ongoing theaterisation reforms in modernizing the command structure of the Indian Armed Forces.'
            ]
        }
    },
    'india-2020-present': {
        'aspects': {
            'COVID-19 Response & Atmanirbhar Bharat': [
                'Pandemic resilience: Massive national mobilization under the Disaster Management Act 2005; development of indigenous vaccine Covaxin (Bharat Biotech & ICMR) and massive rollout via the CoWIN digital platform, administering over 2.2 billion doses.',
                'Atmanirbhar Bharat Abhiyan: Economic package launched in May 2020 focusing on self-reliance across 5 pillars: Economy, Infrastructure, System, Vibrant Demography, and Demand; introduced Production Linked Incentive (PLI) schemes across 14 manufacturing sectors (semiconductors, electronics, solar PV, pharmaceuticals).'
            ],
            'Decolonization of Laws & Cultural Diplomacy': [
                'New Criminal Law Codes (2023): Parliament replaced colonial-era British criminal statutes: 1. Bharatiya Nyaya Sanhita (BNS 2023) replaced Indian Penal Code 1860, 2. Bharatiya Nagarik Suraksha Sanhita (BNSS 2023) replaced CrPC 1898, 3. Bharatiya Sakshya Adhiniyam (BSA 2023) replaced Indian Evidence Act 1872; modernized laws to include digital evidence, community service, and trial in absentia.',
                'Nari Shakti Vandan Adhiniyam (106th Amendment Act 2023): First bill passed in the new Parliament building; provides 33% reservation for women in the Lok Sabha, State Legislative Assemblies, and Delhi Assembly for 15 years.',
                'Space Milestones: Chandrayaan-3 successfully achieved a soft landing on the Lunar South Pole on 23 August 2023 (landing site named "Shiv Shakti Point"; 23 August declared National Space Day); launched Aditya-L1 solar observatory to the Sun-Earth Lagrangian point L1.',
                'G20 Presidency (2023): India hosted the G20 Summit under the theme "Vasudhaiva Kutumbakam" (One Earth, One Family, One Future); achieved 100% consensus on the New Delhi Leaders\' Declaration and permanently inducted the African Union into the G20; launched the India-Middle East-Europe Economic Corridor (IMEC) and Global Biofuels Alliance.'
            ]
        },
        'upsc': {
            'prelims': [
                'The 106th Constitutional Amendment Act of 2023 (Nari Shakti Vandan Adhiniyam) reserves one-third (33%) of seats for women in the Lok Sabha and State Legislative Assemblies.',
                'Chandrayaan-3 successfully soft-landed on the Lunar South Pole on 23 August 2023; the landing site was named "Shiv Shakti Point", and 23 August was declared National Space Day.',
                'Aditya-L1, India\'s first dedicated solar observatory mission, was placed into halo orbit around the Sun-Earth Lagrangian point L1 by ISRO in January 2024.',
                'The three new criminal laws enacted in 2023 are Bharatiya Nyaya Sanhita (replacing IPC), Bharatiya Nagarik Suraksha Sanhita (replacing CrPC), and Bharatiya Sakshya Adhiniyam (replacing IEA).',
                'The African Union was admitted as a permanent member of the G20 during India\'s G20 Presidency at the New Delhi Summit in September 2023.',
                'The National Education Policy (NEP) 2020 replaced the previous 10+2 curricular structure with a new 5+3+3+4 pedagogical structure.',
                'The India-Middle East-Europe Economic Corridor (IMEC) was announced on the sidelines of the G20 Summit in New Delhi in September 2023.'
            ],
            'mains': [
                'Critically evaluate the significance of the 106th Constitutional Amendment Act (Nari Shakti Vandan Adhiniyam) in enhancing female political representation and legislative leadership in India.',
                'Analyze the objectives and structural reforms introduced by the three new criminal laws (BNS, BNSS, BSA 2023) in decolonizing and modernizing India\'s criminal justice delivery system.',
                'Evaluate the diplomatic and strategic achievements of India\'s G20 Presidency (2023), with specific focus on the induction of the African Union and the voice of the Global South.',
                'Discuss the strategic importance of the Atmanirbhar Bharat Abhiyan and the Production Linked Incentive (PLI) schemes in integrating India into global supply chains.'
            ]
        }
    },
    'world-history-context': {
        'aspects': {
            'Epochs of Global Transition': [
                'Renaissance & Scientific Revolution (14th–17th cent): Humanism (Petrarch, Erasmus), printing press by Gutenberg (c. 1440), Heliocentric astronomy (Copernicus, Galileo, Kepler), Newtonian physics; shattered medieval scholasticism.',
                'Enlightenment & Age of Reason (18th cent): John Locke (Social Contract, Natural Rights: Life, Liberty, Property), Montesquieu (Separation of Powers in Spirit of the Laws), Voltaire (freedom of speech and religious toleration), Jean-Jacques Rousseau (General Will in The Social Contract: "Man is born free, and everywhere he is in chains").',
                'Waves of Global Revolution (1776–1991): Atlantic revolutions (American, French, Haitian, Latin American); 19th-century Industrialization and colonial imperialism; 20th-century Totalitarianism, World Wars, Cold War, and Decolonization.'
            ]
        },
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
                'Analyze the transition from medieval feudalism to modern commercial capitalism in Europe, evaluating the roles of the Scientific Revolution and maritime trade.'
            ]
        }
    },
    'industrial-revolution-and-capitalism': {
        'aspects': {
            'Mechanization & The British Lead': [
                'Why Britain pioneered: Vast colonial empire supplying raw materials and captive markets; rich domestic coal and iron ore deposits; agrarian Enclosure Movement providing cheap displaced rural labor; stable parliamentary constitutional monarchy; merchant capital and advanced banking (Bank of England).',
                'Technological Breakthroughs: James Kay (Flying Shuttle, 1733); James Hargreaves (Spinning Jenny, 1764); Richard Arkwright (Water Frame, 1769); Samuel Crompton (Spinning Mule, 1779); Edmund Cartwright (Power Loom, 1785); James Watt and Matthew Boulton (condensing Steam Engine, 1769/1776); Henry Cort (puddling process for iron); George Stephenson (steam locomotive Rocket, 1814).'
            ],
            'Social Transformation & Rise of Capitalism': [
                'Urban Proletarianization: Dramatic migration from rural cottages to squalid industrial cities (Manchester, Birmingham, Leeds); horrific working conditions: 14 to 16-hour workdays, rampant exploitation of child and female labor, toxic air, lack of sanitation, low wages.',
                'Capitalism & Intellectual Critiques: Adam Smith (Wealth of Nations 1776 - Laissez-faire free market, invisible hand, division of labour); Luddite Movement (1811–1816; machine-wrecking workers led by mythical "Ned Ludd"); Chartism (1838–1848; working-class movement demanding universal male suffrage and secret ballots); Karl Marx and Friedrich Engels (The Communist Manifesto 1848, Das Kapital 1867 - historical materialism, class struggle between Bourgeoisie and Proletariat, surplus value, and inevitable socialist revolution).'
            ]
        },
        'upsc': {
            'prelims': [
                'James Watt patented the improved condensing steam engine in 1769, which revolutionized industrial machinery and transportation.',
                'Adam Smith formulated the foundational principles of free-market capitalism and the "invisible hand" in The Wealth of Nations (1776).',
                'The Luddites were early 19th-century English textile workers who smashed industrial weaving machinery to protest against unemployment and wage cuts.',
                'Karl Marx and Friedrich Engels published The Communist Manifesto in 1848, calling for the global unity of the working class ("Workers of the world, unite!").',
                'The Enclosure Acts in 18th-century Britain enclosed common agricultural lands, displacing small peasants who migrated to cities as factory labor.',
                'George Stephenson built the world\'s first public inter-city railway line, the Liverpool and Manchester Railway, in 1830.'
            ],
            'mains': [
                'Critically examine the factors that enabled Great Britain to become the "Workshop of the World" during the Industrial Revolution.',
                'Analyze the social, demographic, and economic consequences of the Industrial Revolution on the working class, women, and urban living conditions.',
                'Compare and contrast Adam Smith\'s free-market capitalism with Karl Marx\'s scientific socialism as economic ideologies responding to the Industrial Revolution.'
            ]
        }
    },
    'american-revolution-and-civil-war': {
        'aspects': {
            'American War of Independence (1775–1783)': [
                'Causes of revolt: British mercantilist restrictions (Navigation Acts, Sugar Act, Stamp Act 1765 - slogan: "No Taxation without Representation"); Boston Massacre (1770); Boston Tea Party (16 December 1773; Sons of Liberty disguised as Native Americans dumped 342 chests of British East India Company tea into Boston harbour); Coercive / Intolerable Acts.',
                'Declaration of Independence (4 July 1776): Adopted by Second Continental Congress in Philadelphia; drafted by Thomas Jefferson; proclaimed self-evident truths: all men are created equal, endowed with inalienable rights to "Life, Liberty, and the pursuit of Happiness"; General George Washington led Continental Army; Battle of Saratoga (1777 - turning point; secured French alliance under Lafayette); British General Cornwallis surrendered at Yorktown (1781); Treaty of Paris (1783) recognized US independence.',
                'Constitutional Convention (Philadelphia 1787): Drafted US Constitution (world\'s oldest written democratic constitution); Bill of Rights (first 10 amendments 1791 guaranteeing freedom of speech, press, religion); federal system with separation of powers.'
            ],
            'American Civil War (1861–1865)': [
                'Sectional conflict: Industrial free-labor Northern States (Union) vs. Plantation slave-labor Southern States (Confederacy); election of Abraham Lincoln (1860, Republican opposed to expansion of slavery) triggered secession of 11 southern states led by Jefferson Davis; Battle of Fort Sumter (April 1861).',
                'Lincoln\'s Leadership & Emancipation: Emancipation Proclamation (1 January 1863; declared all slaves in Confederate rebel territory "forever free"); Battle of Gettysburg (July 1863, decisive turning point); Gettysburg Address (November 1863: "government of the people, by the people, for the people, shall not perish from the earth"); Confederate General Robert E. Lee surrendered to Union General Ulysses S. Grant at Appomattox (April 1865); 13th Constitutional Amendment (1865) permanently abolished slavery across the United States; Lincoln assassinated by John Wilkes Booth (14 April 1865).'
            ]
        },
        'upsc': {
            'prelims': [
                'The slogan "No Taxation without Representation" was popularized during the American Revolution against the British Stamp Act of 1765.',
                'The Boston Tea Party took place on 16 December 1773, where American colonists dumped East India Company tea chests into the harbor.',
                'The American Declaration of Independence was adopted on 4 July 1776 in Philadelphia, authored primarily by Thomas Jefferson.',
                'British General Lord Cornwallis surrendered to George Washington and French forces at the Battle of Yorktown in 1781, ending major combat.',
                'Abraham Lincoln issued the historic Emancipation Proclamation on 1 January 1863, declaring all enslaved persons in rebel Confederate states to be free.',
                'The 13th Amendment to the US Constitution (1865) officially and permanently abolished slavery in the United States.',
                'Abraham Lincoln delivered the famous Gettysburg Address in November 1863, defining democracy as "government of the people, by the people, for the people".'
            ],
            'mains': [
                'Analyze the ideological, commercial, and political causes of the American Revolution (1775–1783) and assess its impact on anti-colonial movements worldwide.',
                'Critically evaluate the significance of the American Declaration of Independence (1776) and the US Constitution of 1787 in establishing modern constitutional democracy.',
                'Examine the causes and historical significance of the American Civil War (1861–1865), assessing Abraham Lincoln\'s leadership in preserving the Union and abolishing slavery.'
            ]
        }
    },
    'french-revolution': {
        'aspects': {
            'Crisis of the Ancien Regime & 1789 Eruption': [
                'Three Estates inequality: 1st Estate (Clergy - 1% of population, owned 10% of land, exempt from direct taxes, collected Tithes), 2nd Estate (Nobility - 2% of population, owned 25% of land, held high state/military offices, collected feudal dues, exempt from taxes), 3rd Estate (97% of population: Bourgeoisie, artisans, peasants - paid all taxes: Taille land tax, Gabelle salt tax, Corvee forced labor).',
                'Fiscal Bankruptcy & Estates-General: King Louis XVI and Queen Marie Antoinette ("Madame Deficit"); bankrupt treasury due to Seven Years\' War and aiding American Revolution; convened Estates-General at Versailles (May 1789) after 175 years; dispute over voting (by head vs by estate); Third Estate broke away, declaring itself the "National Assembly" and taking the Tennis Court Oath (20 June 1789) pledging not to disband until drafting a constitution.',
                'Storming of the Bastille (14 July 1789): Armed Parisian mob stormed the medieval fortress-prison of the Bastille, symbolizing the overthrow of royal despotism (celebrated as French National Day); Great Fear in countryside; National Assembly abolished feudalism (4 August 1789) and adopted the Declaration of the Rights of Man and of the Citizen (26 August 1789 - Liberty, Equality, Fraternity).'
            ],
            'Radical Phase, Reign of Terror & Rise of Napoleon': [
                'Radicalization & Regicide: Flight to Varennes (royal family caught trying to escape, 1791); National Convention abolished monarchy and proclaimed the French Republic (September 1792); Louis XVI executed by guillotine (January 1793); foreign coalition invaded France.',
                'Reign of Terror (1793–1794): Radical Jacobins led by Maximilien Robespierre seized power through the Committee of Public Safety; Law of Suspects; over 40,000 citizens guillotined as counter-revolutionaries (including Marie Antoinette, Danton); ended with Thermidorian Reaction; Robespierre guillotined (July 1794); Directory established (1795–1799).',
                'Napoleon Bonaparte (1799–1815): Seized power in Coup of 18 Brumaire (November 1799), becoming First Consul, and crowned himself Emperor of the French in 1804; Napoleonic Code (Civil Code of 1804 - equality before the law, security of property, secularization, meritocracy); conquered continental Europe (Austerlitz 1805); Continental System (economic blockade of Britain); catastrophic invasion of Russia (1812); defeated at Battle of Leipzig (1813); final defeat at the Battle of Waterloo (18 June 1815) by Duke of Wellington; exiled to Saint Helena.'
            ]
        },
        'upsc': {
            'prelims': [
                'The French National Assembly adopted the historic "Declaration of the Rights of Man and of the Citizen" on 26 August 1789.',
                'The Storming of the Bastille took place on 14 July 1789 in Paris, marking the popular onset of the French Revolution.',
                'The Tennis Court Oath was sworn on 20 June 1789 by members of the Third Estate, pledging not to separate until France had a written constitution.',
                'The "Reign of Terror" (1793–1794) was directed by the Committee of Public Safety headed by radical Jacobin leader Maximilien Robespierre.',
                'Napoleon Bonaparte promulgated the Civil Code (Napoleonic Code) in 1804, establishing uniform legal equality and property rights across France.',
                'Napoleon was decisively defeated in his final battle at the Battle of Waterloo on 18 June 1815 by the Seventh Coalition led by the Duke of Wellington.',
                'Abbe Sieyes published the influential revolutionary pamphlet "What is the Third Estate?" in January 1789.'
            ],
            'mains': [
                'Analyze the social, economic, and intellectual causes of the French Revolution of 1789, examining how Enlightenment ideas influenced the Third Estate.',
                'Critically evaluate the Reign of Terror (1793–1794) under Maximilien Robespierre. Was it a departure from revolutionary ideals or a desperate defense of the Republic?',
                'Assess the legacy of Napoleon Bonaparte as both the "child of the Revolution" and its "liquidator", with specific focus on the Napoleonic Code and European state modernization.',
                'Discuss the global impact of the French revolutionary ideals of "Liberty, Equality, Fraternity" on subsequent nationalist and democratic movements across the world.'
            ]
        }
    },
    'world-war-1': {
        'aspects': {
            'Underlying Causes & July Crisis': [
                'M-A-I-N Framework: 1. Militarism (Anglo-German naval arms race, dreadnought battleships), 2. Alliances (Triple Alliance 1882: Germany, Austria-Hungary, Italy; Triple Entente 1907: Britain, France, Russia), 3. Imperialism (Scramble for Africa, Moroccan Crises), 4. Nationalism (Pan-Slavism, Balkan "powder keg" of Europe).',
                'Sarajevo Catalyst (28 June 1914): Archduke Franz Ferdinand (heir to Austro-Hungarian throne) and his wife Sophie assassinated in Sarajevo (Bosnia) by Gavrilo Princip, a Bosnian Serb member of the terrorist group "Black Hand" (Union or Death); Austria issued harsh ultimatum to Serbia; cascading alliance mobilizations initiated World War I in August 1914.'
            ],
            'Global Warfare, Stalemate & 1917 Turning Points': [
                'Trench warfare stalemate: German Schlieffen Plan (rapid invasion of France through Belgium) halted at the First Battle of the Marne (September 1914); 400 miles of parallel barbed-wire trenches stretched across the Western Front from the Swiss border to the North Sea; industrial slaughter using machine guns, poison mustard gas, flamethrowers, heavy artillery, and tanks (Battle of Verdun 1916, Battle of the Somme 1916 with 1 million casualties).',
                '1917 Turning Points: 1. Russian Revolution (Bolsheviks seized power and pulled Russia out of the war, signing the Treaty of Brest-Litovsk with Germany in March 1918), 2. Entry of the United States (April 1917; provoked by German unrestricted submarine warfare sinking the passenger liner Lusitania, and the intercepted Zimmermann Telegram proposing German-Mexican military alliance against US).',
                'Armistice & Casualties: German spring offensive failed; Allied counter-offensive (Hundred Days); German Kaiser Wilhelm II abdicated; Armistice signed in a railway carriage at Compiegne on the 11th hour of the 11th day of the 11th month (11 November 1918); over 20 million soldiers and civilians died.'
            ],
            'Paris Peace Conference & Treaty of Versailles (1919)': [
                'Treaty of Versailles (28 June 1919): Negotiated by the "Big Four" (Woodrow Wilson of US, David Lloyd George of Britain, Georges Clemenceau of France, Vittorio Orlando of Italy); dictated harsh punitive terms to Germany: Article 231 ("War Guilt Clause" forcing Germany to accept sole responsibility for the war), colossal reparations of 132 billion gold marks, German army reduced to 100,000 men without tanks, military aircraft, or submarines, Rhineland demilitarized in perpetuity, Alsace-Lorraine returned to France, Polish Corridor carved out of German territory; planted the seeds of World War II.',
                'Woodrow Wilson\'s 14 Points & League of Nations: Championed national self-determination (dissolving Austro-Hungarian and Ottoman empires into new nation-states: Poland, Czechoslovakia, Yugoslavia, Hungary); established the League of Nations (headquarters: Geneva) as the first global intergovernmental security body, though crippled because the US Senate refused to ratify it.'
            ]
        },
        'upsc': {
            'prelims': [
                'The assassination of Archduke Franz Ferdinand of Austria in Sarajevo on 28 June 1914 by Gavrilo Princip triggered World War I.',
                'The Schlieffen Plan was Germany\'s military blueprint to rapidly conquer France through Belgium before turning to face Russia.',
                'The United States entered World War I in April 1917 following German unrestricted submarine warfare and the Zimmermann Telegram.',
                'The Treaty of Brest-Litovsk was signed in March 1918 between Bolshevik Russia and the Central Powers, ending Russian participation in World War I.',
                'Article 231 of the Treaty of Versailles (1919) was known as the "War Guilt Clause", placing sole responsibility for the war on Germany.',
                'The League of Nations was established in 1919 as part of the Treaty of Versailles based on Woodrow Wilson\'s Fourteen Points.',
                'Over 1.3 million Indian soldiers served in World War I in the British Indian Army across France, Mesopotamia, Gallipoli, and East Africa; India Gate in Delhi was built as a memorial to them.'
            ],
            'mains': [
                'Critically examine the system of secret alliances and the M-A-I-N factors in precipitating the outbreak of World War I in 1914.',
                'Evaluate the provisions of the Treaty of Versailles (1919), analyzing whether its punitive terms against Germany directly paved the way for the rise of Nazism and World War II.',
                'Assess the contributions and sacrifices of the Indian Army in World War I and examine how the war catalyzed the Indian national freedom struggle.',
                'Analyze the structural weaknesses and geopolitical failures of the League of Nations in preventing aggression in the inter-war period.'
            ]
        }
    },
    'russian-revolution': {
        'aspects': {
            'Collapse of Tsarist Autocracy & 1905 Revolution': [
                'Ancien Regime of the Romanovs: Absolute autocracy of Tsar Nicholas II; backward agrarian economy with 80% peasant population; rapid industrialization in pockets (St. Petersburg, Moscow) creating an exploited, politically conscious working class; humiliating defeat in the Russo-Japanese War (1904–05).',
                '1905 Revolution ("Bloody Sunday"): Peaceful procession of unarmed workers led by priest Father Gapon carrying icons to the Winter Palace fired upon by imperial guards (22 January 1905); sparked nationwide strikes, mutiny on battleship Potemkin, and creation of the first workers\' councils (Soviets); Tsar forced to issue October Manifesto promising civil liberties and an elected parliament (Duma), but repeatedly diluted it.'
            ],
            '1917 Dual Revolutions: February to October': [
                'February Revolution (March 1917): Disastrous Russian losses in WWI (2 million killed, food riots in Petrograd); International Women\'s Day strikes; army garrisons joined demonstrators; Tsar Nicholas II abdicated, ending 304 years of Romanov dynastic rule; established a "Dual Power" system: 1. Provisional Government (headed by Prince Lvov, later Alexander Kerensky, representing liberal bourgeoisie), 2. Petrograd Soviet of Workers\' and Soldiers\' Deputies.',
                'Lenin\'s April Theses & October Revolution: Vladimir Lenin returned from exile in Switzerland (facilitated by German train); issued April Theses demanding: "All Power to the Soviets!", immediate exit from the war ("Peace, Land, and Bread"), and nationalization of land and banks.',
                'October Revolution (7 November 1917): Bolshevik Red Guards organized by Leon Trotsky (Military Revolutionary Committee) seized communication hubs, bridges, and stormed the Winter Palace without major bloodshed; arrested Provisional Government; Second All-Russian Congress of Soviets ratified the Bolshevik seizure of power; proclaimed Decree on Peace and Decree on Land.'
            ],
            'Civil War, War Communism & Lenin\'s NEP': [
                'Russian Civil War (1918–1921): Red Army (organized by Trotsky) fought against the White Army (coalition of monarchists, liberals, and foreign interventionist troops from Britain, France, US, Japan); execution of the Tsar and his family at Yekaterinburg (July 1918); policy of "War Communism" (extreme nationalization, forced grain requisitioning, Cheka secret police red terror) caused economic collapse and famine.',
                'New Economic Policy (NEP, 1921): Lenin implemented pragmatic economic retreat; replaced forced grain requisitioning with a fixed tax-in-kind; permitted private small businesses and retail trade, while the state retained control over the "commanding heights of the economy" (heavy industry, banking, foreign trade); Union of Soviet Socialist Republics (USSR) formally created in December 1922; Lenin died in January 1924, triggering power struggle between Trotsky and Joseph Stalin.'
            ]
        },
        'upsc': {
            'prelims': [
                'The "Bloody Sunday" massacre occurred on 22 January 1905 in St. Petersburg, when imperial troops fired on peaceful workers led by Father Gapon.',
                'The February Revolution of 1917 forced the abdication of Tsar Nicholas II, ending the Romanov dynasty in Russia.',
                'Vladimir Lenin articulated his revolutionary blueprint in the "April Theses" (1917), demanding "All Power to the Soviets" and "Peace, Land, and Bread".',
                'Leon Trotsky organized and led the Bolshevik Red Army to victory during the Russian Civil War (1918–1921).',
                'Lenin introduced the New Economic Policy (NEP) in 1921, introducing pragmatic market elements alongside state control of heavy industry.',
                'The Union of Soviet Socialist Republics (USSR) was officially established in December 1922.',
                'The Bolshevik secret police organization established in December 1917 to eliminate counter-revolutionaries was called the "Cheka" (headed by Felix Dzerzhinsky).'
            ],
            'mains': [
                'Analyze the socio-economic and political causes of the Russian Revolution of 1917, examining why the Provisional Government under Kerensky failed to consolidate power.',
                'Critically evaluate Vladimir Lenin\'s leadership, strategy, and ideology (April Theses, New Economic Policy) in founding the first socialist state in the world.',
                'Compare and contrast the causes and outcomes of the February Revolution and the October Revolution of 1917 in Russia.',
                'Discuss the global impact of the Russian Revolution on anti-colonial nationalist movements and working-class politics across the 20th century.'
            ]
        }
    },
    'world-war-2': {
        'aspects': {
            'Rise of Totalitarianism & Fascist Aggression': [
                'Inter-war crisis: Great Depression of 1929 devastated global trade, causing hyperinflation and unemployment; collapse of the democratic Weimar Republic; rise of Adolf Hitler and the Nazi Party (NSDAP); Hitler appointed Chancellor (January 1933), enacted Enabling Act, established Third Reich totalitarian dictatorship; Benito Mussolini\'s Fascism in Italy (March on Rome 1922); militarist expansionism in Imperial Japan (invasion of Manchuria 1931).',
                'Road to War: Hitler remilitarized the Rhineland (1936), annexed Austria (Anschluss, 1938); Western democracies pursued Policy of Appeasement (British PM Neville Chamberlain signed the Munich Agreement September 1938, surrendering Czechoslovakian Sudetenland to Hitler: "Peace for our time"); Hitler signed the Molotov-Ribbentrop Non-Aggression Pact with Soviet Union (August 1939) with secret protocol to divide Poland.'
            ],
            'Global Combat: Blitzkrieg to Hiroshima': [
                'Outbreak & Blitzkrieg: German army invaded Poland on 1 September 1939 using Blitzkrieg (lightning war: coordinated tanks, dive-bombers, motorized infantry); Britain and France declared war on Germany (3 September 1939); Fall of France (June 1940); Battle of Britain (Royal Air Force defeated Luftwaffe).',
                'Turning Points (1941–1943): 1. Operation Barbarossa (22 June 1941: Hitler invaded USSR with 3 million soldiers; Battle of Stalingrad, August 1942–February 1943, where Soviet Red Army encircled and destroyed German 6th Army under Field Marshal Paulus - definitive turning point on Eastern Front), 2. Attack on Pearl Harbor (7 December 1941: Japanese carrier aircraft attacked US Pacific Fleet in Hawaii; US entered the war), 3. Battle of Midway (June 1942: US Navy sank 4 Japanese aircraft carriers), 4. Battle of El Alamein (October 1942: British General Montgomery defeated Rommel\'s Afrika Korps in Egypt).',
                'Allied Victory & The Holocaust: D-Day / Normandy Landings (Operation Overlord, 6 June 1944: Allied forces commanded by General Dwight Eisenhower landed on beaches of Normandy, liberating Western Europe); Soviet Red Army captured Berlin (May 1945); Hitler committed suicide in his bunker (30 April 1945); The Holocaust (Shoah: industrial genocide executed by the Nazi SS murdering 6 million Jews and millions of others in death camps like Auschwitz-Birkenau, Treblinka); US dropped atomic bombs on Hiroshima ("Little Boy", 6 August 1945) and Nagasaki ("Fat Man", 9 August 1945) under President Harry S. Truman; Japan surrendered on 2 September 1945 on the USS Missouri; over 70 million people died.'
            ],
            'Post-War Order & Creation of the United Nations': [
                'Yalta & Potsdam Conferences (1945): Churchill, Roosevelt, and Stalin agreed on division of Germany into 4 occupation zones, demilitarization, and trial of war criminals (Nuremberg Trials); United Nations Charter signed on 26 June 1945 in San Francisco; UN officially came into existence on 24 October 1945 (United Nations Day) with 51 founding members, including India, with a Security Council containing 5 permanent veto-wielding members (USA, USSR, Britain, France, China).'
            ]
        },
        'upsc': {
            'prelims': [
                'World War II officially began on 1 September 1939 with the German invasion of Poland.',
                'The Munich Agreement of September 1938 was signed by Britain, France, Germany, and Italy, permitting Nazi Germany to annex the Sudetenland region of Czechoslovakia.',
                'The Battle of Stalingrad (1942–1943) was the bloodiest battle in human history and marked the decisive turning point against Nazi Germany on the Eastern Front.',
                'Japan attacked the US naval base at Pearl Harbor on 7 December 1941, bringing the United States into World War II.',
                'The D-Day Allied amphibious invasion of Normandy (France), codenamed Operation Overlord, took place on 6 June 1944 under General Dwight D. Eisenhower.',
                'The United States dropped atomic bombs on Hiroshima on 6 August 1945 ("Little Boy") and Nagasaki on 9 August 1945 ("Fat Man").',
                'The United Nations was officially founded on 24 October 1945 following the ratification of the UN Charter by the majority of signatories.'
            ],
            'mains': [
                'Critically evaluate the British and French "Policy of Appeasement" toward Nazi Germany in the 1930s, analyzing why it failed to prevent World War II.',
                'Discuss the military, geopolitical, and psychological turning points of World War II, specifically the Battle of Stalingrad, Battle of Midway, and the Normandy Landings.',
                'Analyze the humanitarian and moral dimensions of the Holocaust and the atomic bombings of Hiroshima and Nagasaki, examining their impact on international humanitarian law.',
                'Compare the League of Nations and the United Nations in terms of their charter, structure, and ability to maintain collective security and prevent world war.'
            ]
        }
    },
    'cold-war-and-decolonisation': {
        'aspects': {
            'Ideological Chasm & Nuclear Brinkmanship': [
                'Bipolar World: Geopolitical and ideological rivalry between the Capitalist West (led by USA) and the Communist East (led by USSR); Winston Churchill\'s "Iron Curtain" speech at Fulton (March 1946); Truman Doctrine (1947 - policy of containment of communism) and Marshall Plan (1948 - economic reconstruction of Western Europe); military alliances: NATO (North Atlantic Treaty Organization, 1949) vs. Warsaw Pact (1955).',
                'Flashpoints & Proxy Wars: Berlin Blockade and Airlift (1948–49); Korean War (1950–1953: 38th parallel division); Cuban Missile Crisis (October 1962: Soviet nuclear missiles in Cuba; President John F. Kennedy instituted naval quarantine; Premier Nikita Khrushchev agreed to withdraw missiles in exchange for US pledge not to invade Cuba and removal of US missiles from Turkey - closest world came to full nuclear annihilation); Vietnam War (1955–1975: American military intervention against Viet Cong and Ho Chi Minh; US withdrawal and communist reunification of Vietnam).'
            ],
            'Decolonization Waves & The Third World': [
                'Global Decolonization: Collapse of British, French, Dutch, and Portuguese colonial empires across Asia and Africa; Indian independence (1947) triggered a domino effect across Burma, Sri Lanka, Malaya, Indonesia, Ghana (Kwame Nkrumah 1957), Kenya, and Algeria (brutal anti-colonial war against France 1954–62).',
                'Non-Aligned Movement (NAM): Afro-Asian leaders refused to join either superpower bloc, asserting strategic autonomy and active peace; 10 Bandung Principles (1955) codified at Belgrade Summit (1961); championed anti-apartheid struggles in South Africa and support for Palestine.'
            ],
            'Gorbachev\'s Reforms & Collapse of the Soviet Union (1991)': [
                'Soviet stagnation: Economic stagnation, costly arms race (Reagan\'s Strategic Defense Initiative / "Star Wars"), bureaucratic corruption, and disastrous Soviet-Afghan War (1979–1989 - "Soviet Vietnam").',
                'Glasnost & Perestroika: General Secretary Mikhail Gorbachev (1985–1991) introduced twin reforms: Glasnost (political openness, freedom of speech, historical truth) and Perestroika (economic restructuring, decentralization, limited private enterprise); abandoned the Brezhnev Doctrine (no longer using military force to maintain communist satellite regimes in Eastern Europe).',
                'Fall of the Wall & Dissolution: Peaceful revolutions across Eastern Europe (Poland Solidarity movement, Velvet Revolution in Czechoslovakia); Fall of the Berlin Wall (9 November 1989) leading to German reunification (1990); hardline communist August 1991 coup attempt defeated by Boris Yeltsin; Belavezha Accords dissolved the USSR; on 25 December 1991, Gorbachev resigned as Soviet President and the Soviet red flag was lowered over the Kremlin, dissolving the USSR into 15 independent republics and ending the Cold War.'
            ]
        },
        'upsc': {
            'prelims': [
                'Winston Churchill delivered his famous "Iron Curtain" speech in March 1946 at Westminster College in Fulton, Missouri, characterizing the division of Europe.',
                'The North Atlantic Treaty Organization (NATO) was established in 1949 as a collective defense alliance against Soviet expansionism.',
                'The Warsaw Pact was formed in 1955 by the Soviet Union and seven Eastern European satellite states as a counterweight to NATO.',
                'The Cuban Missile Crisis occurred in October 1962, bringing the United States and the Soviet Union to the brink of direct nuclear confrontation.',
                'Mikhail Gorbachev introduced the twin policies of "Glasnost" (openness) and "Perestroika" (restructuring) in the Soviet Union in the mid-1980s.',
                'The Berlin Wall fell on 9 November 1989, symbolizing the imminent end of the Cold War and the reunification of Germany.',
                'The Soviet Union was officially dissolved on 26 December 1991, resulting in the emergence of 15 independent successor republics.'
            ],
            'mains': [
                'Critically analyze the causes and consequences of the Cuban Missile Crisis of 1962, examining how nuclear deterrence operated during the Cold War.',
                'Discuss the ideological, economic, and geopolitical factors that led to the collapse of the Soviet Union in 1991, evaluating Mikhail Gorbachev\'s policies of Glasnost and Perestroika.',
                'Analyze the global wave of decolonization in Asia and Africa post-World War II and evaluate the role of the Non-Aligned Movement (NAM) in fostering third-world solidarity.',
                'Examine the transition from a bipolar Cold War world order to a unipolar American-led order post-1991, discussing its impact on global multilateralism.'
            ]
        }
    }
}

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

count = 0
for p in d['periods']:
    pid = p['id']
    if pid in POST_AND_WORLD_ENRICHMENTS:
        enr = POST_AND_WORLD_ENRICHMENTS[pid]
        if 'aspects' in enr:
            p.setdefault('aspects', {})
            for k, v in enr['aspects'].items():
                p['aspects'][k] = v
        if 'upsc' in enr:
            p['upsc'] = enr['upsc']
        count += 1
        print(f"Successfully enriched Post-Independence / World / Mughal period: {pid}")

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Total post-independence / world / mughal periods enriched: {count}")
