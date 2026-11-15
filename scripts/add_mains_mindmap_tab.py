import re

with open('syllabus.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Navigation Buttons
nav_target = '<button class="syl-nav-btn" onclick="switchSylTab(\'sec-rrb-bank\')">Part B: RRB NTPC &amp; Banking</button>'
new_nav_btn = '''<button class="syl-nav-btn" onclick="switchSylTab('sec-rrb-bank')">Part B: RRB NTPC &amp; Banking</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-mains-mindmap')">Part C: UPSC GS-1 Mains Mind Map &amp; Micro-Topics</button>'''

if nav_target not in html:
    print("ERROR: Nav target not found")
    exit(1)

html = html.replace(nav_target, new_nav_btn)

# 2. Add Mind Map Pane right before the closing </section> of syl-hero or end of panes
pane_target = '''          <div class="syl-action-bar">
            <a href="practice.html?exam=rrb" class="btn btn-primary btn-sm">Practice 940+ Railway NTPC MCQs</a>
            <a href="practice.html?exam=bank" class="btn btn-primary btn-sm">Practice 730+ Banking Awareness MCQs</a>
            <a href="practice.html?category=science-tech" class="btn btn-outline btn-sm">Practice General Science MCQs</a>
          </div>
        </div>
      </div>'''

MINDMAP_PANE = '''

      <!-- =================================================================== -->
      <!-- PART C: UPSC CSE MAINS GS-1 MIND MAP & MICRO-TOPIC BLUEPRINT -->
      <!-- =================================================================== -->
      <div class="syl-section-pane" id="sec-mains-mindmap">
        <div class="section-head">
          <span class="kicker">Part C • Complete Examination Micro-Topic Taxonomy</span>
          <h2>UPSC CSE Mains GS-1 Mind Map &amp; Micro-Topic Navigator</h2>
          <p class="section-desc">Extracted from the master civil services syllabus compendium, this interactive micro-topic navigator deconstructs every single line of UPSC General Studies Paper 1 (Indian Heritage &amp; Culture, History of India &amp; the World, and Indian Society) into high-yield exam modules with canonical textbook mappings and action links.</p>
        </div>

        <!-- Master Mind Map Grid -->
        <div class="syl-card" style="background:var(--bg-raised); border-top: 4px solid var(--accent);">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">GS-1 Master Syllabus Mind Map Tree</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Hierarchical micro-topic breakdown across the 4 foundational pillars of GS Paper 1</p>
            </div>
            <span class="t-cat cat-modern">Complete GS-1 Mind Map</span>
          </div>

          <p>Click any high-yield topic below to explore its essential concepts, analytical dimensions, and recommended sourcebook chapters:</p>

          <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:20px; margin-top:20px;">
            <!-- Pillar 1: Indian Heritage & Culture -->
            <div style="background:var(--bg-sunken); border:1px solid var(--line); border-radius:8px; padding:18px;">
              <h4 style="margin:0 0 12px; color:var(--accent-strong); font-size:1.15rem; display:flex; align-items:center; gap:8px;">
                <span>🏛️</span> 1. Indian Heritage &amp; Culture
              </h4>
              <ul style="padding-left:18px; margin:0; font-size:0.92rem; line-height:1.65;">
                <li><strong>Art Forms:</strong>
                  <ul>
                    <li><em>Ancient:</em> Harappan bronze &amp; steatite seals, Mauryan polished pillars &amp; Yakshas, Post-Mauryan Gandhara vs Mathura vs Amaravati schools, Gupta golden age classical sculpture.</li>
                    <li><em>Medieval:</em> Chola lost-wax bronzes (Nataraja), Mughal miniature karkhanas (Akbar, Jahangir, Shah Jahan), Deccani &amp; Rajasthani schools (Bani Thani, Ragamala).</li>
                    <li><em>Modern:</em> Company school (Patna Qalam), Bengal School (Abanindranath Tagore), Progressive Artists' Group (Husain, Souza), Modernist folk revival (Jamini Roy, Amrita Sher-Gil).</li>
                  </ul>
                </li>
                <li><strong>Literature:</strong>
                  <ul>
                    <li><em>Ancient:</em> Vedic Samhitas, Upanishadic philosophy, Epics (Ramayana, Mahabharata), Buddhist Pitakas &amp; Jatakas, Jain Agamas, Sangam poetry (Ettutogai, Pattuppattu), Classical Sanskrit drama (Kalidasa, Bhasa, Bhavabhuti).</li>
                    <li><em>Medieval:</em> Bhakti-Sufi vernacular explosion (Kabir, Tulsidas's Ramcharitmanas, Guru Nanak, Mirabai, Basavanna's Vachanas), Persian historiography (Ziauddin Barani, Abul Fazl's Akbarnama/Ain-i-Akbari).</li>
                    <li><em>Modern:</em> Vernacular nationalist literature (Bankim Chandra's Anandamath, Rabindranath Tagore, Subramania Bharati, Munshi Premchand, Faiz Ahmad Faiz).</li>
                  </ul>
                </li>
                <li><strong>Architecture:</strong>
                  <ul>
                    <li><em>Ancient:</em> Indus urban grid &amp; hydraulic engineering, Buddhist Stupas (Sanchi, Bharhut, Amaravati) &amp; Rock-cut caves (Barabar, Ajanta, Ellora, Karle), Temple structural styles (Nagara, Dravida, Vesara).</li>
                    <li><em>Medieval:</em> Delhi Sultanate arcuate architecture (true arch, dome, squinch, minaret), Mughal monumental syntheses (Fatehpur Sikri, Taj Mahal), Vijayanagara (Kalyana mandapas, Gopurams).</li>
                    <li><em>Modern:</em> Neo-Classical, Gothic Revival (Victoria Terminus), Indo-Saracenic (Gateway of India, Rashtrapati Bhavan by Lutyens &amp; Baker), Post-Independence Modernism (Le Corbusier's Chandigarh).</li>
                  </ul>
                </li>
              </ul>
            </div>

            <!-- Pillar 2: History of India -->
            <div style="background:var(--bg-sunken); border:1px solid var(--line); border-radius:8px; padding:18px;">
              <h4 style="margin:0 0 12px; color:var(--accent-strong); font-size:1.15rem; display:flex; align-items:center; gap:8px;">
                <span>📜</span> 2. History of India
              </h4>
              <ul style="padding-left:18px; margin:0; font-size:0.92rem; line-height:1.65;">
                <li><strong>Ancient &amp; Medieval Foundations:</strong>
                  <ul>
                    <li>Palaeolithic to Chalcolithic continuum; IVC urbanism &amp; decline; Vedic polity &amp; varna transformation; Second Urbanization &amp; 16 Mahajanapadas; Mauryan imperial statecraft (Arthashastra, Ashoka's Dhamma); Post-Mauryan trade networks &amp; Silk Route; Gupta administration &amp; feudalization; Harsha &amp; regional kingdoms.</li>
                    <li>Early Medieval Tripartite struggle (Palas, Pratiharas, Rashtrakutas); Chola maritime empire &amp; village autonomy (Uttiramerur inscription); Delhi Sultanate administrative institutions (Iqta, Market Reforms of Alauddin Khalji); Vijayanagara statecraft (Nayankara system); Mughal imperial zenith (Mansabdari, Zabt, Sulh-i-Kul) &amp; Maratha Swarajya.</li>
                  </ul>
                </li>
                <li><strong>Modern Indian History (1757 – 1947):</strong>
                  <ul>
                    <li><em>British Conquest &amp; Consolidation:</em> Battles of Plassey (1757) and Buxar (1764); Subsidiary Alliance (Wellesley) &amp; Doctrine of Lapse (Dalhousie); British Land Revenue systems (Permanent Settlement, Ryotwari, Mahalwari); Deindustrialization &amp; Drain of Wealth (Dadabhai Naoroji, R.C. Dutt).</li>
                    <li><em>Popular Resistance &amp; 1857:</em> Pre-1857 Civil, Peasant &amp; Tribal rebellions (Sanyasi, Paika, Santhal Hul); The Great Revolt of 1857 (causes, character, Queen's Proclamation 1858).</li>
                    <li><em>The Freedom Struggle:</em> Moderate Phase (1885–1905, Constitutional agitation); Extremist Phase &amp; Swadeshi Movement (1905–1908); Revolutionary Nationalism (Phase I &amp; II: Bhagat Singh, Surya Sen, Chandrashekhar Azad); Gandhian Mass Movements (Non-Cooperation 1920, Civil Disobedience 1930, Quit India 1942); Subhas Chandra Bose &amp; INA; Constitutional deadlock &amp; Partition 1947.</li>
                  </ul>
                </li>
                <li><strong>Post-Independence Consolidation &amp; Reorganization:</strong>
                  <ul>
                    <li>Integration of 565 Princely States (Sardar Patel &amp; V.P. Menon, Junagadh, Hyderabad Operation Polo, Kashmir Instrument of Accession); States Reorganization Act 1956 (Fazal Ali Commission); Tribal integration (Nehru's Tribal Panchsheel); Official Language dispute; Foreign Policy (Non-Aligned Movement - NAM, Panchsheel); Agrarian &amp; Economic transformation (Land Reforms, Green Revolution, White Revolution).</li>
                  </ul>
                </li>
              </ul>
            </div>

            <!-- Pillar 3: History of the World -->
            <div style="background:var(--bg-sunken); border:1px solid var(--line); border-radius:8px; padding:18px;">
              <h4 style="margin:0 0 12px; color:var(--accent-strong); font-size:1.15rem; display:flex; align-items:center; gap:8px;">
                <span>🌍</span> 3. History of the World
              </h4>
              <ul style="padding-left:18px; margin:0; font-size:0.92rem; line-height:1.65;">
                <li><strong>Key Events from the 18th Century:</strong>
                  <ul>
                    <li><em>Industrial Revolution:</em> Origins in Britain, technological inventions (spinning jenny, steam engine), rise of industrial capitalism, urbanization, working-class exploitation, and global division of labor.</li>
                    <li><em>Atlantic Democratic Revolutions:</em> American Revolution (1776, 'No taxation without representation', Declaration of Independence); French Revolution (1789, Liberty, Equality, Fraternity, Fall of Bastille, Reign of Terror, Rise of Napoleon Bonaparte).</li>
                    <li><em>19th Century Nationalism:</em> Unification of Italy (Mazzini, Garibaldi, Cavour); Unification of Germany (Bismarck's 'Blood and Iron' diplomacy).</li>
                    <li><em>Imperialism &amp; Colonialism:</em> 'Scramble for Africa' (Berlin Conference 1884); Colonization of Southeast Asia; Semi-colonization of China (Opium Wars, Unequal Treaties, Boxer Rebellion).</li>
                    <li><em>20th Century Cataclysms:</em> World War I (causes, Trench warfare, Treaty of Versailles 1919, League of Nations); Russian Revolution (1917, Bolsheviks, Lenin, October Revolution); Interwar Great Depression (1929) &amp; Rise of Fascism (Mussolini) and Nazism (Hitler); World War II (Holocaust, Axis vs Allies, Hiroshima/Nagasaki, Creation of United Nations).</li>
                    <li><em>Decolonization &amp; Cold War:</em> Decolonization in Asia and Africa; Cold War confrontation (USA vs USSR, NATO vs Warsaw Pact, Cuban Missile Crisis); Korean and Vietnam Wars; Fall of Berlin Wall (1989) &amp; Collapse of Soviet Union (1991).</li>
                  </ul>
                </li>
                <li><strong>Political Philosophies &amp; Societal Impacts:</strong>
                  <ul>
                    <li><em>Capitalism:</em> Free market, private ownership, profit motive, laissez-faire (Adam Smith); benefits of innovation vs hazards of monopoly and wealth inequality.</li>
                    <li><em>Socialism:</em> Democratic control of resources, state intervention, equitable distribution, social welfare state (Fabian socialism, Scandinavian model).</li>
                    <li><em>Communism:</em> Scientific socialism (Karl Marx &amp; Friedrich Engels), class struggle, dictatorship of the proletariat, stateless &amp; classless society; practical implementations and authoritarian critiques.</li>
                  </ul>
                </li>
              </ul>
            </div>

            <!-- Pillar 4: Indian Society -->
            <div style="background:var(--bg-sunken); border:1px solid var(--line); border-radius:8px; padding:18px;">
              <h4 style="margin:0 0 12px; color:var(--accent-strong); font-size:1.15rem; display:flex; align-items:center; gap:8px;">
                <span>👥</span> 4. Indian Society &amp; Social Issues
              </h4>
              <ul style="padding-left:18px; margin:0; font-size:0.92rem; line-height:1.65;">
                <li><strong>Salient Features &amp; Diversity of India:</strong>
                  <ul>
                    <li>Composite culture; Pluralism (linguistic, religious, racial, ethnic, regional); Unity in Diversity; Structural resilience of family, marriage, and kinship institutions.</li>
                  </ul>
                </li>
                <li><strong>Role of Women &amp; Women's Organizations:</strong>
                  <ul>
                    <li>Historical trajectory of women's movements (19th c. social reform vs 20th c. nationalist participation vs contemporary rights movements); Self-Help Groups (SHGs, Kudumbashree, Lakhpati Didi); Female Labor Force Participation Rate (FLFPR) dynamics; Care economy; Reproductive rights and legislative safeguards (Protection of Women from Domestic Violence Act, POSH Act, Maternity Benefit Act).</li>
                  </ul>
                </li>
                <li><strong>Population, Poverty &amp; Urbanization:</strong>
                  <ul>
                    <li>Demographic Dividend vs Aging trends; Total Fertility Rate (TFR falling below replacement level of 2.1 in India); Multidimensional Poverty Index (MPI); Urbanization dynamics: unplanned urban sprawl, slums (Dharavi), water stress (Day Zero crisis), urban transport, solid waste management, and smart city interventions.</li>
                  </ul>
                </li>
                <li><strong>Globalization, Social Empowerment &amp; Ideologies:</strong>
                  <ul>
                    <li>Impact of Globalization on family, elderly, youth, food culture ('Glocalization'), and informal labour; Social Empowerment of Scheduled Castes, Scheduled Tribes, OBCs, Persons with Disabilities (PwD), and LGBTQIA+ community; Conceptual dynamics of Communalism (politicization of religion), Regionalism (son-of-the-soil doctrines vs cooperative federalism), and Secularism (principled distance vs Western wall of separation).</li>
                  </ul>
                </li>
              </ul>
            </div>
          </div>

          <!-- Cross-Module Action Links -->
          <div class="syl-action-bar" style="margin-top:24px;">
            <a href="practice.html?mode=mains&book=mrunal" class="btn btn-primary">Practice 287+ UPSC Mains Model Questions &rarr;</a>
            <a href="practice.html" class="btn btn-primary">Practice 8,209+ Prelims MCQs &rarr;</a>
            <a href="art-culture.html" class="btn btn-outline">Explore Art &amp; Culture Hub &rarr;</a>
            <a href="society.html" class="btn btn-outline">Explore Indian Society Hub &rarr;</a>
            <a href="books.html" class="btn btn-outline">View 27 Canonical Textbooks &rarr;</a>
          </div>
        </div>
      </div>'''

html = html.replace(pane_target, pane_target + MINDMAP_PANE)

with open('syllabus.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated syllabus.html with Part C: UPSC GS-1 Mains Mind Map & Micro-Topics!")
