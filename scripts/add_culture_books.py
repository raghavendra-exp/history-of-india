import re

with open('books.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update page title & header
content = content.replace(
    'The 20 Canonical Textbooks & Compendiums Study Hub — Complete History of India',
    'The 23 Canonical Textbooks & Compendiums Study Hub — Complete History of India'
)
content = content.replace(
    'The Canonical Textbooks Study Hub (20 Master Books & Lecture Compendiums)',
    'The Canonical Textbooks Study Hub (23 Master Books & Culture Compendiums)'
)
content = content.replace(
    'Every single concept, chronological period, art tradition, sociological dimension, and practice question across this platform is rigorously mapped to the 20 canonical standard textbooks and master lecture compendiums',
    'Every single concept, chronological period, art tradition, sociological dimension, and practice question across this platform is rigorously mapped to the 23 canonical standard textbooks and master culture compendiums'
)

# Update filter bar
old_filter = '''      <div class="filter-bar" id="booksFilterBar">
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

new_filter = '''      <div class="filter-bar" id="booksFilterBar">
        <button class="filter-chip active" onclick="filterBooks('all', this)">All 23 Books &amp; Compendiums (23)</button>
        <button class="filter-chip" onclick="filterBooks('ncert', this)">NCERT Foundations (5)</button>
        <button class="filter-chip" onclick="filterBooks('ancient', this)">Ancient India (4)</button>
        <button class="filter-chip" onclick="filterBooks('medieval', this)">Medieval India (2)</button>
        <button class="filter-chip" onclick="filterBooks('modern', this)">Modern India (6)</button>
        <button class="filter-chip" onclick="filterBooks('post-independence', this)">Post-Independence (1)</button>
        <button class="filter-chip" onclick="filterBooks('art', this)">Art &amp; Culture (4)</button>
        <button class="filter-chip" onclick="filterBooks('society', this)">Indian Society (3)</button>
        <button class="filter-chip" onclick="filterBooks('world', this)">World History (3)</button>
      </div>'''

content = content.replace(old_filter, new_filter)

# Culture Book Cards
culture_cards = '''
        <!-- Book 21: A Cultural History of India by A.L. Basham -->
        <div class="book-card" data-category="art ancient">
          <div class="book-header">
            <span class="book-icon">🏺</span>
            <span class="book-badge" style="background:#fef3c7; color:#b45309;">Classical Civilization</span>
          </div>
          <h2 class="book-title">A Cultural History of India</h2>
          <div class="book-author">Prof. A.L. Basham (Oxford University Press)</div>
          <div class="book-syllabus">Target: UPSC Heritage &amp; Culture &bull; Ancient Philosophy &bull; Art Traditions &bull; Global Cultural Diffusion</div>
          <p class="book-desc">
            The internationally celebrated master compendium on Indian civilizational history. Authored and edited by the legendary Indologist A.L. Basham, it synthesizes the evolution of Indian religions (Vedic, Buddhist, Jain, Bhakti, Sufi), sculptural and architectural monuments, classical Sanskrit and regional literature, music, science, and the spread of Indian culture across Central and Southeast Asia.
          </p>
          <div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes</h4>
            <ul>
              <li><strong>Philosophy &amp; Religion:</strong> The Upanishadic worldview, heterodox sramana movements (Buddhism and Jainism), Bhakti synthesis, and Islamic cultural fusion.</li>
              <li><strong>Art &amp; Architecture:</strong> The plastic character of Indian art; rock-cut cave shrines (Ajanta, Ellora); bronze casting traditions; classical temple evolution.</li>
              <li><strong>Language &amp; Literature:</strong> Vedic Sanskrit, Epics (Mahabharata, Ramayana), Kavya traditions (Kalidasa, Bhavabhuti), Sangam Tamil poetry, and Persian court literature.</li>
              <li><strong>Global Cultural Reach:</strong> Maritime transmission of Indian philosophy, script, and art forms to Funan, Angkor Wat, Champa, and Borobudur.</li>
            </ul>
          </div>
          <div class="book-pdf-box">
            <div class="pdf-box-head">
              <span class="pdf-tag">📥 Academic Preservation &amp; Reference</span>
              <span class="pdf-source">Oxford University Press / Open Access Archive</span>
            </div>
            <div class="pdf-links-row">
              <a href="https://archive.org/details/culturalhistoryo0000bash" target="_blank" rel="noopener noreferrer" class="btn-pdf">🏺 A.L. Basham: Cultural History Archive Reader ↗</a>
              <a href="https://archive.org/search?query=%22A+Cultural+History+of+India%22+Basham" target="_blank" rel="noopener noreferrer" class="btn-pdf-sub">📖 Digital Lending Library ↗</a>
            </div>
          </div>
          <div class="book-actions">
            <a href="practice.html?book=basham" class="btn btn-primary">🎯 Heritage MCQs</a>
            <a href="practice.html?mode=mains&book=basham" class="btn btn-outline">✍️ Mains Answers</a>
            <a href="art-culture.html" class="btn btn-outline">🎨 Art Hub</a>
            <a href="timeline.html#gupta-age" class="btn btn-outline">⏱️ Classical Era</a>
          </div>
        </div>

        <!-- Book 22: Indian Society by Prof. S.C. Dube -->
        <div class="book-card" data-category="society">
          <div class="book-header">
            <span class="book-icon">👥</span>
            <span class="book-badge" style="background:#ccfbf1; color:#0f766e;">Sociological Foundation</span>
          </div>
          <h2 class="book-title">Indian Society</h2>
          <div class="book-author">Prof. S.C. Dube (National Book Trust, India)</div>
          <div class="book-syllabus">Target: UPSC GS-1 Indian Society &bull; Social Structure &bull; Village Community &bull; Modernization Dynamics</div>
          <p class="book-desc">
            The essential sociological text on the structural foundations, institutional continuities, and contemporary transformations of Indian society. Covers the intricate web of diversity and unity, Varna and Jati dynamics, the traditional village social system (Little and Great Traditions), tribal organization, gender roles, and the impacts of planned development.
          </p>
          <div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes</h4>
            <ul>
              <li><strong>Diversity in Unity:</strong> Racial, linguistic, religious, and regional pluralism synthesizing into shared civilizational underpinnings.</li>
              <li><strong>Social Stratification:</strong> Varna hierarchy, Jati endogamy, ritual purity-pollution, and emerging political assertions of backward classes.</li>
              <li><strong>The Village Community:</strong> Field studies (Shamirpet village study), interdependence of occupational castes (Jajmani ties), and village autonomy vs macro-linkages.</li>
              <li><strong>Tribal India &amp; Social Change:</strong> Tribal classification (geographical, linguistic, racial), isolation vs assimilation debate, and forces of modernization, urbanization, and industrialization.</li>
            </ul>
          </div>
          <div class="book-pdf-box">
            <div class="pdf-box-head">
              <span class="pdf-tag">📥 National Book Trust Digital Reference</span>
              <span class="pdf-source">National Book Trust &amp; Open Educational Library</span>
            </div>
            <div class="pdf-links-row">
              <a href="https://archive.org/search?query=%22Indian+Society%22+S.C.+Dube" target="_blank" rel="noopener noreferrer" class="btn-pdf">👥 S.C. Dube: Indian Society Archive ↗</a>
              <a href="society.html" class="btn-pdf-sub">📊 Open Society Hub Module ↗</a>
            </div>
          </div>
          <div class="book-actions">
            <a href="practice.html?book=dube" class="btn btn-primary">🎯 Society MCQs</a>
            <a href="practice.html?mode=mains&book=dube" class="btn btn-outline">✍️ Mains Sociological Qs</a>
            <a href="society.html" class="btn btn-outline">👥 Society Hub</a>
            <a href="timeline.html#india-1947-1964" class="btn btn-outline">⏱️ Social Reforms</a>
          </div>
        </div>

        <!-- Book 23: Ishani Pandya's Visual Art & Culture Master Compendiums -->
        <div class="book-card" data-category="art">
          <div class="book-header">
            <span class="book-icon">🎨</span>
            <span class="book-badge" style="background:#fce7f3; color:#be185d;">Visual Lecture Frameworks</span>
          </div>
          <h2 class="book-title">Art, Architecture &amp; Culture Master Compendiums</h2>
          <div class="book-author">Ishani Pandya (Visual Arts, Sculpture, Paintings, Classical Dance &amp; Puppetry)</div>
          <div class="book-syllabus">Target: UPSC Prelims &amp; Mains GS-1 &bull; Visual Art Forms &bull; Sculptural Schools &bull; Performing Arts</div>
          <p class="book-desc">
            The acclaimed, highly structured visual lecture series synthesizing Indian Art and Culture into crystal-clear classification schemes, visual matrices, and exam-focused comparative tables. Covers Indus to Mughal architecture, Gandhara vs. Mathura vs. Amaravati schools, cave architecture, mural/miniature/folk paintings, the 8 classical dances, and Indian puppetry.
          </p>
          <div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes</h4>
            <ul>
              <li><strong>Architecture &amp; Sculpture:</strong> Harappan lost-wax bronzes and town planning; Ashokan pillars vs Achaemenian; Gandhara, Mathura, and Amaravati sculptural schools; Nagara, Dravida, and Vesara temple anatomy; Indo-Islamic architectural elements (trabeate vs arcuate).</li>
              <li><strong>Cave Architecture:</strong> Chaitya vs Vihara evolution; Karle, Bhaja, Kanheri, Ajanta, Ellora, Elephanta, and Udayagiri/Khandagiri.</li>
              <li><strong>Painting Traditions:</strong> Murals (Ajanta tempera technique, Ellora, Bagh, Sittanavasal, Lepakshi); Miniatures (Pala, Western Indian, Mughal Tasvir Khana, Rajasthani, Pahari); Folk art (Madhubani, Warli, Kalamkari, Pattachitra).</li>
              <li><strong>Performing Arts &amp; Puppetry:</strong> The 8 Classical Dances (Bharatanatyam, Kathakali, Kathak, Odissi, Kuchipudi, Manipuri, Mohiniyattam, Sattriya); 4 Puppetry Forms (String: Kathputli; Shadow: Tholu Bommalata; Rod: Putul Nach; Glove: Pavakoothu).</li>
            </ul>
          </div>
          <div class="book-pdf-box">
            <div class="pdf-box-head">
              <span class="pdf-tag">📥 Integrated Culture Platform</span>
              <span class="pdf-source">Indian Heritage &amp; Culture Hub</span>
            </div>
            <div class="pdf-links-row">
              <a href="art-culture.html" class="btn-pdf">🎨 Launch Complete Art &amp; Culture Hub ↗</a>
              <a href="practice.html?category=art-culture" class="btn-pdf-sub">🎯 Practice Culture MCQs ↗</a>
            </div>
          </div>
          <div class="book-actions">
            <a href="practice.html?book=ishani-pandya" class="btn btn-primary">🎯 Culture MCQs</a>
            <a href="practice.html?mode=mains&book=ishani-pandya" class="btn btn-outline">✍️ Mains Frameworks</a>
            <a href="art-culture.html#comparisons" class="btn btn-outline">⚖️ Comparative Tables</a>
            <a href="map.html" class="btn btn-outline">🗺️ Heritage Map</a>
          </div>
        </div>
'''

content = content.replace('        <!-- Book 15: From Plassey to Partition and After by Sekhar Bandyopadhyay -->', culture_cards + '\n        <!-- Book 15: From Plassey to Partition and After by Sekhar Bandyopadhyay -->')

with open('books.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated books.html with Books 21, 22, 23 successfully!")
