# -*- coding: utf-8 -*-
"""
build_syllabus_page.py
Generates the comprehensive master syllabus and exam track guide (syllabus.html)
covering the full curriculum for UPSC CSE, UPPSC PCS, UP RO/ARO, RRB NTPC & Banking.
"""

import sys

content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Complete Examination Syllabus &amp; Master Study Guide — History, Art &amp; Culture | Complete History of India</title>
<meta name="description" content="Master examination syllabus and comprehensive study guide covering Ancient, Medieval, Modern, Post-Independence, World History, Art & Culture, UP Special, RO/ARO General Hindi, RRB NTPC, and Banking Awareness.">
<link rel="stylesheet" href="css/style.css">
  <!-- Google Analytics Tracking (G-B0Z2G21W4F) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-B0Z2G21W4F"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-B0Z2G21W4F');
  </script>

  <!-- Google AdSense -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>

<style>
/* Syllabus Hub Styles */
.syl-hero {
  padding: 56px 0 44px;
  background: linear-gradient(180deg, var(--bg-raised) 0%, var(--bg) 100%);
  border-bottom: 1px solid var(--line);
}
.syl-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 5px 14px;
  border-radius: 999px;
  background: var(--accent-tint);
  color: var(--accent-strong);
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 16px;
  border: 1px solid rgba(79, 111, 100, 0.25);
}
.syl-nav-strip {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding: 14px 0 16px;
  border-bottom: 2px solid var(--line-soft);
  margin-bottom: 32px;
  scrollbar-width: thin;
}
.syl-nav-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  background: var(--bg-sunken);
  border: 1px solid var(--line);
  border-radius: 6px;
  color: var(--ink);
  font-family: var(--font-body);
  font-size: 0.92rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s ease;
}
.syl-nav-btn:hover {
  background: var(--bg-raised);
  border-color: var(--accent);
  color: var(--accent-strong);
}
.syl-nav-btn.active {
  background: var(--accent-strong);
  color: #ffffff;
  border-color: var(--accent-strong);
  box-shadow: 0 2px 8px rgba(56, 80, 74, 0.25);
}
.syl-section-pane {
  display: none;
  animation: fadeIn 0.25s ease forwards;
}
.syl-section-pane.active {
  display: block;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

.syl-card {
  background: var(--bg-raised);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 26px 30px;
  margin-bottom: 28px;
  box-shadow: var(--shadow);
}
.syl-card-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}
.syl-card-title {
  font-family: var(--font-display);
  font-size: 1.5rem;
  margin: 0;
  color: var(--ink);
}
.syl-img-banner {
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid var(--line);
  margin: 18px 0;
  background: #000;
  max-height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.syl-img-banner img {
  width: 100%;
  height: 100%;
  max-height: 400px;
  object-fit: cover;
  display: block;
}
.syl-action-bar {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid var(--line-soft);
}
.syl-box-gold {
  background: var(--gold-tint);
  border-left: 4px solid var(--gold);
  padding: 14px 18px;
  border-radius: 0 6px 6px 0;
  margin: 16px 0;
  font-size: 0.94rem;
  color: #4a3511;
}
.syl-box-accent {
  background: var(--accent-tint);
  border-left: 4px solid var(--accent);
  padding: 14px 18px;
  border-radius: 0 6px 6px 0;
  margin: 16px 0;
  font-size: 0.94rem;
  color: #17362d;
}
.syl-box-seal {
  background: var(--seal-tint);
  border-left: 4px solid var(--seal);
  padding: 14px 18px;
  border-radius: 0 6px 6px 0;
  margin: 16px 0;
  font-size: 0.94rem;
  color: #4a1515;
}
</style>
</head>
<body>
<a href="#main" class="skip-link">Skip to content</a>
<nav class="site-nav" id="siteNav"></nav>

<main id="main">
  <div class="wrap"><div class="breadcrumb" id="breadcrumb"></div></div>

  <header class="syl-hero">
    <div class="wrap">
      <span class="syl-badge">📋 Master Examination Blueprint &amp; Syllabus Guide</span>
      <h1 style="font-size:clamp(2.2rem,4.8vw,3.4rem); line-height:1.15; margin:0 0 16px;">
        Complete Syllabus of <em>History, Art &amp; Culture</em>
      </h1>
      <p style="font-size:1.1rem; max-width:82ch; color:var(--ink-soft); line-height:1.6; margin:0 0 24px;">
        Designed from canonical academic textbooks and multi-commission syllabi — covering <strong>UPSC Civil Services</strong>, <strong>UPPSC Combined State Services (GS Paper 1 &amp; 5)</strong>, <strong>UP RO/ARO (Samiksha Adhikari)</strong>, <strong>Railway Recruitment Board (RRB NTPC)</strong>, and <strong>Banking Awareness (IBPS/SBI)</strong>. Includes historiographical perspectives, key terminology, authentic image exhibits, period mappings, and direct 1-click links to the <strong>8,425-Question Practice Hub</strong>.
      </p>

      <div class="hero-ctas" style="display:flex; gap:12px; flex-wrap:wrap; margin-bottom:28px;">
        <a href="practice.html" class="btn btn-primary">🎯 Practice Hub (8,425 Questions)</a>
        <a href="up-history.html" class="btn btn-outline">🏛️ Uttar Pradesh Special Hub</a>
        <a href="art-culture.html" class="btn btn-outline">🎨 Art &amp; Culture Deep Metrics</a>
        <a href="books.html" class="btn btn-outline">📚 27 Standard Textbooks</a>
      </div>

      <div class="stat-strip">
        <div class="stat"><span class="num">6</span><span class="lab">Core National Sections</span></div>
        <div class="stat"><span class="num">2</span><span class="lab">Specialized Exam Tracks</span></div>
        <div class="stat"><span class="num">8,160+</span><span class="lab">Prelims MCQs Available</span></div>
        <div class="stat"><span class="num">265+</span><span class="lab">Mains GS Model Frameworks</span></div>
        <div class="stat"><span class="num">100%</span><span class="lab">Syllabus Coverage</span></div>
      </div>
    </div>
  </header>

  <section class="section" style="padding-top:24px;">
    <div class="wrap">

      <!-- Navigation Strip -->
      <nav class="syl-nav-strip" aria-label="Syllabus Sections">
        <button class="syl-nav-btn active" onclick="switchSylTab('sec-ancient')">Section 1: Ancient History</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-medieval')">Section 2: Medieval History</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-modern')">Section 3: Modern History</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-post')">Section 4: Post-Independence</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-world')">Section 5: World History</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-culture')">Section 6: Art &amp; Culture</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-up')">Part A: UP Special &amp; RO/ARO</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-rrb-bank')">Part B: RRB NTPC &amp; Banking</button>
      </nav>

      <!-- =================================================================== -->
      <!-- SECTION 1: ANCIENT INDIAN HISTORY & ARCHAEOLOGY -->
      <!-- =================================================================== -->
      <div class="syl-section-pane active" id="sec-ancient">
        <div class="section-head">
          <span class="kicker">Section 1 • Deep Time to c. 1200 CE</span>
          <h2>Ancient Indian History &amp; Archaeology</h2>
        </div>

        <!-- 1. Sources & Historiography -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">1. Sources and Historiography</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Archaeological, Epigraphic, Numismatic &amp; Literary Foundations</p>
            </div>
            <span class="t-cat cat-ancient">Ancient Core</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/culture/pottery-chronology.jpg" alt="Archaeological Pottery Chronology">
          </div>
          <p>
            Historiographical understanding of ancient India relies on a cross-critical convergence of tangible material sources and textual corpora:
          </p>
          <ul>
            <li><strong>Archaeological Sources:</strong> Stratigraphic excavation methodologies (Sir Mortimer Wheeler's grid system, vertical vs. horizontal trenching). Epigraphy: decipherment of Ashokan Brahmi and Kharosthi by James Prinsep (1837); imperial prashastis (Harishena's Allahabad Pillar inscription, Ravikirti's Aihole inscription of Pulakeshin II). Numismatics: silver punch-marked coins (Pana) of Mauryas, Indo-Greek bilingual royal portraiture, Kushana pure gold dinaras, and Gupta dynastic gold coin debasement as an index of monetary contraction (R.S. Sharma model).</li>
            <li><strong>Literary Sources:</strong> Indigenous texts: Shruti (four Vedas, Brahmanas, Aranyakas, Upanishads) and Smriti (Vedangas, Epics, Puranas); Buddhist Tri-Pitakas (Sutta, Vinaya, Abhidhamma) and Jatakas; Jain Agamas; Classical Sanskrit treatises: Kalidasa (<em>Abhijnanashakuntalam</em>, <em>Meghaduta</em>), Bhasa (<em>Svapnavasavadatta</em>), and Harishena. Scientific treatises: Charaka Samhita (medicine), Sushruta Samhita (surgery), Aryabhatiya (astronomy/mathematics).</li>
            <li><strong>Foreign Travelers' Chronicles:</strong> Greek/Roman: Megasthenes (<em>Indica</em> - 7 castes, Pataliputra municipal committees), <em>Periplus of the Erythraean Sea</em> (maritime trade routes), Ptolemy (<em>Geography</em>); Chinese pilgrims: Faxian (Gupta tranquility), Xuanzang (Harsha's Kannauj/Prayag assemblies), Yijing (Nalanda pedagogy); Arab chronicles: Al-Biruni (<em>Kitab-ul-Hind</em> - 11th century social customs and astronomy).</li>
            <li><strong>Historiographical Schools:</strong> Colonial/Imperialist (James Mill's communal tri-partition: Hindu, Muslim, British; Vincent Smith); Nationalist (R.G. Bhandarkar, K.P. Jayaswal); Marxist (D.D. Kosambi's dialectical materialism, R.S. Sharma's Indian Feudalism); Subaltern (Ranajit Guha); Revisionist/Integrative (B.D. Chattopadhyaya).</li>
          </ul>
          <div class="syl-action-bar">
            <a href="period.html?id=prehistoric-age" class="btn btn-outline btn-sm">Explore Prehistoric Period →</a>
            <a href="practice.html?category=ancient" class="btn btn-primary btn-sm">Practice 1,517+ Ancient MCQs</a>
          </div>
        </div>

        <!-- 2. Prehistoric & Proto-Historic -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">2. Prehistoric and Proto-Historic Eras</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Palaeolithic, Mesolithic, Neolithic Revolution &amp; Chalcolithic Complexes</p>
            </div>
            <span class="t-cat cat-ancient">Prehistory</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/prehistory.png" alt="Prehistoric Age Infographic Sheet">
          </div>
          <ul>
            <li><strong>Palaeolithic Age (Pleistocene Epoch):</strong> Lower Palaeolithic (Soan Valley, Attirampakkam handaxes), Middle Palaeolithic (Nevasan flake-tool culture), Upper Palaeolithic (blade and burin tools; Bhimbetka rock shelters with earliest green and red hunting pigments; Hunsgi, Belan Valley).</li>
            <li><strong>Mesolithic Age (Holocene Transition):</strong> Microliths (trapezes, lunates, triangles); earliest animal domestication at <em>Bagor</em> (Rajasthan) and <em>Adamgarh</em> (Madhya Pradesh); semi-permanent settlements with burials at Sarai Nahar Rai and Mahadaha.</li>
            <li><strong>Neolithic Revolution (V. Gordon Childe):</strong> Emergence of food production, cattle pastoralism, and polished stone celts. Regional variations: Kashmir (Burzahom pit dwellings, dog burials); Belan Valley (Koldihwa, Chopani Mando); Middle Ganga (Lahuradewa rice); South India (Ashmounds at Utnur, Kupgal, Brahmagiri).</li>
            <li><strong>Chalcolithic Cultures:</strong> Copper-stone farming communities: Ahar-Banas (copper smelting, Gilund), Kayatha, Malwa (finest chalcolithic ceramics, Navdatoli), Jorwe (Daimabad bronze chariot, Inamgaon fortified settlement with adult burials aligned north-south).</li>
          </ul>
        </div>

        <!-- 3. Indus Valley Civilization -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">3. Indus Valley Civilization (IVC / Harappan Civilization)</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Urban Planning, Long-Distance Trade, Metallurgy &amp; Decline Hypotheses</p>
            </div>
            <span class="t-cat cat-ancient">Bronze Age Urbanization</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/indusvalley.png" alt="Indus Valley Civilization Infographic Sheet">
          </div>
          <ul>
            <li><strong>Chronology &amp; Extent:</strong> Early/Formative (Kot Diji, Amri), Mature (2600–1900 BCE), Late Harappan. Geographical spread: Sutkagendor (Makran coast, West) to Alamgirpur (Hindon river, East); Manda (Chenab, North) to Daimabad (Pravara, South); covering over 1 million sq km.</li>
            <li><strong>Urban Engineering:</strong> Dichotomy of Citadel (elevated mud-brick platform for public/administrative structures) and Lower Town (gridiron residential streets intersecting at right angles). Drainage: covered masonry wastewater drains with inspection sumps. Water engineering: Dholavira's cascading stone-cut reservoirs and bunds; Lothal's tidal dockyard and lock-gate mechanics.</li>
            <li><strong>Economy &amp; Trade:</strong> Steatite seals with unicorn, bull, and tiger motifs; long-distance maritime trade with Dilmun (Bahrain), Makan (Oman), and Meluhha (Mesopotamia - Akkad Sargon inscriptions mentioning ships from Meluhha). Bead factories at Chanhudaro and Lothal; standardized weights in binary and decimal fractions (1, 2, 4, 8, 16... 160, 320).</li>
            <li><strong>Religion &amp; De-Urbanization:</strong> Pashupati seal (Proto-Shiva surrounded by elephant, tiger, rhinoceros, buffalo, and deer beneath the throne), terracotta Mother Goddess figurines, phallic lingas, and tree worship. Decline theories: Mortimer Wheeler's Aryan invasion hypothesis (discredited) vs. modern palaeo-climatic models of monsoon shift, drying of the Ghaggar-Hakra / Saraswati river, and ecological degradation.</li>
          </ul>
          <div class="syl-action-bar">
            <a href="period.html?id=indus-valley-civilization" class="btn btn-outline btn-sm">Read Full IVC Period Page →</a>
            <a href="practice.html?category=ancient&exam=upsc" class="btn btn-primary btn-sm">Practice IVC Questions</a>
          </div>
        </div>

        <!-- 4. Vedic Period -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">4. The Vedic Period (c. 1500 – 600 BCE)</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Early Vedic Pastoralism to Later Vedic Agrarian Janapadas</p>
            </div>
            <span class="t-cat cat-ancient">Vedic Transition</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/vedic_age.png" alt="Vedic Age Infographic Sheet">
          </div>
          <ul>
            <li><strong>Early Vedic Age (Rigvedic c. 1500–1000 BCE):</strong> Sapta-Sindhu geographical horizon; pastoral economy where wealth was measured in cattle (Gau); tribal chieftainship (Rajan) checked by popular assemblies (<em>Sabha</em>, <em>Samiti</em>, <em>Vidatha</em>, <em>Gana</em>); flexible social stratification; high status of women (Upanayana investiture, Rishikas like Apala, Lopamudra, Ghosha); naturalistic polytheism (Indra, Agni, Varuna).</li>
            <li><strong>Later Vedic Age (c. 1000–600 BCE):</strong> Migration east into the Gangetic Doab (Kuru-Panchala territory); introduction of iron metallurgy (Ayas) enabling clearing of dense forests and deep ploughing; transformation of tribal chiefs into territorial monarchs (Janapadas); grand legitimizing sacrifices (Rajasuya, Ashvamedha, Vajapeya); atrophy of popular assemblies; rise of court bureaucracy (12 Ratnins); crystallization of the rigid four-fold Varna hierarchy, Gotra endogamy, and degradation of women and Shudras. Reaction leading to Upanishadic discourses on Atman and Brahman.</li>
          </ul>
        </div>

        <!-- 5. Mahajanapadas & Heterodox Movements -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">5. Mahajanapadas, Magadhan Hegemony &amp; Heterodox Faiths</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Second Urbanization, Magadha Imperialism, Buddhism, Jainism &amp; Ajivikas</p>
            </div>
            <span class="t-cat cat-ancient">6th Century BCE</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/age_of_mahajanpadas.png" alt="Age of Mahajanapadas Infographic Sheet">
          </div>
          <ul>
            <li><strong>Second Urbanization &amp; Magadha:</strong> Growth of 16 territorial states (Anguttara Nikaya); Monarchies vs. Oligarchic Republics (Ganasanghas like Vrijis and Mallas). Geostrategic ascendancy of Magadha: iron mines of Rajgir, fertile Gangetic alluvium, riverine transport, and military deployment of war elephants. Dynastic chronology: Haryankas (Bimbisara, Ajatashatru), Shishunagas, and Nandas (Mahapadma Nanda's imperial centralization). Persian conquest under Darius I and Macedonian invasion under Alexander (326 BCE).</li>
            <li><strong>Buddhism:</strong> Gautama Buddha; Four Noble Truths (Chatvari Arya Satyani), Eightfold Path (Ashtangika Marga), Pratityasamutpada (Dependent Origination), Nirvana. Four Buddhist Councils: 1st at Rajgir (483 BCE, Sutta/Vinaya Pitakas), 2nd at Vaishali (383 BCE, Theravada/Mahasanghika schism), 3rd at Pataliputra (250 BCE under Ashoka, Abhidhamma Pitaka), 4th at Kundalvana, Kashmir (72 CE under Kanishka, Mahayana vs. Hinayana division).</li>
            <li><strong>Jainism:</strong> 24 Tirthankaras from Rishabhanatha to Vardhamana Mahavira; philosophy of Anekantavada (multiplicity of viewpoints), Syadvada (relativity of truth), Triratna (Right Faith, Right Knowledge, Right Conduct), strict asceticism and radical Ahimsa. Split into Digambara (sky-clad) and Svetambara (white-clad).</li>
            <li><strong>Ajivikas &amp; Charvakas:</strong> Makkhali Gosala's fatalistic doctrine of Niyati (destiny beyond human control); Ajita Kesakambalin and Charvaka's Lokayata materialist philosophy rejecting Vedic afterlife.</li>
          </ul>
        </div>

        <!-- 6. Mauryan to Gupta Empires -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">6. Mauryas, Post-Mauryas &amp; The Gupta-Vakataka Classical Age</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Imperial Bureaucracy, Ashoka's Dhamma, Sangam Age &amp; Gupta Classicalism</p>
            </div>
            <span class="t-cat cat-ancient">Imperial Synthesis</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/mauryan_empire.png" alt="Mauryan Empire Infographic Sheet">
          </div>
          <ul>
            <li><strong>The Mauryan Empire (321–185 BCE):</strong> Founded by Chandragupta Maurya with Kautilya (Chanakya); Saptanga theory of state; centralized administrative bureaucracy (Samaharta, Sannidhata, Gudha Purushas); Megasthenes' description of Pataliputra's 6 municipal committees. Ashoka's transformation after the Kalinga War (261 BCE, Rock Edict XIII); concept of Dhamma (secular civic ethics propagated via Dhamma Mahamattas and Rock/Pillar edicts in Brahmi, Kharosthi, Aramaic, and Greek).</li>
            <li><strong>Post-Mauryan Confluences (200 BCE – 300 CE):</strong> Shungas (Pushyamitra Shunga, Patanjali), Satavahanas (Gautamiputra Satakarni, royal land grants, Karle and Kanheri rock-cut chaityas), Indo-Greeks (Menander, <em>Milinda Panha</em>), Shakas (Rudradaman I Junagadh Sanskrit inscription), Kushanas (Kanishka, Silk Route control, gold coinage, 4th Buddhist Council, Gandhara and Mathura art schools). Sangam Age in South India: Cheras, Cholas, Pandyas; Sangam anthologies (Ettutogai, Pattupattu) and epics (Silappadikaram); Tinai eco-zones; Roman maritime trade at Arikamedu.</li>
            <li><strong>Gupta Empire (319–550 CE) &amp; Vakatakas:</strong> Samudragupta's Digvijaya policy in the north and Grahana-Moksha-Anugraha in the south recorded in the Prayag Prashasti; Chandragupta II Vikramaditya eliminating the Western Shakas. Administrative tiers: Bhukti, Visaya, Vithi, Grama. Socio-economic: expansion of Agrahara land grants, proliferation of Jatis, untouchability. Cultural achievements in astronomy (Aryabhata, Varahamihira), medicine (Sushruta), Sanskrit drama (Kalidasa), and Ajanta cave paintings under Vakataka patronage.</li>
            <li><strong>Post-Gupta Transition &amp; Imperial Cholas:</strong> Harsha of Kannauj; Tripartite Struggle for Kannauj between Palas, Pratiharas, and Rashtrakutas. The Imperial Cholas (Rajaraja I, Rajendra I): naval expeditions to Southeast Asia (Srivijaya) and Sri Lanka; local self-government at Uttaramerur with democratic Kudavolai pot-lottery elections to village executive committees (Variyams).</li>
          </ul>
          <div class="syl-action-bar">
            <a href="period.html?id=gupta-age" class="btn btn-outline btn-sm">Explore Gupta Classical Age →</a>
            <a href="practice.html?category=ancient" class="btn btn-primary btn-sm">Practice 1,517+ Ancient Questions</a>
          </div>
        </div>
      </div>

      <!-- =================================================================== -->
      <!-- SECTION 2: MEDIEVAL INDIAN HISTORY -->
      <!-- =================================================================== -->
      <div class="syl-section-pane" id="sec-medieval">
        <div class="section-head">
          <span class="kicker">Section 2 • c. 750 – 1707 CE</span>
          <h2>Medieval Indian History</h2>
        </div>

        <!-- 1. Early Medieval & Delhi Sultanate -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">1. Early Medieval Transition &amp; The Delhi Sultanate (1206–1526 CE)</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Feudalism Debate, Turkish Invasions, Market Reforms &amp; Administrative Machinery</p>
            </div>
            <span class="t-cat cat-medieval">Delhi Sultanate</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/delhi_sultanate.png" alt="Delhi Sultanate Infographic Sheet">
          </div>
          <ul>
            <li><strong>Early Medieval India &amp; Invasions:</strong> The Indian Feudalism debate (R.S. Sharma vs. B.D. Chattopadhyaya); sub-infeudation of political authority and emergence of Rajput clans. Arab conquest of Sindh (712 CE, Muhammad bin Qasim); Mahmud of Ghazni's economic raids (sack of Somnath 1026 CE); Muhammad Ghori's campaigns (Battles of Tarain 1191 and 1192 CE); structural factors for the defeat of fragmented Rajput polities.</li>
            <li><strong>Mamluk / Slave Dynasty (1206–1290 CE):</strong> Qutbuddin Aibak (Lakhbaksh, Qutb Minar foundation); Iltutmish (consolidation, introduction of silver Tanka and copper Jital, institutionalization of Iqta system, Turkan-i-Chahalgani corps of forty); Razia Sultan (gender dilemmas in medieval Islamic polity); Ghiyasuddin Balban (divine theory of kingship, Niyabat-i-Khudai, Zill-i-Ilahi, court etiquette of Sajda and Paibos, destruction of the Forty, blood-and-iron policy).</li>
            <li><strong>The Khalji Centralization (1290–1320 CE):</strong> Alauddin Khalji's military and fiscal reforms: standing royal army paid in cash, Dag (horse branding) and Chehra (descriptive rolls). Comprehensive Market Control System: price fixation of essential foodgrains and textiles, separate markets (Sarai-i-Adl), market inspectors (Shahna-i-Mandi, Barid, Munhiyan), state grain warehouses, land measurement (Masahat) and revenue demand at 50% of gross produce.</li>
            <li><strong>The Tughlaqs &amp; Lodis:</strong> Muhammad bin Tughlaq's controversial experimental projects: capital transfer to Daulatabad (1327), copper-brass token currency, Khurasan and Qarachil military expeditions, agricultural loan system (Sondhar), and agrarian ministry (Diwan-i-Kohi). Firoz Shah Tughlaq: extensive canal irrigation networks (Yamuna and Sutlej canals), welfare state initiatives, factory workshops (Karkhanas), imposition of Jizya as an autonomous tax. Lodis: Sikandar Lodi's foundation of Agra (1504) and Afghan tribal egalitarian monarchy.</li>
            <li><strong>Sultanate Administrative Framework:</strong> Four central pillars: Diwan-i-Wizarat (finance/prime minister), Diwan-i-Arz (military administration under Ariz-i-Mamalik), Diwan-i-Insha (state correspondence), and Diwan-i-Rasalat (religious/foreign affairs). Evolution of Iqta tenures from transferable revenue assignments into hereditary landed claims.</li>
          </ul>
        </div>

        <!-- 2. Vijayanagara, Bahmanis & Regional Kingdoms -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">2. Regional Dynasties: Vijayanagara Empire &amp; Deccan Sultanates</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Nayankara System, Hydraulic Engineering &amp; Battle of Talikota (1565)</p>
            </div>
            <span class="t-cat cat-medieval">Deccan Kingdoms</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/vijayanagara_empire.png" alt="Vijayanagara Empire Infographic Sheet">
          </div>
          <ul>
            <li><strong>Vijayanagara Empire (1336–1646 CE):</strong> Founded on the Tungabhadra river by Harihara and Bukka (Sangama dynasty) under the inspiration of sage Vidyaranya; four dynasties: Sangama, Saluva, Tuluva, and Aravidu. Peak under Sri Krishnadeva Raya (Tuluva dynasty): patron of literature (composed Telugu masterpiece <em>Amuktamalyada</em>, patronized Ashtadiggajas including Tenali Rama), naval trade with Portuguese for Arabian horses.</li>
            <li><strong>Administrative &amp; Hydraulic Mechanics:</strong> <em>Nayankara System</em>: military commanders (Amara-Nayakas) assigned revenue tracts (Amara) in exchange for maintaining troops and paying tribute; <em>Ayagar System</em> in village administration (12 hereditary village functionaries). Sophisticated hydraulic infrastructure in semi-arid Hampi: Kamalapuram Tank, Hiriya Canal, boulder anicuts on Tungabhadra. Accounts of foreign visitors: Nicolo de Conti, Abdur Razzaq, Domingos Paes, and Fernao Nuniz.</li>
            <li><strong>Bahmani Kingdom &amp; The Five Deccan Sultanates:</strong> Founded by Alauddin Hasan Bahman Shah (1347 CE); administrative genius of Prime Minister Mahmud Gawan; fragmentation into five sultanates: Bijapur (Adil Shahi), Golconda (Qutb Shahi), Ahmadnagar (Nizam Shahi), Bidar (Barid Shahi), and Berar (Imad Shahi). Battle of Talikota / Bannihatti / Rakshasi-Tangadi (1565 CE): confederacy of Deccan sultanates routed Vijayanagara, sacking the capital city of Hampi.</li>
          </ul>
        </div>

        <!-- 3. Mughal Empire & Marathas -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">3. The Mughal Empire (1526–1707 CE) &amp; Maratha Swarajya</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Babur, Sher Shah, Akbar's Institutional Innovations &amp; Shivaji's Ashta Pradhan</p>
            </div>
            <span class="t-cat cat-medieval">Mughals &amp; Marathas</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/akbar_the_great.png" alt="Akbar the Great Infographic Sheet">
          </div>
          <ul>
            <li><strong>Mughal Foundation &amp; Sur Interregnum:</strong> Babur's military innovations: gunpowder artillery and Tulughma flanking battle arrays (First Battle of Panipat 1526, Khanwa 1527). Sher Shah Suri (1540–1545 CE): administrative genius who introduced standard land survey (Rai system), silver <em>Rupiya</em> currency, and highway infrastructure (Sadak-e-Azam / Grand Trunk Road) with Sarais.</li>
            <li><strong>Akbar's Institutional Foundations (1556–1605 CE):</strong>
              <ul>
                <li><strong>Mansabdari System:</strong> Dual rank system: <em>Zat</em> (personal status and salary tier) and <em>Sawar</em> (cavalry quota required to be maintained); later modified with Du-aspa Sih-aspa under Jahangir.</li>
                <li><strong>Todar Mal's Bandobast / Dahsala System:</strong> Assessment based on 10-year average yields and prices; classification of cultivable land: <em>Polaj</em> (regularly cultivated every year), <em>Parauti</em> (left fallow for 1–2 years), <em>Chachar</em> (fallow for 3–4 years), and <em>Banjar</em> (uncultivated for 5+ years).</li>
                <li><strong>Religious &amp; Social Policy:</strong> Evolution from orthodox Sunni governance to <em>Sulh-i-Kul</em> (Universal Peace and Absolute Toleration); Ibadat Khana inter-faith debates (1575); Mazhar Nama (1579 Infallibility Decree drafted by Sheikh Mubarak); Sulh-i-Kul as the ideological glue of a multi-confessional empire.</li>
              </ul>
            </li>
            <li><strong>Zenith and Decline:</strong> Jahangir (patronage of miniature painting, chain of justice); Shah Jahan (architectural pinnacle: Taj Mahal, Red Fort, Jama Masjid); Aurangzeb: orthodox reversal (re-imposition of Jizya in 1679, estrangement of Rajputs, Sikh resistance); the "Deccan Ulcer" (25-year prolonged war against Marathas bankrupting imperial finances). Structural decline: Jagirdari crisis (be-jagiri), agrarian revolts (Jats, Satnamis, Sikhs), court factionalism (Irani, Turani, Hindustani), and catastrophic external shocks (Nadir Shah 1739, Ahmad Shah Abdali).</li>
            <li><strong>Chhatrapati Shivaji Maharaj &amp; Maratha Movement:</strong> Concept of <em>Hindavi Swarajya</em>; mobile guerrilla warfare (Ganimi Kava); administrative council of eight ministers (<em>Ashta Pradhan</em> headed by Peshwa); revenue instruments: <em>Chauth</em> (1/4th of revenue paid as protection tribute) and <em>Sardeshmukhi</em> (additional 10% hereditary levy). Maratha expansion under Peshwa Baji Rao I; setback at the Third Battle of Panipat (1761 CE).</li>
          </ul>
          <div class="syl-action-bar">
            <a href="period.html?id=akbar-the-great" class="btn btn-outline btn-sm">Explore Akbar's Era →</a>
            <a href="practice.html?category=medieval" class="btn btn-primary btn-sm">Practice 1,014+ Medieval Questions</a>
          </div>
        </div>
      </div>

      <!-- =================================================================== -->
      <!-- SECTION 3: MODERN INDIAN HISTORY -->
      <!-- =================================================================== -->
      <div class="syl-section-pane" id="sec-modern">
        <div class="section-head">
          <span class="kicker">Section 3 • 1757 – 1947 CE</span>
          <h2>Modern Indian History &amp; National Movement</h2>
        </div>

        <!-- 1. British Expansion & Economic Exploitation -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">1. Colonial Expansion, Economic Ruin &amp; Drain of Wealth</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Plassey, Revenue Settlements, De-industrialization &amp; Famine Creation</p>
            </div>
            <span class="t-cat cat-colonial">Colonial Impact</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/british_clolonial_rule.png" alt="British Colonial Rule Infographic Sheet">
          </div>
          <ul>
            <li><strong>British Conquest of India:</strong> Battle of Plassey (1757 - treachery of Mir Jafar); Battle of Buxar (1764 - military triumph over combined forces of Mir Qasim, Shuja-ud-Daula, and Shah Alam II); Treaty of Allahabad (1765 - grant of Diwani rights of Bengal, Bihar, and Orissa); Clive's Dual Government. Subjugation tools: Wellesley's <em>Subsidiary Alliance System</em> (Hyderabad, Mysore, Awadh, Marathas) and Dalhousie's <em>Doctrine of Lapse</em> (Satara, Sambalpur, Jhansi, Nagpur); Annexation of Awadh (1856) on grounds of "maladministration".</li>
            <li><strong>Three Phases of Colonial Exploitation (R. Palme Dutt):</strong> Mercantile Phase (1757–1813: direct plunder, monopoly trade), Industrial/Free Trade Phase (1813–1858: one-way free trade converting India into an exporter of raw materials and importer of British manufactures), Financial Imperialism Phase (post-1858: British capital investments in railways, plantations, and public debt at guaranteed 5% returns).</li>
            <li><strong>Land Revenue Settlements:</strong>
              <ul>
                <li><strong>Permanent Settlement (Zamindari System, 1793):</strong> Introduced by Lord Cornwallis in Bengal, Bihar, and Orissa; revenue fixed in perpetuity; Zamindars recognized as landowners; rigid Sunset Law mechanics; tenantry reduced to exploited tenants-at-will.</li>
                <li><strong>Ryotwari System:</strong> Introduced by Thomas Munro and Alexander Read in Madras and Bombay Presidencies; direct settlement with registered peasant cultivators (Ryots); exorbitant revenue assessments forcing peasants into chronic rural debt and usury.</li>
                <li><strong>Mahalwari System:</strong> Formulated by Holt Mackenzie and Merttins Bird in North-Western Provinces, Punjab, and Central India; collective assessment with village communities (Mahals).</li>
              </ul>
            </li>
            <li><strong>De-industrialization &amp; Drain of Wealth:</strong> Destruction of traditional Indian textile and handicraft industries through discriminatory tariff walls in Britain; commercialization of agriculture forcing cash crops (Indigo, Opium, Jute, Cotton); catastrophic famines (Bengal Famine of 1770, late 19th-century famines). The <em>Drain of Wealth Theory</em> pioneered by Dadabhai Naoroji (<em>Poverty and Un-British Rule in India</em>) and supported by R.C. Dutt (<em>Economic History of India</em>), exposing unrequited surplus transfers through Home Charges, military expenses, and official remittances.</li>
          </ul>
        </div>

        <!-- 2. 1857 Revolt & Socio-Religious Reforms -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">2. Popular Resistance, Revolt of 1857 &amp; Socio-Religious Reforms</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Tribal Uprisings, The Great Revolt, Reformist vs. Revivalist Movements</p>
            </div>
            <span class="t-cat cat-colonial">Resistance &amp; Reform</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/socio_religious_reforms.png" alt="Socio-Religious Reforms Infographic Sheet">
          </div>
          <ul>
            <li><strong>Early Resistance:</strong> Civil uprisings (Sanyasi, Chuar); Tribal rebellions against forest laws and Dikus (outsider moneylenders): Kol Insurrection (1831), Santhal Hool (1855–56 under Sidhu and Kanhu), Munda Ulgulan (1899–1900 under Birsa Munda).</li>
            <li><strong>The Great Revolt of 1857:</strong> Triggered on 10 May 1857 at Meerut; structural causes: political (Doctrine of Lapse), economic (peasant impoverishment), socio-religious (Lex Loci Act, religious interference), military (greased cartridges, General Service Enlistment Act). Key leadership: Bahadur Shah Zafar (Delhi), Begum Hazrat Mahal (Lucknow), Nana Sahib &amp; Tatya Tope (Kanpur), Rani Lakshmibai (Jhansi), Kunwar Singh (Arrah/Bihar). Aftermath: Government of India Act 1858 ending Company rule; Queen's Proclamation; Peel Commission army reorganization based on "martial vs. non-martial" divide.</li>
            <li><strong>Socio-Religious Reform Movements:</strong>
              <ul>
                <li><strong>Reformist:</strong> Raja Ram Mohan Roy (Brahmo Samaj 1828, abolition of Sati Regulation XVII of 1829, Sambad Kaumudi); Ishwar Chandra Vidyasagar (Hindu Widows' Remarriage Act XV of 1856, Bethune School); Sir Syed Ahmed Khan (Aligarh Movement, modern scientific education).</li>
                <li><strong>Revivalist:</strong> Swami Dayanand Saraswati (Arya Samaj 1875, "Back to Vedas", Satyarth Prakash, Shuddhi movement); Swami Vivekananda (Ramakrishna Mission 1897, Neo-Vedanta, Parliament of Religions Chicago 1893); Deoband School.</li>
                <li><strong>Lower-Caste &amp; Justice Movements:</strong> Jyotirao Phule (Satyashodhak Samaj 1873, <em>Gulamgiri</em>); E.V. Ramasamy Periyar (Self-Respect Movement, Dravidian awakening); Dr. B.R. Ambedkar (Mahad Satyagraha 1927, Bahishkrit Hitakarini Sabha, Depressed Classes movement).</li>
              </ul>
            </li>
          </ul>
        </div>

        <!-- 3. Indian National Movement -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">3. The Indian National Movement (1885–1947 CE)</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Moderates, Extremists, Gandhian Mass Struggles &amp; The Road to Partition</p>
            </div>
            <span class="t-cat cat-colonial">Freedom Movement</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/freedom_struggle.png" alt="Indian Freedom Struggle Infographic Sheet">
          </div>
          <ul>
            <li><strong>The Moderate Phase (1885–1905):</strong> Foundation of the Indian National Congress (1885) at Bombay by A.O. Hume and W.C. Bonnerjee; Safety Valve thesis vs. Lightning Conductor thesis; leaders: Dadabhai Naoroji, Gopal Krishna Gokhale, Pherozeshah Mehta, S.N. Banerjee; methods: "3Ps" (Petition, Prayer, Protest); achievement: Indian Councils Act 1892 and pioneering the economic critique of colonialism.</li>
            <li><strong>Extremist Phase &amp; Swadeshi (1905–1918):</strong> Lal-Bal-Pal (Lala Lajpat Rai, Bal Gangadhar Tilak, Bipin Chandra Pal) and Aurobindo Ghosh. Partition of Bengal (1905) by Lord Curzon sparking the Swadeshi and Boycott Movement; national education and indigenous industries; Surat Split (1907); Morley-Minto Reforms (1909) introducing Separate Electorates for Muslims; revolutionary movements abroad (Ghadar Party, Komagata Maru incident); Home Rule League Movements (1916) by Tilak and Annie Besant; Lucknow Pact (1916).</li>
            <li><strong>The Gandhian Era of Mass Mobilization (1919–1947):</strong>
              <ul>
                <li><strong>Early Experiments &amp; Rowlatt:</strong> Champaran Indigo Satyagraha (1917, Tinkathia system), Ahmedabad Mill Strike (1918), Kheda Peasant Satyagraha (1918). Rowlatt Act (1919) and Jallianwala Bagh Massacre (13 April 1919 under General Dyer).</li>
                <li><strong>Non-Cooperation Movement (1920–1922):</strong> Convergence with Khilafat cause; boycott of foreign goods, schools, and courts; suspended after Chauri Chaura incident (4 Feb 1922). Swaraj Party (C.R. Das, Motilal Nehru); Revolutionary Phase II (HRA/HSRA, Kakori Action 1925, Bhagat Singh, Chandrashekhar Azad, Surya Sen's Chittagong Armoury Raid 1930).</li>
                <li><strong>Civil Disobedience Movement (1930–1934):</strong> Simon Commission boycott (1927); Nehru Report (1928) vs. Jinnah's 14 Points; Lahore Congress Purna Swaraj declaration (1929); Dandi Salt March (12 March – 6 April 1930); Dharasana Satyagraha; Round Table Conferences (1–3); Gandhi-Irwin Pact (1931); Poona Pact (1932) between Gandhi and Ambedkar preserving joint electorates with reserved seats for Depressed Classes.</li>
                <li><strong>Final Countdown (1940–1947):</strong> August Offer (1940); Cripps Mission (1942); Quit India Movement (August 1942, "Do or Die", parallel governments in Ballia, Satara, and Tamluk); Subhas Chandra Bose and the Indian National Army (INA), Red Fort Trials, and Royal Indian Navy (RIN) Mutiny (Feb 1946); Cabinet Mission Plan (1946); Direct Action Day (16 August 1946) and communal holocaust; Mountbatten Plan (3 June 1947) and Indian Independence Act 1947.</li>
              </ul>
            </li>
          </ul>
          <div class="syl-action-bar">
            <a href="period.html?id=indian-freedom-struggle" class="btn btn-outline btn-sm">Explore Freedom Struggle Period →</a>
            <a href="practice.html?category=modern" class="btn btn-primary btn-sm">Practice 2,240+ Modern MCQs</a>
          </div>
        </div>
      </div>

      <!-- =================================================================== -->
      <!-- SECTION 4: POST-INDEPENDENCE CONSOLIDATION -->
      <!-- =================================================================== -->
      <div class="syl-section-pane" id="sec-post">
        <div class="section-head">
          <span class="kicker">Section 4 • 1947 – 2000s</span>
          <h2>Post-Independence Consolidation &amp; Reorganization</h2>
        </div>

        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">1. Nation-Building, State Integration &amp; Linguistic Reorganization</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Sardar Patel's Diplomacy, Fazal Ali Commission &amp; Constitutional Architecture</p>
            </div>
            <span class="t-cat cat-independent">Post-Independence</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/1947_to_1964_.png" alt="India 1947 to 1964 Infographic Sheet">
          </div>
          <ul>
            <li><strong>Integration of Princely States (1947–1949):</strong> Masterminded by Deputy Prime Minister Sardar Vallabhbhai Patel and Secretary V.P. Menon; persuasion via the Instrument of Accession (defense, foreign affairs, communications) and Privy Purses; resolution of intractable states: Junagadh (plebiscite following Nawab's flight), Hyderabad (Operation Polo police action in September 1948 dismantling the Razakar militia), and Jammu &amp; Kashmir (Instrument of Accession signed by Maharaja Hari Singh amidst Pakistani tribal invasion).</li>
            <li><strong>Linguistic Reorganization of States:</strong> S.K. Dhar Commission (1948) and JVP Committee (1949) advising against immediate linguistic reorganization; hunger strike and martyrdom of Potti Sreeramulu (1952) forcing the creation of Andhra State (1953); appointment of the States Reorganisation Commission (SRC 1953) under Justice Fazal Ali, K.M. Panikkar, and H.N. Kunzru; enactment of the <em>States Reorganisation Act 1956</em> creating 14 states and 6 union territories on linguistic lines, anchoring regional identities within federal constitutional democracy.</li>
            <li><strong>Tribal &amp; Borderland Integration:</strong> Jawaharlal Nehru's Tribal Panchsheel policy for the North-Eastern frontier (NEFA/Assam), emphasizing cultural preservation, non-imposition, and indigenous tribal administration over aggressive assimilation.</li>
          </ul>
        </div>

        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">2. Economic Modernization, Foreign Policy &amp; Democratic Crises</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Five-Year Plans, Green Revolution, NAM, Wars &amp; The Emergency (1975–77)</p>
            </div>
            <span class="t-cat cat-independent">Modernization &amp; Crises</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/1965_to_1980.png" alt="India 1965 to 1980 Infographic Sheet">
          </div>
          <ul>
            <li><strong>Planned Economic Modernization:</strong> Planning Commission and Five-Year Plans; First Plan (Harrod-Domar model focused on agriculture and major dams); Second Plan (Nehru-Mahalanobis model prioritizing heavy basic industries, public sector capital goods, and PSUs as "Temples of Modern India"); Land reforms (abolition of Zamindari intermediaries, tenancy security, land ceiling laws); the <strong>Green Revolution</strong> (mid-1960s under C. Subramaniam and Dr. M.S. Swaminathan deploying semi-dwarf HYV Mexican wheat and IR-8 rice, achieving national food self-sufficiency while creating inter-regional and ecological groundwater stresses).</li>
            <li><strong>Foreign Policy &amp; Geopolitics:</strong> Non-Aligned Movement (NAM) founded at Belgrade (1961) by Nehru, Tito, and Nasser; Panchsheel principles (1954); Sino-Indian War of 1962 (strategic shock); Indo-Pak Wars of 1965 (Tashkent Agreement) and 1971 (Liberation of Bangladesh, creation of sovereign Bangladesh, Shimla Agreement 1972).</li>
            <li><strong>The Emergency Era (1975–1977):</strong> Political backdrop: JP Movement (Navnirman, Total Revolution); declaration of internal Emergency on 25 June 1975; suspension of Fundamental Rights; 42nd Constitutional Amendment Act; mass arrests and press censorship; defeat of Indira Gandhi in the 1977 elections leading to India's first non-Congress Janata Party coalition government under Morarji Desai, validating democratic institutional resilience.</li>
          </ul>
          <div class="syl-action-bar">
            <a href="period.html?id=india-1947-1964" class="btn btn-outline btn-sm">Explore Post-1947 Periods →</a>
            <a href="practice.html?category=modern" class="btn btn-primary btn-sm">Practice Post-Independence MCQs</a>
          </div>
        </div>
      </div>

      <!-- =================================================================== -->
      <!-- SECTION 5: WORLD HISTORY -->
      <!-- =================================================================== -->
      <div class="syl-section-pane" id="sec-world">
        <div class="section-head">
          <span class="kicker">Section 5 • Mains GS Paper 1 Exclusive</span>
          <h2>World History: Revolutions, World Wars &amp; Global Order</h2>
        </div>

        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">1. Enlightenment, Industrial Revolution &amp; Political Revolutions</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Locke, Rousseau, 1776 American War &amp; 1789 French Revolution</p>
            </div>
            <span class="t-cat cat-world">Age of Revolutions</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/french_revolution.png" alt="French Revolution Infographic Sheet">
          </div>
          <ul>
            <li><strong>The Enlightenment:</strong> Philosophical foundations of modern constitutionalism: John Locke (natural rights to life, liberty, property; social contract based on consent of the governed), Montesquieu (separation of powers), Jean-Jacques Rousseau (General Will and popular sovereignty), Voltaire (secular tolerance and freedom of speech).</li>
            <li><strong>Industrial Revolution (Britain c. 1750s onwards):</strong> Mechanization of cotton textiles (Spinning Jenny, Power Loom), James Watt's steam engine, coal and iron metallurgy, canal and railway transport; transformation of agrarian society into urban capitalism; rise of industrial working class (proletariat), child labor, Dickensian urban slums; intellectual emergence of capitalism (Adam Smith) and socialism/Marxism (Karl Marx and Friedrich Engels).</li>
            <li><strong>American Revolution (1776):</strong> Mercantilist exploitation (Navigation Acts, Stamp Act, "No taxation without representation"), Boston Tea Party (1773), Declaration of Independence (4 July 1776 written by Thomas Jefferson); drafting of the United States Constitution (1787) incorporating separation of powers and Bill of Rights.</li>
            <li><strong>French Revolution (1789):</strong> Structural inequalities of the Ancien Regime (Three Estates: Clergy, Nobility, Third Estate bearing entire tax burden); fiscal insolvency; storming of the Bastille (14 July 1789); <em>Declaration of the Rights of Man and of the Citizen</em>; Reign of Terror under Robespierre; rise of Napoleon Bonaparte (Napoleonic Code, Continental System, Waterloo 1815).</li>
          </ul>
        </div>

        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">2. Imperialism, The World Wars, Cold War &amp; Soviet Dissolution</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Bismarck, Scramble for Africa, WWI/WWII, Decolonization &amp; 1991 USSR Fall</p>
            </div>
            <span class="t-cat cat-world">20th Century Order</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/world_war_II.png" alt="World War II Infographic Sheet">
          </div>
          <ul>
            <li><strong>19th-Century Nationalism &amp; Imperialism:</strong> Unification of Italy (Mazzini, Cavour, Garibaldi); Unification of Germany under Otto von Bismarck's "Blood and Iron" policy (proclamation of the German Empire at Versailles 1871); The New Imperialism: Scramble for Africa (Berlin Conference 1884–85 partition of Africa); imperialist exploitation of Asia (Opium Wars in China, Spheres of Influence, Boxer Rebellion).</li>
            <li><strong>World War I &amp; Russian Revolution (1914–1918):</strong> Secret alliance systems (Triple Entente vs. Triple Alliance), Sarajevo assassination of Archduke Franz Ferdinand, trench warfare. The Russian Revolution (1917): fall of Romanov autocracy in February, Bolshevik Revolution in October led by Vladimir Lenin, establishment of the USSR. The punitive <strong>Treaty of Versailles (1919)</strong>: Article 231 war guilt clause, crushing economic reparations, demilitarization of Rhineland, creating grievance exploited by fascism.</li>
            <li><strong>Interwar Crisis &amp; World War II (1939–1945):</strong> Rise of Italian Fascism (Mussolini) and German Nazism (Hitler); failure of the League of Nations; Anglo-French appeasement policy; German invasion of Poland (1 Sept 1939); Axis vs. Allied powers; Holocaust; Pearl Harbor; turning points: Battle of Stalingrad, D-Day landings; atomic bombing of Hiroshima and Nagasaki (August 1945).</li>
            <li><strong>The Cold War, Decolonization &amp; Collapse of USSR:</strong> Bipolar ideological confrontation between USA (Capitalism/NATO) and USSR (Communism/Warsaw Pact); proxy conflicts (Korea, Cuban Missile Crisis, Vietnam); global decolonization across Asia and Africa; stagnation of Soviet economy, Soviet-Afghan war drain; Mikhail Gorbachev's reforms of <em>Glasnost</em> (openness) and <em>Perestroika</em> (restructuring); fall of the Berlin Wall (1989); dissolution of the Soviet Union into 15 independent republics in December 1991.</li>
          </ul>
          <div class="syl-action-bar">
            <a href="period.html?id=world-war-2" class="btn btn-outline btn-sm">Explore World War II Period →</a>
            <a href="practice.html?category=world-history" class="btn btn-primary btn-sm">Practice 300+ World History MCQs</a>
          </div>
        </div>
      </div>

      <!-- =================================================================== -->
      <!-- SECTION 6: INDIAN ART AND CULTURE -->
      <!-- =================================================================== -->
      <div class="syl-section-pane" id="sec-culture">
        <div class="section-head">
          <span class="kicker">Section 6 • Thematic &amp; Conceptual Deep Digest</span>
          <h2>Indian Art, Architecture &amp; Cultural Heritage</h2>
        </div>

        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">1. Epigraphy &amp; Numismatic Traditions</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Scripts Evolution, Royal Coinage Iconography &amp; Socio-Economic Health</p>
            </div>
            <span class="t-cat cat-ancient">Epigraphy &amp; Coins</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/culture/sculptural-schools.jpg" alt="Sculptural Schools and Iconography">
          </div>
          <ul>
            <li><strong>Evolution of Indian Scripts:</strong> Ashokan Brahmi (written left-to-right, deciphered by James Prinsep); Kharosthi (derived from Aramaic, written right-to-left in northwestern India); Gupta script (cursive cursive offshoot of Brahmi); Devanagari (crystallized c. 10th century CE for Sanskrit and Hindi); Southern Grantha and Pallava-Chola scripts.</li>
            <li><strong>Numismatic Iconography:</strong> Silver Punch-Marked Coins (Pana) featuring solar, taurine, and mountain symbols without monarch names; Indo-Greek bilingual legends and royal realistic portraiture; Kushana high-purity gold dinaras featuring syncretic pantheons (Helios, Mithra, Oesho/Shiva with Nandi, Buddha); Gupta imperial gold coins: Samudragupta's Lyrist type (playing Veena) and Ashvamedha type, Chandragupta II's Archer type and Lion-slayer type; progressive debasement in late Gupta era reflecting monetization contraction.</li>
          </ul>
        </div>

        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">2. Temple Architecture Structural Metrics: Nagara, Dravida &amp; Vesara</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Ground Plans, Superstructures &amp; Canonical Vastu-Shastra Elements</p>
            </div>
            <span class="t-cat cat-ancient">Temple Architecture</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/culture/nagara-temple-style.jpg" alt="Nagara Temple Architecture Style">
          </div>
          <ul>
            <li><strong>Nagara Style (Northern Order):</strong> Built on raised stone platforms (<em>Jagati</em>); sanctum sanctorum (<em>Garbhagriha</em>) containing the deity, preceded by <em>Mandapa</em> (pillared assembly hall) and <em>Antarala</em> (vestibule); absence of monumental boundary walls or gopuram gateways; river goddesses Ganga and Yamuna flanking sanctum doorjambs. <strong>Shikhara Types:</strong>
              <ul>
                <li><em>Latina / Rekha-Prasada:</em> Square base with curvilinear tower curving gently inward to a top point.</li>
                <li><em>Phamsana:</em> Broader, stepped pyramidal roofs that slope upward horizontally (common for Mandapas).</li>
                <li><em>Valabhi:</em> Rectangular barrel-vaulted roof with wagon-vault crest derived from Buddhist Chaitya halls.</li>
                <li>Crowning elements: fluted stone disc (<em>Amalaka</em>) and finial vase (<em>Kalasha</em>). Regional variants: Khajuraho (Chandela, erotic sculptures, Panchayatana layout), Solanki (Modhera Sun Temple with stepped Surya Kund step-well), Odisha School (Deul sanctum tower and Jagamohana hall).</li>
              </ul>
            </li>
            <li><strong>Dravida Style (Southern Order):</strong> Enclosed by concentric fortified boundary walls (<em>Prakaras</em>); monumental gateway towers (<em>Gopurams</em>) that grew taller than the main temple under the Vijayanagara and Nayaka rulers; towering stepped pyramidal superstructure (<em>Vimana</em>) crowned by an octagonal or circular dome-shaped <em>Shikhara</em>; presence of enclosed sacred water tanks (<em>Pushkarini / Kalyani</em>); large pillared wedding halls (<em>Kalyana Mandapa</em>); Dvarapalas flanking the Garbhagriha. Examples: Brihadisvara Temple at Thanjavur (Rajaraja I Chola), Meenakshi Temple at Madurai.</li>
            <li><strong>Vesara Style (Deccan Hybrid):</strong> Synthesized by the Badami Chalukyas, Rashtrakutas, and perfected by the Hoysalas of Belur and Halebidu; characterized by <em>stellate (star-shaped)</em> ground plans; use of soft chloritic schist (soapstone) allowing extraordinarily dense, microscopic horizontal friezes of elephants, lions, horses, mythological epics, and celestial dancers (Shalabhanjikas).</li>
          </ul>
        </div>

        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">3. Indo-Islamic Engineering &amp; Syncretic Architecture</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Arcuate vs. Trabeate, Double-Dome, Pietra Dura &amp; Charbagh Grids</p>
            </div>
            <span class="t-cat cat-medieval">Indo-Islamic Engineering</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/culture/mughal-architecture.jpg" alt="Mughal Architecture and Indo-Islamic Engineering">
          </div>
          <ul>
            <li><strong>The Structural Engineering Shift:</strong> Transition from indigenous Indian <em>Trabeate / Corbelled style</em> (horizontal lintels supported by vertical columns and brackets) to Islamic <em>Arcuate style</em> (true arches, vaults, and domes constructed with radiating wedge-shaped stones called voussoirs locked by central keystones).</li>
            <li><strong>Decorative Aesthetics:</strong> Due to Islamic theological prohibition of animal and human figures in religious edifices, decoration relied on: <em>Arabesque</em> (intertwined continuous geometric and floral motifs), <em>Calligraphy</em> (Quranic verses carved in Naskh and Thuluth scripts), <em>Pietra Dura (Parchin Kari)</em> (inlaying polished semi-precious stones like lapis lazuli, carnelian, jasper, and turquoise into white marble), and <em>Jali Work</em> (delicately perforated marble and sandstone lattice screens allowing geometric light-and-shadow effects).</li>
            <li><strong>Spatial Innovations:</strong> <em>Double-Dome Construction:</em> Deployed at Humayun's Tomb and perfected at the Taj Mahal, featuring an inner dome providing acoustic proportion to the interior chamber and an elevated outer dome providing monumental exterior height; <em>Charbagh:</em> Four-quadrant symmetrical garden grid divided by flowing water channels and raised walkways symbolizing paradise (Jannat); <em>Minarets:</em> Providing structural balance, vertical counterpoise, and acoustic projection.</li>
          </ul>
        </div>

        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">4. Philosophical Schools (Shad-Darshana) &amp; UNESCO Intangible Heritage</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Astika Philosophy Systems &amp; Living Intangible Heritage of India</p>
            </div>
            <span class="t-cat cat-ancient">Philosophy &amp; UNESCO</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/culture/unesco-intangible-heritage.jpg" alt="UNESCO Intangible Cultural Heritage of India">
          </div>
          <ul>
            <li><strong>Shad-Darshana (Six Orthodox Schools of Indian Philosophy):</strong>
              <ul>
                <li><strong>Nyaya (Sage Gautama):</strong> Epistemological logic and rational dialectics; validates four sources of valid knowledge (Pramanas): Pratyaksha (perception), Anumana (inference), Upamana (comparison), and Shabda (testimony).</li>
                <li><strong>Vaisheshika (Sage Kanada):</strong> Atomistic pluralism (Paramanuvada); posits that the material cosmos consists of nine eternal substances and indestructible atoms (Paramanus); classifies reality into seven ontological categories (Padarthas).</li>
                <li><strong>Sankhya (Sage Kapila):</strong> Dualistic realism positing two eternal, uncreated principles: Purusha (pure unattached consciousness) and Prakriti (matter constituted by three Gunas: Sattva, Rajas, Tamas).</li>
                <li><strong>Yoga (Sage Patanjali):</strong> Practical psychological and physical path for realizing Sankhya liberation through <em>Ashtanga Yoga</em> (eight limbs: Yama, Niyama, Asana, Pranayama, Pratyahara, Dharana, Dhyana, Samadhi).</li>
                <li><strong>Purva Mimamsa (Sage Jaimini):</strong> Defends the eternal uncreated authority of Vedic ritualism (Shabda Nityata) for achieving cosmic Dharma and heaven.</li>
                <li><strong>Uttara Mimamsa / Vedanta (Sage Badarayana):</strong> Philosophical inquiry into the Upanishadic nature of Brahman. Major schools: <em>Advaita</em> (Adi Shankara - absolute non-dualism, world as Maya), <em>Vishishtadvaita</em> (Ramanuja - qualified non-dualism), and <em>Dvaita</em> (Madhvacharya - dualism).</li>
              </ul>
            </li>
            <li><strong>UNESCO Intangible Cultural Heritage of India (Living Heritage):</strong>
              <ol style="margin-top:8px;">
                <li>Vedic Chanting (2008)</li>
                <li>Ramlila, the traditional performance of the Ramayana (2008)</li>
                <li>Kutiyattam, Sanskrit theatre of Kerala (2008)</li>
                <li>Ramman, religious festival and ritual theatre of the Garhwal Himalayas (2009)</li>
                <li>Mudiyettu, ritual theatre and dance drama of Kerala (2010)</li>
                <li>Kalbelia folk songs and dances of Rajasthan (2010)</li>
                <li>Chhau dance (classical martial folk dance of Purulia, Seraikella, and Mayurbhanj) (2010)</li>
                <li>Buddhist Chanting of Ladakh (2012)</li>
                <li>Sankirtana, ritual singing, drumming, and dancing of Manipur (2013)</li>
                <li>Traditional brass and copper craft of utensil making among the Thatheras of Jandiala Guru, Punjab (2014)</li>
                <li>Yoga (2016)</li>
                <li>Nowruz (Parsi New Year festival) (2016)</li>
                <li>Kumbh Mela, Prayagraj / Haridwar / Ujjain / Nashik (2017)</li>
                <li>Durga Puja in Kolkata (2021)</li>
                <li>Garba of Gujarat (2023)</li>
              </ol>
            </li>
          </ul>
          <div class="syl-action-bar">
            <a href="art-culture.html" class="btn btn-outline btn-sm">Open Interactive Art &amp; Culture Hub (43 Topics) →</a>
            <a href="practice.html?category=art-culture" class="btn btn-primary btn-sm">Practice 460+ Culture Questions</a>
          </div>
        </div>
      </div>

      <!-- =================================================================== -->
      <!-- PART A: UTTAR PRADESH SPECIAL & RO/ARO TRACK -->
      <!-- =================================================================== -->
      <div class="syl-section-pane" id="sec-up">
        <div class="section-head">
          <span class="kicker">Part A • UPPSC GS Paper 5 &amp; 6 • RO/ARO Track</span>
          <h2>Uttar Pradesh State-Specific History, Heritage &amp; RO/ARO Hindi</h2>
        </div>

        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">1. UP Ancient to Modern Chronological Highlights</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Belan, Lahuradewa, Sanauli, 8 Mahajanapadas, Awadh &amp; 1857 Centicentres</p>
            </div>
            <span class="t-cat cat-up">UP State Core</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/up_history.png" alt="Uttar Pradesh History Comprehensive Revision Sheet">
          </div>
          <ul>
            <li><strong>Archaeological Milestones:</strong> Lahuradewa (Sant Kabir Nagar) yielding c. 7000 BCE rice farming; Belan Valley continuous Palaeolithic-Mesolithic-Neolithic sequence (Sarai Nahar Rai, Mahadaha, Damdama, Koldihwa); Alamgirpur (Meerut) as IVC eastern boundary; Sanauli (Baghpat) ASI excavations of Bronze Age solid-disk wheeled war chariots and royal copper coffins.</li>
            <li><strong>8 of 16 Mahajanapadas in UP:</strong> Kashi (Varanasi), Kosala (Shravasti/Ayodhya), Malla (Kushinagar/Pava republic), Vatsa (Kaushambi), Panchala (Ahichchhatra/Kampilya), Kuru (Hastinapur), Shurasena (Mathura), Chedi (Shuktimati).</li>
            <li><strong>Medieval Transformations:</strong> Jaunpur Sharqi Sultanate ("Shiraz of the East", Atala Masjid propylon screens); Mughal Agra capital &amp; Fatehpur Sikri (Buland Darwaza, Salim Chishti tomb); Kalinjar Fort (Sher Shah Suri demise); Nawabs of Awadh (Asaf-ud-Daula, Bara Imambara vaulted hall, Rumi Darwaza, Ganga-Jamuni Tehzeeb, Wajid Ali Shah).</li>
            <li><strong>Freedom Movement in UP:</strong> 1857 epicenters (Meerut 10 May, Lucknow Hazrat Mahal, Kanpur Nana Sahib/Tatya Tope, Jhansi Lakshmibai, Bareilly Khan Bahadur Khan, Allahabad Liaquat Ali, Faizabad Ahmadullah Shah, Baraut Shah Mal); Socio-religious reforms: Aligarh (Sir Syed, AMU), Deoband (Nanautavi, Gangohi 1866), BHU (Malaviya 1916); Chauri Chaura incident (1922); Kisan Sabhas (Oudh Kisan Sabha Baba Ramchandra, Eka Movement Madari Pasi, AIKS 1936 Lucknow); Revolutionary movement: HRA (Kanpur 1924), Kakori Train Action (1925 martyrs), HSRA (1928), Chandrashekhar Azad Alfred Park martyrdom (1931); Ballia parallel government under Chittu Pandey (1942).</li>
          </ul>
          <div class="syl-action-bar">
            <a href="up-history.html" class="btn btn-outline btn-sm">Open Comprehensive UP History Hub →</a>
            <a href="practice.html?category=up-history" class="btn btn-primary btn-sm">Practice 2,220+ UP Questions</a>
          </div>
        </div>

        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">2. UP RO/ARO General Hindi (Samanya Hindi) Exam Track</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Prelims Paper 2 (60 Questions | 60 Marks) • Target Score: 55+ Marks</p>
            </div>
            <span class="t-cat cat-up">RO/ARO Hindi</span>
          </div>
          <p>
            The UP RO/ARO Preliminary Examination includes an objective General Hindi paper (60 Questions, 60 Minutes) covering exactly six topics (10 questions each):
          </p>
          <div class="up-table-wrap">
            <table class="up-table">
              <thead>
                <tr>
                  <th>Topic (10 Questions Each)</th>
                  <th>Key Exam Rules &amp; Frequent Traps</th>
                  <th>Classic Exemplar Sets</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>1. विलोम शब्द (Antonyms)</strong></td>
                  <td>तत्सम का विलोम सदैव तत्सम होगा; तद्भव का विलोम तद्भव होगा। संज्ञा का विलोम संज्ञा तथा विशेषण का विलोम विशेषण ही होता है।</td>
                  <td>अथ-इति, स्थावर-जंगम, उन्मूलन-रोपण, पाश्चात्य-पौरस्त्य, तिमिर-आलोक, गरिमा-लघिमा, व्यष्टि-समष्टि।</td>
                </tr>
                <tr>
                  <td><strong>2. वाक्य एवं वर्तनी शुद्धि</strong></td>
                  <td>संधि नियमों और प्रत्ययों का ध्यान रखें। दोहरे प्रत्ययों (उदा. पूज्यनीय) तथा 'अनेकों' जैसे अशुद्ध बहुवचनों से बचें।</td>
                  <td>शुद्ध: कवयित्री, शृंगार, उज्ज्वल, आशीर्वाद, अनुगृहीत, पूजनीय, अंत्याक्षरी, याज्ञवल्क्य।</td>
                </tr>
                <tr>
                  <td><strong>3. अनेक शब्दों के एक शब्द</strong></td>
                  <td>इच्छा और इच्छा रखने वाले में अंतर: मोक्ष की इच्छा = मुमुक्षा; मोक्ष चाहने वाला = मुमुक्षु। युद्ध की इच्छा = युयुत्सा; युद्ध चाहने वाला = युयुत्सु।</td>
                  <td>मुमुक्षु, युयुत्सु, जिजीविषा, अपरिमेय, अंतेवासी, किंकर्तव्यविमूढ़, अकिंचन, पाथेय, सव्यसाची।</td>
                </tr>
                <tr>
                  <td><strong>4. तत्सम एवं तद्भव</strong></td>
                  <td>संस्कृत के मूल शब्द तत्सम कहलाते हैं; प्राकृत/अपभ्रंश से परिवर्तित शब्द तद्भव हैं (उदा. 'क्ष' तद्भव में 'ख' या 'छ' बन जाता है: अक्षि -> आँख, मक्षिका -> मक्खी)।</td>
                  <td>गोधूम-गेहूँ, हरिद्रा-हल्दी, अक्षि-आँख, इक्षु-ईख, घृत-घी, कपर्दिका-कौड़ी, ओष्ठ-ओठ, प्रस्तर-पत्थर।</td>
                </tr>
                <tr>
                  <td><strong>5. विशेष्य एवं विशेषण</strong></td>
                  <td>संज्ञा पद 'विशेष्य' कहलाता है; उसकी विशेषता बताने वाला पद 'विशेषण' है।</td>
                  <td>ऋषि (विशेष्य) -> आर्ष (विशेषण); इतिहास -> ऐतिहासिक; उपेक्षा -> उपेक्षित; 'नीली गाय' में 'गाय' विशेष्य है।</td>
                </tr>
                <tr>
                  <td><strong>6. पर्यायवाची शब्द</strong></td>
                  <td>समान अर्थ प्रकट करने वाले शब्द। ध्यान रहे कि संदर्भ के अनुसार ही शब्द का प्रयोग शुद्ध होता है।</td>
                  <td>कमल (अरविंद, राजीव, नलिन); अश्व (हय, तुरंग, वाजि); यमुना (कालिंदी, अर्कजा); सूर्य (मार्तंड, सविता)।</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="syl-action-bar">
            <a href="practice.html?category=ro-hindi" class="btn btn-primary btn-sm">Practice 180+ RO/ARO Hindi Questions</a>
          </div>
        </div>
      </div>

      <!-- =================================================================== -->
      <!-- PART B: RRB NTPC & BANKING TRACK -->
      <!-- =================================================================== -->
      <div class="syl-section-pane" id="sec-rrb-bank">
        <div class="section-head">
          <span class="kicker">Part B • Technical, Science &amp; Banking Track</span>
          <h2>Railway RRB NTPC &amp; Banking Awareness Special Track</h2>
        </div>

        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">1. Railway Recruitment Board (RRB NTPC) Exam Blueprint</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">CBT-1, CBT-2, CBAT Aptitude, Railways History &amp; General Science</p>
            </div>
            <span class="t-cat cat-world">RRB NTPC Track</span>
          </div>
          <ul>
            <li><strong>CBT-1 Screening (100 Questions | 90 Minutes):</strong> Mathematics (30 Qs), General Intelligence &amp; Reasoning (30 Qs), General Awareness (40 Qs with high weightage on 10th-standard General Science). 1/3rd negative marking applies.</li>
            <li><strong>CBT-2 Merit Decider (120 Questions | 90 Minutes):</strong> Mathematics (35 Qs), General Intelligence &amp; Reasoning (35 Qs), General Awareness (50 Qs).</li>
            <li><strong>Skill Tests:</strong> CBAT (Computer Based Aptitude Test for Station Master / Traffic Assistant - requires min. T-score of 42 in each battery); Typing Skill Test (30 wpm English / 25 wpm Hindi for clerks/typists). Strict medical fitness (A-2 Medical Category: 6/9 vision without glasses, zero color blindness).</li>
            <li><strong>Indian Railways Historical Milestones:</strong>
              <ul>
                <li><strong>16 April 1853:</strong> First passenger train ran between Bori Bunder (Bombay) and Thane (34 km, 14 carriages, 400 guests) hauled by three locomotives: <em>Sahib</em>, <em>Sindh</em>, and <em>Sultan</em> under Lord Dalhousie.</li>
                <li><strong>Fairy Queen (1855):</strong> World's oldest working steam locomotive operating tourist runs between New Delhi and Alwar (Guinness World Record).</li>
                <li><strong>18 Railway Zones &amp; Divisions:</strong> 18th zone created is South Coast Railway (SCoR) headquartered at Visakhapatnam; largest zone by route kilometer is Northern Railway (HQ: New Delhi).</li>
                <li><strong>Modern Initiatives:</strong> Dedicated Freight Corridors (Western DFC: Dadri to JNPT; Eastern DFC: Ludhiana to Dankuni); Vande Bharat Express (Train 18 - semi-high-speed indigenous trainsets); Kavach automatic train protection (ATP) system; UNESCO Mountain Railways of India (Darjeeling Himalayan Railway, Nilgiri Mountain Railway, Kalka-Shimla Railway).</li>
              </ul>
            </li>
            <li><strong>General Science for RRB NTPC:</strong>
              <ul>
                <li><strong>Physics:</strong> Newton's Laws of Motion, work, power, energy, gravitational acceleration ($g = 9.8\text{ m/s}^2$), sound waves (ultrasonic/infrasonic), reflection and refraction of light, lenses, Ohm's Law ($V = IR$), electrical power.</li>
                <li><strong>Chemistry:</strong> Periodic Table trends, atomic structure, acids/bases/salts (pH scale), everyday chemicals (Baking soda: $\text{NaHCO}_3$, Washing soda: $\text{Na}_2\text{CO}_3\cdot10\text{H}_2\text{O}$, Bleaching powder: $\text{CaOCl}_2$, Plaster of Paris: $\text{CaSO}_4\cdot\frac{1}{2}\text{H}_2\text{O}$), metals and metallurgy (alloys like brass, bronze, stainless steel).</li>
                <li><strong>Biology:</strong> Human digestive and circulatory systems, blood groups (AB+ universal recipient, O- universal donor), vitamins and deficiency diseases (Vitamin A - night blindness, Vitamin B1 - beriberi, Vitamin C - scurvy, Vitamin D - rickets), infectious diseases caused by bacteria/viruses/protozoa.</li>
              </ul>
            </li>
          </ul>
        </div>

        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">2. Banking &amp; Financial Evolution in India</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Presidency Banks to SBI, RBI Mandate, Nationalization &amp; Monetary Policy</p>
            </div>
            <span class="t-cat cat-world">Banking Awareness</span>
          </div>
          <ul>
            <li><strong>Historical Evolution of Banking:</strong>
              <ul>
                <li><strong>Earliest Banks:</strong> Bank of Hindoostan (1770 at Calcutta by Alexander &amp; Co.); General Bank of India (1786).</li>
                <li><strong>Presidency Banks:</strong> Bank of Calcutta (1806, renamed Bank of Bengal in 1809), Bank of Bombay (1840), and Bank of Madras (1843). Amalgamated in 1921 to form the <em>Imperial Bank of India</em>. Nationalized on 1 July 1955 under the State Bank of India Act to become the <strong>State Bank of India (SBI)</strong> on recommendations of the Gorwala / All India Rural Credit Survey Committee.</li>
                <li><strong>First Purely Indian Banks:</strong> Punjab National Bank (founded 1894 at Lahore by Lala Lajpat Rai); Central Bank of India (1911, first wholly Indian commercial bank owned and managed by Indians under Sir Sorabji Pochkhanawala).</li>
              </ul>
            </li>
            <li><strong>Reserve Bank of India (RBI):</strong> Recommended by the Royal Commission on Indian Currency and Finance (Hilton Young Commission, 1926); established under the <em>Reserve Bank of India Act 1934</em>; commenced operations on <strong>1 April 1935</strong> with initial headquarters at Calcutta (permanently shifted to Bombay in 1937); nationalized on <strong>1 January 1949</strong> under the RBI (Transfer to Public Ownership) Act 1948. First Governor: Sir Osborne Smith; First Indian Governor: C.D. Deshmukh.</li>
            <li><strong>Bank Nationalization:</strong>
              <ul>
                <li><strong>First Wave (19 July 1969):</strong> 14 major commercial banks having deposits over ₹50 crore nationalized by Indira Gandhi government via Banking Companies (Acquisition and Transfer of Undertakings) Ordinance.</li>
                <li><strong>Second Wave (15 April 1980):</strong> 6 commercial banks having deposits over ₹200 crore nationalized.</li>
              </ul>
            </li>
            <li><strong>Monetary Policy Instruments:</strong> Quantitative tools: Cash Reserve Ratio (CRR), Statutory Liquidity Ratio (SLR), Repo Rate (policy interest rate), Standing Deposit Facility (SDF), Marginal Standing Facility (MSF), Open Market Operations (OMO). Monetary Policy Committee (MPC) established in 2016 under Section 45ZB of RBI Act: 6 members (3 from RBI, 3 appointed by Central Government) chaired by RBI Governor, targeting retail inflation (CPI) at $4\% \pm 2\%$.</li>
          </ul>
          <div class="syl-action-bar">
            <a href="practice.html?category=science-tech" class="btn btn-outline btn-sm">Practice General Science MCQs →</a>
            <a href="practice.html?exam=bank" class="btn btn-primary btn-sm">Practice 730+ Banking Questions</a>
            <a href="practice.html?exam=rrb" class="btn btn-primary btn-sm">Practice 940+ Railway Questions</a>
          </div>
        </div>
      </div>

    </div>
  </section>
</main>

<footer id="siteFooter"></footer>

<script src="js/data.js"></script>
<script src="js/app.js"></script>
<script src="js/search.js"></script>
<script src="js/graph.js"></script>
<script>
function switchSylTab(tabId) {
  document.querySelectorAll('.syl-nav-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.syl-section-pane').forEach(p => p.classList.remove('active'));

  const activeBtn = Array.from(document.querySelectorAll('.syl-nav-btn')).find(b => b.getAttribute('onclick').includes(tabId));
  if (activeBtn) activeBtn.classList.add('active');

  const pane = document.getElementById(tabId);
  if (pane) pane.classList.add('active');
}

function initSylHub(){
  renderNav('syllabus.html');
  renderBreadcrumb([{label:'Home',href:'index.html'},{label:'Exam Syllabus & Master Study Guide'}]);
  renderFooter();
  initReveal();
}
initSylHub();
</script>
</body>
</html>
'''

with open('syllabus.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"SUCCESS: Generated comprehensive syllabus.html ({len(content)} characters).")
