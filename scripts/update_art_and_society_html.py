import re

# 1. Update art-culture.html
with open('art-culture.html', 'r', encoding='utf-8') as f:
    ac = f.read()

# Update banner to include Ishani Pandya & A.L. Basham
ac = ac.replace(
    '• <strong>Kapila Vatsyayan</strong> (Classical Indian Dance in Literature &amp; the Arts)',
    '• <strong>Kapila Vatsyayan</strong> (Classical Indian Dance in Literature &amp; the Arts) &bull;\n          • <strong>Ishani Pandya</strong> (Visual Art, Architecture, Paintings &amp; Performing Arts Compendiums)'
)

# Insert new culture cards into CULTURE_DATA
new_culture_items = '''  {
    id: 'sculptural-schools',
    category: 'art-forms',
    type: 'Sculpture',
    title: 'Ancient Sculptural Schools: Gandhara, Mathura & Amaravati',
    era: '1st c. BCE – 4th c. CE (Kushana & Satavahana Periods)',
    subtitle: 'Greco-Roman Synthesis vs. Indigenous Spiritual Realism & Narrative Reliefs',
    desc: 'The Post-Mauryan and Kushana period witnessed the revolutionary anthropomorphic depiction of the Buddha across three great sculptural schools, each distinguished by local stones, aesthetic philosophies, drapery treatments, and patron dynasties.',
    features: [
      'Gandhara School (NW Frontier, Taxila, Bamiyan): Greco-Roman Hellenistic synthesis; grey/bluish schist stone and stucco; Apollo-like realistic facial anatomy, wavy curly hair, sharp nose, muscular torso, heavy toga-like drapery with realistic deep folds, Buddha shown in yogic dhyana with gentle calm.',
      'Mathura School (Uttar Pradesh): Purely indigenous Indian style; spotted red sandstone; Buddha depicted with shaved head, right hand in Abhaya Mudra, broad masculine shoulders, transparent light drapery clinging to body, smiling tranquil countenance; pioneered simultaneous iconography of Hindu deities (Vishnu, Shiva, Surya) and Jain Ayagapatas.',
      'Amaravati School (Andhra Pradesh, Krishna-Godavari Basin): White crystalline marble/limestone; patronized by Satavahanas and Ikshvakus; master of dynamic narrative relief panels on stupas rather than isolated icons; figures depicted in lively, ecstatic movement, elongated limbs, and dramatic Tribhanga postures capturing Jataka stories.'
    ],
    upscFact: 'UPSC Elimination Trap: Gandhara art was heavily influenced by foreign Hellenistic techniques, but its theme was almost exclusively Buddhist; Mathura art was fully indigenous and secularly pan-religious (Buddhist, Jain, and Brahmanical).',
    timelineRef: 'post-mauryan-period',
    bookRef: 'Ishani Pandya L1; Nitin Singhania, Ch. 1; NCERT Fine Arts Ch. 3'
  },
  {
    id: 'cave-architecture',
    category: 'architecture',
    type: 'Cave Architecture',
    title: 'Cave Architecture of India: Chaityas, Viharas & Monolithic Excavations',
    era: '3rd c. BCE – 10th c. CE',
    subtitle: 'From Barabar Rock-Cut Caves to the Grandeur of Ellora Kailash Temple',
    desc: 'Indian rock-cut architecture evolved from simple excavated retreats for heterodox ascetics into colossal multi-storeyed prayer halls (Chaityas) with barrel-vaulted apses, residential monastic cloisters (Viharas), and the pinnacle of monolithic subterranean carving at Kailashnath.',
    features: [
      'Barabar Caves (Bihar, 3rd c. BCE): Excavated by Emperor Ashoka and grandson Dasharatha for Ajivika ascetics; celebrated for mirror-like interior wall polish; Lomas Rishi cave showcases the earliest ornamental horseshoe Chaitya arch carved in live rock.',
      'Western Ghats Buddhist Caves (Maharashtra): Karle (largest rock-cut Chaitya hall with 37-meter depth, soaring wooden vault ribs, and Mithuna sculpted couples), Bhaja, Kanheri (over 100 caves near Mumbai), Bedsa, and Nasik Pandavleni.',
      'Ajanta Caves (Maharashtra): 29 Buddhist rock-cut caves spanning Hinayana and Mahayana phases; combines rock carving with breathtaking tempera mural paintings illustrating Jataka narratives.',
      'Ellora Caves (Maharashtra): 34 caves representing religious harmony (12 Buddhist, 17 Hindu, 5 Jain); zenith represented by Cave 16: The Kailash Temple (carved top-to-bottom from a single basaltic cliff under Rashtrakuta King Krishna I, excavating 200,000 tonnes of rock without mortar or pillars).',
      'Elephanta Caves (Mumbai Harbor): 6th-8th c. Shaivite monolithic caves featuring the colossal 20-foot high Trimurti (Sadashiva) depicting the three faces of the Divine: Creator (Vamadeva/Uma), Preserver (Tatpurusha), and Destroyer (Aghora/Bhairava).'
    ],
    upscFact: 'UPSC Trap: Chaityas are congregational prayer halls containing a stupa at the rear apse; Viharas are residential quadrangular dwelling cells for monks with a central hall and verandah.',
    timelineRef: 'gupta-age',
    bookRef: 'Ishani Pandya L2; Percy Brown; NCERT Class 11 Fine Arts Ch. 4'
  },
  {
    id: 'folk-tribal-paintings',
    category: 'art-forms',
    type: 'Paintings',
    title: 'Folk & Tribal Painting Traditions of India',
    era: 'Traditional Indigenous Heritage',
    subtitle: 'Madhubani, Warli, Pattachitra, Kalamkari, Phad, Pithora & Thangka',
    desc: 'Beyond classical imperial courts, Indian rural and tribal communities preserved extraordinary visual art forms passed down across generations, utilizing natural mineral and vegetable dyes, organic pastes, and handmade surfaces celebrating fertility, deities, and communal cosmos.',
    features: [
      'Madhubani / Mithila (Bihar): Practiced by women on mud walls and paper; distinct styles (Bharni, Katchni, Godna, Kohbar bridal chambers); natural pigments (lampblack, turmeric, flowers); bold double-line borders with fish, peacocks, and lotus flowers.',
      'Warli Painting (Maharashtra): Indigenous art of the Warli tribe; painted with white rice-paste and water/gum on red ochre mud walls; uses fundamental geometric symbols (circle representing sun/moon, triangle representing mountains/trees, square representing sacred space); iconic Tarpa dance spiral.',
      'Pattachitra (Odisha & Bengal): Traditional cloth-based scroll painting; depicted on treated cotton cloth using tamarind seed gum and mineral colors; celebrated for intricate borders and depictions of Lord Jagannath, Subhadra, and Balabhadra.',
      'Kalamkari (Andhra Pradesh): Pen-drawn textile art using bamboo reed (Kalam) and natural vegetable dyes; two famous sub-schools: Srikalahasti (temple hangings depicting mythological epics) and Machilipatnam (block-printed floral designs patronized by Golconda Sultans).',
      'Phad Painting (Rajasthan): Giant 30-foot scroll paintings on khadi cloth depicting the martial legends and folk miracles of local deities Pabuji and Devnarayan, recited at night by itinerant priest-singers (Bhopas) accompanied by the Ravanahatha musical instrument.',
      'Pithora (Gujarat & MP): Ritual wall painting of the Rathwa and Bhil tribes dedicated to Baba Pithora to invoke prosperity, characterized by sacred horses and vibrant animal motifs.',
      'Thangka Painting (Ladakh, Sikkim, Tibet): Buddhist scroll paintings on silk or cotton depicting Mandalas, Tara, and Arhats used as meditation aids in monasteries.'
    ],
    upscFact: 'UPSC Insight: Kalamkari uses purely organic vegetable dyes and milk mordants; in 2021, Karuppur Kalamkari paintings from Tamil Nadu also received the prestigious Geographical Indication (GI) tag.',
    timelineRef: 'kingdoms-of-south',
    bookRef: 'Ishani Pandya L3; Nitin Singhania, Ch. 2; CCRT Visual Arts'
  },
  {
    id: 'puppetry-traditions',
    category: 'art-forms',
    type: 'Puppetry',
    title: 'Traditional Puppetry Forms of India (4 Canonical Categories)',
    era: 'Ancient Natyashastra to Present Day',
    subtitle: 'String, Shadow, Rod & Glove Puppets Preserving Epic Oral Traditions',
    desc: 'Puppetry (Natya-Rupa) is one of India\'s most ancient folk performance mediums, mentioned in the Tamil epic Silappadikaram and Ashokan inscriptions. It synthesizes sculpture, painting, music, and oral storytelling across four distinct technical traditions.',
    features: [
      '1. String Puppets (Marionettes): Controlled by strings attached to puppet limbs. Kathputli of Rajasthan (carved from wood, dressed in vibrant ghagras, operated by Bhatt puppeteers with whistle sound); Kundhei of Odisha; Gombeyatta of Karnataka; Bommalattam of Tamil Nadu (unique hybrid combining strings and rods).',
      '2. Shadow Puppets: Flat leather puppets projected onto a backlit translucent screen. Togalu Gombeyaata of Karnataka (leather figures showing epic episodes); Tholu Bommalata of Andhra Pradesh (large colorful translucent deer/goat skin puppets); Ravanachhaya of Odisha (opaque deer-skin puppets creating silhouette shadows without joints).',
      '3. Rod Puppets: Operated by wooden rods from beneath the stage. Putul Nach of West Bengal (large, heavy marionettes on bamboo rods used in Jatra folk theatre); Yampuri of Bihar (wooden rod puppets portraying Yama and judgments in the underworld).',
      '4. Glove Puppets (Hand/Palm Puppets): Operated directly by fingers and thumbs. Pavakoothu of Kerala (carved wooden head with painted faces influenced by Kathakali makeup and headgear, performing episodes from Ramayana and Mahabharata).'
    ],
    upscFact: 'UPSC Prelims Match: Ravanachhaya (Odisha shadow puppet) uses uncolored, non-jointed skin puppets creating dramatic pure silhouettes, symbolizing the shadow of the demon king Ravana.',
    timelineRef: 'kingdoms-of-north',
    bookRef: 'Ishani Pandya L3; Nitin Singhania, Ch. 4; CCRT Performing Arts'
  },'''

