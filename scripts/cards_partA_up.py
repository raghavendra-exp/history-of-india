# -*- coding: utf-8 -*-
"""
cards_partA_up.py
Part A: Uttar Pradesh State-Specific History, Heritage & Culture (4 Granular Units)
"""

def get_partA_html():
    return '''
      <!-- =================================================================== -->
      <!-- PART A: UTTAR PRADESH STATE-SPECIFIC HISTORY & CULTURE (4 Units) -->
      <!-- =================================================================== -->
      <div class="syl-section-pane" id="sec-up">
        <div class="section-head">
          <span class="kicker">Part A • UPPSC PCS GS Papers 5 &amp; 6 • RO/ARO State Track • 4 Dedicated Units</span>
          <h2>Uttar Pradesh History, Heritage &amp; Cultural Legacy</h2>
        </div>

        <!-- Unit 1 -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">1. Ancient and Prehistoric Heritage of Uttar Pradesh</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Belan Valley Stratigraphy, Lahuradewa Rice c. 7000 BCE, Sanauli Bronze Age Chariots, 8 of 16 Mahajanapadas &amp; Mathura Art</p>
            </div>
            <span class="t-cat cat-up">Unit A.1 • UP Ancient</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/up_prehistoric.png" alt="Prehistoric and Ancient Heritage of Uttar Pradesh" onerror="this.onerror=null; this.src='assets/images/history.png';">
          </div>
          <ul>
            <li><strong>Prehistoric Discoveries in Uttar Pradesh:</strong>
              <ul>
                <li><em>The Belan Valley (Prayagraj / Mirzapur border):</em> One of the world's rare uninterrupted stratigraphic sequences excavated by Prof. G.R. Sharma (University of Allahabad); presents a continuous cultural succession from the Lower Palaeolithic through Middle and Upper Palaeolithic, Mesolithic, to the Neolithic age; site of <strong>Chopani Mando</strong> (transition from food foraging to primitive food production with circular bee-hive huts and wild rice grains) and <strong>Koldihwa</strong> (yielding cord-impressed pottery and domesticated rice grains dated to c. 6500–5000 BCE).</li>
                <li><em>Mesolithic Riverine Settlements (Pratapgarh District):</em> <strong>Sarai Nahar Rai</strong> (earliest documented Mesolithic human skeletal remains in India; microliths; evidence of tribal skirmishes / traumatic skull injuries; microlithic graves with heads pointing west); <strong>Mahadaha</strong> (extended human burials with bone ornaments, earrings, and necklaces made of stag antlers; butchery areas); <strong>Damdama</strong> (excavated 41 human graves including unique double burials of male-female pairs buried together).</li>
                <li><em>Lahuradewa (Sant Kabir Nagar District):</em> Breakthrough archaeological excavation by UP State Archaeology Department yielding carbon-14 dates pushing the origin of <strong>domesticated rice agriculture in South Asia back to c. 7000–6000 BCE</strong>, disproving the earlier Eurocentric view that rice farming migrated into India from the Yangtze River valley in China.</li>
                <li><em>Alamgirpur (Meerut District, Hindon River):</em> Excavated by Y.D. Sharma (1958); represents the absolute <strong>easternmost boundary of the Indus Valley Civilization</strong>; yielded Harappan copper tools, pottery with textile impressions, and terracotta cakes.</li>
                <li><em>Sanauli (Baghpat District):</em> Sensational ASI excavations (2018 under Dr. Sanjay Manjul): unearthing of three full-scale <strong>Bronze Age solid-disk wheeled war chariots</strong>, anthropomorphic copper antennae swords, shields, helmets, and royal copper-sheeted coffins (c. 2000–1800 BCE), confirming sophisticated indigenous martial elite culture in the Gangetic Doab contemporaneous with the Late Harappan era.</li>
              </ul>
            </li>
            <li><strong>8 of the 16 Mahajanapadas Located in Uttar Pradesh:</strong>
              <div class="up-table-wrap">
                <table class="up-table">
                  <thead>
                    <tr>
                      <th>Mahajanapada</th>
                      <th>Capital City</th>
                      <th>Modern UP District / Region</th>
                      <th>Historical &amp; Cultural Significance</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr><td><strong>1. Kashi</strong></td><td>Varanasi</td><td>Varanasi, Chandauli</td><td>Ancient textile and ivory manufacturing hub on the holy Ganga; long-standing rival of Kosala.</td></tr>
                    <tr><td><strong>2. Kosala</strong></td><td>Shravasti (North) / Ayodhya (South)</td><td>Faizabad, Ayodhya, Gonda, Bahraich</td><td>Kingdom of Ikshvaku dynasty (Sri Rama); ruled by King Prasenjit; Buddha spent 25 rainy season retreats (Vassavasa) at Jetavana monastery in Shravasti.</td></tr>
                    <tr><td><strong>3. Vatsa</strong></td><td>Kaushambi</td><td>Prayagraj, Kaushambi</td><td>Ruled by King Udayana (hero of Bhasa's <em>Svapnavasavadatta</em>); celebrated brick fortification walls; visited by Buddha; Ghoshitarama monastery.</td></tr>
                    <tr><td><strong>4. Malla</strong></td><td>Kushinagar &amp; Pava</td><td>Kushinagar, Deoria, Gorakhpur</td><td>Oligarchic Ganasangha republic; site of Lord Buddha's Mahaparinirvana (Kushinagar) and Lord Mahavira's Nirvana (Pavapuri/Pava).</td></tr>
                    <tr><td><strong>5. Panchala</strong></td><td>Ahichchhatra (Bareilly) / Kampilya (Farrukhabad)</td><td>Bareilly, Badaun, Farrukhabad</td><td>Divided by the Ganga into North and South Panchala; Draupadi's homeland; center of Later Vedic scholarship and Painted Grey Ware (PGW).</td></tr>
                    <tr><td><strong>6. Kuru</strong></td><td>Hastinapur / Indraprastha</td><td>Meerut, Baghpat, Ghaziabad</td><td>Legendary realm of the Mahabharata war; capital Hastinapur excavated by B.B. Lal (1950–52) revealing PGW culture and flood abandonment.</td></tr>
                    <tr><td><strong>7. Shurasena</strong></td><td>Mathura</td><td>Mathura, Agra</td><td>Ruled by King Avantiputra; birthplace of Lord Krishna; epic center of the Yadava clan and junction of Uttarapatha and Dakshinapatha trade routes.</td></tr>
                    <tr><td><strong>8. Chedi</strong></td><td>Shuktimati (Sothivati)</td><td>Bundelkhand (Banda, Jhansi)</td><td>Ruled by King Shishupala (slain by Krishna in Mahabharata); branch migrated to Kalinga under Kharavela.</td></tr>
                  </tbody>
                </table>
              </div>
            </li>
            <li><strong>Sacred Buddhist Heritage Hubs in Uttar Pradesh:</strong>
              <ul>
                <li><em>Sarnath (Mrigadava / Isipatana, Varanasi):</em> Site where Siddhartha Gautama preached his historic <strong>First Sermon (Dharmachakrapravartana)</strong> to the five ascetics; established the Buddhist Sangha; site of the towering Dhamek Stupa and Ashoka's Lion Capital.</li>
                <li><em>Kushinagar:</em> Site where Gautama Buddha attained <strong>Mahaparinirvana</strong> (death/final liberation) at age 80 under twin Sala trees; home to the Mahaparinirvana Temple housing the colossal 6.1-meter reclining Buddha statue carved from Chunar sandstone, and the Ramabhar Stupa (cremation stupa).</li>
                <li><em>Shravasti:</em> Site of the Miracle of Shravasti; Buddha spent 25 rainy seasons at Jetavana monastery gifted by merchant Anathapindika.</li>
                <li><em>Kaushambi:</em> Ghoshitarama monastery where Buddha stayed during his 6th and 9th regnal years; Ashokan pillar relocated to Allahabad Fort.</li>
                <li><em>Sankisa (Farrukhabad):</em> Sacred Buddhist site where Buddha is believed to have descended back to earth from Trayastrimsha heaven down a jeweled triple ladder; Ashokan elephant capital discovered.</li>
              </ul>
            </li>
            <li><strong>The Mathura School of Ancient Art:</strong> Indigenous sculptural school that flourished from the 2nd century BCE to the 6th century CE under the Shungas, Kushanas, and Guptas; carved exclusively from locally quarried <strong>spotted red sandstone</strong> from Sikri; sculpted the earliest indigenous anthropomorphic images of Buddha (robust, muscular, smiling face, shaved head, right hand raised in Abhay mudra, modeled on indigenous Yaksha prototypes); pioneered Jain <em>Ayagapatas</em> (votive stone slabs carved with Tirthankaras and Ashta-Mangala symbols); produced colossal royal portraits of Kushana emperors (headless statue of King Kanishka wearing nomad tunic and heavy boots, Mat sanctuary).</li>
          </ul>
          <div class="syl-action-bar">
            <a href="period.html?id=up-prehistoric" class="btn btn-outline btn-sm">Explore UP Prehistoric Period →</a>
            <a href="practice.html?category=up-history" class="btn btn-primary btn-sm">Practice UP Ancient History MCQs</a>
          </div>
        </div>

        <!-- Unit 2 -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">2. Medieval History of Uttar Pradesh and the Sharqi Kingdom</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Jaunpur Sharqi Sultanate (Shiraz-i-Hind), Atala Masjid Pylon Architecture, Mughal Agra Capital &amp; Awadh Imambaras</p>
            </div>
            <span class="t-cat cat-up">Unit A.2 • UP Medieval</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/up_jaunpur_saltante.png" alt="Medieval History of UP and Jaunpur Sultanate" onerror="this.onerror=null; this.src='assets/images/history.png';">
          </div>
          <ul>
            <li><strong>The Sharqi Sultanate of Jaunpur (1394–1479 CE):</strong>
              <ul>
                <li><em>Foundation &amp; Political Independence:</em> Founded by eunuch noble <strong>Malik Sarwar</strong> (given title <em>Sultan-us-Sharq</em> / King of the East by Firoz Shah Tughlaq's son); declared independence during Timur's invasion; ruled an autonomous kingdom stretching from Bihar to Aligarh.</li>
                <li><em>"Shiraz-i-Hind" (The Shiraz of the East):</em> Under <strong>Sultan Ibrahim Shah Sharqi (1402–1440)</strong> and Sultan Husain Shah Sharqi, Jaunpur blossomed into India's premier center of Islamic scholarship, Persian literature, classical music, and architecture, rivaling the Persian city of Shiraz; produced eminent scholars like Qazi Shihabuddin Daulatabadi. Husain Shah Sharqi was a musical genius credited with inventing the <em>Khyal</em> style of singing and creating melodic ragas: Jaunpuri Todi, Jaunpuri Asavari, and Husaini.</li>
                <li><em>Distinctive Sharqi Architectural Style:</em>
                  <ul>
                    <li>Complete absence of minarets; instead, monuments are dominated by a colossal, battered sloping <strong>Propylon / Pylon Screen</strong> (monumental arched gateway with recessed tiered arches) soaring high above the central prayer hall, totally concealing the main dome behind it.</li>
                    <li><strong>Atala Masjid (Jaunpur, built 1408 by Ibrahim Shah Sharqi):</strong> Masterpiece of Sharqi architecture, built on the foundations of the ancient Atala Devi temple; characterized by its 75-foot towering propylon screen, two-storey cloistered arcades, and fine stone lattice jali work.</li>
                    <li><em>Other Monuments:</em> Jami Masjid (1478), Lal Darwaza Masjid (built 1450 by Queen Bibi Raji), and the historic Shahi Bridge (Akbari Pul) over the Gomti river built by Munim Khan under Akbar.</li>
                  </ul>
                </li>
                <li><em>Fall of Jaunpur:</em> Annexed back to Delhi Sultanate by Bahlul Lodi in 1479; Ibrahim Lodi destroyed many Sharqi secular palaces.</li>
              </ul>
            </li>
            <li><strong>Uttar Pradesh as the Imperial Heart of the Mughal Empire:</strong>
              <ul>
                <li><em>Agra (Akbarabad) as Capital:</em> Founded by Sikandar Lodi (1504); transformed into the grand imperial capital of the Mughal Empire by Akbar, Jahangir, and Shah Jahan.
                  <ul>
                    <li><strong>Agra Fort:</strong> Constructed in red sandstone by Akbar (1565–1573); contains Jahangiri Mahal, Khas Mahal, Diwan-i-Aam, Diwan-i-Khas, and the marble Moti Masjid (built by Shah Jahan).</li>
                    <li><strong>Fatehpur Sikri:</strong> Founded by Akbar in 1571 to honor Sufi saint Sheikh Salim Chishti who blessed him with a son (Jahangir); served as imperial capital until 1585; built entirely in red Sikri sandstone: monumental <strong>Buland Darwaza</strong> (54-meter high gateway commemorating Gujarat conquest), white marble Tomb of Salim Chishti, Panch Mahal (five-storey pyramidal open pavilion), Jodha Bai's Palace, Birbal's House, and Diwan-i-Khas with its iconic central lotus-pillar throne.</li>
                    <li><strong>The Taj Mahal:</strong> Built by Shah Jahan on the banks of Yamuna in Agra (1632–1653) as the mausoleum for beloved empress Mumtaz Mahal (Arjumand Banu Begum); UNESCO World Heritage site and Wonder of the World; constructed from pure white Makrana marble inlaid with semi-precious stones (Pietra Dura).</li>
                    <li><strong>Tomb of Itimad-ud-Daulah (Agra):</strong> Built by Empress Nur Jahan for her father Mirza Ghiyas Beg (1622–1628); known as the "Baby Taj" or jewel-box; first Mughal monument constructed entirely in white marble and first to feature extensive Pietra Dura inlay.</li>
                  </ul>
                </li>
              </ul>
            </li>
            <li><strong>The Nawabs of Awadh &amp; Lucknow Court Culture:</strong>
              <ul>
                <li><em>Dynastic Evolution:</em> Founded by <strong>Saadat Khan Burhan-ul-Mulk (1722)</strong>; Safdar Jung (tomb in Delhi); Shuja-ud-Daula (defeated at Buxar 1764; signed Treaty of Allahabad; signed Treaty of Banaras 1773 with Hastings).</li>
                <li><em>Nawab Asaf-ud-Daula (1775–1797):</em> Transferred capital from Faizabad to <strong>Lucknow (1775)</strong>; commissioned the colossal <strong>Bara Imambara (Asafi Imambara, 1784)</strong> as a massive famine relief employment project; contains the Central Hall (50 meters long, 16 meters high) built completely without external iron beams, wooden pillars, or central supports; crowned by the intricate acoustic labyrinth of the <strong>Bhulbhulaiya</strong>; built the grand <strong>Rumi Darwaza</strong> (Turkish Gate, 60 feet high) modeled on the Sublime Porte in Constantinople.</li>
                <li><em>Nawab Saadat Ali Khan II:</em> Built Dilkusha Kothi and Chattar Manzil; signed Subsidiary Alliance (1801) ceding half of Awadh territory to the British.</li>
                <li><em>Nawab Wajid Ali Shah (1847–1856):</em> Last sovereign King of Awadh; passionate patron of the arts: revived and refined <strong>Kathak dance</strong> at the Lucknow court; patronized thumri singing (composed legendary thumri: <em>"Babul mora naihar chhooto hi jaaye"</em> under the pen name <em>Akhtarpiya</em>); deposed by Lord Dalhousie on 7 February 1856 on trumped-up charges of "maladministration" and exiled to Metiabruz near Calcutta; spark that directly triggered the 1857 uprising in Awadh.</li>
              </ul>
            </li>
          </ul>
          <div class="syl-action-bar">
            <a href="period.html?id=up-jaunpur-sultanate" class="btn btn-outline btn-sm">Explore UP Medieval Period →</a>
            <a href="practice.html?category=up-history" class="btn btn-primary btn-sm">Practice Jaunpur &amp; Awadh MCQs</a>
          </div>
        </div>

        <!-- Unit 3 -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">3. Modern Freedom Struggle, Peasant Agitations, and Revolutionary Hubs in UP</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">1857 Epicenters, Aligarh/Deoband/BHU Renaissance, Oudh Kisan Sabha &amp; Eka Movement, Kakori Action &amp; Chittu Pandey Ballia</p>
            </div>
            <span class="t-cat cat-up">Unit A.3 • UP Freedom Struggle</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/images/up_freedom_struggle.png" alt="Modern Freedom Struggle and Revolutionary Movements in UP" onerror="this.onerror=null; this.src='assets/images/history.png';">
          </div>
          <ul>
            <li><strong>Uttar Pradesh Epicenters of the 1857 Great Revolt:</strong>
              <ul>
                <li><em>Meerut (10 May 1857):</em> Birthplace of the revolt; sepoys of the 3rd Native Cavalry refused greased cartridges, broke open the military prison, executed British officers, and marched overnight to Delhi.</li>
                <li><em>Lucknow:</em> <strong>Begum Hazrat Mahal</strong> crowned her 11-year-old son Birjis Qadr as Nawab; organized united resistance of Hindu and Muslim taluqdars, sepoys, and peasants; besieged the British Residency for months; defeated British under Sir Henry Lawrence at Battle of Chinhat; escaped to Nepal after Lucknow fell to Colin Campbell.</li>
                <li><em>Kanpur:</em> <strong>Nana Sahib</strong> (Dhondo Pant), military commander <strong>Tatya Tope</strong> (Ramchandra Pandurang), and diplomat Azimullah Khan; declared Nana Sahib as Peshwa; liberated Kanpur; defeated General Wheeler; retaken by Campbell.</li>
                <li><em>Jhansi:</em> <strong>Rani Lakshmibai</strong> fought British forces under Sir Hugh Rose; escaped from Jhansi fort with infant son tied to her back; captured Gwalior; martyred at Kotah-ki-Serai (18 June 1858).</li>
                <li><em>Other UP Centers:</em> <strong>Khan Bahadur Khan</strong> (Bareilly/Rohilkhand); <strong>Maulvi Ahmadullah Shah</strong> (Faizabad - fiercely resisted Campbell); <strong>Maulvi Liaquat Ali</strong> (Allahabad/Chaukhandi); <strong>Shah Mal</strong> (Baraut, Baghpat - organized 84 villages of the Jat community / Chaurasi Desh against British supplies; martyred in combat).</li>
              </ul>
            </li>
            <li><strong>Socio-Religious &amp; Educational Renaissance Hubs:</strong>
              <ul>
                <li><em>Aligarh:</em> <strong>Sir Syed Ahmed Khan</strong> founded the Scientific Society (1864) and Mohammedan Anglo-Oriental College (MAO College, 1875), fostering scientific modernism among Indian Muslims (became Aligarh Muslim University in 1920).</li>
                <li><em>Deoband (Saharanpur):</em> <strong>Darul Uloom Deoband</strong> founded in 1866 by Muhammad Qasim Nanautavi and Rashid Ahmad Gangohi; spearheaded the anti-colonial Islamic revivalist movement, consistently supporting the Congress and opposing the two-nation theory.</li>
                <li><em>Varanasi (BHU):</em> <strong>Banaras Hindu University</strong> founded in 1916 by Pandit <strong>Madan Mohan Malaviya</strong>, Dr. Annie Besant, and Maharaja Rameshwar Singh of Darbhanga under the BHU Act 1915 as a premier center of nationalist education.</li>
              </ul>
            </li>
            <li><strong>Peasant Agitations &amp; Kisan Sabhas in Uttar Pradesh:</strong>
              <ul>
                <li><em>UP Kisan Sabha (February 1918):</em> Formed at Allahabad by <strong>Gauri Shankar Mishra</strong>, <strong>Indra Narayan Dwivedi</strong>, with the support of Pandit Madan Mohan Malaviya; grew rapidly to 450 branches across 173 tehsils.</li>
                <li><em>Oudh Kisan Sabha (October 1920):</em> Established at Pratapgarh by <strong>Baba Ramchandra</strong> (charismatic Maharashtrian sanyasi who recited Tulsidas's <em>Ramcharitmanas</em> to mobilize illiterate peasants) alongside Jawaharlal Nehru; organized massive non-violent peasant resistance against extortionate Bedakhli (eviction), Nazrana (illegal cash gifts), and forced labor across Pratapgarh, Rae Bareli, Sultanpur, and Faizabad.</li>
                <li><em>The Eka Movement / Unity Movement (1921–1922):</em> Fierce peasant uprising across northern Awadh districts (Hardoi, Bahraich, Sitapur, Kheri) led by low-caste leader <strong>Madari Pasi</strong>; peasants took religious oaths with holy water promising to pay only recorded rents, refuse forced labor (Begar), and boycott eviction decrees; targeted oppressive taluqdars and British officials.</li>
                <li><em>All India Kisan Sabha (AIKS, 11 April 1936):</em> Formed at its inaugural session at <strong>Lucknow</strong>; iconic peasant champion <strong>Swami Sahajanand Saraswati</strong> elected first President and <strong>N.G. Ranga</strong> elected General Secretary; Jawaharlal Nehru addressed the conference; drafted the historic Kisan Manifesto demanding abolition of zamindari and cancellation of rural debts.</li>
              </ul>
            </li>
            <li><strong>Revolutionary Hotspots &amp; Martyrdoms in UP:</strong>
              <ul>
                <li><em>Hindustan Republican Association (HRA):</em> Founded at <strong>Kanpur in October 1924</strong> by Sachindra Nath Sanyal, Ram Prasad Bismil, and Jogesh Chandra Chatterjee; published manifesto <em>The Revolutionary</em>.</li>
                <li><em>The Kakori Train Action (9 August 1925):</em> Daring ambush of the 8-Down passenger train at Kakori railway station near Lucknow by 10 HRA revolutionaries led by Ram Prasad Bismil, Ashfaqullah Khan, Chandrashekhar Azad, Rajendra Lahiri, and Roshan Singh, capturing government cash to fund arms procurement; historic trial (defended by Govind Ballabh Pant and Mohanlal Saxena); 4 martyrs were hanged: Ram Prasad Bismil (Gorakhpur), Ashfaqullah Khan (Faizabad), Roshan Singh (Naini, Prayagraj), and Rajendra Lahiri (Gonda).</li>
                <li><em>Chandrashekhar Azad's Martyrdom:</em> Commander-in-Chief of HSRA; pledged never to be captured alive by British forces (<em>"Azad hi rahe hain, Azad hi rahenge"</em>); surrounded by British police at <strong>Alfred Park (now Chandrashekhar Azad Park), Allahabad, on 27 February 1931</strong>; fought single-handedly with his Colt pistol until only one bullet remained, shooting himself through the temple to fulfill his sacred vow.</li>
              </ul>
            </li>
            <li><strong>Gandhian Movements &amp; Quit India in UP:</strong>
              <ul>
                <li><em>Chauri Chaura Incident (4 February 1922, Gorakhpur):</em> Protesting peasants fired upon by British police; infuriated crowd locked 22 policemen inside the local police post and set it ablaze; deeply pained by this deviation from non-violence, Mahatma Gandhi unilaterally suspended the nationwide Non-Cooperation Movement at Bardoli on 12 February 1922.</li>
                <li><em>Quit India Movement &amp; The Ballia Parallel Government (August 1942):</em> Revolutionary mass uprising in Ballia led by Congress leader <strong>Chittu Pandey ('Sher-e-Ballia' / Tiger of Ballia)</strong>; overwhelmed local British authorities, broke open the district jail liberating all political prisoners, took control of the treasury, and proclaimed an <strong>Independent Parallel Government (National Government / Swatantra Sarkar)</strong> in Ballia on 19 August 1942; governed the district for nearly a week before massive British military reinforcements reoccupied it.</li>
              </ul>
            </li>
          </ul>
          <div class="syl-action-bar">
            <a href="period.html?id=up-freedom-struggle" class="btn btn-outline btn-sm">Explore UP Freedom Struggle Period →</a>
            <a href="practice.html?category=up-history" class="btn btn-primary btn-sm">Practice UP 1857, Kisan &amp; Kakori MCQs</a>
          </div>
        </div>

        <!-- Unit 4 -->
        <div class="syl-card">
          <div class="syl-card-head">
            <div>
              <h3 class="syl-card-title">4. Art, Architecture, Gharanas, Festivals, and Intangible Heritage of UP</h3>
              <p style="margin:4px 0 0; color:var(--ink-soft);">Kathak Lucknow Gharana, Varanasi/Kirana Music Gharanas, Folk Dances, Kumbh Mela &amp; 12+ Geographical Indication (GI) Crafts</p>
            </div>
            <span class="t-cat cat-up">Unit A.4 • UP Art &amp; Heritage</span>
          </div>
          <div class="syl-img-banner">
            <img src="assets/culture/fairs-festivals-calendars.jpg" alt="Fairs, Festivals, Gharanas and Intangible Heritage of UP" onerror="this.onerror=null; this.src='assets/images/history.png';">
          </div>
          <ul>
            <li><strong>Kathak Dance &amp; The Lucknow Gharana:</strong>
              <ul>
                <li><em>Sole Classical Dance of North India:</em> Evolved from ancient temple storytellers (<em>Kathakars</em>: "Katha kahe so Kathak kahave") who narrated epics using hand gestures, facial expressions, and rhythmic footwork; synthesized with Persian courtly elegance during the Mughal and Awadh eras.</li>
                <li><em>The Lucknow Gharana of Kathak:</em> Established by <strong>Ishwari Prasad</strong>; reached golden zenith under the patronage of Nawab <strong>Wajid Ali Shah</strong>; characterized by graceful, delicate body movements (Anga), subtle emotional expression (Bhava), dramatic storytelling (Gat-Nikas), lyrical Thaat, and intricate footwork (Tatkar) synchronized with rapid pirouettes (Chakkars).</li>
                <li><em>Legendary Exponents:</em> Pandit Kalka Prasad and Bindadin Maharaj; Pandit Shambhu Maharaj (Abhinaya king); Pandit Lachhu Maharaj; and the world-renowned <strong>Pandit Birju Maharaj</strong> (Padma Vibhushan, who carried the tradition globally).</li>
              </ul>
            </li>
            <li><strong>Major Classical Music Gharanas of Uttar Pradesh:</strong>
              <ul>
                <li><em>Varanasi / Banaras Gharana:</em> Revered for its versatility across Khayal, Thumri, Dadra, Chaiti, Kajari, and Tabla. Eminent luminaries: <strong>Ustad Bismillah Khan</strong> (Bharat Ratna, who brought the folk Shehnai to the global classical concert stage); <strong>Girija Devi</strong> ('Queen of Thumri'); Pandit Kishan Maharaj and Pandit Samta Prasad ('Gudai Maharaj') on Tabla; Rajan and Sajan Mishra (vocal).</li>
                <li><em>Kirana Gharana (Muzaffarnagar):</em> Founded by <strong>Ustad Abdul Karim Khan</strong> and Ustad Abdul Wahid Khan; named after village of Kairana; famous for slow, introspective, emotionally profound note-by-note exposition (Alap) and strict adherence to melodic pitch purity (Swara); luminaries include Pandit Bhimsen Joshi (Bharat Ratna) and Gangubai Hangal.</li>
                <li><em>Agra Gharana (Rangeela Gharana):</em> Traces ancestry to Haji Sujan Khan (court of Akbar); revitalized by <strong>Ustad Faiyaz Khan</strong> (conferred title 'Aftab-e-Mousiqi' - Sun of Music); characterized by robust, resonant, full-throated voice production, Dhrupad-like Nom-Tom alap, and dramatic rhythmic play with the tabla.</li>
                <li><em>Rampur-Sahaswan Gharana:</em> Founded by Ustad Inayat Hussain Khan; closely associated with Gwalior tradition; characterized by intricate, rapid, crystalline Taan patterns (prominent exponent: Ustad Rashid Khan).</li>
              </ul>
            </li>
            <li><strong>Folk Music, Theatre &amp; Dances of Uttar Pradesh:</strong>
              <ul>
                <li><em>Folk Songs:</em>
                  <ul>
                    <li><strong>Kajari:</strong> Soulful monsoon folk song of eastern UP (Mirzapur, Varanasi), sung by women expressing the longing of separation from their beloved amidst falling monsoon rains.</li>
                    <li><strong>Chaiti:</strong> Romantic folk songs sung during the Hindu month of Chaitra (spring/harvest season), concluding with the characteristic refrain "Ho Rama".</li>
                    <li><strong>Rasia / Hori:</strong> Vibrant, playful folk songs of the Braj region (Mathura, Vrindavan) celebrating the divine love and Holi celebrations of Radha and Lord Krishna.</li>
                    <li><strong>Birha:</strong> Narrative heroic folk ballad of the Ahir/Yadav community in Bhojpuri eastern UP, recounting folk tales and contemporary social struggles.</li>
                    <li><strong>Alha:</strong> Legendary martial epic ballad of Bundelkhand composed by court poet Jagnik (Alha-Khand), celebrating the 52 heroic battles fought by warrior brothers Alha and Udal against Prithviraj Chauhan.</li>
                  </ul>
                </li>
                <li><em>Folk Theatre:</em> <strong>Nautanki</strong> (musical operatic folk theatre with energetic Nagada drums and couplets / Dohas; two major styles: <em>Hathras School</em> with high-pitched classical singing, and <em>Kanpur School</em> with theatrical social dialogues) and <strong>Ramlila / Raslila</strong>.</li>
                <li><em>Folk Dances:</em> <strong>Charkula Dance</strong> (spectacular folk dance of the Braj region where female dancers balance a 4-to-5 tier wooden pyramidal wheel holding 108 illuminated mustard-oil lamps on their heads while dancing to Rasia songs); <strong>Karma Dance</strong> (tribal dance of Mirzapur and Sonbhadra performed by Kharwar, Gond, and Baiga tribes around the sacred Karma tree); Pai Danda (Bundelkhand martial stick dance); Dhobiya (eastern UP washerman community dance).</li>
              </ul>
            </li>
            <li><strong>Major Fairs &amp; Cultural Festivals:</strong>
              <ul>
                <li><em>Kumbh Mela &amp; Mahakumbh (Prayagraj):</em> Held at the holy <strong>Triveni Sangam</strong> (confluence of Ganga, Yamuna, and mythical Saraswati); rotationally held every 12 years (Mahakumbh every 144 years, Ardh Kumbh every 6 years); inscribed on UNESCO Representative List of Intangible Cultural Heritage; largest spiritual gathering on planet Earth.</li>
                <li><em>Lathmar Holi (Barsana &amp; Nandgaon):</em> Unique traditional celebration where women of Barsana (Radha's village) playfully beat the men of Nandgaon (Krishna's village) with wooden batons (Lathis) as men defend themselves with shields.</li>
                <li><em>Dev Deepawali (Varanasi):</em> Celebrated on Kartik Purnima (15 days after Diwali); millions of earthen oil lamps (Diyas) light up all 84 historic stone ghats of Varanasi along the Ganga in tribute to the victory of Lord Shiva over the demon Tripurasura.</li>
                <li><em>Other Fairs:</em> Bateshwar Fair (Agra - ancient animal and camel fair on Yamuna), Magh Mela (Prayagraj annual winter fair), Shakumbhari Devi Fair (Saharanpur), Dadhikando Fair (Prayagraj), Taj Mahotsav (Agra - 10-day cultural craft festival).</li>
              </ul>
            </li>
            <li><strong>Traditional Crafts &amp; Geographical Indications (GI Tags) of Uttar Pradesh:</strong>
              <p>Uttar Pradesh is among India's leading states in registered Geographical Indications (GI), fostering traditional artisanal livelihoods:</p>
              <div class="up-table-wrap">
                <table class="up-table">
                  <thead>
                    <tr>
                      <th>Product / Craft</th>
                      <th>Registered Region</th>
                      <th>Salient Craftsmanship &amp; Technical Attributes</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr><td><strong>Lucknow Chikan Craft</strong></td><td>Lucknow</td><td>Delicate, artistic hand embroidery performed on fine muslin/cotton using 32 distinct traditional stitches (e.g., Bakhiya, Phanda, Murri, Tepchi, Jali).</td></tr>
                    <tr><td><strong>Lucknow Zardozi</strong></td><td>Lucknow</td><td>Heavy, opulent gold and silver metallic wire thread embroidery embellished with pearls, sequins, and precious stones on silk and velvet.</td></tr>
                    <tr><td><strong>Banaras Brocade Silk</strong></td><td>Varanasi</td><td>Luxurious pure mulberry silk handloom sarees woven with real gold and silver Zari threads featuring intricate Mughal floral motifs (Kalka, Bel).</td></tr>
                    <tr><td><strong>Varanasi Pink Meenakari</strong></td><td>Varanasi</td><td>Rare, exquisite enamel art (Gulabi Meenakari) on silver and gold metal surfaces practiced exclusively in the narrow alleys of Varanasi.</td></tr>
                    <tr><td><strong>Mirzapur / Bhadohi Carpets</strong></td><td>Bhadohi, Mirzapur</td><td>World-famous hand-knotted woolen and silk carpets; Bhadohi is recognized as the "Carpet City of South Asia", exporting over 60% of India's carpets.</td></tr>
                    <tr><td><strong>Moradabad Metalware</strong></td><td>Moradabad</td><td>Renowned as <strong>"Peetal Nagari" (Brass City)</strong>; master craftsmanship in engraved, etched, and cast brass and copper utensils, lamps, and statues.</td></tr>
                    <tr><td><strong>Firozabad Glassware</strong></td><td>Firozabad</td><td>Known as <strong>"Suhag Nagari"</strong>; century-old hub producing vibrant glass bangles, chandeliers, laboratory glassware, and decorative blown glass.</td></tr>
                    <tr><td><strong>Kannauj Perfume (Attar)</strong></td><td>Kannauj</td><td>Known as the <strong>"Perfume City of India" (Grasso of the East)</strong>; traditional hydro-distillation (Deg-Bhapka) using copper stills over wood fires to produce natural floral attars (Gulab, Bela, Khas) and unique Mitti Attar (capturing the aroma of baked earth).</td></tr>
                    <tr><td><strong>Saharanpur Wood Carving</strong></td><td>Saharanpur</td><td>Intricate hand carving on Sheesham and mango wood producing fretwork screens (Jalis), carved furniture, jewel boxes, and architectural panels.</td></tr>
                    <tr><td><strong>Gorakhpur Terracotta</strong></td><td>Gorakhpur</td><td>Traditional handmade red clay figurines, hollow equestrian statues (horses and elephants), and bells crafted by hereditary Potters without artificial molds.</td></tr>
                    <tr><td><strong>Khurja Pottery</strong></td><td>Bulandshahr</td><td>Known as the <strong>"Ceramic City"</strong>; traditional glazed ceramic pottery, hand-painted floral tiles, and stoneware household items.</td></tr>
                    <tr><td><strong>Nizamabad Black Pottery</strong></td><td>Azamgarh</td><td>Unique earthenware pottery baked with mustard-cake smoke in closed kilns giving it a glossy jet-black color, engraved and inlaid with shimmering silver zinc-lead amalgam.</td></tr>
                  </tbody>
                </table>
              </div>
            </li>
          </ul>
          <div class="syl-action-bar">
            <a href="up-history.html" class="btn btn-outline btn-sm">Explore UP Special Hub →</a>
            <a href="practice.html?category=up-history" class="btn btn-primary btn-sm">Practice UP Art, Gharanas &amp; GI Tags MCQs</a>
          </div>
        </div>
      </div>
'''
