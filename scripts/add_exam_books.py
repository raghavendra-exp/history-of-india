# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('books.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update titles & header
content = content.replace(
    'The 23 Canonical Textbooks & Compendiums Study Hub — Complete History of India',
    'The 27 Canonical Textbooks & Compendiums Study Hub — Complete History of India'
)
content = content.replace(
    'The Canonical Textbooks Study Hub (23 Master Books & Culture Compendiums)',
    'The Canonical Textbooks Study Hub (27 Master Books & Competitive Exam Compendiums)'
)
content = content.replace(
    'Every single concept, chronological period, art tradition, sociological dimension, and practice question across this platform is rigorously mapped to the 23 canonical standard textbooks and master culture compendiums',
    'Every single concept, chronological period, art tradition, sociological dimension, and practice question across this platform is rigorously mapped to the 27 canonical standard textbooks and competitive examination archives (UPSC, UPPSC, UP RO/ARO, Bank IBPS/SBI, Railway RRB NTPC)'
)

# 2. Update filter bar
old_filter = '''      <div class="filter-bar" id="booksFilterBar">
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

new_filter = '''      <div class="filter-bar" id="booksFilterBar">
        <button class="filter-chip active" onclick="filterBooks('all', this)">All 27 Books &amp; Compendiums (27)</button>
        <button class="filter-chip" onclick="filterBooks('ncert', this)">NCERT Foundations (5)</button>
        <button class="filter-chip" onclick="filterBooks('ancient', this)">Ancient India (4)</button>
        <button class="filter-chip" onclick="filterBooks('medieval', this)">Medieval India (2)</button>
        <button class="filter-chip" onclick="filterBooks('modern', this)">Modern India (6)</button>
        <button class="filter-chip" onclick="filterBooks('post-independence', this)">Post-Independence (1)</button>
        <button class="filter-chip" onclick="filterBooks('art', this)">Art &amp; Culture (4)</button>
        <button class="filter-chip" onclick="filterBooks('society', this)">Indian Society (3)</button>
        <button class="filter-chip" onclick="filterBooks('world', this)">World History (3)</button>
        <button class="filter-chip" onclick="filterBooks('exam-compendium', this)">Exam Archives &amp; PYQs (4)</button>
      </div>'''

content = content.replace(old_filter, new_filter)

# 3. Exam Book Cards
exam_cards = '''
        <!-- Book 24: Ghatna Chakra Samanya Adhyayan Purvavalokan -->
        <div class="book-card" data-category="exam-compendium modern ancient medieval">
          <div class="book-header">
            <span class="book-icon">📜</span>
            <span class="book-badge" style="background:#fee2e2; color:#b91c1c;">State Commission Benchmark</span>
          </div>
          <h2 class="book-title">Samanya Adhyayan Purvavalokan: Bharatiya Itihas &amp; UP Special</h2>
          <div class="book-author">Sam-Samayik Ghatna Chakra Editorial Board (Prayagraj)</div>
          <div class="book-syllabus">Target: UPPSC PCS &bull; UP RO/ARO (Samiksha Adhikari) &bull; BPSC &bull; MPPSC &bull; RAS</div>
          <p class="book-desc">
            The undisputed gold-standard previous-year question compendium for Uttar Pradesh Public Service Commission (UPPSC) and State Civil Services. Synthesizes over 30 years of authentic solved papers classified chronologically and conceptually, featuring rigorous explanations, commission answer keys, and district-level historical breakdowns.
          </p>
          <div class="book-chapters">
            <h4>Core Exam Modules &amp; Coverage</h4>
            <ul>
              <li><strong>Pracheen Bharat:</strong> Stone Age to Guptas with special focus on Belan Valley, Koldihwa, Chopani Mando, and ancient Mahajanapada capitals in Uttar Pradesh.</li>
              <li><strong>Madhyakaleen Bharat:</strong> Delhi Sultanate, Sharqi Dynasty of Jaunpur, Mughal Agra/Fatehpur Sikri, and Awadh Nawabi architecture.</li>
              <li><strong>Adhunik Bharat &amp; Rashtriya Andolan:</strong> 1857 leaders in UP (Meerut, Jhansi, Lucknow, Kanpur, Bareilly, Faizabad), Kakori Train Action (1925), Chauri Chaura (1922), and Ballia Parallel Government (1942).</li>
              <li><strong>Uttar Pradesh Vishesh:</strong> Historic fairs (Kumbh, Bateshwar, Nauchandi), folk arts (Charkula, Kajari, Alha), and literary icons.</li>
            </ul>
          </div>
          <div class="book-pdf-box">
            <div class="pdf-box-head">
              <span class="pdf-tag">📥 Purvavalokan Integration</span>
              <span class="pdf-source">State PSC &amp; RO/ARO Solved Papers</span>
            </div>
            <div class="pdf-links-row">
              <a href="practice.html?exam=ro-aro" class="btn-pdf">📜 Practice UP RO/ARO Questions ↗</a>
              <a href="practice.html?exam=uppsc" class="btn-pdf-sub">🏛️ Practice UPPSC PCS MCQs ↗</a>
            </div>
          </div>
          <div class="book-actions">
            <a href="practice.html?book=ghatna-chakra" class="btn btn-primary">🎯 Solved MCQs</a>
            <a href="up-history.html" class="btn btn-outline">🏛️ UP History Track</a>
            <a href="timeline.html" class="btn btn-outline">⏱️ Chronology</a>
          </div>
        </div>

        <!-- Book 25: History of Indian Banking & Financial Systems -->
        <div class="book-card" data-category="exam-compendium modern">
          <div class="book-header">
            <span class="book-icon">🏦</span>
            <span class="book-badge" style="background:#e0f2fe; color:#0369a1;">Banking &amp; Financial History</span>
          </div>
          <h2 class="book-title">History of Indian Banking &amp; Financial Systems</h2>
          <div class="book-author">Reserve Bank of India Historical Archives &amp; Banking Awareness Editorial Board</div>
          <div class="book-syllabus">Target: IBPS PO / Clerk &bull; SBI PO / Clerk &bull; RBI Grade B &bull; NABARD &bull; SEBI Grade A</div>
          <p class="book-desc">
            The definitive examination compendium covering the evolutionary history of banking, central banking, and financial regulation in India. Traces the timeline from the Bank of Hindostan (1770) and Presidency Banks to the Imperial Bank of India, the creation of the Reserve Bank of India (1935), post-independence nationalization waves (1969 &amp; 1980), and modern financial reforms.
          </p>
          <div class="book-chapters">
            <h4>Core Banking Modules &amp; Coverage</h4>
            <ul>
              <li><strong>Pre-Independence Era:</strong> Agency houses, Bank of Hindostan (1770), Presidency Banks amalgamation into Imperial Bank of India (1921), Oudh Commercial Bank (1881), and Punjab National Bank (1894).</li>
              <li><strong>Reserve Bank of India Genesis:</strong> Hilton Young Commission (1926), RBI Act 1934, operations commencement (1 April 1935), and nationalization (1 January 1949).</li>
              <li><strong>Nationalization &amp; Institutional Expansion:</strong> SBI Act 1955, 14 Banks nationalized (19 July 1969), 6 Banks nationalized (15 April 1980), Regional Rural Banks (Prathama Bank 1975), and NABARD (1982).</li>
              <li><strong>Banking Committees &amp; Modern Frameworks:</strong> M. Narasimham Committee I (1991) &amp; II (1998), Urjit Patel Committee (MPC inflation targeting), Nachiket Mor Committee (Payments &amp; SFBs), and Bimal Jalan Committee (2019).</li>
            </ul>
          </div>
          <div class="book-pdf-box">
            <div class="pdf-box-head">
              <span class="pdf-tag">📥 Banking Awareness Hub</span>
              <span class="pdf-source">Financial History &amp; Regulatory Frameworks</span>
            </div>
            <div class="pdf-links-row">
              <a href="practice.html?exam=bank" class="btn-pdf">🏦 Launch Banking Awareness MCQs ↗</a>
              <a href="practice.html?book=banking-awareness" class="btn-pdf-sub">🎯 RBI &amp; Banking Questions ↗</a>
            </div>
          </div>
          <div class="book-actions">
            <a href="practice.html?exam=bank" class="btn btn-primary">🏦 Practice Banking MCQs</a>
            <a href="practice.html?book=banking-awareness" class="btn btn-outline">🎯 RBI Archives</a>
            <a href="themes.html" class="btn btn-outline">📊 Economic History</a>
          </div>
        </div>

        <!-- Book 26: Railway Recruitment Board (RRB NTPC) General Awareness -->
        <div class="book-card" data-category="exam-compendium modern ancient medieval">
          <div class="book-header">
            <span class="book-icon">🚆</span>
            <span class="book-badge" style="background:#fef9c3; color:#a16207;">Railway Heritage &amp; GS</span>
          </div>
          <h2 class="book-title">Railway Recruitment Board (RRB NTPC &amp; Group D) Master Archive</h2>
          <div class="book-author">Railway Recruitment Board Examination Research Group &amp; Lucent GS Compendium</div>
          <div class="book-syllabus">Target: RRB NTPC (Stages 1 &amp; 2) &bull; RRB Group D &bull; RRB ALP &bull; RRB JE &bull; RPF SI/Constable</div>
          <p class="book-desc">
            The comprehensive examination repository synthesized from over two decades of Railway Recruitment Board examinations. Integrates high-frequency historical milestones, dynasties, founders, capitals, decisive battles, historic slogans, and Indian Railway administrative and technical heritage.
          </p>
          <div class="book-chapters">
            <h4>Core Railway GK Modules &amp; Coverage</h4>
            <ul>
              <li><strong>Indian Railway Heritage:</strong> First passenger train (16 April 1853, Bombay to Thane, 34 km, locomotives Sultan, Sindh, Sahib), first electric train (1925), Acworth Committee (1924 Rail Budget separation), Kolkata Metro (1984), and Fairy Queen.</li>
              <li><strong>Ancient Dynasties &amp; Decisive Battles:</strong> Haryanka, Maurya, Gupta, Chola, Rashtrakuta founders and capitals; Battles of Hydaspes, Kalinga, Tarain, Panipat, Plassey, and Buxar.</li>
              <li><strong>Freedom Movement Slogans &amp; Titles:</strong> Historic slogans of Tilak, Gandhi, Bose, Bhagat Singh, and Shastri; titles of Frontier Gandhi, Deshbandhu, Lokmanya, and Iron Man.</li>
              <li><strong>Authors, Monuments &amp; Treaties:</strong> Classical treatises (Arthashastra, Indica, Rajatarangini), travelers (Ibn Battuta, Al-Biruni), and landmark treaties (Purandar, Allahabad, Seringapatam).</li>
            </ul>
          </div>
          <div class="book-pdf-box">
            <div class="pdf-box-head">
              <span class="pdf-tag">📥 Railway Recruitment Board Archive</span>
              <span class="pdf-source">RRB Chapterwise General Awareness</span>
            </div>
            <div class="pdf-links-row">
              <a href="practice.html?exam=rrb" class="btn-pdf">🚆 Launch RRB NTPC Practice ↗</a>
              <a href="practice.html?book=rrb-kiran" class="btn-pdf-sub">🎯 Railway History MCQs ↗</a>
            </div>
          </div>
          <div class="book-actions">
            <a href="practice.html?exam=rrb" class="btn btn-primary">🚆 Practice RRB Questions</a>
            <a href="timeline.html" class="btn btn-outline">⏱️ Interactive Timeline</a>
            <a href="map.html" class="btn btn-outline">🗺️ Historical Map</a>
          </div>
        </div>

        <!-- Book 27: Uttar Pradesh Samanya Gyan & Aitihasik Dharohar -->
        <div class="book-card" data-category="exam-compendium ancient medieval modern">
          <div class="book-header">
            <span class="book-icon">🏛️</span>
            <span class="book-badge" style="background:#ecfdf5; color:#047857;">UP Special GS-5 &amp; 6</span>
          </div>
          <h2 class="book-title">Uttar Pradesh Samanya Gyan &amp; Aitihasik Dharohar</h2>
          <div class="book-author">Dr. Rakesh Saraswat &amp; Uttar Pradesh Information &amp; Public Relations Directorate</div>
          <div class="book-syllabus">Target: UPPSC GS Paper 5 &amp; 6 &bull; UP RO/ARO &bull; UP Police SI &bull; UPSSSC VDO/Lekhpal</div>
          <p class="book-desc">
            The definitive reference work covering the exhaustive archaeological, administrative, dynastic, and socio-cultural history of Uttar Pradesh. Tailored specifically for the newly introduced UPPSC Mains GS Papers 5 &amp; 6 and the UP RO/ARO General Studies paper, detailing districts, historical monuments, folk arts, and freedom struggle leaders.
          </p>
          <div class="book-chapters">
            <h4>Core UPPSC GS-5 &amp; 6 Syllabus Modules</h4>
            <ul>
              <li><strong>Prehistoric &amp; Ancient UP:</strong> Belan Valley, Chopani Mando, Koldihwa, Damdama, Sarai Nahar Rai, Kaushambi, Sarnath, Shravasti, Kushinagar, Ayodhya, and Mathura.</li>
              <li><strong>Medieval Dynasties &amp; Architecture:</strong> Harsha at Kannauj, Gurjara-Pratiharas, Gahadavalas, Jaunpur Sharqi Sultanate (Atala Masjid), Agra &amp; Fatehpur Sikri, and Awadh Nawabs (Bada Imambara, Rumi Darwaza).</li>
              <li><strong>Freedom Struggle &amp; Revolutionary Sites:</strong> 1857 leaders across UP districts, Kakori Train Action (1925), Chauri Chaura (1922), Ballia Parallel Government (1942), and INC sessions in UP.</li>
              <li><strong>Culture, Fairs &amp; Institutions:</strong> Kumbh Mela, Bateshwar, Nauchandi, Shakumbhari, Dev Sharif; Charkula, Karma, Kajari, Alha, Birha; Bhatkhande Sanskriti Vishwavidyalaya and Bharat Kala Bhavan.</li>
            </ul>
          </div>
          <div class="book-pdf-box">
            <div class="pdf-box-head">
              <span class="pdf-tag">📥 UPPSC GS-5 &amp; 6 Comprehensive Track</span>
              <span class="pdf-source">Uttar Pradesh Heritage Directorate</span>
            </div>
            <div class="pdf-links-row">
              <a href="up-history.html" class="btn-pdf">🏛️ Launch UP History Master Track ↗</a>
              <a href="practice.html?category=up-history" class="btn-pdf-sub">🎯 Practice UP Special MCQs ↗</a>
            </div>
          </div>
          <div class="book-actions">
            <a href="up-history.html" class="btn btn-primary">🏛️ Explore UP Track</a>
            <a href="practice.html?category=up-history" class="btn btn-outline">🎯 UP Special MCQs</a>
            <a href="practice.html?exam=ro-aro" class="btn btn-outline">📜 RO/ARO Practice</a>
          </div>
        </div>
'''

content = content.replace('        <!-- Book 15: From Plassey to Partition and After by Sekhar Bandyopadhyay -->', exam_cards + '\n        <!-- Book 15: From Plassey to Partition and After by Sekhar Bandyopadhyay -->')

with open('books.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated books.html with Books 24, 25, 26, 27 successfully!")

# Update index.html CTA
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

idx_content = idx_content.replace('📚 23 Master Books', '📚 27 Master Books & Exam Compendiums')
idx_content = idx_content.replace('📚 20 Master Books', '📚 27 Master Books & Exam Compendiums')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

print("Updated index.html CTA to 27 Master Books & Exam Compendiums!")