ac = ac.replace('const CULTURE_DATA = [', 'const CULTURE_DATA = [\n' + new_culture_items)

with open('art-culture.html', 'w', encoding='utf-8') as f:
    f.write(ac)
print("Updated art-culture.html successfully!")


# 2. Update society.html
with open('society.html', 'r', encoding='utf-8') as f:
    soc = f.read()

# Update banner to include S.C. Dube
soc = soc.replace(
    '• <strong>Yogendra Singh</strong> (Modernization of Indian Tradition)',
    '• <strong>Yogendra Singh</strong> (Modernization of Indian Tradition) &bull;\n          • <strong>Prof. S.C. Dube</strong> (Indian Society, National Book Trust &bull; Village &amp; Tribal Structural Studies)'
)

# Insert new society card into SOCIETY_DATA
new_society_item = '''  {
    id: 'village-tribal-social-system',
    category: 'diversity',
    title: 'The Indian Village Community & Tribal Social Systems',
    subtitle: 'Structural Reality, Little & Great Traditions, Jajmani Ties, and Transformation (Prof. S.C. Dube Synthesis)',
    desc: 'The traditional Indian village and tribal communities represent the foundational social laboratories of Indian civilization. As analyzed by Prof. S.C. Dube in his landmark Shamirpet village study and classical sociology, the village was neither an isolated self-sufficient republic nor a stagnant fossil, but a dynamic web of caste interdependence, ritual hierarchies, and regional linkages.',
    dimensions: [
      {
        name: 'The Village as a Social System (Prof. S.C. Dube)',
        points: [
          'Deconstructing Colonial Myths: Colonial administrators (Charles Metcalfe) characterized Indian villages as immutable "little republics that last where nothing else lasts". S.C. Dube proved that Indian villages were deeply integrated into wider regional trading networks, pilgrimage circuits, and matrimonial alliances.',
          'Inter-Caste Interdependence (Jajmani System): Hereditary economic and ritual ties where landowning patron castes (Jajmans) received institutionalized services from artisan and service castes (Kamins/Prajas) paid in customary harvest shares rather than cash.',
          'Little Tradition vs Great Tradition (Robert Redfield & McKim Marriott): Constant interaction between local folk village customs (Little Tradition) and pan-Indian Sanskritic scriptural traditions (Great Tradition) through processes of Universalization and Parochialization.'
        ]
      },
      {
        name: 'Tribal Social Structure & Contemporary Dynamics',
        points: [
          'Geographical & Linguistic Zones: North-Eastern zone (Tibeto-Burman language family, matrilineal traits in Khasi/Garo); Central/Middle zone (Munda and Dravidian languages, Santhal, Gond, Bhil, Oraon); Southern zone (Dravidian, Toda, Kadar).',
          'Isolation vs Assimilation Historiographical Debate: Verrier Elwin advocated protection and tribal reserves (National Parks approach) to preserve tribal identity; G.S. Ghurye viewed tribes as "imperfectly integrated Hindus" (Backward Hindus) advocating assimilation; Jawaharlal Nehru formulated the Tribal Panchsheel (1958) promoting development along the lines of indigenous genius without cultural imposition.',
          'Contemporary Challenges: Land alienation, displacement due to mineral extraction and dam building, depletion of Minor Forest Produce (MFP), and the protective constitutional mechanisms of Fifth and Sixth Schedules paired with the Forest Rights Act (FRA 2006).'
        ]
      }
    ],
    upscAngle: 'Mains GS-1 Question Trend: Evaluates whether the Indian village community is disintegrating under market economy and democratic politics, or mutating into new assertive caste and class configurations.',
    dataPoint: '68.8% of India remains rural (2011 Census); Scheduled Tribes constitute 8.6% of India\'s population with 705 distinct ethnic groups.',
    bookRef: 'Prof. S.C. Dube, Indian Society (NBT); Ram Ahuja; NCERT Class 12 Indian Society Ch. 3'
  },'''

soc = soc.replace('const SOCIETY_DATA = [', 'const SOCIETY_DATA = [\n' + new_society_item)

with open('society.html', 'w', encoding='utf-8') as f:
    f.write(soc)
print("Updated society.html successfully!")
