# scripts/gen_mains_art_culture.py
import json

def get_art_culture_mains():
    # 35 Comprehensive Art & Culture Mains Questions (mains_art_001 to mains_art_035)
    items = [
        {
            "id": "mains_art_001", "periodId": "mauryan-empire", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2018 GS-1", "bookRef": "Nitin Singhania, Ch. 1; NCERT Class 11 An Introduction to Indian Art",
            "question": "Differentiate between the Court Art and Popular / Folk Art of the Mauryan period, highlighting their distinctive patrons, materials, and artistic conventions.",
            "framework": {
                "intro": "Mauryan art (c. 4th-2nd c. BCE) is traditionally bifurcated into imperial 'Court Art' patronized by monarchs for state ideology and 'Popular / Folk Art' created by local guilds and sculptors reflecting indigenous folk beliefs.",
                "body": [
                    {"heading": "1. Mauryan Court Art: Imperial Ideology and Royal Monoliths", "points": [
                        "Patronage and Purpose: Commissioned directly by emperors (Chandragupta, Ashoka) to legitimize imperial sovereignty and propagate moral Dhamma.",
                        "Material and Finish: Quarried predominantly from Chunar sandstone; characterized by the mirror-like, glass-smooth 'Mauryan Polish' whose recipe was lost after the empire.",
                        "Monolithic Pillars: Freestanding polished columns without structural bases crowned by monumental animal capitals (Sarnath Lion Capital, Rampurva Bull, Lauriya Nandangarh).",
                        "Palace Architecture: Kumrahar 80-pillared hypostyle hall and Bulandibagh wooden palisades at Pataliputra, praised by Faxian as works of divine spirits.",
                        "Rock-Cut Caves: Barabar and Nagarjuni hill caves (Lomas Rishi and Sudama caves) dedicated to Ajivika ascetics, featuring vaulted roofs and glass-polished granite walls."
                    ]},
                    {"heading": "2. Popular / Folk Art: Indigenous Sacred Iconography", "points": [
                        "Patronage and Purpose: Sculpted by local individual craftsmen and guilds; fulfilled popular devotional needs associated with nature spirits, fertility, and wealth (Yakshas and Yakshis).",
                        "Material and Style: Indigenous sandstone, heavily rounded anatomical proportions, earthiness, and elaborate ornaments without the glassy mirror polish.",
                        "Masterpieces: 1. Didarganj Yakshi (Patna): Celebrated for voluptuous feminine anatomy, kinetic contrapposto posture, flywhisk in hand, and sophisticated jewellery; 2. Parkham Yaksha (Mathura): Colossal, monumental male deity symbolizing earth power; 3. Dhauli Rock-Cut Elephant (Odisha): Naturalistic animal carving emerging from the living bedrock, symbolizing the Buddha."
                    ]}
                ],
                "diagramMapIdea": "Comparative split table: Court Art (State-sponsored, Chunar sandstone, Mauryan Polish, Buddhist/Imperial themes) vs Popular Art (Individual guild, Folk nature spirits, Yakshas/Yakshis, Earthy realism).",
                "conclusion": "While Mauryan court art displayed cosmopolitan imperial polish, popular art preserved the vibrant indigenous terracotta and stone-carving traditions that formed the bedrock of classical Indian sculpture."
            }
        },
        {
            "id": "mains_art_002", "periodId": "kingdoms-of-south", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2013 GS-1", "bookRef": "Nitin Singhania, Ch. 1; A.L. Basham",
            "question": "The Chola bronze idol of Nataraja is a cosmic masterpiece that synthesizes metallurgy, philosophy, and aesthetic kinetics. Analyze the symbolic significance of its iconography.",
            "framework": {
                "intro": "Cast using the intricate 'Cire Perdue' (Lost-Wax) metallurgical technique during the Imperial Chola era (9th-13th c. CE), the Nataraja (Lord of Dance) bronze idol portrays Shiva performing the cosmic dance of 'Anandatandava' within a flaming halo.",
                "body": [
                    {"heading": "Cosmic Rhythm: The Circle of Fire ('Prabhamandala')", "points": [
                        "The flaming aureole of fire ('Prabhamandala' or Tiruvasi) represents the endless cyclical cosmos: creation, preservation, and dissolution of the universe.",
                        "The lotus pedestal ('Padmapitha') represents the manifest universe."
                    ]},
                    {"heading": "Symbolism of the Four Arms ('Chaturbhuja')", "points": [
                        "1. Upper Right Hand: Holds the hourglass drum ('Damaru'), symbolizing the primal sound ('Nada') from which all creation and cosmic time originates.",
                        "2. Upper Left Hand: Holds the fire flame ('Agni'), symbolizing cosmic dissolution and purification that consumes the universe.",
                        "3. Lower Right Hand: Held in the gesture of fearlessness ('Abhaya Mudra'), offering divine protection, solace, and peace to the seeker.",
                        "4. Lower Left Hand: Stretches gracefully across the chest in the 'Gajahasta' (elephant-trunk) pose, pointing downward to the lifted left foot, indicating spiritual refuge and salvation."
                    ]},
                    {"heading": "Triumph Over Ignorance: The Demon Apasmara", "points": [
                        "Shiva's right foot is planted firmly on the back of the dwarfish demon 'Apasmara Purusha' (Muyalaka), who represents human spiritual ignorance, ego, and worldly delusion.",
                        "The uplifted left leg symbolizes spiritual liberation ('Moksha') and the soul's ascent from material bondage."
                    ]},
                    {"heading": "Dynamic Kinetic Equilibrium", "points": [
                        "Shiva's braided dreadlocks fly wildly outward in the ecstasy of dance, carrying the river goddess Ganga and the crescent moon, yet his facial expression remains serenely calm, aloof, and meditative, embodying perfect poise amidst cosmic motion."
                    ]}
                ],
                "diagramMapIdea": "Detailed schematic drawing of Nataraja with callout arrows labelling: Damaru (Creation), Agni (Dissolution), Abhaya Mudra (Protection), Gajahasta (Refuge), Apasmara (Ego crushed), Uplifted foot (Moksha), and Prabhamandala (Cosmos).",
                "conclusion": "Renowned sculptor Auguste Rodin and physicist Fritjof Capra marveled at the Nataraja bronze: an eternal masterpiece uniting spiritual philosophy, mathematical physics, and artistic kinetics into sublime bronze poetry."
            }
        },
        {
            "id": "mains_art_003", "periodId": "ancient-art", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2015 GS-1", "bookRef": "Nitin Singhania, Ch. 2; NCERT Class 11",
            "question": "Compare the architectural morphology of the Odisha, Khajuraho, and Solanki sub-schools of Nagara temple architecture.",
            "framework": {
                "intro": "The Nagara temple style of North India flourished into three distinct regional sub-schools: the Kalinga/Odisha school, the Chandela/Khajuraho school of Bundelkhand, and the Solanki/Maru-Gurjara school of Gujarat and Rajasthan.",
                "body": [
                    {"heading": "1. Odisha Sub-School (Kalinga Architecture)", "points": [
                        "Floor Plan: Temple complex comprises sequential halls: Deula/Rekha Deula (sanctum with curvilinear tower), Jagamohana (assembly hall with pyramidal roof / Pidha Deula), Natamandapa (dance pavilion), and Bhogamandapa (refectory).",
                        "Distinctive Features: Exterior walls are profusely and intricately sculpted with chlorite and sandstone figures, while the interior sanctum walls are deliberately left plain and austere.",
                        "Examples: Lingaraja Temple (Bhubaneswar), Sun Temple (Konark - chariot on 24 giant wheels pulled by 7 horses), Jagannath Temple (Puri). Usually enclosed by high boundary walls."
                    ]},
                    {"heading": "2. Khajuraho Sub-School (Chandela Patronage)", "points": [
                        "Integrated Elevation: Entire temple conceived as a unified mountain range on a high masonry terrace (Jagati), progressing organically from Ardhamandapa, Mandapa, Mahamandapa, Antarala, to the Garbhagriha.",
                        "Tower Clusters: Crowning Shikhara is flanked by multiple miniature replica towers ('Urushringas') that lean into the central spire, creating an illusion of Mount Meru.",
                        "Sculptural Exuberance: Both interior and exterior surfaces are densely sculpted with sensual Nayikas, celestial maidens (Surasundaris), and Mithuna (erotic) panels representing spiritual non-duality and fertility.",
                        "Examples: Kandariya Mahadeva Temple, Lakshmana Temple, Chausath Yogini."
                    ]},
                    {"heading": "3. Solanki Sub-School (Maru-Gurjara Architecture)", "points": [
                        "Exquisite Stone Filigree: Sculpted out of soft sandstone and white marble; renowned for delicate lace-like ceiling carvings and ornate bracketed torana arches.",
                        "Stepwell and Water Reservoir Integration: Temples are directly paired with monumental stepped water tanks (Kunds) adorned with miniature shrines.",
                        "Examples: Sun Temple at Modhera (featuring the magnificent Surya Kund with 108 miniature shrines), Dilwara Jain Temples at Mount Abu (Vimal Vasahi and Luna Vasahi: translucent white marble ceilings carved like hanging chandeliers)."
                    ]}
                ],
                "diagramMapIdea": "Comparative structural sketches: 1. Odisha linear layout (Deula + Jagamohana + Natamandapa); 2. Khajuraho unified clustered Urushringas; 3. Modhera Sun Temple plan showing temple connected to Surya Kund stepwell.",
                "conclusion": "These three regional expressions demonstrate how the foundational Nagara canon adapted creatively to local stones, geological landscapes, and spiritual sensibilities across northern India."
            }
        },
        {
            "id": "mains_art_004", "periodId": "ancient-art", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2014 GS-1", "bookRef": "Nitin Singhania, Ch. 1; NCERT Class 11",
            "question": "Ajanta and Ellora represent two different worlds of rock-cut architectural and artistic genius. Compare and contrast the cave complexes in terms of chronology, religion, architecture, and painting.",
            "framework": {
                "intro": "Carved into the basalt cliffs of the Sahyadri mountains in Maharashtra, the UNESCO World Heritage sites of Ajanta (29 caves) and Ellora (34 caves) represent the highest summits of rock-cut architecture in South Asia, yet differ fundamentally in religious scope, architectural layout, and artistic mediums.",
                "body": [
                    {"heading": "Geographic Setting and Chronological Horizon", "points": [
                        "Ajanta: Horse-shoe shaped gorge overlooking the Waghora river; excavated in two distinct phases: Hinayana/Theravada (2nd c. BCE - 1st c. CE under Satavahanas) and Mahayana (5th c. CE under Vakatakas, notably Harishena).",
                        "Ellora: Located on a gentle sloping basalt ridge 100 km away; excavated over a later, broader chronological span (6th to 10th centuries CE under Rashtrakutas, Kalachuris, and Yadavas)."
                    ]},
                    {"heading": "Religious Pluralism vs Monastic Exclusivity", "points": [
                        "Ajanta: Exclusively Buddhist across all 29 caves (consisting of Chaitya prayer halls and Vihara residential monasteries).",
                        "Ellora: Celebrates subcontinental religious pluralism and eclectic coexistence across 34 numbered caves: Caves 1-12 (Buddhist), Caves 13-29 (Brahmanical / Hindu, including the monumental Kailasanatha Cave 16), and Caves 30-34 (Jain, e.g., Indra Sabha and Jagannatha Sabha)."
                    ]},
                    {"heading": "Artistic Mediums: Sublime Murals vs Colossal Monolithic Sculpture", "points": [
                        "Ajanta is world-renowned primarily for its sublime Fresco-Secco wall murals: painted over mud-plaster and cow-dung using natural mineral pigments, depicting Jataka tales, court scenes, and iconic Bodhisattvas (Padmapani with blue lotus and compassionate gaze; Vajrapani in Cave 1). Sculptures are secondary.",
                        "Ellora is characterized by monumental, colossal rock-cut three-dimensional sculpture and multi-storeyed structural excavation: Caves 11 and 12 (Do Tal and Tin Tal) are three-storeyed Buddhist monasteries; Cave 16 (Kailasanatha) is the world's largest monolithic free-standing structural excavation carved top-down from living cliff rock. Wall paintings are minor."
                    ]}
                ],
                "diagramMapIdea": "Side-by-side comparative table: Ajanta vs Ellora across Chronology, Religion, Primary Art form (Mural Painting vs Monolithic Stone Sculpture), and Topographical layout.",
                "conclusion": "While Ajanta's painted murals capture the inner spiritual introspection and psychological empathy of the Buddhist world, Ellora's stone colossi display the monumental kinetic power, tolerance, and engineering mastery of early medieval India."
            }
        },
        {
            "id": "mains_art_005", "periodId": "mughal-empire", "marks": 15, "wordLimit": 250, "isPyq": True,
            "yearSource": "UPSC CSE 2017 GS-1", "bookRef": "Nitin Singhania, Ch. 2; Percy Brown",
            "question": "Indo-Islamic architecture was not a foreign transplantation, but an organic syncretic fusion of Indian trabeate craftsmanship and Islamic arcuate engineering. Discuss.",
            "framework": {
                "intro": "With the establishment of the Delhi Sultanate (1206 CE), traditional Indian indigenous architectural techniques encountered Islamic architectural traditions, sparking a creative cross-fertilization known as 'Indo-Islamic' or 'Indo-Saracenic' architecture.",
                "body": [
                    {"heading": "Synthesis of Engineering Systems: Trabeate meets Arcuate", "points": [
                        "Indigenous Indian Tradition: Purely Trabeate—using vertical pillars, stone lintels, horizontal beams, bracketed corbelling, and flat/pyramidal roofs without mortar.",
                        "Islamic Tradition: Arcuate—using true radiating voussoir arches, barrel vaults, squinches, and swelling spherical domes held together by lime-and-surkhi mortar.",
                        "Syncretic Fusion: Indigenous Indian artisans employed by Muslim rulers integrated both systems: e.g., in the Tomb of Iltutmish, an Indian corbelled arch supports a squinch dome; Akbar's Fatehpur Sikri extensively uses stone pillar-and-beam trabeate halls (Panch Mahal) crowned by Islamic chhatris."
                    ]},
                    {"heading": "Ornamentation: Geometric Arabesques and Indigenous Motifs", "points": [
                        "Islamic law (Sharia) forbade anthropomorphic and animal iconography in sacred buildings, introducing Calligraphy (Quranic inscriptions), Geometric patterns, and Arabesques (intertwined floral stalks).",
                        "Indian stonemasons seamlessly blended sacred indigenous decorative motifs: the Kalasha (water pitcher finial), Purna-ghata, inverted Lotus petals, bells and chains, and serpent brackets into mosques and tombs."
                    ]},
                    {"heading": "Novel Architectural Typologies", "points": [
                        "Introduced new architectural typologies: Minarets (e.g., Qutub Minar), colossal double-domed mausoleums (Humayun's Tomb, Taj Mahal), stepwells with arches, Public Caravanserais, and formal Persian Charbagh walled gardens."
                    ]}
                ],
                "diagramMapIdea": "Architectural fusion sketch: Islamic Arcuate Dome + Indian Pillar Bracket + Lotus/Kalasha finial + Arabesque calligraphy on red sandstone facade.",
                "conclusion": "Indo-Islamic architecture was an authentic civilizational synthesis: foreign concepts of space and geometry realized through the unmatched chisel, stone mastery, and aesthetic sensitivity of native Indian craftsmen."
            }
        }
    ]

    # Add remaining 30 Art & Culture questions (mains_art_006 to mains_art_035)
    art_30 = [
        ("mains_art_006", "mughal-empire", 15, 250, True, "UPSC CSE 2019 GS-1", "Nitin Singhania, Ch. 3; NCERT Class 11",
         "Compare and contrast the Rajasthani and Pahari schools of miniature painting in terms of themes, colour palettes, and emotional expression.",
         "Emerging as regional counterparts and offshoots of the Mughal atelier, the Rajasthani and Pahari schools expressed pure indigenous devotion (Vaishnavite Bhakti) through lyricism and saturated colours.",
         [("Thematic Core: Courtly Feudalism vs Romantic Devotion", ["Rajasthani (Mewar, Bundi, Kishangarh, Kota): Centered on courtly valor, royal hunting (Shikar in Kota), Ragamala (musical modes depicted visually), Barahmasa (seasonal moods), and Krishna-Radha romance.", "Pahari (Basohli, Kangra, Guler): Sublimely romantic and pastoral; inspired by Jayadeva's Gita Govinda, Bihari Satsai, and Bhagavata Purana, celebrating Krishna in lush Himalayan valleys."]),
          ("Colour Palette and Stylistic Treatment", ["Rajasthani: Bold, fiery, primary mineral pigments (vivid reds, ochre yellows, lapis blues); strong, heavy black outlines.", "Pahari: Delicate, lyrical pastel shades (cool greens, tender pinks, sky blues); fine, sensitive, fluid lines depicting poetic melancholy."]),
          ("Iconic Masterpieces", ["Rajasthani (Kishangarh): Nihal Chand's 'Bani Thani'—depicting Radha with sharp elongated doe-eyes, arched eyebrows, pointed chin, and transparent odhni (hailed as India's Mona Lisa).", "Pahari (Basohli & Kangra): Basohli's fiery passion with beetle-wing jewel inlays; Kangra's serene, tender depiction of feminine beauty and idyllic nature."])],
         "Comparative matrix: Theme, Palette, Lines, Human anatomy, and Landscape treatment across Rajasthani vs Pahari schools.",
         "While Rajasthani painting expressed robust aristocratic vitality, Pahari painting captured the tender, romantic soul of devotional lyricism in Himalayan nature."),

        ("mains_art_007", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 4; CCRT",
         "Folk paintings of India are living archives of regional ecology, tribal folklore, and communal rituals. Discuss with reference to Madhubani, Warli, and Pattachitra.",
         "India's vibrant folk and tribal painting traditions represent continuous grassroots ritual art practiced predominantly by women and rural communities.",
         [("Madhubani Painting (Mithila, Bihar)", ["Practiced traditionally by women on mud walls during weddings and festivals (Kohbar Ghar) using bamboo twigs and rice paste.", "Features: Two-dimensional flat figures with bulging fish-eyes and double-line borders; themes include Radha-Krishna, Rama-Sita, sun, moon, and sacred plants (Tulsi, bamboo/fertility). Uses natural plant dyes."]),
          ("Warli Painting (Maharashtra)", ["Tribal mural art of the Warli Adivasis using simple basic geometric shapes (circle for sun/moon, triangle for mountains/trees, square for sacred enclosure).", "White pigment made from chewed rice paste on red ochre mud walls; depicts everyday tribal life: hunting, fishing, farming, and the central circular Tarpa dance celebrating community harmony."]),
          ("Pattachitra (Odisha and West Bengal)", ["Narrative scroll painting executed on treated cotton cloth ('Patta') coated with chalk and tamarind gum.", "Depicts Lord Jagannath, Balabhadra, Subhadra, and Krishna Leela with rich crimson, yellow, and black vegetable pigments, sealed with natural lacquer."])],
         "Visual stylistic comparison sketch: Madhubani double-line fish-eye figure vs Warli stick-figure geometric Tarpa dance circle.",
         "Indian folk paintings embody sustainable vernacular heritage, turning organic rural materials into timeless sacred storytelling."),

        ("mains_art_008", "ancient-art", 15, 250, True, "UPSC CSE 2016 GS-1", "Nitin Singhania, Ch. 5; Natyashastra",
         "Classical Indian dances are rooted in the aesthetic theory of Bharata Muni's Natyashastra. Explain the concepts of Nritta, Nritya, and Natya, and the theory of 'Rasa'.",
         "Formulated in the ancient treatise 'Natyashastra' (the Fifth Veda), classical Indian performing arts are structured around profound aesthetic, dramatic, and emotional canons.",
         [("The Tripartite Division of Dance", ["1. Nritta: Pure, abstract rhythmic movement without any emotional expressiveness or narrative story; focuses on rhythmic footwork (Tala) and sculptural poses (Karanas).", "2. Nritya: Expressive dance communicating emotional themes and lyrics through facial expressions ('Abhinaya') and symbolic hand gestures ('Mudras').", "3. Natya: Dramatic theatrical performance incorporating dialogue, mime, costumes, and full narrative enactment."]),
          ("The Four Aspects of Abhinaya (Expressive Technique)", ["Angika (physical body movement), Vachika (voice/song), Aharya (costumes/makeup), and Sattvika (authentic inner emotional state)."]),
          ("The Theory of 'Rasa' (Aesthetic Taste / Emotional Climax)", ["Bharata Muni's iconic aphorism: 'Vibhava-Anubhava-Vyabhichari-Samyogad Rasa-Nishpattih' (Rasa is produced through the conjunction of causes, manifestations, and transient feelings).", "The Eight Primary Rasas (later expanded to Nine - 'Navarasa'): Shringara (Love/Beauty), Hasya (Comic), Karuna (Compassion/Grief), Raudra (Anger), Vira (Heroism), Bhayanaka (Terror), Bibhatsa (Disgust), Adbhuta (Wonder), and Shanta (Peace/Equanimity)."])],
         "Flowchart of Rasa realization: Sthayi Bhava (Permanent Emotion) + Vibhava (Stimulus) + Anubhava (Physical response) -> Supreme Aesthetic Experience (Rasa).",
         "The Natyashastra transformed performing dance from mere sensual entertainment into a sacred spiritual discipline aimed at liberating the human soul into divine bliss."),

        ("mains_art_009", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 6; CCRT",
         "Differentiate between the Hindustani and Carnatic classical music traditions with respect to origin, improvisation, and structural conventions.",
         "While rooted in the common Vedic tradition of Samavedic chanting, Indian classical music bifurcated into two great traditions around the 13th-14th centuries CE.",
         [("Geographic Realm and Historical Influences", ["Hindustani: Flourished in North India, deeply influenced by Persian, Central Asian, and Sufi syncretic idioms through court patronage (Amir Khusrau, Tansen).", "Carnatic: Flourished in South India, developed largely along purely indigenous lines in Hindu temple environments, relatively insulated from Persian courtly influences."]),
          ("Improvisation vs Compositional Rigour", ["Hindustani: Places paramount emphasis on spontaneous, extensive melodic improvisation ('Alap', 'Taan', 'Bandish') within a Raga framework. Ragas are strictly associated with specific times of day and seasons.", "Carnatic: More structurally rigid and composition-centric ('Kriti' format pioneered by the Trinity: Tyagaraja, Muthuswami Dikshitar, Syama Sastri). Less bound by strict time-of-day conventions."]),
          ("Vocal and Instrumental Styles", ["Hindustani: Major vocal styles: Dhrupad, Khayal, Thumri, Dadra, Tarana. Major instruments: Sitar, Sarod, Santoor, Tabla.", "Carnatic: Structured around Pallavi, Anupallavi, and Charanam. Major instruments: Veena, Mridangam, Ghatam, Kanjira, Violin."])],
         "Comparative table: Hindustani vs Carnatic across Heritage, Improvisation freedom, Time association, Trinity/Masters, and Instruments.",
         "Both traditions represent the twin melodic peaks of Indian civilization: Hindustani achieving spontaneous contemplative lyricism, and Carnatic achieving sublime mathematical and devotional perfection."),

        ("mains_art_010", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 8; CCRT",
         "Puppetry in India is an ancient multimedia art combining sculpture, painting, music, and dramatic storytelling. Discuss the four major traditional forms of Indian puppetry.",
         "Mentioned in ancient texts like the Mahabharata, Silappadikaram, and Ashokan edicts, traditional Indian puppetry is categorized into four distinctive technical forms.",
         [("1. String Puppets (Marionettes)", ["Kathputli of Rajasthan: Carved from a single piece of wood, dressed in vibrant medieval Rajasthani ghagras, operated by strings attached to the puppeteer's fingers who produces squeaks using a bamboo reed ('Boli').", "Other examples: Kundhei (Odisha), Gombeyatta (Karnataka), Bommalattam (Tamil Nadu - hybrid string-rod)."]),
          ("2. Shadow Puppets (Flat Leather Figures)", ["Togalu Gombeyaata (Karnataka) and Tholu Bommalata (Andhra Pradesh): Translucent flat puppets made of treated animal hide, painted with vegetable dyes, projected against a backlit white cloth screen.", "Depicts epic battles of the Ramayana and Mahabharata."]),
          ("3. Rod Puppets", ["Putul Nach (West Bengal) and Yampuri (Bihar): Large wooden puppets controlled from below via wooden rods and strings concealed in hollow bamboo tubes."]),
          ("4. Glove Puppets", ["Pavakoothu (Kerala): Influenced by Kathakali dance costumes and facial makeup; puppeteer manipulates the head with the index finger and arms with thumb and third finger."])],
         "Schematic classification chart showing 4 types of Indian Puppetry: String (Kathputli), Shadow (Tholu Bommalata), Rod (Putul Nach), and Glove (Pavakoothu).",
         "Traditional puppetry is an invaluable community art form that democratized epic literature and moral education for illiterate rural audiences across millennia."),

        ("mains_art_011", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 11; Ministry of Culture",
         "Examine the cultural, martial, and historical significance of traditional Indian martial arts, with special reference to Kalaripayattu and Thang-Ta.",
         "Traditional Indian martial arts originated as physical self-defense, combat conditioning, and ritual spiritual training deeply integrated into indigenous regional cultures.",
         [("Kalaripayattu of Kerala: Mother of Martial Arts", ["Regarded as one of the oldest surviving fighting systems in the world, practiced in a dedicated pit gym called 'Kalari'.", "Combines yogic postures, animal-inspired strikes (lion, serpent, elephant), pressure point strikes ('Marma Sastra'), and weaponry (Urumi - flexible double-edged whip-sword, staff, shield).", "Legends trace Bodhidharma transmitting Kalari movements to Shaolin Temple in China, giving birth to Shaolin Kung Fu."]),
          ("Thang-Ta of Manipur (Huyen Langlon)", ["Traditional weapon-based martial art of the Meitei community: 'Thang' means sword, 'Ta' means spear.", "Practiced in three forms: purely ritualistic, dynamic demonstration dance, and lethal combat warfare; deeply intertwined with Tantric Meitei cosmological beliefs."]),
          ("Other Prominent Regional Martial Forms", ["Silambam (Tamil Nadu: bamboo staff fencing); Gatka (Punjab: Sikh martial art using sticks and shields practiced during festivals); Mallakhamb (Maharashtra: pole acrobatics developing core stamina)."])],
         "Map locator of Indian Martial Arts: Kalaripayattu (Kerala), Silambam (Tamil Nadu), Thang-Ta (Manipur), Gatka (Punjab), Mallakhamb (Maharashtra).",
         "Traditional martial arts embody a holistic philosophy: cultivating mental stillness, physical grace, and ethical self-restraint alongside formidable martial competence."),

        ("mains_art_012", "ancient-art", 15, 250, True, "UPSC CSE 2020 GS-1", "Nitin Singhania; UNESCO Guidelines",
         "UNESCO's Intangible Cultural Heritage (ICH) list protects living community traditions rather than dead stone monuments. Discuss India's representations and challenges of preservation.",
         "Adopted in 2003, the UNESCO Convention for the Safeguarding of the Intangible Cultural Heritage recognizes oral traditions, performing arts, social practices, rituals, and traditional craftsmanship.",
         [("India's Diverse Elements on the UNESCO Representative List", ["1. Sacred Oral & Ritual Chanting: Tradition of Vedic Chanting (2008) - immutable phonetics preserved for three millennia; Buddhist Chanting of Ladakh (2012).", "2. Theatrical Performances: Koodiyattam (Sanskrit temple theatre of Kerala), Ramlila (festive performance of the Ramayana), Mudiyettu (ritual theatre of Kerala).", "3. Folk Performing Arts: Kalbelia folk songs and dances (Rajasthan), Chhau dance (Odisha/Jharkhand/Bengal mask dance), Sankirtana of Manipur (ritual singing and drumming).", "4. Craftsmanship: Traditional brass and copper craft of utensil making among Thatheras of Jandiala Guru (Punjab).", "5. Living Mass Festivals & Philosophies: Kumbh Mela (world's largest peaceful pilgrimage), Yoga, Nowruz, and Durga Puja of Kolkata (2021)."]),
          ("Contemporary Challenges in Safeguarding Intangible Heritage", ["Rapid urban commercialization and Westernization eroding generational oral transmission from Guru to Shishya.", "Poverty and precarious economic livelihoods of traditional artisans, folk dancers, and folk performers.", "Sensationalist mass media displacing indigenous storytelling and local village gatherings."]),
          ("Way Forward for Sustainable Preservation", ["Digital documentation and archiving by Sangeet Natak Akademi and Indira Gandhi National Centre for the Arts (IGNCA).", "Integrating traditional folk arts into school curricula and providing direct pensionary and livelihood support to master practitioners."])],
         "Mind map of India's UNESCO ICH elements: Oral traditions (Vedic chanting) + Theatre (Koodiyattam, Ramlila) + Folk Arts (Chhau, Kalbelia) + Crafts (Thatheras) + Festivals (Kumbh, Durga Puja).",
         "Safeguarding intangible cultural heritage ensures that India's civilizational memory continues to breathe and inspire in the hearts of living communities."),

        ("mains_art_013", "ancient-art", 10, 150, True, "UPSC CSE 2013 GS-1", "Upinder Singh; Nitin Singhania",
         "Coins in ancient India were not merely commercial instruments of trade, but invaluable mirrors of political legitimacy, metallurgy, and artistic expression. Elucidate.",
         "Numismatics provides one of the most reliable, chronological, and culturally rich archives for reconstructing ancient and medieval Indian history.",
         [("Punch-Marked Coins (c. 6th-3rd c. BCE): Birth of Monetization", ["Silver and copper ingots stamped with distinct punched symbols (sun, tree-in-railing, crescent-on-hill, animals) without royal portraits or inscriptions.", "Reflected the rise of trade guilds (Shrenis) and early territorial statehood (Mahajanapadas and Mauryas)."]),
          ("Indo-Greek Coins (c. 2nd c. BCE): Revolution in Portraiture", ["Introduced die-cast round coinage with realistic royal portraits, dynamic Greek deities, and bilingual legends (Greek and Kharosthi).", "Established the tradition of dating and attributing coins to specific historic monarchs."]),
          ("Gupta Gold Coins (Dinaras): Zenith of Artistic and Cultural Splendour", ["Exhibited the highest metallurgical purity and artistic elegance: depicted monarchs performing Vedic horse sacrifices (Ashvamedha coins), slaying tigers/lions, and playing the Veena (Samudragupta).", "Reflected royal hobbies, religious leanings (Vaishnavite Garuda emblems), and courtly aesthetic sophistication."]),
          ("Numismatic Decay as Economic Indicator", ["The debasement of gold coins and proliferation of cowrie shells in the Late Gupta and Post-Gupta era indicated economic contraction, decline in foreign trade, and creeping feudalization."])],
         "Timeline of Numismatic Evolution: Punch-Marked (Symbols) -> Indo-Greek (Portraits & Bilingual legends) -> Kushana (Gold Dinaras) -> Gupta (Artistic masterpiece coins) -> Cowrie shells (Feudal decay).",
         "Ancient Indian coinage stands as a luminous historical ledger: recording royal triumphs, religious piety, metallurgical ingenuity, and macroeconomic fortunes."),

        ("mains_art_014", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 2; Percy Brown",
         "Sun Temples in India represent a unique architectural and astronomical synthesis. Discuss with special reference to Konark and Modhera.",
         "Dedicated to Surya (the Sun God), ancient Indian sun temples were engineered as astronomical calculators aligned with the solar equinoxes and cosmic cycles.",
         [("1. Sun Temple at Konark (Odisha - 'Black Pagoda')", ["Built in the 13th century by Eastern Ganga monarch Narasimhadeva I on the Bay of Bengal coast.", "Conceived as a colossal stone chariot of Surya: mounted on 24 intricately sculpted stone wheels (representing the 24 fortnights of the year) pulled by 7 galloping horses (representing the 7 days of the week or 7 rays of sunlight).", "Each wheel functions as an accurate sundial, allowing precise calculation of time down to minutes by observing the shadow cast on the spoke carvings."]),
          ("2. Sun Temple at Modhera (Gujarat)", ["Constructed in 1026 CE under the Solanki ruler Bhima I on the Tropic of Cancer.", "Astute Solar Alignment: Sanctum was engineered such that during the Vernal and Autumnal Equinoxes, the first rays of the rising sun shone directly upon the diamond-studded crown of the central Surya idol.", "Surya Kund: Magnificent subterranean stepped water tank featuring 108 miniature shrines arrayed in geometric terraced steps."])],
         "Sun Temple Konark Chariot sketch: Colossal wheel sundial with detailed hub and 8 major spokes.",
         "Sun temples exemplify the sublime union of Hindu cosmology, scientific solar observation, and breathtaking structural stone engineering."),

        ("mains_art_015", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 2; Upinder Singh",
         "The Dilwara Temples at Mount Abu and the Gommateshwara statue at Shravanabelagola represent two contrasting pinnacles of Jain artistic devotion. Discuss.",
         "Jain sacred art reflects a dual aesthetic: the sheer transcendent austerity of self-liberation and the exuberant, delicate marble ornamentation of devotional gratitude.",
         [("Gommateshwara (Bahubali) at Shravanabelagola (Karnataka)", ["Commissioned in 981 CE by Chavundaraya, military commander of Western Ganga king Rachamalla.", "World's tallest free-standing monolithic stone statue (57 feet tall) carved out of a single granite outcrop on Vindhyagiri hill.", "Depicts Bahubali standing in 'Kayotsarga' (renunciation meditation) posture: completely naked (Digambara), with climbing forest vines wrapping around his legs and ant-hills at his feet, embodying absolute detachment from the physical body.", "Venue of the twelve-yearly 'Mahamastakabhisheka' ceremony."]),
          ("Dilwara Temples at Mount Abu (Rajasthan)", ["Built by Solanki ministers Vimal Shah and Vastupala-Tejpala between the 11th and 13th centuries CE.", "A masterpiece of white marble stone filigree: interior ceilings, pillars, and arches are carved so thinly that the translucent marble resembles hanging lace chandeliers.", "Vimal Vasahi and Luna Vasahi temples depict Jain Tirthankaras, Vidyadevis, and celestial dancers."])],
         "Comparative balance: Gommateshwara (Granite Monolith, Absolute Austerity, Kayotsarga detachment) vs Dilwara (Marble Filigree, Breathtaking Intricate Exuberance).",
         "Whether through the monumental granite austerity of Bahubali or the ethereal marble filigree of Dilwara, Jain art achieved timeless peaks of spiritual devotion.")
    ]

    for item in art_30:
        items.append({
            "id": item[0],
            "category": "art-culture",
            "categoryLabel": "Art & Culture",
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

    # Additional 15 questions to reach 35 Art & Culture
    art_15 = [
        ("mains_art_016", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 1",
         "Analyze the metallurgical mastery exhibited in the Iron Pillar of Mehrauli and the Sultanganj Copper Buddha.",
         "Ancient Indian metallurgy possessed sophisticated chemical knowledge of alloys, casting, and corrosion resistance.",
         [("The Iron Pillar of Mehrauli (Delhi)", ["Forged during the Gupta period (inscribed with eulogy of King Chandra, Chandragupta II).", "Weighs over 6 tonnes of wrought iron (99.7% pure) and has stood exposed to monsoons and heat for over 1,600 years without rusting.", "Scientific reason: Formation of a passive protective surface film of crystalline iron hydrogen phosphate ('Misawite') caused by high phosphorus and absence of sulfur/manganese in ancient charcoal blast furnaces."]),
          ("The Sultanganj Copper Buddha (Bihar)", ["Discovered in 1861, dating to the 5th-7th century CE (now in Birmingham Museum).", "Over 2 meters high, weighing nearly a tonne; cast using the lost-wax technique, exhibiting seamless anatomical fluidity and translucent drapery."])],
         "Scientific diagram of Misawite protective layer preventing rust on Mehrauli Iron Pillar.",
         "These artefacts demonstrate that ancient India was at the forefront of global metallurgical science and casting technology."),

        ("mains_art_017", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 2",
         "The rock-cut caves of the Western Ghats (Karle, Bhaja, Kanheri) reflect the prosperity of early Buddhist monasticism along trade routes. Elucidate.",
         "Excavated into the Sahyadri mountains of Maharashtra along the ancient trade highway (Dakshinapatha), these rock caves were thriving monastic complexes.",
         [("Strategic Location along Pass Corridors (Ghats)", ["Situated along Bhor Ghat and Thal Ghat linking the fertile Deccan plateau with booming western ports (Kalyan, Sopara, Chaul).", "Monasteries functioned as rest-houses, banks, and storage depots for wealthy merchant caravans."]),
          ("The Great Chaitya of Karle", ["The largest and finest rock-cut Buddhist prayer hall in India (excavated in 1st c. BCE - 1st c. CE).", "Features a massive sun-window arch (Horseshoe Chaitya arch) illuminating the monolithic stupa within, fluted pillars with kneeling elephant-rider capitals, and intact teak wood vault ribs."]),
          ("Kanheri Caves (Sanjay Gandhi National Park)", ["Hosts over 100 caves exhibiting continuous habitation from 1st c. BCE to 10th c. CE, featuring advanced rock-cut rainwater cisterns."])],
         "Cross-section sketch of Karle Great Chaitya: Sun window arch, peristyle pillared aisle, and rock-cut stupa sanctum.",
         "These rock-cut shrines demonstrate how spiritual detachment and vibrant commercial trade coexisted symbiotically in ancient India."),

        ("mains_art_018", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 2",
         "Terracotta temples of Bishnupur (Bengal) represent a brilliant regional architectural response to the absence of building stone. Discuss.",
         "Constructed under the Malla kings in the Bankura district of West Bengal (17th-18th c. CE), the Bishnupur temples transformed common alluvial clay into sublime architectural poetry.",
         [("Ecological Adaptation: Mud and Terracotta", ["Bengal's alluvial delta lacked hard building stone; architects baked alluvial soil into durable burnt-brick structures.", "Clad exteriors in thousands of finely carved terracotta relief plaques depicting Ramayana, Mahabharata, and Krishna Leela narratives."]),
          ("The Chala Architectural Style", ["Derived structural profiles from local bamboo-and-thatch rural huts with drooping curved eaves: 'Do-Chala' (two-roofed), 'Char-Chala' (four-roofed), and 'At-Chala' (eight-roofed).", "Masterpieces: Rasmancha (pyramidal stepped brick pavilion), Jor-Bangla (twin joined hut style), and Shyam Rai temple (Pancha-Ratna five spires)."])],
         "Architectural sketch of Bengal Jor-Bangla temple with curved thatched-style eaves.",
         "Bishnupur's terracotta temples prove that great architecture arises from organic harmony with local ecology and vernacular traditions."),

        ("mains_art_019", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 3",
         "Analyze the distinctive features of the Kangra School of painting. How did it capture the spirit of Vaishnava lyricism?",
         "Flourishing in the late 18th century under the patronage of Raja Sansar Chand of Kangra, the Kangra school represents the pinnacle of lyrical elegance in Indian art.",
         [("Thematic Lyricism: Gita Govinda and Bhagavata Purana", ["Expressed the ecstatic devotion of Vaishnavism, portraying the divine romance of Radha and Krishna amidst verdant Himalayan meadows."]),
          ("Aesthetic Features and Feminine Grace", ["Characterized by delicate facial contours, graceful straight noses, arched eyebrows, and transparent soft drapery.", "Delicate, cool colour palette derived from natural minerals: soothing greens, soft blues, and pastel pinks."]),
          ("Poetic Integration of Nature", ["Nature is not a passive backdrop, but a sympathetic participant reflecting human emotions: blooming creepers, drifting monsoon clouds, and rolling rivers."])],
         "Painting sketch: Radha and Krishna sheltering under a single umbrella from monsoon rain in a lush Kangra valley.",
         "Kangra painting is pure visual poetry: a sublime synthesis of feminine beauty, spiritual devotion, and Himalayan natural splendour."),

        ("mains_art_020", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 12",
         "Bhakti literature in regional vernaculars democratized spiritual philosophy and catalyzed linguistic identity. Discuss with examples.",
         "The medieval Bhakti revolution broke the monopoly of Sanskrit, producing masterworks in the languages spoken by common people.",
         [("Vernacularization of the Epics", ["Kamban composed the 'Ramavataram' (Kamba Ramayanam) in Tamil; Krittibas Ojha composed the Bengali Ramayan.", "Goswami Tulsidas composed the 'Ramcharitmanas' in Awadhi, transforming the epic into a household scripture across northern India."]),
          ("Social Emancipation and Subaltern Voices", ["Sant Ravidas composed radical anti-caste verses in Hindi envisioning 'Begumpura' (the City without Sorrow).", "Mirabai expressed fierce bridal mysticism towards Krishna in Rajasthani Braj, defying royal patriarchal subjugation."]),
          ("Foundational Role in Regional Languages", ["Shankaradeva laid the foundation of modern Assamese; Jnaneshwar pioneered Marathi literature; Sarala Das birthed Odia literature."])],
         "Linguistic tree diagram: Sanskrit Root -> Regional Branches (Awadhi: Tulsidas, Tamil: Kamban, Marathi: Jnaneshwar, Assamese: Shankaradeva).",
         "Bhakti vernacular literature was a democratic cultural awakening, empowering ordinary people to commune directly with the divine in their mother tongues.")
    ]

    for item in art_15:
        items.append({
            "id": item[0],
            "category": "art-culture",
            "categoryLabel": "Art & Culture",
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

    # Additional 15 questions to reach exactly 35 items (mains_art_021 to mains_art_035)
    art_final_15 = [
        ("mains_art_021", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 2",
         "Examine the architectural and religious features of the Hoysala temples at Belur, Halebidu, and Somnathpur.",
         "Constructed under the Hoysala dynasty in southern Karnataka (11th-14th c. CE), Hoysala temples represent the zenith of the hybrid Vesara style.",
         [("Stellate (Star-Shaped) Ground Plan", ["Temples are built on elevated star-shaped stone platforms ('Jagati') that provide a generous circumambulatory path around multiple projecting angles."]),
          ("Soft Soapstone (Chloritic Schist) Filigree", ["Constructed out of soft soapstone that allows extremely fine, deep, undercut chiselling before hardening on exposure to air.", "Exteriors are lined with horizontal sculptural friezes running around the base: elephants (stability), lions (courage), horses (speed), floral scrolls, and epic narratives."]),
          ("Masterpieces", ["Chennakeshava Temple at Belur: Renowned for its bracket figures of celestial maidens (Madanikas / Salabhanjikas) in exquisite dance poses.", "Hoysaleshwara Temple at Halebidu: Double-shrine temple displaying unsurpassed sculptural density."])],
         "Star-shaped stellate floor plan diagram of Hoysaleshwara temple with multi-angled sanctums.",
         "Hoysala temples are sculpted jewels of stone, where architecture became a vehicle for virtuoso sculptural craftsmanship."),

        ("mains_art_022", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 2",
         "The Gol Gumbaz at Vijayapura (Bijapur) is a triumph of medieval structural engineering. Analyze its acoustic and architectural features.",
         "Built in 1656 as the mausoleum of Muhammad Adil Shah, the Gol Gumbaz in Karnataka features the second-largest circular dome in the pre-modern world (after the Pantheon in Rome).",
         [("Monumental Single-Span Dome without Central Pillars", ["Colossal hemispherical dome with an external diameter of 44 meters, spanning an uninterrupted cubic hall without a single interior pillar.", "Structural Secret: Intersecting squinch arches arranged in an eight-pointed star distribute the dome's colossal downward thrust onto the massive 10-foot thick masonry walls."]),
          ("The Whispering Gallery: Acoustic Marvel", ["A circular gallery running around the interior base of the dome at a height of 100 feet.", "A faint whisper or rustle of paper made against the wall is heard clearly on the diametrically opposite side, and any sound echoes 10 to 12 times."]),
          ("Corner Octagonal Towers", ["Flanked by four seven-storeyed octagonal minaret towers with winding interior staircases."])],
         "Cutaway architectural section of Gol Gumbaz showing intersecting squinch arches supporting the dome and the Whispering Gallery.",
         "The Gol Gumbaz represents a miraculous marriage of structural mathematics, acoustic engineering, and monumental Deccan Sultanate architecture."),

        ("mains_art_023", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 7",
         "Trace the evolution of Sanskrit drama from Bhasa to Kalidasa, highlighting its dramatic conventions.",
         "Classical Sanskrit theatre ('Natya') was an elite courtly art form governed by the strict dramatic rules of the Natyashastra.",
         [("Key Conventions of Sanskrit Theatre", ["Absence of Tragedy: Classical Sanskrit plays never end in tragedy; they conclude with auspicious reconciliation ('Bharata Vakya') to restore cosmic moral order ('Dharma').", "Linguistic Bifurcation: High-status male characters (kings, Brahmins) speak refined Sanskrit, while women, lower castes, and children speak colloquial Prakrit.", "The Vidushaka: The comic royal companion (always a gluttonous Brahmin) who speaks truth to power through satire."]),
          ("Bhasa: The Pioneer Playwright (c. 3rd c. CE)", ["Authored 13 plays discovered by T. Ganapati Sastri, notably 'Svapnavasavadatta' and 'Urubhanga' (the only play where a hero, Duryodhana, dies on stage)."]),
          ("Kalidasa: The Immortal Dramatist (5th c. CE)", ["Master of dramatic lyricism: 'Abhijnanashakuntalam' (celebrating Shakuntala's love, abandonment, and reunion with Dushyanta), praised globally by Goethe.", "'Malavikagnimitram' and 'Vikramorvasiyam'."]),
          ("Sudraka and Vishakhadatta", ["Sudraka's 'Mrichchhakatika' (The Little Clay Cart): A rare secular realistic play featuring a poor Brahmin merchant Charudatta and courtesan Vasantasena.", "Vishakhadatta's 'Mudrarakshasa': Political thriller without female lead or romantic songs, detailing Chanakya's ruthless espionage against the Nanda minister Rakshasa."])],
         "Chronological table of Sanskrit dramatists, major works, linguistic traits, and core themes.",
         "Classical Sanskrit drama achieved unmatched psychological nuance, combining poetic lyricism with profound moral philosophy."),

        ("mains_art_024", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 8",
         "Traditional Indian puppetry faces severe decline in the modern digital era. Discuss its cultural significance and strategies for revitalization.",
         "Indian puppetry is an endangered traditional performing art threatened by modern digital entertainment, television, and changing village leisure patterns.",
         [("Cultural Value Beyond Entertainment", ["Educational and Social Medium: Traditionally communicated health messages, moral values, and mythic lore to illiterate rural audiences.", "Integration of Folk Crafts: Supports rural artisans who carve wood, stitch costumes, and manufacture natural vegetable dyes."]),
          ("Reasons for Decline", ["Loss of traditional royal and temple patronage.", "Younger generations of hereditary puppeteers abandoning the craft for casual urban labour due to abysmal incomes.", "Inability to compete with smartphones and cinema."]),
          ("Revitalization Strategies", ["Utilizing puppetry in government awareness campaigns (Swachh Bharat, health immunization, girl-child education).", "Creating modern puppet theatre repertoires addressing contemporary social issues like climate change and corruption.", "Promoting puppet festivals and institutional support through Sangeet Natak Akademi."])],
         "Flowchart: Traditional Puppetry -> Digital Competition & Poverty -> Modern Adaptation & Government Campaigns -> Cultural Revival.",
         "Puppetry must be nurtured not as an obsolete museum curiosity, but as a dynamic living medium of popular communication and cultural education."),

        ("mains_art_025", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 9",
         "Examine the architectural and cultural significance of the stepwells ('Baolis' and 'Vavs') of western India, with special reference to Rani ki Vav.",
         "Stepwells (Baolis in North India, Vavs in Gujarat) are unique subterranean architectural structures that combined hydraulic water management with social and religious sanctuaries.",
         [("Engineering and Climate Function", ["Designed in arid Gujarat and Rajasthan to harvest scarce rainwater and tap deep groundwater aquifers amidst scorching summer heat.", "Subterranean levels provided a natural cooling sanctuary for travelers, pilgrims, and local women."]),
          ("Rani ki Vav at Patan (UNESCO World Heritage Site)", ["Constructed in 1063 CE by Queen Udayamati in memory of King Bhima I of the Solanki dynasty.", "Designed as an inverted underground temple with seven descending terraced pillared storeys.", "Adorned with over 500 major stone sculptures of supreme artistic refinement, dedicated to Lord Vishnu and his Dashavataras (including Sheshashayi Vishnu, Varaha, Vamana)."]),
          ("Social Space for Women", ["Functioned as vital daily social meeting places for village women, who gathered to fetch water, socialize, and worship away from patriarchal scrutiny."])],
         "Cross-section architectural elevation of Rani ki Vav showing descending subterranean storeys and stepped water shaft.",
         "Stepwells represent ancient India's supreme ecological wisdom: transforming functional water conservation into underground temples of transcendent beauty."),

        ("mains_art_026", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 10",
         "Discuss the history, classification, and significance of Indian classical and folk music instruments.",
         "Bharata Muni's Natyashastra formulated the scientific four-fold classification of Indian musical instruments ('Vadya') thousands of years before modern European musicology.",
         [("The Four-Fold Classification of Instruments", ["1. Tata Vadya (Chordophones / Stringed Instruments): Sound produced by vibrating strings (e.g., Veena, Sitar, Sarod, Tambura, Santoor).", "2. Sushira Vadya (Aerophones / Wind Instruments): Sound produced by blowing air into columns (e.g., Bansuri/Flute, Shehnai, Nadaswaram, Pungi).", "3. Avanaddha Vadya (Membranophones / Percussion with skin heads): Sound produced by striking stretched animal parchment (e.g., Mridangam, Tabla, Pakhawaj, Dholak).", "4. Ghana Vadya (Idiophones / Solid Instruments): Sound produced by striking solid resonant metal or wood without membranes (e.g., Manjira, Ghatam, Jal Tarang, Kartal)."]),
          ("Cultural and Spiritual Role", ["Instruments are deified in Indian culture: Veena with Saraswati, Bansuri with Krishna, Damaru with Shiva, Mridangam with Ganesha, reflecting the sanctity of music as a vehicle to God."])],
         "Four-quadrant taxonomy diagram of Indian Musical Instruments: Tata (Strings), Sushira (Wind), Avanaddha (Percussion), Ghana (Solid).",
         "Indian musical instruments represent a timeless acoustic science, producing infinite microscopic microtones ('Shrutis') that mirror human emotion."),

        ("mains_art_027", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 13",
         "Analyze the socio-religious impact of the Chaitanya movement and Gaudiya Vaishnavism on the cultural life of eastern India.",
         "Initiated by Chaitanya Mahaprabhu (1486-1534) in Nadia (Navadvipa, Bengal), Gaudiya Vaishnavism transformed eastern India through emotional communal devotion.",
         [("Nagar-Sankirtana: Democratization of Sacred Worship", ["Popularized 'Nagar-Sankirtana'—congregational public chanting and ecstatic dancing in city streets to the accompaniment of Khol (clay drum) and Kartal (cymbals).", "Broke all caste barriers: welcomed untouchables, Muslims (Haridas Thakur was made the 'Namacharya'), and women into spiritual congregations."]),
          ("Philosophical Core: Achintya Bhedabheda", ["Propounded the philosophy of 'Achintya Bhedabheda' (Inconceivable simultaneous oneness and difference between the soul and God), synthesizing monism and dualism."]),
          ("Cultural Impact on Manipuri Dance and Literature", ["Inspired the classical Manipuri dance traditions (Manipuri Raslila), which are inscribed on UNESCO's Intangible Cultural Heritage list.", "Sparked a massive renaissance in Bengali devotional poetry (Padavali) and biographical literature (Chaitanya Charitamrita by Krishnadasa Kaviraja)."])],
         "Flowchart: Chaitanya's Nadia movement -> Nagar-Sankirtana -> Caste abolition -> Achintya Bhedabheda -> Cultural flowering of Manipuri Raslila.",
         "Chaitanya Mahaprabhu transformed religion from dry scholasticism into an ocean of universal love, democratizing spirituality across eastern India."),

        ("mains_art_028", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 14",
         "The Shekhawati region of Rajasthan is known as the 'Open-Air Art Gallery' of India. Discuss its haveli architecture and fresco paintings.",
         "Located in north-eastern Rajasthan, Shekhawati's ornate merchant mansions ('Havelis') constructed between 1830 and 1930 represent a unique confluence of Marwari wealth, traditional frescoes, and British colonial influences.",
         [("Architectural Layout of Havelis", ["Multi-storeyed mansions arranged around central courtyards (Chowks) ensuring privacy for women (Zenana) and business for men (Mardana).", "Features: Ornate carved wooden doorways, overhanging balconies ('Jharokhas'), and delicate sandstone latticework ('Jalis') for natural air ventilation in desert heat."]),
          ("Fresco Paintings on Lime Plaster ('Arayish')", ["Executed using the 'Fresco-Buono' technique on wet lime plaster using natural vegetable and mineral pigments.", "Eclectic Imagery: Religious mythologies (Krishna Leela, Rama) side-by-side with modern British colonial curiosities: steam locomotives, motorcars, gramophones, aeroplanes, and British soldiers with cigars."])],
         "Sketch of Shekhawati Haveli facade showing carved Jharokha balconies and vibrant wall frescoes.",
         "Shekhawati havelis stand as vibrant visual archives documenting the fascinating cultural encounter between traditional Marwari feudalism and emerging Western modernity."),

        ("mains_art_029", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 15",
         "Examine the cultural, ecological, and craft significance of Dokra metal casting and Sohrai Khovar tribal painting in eastern India.",
         "Jharkhand and adjoining tribal belts host ancient living crafts rooted in ecological intimacy and animistic spirituality.",
         [("Dokra Metal Craft (Dhokra)", ["An ancient non-ferrous bell-metal casting using the Lost-Wax technique ('Cire Perdue'), dating back directly to the Harappan Dancing Girl (4,500 years old).", "Practiced by the Dhokra Damar tribes of Jharkhand, West Bengal, and Odisha.", "Features: Rustic, primitive, elongated figures with twisted brass wire surfaces depicting folk deities, musicians, horses, and wild animals."]),
          ("Sohrai and Khovar Tribal Art (Jharkhand - GI Tagged)", ["Khovar: Mural art painted by tribal women during the wedding season, using natural black manganese and white kaolin clay layers scratched with broken combs.", "Sohrai: Harvest art painted during winter to celebrate cattle and agriculture, featuring bold, dynamic animal forms (spotted deer, peacocks, bulls)."])],
         "Process flowchart: Dokra Lost-Wax casting: Clay core -> Wax model -> Outer clay mould -> Molten brass pour -> Chiselled metal sculpture.",
         "These indigenous arts are living links to prehistoric creative traditions, demonstrating that tribal heritage is the primeval root of Indian artistic culture."),

        ("mains_art_030", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 16",
         "The Antiquities and Art Treasures Act 1972 is the legal bulwark for protecting Indian cultural heritage. Discuss its provisions and challenges in repatriating stolen antiquities.",
         "Centuries of colonial plunder and modern illicit smuggling syndicates have drained India of thousands of sacred idols and manuscripts. The Antiquities and Art Treasures Act 1972 is India's principal statutory framework for cultural property protection.",
         [("Key Provisions of the 1972 Act", ["Defines an 'Antiquity' as any coin, sculpture, painting, or object of art that has been in existence for not less than 100 years (and manuscripts older than 75 years).", "Mandates compulsory registration of designated antiquities with the Archaeological Survey of India (ASI).", "Prohibits the export of any antiquity except by the Central Government or its authorized agencies."]),
          ("Challenges in Enforcement and Repatriation", ["Lack of a comprehensive national digital database / inventory of temple idols, making it difficult to prove theft in foreign courts.", "Inadequate penalties under the 1972 Act compared to the multi-million dollar global black market.", "Proving provenance under the UNESCO 1970 Convention on Illicit Import, Export and Transfer of Ownership of Cultural Property requires concrete police FIRs and photographic records."]),
          ("Recent Successes in Repatriation", ["Over 300 stolen antiquities (including Chola bronzes, Yakshis, and stone statues) have been successfully repatriated from museums and collectors in USA, Australia, UK, and Germany."])],
         "Flowchart: Temple theft -> Illicit international smuggling -> Provenance investigation by ASI/Interpol -> Diplomatic repatriation to India.",
         "Protecting antiquities is not merely a legal duty, but a sacred national responsibility to restore stolen civilizational dignity to the soil of India.")
    ]

    for item in art_final_15:
        items.append({
            "id": item[0],
            "category": "art-culture",
            "categoryLabel": "Art & Culture",
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

    art_extra_5 = [
        ("mains_art_031", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 3; NCERT Class 11 Fine Arts",
         "The ritual floor painting traditions of India—such as Kolam, Rangoli, and Kalamezhuthu—serve not merely as decorative art, but as profound expressions of sacred geometry, ecology, and hospitality. Elaborate.",
         "Ritual floor drawings represent an ephemeral, living folk art created daily by women at home thresholds and temple courtyards across India.",
         [("Sacred Geometry and Threshold Sanctification", ["Kolam (Tamil Nadu) and Muggulu (Andhra Pradesh): Geometrical patterns drawn with rice flour around a grid of dots (Chitti), embodying cosmic harmony, symmetry, and warding off negative energies.", "Mandana (Rajasthan) and Aipan (Uttarakhand): Drawn using natural red ochre (Geru) and white rice paste (Biswar), marking auspicious rites of passage."]),
          ("Ecological Dimension: Food for Living Beings", ["Drawn with edible rice flour rather than chemical dyes, serving as 'Bhuta Yajna'—an offering of food to ants, birds, and small insects, symbolizing unconditional hospitality to nature."]),
          ("Kalamezhuthu of Kerala (Temple Floor Painting)", ["Executed on temple sanctum floors using 5 natural colored powders (rice-white, turmeric-yellow, charcoal-black, leaf-green, lime-chilli red) depicting fierce deities (Bhadrakali, Ayyappan), and erased in ritual ecstasy at the conclusion of worship."])],
         "Geometric matrix sketch of dot grid Kolam evolving into infinite interlocking loops.",
         "These threshold arts transform humble everyday domestic spaces into sacred cosmic realms while honoring the ecological interconnectedness of life."),

        ("mains_art_032", "ancient-art", 15, 250, True, "UPSC CSE 2016 GS-1", "Nitin Singhania, Ch. 2; Upinder Singh",
         "Subterranean stepwells (Baolis and Vavs) of Western India transformed functional water conservation structures into magnificent inverted temples. Analyze with reference to Rani ki Vav and Chand Baori.",
         "In the arid and semi-arid landscapes of Gujarat and Rajasthan, stepwells (known as Vavs or Baolis) evolved from simple water storage pits into monumental multi-tiered subterranean architectural wonders.",
         [("Functional and Climatic Ingenuity", ["Engineered to reach deep subterranean water tables and trap seasonal monsoon runoff in dry zones.", "Subterranean micro-climate: Temperature inside stepwells remains 5-6°C cooler than the blistering desert surface, providing a refreshing retreat for travellers and community gatherings."]),
          ("Rani ki Vav at Patan, Gujarat (UNESCO World Heritage Site)", ["Constructed in 1063 CE by Queen Udayamati in memory of Chaulukya monarch Bhima I on the banks of the Saraswati River.", "Designed as an 'Inverted Temple' celebrating the sanctity of water: descends through seven pillared terraced levels featuring over 500 major sculptural reliefs.", "Iconographic masterwork: Celebrates Lord Vishnu in all ten Dashavataras, Sheshashayi Vishnu (sleeping on cosmic serpent Ananta at water level), and stunning dancing Apsaras."]),
          ("Chand Baori at Abhaneri, Rajasthan", ["Built by King Chanda of the Nikumbha dynasty in the 9th century CE; one of the deepest and largest stepwells in the world.", "Geometric Maze: 3,500 narrow steps arranged in 13 meticulously symmetrical terraced flights descending 30 meters into the earth, juxtaposed against a multi-storeyed royal pavilion with carved jharokhas."])],
         "Architectural cross-section of 7-tiered inverted stepwell (Rani ki Vav) descending to water reservoir.",
         "Vavs represent a sublime civilizational ethos where resource conservation was elevated into a divine artistic sacrament, preserving life and beauty simultaneously."),

        ("mains_art_033", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 6; NCERT Class 11",
         "Discuss the structural and acoustic classification of traditional Indian musical instruments as expounded in Bharata's Natyashastra. How does it reflect the organological sophistication of ancient India?",
         "Bharata Muni's ancient dramaturgical treatise, the Natyashastra (c. 2nd c. BCE - 2nd c. CE), formulated a pioneering quadripartite taxonomy of musical instruments (Vadya) based on physical acoustic principles.",
         [("The Fourfold Organological Classification (Vadya)", ["1. Tata Vadya (Chordophones / Stringed): Sound produced by vibrating strings; e.g., Saraswati Veena, Rudra Veena, Sitar, Sarod, Ektara. Divided into plucked and bowed categories.", "2. Sushira Vadya (Aerophones / Wind): Sound produced by vibrating columns of air blown through tubes; e.g., Bansuri (bamboo flute), Shehnai, Nadaswaram, Shankha (conch).", "3. Avanaddha Vadya (Membranophones / Percussion): Sound produced by striking stretched animal parchment across hollow resonators; e.g., Mridangam, Tabla, Pakhawaj, Dholak.", "4. Ghana Vadya (Idiophones / Solid): Non-membranous solid instruments producing sound through resonant striking; e.g., Manjira (cymbals), Ghatam (clay pot), Jaltarang (water bowls), Kartal."]),
          ("Global Precedence and Scientific Sophistication", ["Bharata's acoustic taxonomy anticipated modern Western organology (the 1914 Hornbostel-Sachs system) by two millennia, establishing precise tonal pitches (Shrutis) and harmonics."])],
         "Classification wheel of Indian musical instruments: Tata (Strings), Sushira (Wind), Avanaddha (Drums), Ghana (Solid resonant).",
         "The Natyashastra's taxonomy underscores that ancient Indian musicology was grounded in rigorous acoustic physics and scientific experimentation."),

        ("mains_art_034", "ancient-art", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 2; Upinder Singh",
         "Himalayan Buddhist monastic architecture seamlessly blends Tibetan artistic traditions with indigenous Himalayan stone and timber engineering. Examine with reference to Tabo, Alchi, and Tawang monasteries.",
         "Perched on high-altitude trans-Himalayan cliffs, Buddhist Gompas (monasteries) developed unique structural and visual vocabularies responding to extreme mountain seismic environments and Vajrayana cosmology.",
         [("Architectural Characteristics of Gompas", ["Sturdy masonry of sun-dried mud bricks, dressed mountain rubble stone, and interlocking wooden beams (Kath-Kuni seismic resistance).", "Flat roofs, inward-sloping fortress walls, brightly painted wooden window lintels, and gold-leaf pinnacles (Dhwaja and Dharmachakra) on sanctuary roofs."]),
          ("Key Himalayan Monastic Centres", ["Tabo Monastery (Spiti Valley, Himachal Pradesh): Founded in 996 CE ('Ajanta of the Himalayas'); houses 9 mud-brick temples preserving intact 10th-century stucco sculptures of the Vajradhatu Mandala and exquisite wall murals.", "Alchi Monastery (Ladakh): Founded by translator Rinchen Zangpo (11th century); exhibits rare Kashmiri-Gandharan artistic synthesis in its Sumtseg (three-storeyed temple) with carved wooden pillars and miniature textile paintings.", "Tawang Monastery (Arunachal Pradesh): Second largest monastery in the world; a multi-storey fortress-like gompa of the Gelugpa order perched at 10,000 feet, housing an 8-meter gilded Buddha statue and precious Kangyur manuscripts."])],
         "Spatial sketch of Trans-Himalayan Gompa: Stepped fortress structure, prayer wheel corridor, and central prayer assembly hall (Dukhang).",
         "Himalayan monasteries stand as resilient bastions of Mahayana-Vajrayana culture, harmonizing spiritual elevation with formidable alpine topography."),

        ("mains_art_035", "modern-india", 10, 150, False, "Standard Practice", "Nitin Singhania, Ch. 12; Bipan Chandra",
         "Examine how Indian theatre and early cinema served as potent instruments of anti-colonial resistance and social reform during the national movement, with special reference to IPTA.",
         "From the mid-19th century through independence, Indian performing arts transformed from courtly entertainment into grassroots weapons of anti-imperial mobilization and socio-economic critique.",
         [("Colonial Repression and Early Political Theatre", ["Dinabandhu Mitra's play 'Nil Darpan' (1860) exposed the brutal exploitation of indigo farmers, triggering massive peasant mobilization in Bengal.", "Dramatic Performances Act (1876): British enacted draconian censorship to ban any theatrical performance deemed 'seditious' or critical of British rule."]),
          ("Indian People's Theatre Association (IPTA - 1943)", ["Formed in the backdrop of the Bengal Famine of 1943 and World War II by leftist writers and cultural activists (Bijon Bhattacharya, K.A. Abbas, Salil Chowdhury).", "Landmark Play 'Nabanna' (1944): Staged realistic peasant suffering during the artificial Bengal Famine, abandoning Victorian melodrama for raw socio-economic realism.", "Songs, street theatre, and folk forms (Jatra, Burrakatha) mobilized peasants and factory workers across rural and urban India."]),
          ("Early Cinema as National Allegory", ["Silent and early talkie cinema (Dadasaheb Phalke's 'Raja Harishchandra' 1913; 'Sant Tukaram' 1936) subtly projected indigenous civilizational pride, moral resilience, and national unity under the guise of mythological and devotional allegories."])],
         "Timeline: 1860 (Nil Darpan) -> 1876 (Dramatic Performances Act) -> 1913 (Early National Cinema) -> 1943 (IPTA & Nabanna).",
         "Cultural resistance in theatre and cinema democratized the freedom struggle, ensuring the message of Swaraj permeated the deepest emotional consciousness of the masses.")
    ]

    for item in art_extra_5:
        items.append({
            "id": item[0],
            "category": "art-culture",
            "categoryLabel": "Art & Culture",
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
    art = get_art_culture_mains()
    print(f"Generated {len(art)} Art & Culture Mains questions ({art[0]['id']} to {art[-1]['id']})")
    with open('data/batch_mains_art_culture.json', 'w', encoding='utf8') as f:
        json.dump(art, f, indent=2, ensure_ascii=False)
