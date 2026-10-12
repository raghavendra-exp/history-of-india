import re

with open('books.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update title & heading
content = content.replace(
    'The 10 Canonical Textbooks Study Hub — Complete History of India',
    'The 20 Canonical Textbooks & Compendiums Study Hub — Complete History of India'
)
content = content.replace(
    'The Canonical Textbooks Study Hub (15 Master Books)',
    'The Canonical Textbooks Study Hub (20 Master Books & Lecture Compendiums)'
)
content = content.replace(
    'Every single concept, chronological period, art tradition, sociological dimension, and practice question across this platform is rigorously mapped to the 15 canonical standard textbooks',
    'Every single concept, chronological period, art tradition, sociological dimension, and practice question across this platform is rigorously mapped to the 20 canonical standard textbooks and master lecture compendiums'
)

# 2. Update filter chips
old_filter = '''      <div class="filter-bar" id="booksFilterBar">
        <button class="filter-chip active" onclick="filterBooks('all', this)">All 15 Books (15)</button>
        <button class="filter-chip" onclick="filterBooks('ncert', this)">NCERT Foundations (5)</button>
        <button class="filter-chip" onclick="filterBooks('ancient', this)">Ancient India (2)</button>
        <button class="filter-chip" onclick="filterBooks('medieval', this)">Medieval India (1)</button>
        <button class="filter-chip" onclick="filterBooks('modern', this)">Modern India (3)</button>
        <button class="filter-chip" onclick="filterBooks('post-independence', this)">Post-Independence (1)</button>
        <button class="filter-chip" onclick="filterBooks('art', this)">Art &amp; Culture (2)</button>
        <button class="filter-chip" onclick="filterBooks('society', this)">Indian Society (2)</button>
        <button class="filter-chip" onclick="filterBooks('world', this)">World History (1)</button>
      </div>'''

new_filter = '''      <div class="filter-bar" id="booksFilterBar">
        <button class="filter-chip active" onclick="filterBooks('all', this)">All 20 Books &amp; Compendiums (20)</button>
        <button class="filter-chip" onclick="filterBooks('ncert', this)">NCERT Foundations (5)</button>
        <button class="filter-chip" onclick="filterBooks('ancient', this)">Ancient India (3)</button>
        <button class="filter-chip" onclick="filterBooks('medieval', this)">Medieval India (2)</button>
        <button class="filter-chip" onclick="filterBooks('modern', this)">Modern India (6)</button>
        <button class="filter-chip" onclick="filterBooks('post-independence', this)">Post-Independence (1)</button>
        <button class="filter-chip" onclick="filterBooks('art', this)">Art &amp; Culture (2)</button>
        <button class="filter-chip" onclick="filterBooks('society', this)">Indian Society (2)</button>
        <button class="filter-chip" onclick="filterBooks('world', this)">World History (3)</button>
      </div>'''

content = content.replace(old_filter, new_filter)

# 3. Add new book cards before the closing of booksContainer
new_cards = '''
        <!-- Book 16: A New Look at Modern Indian History by B.L. Grover & Alka Mehta -->
        <div class="book-card" data-category="modern">
          <div class="book-header">
            <span class="book-icon">🏛️</span>
            <span class="book-badge" style="background:#e0e7ff; color:#3730a3;">Administrative &amp; Constitutional</span>
          </div>
          <h2 class="book-title">A New Look at Modern Indian History</h2>
          <div class="book-author">B.L. Grover &amp; Alka Mehta (S. Chand Publishing)</div>
          <div class="book-syllabus">Target: UPSC Prelims &bull; Governor-Generals &bull; Administrative Acts &bull; Famine &amp; Financial Reforms</div>
          <p class="book-desc">
            The definitive analytical reference on British administrative statecraft, diplomatic treaties, and constitutional statutes. Renowned for its rigorous biographical critiques of Governor-Generals from Warren Hastings to Mountbatten, detailed clauses of Charter and Councils Acts, land revenue tenures, and famine commissions.
          </p>
          <div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes</h4>
            <ul>
              <li><strong>Doctrines &amp; Treaties:</strong> Subsidiary Alliance 4-stage mechanism; Ring Fence policy; Doctrine of Lapse annexations; Treaty of Allahabad (1765), Salbai (1782), Bassein (1802).</li>
              <li><strong>Administrative Statecraft:</strong> Cornwallis Code (1793 separation of powers); Macaulay's 1835 Minute; Wood's Despatch 1854; Metcalfe Press Act 1835; Vernacular Press Act 1878.</li>
              <li><strong>Famine &amp; Finance:</strong> Campbell (1866), Strachey (1880), Lyall (1897), and MacDonnell (1901) Commissions; Financial decentralization under Mayo (1870) and Lytton.</li>
              <li><strong>Constitutional Chronology:</strong> Regulating Act 1773 to Government of India Acts 1919 &amp; 1935, analyzing dyarchy, federal court, and provincial autonomy.</li>
            </ul>
          </div>
          <div class="book-pdf-box">
            <div class="pdf-box-head">
              <span class="pdf-tag">📥 Academic Preservation &amp; Reference</span>
              <span class="pdf-source">National Digital Library / Open Access</span>
            </div>
            <div class="pdf-links-row">
              <a href="https://archive.org/search?query=%22A+New+Look+at+Modern+Indian+History%22+Grover" target="_blank" rel="noopener noreferrer" class="btn-pdf">🏛️ B.L. Grover Archive Reference ↗</a>
              <a href="https://archive.org/details/dli.ernet.245842" target="_blank" rel="noopener noreferrer" class="btn-pdf-sub">📖 Digital Library of India Copy ↗</a>
            </div>
          </div>
          <div class="book-actions">
            <a href="practice.html?book=bl-grover" class="btn btn-primary">🎯 Prelims MCQs</a>
            <a href="practice.html?mode=mains&book=bl-grover" class="btn btn-outline">✍️ Mains Drills</a>
            <a href="timeline.html#british-administration" class="btn btn-outline">⏱️ Administration Timeline</a>
            <a href="map.html" class="btn btn-outline">🗺️ Historical Map</a>
          </div>
        </div>

        <!-- Book 17: Annals and Antiquities of Rajasthan by Lieut.-Col. James Tod -->
        <div class="book-card" data-category="medieval ancient">
          <div class="book-header">
            <span class="book-icon">🏰</span>
            <span class="book-badge" style="background:#fef3c7; color:#b45309;">Regional Epic &amp; Chivalry</span>
          </div>
          <h2 class="book-title">Annals &amp; Antiquities of Rajasthan</h2>
          <div class="book-author">Lieut.-Col. James Tod (Classical Monumental Chronicle)</div>
          <div class="book-syllabus">Target: Medieval Indian History &bull; Rajput Clans &bull; Feudal Chivalry &bull; Architecture &amp; Resistance</div>
          <p class="book-desc">
            The monumental primary narrative preserving the genealogies, feudal institutions, military chivalry, and heroic resistance of Rajputana. Essential for understanding the Rajput clan system, Agnikula origins, the legendary fortresses of Mewar (Chittorgarh, Kumbhalgarh), and battles against Delhi Sultans and Mughals.
          </p>
          <div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes</h4>
            <ul>
              <li><strong>Rajput Origins:</strong> The Agnikula sacrificial myth of Mount Abu (Pratiharas, Paramaras, Chalukyas, Chauhans) vs Suryavanshi (Guhilas/Sisodias, Rathores) and Chandravanshi lineages.</li>
              <li><strong>Mewar's Resistance:</strong> Bappa Rawal; Rana Kumbha's architectural renaissance (Vijay Stambha, 32 hill fortresses); Rana Sanga at Khanwa (1527); Maharana Pratap at Haldighati (1576) and Chavand.</li>
              <li><strong>Feudal Hierarchy &amp; Code:</strong> The Patta and Jagir land tenures; hereditary Thakurs; Chhatri memorials; the martial ethos of Rajput chivalry.</li>
              <li><strong>Jauhar &amp; Saka:</strong> Supreme sacrifice traditions during historical sieges of Chittorgarh — 1303 (Rani Padmini / Alauddin Khalji), 1535 (Rani Karnavati / Bahadur Shah), and 1568 (Akbar).</li>
            </ul>
          </div>
          <div class="book-pdf-box">
            <div class="pdf-box-head">
              <span class="pdf-tag">📥 Classical Open-Access Digital Vault</span>
              <span class="pdf-source">Internet Archive / British Library Digitization</span>
            </div>
            <div class="pdf-links-row">
              <a href="https://archive.org/details/annalsandantiqu00croogoog" target="_blank" rel="noopener noreferrer" class="btn-pdf">🏰 James Tod: Annals Vol. I &amp; II PDF ↗</a>
              <a href="https://archive.org/details/annalsantiquitie01toduoft" target="_blank" rel="noopener noreferrer" class="btn-pdf-sub">📖 Toronto Library Scan ↗</a>
            </div>
          </div>
          <div class="book-actions">
            <a href="practice.html?book=james-tod" class="btn btn-primary">🎯 Rajput Polity MCQs</a>
            <a href="practice.html?mode=mains&book=james-tod" class="btn btn-outline">✍️ Mains Answers</a>
            <a href="timeline.html#kingdoms-of-north" class="btn btn-outline">⏱️ Rajput Timeline</a>
            <a href="map.html" class="btn btn-outline">🗺️ Fortress Map</a>
          </div>
        </div>

        <!-- Book 18: Sapiens: A Brief History of Humankind by Yuval Noah Harari -->
        <div class="book-card" data-category="ancient world">
          <div class="book-header">
            <span class="book-icon">🧠</span>
            <span class="book-badge" style="background:#ecfdf5; color:#047857;">Prehistory &amp; Human Evolution</span>
          </div>
          <h2 class="book-title">Sapiens: A Brief History of Humankind</h2>
          <div class="book-author">Prof. Yuval Noah Harari (Harper / Vintage Books)</div>
          <div class="book-syllabus">Target: Prehistory &bull; Cognitive &amp; Agricultural Revolutions &bull; Imagined Orders &bull; State Formation</div>
          <p class="book-desc">
            A revolutionary interdisciplinary lens synthesizing evolutionary biology, anthropology, and world prehistory. Illuminates the Cognitive Revolution, the myth-making capacity enabling large-scale human cooperation, the paradoxical traps of the Agricultural Revolution, and the unifying forces of money, empire, and religion.
          </p>
          <div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes</h4>
            <ul>
              <li><strong>The Cognitive Revolution (70k BCE):</strong> Fiction-enabled language; collective myths allowing stranger cooperation beyond Dunbar's number (150); Paleolithic foragers of Bhimbetka.</li>
              <li><strong>Agricultural Revolution (10k BCE):</strong> The 'Luxury Trap' — wheat and rice domesticating Homo sapiens; Mehrgarh transition to sedentary village farming; demographic boom vs health decline.</li>
              <li><strong>The Three Universal Orders:</strong> Money (the supreme inter-subjective trust system), Imperial Empires (blending cultures), and Universal Religions (Buddhism, Islam, Christianity).</li>
              <li><strong>Scientific Revolution &amp; Capital:</strong> The discovery of ignorance (Ignoramus), marriage of imperial exploration and modern science, and the credit-driven capitalist economy.</li>
            </ul>
          </div>
          <div class="book-pdf-box">
            <div class="pdf-box-head">
              <span class="pdf-tag">📥 Academic Concept Companion</span>
              <span class="pdf-source">Open Educational Resources &amp; Summaries</span>
            </div>
            <div class="pdf-links-row">
              <a href="https://archive.org/search?query=%22Sapiens+A+Brief+History+of+Humankind%22+Harari" target="_blank" rel="noopener noreferrer" class="btn-pdf">🧠 Sapiens Global Archive Reader ↗</a>
              <a href="https://archive.org/details/sapiens-a-brief-history-of-humankind-by-yuval-noah-harari" target="_blank" rel="noopener noreferrer" class="btn-pdf-sub">📖 Digital Lending Edition ↗</a>
            </div>
          </div>
          <div class="book-actions">
            <a href="practice.html?book=harari" class="btn btn-primary">🎯 Prehistory MCQs</a>
            <a href="practice.html?mode=mains&book=harari" class="btn btn-outline">✍️ Mains Synthesis</a>
            <a href="timeline.html#prehistoric-age" class="btn btn-outline">⏱️ Deep Timeline</a>
            <a href="map.html" class="btn btn-outline">🗺️ Paleolithic Map</a>
          </div>
        </div>

        <!-- Book 19: The Story of My Experiments with Truth by M.K. Gandhi -->
        <div class="book-card" data-category="modern">
          <div class="book-header">
            <span class="book-icon">🕊️</span>
            <span class="book-badge" style="background:#fffbeb; color:#b45309;">Primary Source &amp; Ethics</span>
          </div>
          <h2 class="book-title">The Story of My Experiments with Truth</h2>
          <div class="book-author">Mohandas Karamchand Gandhi (Navajivan Publishing House)</div>
          <div class="book-syllabus">Target: Gandhian Philosophy &bull; Satyagraha &bull; Non-Violent Mass Mobilization &bull; GS-4 Ethics</div>
          <p class="book-desc">
            The foundational primary autobiography detailing Mahatma Gandhi's moral, spiritual, and political evolution. Explains the core principles of Satyagraha, Ahimsa, Sarvodaya (inspired by Ruskin), non-resistance to evil (Tolstoy), the South African struggles, Champaran, and the spiritualization of Indian politics.
          </p>
          <div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes</h4>
            <ul>
              <li><strong>Formative Crucible:</strong> London experiments; Ruskin's 'Unto This Last' (Sarvodaya); Tolstoy's 'Kingdom of God is Within You'; Thoreau's 'Civil Disobedience'; Raychandbhai's guidance.</li>
              <li><strong>South African Campaign (1893–1914):</strong> Natal Indian Congress; Indian Opinion; Phoenix Settlement &amp; Tolstoy Farm; Satyagraha against Asiatic Registration and marriage laws.</li>
              <li><strong>Indian Mass Satyagrahas:</strong> Champaran (1917 Tinkathia abolition), Ahmedabad Mill Strike (1918 hunger strike), Kheda (1918 revenue refusal), Rowlatt Satyagraha, and Non-Cooperation.</li>
              <li><strong>Constructive Programme:</strong> Khadi and Charkha (decentralized swadeshi), Harijan upliftment (eradication of untouchability), Hindu-Muslim unity, basic education (Nai Talim), Trusteeship.</li>
            </ul>
          </div>
          <div class="book-pdf-box">
            <div class="pdf-box-head">
              <span class="pdf-tag">📥 Official Navajivan Trust Open Access</span>
              <span class="pdf-source">Gandhi Heritage Portal / Navajivan Trust</span>
            </div>
            <div class="pdf-links-row">
              <a href="https://www.gandhiheritageportal.org/the-story-of-my-experiments-with-truth" target="_blank" rel="noopener noreferrer" class="btn-pdf">🕊️ Official Gandhi Heritage Portal PDF ↗</a>
              <a href="https://archive.org/details/TheStoryOfMyExperimentsWithTruthByMahatmaGandhi" target="_blank" rel="noopener noreferrer" class="btn-pdf-sub">📖 Archive Complete Autobiography ↗</a>
            </div>
          </div>
          <div class="book-actions">
            <a href="practice.html?book=gandhi" class="btn btn-primary">🎯 Gandhian MCQs</a>
            <a href="practice.html?mode=mains&book=gandhi" class="btn btn-outline">✍️ Ethics &amp; Mains Qs</a>
            <a href="timeline.html#mahatma-gandhi" class="btn btn-outline">⏱️ Gandhi Timeline</a>
            <a href="map.html" class="btn btn-outline">🗺️ Satyagraha Map</a>
          </div>
        </div>

        <!-- Book 20: Pratik Nayak's Visual History & Modern India Lecture Compendiums -->
        <div class="book-card" data-category="modern world">
          <div class="book-header">
            <span class="book-icon">📊</span>
            <span class="book-badge" style="background:#eff6ff; color:#1d4ed8;">Visual Frameworks &amp; Flowcharts</span>
          </div>
          <h2 class="book-title">Modern India &amp; World History Master Compendiums</h2>
          <div class="book-author">Pratik Nayak (Visual Frameworks, Chronological Pipelines &amp; UPSC Compendium)</div>
          <div class="book-syllabus">Target: UPSC Prelims &amp; Mains GS-1 &bull; Visual Cause-Effect Flowcharts &bull; Constitutional Evolutions</div>
          <p class="book-desc">
            The acclaimed, comprehensive visual lecture compendiums synthesizing Modern Indian History, the Indian National Movement, and World History into structured cause-and-effect flowcharts, chronological pipelines, comparative matrices, and high-yield Prelims-to-Mains analytical nodes.
          </p>
          <div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes</h4>
            <ul>
              <li><strong>Conquest to Nationalism Pipelines:</strong> European entry (Plassey, Buxar) -> British Doctrines (Subsidiary Alliance, Lapse) -> Land Revenue (Zamindari, Ryotwari, Mahalwari) -> Drain of Wealth -> 1857 Revolt -> Pre-Congress associations -> Moderate-Extremist split.</li>
              <li><strong>Revolutionary Movements Matrix:</strong> Systematic comparative breakdown of Phase I (1907-17: Anushilan, Ghadar, Komagata Maru) vs Phase II (1920s-30s: HSRA, Bhagat Singh, Chittagong Raid).</li>
              <li><strong>Constitutional Deadlock Pipeline (1920–1947):</strong> Swarajists vs No-Changers -> Simon Commission -> Nehru Report -> 14 Points -> Lahore Purna Swaraj -> Salt Satyagraha -> Karachi Session 1931 -> RTCs &amp; Poona Pact -> 1935 Act -> August Offer -> Cripps -> Quit India 1942 -> INA Trials &amp; RIN Mutiny 1946 -> Cabinet Mission -> Partition.</li>
              <li><strong>World History Revolutions:</strong> Three Estates to Reign of Terror (French Revolution); American Revolution &amp; Civil War with US-India Constitutional comparisons; Italian &amp; German Unifications; Russian 1917 Revolutions; WWI &amp; WWII.</li>
            </ul>
          </div>
          <div class="book-pdf-box">
            <div class="pdf-box-head">
              <span class="pdf-tag">📥 Integrated Study Platform</span>
              <span class="pdf-source">Interactive Digital Atlas &amp; Visual Flowcharts</span>
            </div>
            <div class="pdf-links-row">
              <a href="timeline.html" class="btn-pdf">📊 Launch Master Visual Timeline ↗</a>
              <a href="practice.html" class="btn-pdf-sub">🎯 Launch Prelims &amp; Mains Drills ↗</a>
            </div>
          </div>
          <div class="book-actions">
            <a href="practice.html?book=pratik-nayak" class="btn btn-primary">🎯 All Freedom Struggle MCQs</a>
            <a href="practice.html?mode=mains&book=pratik-nayak" class="btn btn-outline">✍️ Mains Frameworks</a>
            <a href="timeline.html#indian-freedom-struggle" class="btn btn-outline">⏱️ Visual Pipeline</a>
            <a href="graph.html" class="btn btn-outline">🕸️ Knowledge Graph</a>
          </div>
        </div>
'''

content = content.replace('        <!-- Book 15: From Plassey to Partition and After by Sekhar Bandyopadhyay -->', new_cards + '\n        <!-- Book 15: From Plassey to Partition and After by Sekhar Bandyopadhyay -->')

with open('books.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated books.html successfully!")
