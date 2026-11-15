import re

with open('art-culture.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '''              <td>Official script for Santhali under the Eighth Schedule of the Constitution.</td>
            </tr>
          </tbody>
        </table>
      </div>'''

if target not in html:
    print("ERROR: Target anchor not found in art-culture.html")
    exit(1)

NEW_COMPARISONS = '''
      <!-- Comparison 11: 8 Classical Dance Traditions of India -->
      <h3 style="margin-top:36px;">11. Classical Dance Traditions of India (8 Sangeet Natak Akademi Styles Master Matrix)</h3>
      <div class="comparison-table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th style="width:15%;">Classical Dance &amp; State</th>
              <th style="width:18%;">Textual &amp; Sacred Origins</th>
              <th style="width:23%;">Distinctive Costume, Adornments &amp; Makeup</th>
              <th style="width:24%;">Signature Stances, Mudras &amp; Repertoire Sequence</th>
              <th style="width:20%;">Pivotal Maestros &amp; Institutional Revivers</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Bharatanatyam</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Tamil Nadu</span></td>
              <td>Bharata Muni's <em>Natya Shastra</em> &amp; Nandikeshvara's <em>Abhinaya Darpana</em>; evolved from ancient temple <em>Sadir Attam</em> danced by Devadasis.</td>
              <td>Kanchipuram silk sarees with front pleated accordion fan that spreads in <em>Araimandi</em>; temple gold jewelry (Talai Samanam, Suryan-Chandran, Odiyanam); red alta on fingers and feet.</td>
              <td>Tandava &amp; Lasya balance; <em>Adavus</em> rhythmic units; sequence: <strong>Alarippu</strong> (invocation) &rarr; <strong>Jatiswaram</strong> &rarr; <strong>Shabdam</strong> &rarr; <strong>Varnam</strong> (climax of Nritta &amp; Nritya) &rarr; <strong>Padam</strong> &rarr; <strong>Tillana</strong> &rarr; <strong>Mangalam</strong>.</td>
              <td>Rukmini Devi Arundale (founded Kalakshetra 1936), T. Balasaraswati, Yamini Krishnamurthy, Padma Subrahmanyam.</td>
            </tr>
            <tr>
              <td><strong>Kathakali</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Kerala</span></td>
              <td>Roots in <em>Ramanattam</em> &amp; <em>Krishnanattam</em> temple dramas; highly stylized all-night dance-drama depicting victory of Dharma over Adharma.</td>
              <td>Elaborate facial makeup (<em>Vesham</em>) with white rice-paste ruffle (<em>Chutti</em>) and towering headdresses (<em>Kireedam</em>):<br>
                &bull; <strong>Pacha (Green)</strong>: Divine, noble heroes (Rama, Arjuna, Krishna).<br>
                &bull; <strong>Kathi (Knife/Green+Red)</strong>: Arrogant villains of noble origin (Ravana, Duryodhana).<br>
                &bull; <strong>Kari (Black)</strong>: Demonic she-devils (Surpanakha).<br>
                &bull; <strong>Thaadi (Beards)</strong>: White (divine Hanuman), Red (monstrous Dushasana), Black (hunters).<br>
                &bull; <strong>Minukku (Peach/Yellow)</strong>: Sages, Brahmins, and virtuous women (Sita, Damayanti).</td>
              <td>24 root hand mudras (<em>Hathalakshana Deepika</em>); dramatic eye and eyebrow control portraying <em>Navarasas</em>; heavy percussive acoustic backing (Chenda, Maddalam, Chengila gong).</td>
              <td>Poet Vallathol Narayana Menon (founded Kerala Kalamandalam 1930), Kalamandalam Gopi, Guru Kunchu Kurup.</td>
            </tr>
            <tr>
              <td><strong>Kathak</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Uttar Pradesh &amp; Northern India</span></td>
              <td>Derived from <em>Katha</em> (story) and <em>Katthaka</em> (wandering temple storytellers who enacted Epics); transformed in Mughal and Awadh royal courts.</td>
              <td>Anarkali churidar or lehenga-choli with transparent odhani; male dancers wear embroidered achkan/sherwani and cap; dense brass <em>Ghungroos</em> (100–150 per ankle).</td>
              <td>Intricate mathematical footwork (<strong>Tatkar</strong>); lightning-speed pirouettes (<strong>Chakkars</strong>); vocal recitation of rhythmic mnemonics (<strong>Padhant</strong>); <em>Amad</em>, <em>Thaat</em>, <em>Tukra</em>, <em>Tora</em>, <em>Paran</em>; subtle mime (<em>Bhav</em>).</td>
              <td>Pandit Birju Maharaj, Shambhu Maharaj, Sitara Devi, Lachhu Maharaj; 3 major Gharanas: Lucknow (Nazakat/grace), Jaipur (speed/footwork), Banaras (Thumri bhava).</td>
            </tr>
            <tr>
              <td><strong>Kuchipudi</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Andhra Pradesh</span></td>
              <td>Founded in Kuchelapuram village by 17th c. saint <strong>Siddhendra Yogi</strong>; originally performed by male Brahmin actor-dancers (<em>Bhagavatulu</em>).</td>
              <td>Pleated silk saree featuring the unique <strong>Katcham</strong> (long central fold or pleated cloth tucked at the back); traditional South Indian gold temple ornaments and floral braid.</td>
              <td>Blends spoken dialogue with dance; landmark pieces:<br>
                &bull; <strong>Tarangam</strong>: Dancing rhythmically on the elevated edge of a brass plate while balancing a water pot (<em>Kundi</em>) on the head.<br>
                &bull; <strong>Manduka Shabdam</strong>: Enactment of the frog maiden rescued by Gajendra/Vishnu.<br>
                &bull; <strong>Bhama Kalapam</strong>: Depicting queen Satyabhama's pride and pining for Krishna.</td>
              <td>Vempati Chinna Satyam (modernized solo repertoire), Raja &amp; Radha Reddy, Yamini Krishnamurthy, Swapnasundari.</td>
            </tr>
            <tr>
              <td><strong>Mohiniyattam</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Kerala</span></td>
              <td>Named after <em>Mohini</em> (celestial enchantress avatar of Vishnu); solo feminine classical dance dedicated to the ultimate aesthetic of <strong>Lasya</strong> (lyrical feminine grace).</td>
              <td>Iconic pristine off-white/cream handloom saree (<strong>Kasavu</strong>) with rich gold-embroidered zari borders; hair gathered in a graceful asymmetrical side bun (<strong>Kuduma</strong>) wrapped in white jasmine.</td>
              <td>Gentle, fluid torso sway evoking the swaying of coconut palms and ocean waves; circular movements without harsh foot-stamping; music set in Kerala's <strong>Sopana Sangeetam</strong> style with verses from Jayadeva's <em>Gita Govinda</em>.</td>
              <td>Kalamandalam Kalyanikutty Amma ('Mother of Mohiniyattam'), Bharati Shivaji, Kanak Rele, Sunanda Nair.</td>
            </tr>
            <tr>
              <td><strong>Odissi</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Odisha</span></td>
              <td>Traced to Udayagiri-Khandagiri cave reliefs (Ranigumpha, 2nd c. BCE); preserved by temple <strong>Maharis</strong> (female dancers) and young male <strong>Gotipuas</strong>.</td>
              <td>Sambalpuri or Bomkai silk sarees; Cuttack silver filigree jewelry (<em>Tarakasi</em>); elaborate floral headgear crown (<em>Tahia</em>) representing temple spires and spiritual enlightenment.</td>
              <td>Dual structural foundation:<br>
                &bull; <strong>Chowk</strong>: Square, masculine stance mimicking Lord Jagannath.<br>
                &bull; <strong>Tribhanga</strong>: Three-bend feminine posture (neck, waist, knee) mirroring temple sculptures.<br>
                Sequence: Mangalacharan &rarr; Batu Nritya &rarr; Pallavi &rarr; Abhinaya &rarr; Moksha.</td>
              <td>Guru Kelucharan Mohapatra, Sanjukta Panigrahi, Sonal Mansingh, Madhavi Mudgal, Kumkum Mohanty.</td>
            </tr>
            <tr>
              <td><strong>Manipuri</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Manipur</span></td>
              <td>Ancient animistic <em>Lai Haraoba</em> festival merged with Gaudiya Vaishnavism under King <strong>Bhagyachandra</strong> (18th c.); revolves around the devotional <strong>Raas Leela</strong> of Radha-Krishna.</td>
              <td>Female dancers (Gopis) wear the iconic stiff, cylindrical barrel skirt called <strong>Kumil</strong> (or <em>Kumin</em>) adorned with mirrors and sequins; translucent overskirt (<em>Pasuan</em>) and fine white face veil (<em>Kokyet</em>). Male Krishna wears yellow dhoti and peacock crown.</td>
              <td>Ethereal, gliding footwork without harsh floor strikes; gentle circular curves (<em>Nagabandha</em> posture); <strong>Pung Cholom</strong> (acrobatic drum dance) and <strong>Kartal Cholom</strong> (cymbal dance) performed by male dancers.</td>
              <td>Guru Bipin Singh, Jhaveri Sisters (Darshana, Nayana, Suverna, Ranjana), Charu Mathur.</td>
            </tr>
            <tr>
              <td><strong>Sattriya</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Assam</span></td>
              <td>Created in 15th c. by saint-reformer <strong>Srimanta Sankardev</strong> as part of the Neo-Vaishnavite Bhakti reform in monastic institutions called <strong>Sattras</strong>; recognized by SNA in 2000.</td>
              <td>Woven indigenous Assam silk—cream <em>Pat silk</em> or golden <em>Muga silk</em>; traditional Assamese ornaments including <em>Kopali</em> forehead piece, <em>Lokaparo</em> bird earrings, and <em>Galgam Kharu</em> bangles.</td>
              <td>Staged in monastery prayer halls (<strong>Namghar</strong>); incorporates <strong>Ankia Naat</strong> one-act plays; accompanied by devotional <strong>Borgeet</strong> hymns, terracotta drum (<strong>Khol</strong>), and large bronze cymbals (<strong>Taal</strong>); masculine <em>Paurashik Bhangi</em> and feminine <em>Stri Bhangi</em>.</td>
              <td>Jatin Goswami, Ghanakanta Bora, Bhabananda Barbayan, Tankeswar Hazarika Borbayan.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Comparison 12: Indian Puppetry Traditions -->
      <h3 style="margin-top:36px;">12. Indian Puppetry Traditions (All 4 Forms &amp; State Heritage Master Matrix)</h3>
      <div class="comparison-table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th style="width:16%;">Puppetry Category</th>
              <th style="width:20%;">Regional Form &amp; State</th>
              <th style="width:28%;">Physical Construction, Material &amp; Manipulation Mechanics</th>
              <th style="width:36%;">Distinctive Artistry, Performance Customs &amp; Story Themes</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td rowspan="4"><strong>1. String Puppets<br>(Dhaaga Putli)</strong></td>
              <td><strong>Kathputli</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Rajasthan (Bhatt Community)</span></td>
              <td>Carved from single blocks of light mango wood; dressed in colorful flowing Rajasthani ghagra-choli; characteristic <strong>complete absence of legs</strong>; operated by 2 to 4 strings looped over puppeteer's fingers.</td>
              <td>Puppeteer speaks through a unique bamboo reed whistle squeaker (<strong>Boli / Ghoghi</strong>) producing high-pitched voice, interpreted by the dholak-playing female singer; depicts ballads of hero <strong>Amar Singh Rathore</strong> of Nagaur.</td>
            </tr>
            <tr>
              <td><strong>Kundhei</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Odisha</span></td>
              <td>Light ganso wood; light-weight with multiple articulated joints; dressed in regional pleated skirts; manipulated with strings tied to a triangular wooden control frame (<strong>Khilari</strong>).</td>
              <td>Strong influence of Odissi classical dance; puppet gestures follow Odissi postures; themes draw from Radha-Krishna pastimes and Ramayana episodes.</td>
            </tr>
            <tr>
              <td><strong>Gombeyatta</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Karnataka</span></td>
              <td>Intricately sculpted wood; styled, painted, and costumed exactly like <strong>Yakshagana</strong> classical theatre actors with towering ornate headgear (Pagade) and painted facial expressions.</td>
              <td>Operated by multi-string wooden cross-bars; accompanied by Yakshagana instruments (Chande drum, Maddale, and Bhagavata vocalist); enacted during harvest festivals.</td>
            </tr>
            <tr>
              <td><strong>Bommalattam</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Tamil Nadu</span></td>
              <td><strong>Largest and heaviest puppets in India</strong> (up to 4.5 feet height and 10 kg weight); combines both strings and rods: puppeteer wears an iron ring around the forehead with strings attached, and holds thin rods to move puppet hands.</td>
              <td>Begins with elaborate invocation to Lord Ganesha; accompanied by Carnatic musicians; famous comedic character <em>Komi</em> and her buffoon husband <em>Kalyanarayan</em> punctuate heroic puranic scenes.</td>
            </tr>
            <tr>
              <td rowspan="4"><strong>2. Shadow Puppets<br>(Chhaya Putli)</strong></td>
              <td><strong>Togalu Gombeyaata</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Karnataka</span></td>
              <td>Cut from treated, cured goat or deer skin made translucent; painted with bright vegetable pigments; two distinct sizes: <em>Chikka</em> (small folk puppets) and <em>Dodda</em> (massive life-sized royal figures).</td>
              <td>Cast brilliant multi-colored silhouette shadows onto backlit white cotton cloth screens; manipulated with bamboo central rods and arm sticks; enacts local retellings of the epics.</td>
            </tr>
            <tr>
              <td><strong>Tholu Bommalata</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Andhra Pradesh</span></td>
              <td>Translucent leather cutouts articulated at neck, shoulders, elbows, and knees; painted on both sides with vivid luminous colors; puppets stand 3 to 6 feet tall.</td>
              <td>Puppeteers stamp ankle bells against heavy wooden planks laid on the stage floor to simulate lightning, galloping horses, and epic combat sounds; accompanied by classical Telugu verses.</td>
            </tr>
            <tr>
              <td><strong>Ravana Chhaya</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Odisha</span></td>
              <td>Made from untanned, opaque deer skin; <strong>puppets have no jointed limbs</strong>; creates stark, opaque monochromatic black-and-white silhouettes on screen.</td>
              <td>Named 'Ravana's Shadow' because local belief holds that the divine Rama casts no mortal shadow; lyrical poetry of Odia poet Balaram Das's <em>Bichitra Ramayana</em>; accompanied by Khanjani tambourine.</td>
            </tr>
            <tr>
              <td><strong>Tolpavakoothu</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Kerala</span></td>
              <td>Opaque buffalo skin puppets with perforated geometric patterns; staged exclusively inside permanent temple shadow theatres (<strong>Koothumadams</strong>) in front of <strong>Bhadrakali</strong> temples.</td>
              <td>All-night rituals staged over 7 to 21 consecutive nights; illuminated by 42 oil lamps burning in coconut halves along the screen; puppeteers (Pulavars) chant verses from Kamba Ramayanam.</td>
            </tr>
            <tr>
              <td rowspan="2"><strong>3. Glove Puppets<br>(Hasta Putli)</strong></td>
              <td><strong>Pavakoothu</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Kerala</span></td>
              <td>Emerged in the 18th century; carved wooden heads and arms attached to a colorful cloth bag; facial makeup, crowns, and costumes mimic <strong>Kathakali</strong> actors with utmost fidelity.</td>
              <td>Puppeteer inserts forefinger into the head and thumb and middle finger into the puppet's two arms; accompanied by Chenda, Maddalam, and Elathalam; themes focus on Mahabharata duels.</td>
            </tr>
            <tr>
              <td><strong>Beni Putul</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">West Bengal</span></td>
              <td>Terracotta or papier-mâché heads with cloth robes; manipulated by three fingers of the street puppeteer.</td>
              <td>Lively satirical village street theatre; historically used by folk performers to mock colonial tax collectors, moneylenders, and social hypocrisies.</td>
            </tr>
            <tr>
              <td rowspan="2"><strong>4. Rod Puppets<br>(Danda Putli)</strong></td>
              <td><strong>Putul Nach</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">West Bengal, Odisha &amp; Assam</span></td>
              <td>Large, heavy wooden puppets sculpted from lightweight wood; jointed at shoulders and neck; supported and operated by wooden rods extending from below through the body.</td>
              <td>Puppeteers stand behind a head-high backdrop screen holding the main rod fastened to a waist belt, pulling control cords to move limbs; dramatic dialogue inspired by regional Jatra folk theatre.</td>
            </tr>
            <tr>
              <td><strong>Yampuri</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Bihar</span></td>
              <td>Sculpted from single pieces of wood with no joints; mounted directly on top of manipulation rods.</td>
              <td>Traditional morality play depicting the court of <strong>Yamaraja</strong> (Lord of Death) and <strong>Chitragupta</strong> recording human virtues and sins; delivers didactic moral lessons on karma and reincarnation.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Comparison 13: Rock-Cut Cave Architecture of India -->
      <h3 style="margin-top:36px;">13. Rock-Cut Cave Architecture of India (Mauryan Foundations to Monolithic Climax)</h3>
      <div class="comparison-table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th style="width:16%;">Cave Complex &amp; Location</th>
              <th style="width:18%;">Historical Era &amp; Royal Patrons</th>
              <th style="width:30%;">Architectural Layout, Engineering &amp; Rock Typology</th>
              <th style="width:36%;">Celebrated Murals, Sculptures &amp; Epigraphic Significance</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Barabar &amp; Nagarjuni Caves</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Jehanabad, Bihar</span></td>
              <td><strong>Mauryan Empire</strong> (3rd c. BCE); commissioned by Emperor <strong>Ashoka</strong> and grandson <strong>Dasharatha</strong>.</td>
              <td>Earliest rock-cut architecture in India; excavated into solid granite plutons; imitation of wooden huts; circular domed chamber (*Chaityagriha*) with vaulted barrel anteroom; <strong>Lomas Rishi Cave</strong> features the iconic ogee arched doorway with carved elephant frieze paying homage to stupas.</td>
              <td>Legendary mirror-like glassy <strong>Mauryan Polish</strong>; Ashokan Brahmi inscriptions dedicate the caves to the ascetic <strong>Ajivika sect</strong> (Makkhali Gosala), proving early imperial secular pluralism.</td>
            </tr>
            <tr>
              <td><strong>Western Ghats Caves</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Karle, Bhaja, Kanheri, Bedse (Maharashtra)</span></td>
              <td><strong>Satavahana &amp; Western Kshatrapa</strong> era (2nd c. BCE – 2nd c. CE); patronized by merchant guilds (Shrenis).</td>
              <td>Established the canonical Buddhist rock-cut layout:<br>
                &bull; <strong>Chaitya Hall</strong>: Apsidal sanctuary with arched nave, aisles, aniconic stupa, and horseshoe Sun-window (Chaitya arch); <strong>Karle Cave 8</strong> is India's largest rock-cut Chaitya (40m long) retaining 2,000-year-old teakwood vaulted roof ribs.<br>
                &bull; <strong>Vihara</strong>: Monastic dwelling hall with rock-cut stone sleeping benches.</td>
              <td>Donor inscriptions record gifts from Yavanas (Greeks), weavers, ironmongers, and royal queens; strategic locations guarded Bhor Ghat trade passes connecting Konkan ports (Sopara, Kalyan) to the Deccan hinterland.</td>
            </tr>
            <tr>
              <td><strong>Ajanta Caves</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Aurangabad, Maharashtra<br>(Waghora River Gorge)</span></td>
              <td>Two distinct phases:<br>
                &bull; 1st Phase: Hinayana / Satavahana (2nd c. BCE – 1st c. CE; Caves 9, 10, 12, 13, 15A).<br>
                &bull; 2nd Phase: Mahayana / Vakataka under King <strong>Harishena</strong> (5th c. CE; Caves 1, 2, 16, 17, 19, 26).</td>
              <td>29 rock-cut caves carved into a sheer horseshoe basalt cliff; absence of external courtyards due to vertical topography; contains both elaborate chaityas (Caves 19, 26) and multi-celled pillared viharas.</td>
              <td>UNESCO World Heritage; peak of <strong>Fresco-secco</strong> mural art (mineral colors on dry clay-cowdung plaster):<br>
                &bull; Cave 1: <strong>Bodhisattva Padmapani</strong> (holding blue lotus in Tribhanga) &amp; <strong>Vajrapani</strong>.<br>
                &bull; Cave 16: The poignant <em>Dying Princess</em> (Sundari, wife of Nanda).<br>
                &bull; Cave 17: Jataka narrative cycles (Vessantara, Shibi, Chhadanta).<br>
                &bull; Cave 26: Monumental 29-foot rock-carved <strong>Mahaparinirvana of Buddha</strong>.</td>
            </tr>
            <tr>
              <td><strong>Ellora Caves (Verul)</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Aurangabad, Maharashtra<br>(Charanandri Hills)</span></td>
              <td>Rashtrakuta, Kalachuri, and Yadava dynasties (c. 6th to 10th c. CE); unique triple-faith confluence.</td>
              <td>34 caves carved on sloping basalt hills with spacious open courtyards:<br>
                &bull; <strong>Buddhist Caves (1–12)</strong>: Multi-storeyed viharas; Cave 10 <em>Vishvakarma</em> (Carpenter's Chaitya) with vaulted ribs.<br>
                &bull; <strong>Hindu Caves (13–29)</strong>: Cave 15 <em>Dashavatara</em>; Cave 21 <em>Rameshvara</em>; Cave 29 <em>Dhumar Lena</em>.<br>
                &bull; <strong>Jain Caves (30–34)</strong>: Digambara sect; Cave 32 <em>Indra Sabha</em> with Bahubali entangled in forest creepers.<br>
                &bull; <strong>Monolithic Climax</strong>: Cave 16 <strong>Kailash Temple</strong> built by Rashtrakuta King <strong>Krishna I</strong> (8th c. CE)—world's largest monolithic top-down vertical excavation, quarrying 200,000 tons of basalt to carve a complete Dravidian temple complex.</td>
              <td>Cave 15 depicts Vishnu as <strong>Narasimha</strong> disemboweling Hiranyakashipu; Cave 21 Rameshvara features breathtaking life-sized river goddesses <strong>Ganga</strong> (on Makara) and <strong>Yamuna</strong> (on Tortoise) and the Kalyanasundaramurti (marriage of Shiva-Parvati); Cave 16 contains the titanic relief of <em>Ravana Shaking Mount Kailash</em>.</td>
            </tr>
            <tr>
              <td><strong>Elephanta Caves (Gharapuri)</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Mumbai Harbour, Maharashtra</span></td>
              <td>Kalachuri &amp; Rashtrakuta contemporary (c. 6th – 8th c. CE); Shaivite rock sanctuary.</td>
              <td>Colossal rock-hewn pillared mandapa with fluted columns and cushion capitals; architectural affinity with Ellora Cave 21 and Kailash temple.</td>
              <td>The world-renowned 20-foot <strong>Sadashiva Trimurti</strong> colossal bust capturing the threefold cosmic persona of Shiva:<br>
                &bull; Central Face: <em>Tatpurusha / Mahadeva</em> (serene, contemplative creator).<br>
                &bull; Left (Viewer's): <em>Aghora / Bhairava</em> (fierce destroyer, skull in matted locks).<br>
                &bull; Right (Viewer's): <em>Vamadeva / Uma</em> (graceful, feminine preserver holding a lotus).<br>
                Also showcases dramatic rock reliefs of Gangadhara, Ardhanarishvara, and Nataraja.</td>
            </tr>
            <tr>
              <td><strong>Bagh Caves</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Dhar, Madhya Pradesh<br>(Bagh River)</span></td>
              <td>Gupta-Vakataka contemporary (c. 5th – 6th c. CE); Buddhist monastic sanctuary.</td>
              <td>Group of 9 rock-cut Buddhist caves excavated into soft red sandstone; primarily large residential monastic Viharas with pillared central halls.</td>
              <td>Renowned for secular, courtly, and religious tempera wall murals in Cave 4 (<strong>Rang Mahal</strong>): portrays royal processions of caparisoned elephants, cavalry, and the lively group folk dance <strong>Hallisaka</strong> (circular dance of women accompanied by sticks and drums).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Comparison 14: Fourfold Classification of Indian Musical Instruments -->
      <h3 style="margin-top:36px;">14. Fourfold Classification of Indian Musical Instruments (Natya Shastra &amp; Ancient Acoustic Scheme)</h3>
      <div class="comparison-table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th style="width:16%;">Acoustic Category (Vadya)</th>
              <th style="width:20%;">Physical Mechanics &amp; Acoustic Physics</th>
              <th style="width:34%;">Landmark Classical, Folk &amp; Temple Instruments</th>
              <th style="width:30%;">Vedic, Epigraphic &amp; Treatise Documentation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1. Tata Vadya</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Chordophones (Stringed Instruments)</span></td>
              <td>Sound produced by the vibration of stretched strings under tension; sound amplified by hollow wooden soundboxes or dried gourds (<em>Tumba</em>); played by plucking with fingers/plectrum (Tat) or bowing with a horsehair bow (Vitat).</td>
              <td><strong>Classical Plucked</strong>: Saraswati Veena (South), Rudra Veena (Dhrupad), Chitra Veena (Gottuvadhyam fretless), Sitar (Amir Khusrau evolution), Sarod (fretless steel plate), Surbahar, Santoor (100-string hammered dulcimer of Kashmir).<br>
                <strong>Classical Bowed</strong>: Sarangi (carved from single block of cedar wood with 3 gut playing strings and up to 39 sympathetic resonance strings), Dilruba, Esraj.<br>
                <strong>Folk</strong>: Ektara (Baul singers), Dotara, Ravanahatha (Rajasthan), Kamayacha (Manganiyars).</td>
              <td>Rigveda mentions the 100-stringed <em>Vana</em>; Samaveda chants accompanied by the <em>Katyayana Veena</em>; Bharata's <em>Natya Shastra</em> classifies stringed instruments into Tat and Vitat; Sarangadeva's <em>Sangita Ratnakara</em> details veena fret construction.</td>
            </tr>
            <tr>
              <td><strong>2. Sushira Vadya</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Aerophones (Wind Instruments)</span></td>
              <td>Sound produced by vibrating air columns enclosed within hollow cylindrical tubes, reeds, or chambers; pitch altered by opening and closing fingerholes or modulating breath pressure.</td>
              <td><strong>Classical Flutes</strong>: Bansuri (North Indian bamboo flute with 6–7 fingerholes, popularized by Pt. Hariprasad Chaurasia), Venu / Pullanguzhal (South Indian 8-hole Carnatic flute).<br>
                <strong>Double-Reed Sanctum Winds</strong>: Shehnai (auspicious double-reed oboe, elevated to global concert status by Ustad Bismillah Khan), Nadaswaram (world's loudest non-brass acoustic wind instrument; mandatory <em>Mangala Vadya</em> in South Indian temples).<br>
                <strong>Folk &amp; Ritual</strong>: Pungi / Been (snake-charmer's dried bottle gourd pipe), Algorza (double flute played simultaneously via circular breathing in Rajasthan), Kombu (brass C-shaped trumpet of Kerala).</td>
              <td>Eternally personified in Lord Krishna's divine flute (<em>Murali / Venu</em>); described in Aitareya Brahmana and Valmiki Ramayana; considered the purest acoustic medium closely mimicking the human vocal range.</td>
            </tr>
            <tr>
              <td><strong>3. Avanaddha Vadya</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Membranophones (Percussion Drums)</span></td>
              <td>Sound produced by striking animal skins or membranes stretched tightly over hollow clay, wooden, or metal resonators; struck with bare hands, finger pads, or curved wooden sticks.</td>
              <td><strong>Classical Dual Drums</strong>: Tabla (pair of drums: left bass <em>Bayan/Dagga</em> made of brass/clay, and right wooden treble <em>Dayan</em>; tuned with black iron-dust paste patch <em>Siyahi</em>).<br>
                <strong>Barrel Drums</strong>: Mridangam (the primary rhythmic engine of Carnatic music; two-headed barrel drum tuned with semolina/rice paste), Pakhawaj (deep, majestic resonance for Dhrupad singing), Khol / Mridanga (terracotta drum of Bengal and Assam Bhakti Sattras).<br>
                <strong>Temple &amp; Folk Drums</strong>: Chenda (cylindrical vertical wooden drum played with sticks in Kathakali), Thavil (played with finger caps in South Indian temple ensembles), Dholak, Damaru (hourglass drum of Lord Shiva).</td>
              <td>Rigveda repeatedly praises the thunderous <em>Dundubhi</em> war drum; Bharata dedicates extensive chapters of <em>Natya Shastra</em> to rhythmic syllables (<em>Bols</em>) and the craft of applying paste to drumheads to dampen unwanted acoustic overtones.</td>
            </tr>
            <tr>
              <td><strong>4. Ghana Vadya</strong><br><span style="font-size:0.82rem; color:var(--ink-soft);">Idiophones (Solid Resonant Percussion)</span></td>
              <td>Solid instruments that vibrate by their own structural mass without requiring strings or stretched membranes; sound generated by striking, clashing, shaking, or scraping resonant metal, clay, stone, wood, or glass.</td>
              <td><strong>Classical Cymbals &amp; Percussion</strong>: Manjira / Taal / Kartal (tuned bronze hand cymbals keeping tala cycles in Bhakti bhajans), Ghatam (specially baked clay pot reinforced with brass and copper filings, played with finger knuckles and palm across the open mouth to produce acoustic bass resonances), Jal Tarang (porcelain bowls filled with calibrated water levels struck with bamboo sticks).<br>
                <strong>Folk &amp; Classical Accompaniments</strong>: Morsing (metal jaw harp vibrating between player's teeth), Kanjira (small frame drum with lizard-skin and brass jingles), Chimta (iron tongs with attached brass jingle discs), Ghungroos (resonant brass ankle bells worn by classical dancers).</td>
              <td>Oldest class of acoustic instruments in human civilization; prehistoric rock art depicts idiophones; Yajurveda mentions metal clappers; serves as the foundational timekeeping metronome for all Indian ritual music.</td>
            </tr>
          </tbody>
        </table>
      </div>
'''

html_updated = html.replace(target, target + NEW_COMPARISONS)

with open('art-culture.html', 'w', encoding='utf-8') as f:
    f.write(html_updated)

print("Updated art-culture.html with Comparisons 11, 12, 13, and 14!")
