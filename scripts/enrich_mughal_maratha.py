import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Enrichment mapping for Mughal, Maratha, Regional, and Sikh history
MUGHAL_MARATHA_ENRICHMENTS = {
    'babur': {
        'aspects': {
            'Central Asian Heritage & Military Innovation': [
                'Lineage and early career: Zahiruddin Muhammad Babur was a Timurid prince of Fergana; descended from Timur on father\'s side and Genghis Khan on mother\'s side; seized Kabul in 1504 CE after losing Samarkand twice.',
                'Tactical revolution in Indian warfare: Introduced gunpowder artillery and field matchlocks (Tufang) to North India, directed by Ottoman master-gunners Ustad Ali Quli and Mustafa Rumi; deployed the Ottoman tactical formation (Rumi device / Araba carts tied together with rawhide ropes) combined with the central Asian flanking maneuver (Tulghuma) to encircle hostile armies.'
            ],
            'Four Decisive Battles': [
                '1. First Battle of Panipat (21 April 1526): Decisively crushed Ibrahim Lodi, breaking the Delhi Sultanate.',
                '2. Battle of Khanwa (16 March 1527 near Bharatpur): Crushed the formidable Rajput confederacy led by Rana Sanga of Mewar; Babur declared the war a Jihad, broke his wine goblets, swore total abstinence, and assumed the triumphant title "Ghazi".',
                '3. Battle of Chanderi (1528): Besieged and captured Chanderi from Rajput ruler Medini Rai, resulting in Rajput women committing Jauhar.',
                '4. Battle of Ghagra (1529): Fought on the Ghagra river (Bihar/UP) against the allied Afghan forces under Mahmud Lodi and Sultan Nusrat Shah of Bengal; secured Mughal hegemony across the entire Gangetic plains from Kabul to Bihar.'
            ],
            'Literary & Aesthetic Genius': [
                'Autobiography (Tuzuk-i-Baburi / Baburnama): Composed in his mother-tongue Chagatai Turkic; celebrated worldwide for unvarnished frankness, acute naturalist observations of Indian flora, fauna, climate, geography, fruits (mango, melons), and psychological portraits of contemporaries; translated into Persian by Abdur Rahim Khan-i-Khanan during Akbar\'s reign.',
                'Charbagh Garden Design: Pioneered the formal symmetrical Persian four-quadrant garden (Charbagh) layout with raised stone pathways and intersecting running water channels; laid out Aram Bagh (Ram Bagh) at Agra.'
            ]
        },
        'upsc': {
            'prelims': [
                'Babur defeated Ibrahim Lodi in the First Battle of Panipat on 21 April 1526, using Ottoman Araba cart lines and Tulghuma flanking tactics.',
                'Babur assumed the title of "Ghazi" after defeating Rana Sanga of Mewar at the Battle of Khanwa in 1527.',
                'Babur\'s autobiography, the Tuzuk-i-Baburi (Baburnama), was originally written in Chagatai Turkic and later translated into Persian by Abdur Rahim Khan-i-Khanan.',
                'Babur introduced the symmetrical Persian four-fold garden layout (Charbagh) into India, creating the Aram Bagh at Agra.',
                'The two master Ottoman artillery experts who directed Babur\'s cannons were Ustad Ali Quli and Mustafa Rumi.',
                'The Battle of Ghagra (1529) was the first major battle in India fought simultaneously on land and in river waters, in which Babur defeated the allied Afghan chiefs.',
                'Babur was initially buried in the Aram Bagh at Agra before his mortal remains were relocated to the Bagh-e-Babur in Kabul according to his will.'
            ],
            'mains': [
                'Evaluate the military innovations introduced by Babur in Indian warfare, with special reference to field artillery, gunpowder, and the Tulghuma tactical system.',
                'Assess the historical, literary, and naturalist value of Babur\'s autobiography, the Baburnama, as a primary source for early 16th-century Indian geography, flora, and society.',
                'Analyze the geopolitical consequences of the Battle of Khanwa (1527), examining why it was far more decisive than the First Battle of Panipat in consolidating Mughal supremacy.'
            ]
        }
    },
    'humayun': {
        'aspects': {
            'Fratricidal Divisions & Afghan Resurgence': [
                'Inherited weaknesses: Nasiruddin Humayun (r. 1530–1540 and 1555–1556 CE) divided his vast, unassimilated empire among his three disloyal brothers according to Timurid tradition: Kamran received Kabul and Kandahar, Askari received Sambhal, and Hindal received Alwar/Mewat; undermined central treasury and unified military command.',
                'Duel with Sher Khan Suri: Confronted the strategic Afghan genius Sher Khan; suffered catastrophic routs at the Battle of Chausa (1539, where Humayun escaped drowning in the Ganga with the help of water-carrier Nizam) and the Battle of Bilgram / Kannauj (1540), forcing Humayun into a 15-year harrowing exile in Sindh, Rajasthan, and Persia.'
            ],
            'Exile in Safavid Persia & Restoration (1555)': [
                'Safavid alliance: Welcomed by Shah Tahmasp I of Safavid Persia; received Persian troops in exchange for ceding Kandahar and embracing Shia rituals; brought illustrious Persian master painters Mir Sayyid Ali and Abdus Samad back to India, founding the Mughal School of Miniature Painting.',
                'Restoration & Death: Recaptured Lahore and Delhi in 1555 CE following the collapse of the Sur successors (defeating Sikandar Suri at the Battle of Sirhind); founded the city of Dinpanah in Delhi; died tragically in January 1556 after tumbling down the steep stone stairs of his library (Sher Mandal) in Delhi; historian Stanley Lane-Poole remarked: "Humayun tumbled through life, and tumbled out of it."'
            ],
            'Humayun\'s Tomb (Prototypical Masterpiece)': [
                'Architectural landmark: Commissioned in 1565 CE by his senior widow Biga Begum (Haji Begum); designed by Persian architect Mirak Mirza Ghiyas; first monumental garden-tomb (Charbagh) on the Indian subcontinent; first monument to feature a colossal double-dome of white marble, red sandstone cladding, and octagonal Hasht-Bihisht chambers; direct stylistic progenitor of the Taj Mahal.'
            ]
        },
        'upsc': {
            'prelims': [
                'Humayun was decisively routed by Sher Shah Suri at the Battle of Chausa (1539) and the Battle of Bilgram/Kannauj (1540), driving him into exile.',
                'Humayun regained the throne of Delhi in 1555 CE by defeating Sikandar Suri at the Battle of Sirhind.',
                'Humayun brought master Persian miniature painters Mir Sayyid Ali and Abdus Samad to India, laying the foundation of the Mughal atelier.',
                'Humayun built the fortress city of Dinpanah on the banks of the Yamuna in Delhi.',
                'Humayun died in 1556 CE from injuries sustained after falling down the staircase of the Sher Mandal library building in Purana Qila.',
                'Humayun\'s Tomb in Delhi was designed by the Persian architect Mirak Mirza Ghiyas and commissioned by his widow Haji Begum (Biga Begum).',
                'The Humayun-Nama, an intimate biographical account of Humayun\'s life and court, was composed in Persian by his sister Gulbadan Begum.'
            ],
            'mains': [
                'Examine the internal and external factors that caused the collapse of Humayun\'s empire in 1540 CE, evaluating his personal character and political miscalculations.',
                'Assess the architectural significance of Humayun\'s Tomb in Delhi, explaining how it served as a transitional model and structural prototype for the Taj Mahal.',
                'Discuss the cultural impact of Humayun\'s exile at the Safavid court of Persia on the evolution of Mughal art, architecture, and court etiquette.'
            ]
        }
    },
    'sur-interregnum': {
        'aspects': {
            'Sher Shah Suri\'s Administrative Zenith': [
                'Rise from Farid to Sultan: Born Farid Khan in Sasaram (Bihar); awarded the title "Sher Khan" after slaying a tiger single-handedly; established the Second Afghan Empire (r. 1540–1545 CE).',
                'Hierarchical administrative structure: Empire divided into 47 territorial divisions called Sarkars; each Sarkar administered by two royal officers: Shiqdar-i-Shiqdaran (law, order, and criminal justice) and Munsif-i-Munsifan (revenue assessment and civil disputes); each Sarkar was subdivided into several Parganas headed by a Shiqdar (executive), Amin/Munsif (revenue), Fotadar (treasurer), and two Karkuns (Persian and Hindi record scribes).'
            ],
            'Pioneering Agrarian & Currency Reforms': [
                'Rai system of crop measurement: Land scientifically measured using a standard rope Gaz-i-Sikandari; cultivable soil classified into three grades based on fertility: Good, Middling, and Bad; average yield calculated and state revenue fixed at 1/3rd of produce, payable in cash or kind.',
                'Patta and Qabuliyat: Instituted written title deeds (Patta) issued by the state specifying the peasant\'s land holdings and assessed tax, while the cultivator signed an agreement deed of acceptance (Qabuliyat); eliminated fraudulent extortion by corrupt revenue officers.',
                'Standardized Imperial Coinage: Reformed monetary chaos by introducing standard tri-metallic coinage: pure silver Rupiya (178 grains of high-purity silver, which served as the direct ancestor of modern Indian currency) and copper Dam (380 grains; exchange ratio 1 Rupiya = 64 Dams).'
            ],
            'Communications, Highway Infrastructure & Tomb': [
                'Sadak-e-Azam (Grand Trunk Road): Re-engineered and paved the ancient imperial highway from Sonargaon (Bengal) through Delhi and Lahore to Peshawar (Indus river) spanning over 2,500 km; lined with shady trees, fruit orchards, and freshwater wells.',
                'Sarais (Caravanserais) & Postal Dak: Constructed 1,700 fortified roadside inns (Sarais) every two kos (approx 6 km), providing separate food, water, and lodging for Hindus and Muslims; functioned as state post-houses (Dak-Chowkis) where horses were kept for rapid message transmission.',
                'Mausoleum at Sasaram: Magnificent octagonal red sandstone tomb built in the middle of a vast artificial lake at Sasaram (Bihar), representing the transition from Sultanate architectural massiveness to Mughal aesthetic grace; died in 1545 CE during the siege of Kalinjar fort due to an accidental explosion of a gunpowder magazine.'
            ]
        },
        'upsc': {
            'prelims': [
                'Sher Shah Suri introduced the standard silver coin called "Rupiya" (178 grains) and copper coin called "Dam" (380 grains), with an exchange ratio of 1 Rupiya = 64 Dams.',
                'The system of "Patta" (deed of title) and "Qabuliyat" (deed of agreement) for peasant land revenue settlement was introduced by Sher Shah Suri.',
                'Under Sher Shah, the empire was divided into Sarkars, each headed by a Shiqdar-i-Shiqdaran (law and order) and Munsif-i-Munsifan (revenue).',
                'Sher Shah rebuilt the ancient highway from Sonargaon (Bengal) to Peshawar, known as the "Sadak-e-Azam", later named the "Grand Trunk Road" by Lord Auckland.',
                'Sher Shah constructed 1,700 roadside Sarais (inns) that also functioned as royal postal exchange stations (Dak-Chowkis).',
                'The magnificent octagonal tomb of Sher Shah Suri, standing in the centre of a large artificial water tank, is located at Sasaram (Bihar).',
                'Sher Shah Suri died in 1545 CE during the siege of Kalinjar Fort (Bundelkhand) when a store of gunpowder exploded accidentally.'
            ],
            'mains': [
                'Critically examine the administrative, agrarian, and monetary reforms of Sher Shah Suri, evaluating why historians describe him as the "fore-runner of Akbar".',
                'Analyze the infrastructure, trade, and communication achievements of Sher Shah Suri with special reference to the Sadak-e-Azam and the Sarai postal network.',
                'Assess the architectural features of Sher Shah\'s Tomb at Sasaram and the Qila-i-Kuhna Mosque in Purana Qila, Delhi.'
            ]
        }
    },
    'akbar-the-great': {
        'aspects': {
            'Consolidation & Rajput Matrimonial Policy': [
                'Accession & Regency: Crowned at Kalanaur (Punjab) at age 13 (1556 CE); regency of Bairam Khan (Khan-i-Khanan); defeated Hemu (Hemu Vikramaditya) at the Second Battle of Panipat (5 November 1556); ended Petticoat Government (Maham Anaga) in 1562 CE.',
                'Rajput Conciliation Policy: Married Harkha Bai (Jodha Bai / Mariam-uz-Zamani), daughter of Raja Bharmal of Amber (1562 CE); inducted Rajput princes into highest imperial ranks (Raja Bhagwant Das, Raja Man Singh, Todar Mal); conquered Chittor (1568; siege resisted by Jaimal and Patta) and Ranthambore; Maharana Pratap resisted heroically, fighting the epic Battle of Haldighati (18 June 1576; Mughal army commanded by Raja Man Singh).'
            ],
            'Mansabdari System & Military Hierarchy': [
                'Institutional structure: Universal administrative, civil, and military cadre introduced in 1571 CE; every officer assigned a numerical rank (Mansab) ranging from 10 to 10,000 (highest reserved for princes).',
                'Zat and Sawar duality: Introduced dual ranks in 1595–96 CE: Zat indicated the officer\'s personal status, hierarchical standing, and basic salary; Sawar determined the number of mounted horsemen (cavalry troops) the officer was obligated to maintain for state service.',
                'Dagh and Chehra: Revived the branding of horses (Dagh) and descriptive rolls of troopers (Chehra); classified troops into Dah-Bisti (2 horses per trooper); payment made either in cash (Naqdi) or through revenue assignments of land (Jagir).'
            ],
            'Todar Mal\'s Dahsala (Zabt) Land Revenue': [
                'Ain-i-Dahsala (1580 CE): Formulated by finance minister Raja Todar Mal; average yield of each crop and its average market price over the past 10 years (1570–1580) were scientifically calculated; state revenue share fixed at one-third (33.3%) of average produce, payable in cash.',
                'Land classification into 4 categories: 1. Polaj (annually cultivated land, never left fallow), 2. Parauti (land left fallow for 1 or 2 years to regain fertility), 3. Chachar (land left fallow for 3 to 4 years), 4. Banjar (uncultivated wasteland for 5 or more years).',
                'Measurement & Offices: Replaced rope measurement with bamboo rods joined with iron rings (Tanab / Bamboo jarib); introduced the Ilahi Gaz (41 digits / 33 inches). Pargana officers: Amalguzar (revenue collector), Qanungo (keeper of village revenue records), Patwari (village accountant).'
            ],
            'Religious Evolution: Ibadat Khana to Sulh-i-Kul': [
                'Early reforms: Abolished pilgrimage tax on Hindus (1563 CE) and repealed Jizya (1564 CE).',
                'Ibadat Khana (House of Worship, 1575 CE): Erected at Fatehpur Sikri; initially for debates among Sunni Muslim scholars; later opened in 1578 CE to representatives of all faiths: Purushottam and Devi (Hinduism), Dastur Meherji Rana (Zoroastrianism / Parsi), Harivijaya Suri and Vijayasena Suri (Jainism - awarded title Jagadguru), Father Rudolf Acquaviva and Antonio Monserrate (Jesuit Portuguese Christianity).',
                'Mahzarnama (Infallibility Decree, September 1579): Drafted by Sheikh Mubarak (father of Abul Fazl and Faizi); proclaimed Akbar as the "Imam-i-Adil" (supreme arbiter in religious disputes), empowering him to choose any interpretation of Islamic law consistent with public welfare.',
                'Sulh-i-Kul & Din-i-Ilahi (Tauhid-i-Ilahi, 1582 CE): Ethos of universal peace, toleration, and harmony (Sulh-i-Kul); launched Din-i-Ilahi as an ethical-spiritual fellowship promoting reason, self-restraint, and devotion to the Emperor without dogma, holy book, or priestly class; only 18 prominent courtiers joined, including Raja Birbal.'
            ],
            'Art, Literature & Fatehpur Sikri': [
                'Fatehpur Sikri Capital: Founded in 1571 CE near shrine of Sufi saint Shaikh Salim Chishti; built Buland Darwaza (lofty 176-foot triumphal gateway commemorating Gujarat conquest 1572), Panch Mahal (five-storey pyramidal colonnaded palace), Diwan-i-Khas (with central carved pillar bracket), Jodha Bai\'s Palace.',
                'Navaratnas & Literary translations: Court adorned by Nine Gems (Abul Fazl, Faizi, Tansen, Birbal, Todar Mal, Man Singh, Abdur Rahim Khan-i-Khanan, Fakir Aziao-Din, Mullah Do-Piyaza); Abul Fazl authored Akbarnama and Ain-i-Akbari; Maktab Khana (translation bureau) translated Mahabharata into Persian as Razmnama (illustrated by Daswant and Basawan), Ramayana, and Rajatarangini.'
            ]
        },
        'upsc': {
            'prelims': [
                'Akbar introduced the Mansabdari system based on the twin ranks of "Zat" (personal status and salary) and "Sawar" (cavalry quota required to maintain).',
                'The "Ain-i-Dahsala" system of land revenue, introduced in 1580 CE, was engineered by Akbar\'s finance minister Raja Todar Mal.',
                'Under Akbar\'s revenue system, land was classified into four categories: Polaj (regularly cultivated), Parauti (fallow 1–2 yrs), Chachar (fallow 3–4 yrs), and Banjar (fallow 5+ yrs).',
                'Akbar established the Ibadat Khana (Hall of Prayer) at Fatehpur Sikri in 1575 CE for inter-faith religious debates.',
                'The "Mahzarnama" (Infallibility Decree) was issued in 1579 CE, declaring Akbar the supreme arbiter (Imam-i-Adil) in religious disputes.',
                'Akbar abolished the pilgrimage tax in 1563 CE and the Jizya tax on non-Muslims in 1564 CE.',
                'The Buland Darwaza at Fatehpur Sikri was built by Akbar in 1601 CE to commemorate his conquest of Gujarat.'
            ],
            'mains': [
                'Critically evaluate the administrative and military structure of the Mansabdari system, discussing how the dual Zat and Sawar ranks functioned.',
                'Trace the intellectual and religious evolution of Akbar from orthodoxy to the Ibadat Khana debates, the Mahzarnama, and the philosophy of Sulh-i-Kul.',
                'Analyze the features and economic impact of Todar Mal\'s Dahsala (Zabt) system on the agrarian economy of the Mughal Empire.',
                'Examine Akbar\'s Rajput policy, highlighting the diplomatic balance of matrimonial alliances, military induction, and religious toleration in building an all-India empire.'
            ]
        }
    },
    'jahangir': {
        'aspects': {
            'Consolidation & The Golden Chain of Justice': [
                'Accession & Twelve Edicts: Nuruddin Muhammad Jahangir (r. 1605–1627 CE) installed the famous Zanjir-i-Adl (Golden Chain of Justice) linking the Shah Burj of Agra Fort to a stone post on the Yamuna bank, equipped with 60 golden bells for direct access by any oppressed subject; issued 12 imperial decrees (Dastur-ul-Amal) prohibiting arbitrary transit cesses (Tamgha), house confiscation, and animal slaughter on certain days.',
                'Rebellion of Prince Khusrau (1606): Eldest son Prince Khusrau revolted with blessings of fifth Sikh Guru, Guru Arjan Dev; Khusrau was captured and blinded; Guru Arjan Dev was executed at Lahore, creating an enduring rift between the Mughal state and the Sikh Panth.'
            ],
            'Diplomacy & European Contacts': [
                'Mewar Settlement (1615 CE): Concluded an honorable peace treaty with Rana Amar Singh of Mewar negotiated by Prince Khurram (Shah Jahan); Rana was exempt from personal attendance at court and sent crown prince Karan Singh as Mansabdar of 5,000; Chittor fort restored on condition it would not be fortified.',
                'British East India Company Embassies: Captain William Hawkins (1608–1611, received 400 Mansab, styled "English Khan") and Sir Thomas Roe (1615–1619, ambassador of King James I of England); Roe secured imperial farmans granting English trading factories at Surat, Cambay, and Ahmedabad.'
            ],
            'Nur Jahan Junta & Artistic Splendor': [
                'Nur Jahan (Mehr-un-Nisa): Married Jahangir in 1611 CE; assumed title "Nur Mahal" then "Nur Jahan" (Light of the World); formed the powerful court faction (Junta) consisting of herself, her father Mirza Ghiyas Beg (Itmad-ud-Daula), brother Asaf Khan, and Prince Khurram; royal coins struck jointly in her name; issued imperial farmans.',
                'Mughal Miniature Painting Zenith: Jahangir was a consummate aesthetic connoisseur (boasted in his autobiography Tuzuk-i-Jahangiri that he could identify the brushstrokes of individual artists on a single portrait); specialized in naturalist studies of birds, animals, flowers, and individual portraiture; master court artists: Ustad Mansur (Wunder of the Age / Nadir-ul-Asr, famed for painting the Siberian crane, Dodo, and Bengal Florican), Abul Hasan (Nadir-uz-Zaman), Bishandas, Manohar, and Govardhan.',
                'Itmad-ud-Daula\'s Tomb (Agra): Built by Nur Jahan (1622–1628 CE); first monument built entirely of white marble inlaid with extensive delicate Pietra Dura (semi-precious stone inlays forming floral arabesques), serving as the stylistic transition from red sandstone to Shah Jahan\'s marble architecture.'
            ]
        },
        'upsc': {
            'prelims': [
                'Jahangir installed the "Zanjir-i-Adl" (Chain of Justice) with 60 bells at Agra Fort to provide direct access to royal justice.',
                'The fifth Sikh Guru, Guru Arjan Dev, was executed in 1606 CE during the reign of Jahangir for blessing the rebellious Prince Khusrau.',
                'Sir Thomas Roe visited the court of Jahangir as an official ambassador of King James I of England in 1615 CE, securing trading concessions for the British East India Company.',
                'The court painter Ustad Mansur was conferred the title "Nadir-ul-Asr" by Jahangir for his peerless scientific paintings of rare birds, animals, and flora.',
                'The tomb of Itmad-ud-Daula in Agra, built by Nur Jahan, was the first Mughal structure made entirely of white marble adorned with extensive Pietra Dura inlay work.',
                'Jahangir recorded his memoirs in Persian in his autobiography, the Tuzuk-i-Jahangiri.',
                'In 1615 CE, Jahangir successfully concluded a historic peace treaty with Rana Amar Singh of Mewar, ending decades of hostilities without humiliating the Rajput house.'
            ],
            'mains': [
                'Evaluate the political and administrative influence of Nur Jahan and the "Nur Jahan Junta" on the imperial court and foreign policy during Jahangir\'s reign.',
                'Analyze the development of Mughal miniature painting under Jahangir\'s patronage, highlighting the naturalist works of Ustad Mansur and Abul Hasan.',
                'Assess the commercial and geopolitical implications of the diplomatic missions of Captain William Hawkins and Sir Thomas Roe to the court of Jahangir.'
            ]
        }
    },
    'shah-jahan': {
        'aspects': {
            'Golden Age of Mughal Architecture': [
                'Culmination of Imperial Building: Shahabuddin Muhammad Shah Jahan (r. 1628–1658 CE) represented the architectural zenith of the dynasty, shifting preference from red sandstone to pristine white Makrana marble, bulbous double domes, cusped multifoil arches, and delicate Pietra Dura floral inlay.',
                'Taj Mahal (Agra): Built (1631–1648 CE) as a mausoleum for his beloved consort Arjumand Banu Begum (Mumtaz Mahal); designed by architect Ustad Ahmad Lahori; perfect bilateral symmetry, central white marble dome framed by four slender minarets, Charbagh garden setting, reflecting pools, and Quranic calligraphy by Amanat Khan Shirazi.',
                'Shahjahanabad & Red Fort: Shifted imperial capital from Agra to Delhi, founding the walled metropolis of Shahjahanabad (1638 CE); constructed the massive Red Fort (Lal Qila) containing the Diwan-i-Aam, Diwan-i-Khas (inscribed: "If there is paradise on earth, it is here, it is here, it is here"), Rang Mahal, and the legendary Peacock Throne (Takht-i-Taus) studded with diamonds and emeralds; built the monumental Jama Masjid of Delhi; founded the Moti Masjid (Pearl Mosque) at Agra Fort.'
            ],
            'Deccan Expeditions & Foreign Policy': [
                'Subjugation of Deccan: Annexed the Nizam Shahi kingdom of Ahmednagar (1633 CE); compelled Bijapur (Adil Shah) and Golconda (Qutb Shah) to accept Mughal suzerainty, pay tribute, and mention Shah Jahan in Friday Khutba (1636 CE); appointed Prince Aurangzeb as Viceroy of Deccan twice (1636–44 and 1653–57; where Murshid Quli Khan reformed Deccan revenue administration).',
                'Central Asian failures: Dispatched three disastrous imperial expeditions to Balkh and Badakhshan (1646–47 CE) and three failed sieges of Kandahar (1649, 1652, 1653 CE) against Safavid Persia, draining over 120 million rupees from the imperial treasury without territorial gain.'
            ],
            'Dara Shikoh & The War of Succession (1657–1658)': [
                'Dara Shikoh\'s syncretism: Eldest son and chosen heir; mystical Sufi scholar of Qadiri order; translated 50 Upanishads from Sanskrit into Persian under the title Sirr-i-Akbar (The Great Secret); authored Majma-ul-Bahrain (The Mingling of Two Oceans), harmonizing Sufi Islam and Advaita Vedanta philosophy; translated the Bhagavad Gita and Yoga Vasistha into Persian.',
                'War of Succession: Illness of Shah Jahan triggered a fratricidal war among his four sons: Dara Shikoh, Shah Shuja, Aurangzeb, and Murad Bakhsh; Aurangzeb defeated imperial armies at Battle of Dharmat (April 1658) and crushed Dara Shikoh at the decisive Battle of Samugarh (May 1658 near Agra); imprisoned father Shah Jahan in Agra Fort for his remaining 8 years (overlooking the Taj Mahal); executed Dara Shikoh and Murad, driving Shuja to perish in the Arakan jungles.'
            ]
        },
        'upsc': {
            'prelims': [
                'Ustad Ahmad Lahori was the chief architect of the Taj Mahal and the Red Fort of Delhi under Shah Jahan.',
                'Dara Shikoh translated 50 Upanishads into Persian under the title "Sirr-i-Akbar" (The Great Secret) and authored the comparative philosophical classic Majma-ul-Bahrain.',
                'The legendary Peacock Throne (Takht-i-Taus), which housed the Koh-i-Noor diamond, was commissioned by Shah Jahan and crafted by Bebadal Khan.',
                'The decisive Battle of Samugarh (May 1658) was fought between Aurangzeb and Dara Shikoh, determining the succession to the Mughal throne.',
                'Shah Jahan shifted the Mughal capital from Agra to Delhi in 1638 CE, founding the new walled imperial city of Shahjahanabad.',
                'Murshid Quli Khan reformed the land revenue administration of the Deccan during Aurangzeb\'s second viceroyalty under the reign of Shah Jahan.',
                'Shah Jahan was imprisoned by Aurangzeb in the Musamman Burj of Agra Fort from 1658 until his death in 1666 CE.'
            ],
            'mains': [
                'Critically evaluate the architectural achievements of Shah Jahan, analyzing the aesthetic, symmetry, and engineering features that distinguished his monuments from earlier Mughal buildings.',
                'Examine the intellectual and religious contributions of Dara Shikoh, assessing the significance of his Persian translations of the Upanishads and Majma-ul-Bahrain.',
                'Analyze the political, psychological, and military factors that led to Aurangzeb\'s victory over Dara Shikoh in the War of Succession (1657–1658).',
                'Discuss the geopolitical and fiscal consequences of Shah Jahan\'s Central Asian expeditions (Balkh and Badakhshan) and the sieges of Kandahar.'
            ]
        }
    },
    'aurangzeb': {
        'aspects': {
            'Orthodoxy & Administrative Measures': [
                'Ascension & Regnal Title: Muhi-ud-Din Muhammad Aurangzeb assumed title "Alamgir" (Conqueror of the World; r. 1658–1707 CE); discontinued court practices deemed un-Islamic: banned Nauroz celebration, Jharokha Darshan (balcony royal viewing), Tula Dan (weighing the Emperor against gold/silver), music at court, and drinking of alcohol; appointed Muhtasibs (censors of public morals) to enforce Sharia.',
                'Taxation and religious measures: Re-imposed Jizya tax on non-Muslim subjects in 1679 CE; abolished nearly 80 transit tolls (Abwabs); commissioned the monumental encyclopaedic compendium of Hanafi Islamic jurisprudence, Fatawa-i-Alamgiri; executed the ninth Sikh Guru, Guru Tegh Bahadur, at Chandni Chowk Delhi (1675 CE) for defending Kashmiri Pandits.'
            ],
            'Agrarian Crises & Popular Rebellions': [
                'Agrarian resistance: Irfan Habib\'s "Agrarian Crisis" thesis: hyper-exploitation by short-term Jagirdars caused flight of peasants and widespread armed revolts.',
                'Major rebellions: 1. Jat Rebellion in Mathura/Agra led by Gokula (1669), Rajaram (1685, who plundered Akbar\'s tomb at Sikandra), and Churaman (founded Bharatpur kingdom); 2. Satnami Revolt (1672 near Narnaul, Haryana; armed peasant-religious revolt); 3. Bundela Rebellion under Raja Chhatrasal (establishing an autonomous Bundelkhand state); 4. Sikh resistance under Guru Gobind Singh (created Khalsa Panth in 1699 CE at Anandpur Sahib; fought battles of Chamkaur and Muktsar; sent Persian letter of moral admonition Zafarnama to Aurangzeb).'
            ],
            'Deccan Campaigns: "The Deccan Ulcer"': [
                'Prolonged southern quagmire: Annexed the Sultanate of Bijapur (1686 CE) and the Sultanate of Golconda (1687 CE); executed Maratha king Chhatrapati Sambhaji (1689 CE) and imprisoned infant Shahu.',
                'The Deccan Ulcer: Spent the last 25 uninterrupted years of his reign (1681–1707 CE) living in military tents in the Deccan fighting intractable Maratha guerrilla warfare (led by Rajaram, Santaji Ghorpade, Dhanaji Jadhav, and Queen Tarabai); drained imperial finances, neglected North Indian administration, and ruined the grand army; historian V.A. Smith remarked: "The Deccan was the grave of his reputation as well as of his body."'
            ]
        },
        'upsc': {
            'prelims': [
                'Aurangzeb re-imposed the Jizya tax on non-Muslim subjects in 1679 CE, 115 years after its repeal by Akbar.',
                'Guru Tegh Bahadur, the ninth Sikh Guru, was executed at Chandni Chowk in Delhi in 1675 CE on the orders of Aurangzeb; Gurdwara Sis Ganj marks the site.',
                'Aurangzeb annexed the Sultanate of Bijapur in 1686 CE and the Sultanate of Golconda in 1687 CE into the Mughal Empire.',
                'Fatawa-i-Alamgiri, the comprehensive encyclopaedia of Islamic law (Hanafi jurisprudence), was compiled by a board of scholars under Aurangzeb\'s patronage.',
                'Aurangzeb built the Bibi ka Maqbara at Aurangabad in 1679 CE as a memorial to his wife Dilras Banu Begum (Rabia-ud-Daurani), known as the "Poor Man\'s Taj".',
                'Aurangzeb appointed moral officers called "Muhtasibs" to inspect markets, regulate weights, and enforce Islamic ethical codes in public life.',
                'The Zafarnama (Epistle of Victory) was a famous Persian letter of moral defiance written by the tenth Sikh Guru, Guru Gobind Singh, addressed to Aurangzeb in 1705 CE.'
            ],
            'mains': [
                'Critically evaluate the religious policies of Aurangzeb, analyzing whether his measures (re-imposition of Jizya, demolition of temples, banning of court music) were religiously dogmatic or politically motivated.',
                'Examine the "Deccan Ulcer" thesis with reference to Aurangzeb\'s 25-year campaigns in South India, explaining how the annexation of Bijapur and Golconda contributed to the financial and military collapse of the Mughal Empire.',
                'Analyze the socio-economic causes of agrarian rebellions during Aurangzeb\'s reign, specifically the uprisings of the Jats, Satnamis, and Bundelas.',
                'Discuss the Jagirdari Crisis of the late 17th century as articulated by Satish Chandra, examining the imbalance between Paibaqi land and Mansabdar expectations (Be-Jagiri).'
            ]
        }
    },
    'maratha-empire': {
        'aspects': {
            'Chhatrapati Shivaji Maharaj & Hindavi Swarajya': [
                'Early career and fort conquests: Born at Shivneri Fort (1630 CE); inspired by mother Jijabai and mentor Dadoji Kondadev; conquered strategic hill-forts: Torna (1646, first conquest), Kondana (renamed Sinhagad), and Raigad; slayed Bijapur general Afzal Khan with tiger claws (Bagh Nakh) at Pratapgad (1659); wounded Mughal viceroy Shaista Khan in a night raid on his palace at Lal Mahal, Pune (1663); sacked the premier Mughal commercial port of Surat twice (1664 and 1670).',
                'Treaty of Purandar (1665 CE): Concluded with Rajput general Raja Jai Singh I; Shivaji surrendered 23 of his 35 hill forts to the Mughals, retaining 12 forts; agreed to send son Sambhaji as a 5,000 Mansabdar; escaped from house arrest in Agra in a sweetmeat basket (1666 CE).',
                'Coronation & Royal Titles (1674 CE): Solemnly crowned as sovereign monarch (Chhatrapati) at Raigad Fort on 6 June 1674 by Pandit Gaga Bhatt of Varanasi; assumed titles "Haidava Dharmoddharak" (Protector of the Hindu Faith) and "Kshatriya Kulavantas".'
            ],
            'Ashtapradhan Council & Fiscal Structure': [
                'Ashtapradhan (Council of Eight Ministers): Advisory cabinet directly responsible to the King: 1. Peshwa / Mukhya Pradhan (Prime Minister / general administration), 2. Amatya / Majumdar (Finance and revenue minister), 3. Senapati / Sari-Naubat (Commander-in-Chief of army), 4. Waqia-Navis / Mantri (Intelligence and home records), 5. Sachiv / Shuru-Navis (Royal correspondence and edicts), 6. Sumant / Dabir (Foreign minister), 7. Nyayadhish (Chief Justice), 8. Panditrao (Charity, religious endowments, and rituals).',
                'Revenue system (Chauth & Sardeshmukhi): Assessment based on Kathi measuring rod (Malik Ambar system); state share fixed at 40% of produce; extracted two famous levies from neighboring Mughal and foreign territories: 1. Chauth (one-fourth / 25% of gross revenue collected in exchange for protection against Maratha raids), 2. Sardeshmukhi (additional 10% levy claimed by Shivaji as the hereditary supreme lord / Sardeshmukh of Maharashtra).',
                'Military organization: Disciplined cavalry divided into Bargirs (state-mounted troopers provided with state horses and weapons) and Silahdars (cavalrymen bringing their own horses and arms); naval fleet (pioneered by Kanhoji Angre, "Father of the Indian Navy").'
            ],
            'Peshwa Hegemony & The Panipat Catastrophe (1761)': [
                'Rise of the Peshwas: Balaji Vishwanath (First hereditary Peshwa, 1713–1720; secured imperial Farman from Farrukhsiyar in 1719 recognizing Chauth/Sardeshmukhi rights across the 6 Deccan Subahs); Baji Rao I (1720–1740; brilliant cavalry commander, champion of "Hindu Pad-Padshahi", conquered Malwa, Gujarat, Bundelkhand, defeated Nizam at Palkhed 1728, dashed to Delhi gates 1737: "Strike at the trunk of the withered tree, and the branches will fall of themselves").',
                'Balaji Baji Rao (Nana Saheb, 1740–1761): Sangola Agreement (1750) transferring de facto imperial sovereignty from the Chhatrapati to the Peshwa at Pune; Maratha power expanded from Cuttack to Attock (hoisting flag on Indus under Raghunath Rao 1758).',
                'Third Battle of Panipat (14 January 1761): Maratha confederacy army led by Sadashivrao Bhau and Vishwasrao, with artillery under Ibrahim Khan Gardi, confronted Afghan invader Ahmad Shah Abdali; alienated potential allies (Rajputs, Jats, Awadh Nawab Shuja-ud-Daula backed Abdali); Marathas were annihilated, losing 100,000 soldiers and top leadership; shattered dream of pan-Indian Maratha empire and cleared the way for the British East India Company.'
            ]
        },
        'upsc': {
            'prelims': [
                'Shivaji was formally crowned as "Chhatrapati" at Raigad Fort in 1674 CE by Pandit Gaga Bhatt of Varanasi.',
                'The Treaty of Purandar was signed in 1665 CE between Chhatrapati Shivaji and Raja Jai Singh I representing Mughal Emperor Aurangzeb.',
                'Shivaji\'s council of eight ministers was known as the "Ashtapradhan", with the Peshwa serving as the prime minister.',
                'In the Maratha fiscal system, "Chauth" was 25% of land revenue collected from neighboring regions for protection, while "Sardeshmukhi" was an additional 10% levy claimed as hereditary chief.',
                'In the Maratha cavalry, "Bargirs" were soldiers supplied with horses and equipment by the state, whereas "Silahdars" provided their own horses and arms.',
                'Peshwa Baji Rao I defeated the Nizam of Hyderabad at the Battle of Palkhed in 1728 CE through brilliant cavalry mobility.',
                'The Third Battle of Panipat took place on 14 January 1761, where Ahmad Shah Abdali crushed the Maratha army led by Sadashivrao Bhau.'
            ],
            'mains': [
                'Evaluate the military strategy and administrative institutions of Chhatrapati Shivaji Maharaj, analyzing how the Ashtapradhan and hill-fort defense system helped establish "Swarajya".',
                'Examine the nature and economic impact of Chauth and Sardeshmukhi in the expansion of the Maratha Empire across the Deccan and Northern India.',
                'Critically analyze the causes and long-term historical consequences of the Maratha defeat at the Third Battle of Panipat (1761), assessing its impact on British colonial ascendancy.',
                'Trace the transformation of the Maratha state from Shivaji\'s centralized monarchy to the decentralized Peshwa-led Maratha Confederacy (Scindia, Holkar, Gaekwad, Bhonsle).'
            ]
        }
    },
    'sikh-empire': {
        'aspects': {
            'Ten Gurus & Evolution of the Khalsa': [
                'Spiritual foundations: Guru Nanak (1469–1539, founded Sikhism, Langar institution); Guru Angad (standardized Gurmukhi script); Guru Amar Das (Manji system, opposed Sati and Purdah); Guru Ram Das (founded Amritsar / Ramdaspur); Guru Arjan Dev (compiled the Adi Granth in 1604 CE, built Harmandir Sahib / Golden Temple, executed by Jahangir in 1606 CE).',
                'Militarization: Guru Hargobind (introduced concept of Miri / temporal authority and Piri / spiritual authority, constructed the Akal Takht opposite Golden Temple); Guru Har Rai and Guru Har Krishan; Guru Tegh Bahadur (martyred by Aurangzeb in 1675 at Chandni Chowk); Guru Gobind Singh (created the Khalsa Panth on Baisakhi 1699 at Anandpur Sahib, instituting the Five Ks: Kesh, Kangha, Kara, Kachhera, Kirpan; ended personal Guruship, vesting eternal spiritual authority in Guru Granth Sahib).',
                'Banda Singh Bahadur & 12 Misls: Banda Singh Bahadur abolished the Zamindari system in Punjab and struck coins in the names of Guru Nanak and Guru Gobind Singh; martyred in Delhi (1716 CE); rise of Dal Khalsa and 12 autonomous military confederacies (Misls: Sukerchakia, Bhangi, Ahluwalia, Phulkian, Ramgarhia, etc.).'
            ],
            'Maharaja Ranjit Singh & The Sikh Empire': [
                'Unification of Punjab: Born into the Sukerchakia Misl; captured Lahore (1799 CE, made his capital) and Amritsar (1802 CE); unified Punjab from the Satluj to Khyber Pass, including Kashmir (1819), Multan (1818), and Peshawar (1834); styled "Sher-e-Punjab" (Lion of Punjab); gilded the sanctum of Harmandir Sahib with gold leaf; recovered the Koh-i-Noor diamond from Afghan ruler Shah Shuja.',
                'Military Modernization (Fauj-i-Khas): Created the second most formidable standing army in Asia after the British; recruited European generals (General Jean-Baptiste Ventura, Jean-Francois Allard, Paolo Avitabile, Claude Court) to drill infantry and artillery along modern Napoleonic lines; established royal foundries producing horse-artillery cannons in Lahore.',
                'Anglo-Sikh Wars & Annexation: Treaty of Amritsar (1809) with Lord Minto fixed the Satluj river as the eastern boundary; death of Ranjit Singh (1839) led to court anarchy; First Anglo-Sikh War (1845–46: battles of Mudki, Ferozeshah, Aliwal, Sobraon; concluded by Treaty of Lahore 1846); Second Anglo-Sikh War (1848–49: battles of Ramnagar, Chillianwala, Gujarat; Punjab annexed on 29 March 1849 by Lord Dalhousie; young Maharaja Duleep Singh pensioned off to England and Koh-i-Noor surrendered to Queen Victoria).'
            ]
        },
        'upsc': {
            'prelims': [
                'Guru Gobind Singh established the Khalsa Panth at Anandpur Sahib on Baisakhi day in 1699 CE, introducing the "Five Ks" and the baptismal ceremony of Khande di Pahul.',
                'The Akal Takht (Throne of the Timeless One) facing the Harmandir Sahib was established in 1606 CE by the sixth Sikh Guru, Guru Hargobind.',
                'Maharaja Ranjit Singh belonged to the Sukerchakia Misl and established his capital at Lahore in 1799 CE.',
                'The Treaty of Amritsar was signed in 1809 between Maharaja Ranjit Singh and Charles Metcalfe (representing the British), fixing the Satluj river as the boundary.',
                'The modernization of Maharaja Ranjit Singh\'s army (Fauj-i-Khas) was directed by European generals including Jean-Baptiste Ventura (French) and Jean-Francois Allard (French).',
                'The Second Anglo-Sikh War concluded in 1849 following the decisive Battle of Gujarat ("Battle of the Guns"), leading to Dalhousie\'s annexation of Punjab.',
                'Maharaja Ranjit Singh donated gold to plate the marble dome of Harmandir Sahib in Amritsar and the Kashi Vishwanath Temple in Varanasi.'
            ],
            'mains': [
                'Trace the socio-religious and military transformation of the Sikh community from a pacifist devotional fellowship under Guru Nanak into the armed Khalsa brotherhood under Guru Gobind Singh.',
                'Critically evaluate the administrative, military, and secular statecraft of Maharaja Ranjit Singh, highlighting the modern organization of the Fauj-i-Khas.',
                'Analyze the causes, military campaigns, and geopolitical consequences of the two Anglo-Sikh Wars (1845–1849), leading to the annexation of Punjab by the British East India Company.'
            ]
        }
    }
}

with open('data/history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

count = 0
for p in d['periods']:
    pid = p['id']
    if pid in MUGHAL_MARATHA_ENRICHMENTS:
        enr = MUGHAL_MARATHA_ENRICHMENTS[pid]
        if 'aspects' in enr:
            p.setdefault('aspects', {})
            for k, v in enr['aspects'].items():
                p['aspects'][k] = v
        if 'upsc' in enr:
            p['upsc'] = enr['upsc']
        count += 1
        print(f"Successfully enriched Mughal/Maratha/Sikh period: {pid}")

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Total Mughal/Maratha/Sikh periods enriched: {count}")
