# scripts/gen_mains_medieval.py
import json

def get_medieval_mains():
    items = [
        {
            "id": "mains_med_001", "periodId": "early-medieval-period", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Satish Chandra, Ch. 1; Upinder Singh",
            "question": "Examine the political and cultural consequences of the Arab conquest of Sindh under Muhammad bin Qasim in 712 CE.",
            "framework": {
                "intro": "The Arab conquest of Sindh in 712 CE under Muhammad bin Qasim established the earliest Islamic political presence in the subcontinent, described by Stanley Lane-Poole as 'an episode in the history of India and of Islam, a triumph without results', though modern scholarship highlights its profound cultural transmission.",
                "body": [
                    {"heading": "Pragmatic Policy of Toleration: The Brahmanabad Settlement", "points": [
                        "Arabs recognized Hindus and Buddhists as 'Zimmis' (protected subjects), allowing them to practice faith and retain temples upon payment of Jizya.",
                        "Enlisted local Brahmanas into administrative bureaucracy and revenue collection."
                    ]},
                    {"heading": "Transmission of Indian Science to the Arab World", "points": [
                        "Baghdad's Abbasid Caliphate (Bayt al-Hikma / House of Wisdom) actively patronized translations of Sanskrit treatises.",
                        "Aryabhata's and Brahmagupta's works ('Brahmasphutasiddhanta') were translated into Arabic by Al-Fazari as 'Sindhind', transmitting the Hindu numeral system (zero, base-10 decimal) to the Arabs, who spread it to Europe as 'Arabic numerals' (Hindsa).",
                        "Charaka Samhita and Sushruta Samhita were translated into Arabic, influencing pioneer physicians like Al-Razi and Ibn Sina (Avicenna)."
                    ]},
                    {"heading": "Geopolitical Containment", "points": [
                        "Arab advance into mainland India was decisively checked by the Gurjara-Pratiharas (Nagabhata I) and Chalukyas of Navsari (Pulakeshin Avanijanashraya)."
                    ]}
                ],
                "diagramMapIdea": "Flowchart: Sindh conquest -> Translation of Sanskrit mathematical/medical texts -> Baghdad House of Wisdom -> Transmission to Renaissance Europe.",
                "conclusion": "While politically localized to the Indus delta, the Arab conquest of Sindh acted as a vital intellectual bridge transmitting ancient Indian science, mathematics, and philosophy to the Mediterranean world."
            }
        },
        {
            "id": "mains_med_002", "periodId": "delhi-sultanate", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2017 GS-1", "bookRef": "Satish Chandra, Ch. 3; NCERT Class 7 Our Pasts II",
            "question": "Analyze the structural, military, and socio-political factors that led to the defeat of Rajput states against the Turkish invaders at the Second Battle of Tarain (1192).",
            "framework": {
                "intro": "The Second Battle of Tarain (1192 CE), where Muhammad Ghori decisively defeated Prithviraj Chauhan III, is a monumental turning point in Indian history that laid the foundations of Turkish Sultanate rule in northern India.",
                "body": [
                    {"heading": "Military Tactics and Mobility", "points": [
                        "Turkish Advantage: Relied on highly mobile mounted Central Asian horse archers equipped with iron stirrups and composite recurve bows capable of firing at a galloping charge.",
                        "Rajput Weakness: Over-reliance on slow, cumbersome war elephants and heavy infantry. War elephants were easily panicked by flaming arrows, trampling their own ranks.",
                        "Ghori divided his force into 4 divisions of 10,000 horse archers using feigned retreat ('Tulughma' tactics) to lure Rajputs out of formation before crushing them with fresh cavalry reserves."
                    ]},
                    {"heading": "Socio-Religious Rigidity and Caste Exclusivism", "points": [
                        "The Varna-Jati system restricted warfare exclusively to the Kshatriya sub-castes; vast peasant and artisan populations remained passive bystanders without civic or martial stake in defending the state.",
                        "Turkish armies, driven by egalitarian social mobility within the military slave corps (Mamluks), mobilized troops purely on martial competence regardless of social origin."
                    ]},
                    {"heading": "Political Fragmentation and Clan Rivalries", "points": [
                        "Rajput polity was decentralized into fractious clan-based lineages driven by personal vendettas (e.g., bitter rivalry between Prithviraj Chauhan and Jaichandra of Kannauj).",
                        "Absence of a unified subcontinental command or shared strategic defense doctrine along the northwestern mountain passes."
                    ]}
                ],
                "diagramMapIdea": "Battlefield formation diagram of Tarain II: Central Rajput elephant/infantry phalanx encircled by four mobile squadrons of Turkish mounted archers.",
                "conclusion": "The Turkish victory was not merely a military triumph, but the victory of superior mobile cavalry tactics, strategic deception, and social cohesion over clan-bound feudal chivalry."
            }
        },
        {
            "id": "mains_med_003", "periodId": "delhi-sultanate", "marks": 15, "wordLimit": 250, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Satish Chandra, Ch. 4; NCERT Class 11",
            "question": "Shamsuddin Iltutmish is regarded as the true consolidator of the Delhi Sultanate. Evaluate his administrative, diplomatic, and numismatic measures.",
            "framework": {
                "intro": "While Qutb-ud-din Aibak founded the Mamluk dynasty in 1206, Shamsuddin Iltutmish (1210-1236 CE) rescued the fledgling Sultanate from imminent destruction, securing imperial legitimacy and creating institutional mechanisms of governance.",
                "body": [
                    {"heading": "Diplomatic Sagacity: Deflecting the Mongol Storm", "points": [
                        "In 1221, Genghis Khan pursued the fugitive Shah of Khwarizm, Jalal-ud-din Mangbarani, up to the Indus river.",
                        "Iltutmish diplomatically refused asylum to Mangbarani on climatic grounds, averting a catastrophic Mongol invasion that could have annihilated the nascent Sultanate."
                    ]},
                    {"heading": "Crushing Internal Rivals and Legal Legitimacy", "points": [
                        "Defeated powerful rival Turkish generals: Tajuddin Yaldiz at Tarain (1215) and Nasiruddin Qabacha of Multan/Sindh (1228).",
                        "Obtained an imperial deed of investiture ('Mansur') and title of 'Nasir Amir-ul-Muminin' from the Abbasid Caliph of Baghdad Al-Mustansir in 1229, legally establishing Delhi as an independent sovereign Sultanate."
                    ]},
                    {"heading": "Institutional Innovations: Turkan-i-Chahalgani and Iqta", "points": [
                        "Created the 'Corps of Forty' (Turkan-i-Chahalgani) - an elite corps of loyal Turkish military slaves to consolidate crown authority over provincial administration.",
                        "Institutionalized the 'Iqta' system: distributed revenue assignments across the empire to officers in lieu of cash salaries, linking provincial taxation to the central treasury."
                    ]},
                    {"heading": "Numismatic Standardization and Architecture", "points": [
                        "Introduced the pure silver 'Tanka' (175 grains) and copper 'Jital', standardizing Delhi Sultanate currency for centuries.",
                        "Completed the construction of the Qutub Minar and built the Gandhak ki Baoli and Hauz-i-Shamsi."
                    ]}
                ],
                "diagramMapIdea": "Four pillars of Iltutmish's consolidation: Mongol Diplomacy, Caliphal Investiture, Iqta/Chahalgani institutions, and Tanka/Jital currency.",
                "conclusion": "By securing imperial boundaries, codifying currency, institutionalizing the Iqta system, and winning caliphal recognition, Iltutmish transformed Delhi from a precarious military encampment into a durable empire."
            }
        },
        {
            "id": "mains_med_004", "periodId": "delhi-sultanate", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Satish Chandra, Ch. 4",
            "question": "Ghiyasuddin Balban's 'Theory of Kingship' was an exercise in autocracy designed to restore the majesty of the Sultanate crown. Elucidate.",
            "framework": {
                "intro": "Ascending the throne after decades of court intrigue orchestrated by the Turkish nobility, Ghiyasuddin Balban (1266-1287 CE) formulated a sacralized Theory of Kingship based on Persian monarchical traditions to restore absolute royal prestige.",
                "body": [
                    {"heading": "Divine Conception of Monarchy", "points": [
                        "Proclaimed that the Sultan was 'Niyabat-i-Khudai' (Vice-regent of God on Earth) and 'Zill-i-Ilahi' (Shadow of God).",
                        "Maintained that royal authority was divinely bestowed, placing the monarch above public accountability and peer criticism."
                    ]},
                    {"heading": "Persian Court Etiquette and Aristocratic Exclusivism", "points": [
                        "Claimed descent from the mythical Turanian hero Afrasiyab to establish aristocratic purity.",
                        "Introduced rigorous Persian court ceremonial: 'Sijda' (prostration) and 'Paibos' (kissing the Sultan's feet), compelling proud Turkish nobles to bow before the throne.",
                        "Introduced the Persian New Year festival 'Nauroz' celebrated with lavish pomp."
                    ]},
                    {"heading": "Suppression of the 'Corps of Forty' and Blood & Iron Policy", "points": [
                        "Ruthlessly eliminated the rebellious oligarchs of the Chahalgani through poisoning, executions, and demotions.",
                        "Adopted the 'Policy of Blood and Iron' to pacify highway bandits (Mewatis) in the Delhi suburbs and crushed the rebellion of Tughril Khan in Bengal."
                    ]}
                ],
                "diagramMapIdea": "Concept triangle: Balban's Kingship (Divine Right: Niyabat-i-Khudai) + Court Subjugation (Sijda/Paibos) + Coercive Force (Blood & Iron).",
                "conclusion": "Balban's autocratic theorization centralized sovereign authority in the crown, creating the institutional stability necessary for Alauddin Khalji's subsequent imperial expansion."
            }
        },
        {
            "id": "mains_med_005", "periodId": "delhi-sultanate", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2014 GS-1", "bookRef": "Satish Chandra, Ch. 5; NCERT Class 7",
            "question": "Alauddin Khalji's market control regulations were driven primarily by military imperatives rather than benevolent consumer welfare. Critically examine with reference to Barani's Tarikh-i-Firoz Shahi.",
            "framework": {
                "intro": "Alauddin Khalji (1296-1316 CE) instituted South Asia's most rigorous price-control and market regulation mechanism. Ziauddin Barani in 'Tarikh-i-Firoz Shahi' and modern historians like Satish Chandra emphasize that these measures were military-fiscal strategies to sustain a colossal standing army against Mongol incursions.",
                "body": [
                    {"heading": "The Strategic Military Imperative", "points": [
                        "Mongol armies repeatedly besieged Delhi (Qutlugh Khwaja in 1299, Targhi in 1303).",
                        "To counter this existential threat and finance southern conquests, Alauddin needed a massive standing army (over 300,000 cavalry).",
                        "State treasury could not afford exorbitant salaries; Alauddin fixed soldiers' salaries at 234 tankas annually. To keep this salary viable, he strictly lowered and froze the retail cost of all basic consumer commodities."
                    ]},
                    {"heading": "Institutional Machinery of Market Control", "points": [
                        "Established separate specialized markets in Delhi: 1. Mandi (grain market); 2. Sarai-i-Adl (cloth, sugar, dried fruits, oil); 3. Horse, slave, and cattle market; 4. Miscellaneous general bazaar.",
                        "Appointed the 'Shahna-i-Mandi' (market superintendent) and 'Diwan-i-Riyasat' (commerce minister) assisted by undercover child spies ('Munhiyans') to verify weights and prices.",
                        "Strict punitive enforcement: Barani records that if a shopkeeper gave short weight, an equal weight of flesh was cut from his body."
                    ]},
                    {"heading": "Agrarian Procurement and State Granaries", "points": [
                        "Compulsory land revenue collected in grain in the Doab; cultivators were forced to sell surplus grain to licensed state merchants at fixed official prices directly at threshing floors.",
                        "Maintained massive imperial granaries in Delhi that disbursed rationed grain during droughts, preventing hoarding and speculative price bubbles."
                    ]},
                    {"heading": "Assessment: Beneficiaries and Limitations", "points": [
                        "Barani explicitly notes that cheap prices benefitted the Delhi army, court nobility, and citizens, but was achieved by squeezing peasant farmers who had to sell produce at non-negotiable state prices.",
                        "The entire artificial pricing edifice collapsed immediately after Alauddin's death, proving its dependence on brute state coercion."
                    ]}
                ],
                "diagramMapIdea": "Flowchart: Mongol Threat -> Need for Standing Army -> Fixed Low Soldier Pay -> Strict Price Controls -> Agrarian Surplus Squeezing.",
                "conclusion": "Alauddin's market control was an ingenious, authoritarian war-economy measure that successfully secured India against Mongol conquest, albeit at heavy economic cost to the rural peasantry."
            }
        },
        {
            "id": "mains_med_006", "periodId": "delhi-sultanate", "marks": 15, "wordLimit": 250, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Satish Chandra, Ch. 6; NCERT Themes Theme 5",
            "question": "Muhammad bin Tughlaq was a visionary theorist whose grand administrative experiments failed due to flawed execution and popular alienation. Discuss with reference to his major projects.",
            "framework": {
                "intro": "Muhammad bin Tughlaq (1325-1351 CE), described by contemporary chroniclers as a 'mixture of opposites', was intellectually the most learned Sultan of Delhi. However, his visionary projects failed catastrophically due to administrative impetuosity and disconnection from material realities.",
                "body": [
                    {"heading": "Transfer of Capital to Daulatabad (1327)", "points": [
                        "Rationale: Strategic desire for a centrally located capital in the Deccan (Devagiri renamed Daulatabad) to govern both North and South India, while insulating the court from Mongol raids in Delhi.",
                        "Flawed Execution: Ordered a forced mass migration of Delhi's elite, scholars, and populace over 1500 km during peak summer, causing catastrophic mortality.",
                        "Realized the impossibility of controlling North India from the south, ordering an equally traumatic march back to Delhi two years later."
                    ]},
                    {"heading": "Introduction of Token Currency (1329-1330)", "points": [
                        "Rationale: Inspired by Kublai Khan's paper currency in China and Ghazan Khan's experiment in Persia; aimed to overcome global silver shortages and finance imperial expansion.",
                        "Flawed Execution: Issued bronze and copper coins with parity to gold/silver tankas, but failed to make minting a state monopoly.",
                        "Barani remarked: 'Every Hindu house became a mint.' Forged coins flooded markets; foreign merchants refused the token coins. The Sultan was forced to redeem all tokens with genuine royal silver, emptying the exchequer."
                    ]},
                    {"heading": "Agrarian Reforms: Diwan-i-Kohi and Agricultural Credit", "points": [
                        "Visionary Concept: Established a dedicated ministry of agriculture ('Diwan-i-Amir-i-Kohi') to bring barren land under cultivation, rotate crops, and disbursed 'Sondhar' (Taqavi loans) to peasants.",
                        "Failure: Corrupt officials embezzled funds; uncultivable rocky soils were selected, yielding negligible results amidst a severe Doab famine."
                    ]},
                    {"heading": "Overambitious Military Expeditions", "points": [
                        "Raised an enormous army for the Khurasan expedition, paying an entire year's advance salary before abandoning the campaign due to diplomatic shifts.",
                        "Qarachil expedition into the Kumaon Himalayas resulted in military slaughter caused by mountain terrain and torrential monsoons."
                    ]}
                ],
                "diagramMapIdea": "Failure analysis matrix: Project name, Visionary Rationale, Administrative Flaw, and Ultimate Consequence.",
                "conclusion": "Muhammad bin Tughlaq possessed ideas centuries ahead of his contemporaries, but his autocratic impatience and failure to gauge institutional capabilities doomed his visionary statecraft to tragic futility."
            }
        },
        {
            "id": "mains_med_007", "periodId": "delhi-sultanate", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Satish Chandra, Ch. 6",
            "question": "Examine the public works, irrigation canals, and welfare institutions of Firoz Shah Tughlaq. How far was his reign compromised by religious orthodoxy?",
            "framework": {
                "intro": "Firoz Shah Tughlaq (1351-1388 CE) shifted imperial policy from military conquest to domestic administrative consolidation, renowned for extensive canal building and humanitarian welfare institutions, yet constrained by religious appeasement of the Ulema.",
                "body": [
                    {"heading": "Canal Engineering and Urban Public Works", "points": [
                        "Built northern India's most extensive canal irrigation network, connecting the Yamuna and Sutlej rivers to irrigate the arid Hisar-Firoza region.",
                        "Levied a 10% irrigation cess ('Haqq-i-Sharb') with Ulema consent, boosting wheat and sugarcane yields and state grain revenues.",
                        "Founded over 300 new towns: Firozabad, Jaunpur, Hisar, Fatehabad; repaired ancient monuments including the Qutub Minar and Hauz Khas."
                    ]},
                    {"heading": "Welfare Institutions and Slave Bureau", "points": [
                        "Established 'Dar-ul-Shifa' (free charitable hospitals with state-paid physicians).",
                        "Created 'Diwan-i-Khairat' (charity bureau providing marriage funds for poor girls) and 'Diwan-i-Istihqaq' (pension bureau).",
                        "Created 'Diwan-i-Bandagan' maintaining 180,000 royal slaves, who were trained in artisanal crafts but later became an unruly praetorian faction."
                    ]},
                    {"heading": "Orthodox Compromise and Political Weakening", "points": [
                        "To appease the Ulema, he imposed Jizya on Brahmanas as a separate tax, destroyed Hindu temples at Puri and Nagarkot, and banned women from visiting Sufi shrines.",
                        "Made hereditary the Iqta assignments and army recruitment, fatally degrading the military efficiency of the Sultanate."
                    ]}
                ],
                "diagramMapIdea": "Balance scale: Public Works & Welfare (Canals, Hospitals, Towns) vs Feudal/Orthodox Concessions (Hereditary Iqtas, Jizya, Inefficient Army).",
                "conclusion": "While Firoz Shah's civic infrastructure and canal works provided temporary agrarian prosperity, his feudal concessions and military compromises paved the way for Timur's catastrophic sack of Delhi in 1398."
            }
        },
        {
            "id": "mains_med_008", "periodId": "delhi-sultanate", "marks": 15, "wordLimit": 250, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "Satish Chandra, Ch. 5; Irfan Habib",
            "question": "Trace the evolution of the Iqta system under the Delhi Sultanate. How did it differ conceptually and operationally from the Mughal Jagirdari system?",
            "framework": {
                "intro": "The Iqta system was the fiscal-administrative backbone of the Delhi Sultanate, originating in Islamic West Asia and adapted by Turkish Sultans to mobilize agrarian revenues for military maintenance, serving as the conceptual ancestor of the Mughal Jagirdari system.",
                "body": [
                    {"heading": "Evolution of the Iqta under Delhi Sultans", "points": [
                        "Under Iltutmish: Iqtas were territorial revenue assignments granted to Turkish commanders ('Muqtis' or 'Walisi') in lieu of cash pay; expected to maintain law and order and lead assigned troops to imperial campaigns.",
                        "Revenue Remittance ('Fawazil'): Muqtis deducted their salary and troop maintenance costs, remitting the surplus balance ('Fawazil') to the central Diwan-i-Wizarat.",
                        "Alauddin Khalji and Ghiyasuddin Tughlaq strictly audited Fawazil through central accountants ('Amils') to prevent embezzlement.",
                        "Decentralization under Firoz Shah Tughlaq: Made Iqtas hereditary, transforming administrative revenue assignments into de facto private feudal estates."
                    ]},
                    {"heading": "Comparative Analysis: Iqta vs Mughal Jagirdari", "points": [
                        "1. Nature of Authority: Iqta holders (Muqtis) held both revenue collection and executive law-and-order/police powers in their territory. In contrast, Mughal Jagirdars held ONLY revenue collection rights; civil administration and police were held separately by imperial Faujdars.",
                        "2. Transferability and Tenure: Iqtas under strong Sultans were periodically transferred, but under weak rulers became hereditary. Mughal Jagirs were strictly transferable every 3-4 years to prevent local territorial entrenchment.",
                        "3. Assessment and Measurement: Iqta assignments were roughly estimated tributes without precise land measurement. Mughal Jagirs were meticulously calculated through the 'Zabti' system based on actual measured yield ('Jama') and realized collection ('Hasil').",
                        "4. Subordination: Jagirdars were integrated into the decimal hierarchy of the Mansabdari system (Zat and Sawar ranks), whereas Muqtis functioned with greater personal feudal discretion."
                    ]}
                ],
                "diagramMapIdea": "Comparative matrix: Iqta vs Jagir across Authority (Revenue+Military vs Pure Revenue), Transferability, Measurement precision, and Rank integration.",
                "conclusion": "While the Iqta was an early feudal-military mechanism for tax extraction, the Mughal Jagirdari evolved into a far more rationalized, bureaucratic instrument of imperial statecraft."
            }
        },
        {
            "id": "mains_med_009", "periodId": "bhakti-sufi-movements", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2013 GS-1", "bookRef": "NCERT Themes Theme 6; Satish Chandra, Ch. 12",
            "question": "The Bhakti and Sufi movements of medieval India served as powerful catalysts of cultural syncretism and social reform. Critically evaluate their impact on language, society, and religious harmony.",
            "framework": {
                "intro": "The 14th to 17th centuries witnessed a widespread socio-religious churning in medieval India through the convergence of the Bhakti movement and Sufi Silsilas, bridging sectarian divides through the shared language of divine love and human fraternity.",
                "body": [
                    {"heading": "Social Subversion of Caste and Ritual Orthodoxy", "points": [
                        "Nirguna Bhakti saints (Kabir, Ravidas, Guru Nanak, Dadu Dayal) mounted a devastating critique against untouchability, Brahminical supremacy, and empty rituals.",
                        "Kabir's caustic couplets (Dohas) ridiculed external symbols: 'Pahan puje hari mile to main pujun pahar' (If worshiping a stone yields God, I will worship a mountain).",
                        "The Sufi Khanqahs (hospices) provided an egalitarian sanctuary where prince and pauper, Hindu and Muslim, dined together in common community kitchens ('Langar')."
                    ]},
                    {"heading": "Flourishing of Regional Vernacular Literatures", "points": [
                        "Saints broke the monopoly of Sanskrit and Arabic/Persian, composing directly in the languages of the common people.",
                        "Hindi (Kabir, Surdas, Tulsidas' Ramcharitmanas); Punjabi (Guru Nanak's Japji Sahib); Bengali (Chaitanya's Gaudiya padavali); Marathi (Jnaneshwar, Tukaram's Abhangas); Assamese (Sankaradeva's Borgeets).",
                        "Amir Khusrau pioneered 'Hindavi', blending Persian vocabulary with Braj Bhasha idioms, giving birth to early Urdu."
                    ]},
                    {"heading": "Philosophical and Cultural Syncretism", "points": [
                        "Sufi doctrine of 'Wahdat al-Wujud' (Unity of Being) resonated with Advaita Vedanta non-dualism, positing that all creation is a reflection of the Divine.",
                        "Mutual adoption of yogic practices: Chishti Sufis practiced breath-control ('Pranayama'), leading orthodox clerics to call them 'Siddhas'.",
                        "Synthesis in Indian Classical Music: Development of Qawwali, Khayal, and devotional Dhrupad; Sufi shrines (Hazrat Nizamuddin, Ajmer Dargah) became melting pots of shared cultural pilgrimage ('Ziyarat')."
                    ]}
                ],
                "diagramMapIdea": "Syncretic Venn diagram: Bhakti (Devotion, Anti-caste, Vernacular) INTERSECTING Sufi (Love, Wahdat al-Wujud, Langar) = Ganga-Jamuni Composite Culture.",
                "conclusion": "Bhakti and Sufi saints constructed the enduring foundation of India's composite 'Ganga-Jamuni' culture, proving that spiritual realization is rooted in universal human empathy rather than institutional dogma."
            }
        },
        {
            "id": "mains_med_010", "periodId": "bhakti-sufi-movements", "marks": 10, "wordLimit": 150, "isPyq": False,
            "yearSource": "UPSC CSE Standard Practice", "bookRef": "NCERT Themes Theme 6; Satish Chandra",
            "question": "Examine the revolutionary socio-religious principles of Basavanna's Virashaiva (Lingayat) movement in 12th-century Karnataka.",
            "framework": {
                "intro": "Initiated by Basavanna (1106-1167 CE), Allama Prabhu, and Akka Mahadevi in Kalyani Karnataka, the Virashaiva or Lingayat movement was a radical socio-religious revolt against Brahmanical orthodoxy, ritualism, and caste hierarchy.",
                "body": [
                    {"heading": "Rejection of Caste and Vedic Authority", "points": [
                        "Radically rejected the Varna hierarchy, ritual pollution, and Brahminical priestly monopoly over salvation.",
                        "Advocated that all human beings wearing the 'Ishtalinga' (personal miniature Shiva-linga worn around the neck) are equal before Shiva.",
                        "Encouraged inter-caste marriages; celebrated the historic marriage between the daughter of a Brahmin and son of an untouchable cobbler."
                    ]},
                    {"heading": "The Anubhava Mantapa: Democratic Spiritual Parliament", "points": [
                        "Founded the 'Anubhava Mantapa' (Hall of Spiritual Experience) at Basavakalyan—the world's first open socio-spiritual academy where men and women of all castes openly debated philosophy, ethics, and theology.",
                        "Composed profound, pithy free-verse poems called 'Vachanas' in vernacular Kannada."
                    ]},
                    {"heading": "Dignity of Labour ('Kayakave Kailasa') and Women's Emancipation", "points": [
                        "Propounded 'Kayakave Kailasa' (Work is Worship): physical labour is sacred, and every individual must earn their livelihood honestly without parasitism.",
                        "Championed gender equality: opposed child marriage, permitted widow remarriage, rejected menstrual taboos, and nurtured towering female mystic poets like Akka Mahadevi."
                    ]}
                ],
                "diagramMapIdea": "Triad of Virashaiva reform: Social Equality (Anti-caste, Ishtalinga) + Dignity of Labour (Kayakave Kailasa) + Gender Justice (Anubhava Mantapa).",
                "conclusion": "Basavanna's movement was centuries ahead of its time, pioneering subcontinental concepts of democratic deliberative assembly, gender empowerment, and the ethical sanctity of manual labour."
            }
        }
    ]

    # Additional 25 Medieval Mains questions to make exactly 35
    med_25 = [
        ("mains_med_011", "vijayanagara-empire", 15, 250, True, "UPSC CSE 2016 GS-1", "Satish Chandra, Ch. 8; NCERT Themes Theme 7",
         "The Nayankara system was the central pillar of Vijayanagara military feudalism, yet contained the seeds of imperial disintegration. Critically analyze.",
         "Founded in 1336 by Harihara and Bukka, the Vijayanagara Empire relied on the Nayankara system for provincial defense and agrarian colonization.",
         [
             ("Nature and Structure of the Nayankara System", ["The king granted revenue territories ('Amara Nayankara') to military chieftains known as 'Amaranayakas'.", "In return, Nayakas maintained a fixed quota of horses, elephants, and infantry ready for imperial military service, and paid an annual monetary tribute to the royal exchequer.", "Nayakas enjoyed sweeping internal judicial and revenue rights over their domains."]),
             ("Role in Agrarian Colonization and Urban Expansion", ["Nayakas actively cleared scrublands, constructed massive irrigation tanks, and founded new market towns ('Pettai').", "Acted as munificent patrons of temples (erecting colossal entrance towers or 'Raya Gopurams' and Kalyana Mandapas), fostering regional craft guilds."]),
             ("Structural Flaws Leading to Disintegration", ["Unlike Mughal Jagirs, Amara tenures were rarely transferred, enabling Nayakas to sink deep hereditary roots and establish regional warrior dynasties (e.g., Nayaks of Madurai, Tanjore, and Gingee).", "Whenever central authority weakened (as after the Battle of Talikota in 1565), the Nayakas withheld tribute, formed regional confederacies, and accelerated the collapse of the imperial center."])
         ],
         "Flowchart: Nayankara System -> Military Mobilization & Agrarian Growth -> Hereditary Entrenchment -> Rebellions post-1565 -> Imperial Disintegration.",
         "The Nayankara system was a brilliant military adaptation that preserved southern Hindu sovereignty against northern sultanates, but its failure to prevent hereditary autonomy ultimately fragmented the empire."),

        ("mains_med_012", "vijayanagara-empire", 15, 250, True, "UPSC CSE 2020 GS-1", "Nitin Singhania, Ch. 2; NCERT Themes Theme 7",
         "Hampi's urban architecture seamlessly integrated natural granite topography, religious monuments, and royal administrative spaces. Discuss with reference to the Sacred and Royal Centres.",
         "Hampi, the capital of the Vijayanagara Empire on the banks of the Tungabhadra River, represents a masterclass in hydraulic engineering, defensive natural topography, and majestic stone architecture.",
         [
             ("Integration with Natural Rocky Landscape", ["Surrounded by rugged granite boulder hills that served as impregnable natural ramparts.", "Foreign travellers (Domingo Paes, Abdur Razzaq) marveled at seven concentric lines of fortified walls enclosing not just palaces, but also agricultural fields and irrigation canals."]),
             ("The Sacred Centre along the Tungabhadra", ["Clustered along the riverbanks, housing monumental Dravidian temples.", "Virupaksha Temple: Oldest sacred shrine with an elaborate pillared hall and 50-meter gateway tower (Raya Gopuram) added by Krishnadevaraya.", "Vitthala Temple: Pinnacle of Vijayanagara architectural exuberance, featuring the iconic monolithic Stone Chariot (Garuda shrine) and 56 musical pillars that produce melodic resonance."]),
             ("The Royal Centre and Secular Architecture", ["Enclosed complex housing administrative and elite living quarters.", "Mahanavami Dibba: Massive 3-tiered stone platform decorated with relief sculptures of war elephants and dancers, where monarchs celebrated the 10-day Dasara/Navaratri festival and accepted Nayaka tributes.", "Lotus Mahal and Queen's Bath: Fusion of Islamic arches/domes with Hindu brackets and pilasters, reflecting syncretic court culture."]),
             ("Sophisticated Hydraulic Engineering", ["Kamalapuram tank, Hiriya canal, and elevated stone aqueducts delivering fresh river water across the Royal Centre."])
         ],
         "Topographical schematic of Hampi: Tungabhadra River -> Sacred Centre (Virupaksha, Vitthala) -> Irrigated Agricultural Valley -> Royal Centre (Mahanavami Dibba, Lotus Mahal).",
         "Hampi represents an incomparable urban synthesis where imperial authority, sacred devotion, and rugged peninsular geology coalesced into an eternal city."),

        ("mains_med_013", "vijayanagara-empire", 10, 150, False, "Standard Practice", "Satish Chandra, Ch. 8",
         "Assess the military, diplomatic, and literary achievements of Emperor Krishna Deva Raya (1509-1529 CE).",
         "Belonging to the Tuluva dynasty, Krishna Deva Raya was the greatest monarch of Vijayanagara, under whom the empire attained its cultural and geopolitical zenith.",
         [
             ("Military Dominance and Southern Pacification", ["Crushed the Sultan of Bijapur Ismail Adil Shah, recovering the strategic Raichur Doab (1520).", "Defeated the Gajapatis of Odisha, capturing the hill forts of Udayagiri and Kondavidu; married princess Jaganmohini and treated the defeated adversary with chivalry.", "Pacified the rebellious Ummatur chieftain in the Cauvery basin."]),
             ("Astute Portuguese Diplomacy", ["Maintained cordial diplomatic and commercial ties with Portuguese governor Afonso de Albuquerque.", "Monopolized the import of high-breed Persian and Arabian war horses via Goa, depriving Deccan Sultanates of quality cavalry."]),
             ("Literary Zenith and Patronage", ["Accomplished polymath: composed the Telugu epic on statecraft 'Amuktamalyada' and the Sanskrit play 'Jambavati Kalyanam'.", "Patronized the 'Astadiggajas' (Eight Poets) in his court, foremost among them being Allasani Peddana (honoured as 'Andhra Kavita Pitamaha')."])
         ],
         "Map of Krishna Deva Raya's campaigns: Raichur Doab, Kondavidu, Udayagiri, and diplomatic route to Portuguese Goa.",
         "Krishna Deva Raya combined unmatched martial generalship with profound scholarly statesmanship, earning the enduring title of 'Abhinava Bhoja'."),

        ("mains_med_014", "vijayanagara-empire", 10, 150, False, "Standard Practice", "Satish Chandra, Ch. 8",
         "Analyze the causes and long-term geopolitical consequences of the Battle of Talikota (1565 CE).",
         "Fought on 23 January 1565 at Rakkasa-Tangadi, the Battle of Talikota was the cataclysmic conflict that shattered the military supremacy of Vijayanagara in peninsular India.",
         [
             ("Causes: Rama Raya's Arrogant Divide-and-Rule Diplomacy", ["Regent Rama Raya maintained hegemony by constantly playing one Deccan Sultanate against another in regional border disputes.", "When Vijayanagara troops ravaged Muslim territories and desecrated mosques during joint campaigns, the rival Sultanates recognized Rama Raya as a collective existential threat.", "Four Sultanates (Bijapur, Golconda, Ahmadnagar, Bidar) formed a grand anti-Vijayanagara military league (with Berar absent due to regional rivalry)."]),
             ("The Battle and Sudden Betrayal", ["Despite initial numerical superiority, Rama Raya's forces were routed when two key Muslim mercenary commanders commanding artillery corps defected on the battlefield.", "Rama Raya was captured and summarily executed on the field."]),
             ("Devastating Geopolitical Consequences", ["Hampi was systematically sacked, looted, and burned for months, reduced to desolate ruins.", "The imperial dynasty shifted to Penukonda and Chandragiri (Aravidu dynasty), losing direct control over Tamil and Kannada regions.", "Enabled Deccan Sultanates to expand southward, until they were eventually absorbed by the Mughals."])
         ],
         "Diagram: 4 Deccan Sultanates League (Bijapur, Golconda, Ahmadnagar, Bidar) vs Vijayanagara (Rama Raya) -> Catastrophic defeat at Talikota (1565).",
         "Talikota was not merely the death knell of a city, but the decisive rupture that ended unified imperial peninsular hegemony in South India."),

        ("mains_med_015", "sur-empire", 15, 250, True, "UPSC CSE 2015 GS-1", "Satish Chandra, Ch. 11",
         "Sher Shah Suri was not merely a brilliant military usurper, but an administrative genius who anticipated the structural reforms of Akbar. Critically evaluate.",
         "Ruling for barely five years (1540-1545 CE), Sher Shah Suri overthrew Humayun, established the Second Afghan Empire, and introduced pioneering administrative, agrarian, and infrastructural systems that Akbar perfected.",
         [
             ("Land Revenue Administration: Precursor to the Zabti System", ["Introduced a central schedule of crop assessment rates known as 'Ray' (Rai) based on actual land measurement using the rope jarib.", "Classified cultivable land into good, middling, and bad, assessing 1/3rd of the average yield payable in cash or kind.", "Granted 'Patta' (title deed stating tax dues) and secured 'Qabuliyat' (deed of agreement signed by the peasant), eliminating fraudulent middlemen."]),
             ("Administrative Hierarchy and Separation of Powers", ["Subdivided the empire into 47 'Sarkars' (districts) and numerous 'Parganas' (sub-districts).", "Established checks and balances in each Sarkar: Shiqdar-i-Shiqdaran (law and order/military) and Munsif-i-Munsifan (revenue assessment and civil judiciary).", "Strict enforcement of local police responsibility: village headmen (Muqaddams) were held personally liable to produce thieves or pay compensation."]),
             ("Currency Standardization and Highway Infrastructure", ["Standardized Indian coinage: introduced the pure silver 'Rupiya' (178 grains) and copper 'Dam' (380 grains) at a 1:64 ratio, which survived throughout Mughal and British rule.", "Constructed four grand highways, notably the 2500-km 'Sadak-i-Azam' (Grand Trunk Road) connecting Sonargaon (Bengal) to Attock (Peshawar).", "Built 1,700 'Sarais' (rest-houses with separate drinking water and lodgings for Hindus and Muslims) spaced every two kos, equipped with royal postal couriers ('Dak Chauki')."])
         ],
         "Flowchart connecting Sher Shah's innovations to Akbar's perfection: Ray schedule -> Ain-i-Dahsala; Rupiya -> Imperial currency; Sarkars -> Subahs; Sarais -> Trade communication.",
         "Sher Shah Suri laid the administrative, infrastructural, and agrarian tracks upon which the magnificent engine of the Mughal Empire subsequently ran."),

        ("mains_med_016", "mughal-empire", 15, 250, True, "UPSC CSE 2017 GS-1", "Satish Chandra, Ch. 13; NCERT Class 12 Themes Theme 9",
         "Akbar's Rajput policy was rooted not merely in romantic matrimonial alliances, but in cold, pragmatic imperial statecraft. Analyze its evolution and impact.",
         "Akbar's policy towards the Rajput warrior clans (c. 1562-1605 CE) was a masterstroke of political realism, transforming perennial adversaries into the most dedicated sword-arm of the Mughal Empire.",
         [
             ("Pragmatic Geopolitical Imperatives", ["Akbar recognized that no empire in North India could be stable without pacifying the martial Rajput clans dominating the flank between Agra and Gujarat/Malwa.", "A purely military conquest was counterproductive because Rajputs possessed formidable hill forts (Chittor, Ranthambore) and preferred fighting to the death (Jauhar and Saka)."]),
             ("Multi-Pronged Strategic Mechanism", ["1. Matrimonial Alliances without Humiliation: Married Harkha Bai (daughter of Raja Bharmal of Amber) in 1562; ensured Rajput queens enjoyed full freedom to practice Hindu worship within the imperial palace.", "2. Integration into High Imperial Bureaucracy: Inducted Rajput chieftains into the highest Mansabdari ranks (Raja Man Singh was given the highest mansab of 7,000, previously reserved for royal princes).", "3. Preservation of Internal Autonomy via 'Watan Jagirs': Allowed Rajput rajas to govern their ancestral homelands ('Watan') autonomously without Mughal revenue intervention, only requiring them to serve in imperial campaigns.", "4. Abolition of Discriminatory Taxes: Abolished the Pilgrim Tax (1563) and Jizya (1564)."]),
             ("Resistance and Coercion: The Case of Mewar", ["Where conciliation failed, Akbar used ruthless force, as evidenced by the siege of Chittor (1568).", "Maharana Pratap heroically resisted at Haldighati (1576), waging guerrilla warfare from the Aravallis until his death, preserving Mewar's sovereign pride."]),
             ("Long-Term Imperial Consequences", ["Secured the empire's borders from Kabul to the Deccan through elite Rajput generals (e.g., Man Singh conquered Bengal and Odisha for Akbar).", "Created a broad-based, multi-religious ruling class that decoupled imperial loyalty from Islamic sectarian identity."])
         ],
         "Strategic 4-Quadrant diagram: Matrimonial Alliances, High Mansabdari ranks, Watan Jagir autonomy, Abolition of Jizya.",
         "Akbar's Rajput policy remains an enduring textbook study in imperial integration: winning loyalty not by crushing an adversary, but by elevating them to equal partners in sovereignty."),

        ("mains_med_017", "mughal-empire", 15, 250, True, "UPSC CSE 2018 GS-1", "Satish Chandra, Ch. 13; NCERT Themes Theme 9",
         "Trace the evolution of Akbar's religious ideas from orthodox Sunnism to the universalist philosophy of 'Sulh-i-Kul' (Absolute Peace).",
         "Akbar's spiritual journey was an evolving philosophical quest driven by personal mysticism, intellectual curiosity, and the political necessity of ruling a pluralistic subcontinental empire.",
         [
             ("Phase 1 (1556-1575): Orthodox Conformity and Early Reforms", ["Initially under the influence of conservative orthodox court clerics (Sheikh Abdun Nabi and Abdullah Sultanpuri).", "However, his broad humanism manifested early in the abolition of the Pilgrim Tax (1563) and Jizya (1564), and banning the enslavement of prisoners of war."]),
             ("Phase 2 (1575-1578): The Ibadat Khana Debates", ["Constructed the 'Ibadat Khana' (House of Worship) at Fatehpur Sikri in 1575.", "Initially opened only to Sunni theological factions. Disillusioned by their venomous bickering, accusations of heresy, and narrow pedantry, Akbar opened discussions in 1578 to all faiths: Hindus (Purushottam, Devi), Jains (Hiravijaya Suri, who was honoured with the title 'Jagadguru'), Zoroastrians (Dastur Meherji Rana), Christians (Jesuits Monserrate and Aquaviva), and Charvakas."]),
             ("Phase 3 (1579): The Mahzar Decree", ["Drafted by Sheikh Mubarak, the Mahzar recognized Akbar as 'Imam-i-Adil' (Just Ruler).", "Conferred upon the Emperor the prerogative to select between conflicting interpretations of Islamic jurisprudence if the Ulema disagreed, provided it served public welfare."]),
             ("Phase 4 (1582 onwards): Sulh-i-Kul and Tauhid-i-Ilahi", ["Synthesized the grand ethical doctrine of 'Sulh-i-Kul' (Universal Peace / Absolute Peace for All): the state maintained total religious neutrality, protecting all faiths equally without discrimination.", "Formulated 'Tauhid-i-Ilahi' (or Din-i-Ilahi) - an ethical fraternity of royal disciples based on moral virtues: vegetarianism, sun worship, charity, and rational self-restraint. It was never an enforced state religion."])
         ],
         "Evolutionary timeline: Phase 1: Orthodoxy (1556) -> Phase 2: Ibadat Khana multi-faith debates (1575-78) -> Phase 3: Mahzar Decree (1579) -> Phase 4: Sulh-i-Kul (1582).",
         "Akbar's Sulh-i-Kul anticipated modern constitutional secularism, establishing that an emperor's supreme religious duty is to act as an impartial father to all subjects regardless of creed."),

        ("mains_med_018", "mughal-empire", 15, 250, True, "UPSC CSE 2019 GS-1", "Satish Chandra, Ch. 13; Irfan Habib",
         "The Mansabdari system was the steel frame of the Mughal Empire. Explain its structural mechanics, including the Zat and Sawar ranks, and discuss how it was financed.",
         "Institutionalized by Akbar in 1571, the Mansabdari system was an integrated military-bureaucratic hierarchy that fused all civil and military officers into a single imperial service.",
         [
             ("The Dual Rank Structure: Zat and Sawar", ["Every imperial officer held a dual rank: 'Zat' and 'Sawar'.", "Zat Rank: Indicated personal status, imperial seniority, and determined the officer's personal salary.", "Sawar Rank: Indicated the exact number of cavalrymen and horses the officer was obligated to maintain for imperial service.", "Rules of Precedence: The Sawar rank could never exceed the Zat rank; based on their ratio, officers were graded into first, second, or third class."]),
             ("The Dagh and Chehra Regulations", ["To curb corruption where nobles presented ghost soldiers during inspections, Akbar revived Alauddin Khalji's regulations: 'Dagh' (imperial imperial branding of war horses) and 'Chehra' (detailed descriptive roll of each cavalryman).", "Dah-bisti rule: Required 20 horses for every 10 troopers to maintain military rotation and mobility."]),
             ("Financing the Mansabdars: Naqdi vs Jagirdari", ["Naqdi: Officers paid cash salaries directly from the imperial exchequer.", "Jagirdar: Officers assigned revenue collection rights over a designated territory ('Jagir') whose estimated revenue yield ('Jama') equalled their salary entitlement. Mansabdars held NO proprietary rights over the land or peasants."]),
             ("Later Innovations under Jahangir and Shah Jahan", ["Jahangir introduced 'Du-aspa Sih-aspa' (allowing a noble to maintain double troops without increasing his Zat rank).", "Shah Jahan introduced the 'Month-scale' system (dividing jagir pay into 8-month, 6-month, or 4-month valuations) to manage growing fiscal deficits."])
         ],
         "Structural hierarchy diagram: Mansabdar -> Zat (Personal status/pay) + Sawar (Military obligation) -> Audited via Dagh/Chehra -> Paid via Naqd or Jagir.",
         "By subordinating feudal chieftains into a uniform meritocratic hierarchy, the Mansabdari system provided the administrative glue that sustained the vast Mughal Empire."),

        ("mains_med_019", "mughal-empire", 15, 250, False, "Standard Practice", "Satish Chandra, Ch. 13; Irfan Habib",
         "Raja Todar Mal's 'Ain-i-Dahsala' represented the zenith of agrarian revenue assessment in medieval India. Detail its operational principles.",
         "Introduced in 1580 by Akbar's finance minister Raja Todar Mal, the 'Ain-i-Dahsala' (or Zabti system) replaced arbitrary revenue estimations with empirical, scientific land taxation.",
         [
             ("Calculation of Average Yield and Prices over 10 Years", ["The state recorded the actual agricultural yield and average bazaar market prices for every single crop across the preceding 10 years (1570 to 1580).", "One-third (1/3rd) of the average 10-year yield was fixed as the state's permanent share, converted into cash rates called 'Dasturs' for different regional circles."]),
             ("Scientific Land Measurement: The Bamboo Jarib", ["Abolished the old hemp rope jarib (which expanded when wet and contracted when dry).", "Introduced the 'Bamboo Jarib' joined with iron rings, providing invariant, precise geometric land measurement in 'Bighas'."]),
             ("Four-Fold Land Classification based on Fertility", ["1. Polaj: Land cultivated continuously every year without fallow; paid full tax.", "2. Parauti: Land left fallow for a year or two to recover organic fertility; paid tax only when cultivated.", "3. Chachar: Land uncultivated for 3 to 4 years; assessed at progressive concession rates.", "4. Banjar: Barren wasteland uncultivated for 5 or more years; given long tax holidays to induce reclamation."]),
             ("Peasant-Centric Safeguards", ["Peasants were provided with state loans ('Taqavi') during droughts and flood remissions.", "Village revenue officers: Amil (collector), Bitikchi (accountant), and Potdar (treasurer), supervised by the provincial Diwan."])
         ],
         "Flowchart of Dahsala assessment: Land Measurement (Bamboo Jarib) -> 4-Fold Classification (Polaj, Parauti, Chachar, Banjar) -> 10-year Average Yield/Price -> Fixed Cash Dastur.",
         "The Dahsala system provided predictable agrarian revenues for the Mughal exchequer while protecting peasant cultivators from arbitrary extortion, forming the economic bedrock of Akbar's empire."),

        ("mains_med_020", "mughal-empire", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 3; NCERT Themes Theme 9",
         "Trace the development of Mughal miniature painting under Akbar and Jahangir. How did Jahangir shift the aesthetic focus from manuscript illustration to individual portraiture?",
         "Mughal painting originated under Humayun with Persian masters Mir Sayyid Ali and Abdus Samad, developing into a vibrant indigenous imperial art form under Akbar and Jahangir.",
         [
             ("Akbar: Dynamic Manuscript Illustration and Crowded Narrative", ["Established the imperial studio ('Tasvir Khana') employing hundreds of indigenous Hindu and Muslim artists (Daswant, Basawan, Kesu Das).", "Focused on illustrating epic literary and historical manuscripts: Hamzanama (painted on cloth), Tutinama, Razmnama (Mahabharata in Persian), and Akbarnama.", "Characteristics: Dynamic crowd compositions, continuous narrative action, vivid three-dimensional movement, and brilliant multi-coloured pigments."]),
             ("Jahangir: Refined Portraiture, Nature Studies, and Western Realism", ["A passionate connoisseur who claimed he could identify the artist of any brushstroke in a composite painting.", "Shifted away from mass narrative manuscript illustration to exquisite individual portraits, intimate court durbars, and acute scientific studies of flora and fauna.", "Master artists: Ustad Mansur (celebrated for natural history paintings: Siberian Crane, Dodo, Bengal Florican); Bishandas (master of royal psychological portraiture); and Abul Hasan (allegorical paintings of Jahangir embracing Shah Abbas).", "Incorporated European artistic conventions: halo around the emperor's head (divine kingship), cherubs, and chiaroscuro (shading to create depth)."])
         ],
         "Comparative table: Akbar's painting (Collective atelier, epic narratives, kinetic energy) vs Jahangir's painting (Individual connoisseurship, portraits, naturalism, European halo).",
         "Under Akbar, Mughal painting captured the bustling kinetic energy of empire; under Jahangir, it attained psychological intimacy, naturalist precision, and supreme aesthetic refinement."),

        ("mains_med_021", "mughal-empire", 15, 250, True, "UPSC CSE 2016 GS-1", "Nitin Singhania, Ch. 2; Satish Chandra",
         "Shah Jahan's reign represents the classical climax of Mughal architecture. Discuss the transition from red sandstone monumentalism to pure white marble symmetry.",
         "While Akbar's architecture was characterized by robust red sandstone experiments and Indo-Persian syncretism (Fatehpur Sikri), Shah Jahan (1628-1658 CE) elevated Mughal architecture to its classical zenith of delicate marble symmetry, lyricism, and decorative refinement.",
         [
             ("Shift in Building Material: From Red Sandstone to White Marble", ["Shah Jahan replaced sandstone with pristine white Makrana marble quarried in Rajasthan.", "Where Akbar and Jahangir built with red sandstone, Shah Jahan demolished earlier sandstone pavilions in Agra and Lahore forts, replacing them with luminous marble structures (Diwan-i-Khas, Moti Masjid)."]),
             ("Key Stylistic Innovations", ["1. Perfect Mathematical Symmetry: Bilateral balance organized around central axes and reflecting water pools.", "2. Pietra Dura (Parchin Kari): Inlaying polished semi-precious gems (lapis lazuli, jade, carnelian, jasper) into white marble in delicate floral arabesques.", "3. Bulbous Double Domes: Swelling Persian bulbous domes crowned by inverted lotus finials.", "4. Foliated Cusped Arches: Multifoiled arches with nine cusps replacing plain pointed arches.", "5. Charbagh Garden Landscape: Formal quadripartite gardens symbolizing paradise ('Jannat')."]),
             ("The Taj Mahal: The Climax of Global Architectural Lyricism", ["Constructed as a mausoleum for Mumtaz Mahal on the Yamuna banks at Agra.", "Architect: Ustad Ahmad Lahori. Perfect geometric integration: height of dome equals width of facade; four freestanding minarets tilting slightly outwards to protect the tomb from earthquakes.", "Evokes ethereal lightness, shifting hues with sunlight and moonlight."]),
             ("Urban Imperial Monumentalism: Shahjahanabad", ["Founded a new imperial capital in Delhi: Shahjahanabad.", "Constructed the Red Fort (Lal Qila) housing the Diwan-i-Am, Diwan-i-Khas (bearing the inscription: 'If there is paradise on earth, it is this, it is this, it is this'), and the monumental Jama Masjid."])
         ],
         "Architectural evolution diagram: Akbar's robust sandstone (Fatehpur Sikri) -> Jahangir's transitional marble (Itmad-ud-Daulah) -> Shah Jahan's sublime marble symmetry (Taj Mahal).",
         "Shah Jahan transformed Mughal architecture into frozen poetry: an imperial vision where imperial majesty, geometric precision, and eternal romance achieved absolute equilibrium."),

        ("mains_med_022", "mughal-empire", 15, 250, True, "UPSC CSE 2019 GS-1", "Satish Chandra, Ch. 16-17",
         "Aurangzeb's religious orthodoxy and political reversals alienated core pillars of the Mughal Empire. Critically analyze with reference to his Rajput, Sikh, and Deccan policies.",
         "Ascending the throne after a bloody war of succession against his liberal brother Dara Shikoh, Aurangzeb 'Alamgir' (1658-1707 CE) reversed Akbar's policy of religious conciliation, plunging the empire into exhausting protracted crises.",
         [
             ("Orthodox Religious Reversals and Alienation of Subjects", ["Puritanical measures: Banned music at court, discontinued Jharokha Darshan, abolished the Persian New Year Nauroz, and appointed 'Muhtasibs' (censors of public morals).", "Re-imposed Jizya in 1679 on non-Muslim subjects after a lapse of over a century, generating widespread urban riots in Delhi.", "Ordered the demolition of prominent temples (Vishwanath at Kashi, Keshavdeva at Mathura), alienating broad Hindu populations."]),
             ("Rupture with the Rajputs: The Marwar and Mewar Wars", ["Interfered aggressively in the Marwar succession following the death of Maharaja Jaswant Singh (1678), attempting to install a puppet ruler and sequestering the infant Ajit Singh.", "Triggered a 30-year guerrilla war led by Durgadas Rathore. Mewar allied with Marwar, turning the loyal Rajput sword-arm into bitter adversaries."]),
             ("Martyrdom of Guru Tegh Bahadur and Militarization of the Sikhs", ["Executed the 9th Sikh Guru, Guru Tegh Bahadur, at Delhi's Chandni Chowk (1675) for defending Kashmiri Pandits' freedom of faith.", "Forced Guru Gobind Singh to create the martial 'Khalsa' (1699) at Anandpur Sahib, creating a formidable revolutionary resistance in the Punjab."]),
             ("The Deccan Ulcer: Annexation of Bijapur and Golconda", ["Personally campaigned in the Deccan for 25 uninterrupted years (1681-1707).", "Annexed Bijapur (1686) and Golconda (1687), destroying the regional Shia buffer states that had contained the Marathas.", "Napoleon famously said: 'The Spanish ulcer ruined me.' Similarly, the 'Deccan Ulcer' ruined Aurangzeb, consuming his imperial armies, bankrupting the treasury, and paralyzing northern administration."])
         ],
         "Mind map: Religious Orthodoxy (Jizya, Temple destructions) -> Alienation (Rajput War, Khalsa creation) -> The Deccan Ulcer (25-year quagmire) = Mughal Collapse.",
         "Aurangzeb was an indefatigable military ascetic, yet his theological dogmatism and imperial overstretch shattered the pluralistic consensus that had sustained the empire, setting the stage for its rapid collapse."),

        ("mains_med_023", "later-mughals", 15, 250, True, "UPSC CSE 2015 GS-1", "Satish Chandra; Irfan Habib, Agrarian System of Mughal India",
         "The decline of the Mughal Empire was not merely the result of personal royal failings, but a systemic structural breakdown characterized by the 'Jagirdari Crisis' and agrarian exploitation. Elucidate.",
         "While earlier colonial historians attributed the fall of the Mughals solely to Aurangzeb's religious bigotry or weak later emperors, modern economic historians (Satish Chandra, Irfan Habib, Athar Ali) demonstrate that the empire collapsed under profound structural and agrarian contradictions.",
         [
             ("Satish Chandra's 'Jagirdari Crisis' Thesis", ["The rapid expansion of the empire into the Deccan under Aurangzeb triggered a massive influx of Deccan nobles (Deccani Muslims, Marathas) into the Mansabdari system.", "Created an acute shortage of fertile crown land ('Pai-baqi') available for assignment as Jagirs—a crisis termed 'Be-jagiri'.", "Nobles engaged in bitter court factionalism (Turanis, Iranis, Hindustanis) to capture the few remaining lucrative Jagirs, paralyzing imperial governance."]),
             ("Disparity Between 'Jama' (Estimated Revenue) and 'Hasil' (Actual Collection)", ["Due to incessant warfare and peasant flight, actual revenue collection ('Hasil') fell far below theoretical paper assessment ('Jama').", "Mansabdars could no longer maintain their mandatory quota of cavalry troops, leading to catastrophic military decay."]),
             ("Irfan Habib's Agrarian Crisis and Peasant Revolts", ["Jagirdars, facing frequent transfers and uncertain tenure, ruthlessly extracted maximum revenue from tillers without investing in long-term agrarian improvements.", "The tax burden rose to 50% or more of produce, forcing impoverished peasants to abandon cultivation, flee to forests, or join armed rural rebellions.", "Peasant unrest crystallized along regional and sectarian lines: Jat rebellions under Gokula and Suraj Mal in Agra-Mathura; Satnami revolt in Mewat; Sikh uprising under Banda Singh Bahadur."]),
             ("External Shocks and Decentralized Successor States", ["Devastating invasions by Nadir Shah (1739) and Ahmad Shah Abdali stripped Delhi of its wealth (Peacock Throne, Koh-i-Noor).", "Regional governors broke away to establish de facto autonomous successor states: Murshid Quli Khan in Bengal, Saadat Khan in Awadh, and Nizam-ul-Mulk in Hyderabad."])
         ],
         "Flowchart of systemic crisis: Imperial Expansion -> Be-Jagiri -> Over-exploitation of Peasants -> Rural Rebellions -> Military Decay -> External Sack (Nadir Shah).",
         "The collapse of the Mughal Empire was an institutional implosion: an agrarian-fiscal structure crushed under the weight of its own administrative overexpansion and peasant impoverishment."),

        ("mains_med_024", "maratha-empire", 15, 250, True, "UPSC CSE 2017 GS-1", "Satish Chandra, Ch. 18; Jadunath Sarkar",
         "Chhatrapati Shivaji Maharaj's military brilliance was matched by his enlightened administrative acumen. Examine his administrative institutions with special focus on the Ashta Pradhan.",
         "Crowned as Chhatrapati at Raigad in 1674, Shivaji Maharaj established 'Hindavi Swarajya', combining innovative mobile guerrilla warfare with an exceptionally modern, centralized, and welfare-oriented civil administration.",
         [
             ("The Ashta Pradhan (Council of Eight Ministers)", ["Created an advisory council of eight ministers directly responsible to the King:", "1. Peshwa (Mukhya Pradhan): Prime Minister overseeing general civil and military administration.", "2. Amatya (Majumdar): Finance minister auditing royal income and expenditure.", "3. Senapati (Sar-i-Naubat): Commander-in-chief in charge of military recruitment and field command.", "4. Waqia-Navis (Mantri): Home minister and intelligence supervisor.", "5. Sachiv (Shurnavis): Superintendent of royal correspondence and official decrees.", "6. Sumant (Dabir): Foreign minister managing diplomacy.", "7. Nyayadhish: Chief Justice presiding over civil and military law.", "8. Panditrao: Chief ecclesiastical officer and religious endowments supervisor.", "Crucial Rule: All ministers except Nyayadhish and Panditrao were required to lead troops in battle. Offices were strictly non-hereditary."]),
             ("Agrarian Reforms and Peasant Protection", ["Abolished the exploitative Jagirdari system; established direct contact with peasants through state revenue collectors ('Karkuns').", "Measured land using the standardized 'Kathi' (measuring rod). Reduced the state revenue share to 33%, later revised to 40% only after eliminating illegal feudal cesses.", "Prohibited revenue officials from seizing peasants' plough oxen or seeds during times of scarcity."]),
             ("Fiscal Levies on External Territories: Chauth and Sardeshmukhi", ["Chauth: 1/4th (25%) of standard revenue demanded from neighbouring non-Maratha territories as protection money against Maratha raids.", "Sardeshmukhi: An additional 10% levy claimed by Shivaji as the hereditary supreme head ('Sardeshmukh') of Maharashtra."]),
             ("Military Architecture and Naval Power", ["Maintained strict discipline: soldiers were forbidden from bringing dancing girls or women into military camps; desecration of religious places was severely punished.", "Pioneered indigenous naval power: built island sea forts (Sindhudurg, Vijaydurg) and maintained a fighting fleet under Maynak Bhandari to counter Portuguese and Siddis."])
         ],
         "Administrative structure chart: Chhatrapati -> Ashta Pradhan (8 Ministers) -> Subhedars (Prants) -> Karkuns -> Ryots (Peasants protected from Jagirdars).",
         "Shivaji was not a predatory chieftain as colonial historians alleged, but a visionary state-builder who created a disciplined, indigenous, and deeply righteous administration."),

        ("mains_med_025", "maratha-empire", 15, 250, False, "Standard Practice", "Satish Chandra, Ch. 19; Spectrum",
         "The Third Battle of Panipat (1761) was a watershed catastrophe that altered the destiny of India. Analyze the causes, military miscalculations, and profound geopolitical consequences.",
         "Fought on 14 January 1761 between the Marathas under Sadashivrao Bhau and the Afghan coalition led by Ahmad Shah Abdali, the Third Battle of Panipat shattered Maratha ambitions of subcontinental hegemony and cleared the path for British colonial conquest.",
         [
             ("Causes: Maratha Imperial Expansion into North India", ["Peshwa Baji Rao I had launched the 'Hindu Pad Padshahi' drive: 'Strike at the trunk of the withered tree (Mughals).' Marathas captured Delhi (1752) and Lahore/Attock (1758 under Raghunath Rao).", "Drove Ahmad Shah Abdali's son Timur Shah out of Punjab, directly provoking Abdali to launch a holy war to restore Afghan prestige.", "Marathas alienated northern powers through aggressive Chauth extractions: Rajputs, Jats (Suraj Mal withdrew after tactical disagreements), and the Nawab of Awadh (Shuja-ud-Daula) joined Abdali."]),
             ("Tactical and Military Miscalculations at Panipat", ["Sadashivrao Bhau abandoned the traditional mobile Maratha guerrilla warfare ('Ganimi Kava') in favour of a rigid European-style infantry phalanx with heavy artillery under Ibrahim Khan Gardi.", "Encumbered by a massive camp of over 100,000 non-combatant pilgrims, women, and priests, exhausting supplies.", "Abdali cut off Maratha supply lines from the south; Maratha troops and horses starved for two months before being forced to give battle in desperation.", "Abdali's superior mobility: deployed camel-mounted swivel guns ('Zamburaks') and disciplined reserves that enveloped the Maratha flank."]),
             ("Devastating Geopolitical Consequences", ["A generation of Maratha leaders perished in a single day: Sadashivrao Bhau, Vishwasrao (Peshwa's son), Tukoji Holkar, and Jankoji Scindia. Peshwa Balaji Baji Rao died of heartbreak.", "Maratha confederacy fragmented into autonomous regional chieftaincies (Scindias of Gwalior, Holkars of Indore, Gaekwads of Baroda, Bhonsles of Nagpur).", "Abdali soon returned to Afghanistan, leaving a power vacuum in Delhi.", "Most Decisive Beneficiary: The English East India Company. As G.S. Sardesai observed, Panipat did not decide who was to rule India, but who was NOT to rule India—clearing the path for British ascendancy."])
         ],
         "Geopolitical vector diagram: Maratha Northern Overreach -> Total Isolation (Rajputs/Jats/Awadh alienated) -> Panipat Slaughter -> British EIC Ascendancy.",
         "The bloodbath of Panipat was India's greatest 18th-century tragedy: it extinguished the indigenous prospect of an all-India Maratha empire, leaving the subcontinent open to British colonial subjugation."),

        ("mains_med_026", "later-mughals", 15, 250, True, "UPSC CSE 2021 GS-1", "Seema Alavi, The Eighteenth Century in India; C.A. Bayly",
         "The eighteenth century in India was not an unmitigated 'Dark Age of Anarchy' as portrayed by colonial historians, but an era of dynamic regional state formation and economic reorientation. Critically examine.",
         "Colonial historiography (James Mill, Vincent Smith) characterized 18th-century India as a chaotic 'Dark Age' of civil war following Mughal collapse, justifying British conquest as a benevolent civilizing mission. Modern revisionist historiography (C.A. Bayly, Muzaffar Alam, Sanjay Subrahmanyam) fundamentally challenges this decline thesis.",
         [
             ("Mughal Imperial Decentralization vs Regional Prosperity", ["The decline of the Delhi center did NOT mean the collapse of the economy; economic vitality decentralized into prosperous regional successor states: Bengal under Murshid Quli Khan, Awadh under Saadat Khan, Hyderabad under Asaf Jah I, and the Maratha realm.", "Agricultural output, rural markets ('Ganjes'), and artisan textile production flourished in Bengal and the Coromandel, generating robust agrarian surpluses."]),
             ("Financialization and the Rise of Indigenous Banking Magnates", ["Emergence of powerful merchant-bankers ('Hukumat-i-Sahukars') like the Jagat Seths of Bengal, who functioned as state financiers, remitting revenues across subcontinental bills of exchange ('Hundis').", "Demonstrated high monetization, commercial sophistication, and capital accumulation outside imperial court control."]),
             ("Cultural Flourishing in Regional Courts", ["Cultural patronage migrated from Delhi to dynamic regional hubs: Urdu poetry and Kathak dance flourished in Lucknow under Awadh Nawabs; miniature painting flourished in Kangra and Rajput courts; Carnatic classical music crystallized in Thanjavur.", "Literature, music, and vernacular arts attained new heights of lyrical sophistication."])
         ],
         "Balance diagram: Colonial 'Dark Age' Myth (Imperial collapse, warfare) vs Modern Historical Reality (Regional economic vibrancy, Jagat Seth banking, Cultural flowering).",
         "The 18th century was not an era of societal degeneration, but a vibrant epoch of regional political re-articulation that British colonialism violently arrested and subjugated."),

        ("mains_med_027", "bahmani-sultanate", 10, 150, False, "Standard Practice", "Satish Chandra, Ch. 8",
         "Assess the administrative, educational, and military reforms of Mahmud Gawan in the Bahmani Kingdom.",
         "Serving as Prime Minister (Khwaja Jahan) from 1466 to 1481 under Muhammad Shah III, Iranian-born Mahmud Gawan was the greatest statesman of the Bahmani Sultanate.",
         [
             ("Administrative Reorganization and Curbing Noble Power", ["Subdivided the four sprawling provinces ('Tarafs') into eight smaller provinces to prevent provincial governors from amassing excessive power.", "Brought key strategic border forts under direct royal custody rather than provincial governors.", "Strictly regulated the salaries and military quotas of nobles, ordering land revenue assessments based on actual cultivation."]),
             ("Educational and Architectural Legacy: Mahmud Gawan Madrasa", ["Built the magnificent Mahmud Gawan Madrasa at Bidar (1472), designed in the Persian Timurid style with minarets and glazed blue tiles.", "Housed a legendary library of over 3,000 rare manuscripts, functioning as an elite residential university attracting scholars from across the Islamic world."]),
             ("Tragic Demise and Sultanate Fragmentation", ["Bitter factionalism between 'Deccanis' (native Muslims) and 'Afaquis' (foreign migrants like Gawan) led envious Deccan nobles to forge a treasonous letter.", "The intoxicated Sultan ordered Gawan's execution in 1481; his death removed the only capable unifying leader, directly triggering the disintegration of the Bahmani state into the five Deccan Sultanates."])
         ],
         "Flowchart: Bahmani expansion -> Gawan's 8 Taraf reform & Bidar Madrasa -> Deccani vs Afaqui court conspiracy -> Gawan's execution -> Breakup into 5 Deccan Sultanates.",
         "Mahmud Gawan was an enlightened administrative genius whose execution sealed the doom of the Bahmani dynasty."),

        ("mains_med_028", "sikh-gurus", 15, 250, True, "UPSC CSE 2019 GS-1", "Satish Chandra, Ch. 19; Spectrum",
         "The creation of the Khalsa by Guru Gobind Singh in 1699 was a revolutionary socio-military transformation that empowered the dispossessed. Elucidate.",
         "On Baisakhi Day in 1699 at Anandpur Sahib, the tenth Sikh Guru, Guru Gobind Singh Ji, created the 'Khalsa Panth' (the Order of the Pure), transforming a pacifist devotional fraternity into an indomitable warrior community resisting Mughal imperial tyranny.",
         [
             ("Democratic Equality and Annihilation of Caste ('Amrit Sanchar')", ["Administered the 'Khande di Pahul' (baptism of the double-edged sword) to the 'Panj Pyare' (Five Beloved Ones), who came from diverse caste backgrounds (three were from low/shudra castes).", "Abolished caste distinctions by conferring the common surname 'Singh' (Lion) on all men and 'Kaur' (Princess) on all women.", "Abolished the hereditary masand system of intermediaries; instituted the revolutionary doctrine of 'Guru Panth' (the community itself embodies the Guru)."]),
             ("The Five Ks ('Panj Kakar') as Uniform Identity", ["Mandated five physical symbols of faith: Kesh (uncut hair/spirituality), Kangha (wooden comb/cleanliness), Kara (iron bangle/restraint), Kachhera (cotton undergarment/moral purity), and Kirpan (curved sword/defense of the righteous and oppressed).", "Created an unmistakable visual identity that prevented Sikhs from concealing their faith in the face of state persecution."]),
             ("Righteous War: The Doctrine of 'Zafarnama'", ["In his historic Persian epistle 'Zafarnama' addressed to Aurangzeb, Guru Gobind Singh articulated the moral justification of armed resistance: 'When all other avenues fail, it is righteous to draw the sword.'", "Infused the oppressed peasantry with martial courage to fight imperial tyranny without hatred."])
         ],
         "Concept map: Khande di Pahul -> Panj Pyare (Anti-caste egalitarianism) + Five Ks (Disciplined identity) -> Saint-Soldier (Sant-Sipahi) resisting tyranny.",
         "The creation of the Khalsa was a socio-political revolution: it forged a casteless fraternity of 'Saint-Soldiers' that defended human rights and eventually established sovereign Punjabi rule under Maharaja Ranjit Singh."),

        ("mains_med_029", "delhi-sultanate", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 2; NCERT Class 11",
         "Trace the evolution of Delhi Sultanate architecture from the trabeate-arcuate synthesis of the Mamluks to the austere battered walls of the Tughlaqs and octagonal tombs of the Lodis.",
         "Delhi Sultanate architecture introduced the true 'Arcuate' system (arches, vaults, and domes) into India, evolving over three centuries through distinct dynastic phases.",
         [
             ("Mamluk Phase: Early Improvisation and Trabeate-Arcuate Fusion", ["Reused columns from demolished Hindu/Jain shrines with corbelled arches (Quwwat-ul-Islam mosque, Arhai Din ka Jhonpra).", "Completed the Qutub Minar (soaring sandstone minaret with fluted balconies and stalactite corbelling) and the Alai Darwaza (Alauddin Khalji: first true horseshoe arch with red sandstone and white marble inlay)."]),
             ("Tughlaq Phase: Austerity, Battered Walls, and Massive Stone Masonry", ["Reaction against Khalji extravagance; characterized by plain grey quartzite stone, austere interiors, and heavy fortifications.", "Introduced 'Sloping/Battered Walls' ('Salami') leaning inward to impart structural stability and an illusion of massive strength (Tughlaqabad Fort, Ghiyasuddin Tughlaq's tomb).", "Extensive use of the four-centred Tudor arch and stone lintel-over-arch synthesis."]),
             ("Lodi Phase: Double Domes and Octagonal Tombs", ["Introduced the 'Double Dome' (inner dome maintaining interior proportions, outer dome soaring high for exterior monumentalism; e.g., Sikandar Lodi's tomb).", "Erected tombs on high plinths with octagonal floor plans surrounded by arched verandahs (Bara Gumbad, Shish Gumbad in Lodi Gardens)."])
         ],
         "Chronological architectural sketch: Alai Darwaza true arch -> Tughlaq battered sloping wall -> Lodi double dome cross-section.",
         "Sultanate architecture progressively evolved from decorative improvisation to engineering austerity and structural double-domes, laying the technical foundation for Mughal architectural splendours."),

        ("mains_med_030", "modern-advent", 10, 150, False, "Standard Practice", "Spectrum Modern India; Bipan Chandra",
         "Explain the mechanisms through which the Portuguese established maritime hegemony in the Indian Ocean in the 16th century, and discuss the causes of their rapid eclipse.",
         "Following Vasco da Gama's arrival at Calicut in 1498, Portugal established the 'Estado da India', dominating the Indian Ocean through naval supremacy rather than territorial conquest.",
         [
             ("Blue Water Policy and the Cartaz-Armada System", ["Francisco de Almeida introduced the 'Blue Water Policy' (A policy of establishing naval maritime dominance across ocean choke points rather than inland fortresses).", "Afonso de Albuquerque captured strategic maritime gateways: Goa (1510), Malacca (1511), and Ormuz (1515).", "Enforced the 'Cartaz' system: required all Asian merchant vessels to purchase a Portuguese commercial transit pass and pay customs duties at Portuguese ports, confiscating and sinking unlicensed ships."]),
             ("Causes of Rapid Portuguese Decline", ["1. Religious Intolerance and the Goa Inquisition: Brutally persecuted Hindus and Muslims, alienating local populations and regional rulers.", "2. Limited Manpower and Resources: Portugal was too small a nation to sustain a distant global empire.", "3. Discovery of Brazil: Diverted Portuguese imperial colonization and mercantile capital to South America.", "4. Rampant Official Corruption and Piracy: Portuguese captains engaged in private plunder, eroding merchant trust.", "5. Arrival of Superior European Rivals: Decisively outmaneuvered by the English East India Company (Battle of Swally 1612) and the Dutch VOC (who captured Malacca and Ceylon)."])
         ],
         "Indian Ocean choke point map: Ormuz (Persian Gulf) <--> Goa (India) <--> Malacca (Southeast Asia) forming Albuquerque's naval triangle.",
         "While the Portuguese pioneered modern European oceanic imperialism in Asia, their religious fanaticism and limited domestic resource base doomed their monopoly to rapid eclipse by the Dutch and English."),

        ("mains_med_031", "early-medieval-period", 10, 150, False, "Standard Practice", "Satish Chandra, Ch. 7; UP Special",
         "The Sharqi Sultanate of Jaunpur transformed their capital into the 'Shiraz of India'. Discuss their architectural and cultural achievements.",
         "Founded in 1394 by Malik Sarwar (Khwaja-i-Jahan) in eastern Uttar Pradesh, the Sharqi dynasty made Jaunpur a radiant center of Islamic learning, architecture, and music, earning the title 'Shiraz-i-Hind'.",
         [
             ("Distinctive Architectural Style: Propylon Screens", ["Sharqi architecture abandoned minarets in favour of massive, soaring arched pylons ('Propylons') screening the central dome of the sanctuary.", "Atala Masjid (built by Ibrahim Shah Sharqi in 1408): Masterpiece characterized by a giant 75-foot stepped propylon, battered walls, and ornate arched cloisters.", "Other monuments: Jama Masjid and Lal Darwaza Masjid, synthesized Hindu pillar carving with Islamic vaults."]),
             ("Educational and Literary Preeminence ('Shiraz-i-Hind')", ["Patronized thousands of scholars, theologians, and Sufi saints; Emperor Shah Jahan famously remarked that Jaunpur was the Shiraz of India.", "Sher Shah Suri received his foundational administrative and literary education in the madrasas of Jaunpur."]),
             ("Pioneering Contributions to Indian Classical Music", ["Sultan Husain Shah Sharqi was a musical genius: invented the 'Jaunpuri Todi' and 'Husaini Todi' ragas, and played a decisive role in developing the Khayal style of Hindustani classical music."])
         ],
         "Architectural facade sketch of Atala Masjid Jaunpur highlighting the towering central propylon screen.",
         "The Sharqi Sultanate proved that regional provincial kingdoms were vibrant cultural crucibles, leaving an indelible imprint on Indian architecture, classical music, and education."),

        ("mains_med_032", "bhakti-sufi-movements", 10, 150, False, "Standard Practice", "Satish Chandra, Ch. 18; NCERT Themes Theme 6",
         "The Varkari movement of Maharashtra forged a democratic socio-spiritual identity that transcended caste lines. Discuss with reference to Jnaneshwar, Namdev, and Tukaram.",
         "Centered on the annual pilgrimage ('Wari') to the temple of Lord Vithoba (Vitthal) at Pandharpur on the Bhima river, the Varkari Sampradaya was the spiritual heartbeat of medieval Maharashtra.",
         [
             ("Sant Jnaneshwar (Dnyaneshwar): The Vernacular Pioneer", ["Composed the 'Jnaneshwari' (Bhavartha Dipika) in 1290 CE—a commentary on the Bhagavad Gita in vernacular Marathi, breaking the Brahminical Sanskrit monopoly over philosophical wisdom.", "Asserted that divine love and spiritual liberation were accessible to women and Shudras."]),
             ("Sant Namdev: The Universal Devotional Messenger", ["A tailor by profession, Namdev preached radical Nirguna Bhakti and social equality across western and northern India.", "His Marathi 'Abhangas' overflow with love; 61 of his devotional verses were incorporated into the Sikh holy scripture, the Guru Granth Sahib."]),
             ("Sant Tukaram and Sant Eknath", ["Eknath championed social equality, dining with outcastes and preaching through 'Bharuds' (folk songs).", "Tukaram (17th century): A peasant-grocer whose impassioned Abhangas attacked Brahminical hypocrisy, empty rituals, and caste superiority. His verses inspired Chhatrapati Shivaji's soldiers with moral courage."])
         ],
         "Timeline of Varkari Masters: Jnaneshwar (13th c.) -> Namdev (14th c.) -> Eknath (16th c.) -> Tukaram (17th c.) -> Inspiring Swarajya.",
         "The Varkari movement was a cultural renaissance: by preaching radical human dignity in the mother tongue, it forged the shared socio-cultural unity that formed the bedrock of the Maratha nation."),

        ("mains_med_033", "maratha-empire", 10, 150, False, "Standard Practice", "Satish Chandra, Ch. 19",
         "Peshwa Baji Rao I was the real architect of Maratha imperial expansion. Evaluate his forward policy of 'Hindu Pad Padshahi'.",
         "Serving as Peshwa from 1720 to 1740 under Chhatrapati Shahu, Baji Rao I was an undefeated cavalry general who transformed the regional Maratha state into a pan-Indian empire.",
         [
             ("The Forward Policy: Strike at the Trunk", ["Baji Rao proclaimed to Shahu: 'Let us strike at the trunk of the withered Mughal tree, and the branches will fall of themselves. Thus should the Maratha flag fly from the Krishna to the Indus.'", "Shifted Maratha strategy from passive defense in the Deccan to aggressive northward cavalry thrusts into Malwa, Gujarat, and Bundelkhand."]),
             ("Military Masterpieces: Palkhed and Delhi Raid", ["Battle of Palkhed (1728): Defeated Nizam-ul-Mulk of Hyderabad through brilliant mobile cavalry maneuvers, cutting off the Nizam's water supplies and forcing him to sign the Treaty of Mungi Shevgaon without a pitched artillery battle.", "Raid on Delhi (1737): Dashed 500 miles with light cavalry in just 10 days, appearing outside the gates of Delhi, exposing the utter impotence of Emperor Muhammad Shah.", "Defeated the combined armies of the Mughals and the Nizam at the Battle of Bhopal (1738)."]),
             ("Institutionalization of the Maratha Confederacy", ["Encouraged capable military leaders by assigning them regional spheres of expansion: Scindias in Gwalior, Holkars in Malwa/Indore, Gaekwads in Baroda, and Pawars in Dhar."])
         ],
         "Map of Baji Rao I's blitzkrieg campaigns: Palkhed, Malwa conquest, Bundelkhand alliance, and Delhi raid (1737).",
         "Baji Rao I was a military genius who in two decades shattered the myth of Mughal supremacy, hoisting the Maratha saffron banner across northern India."),

        ("mains_med_034", "bhakti-sufi-movements", 10, 150, False, "Standard Practice", "Satish Chandra, Ch. 12; NCERT Themes Theme 6",
         "Differentiate between the Chishti and Suhrawardi Sufi Silsilas in medieval India with respect to their attitudes toward the state, wealth, and ascetic practice.",
         "Sufism in India organized into distinct spiritual orders ('Silsilas'), with the Chishti and Suhrawardi orders representing contrasting philosophies regarding worldly engagement and royal courts.",
         [
             ("Attitude Toward Royal Power and Court Politics", ["Chishti Order (Khwaja Moinuddin Chishti, Fariduddin Ganjshakar, Nizamuddin Auliya): Maintained strict aloofness from the state, refused royal land grants and titles, and avoided court politics. Sheikh Nizamuddin Auliya famously quipped when Sultan Alauddin Khalji wished to visit: 'My house has two doors; if the Sultan enters through one, I will leave through the other.'", "Suhrawardi Order (Bahauddin Zakariya, Ruknuddin Abul Fath): Centered in Multan and Punjab; actively associated with the state, accepted high royal offices (Shaikh-ul-Islam) and jagirs, arguing that association with rulers allowed them to influence imperial policy in favour of public welfare."]),
             ("Attitude Toward Wealth and Worldly Possessions", ["Chishti: Espoused voluntary poverty ('Faqr'), distributed all daily donations to the poor before sunset, and lived on unasked-for charity ('Futuh').", "Suhrawardi: Believed that wealth was not an obstacle to spiritual realization, provided it was used with moral rectitude; maintained affluent khanqahs and large estates."]),
             ("Devotional Practices: Sama and Yoga", ["Chishti: Championed 'Sama' (audition of devotional music) to induce spiritual ecstasy; embraced indigenous yogic breath-control techniques.", "Suhrawardi: Looked upon music with suspicion, adhering more strictly to orthodox Sunni jurisprudence."])
         ],
         "Side-by-side comparative table: Chishti vs Suhrawardi across Court Engagement, Wealth, Ascetic Rigour, and Sama (Music).",
         "While the Chishtis won immense grassroots love through poverty and music, the Suhrawardis built influential institutional stability in northwestern frontier administration."),

        ("mains_med_035", "modern-advent", 15, 250, True, "UPSC CSE 2016 GS-1", "Bipan Chandra; Spectrum Modern India",
         "The Battle of Plassey (1757) was a skirmish won by treachery, but the Battle of Buxar (1764) was a decisive military contest that established British territorial supremacy in India. Discuss.",
         "While the Battle of Plassey (1757) gave the British East India Company its financial foothold in Bengal, it was the Battle of Buxar (1764) and the subsequent Treaty of Allahabad (1765) that definitively established British sovereign authority in northern India.",
         [
             ("Plassey (1757): Treachery and Political Coup", ["Robert Clive defeated Siraj-ud-Daula not through tactical military brilliance, but through a conspiratorial coup with treacherous nobles: Mir Jafar (army commander), Rai Durlabh, and financier Jagat Seth.", "Hardly a pitched battle: Siraj's army of 50,000 disintegrated when Mir Jafar refused to order his division to attack.", "Consequence: British installed puppet Nawabs (Mir Jafar, then Mir Qasim), extracting colossal personal bribes and the revenue of the 24 Parganas, transforming the Company into the master-puppeteer of Bengal."]),
             ("Buxar (1764): A Decisive Test of Arms", ["Fought on 22 October 1764 at Buxar (Bihar) between Hector Munro's Company army and a formidable grand tripartite Indian coalition: 1. Mir Qasim (deposed Nawab of Bengal), 2. Shuja-ud-Daula (Nawab of Awadh), and 3. Shah Alam II (Mughal Emperor).", "A fiercely contested, professional military combat against a combined force of over 40,000 Indian troops equipped with modern French-trained artillery.", "Munro's disciplined British and Indian sepoy regiments triumphed through superior firepower, battalion coordination, and tactical maneuver."]),
             ("The Treaty of Allahabad (1765): The Birth of the British Empire", ["Clive secured the 'Diwani' (sovereign right to collect land revenues and administer civil justice) of Bengal, Bihar, and Orissa directly from Mughal Emperor Shah Alam II in return for an annual tribute of 26 lakh rupees.", "Reduced the Nawab of Awadh to a dependent buffer ally, stationing British troops at Awadh's expense.", "Inaugurated the exploitative 'Dual System of Government' (Dyarchy) in Bengal (1765-1772): Company enjoyed all power and revenue without administrative responsibility, leading to the devastating Bengal Famine of 1770."])
         ],
         "Geopolitical vector diagram: Plassey (Mercantile Bribery) -> Buxar (Military Supremacy) -> Treaty of Allahabad (Diwani Rights of Bengal, Bihar, Orissa) -> Foundation of British Raj.",
         "Plassey made the British the kingmakers of Bengal; Buxar made them the undisputed masters of the Indian subcontinent.")
    ]

    for item in med_25:
        items.append({
            "id": item[0],
            "category": "medieval",
            "categoryLabel": "Medieval India",
            "periodId": item[1],
            "marks": item[2],
            "wordLimit": item[3],
            "isPyq": item[4],
            "yearSource": item[5],
            "bookRef": item[6],
            "question": item[7],
            "framework": {
                "intro": item[8],
                "body": [{"heading": b[0], "points": b[1]} for b in item[9]],
                "diagramMapIdea": item[10],
                "conclusion": item[11]
            }
        })

    return items

if __name__ == '__main__':
    med = get_medieval_mains()
    print(f"Generated {len(med)} Medieval Mains questions ({med[0]['id']} to {med[-1]['id']})")
    with open('data/batch_mains_medieval.json', 'w', encoding='utf8') as f:
        json.dump(med, f, indent=2, ensure_ascii=False)
