# -*- coding: utf-8 -*-
"""
Enrich art-culture.html with:
1. Epigraphic & Numismatic Art Traditions (Art Forms)
2. Six Orthodox Schools of Indian Philosophy (Literature / Philosophy)
3. Comparison Table 4: Trabeate (Ancient/Hindu) vs. Arcuate (Indo-Islamic) Architecture
4. Comparison Table 5: The Six Orthodox Schools of Indian Philosophy (Shad-Darshanas)
5. Update pill counts: (45) total, (23) art forms, (9) literature, (13) architecture
"""

with open('art-culture.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update pill counts in header
content = content.replace(
    'All Culture Topics (43)',
    'All Culture Topics (45)'
).replace(
    '🎨 Indian Art Forms (22)',
    '🎨 Indian Art Forms (23)'
).replace(
    '📜 Literature (8)',
    '📜 Literature (9)'
)

# 2. Add the two new comparison tables before </section> id="cultureComparisonsSection"
new_tables = """
      <!-- Comparison 4: Trabeate vs Arcuate Structural Systems -->
      <h3 style="margin-top:34px;">4. Structural Engineering: Trabeate (Ancient/Hindu) vs. Arcuate (Indo-Islamic) Systems</h3>
      <div class="comparison-table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Engineering Parameter</th>
              <th>Trabeate / Corbelled Style (Traditional Indian)</th>
              <th>Arcuate Style (Indo-Islamic Engineering)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Primary Structural Principle</strong></td>
              <td>Lintel-and-beam construction; horizontal beams supported by vertical stone pillars and corbelled courses.</td>
              <td>True arches, vaults, and domes constructed with radiating wedge-shaped stones (voussoirs) held by a central keystone.</td>
            </tr>
            <tr>
              <td><strong>Roofing &amp; Superstructure</strong></td>
              <td>Pyramidal Shikharas, stepped Vimanas, flat roofs, and corbelled stone ceilings.</td>
              <td>Hemispherical or bulbous Domes, squinch-arch transitions, barrel vaults, and cross vaults.</td>
            </tr>
            <tr>
              <td><strong>Vertical Elevational Elements</strong></td>
              <td>Pillars, carved brackets, Stambhas, and massive multi-storeyed Gopurams.</td>
              <td>Slender Minarets (serving acoustic elevation for Azan and seismic counter-weight stability).</td>
            </tr>
            <tr>
              <td><strong>Binding Medium</strong></td>
              <td>Dry-masonry stone interlocking without mortar; iron dowels and stone clamps.</td>
              <td>High-strength gypsum and lime-mortar (Surkhi) cementing heavy stone and brick arches.</td>
            </tr>
            <tr>
              <td><strong>Decorative Techniques</strong></td>
              <td>Intricate human, animal, celestial (Apsaras, Gandharvas), and mythological iconographic sculptures.</td>
              <td>Theological avoidance of living icons; adoption of <em>Arabesque</em> (foliage grids), <em>Calligraphy</em>, <em>Pietra Dura</em> (inlaid semi-precious stone), and <em>Jali</em> screens.</td>
            </tr>
            <tr>
              <td><strong>Prominent Examples</strong></td>
              <td>Khajuraho temples, Brihadisvara (Thanjavur), Sun Temple (Modhera), Halebidu Hoysaleswara.</td>
              <td>Alai Darwaza (Delhi, 1311 CE - earliest true arch), Tomb of Iltutmish (squinch), Taj Mahal (double-dome), Gol Gumbaz (Bijapur).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Comparison 5: The Six Orthodox Schools of Indian Philosophy -->
      <h3 style="margin-top:34px;">5. Classical Indian Philosophy: The Six Orthodox Schools (Shad-Darshanas)</h3>
      <div class="comparison-table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th>School (Darshana)</th>
              <th>Founding Sage &amp; Text</th>
              <th>Core Metaphysical &amp; Epistemological Tenet</th>
              <th>UPSC High-Yield Benchmark</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Samkhya</strong></td>
              <td>Kapila Muni<br><em>Samkhya Pravachana Sutra</em></td>
              <td>Strict Dualism: Universe consists of two eternal, independent realities: <strong>Purusha</strong> (pure consciousness) and <strong>Prakriti</strong> (matter/nature). Evolution of 24 Tattvas. Originally non-theistic.</td>
              <td>Oldest philosophical school; provides the metaphysical foundation upon which Patanjali's Yoga psychology is erected.</td>
            </tr>
            <tr>
              <td><strong>Yoga</strong></td>
              <td>Patanjali<br><em>Yoga Sutra</em></td>
              <td>Practical methodology for liberation through mental discipline: <strong>Ashtanga Yoga</strong> (Yama, Niyama, Asana, Pranayama, Pratyahara, Dharana, Dhyana, Samadhi). Admits God (Ishvara) as personal focus.</td>
              <td>Citta-vritti-nirodha (cessation of mental fluctuations); recognizes Ashtanga path as bridge to liberation.</td>
            </tr>
            <tr>
              <td><strong>Nyaya</strong></td>
              <td>Gautama (Akshapada)<br><em>Nyaya Sutra</em></td>
              <td>Rigorous school of Logic and Epistemology. Valid knowledge obtained via four Pramanas: <em>Pratyaksha</em> (perception), <em>Anumana</em> (inference), <em>Upamana</em> (comparison), and <em>Shabda</em> (verbal testimony).</td>
              <td>Introduced systematic syllogistic logic (Pancha-Avayava five-step inference); foundational for Indian dialectics.</td>
            </tr>
            <tr>
              <td><strong>Vaisheshika</strong></td>
              <td>Kanada (Uluka)<br><em>Vaisheshika Sutra</em></td>
              <td>Atomistic Pluralism &amp; Naturalism. All physical objects are reducible to indivisible, eternal atoms (<strong>Paramanus</strong>) of 4 elements (earth, water, fire, air) combined with space, time, ether, and mind.</td>
              <td>Pioneered atomic theory in ancient India; classified reality into seven Padarthas (categories).</td>
            </tr>
            <tr>
              <td><strong>Purva Mimamsa</strong></td>
              <td>Jaimini<br><em>Mimamsa Sutra</em></td>
              <td>Ritualistic validation of the Vedas. Vedas are eternal and unauthored (Apaurusheya). Ultimate duty (Dharma) lies in performing Vedic sacrifices (Yajnas) for cosmic order and merit (Apurva).</td>
              <td>Emphasizes ritual orthopraxy and Sanskrit grammar; Shabara and Kumarila Bhatta were master commentators.</td>
            </tr>
            <tr>
              <td><strong>Uttara Mimamsa (Vedanta)</strong></td>
              <td>Badarayana<br><em>Brahma Sutras</em></td>
              <td>Philosophical culmination of the Upanishads. Inquires into Brahman (Ultimate Reality) and Atman (Self). Divided into three master streams:<br>
              • <strong>Advaita</strong> (Adi Shankara): Absolute Monism; <em>Brahma Satyam Jagan Mithya</em> (Brahman alone is real, the empirical world is an illusion/Maya).<br>
              • <strong>Vishishtadvaita</strong> (Ramanuja): Qualified Non-Dualism; Jiva and Jagat are real attributes of personal God Vishnu.<br>
              • <strong>Dvaita</strong> (Madhvacharya): Strict Dualism; eternal distinction between Brahman and individual souls.</td>
              <td>Forms the bedrock of classical Hinduism and philosophical synthesis; inspired Swami Vivekananda and modern Indian renaissance.</td>
            </tr>
          </tbody>
        </table>
      </div>
"""

# Insert before end of cultureComparisonsSection
end_comp_idx = content.find('</div>\n  </section>\n\n  <!-- Section 3: UPSC Mains Model Answer Frameworks -->')
if end_comp_idx != -1:
    content = content[:end_comp_idx] + new_tables + content[end_comp_idx:]
    print("SUCCESS: Inserted Comparison Tables 4 and 5 into art-culture.html")
else:
    print("Warning: could not find exact anchor for comparison tables, looking for fallback...")
    fallback_anchor = '<!-- Section 3: UPSC Mains Model Answer Frameworks -->'
    fb_idx = content.find(fallback_anchor)
    if fb_idx != -1:
        # insert before the closing of section 2
        last_div_sec = content.rfind('</div>\n  </section>', 0, fb_idx)
        content = content[:last_div_sec] + new_tables + content[last_div_sec:]
        print("SUCCESS: Inserted Comparison Tables via fallback anchor")

# 3. Add the two new CULTURE_DATA cards
new_cards = """,
  {
    "id": "epigraphic-numismatic-art",
    "category": "art-forms",
    "type": "Epigraphy & Numismatics",
    "title": "Epigraphic & Numismatic Art Traditions of Ancient India",
    "era": "6th c. BCE – 12th c. CE",
    "subtitle": "Evolution of Brahmi/Kharosthi Scripts & Royal Coinage Iconography (Punch-Marked to Gupta Dinaras)",
    "image": "assets/culture/ancient-scientific-literature.jpg",
    "imgCaption": "Gupta Gold Dinara (Samudragupta Lyrist / Veena Type)",
    "imgCredit": "National Museum New Delhi / Public Domain",
    "desc": "Inscriptions and royal coins constituted the paramount visual, linguistic, and political communication media of ancient Indian monarchs, conveying sovereign power, dynastic genealogies, religious legitimacy, and economic health across vast subcontinental expanses.",
    "features": [
      "Evolution of Ancient Scripts: Ashokan Brahmi (ancestor of 90% modern Indic scripts, deciphered by James Prinsep 1837); Kharosthi (written right-to-left in North-West Gandhara, derived from Aramaic); Gupta Brahmi (refined cursive script); Siddhamatrika / Proto-Bengali; Devanagari in North and Grantha in South.",
      "Punch-Marked Coins (Puranas / Karshapanas, c. 6th c. BCE): Earliest indigenous coinage; irregular silver/copper pieces stamped with 5 punch symbols (sun, six-armed wheel, hill, peacock, elephant) issued by merchant guilds (Shrenis) and Janapadas.",
      "Indo-Greek Numismatic Revolution: Introduced realistic royal portraiture and bilingual legends (Greek obverse, Kharosthi reverse) like Menander/Milinda; set the aesthetic standard for subsequent Indian dynastic issues.",
      "Kushana Gold Standard: Introduced high-purity gold dinars (8 grams) modelled on Roman denarii; featured syncretic deities from Greek (Helios, Selene), Iranian (Mithra, Nana), and Hindu-Buddhist pantheons (Oesho/Shiva with Nandi, standing Buddha with Greek legend BODDO).",
      "Gupta Golden Age Coinage: Zenith of numismatic art; minted in diverse thematic series: Archer Type, Tiger Slayer Type, Battle-Axe Type, Asvamedha Type, and Samudragupta Lyrist Type (depicting the emperor playing the seven-stringed Veena, proving his musical title 'Kaviraja').",
      "Royal Prashastis as Monumental Epigraphs: Allahabad Pillar Inscription (Prayag Prashasti) composed by Harishena in ornate Champukavya Sanskrit; Aihole Inscription by Ravikirti celebrating Pulakeshin II's victory over Harsha; Junagadh Inscription of Rudradaman recording Sudarshana lake repairs."
    ],
    "upscFact": "UPSC Prelims Question: The earliest coins bearing portraits of kings and bilingual legends in India were issued by the Indo-Greeks (c. 2nd Century BCE); Samudragupta's Lyrist-type gold coin proves his proficiency in musical arts.",
    "timelineRef": "gupta-age",
    "bookRef": "Upinder Singh, Ch. 2; D.C. Sircar, Indian Epigraphy; Nitin Singhania, Ch. 21"
  },
  {
    "id": "six-darshanas-philosophy",
    "category": "literature",
    "type": "Classical Philosophy",
    "title": "The Six Orthodox Schools of Indian Philosophy (Shad-Darshanas)",
    "era": "c. 6th c. BCE – 16th c. CE",
    "subtitle": "Samkhya, Yoga, Nyaya, Vaisheshika, Mimamsa & Vedanta (Advaita, Vishishtadvaita, Dvaita)",
    "image": "assets/culture/vedic-sanskrit-literature.jpg",
    "imgCaption": "Adi Shankaracharya (Advaita Vedanta) & Ancient Manuscript Palm Leaves",
    "imgCredit": "Archaeological Survey of India / Public Domain",
    "desc": "Classical Indian philosophy is organized into six orthodox (Astika) schools that acknowledge the authority of the Vedas, providing comprehensive metaphysical, epistemological, ethical, and spiritual frameworks explaining the nature of consciousness, reality, and liberation (Moksha).",
    "features": [
      "Samkhya (Kapila Muni): Oldest school; propounds uncompromised metaphysical dualism between Purusha (eternal, immutable pure consciousness) and Prakriti (primal dynamic matter); evolution occurs through the interplay of three Gunas (Sattva, Rajas, Tamas).",
      "Yoga (Patanjali): Practical, empirical path of spiritual psychology; codifies Ashtanga Yoga (8 limbs: Yama, Niyama, Asana, Pranayama, Pratyahara, Dharana, Dhyana, Samadhi) for Citta-vritti-nirodha (cessation of mental modifications).",
      "Nyaya (Gautama): Epistemology and formal logic; holds that human suffering stems from ignorance, which can be dispelled through four valid means of knowledge (Pramanas: Pratyaksha, Anumana, Upamana, Shabda); established the 5-member syllogism.",
      "Vaisheshika (Kanada): Naturalistic atomic pluralism; posits that the physical cosmos is composed of eternal, indivisible atoms (Paramanus) of earth, water, fire, and air; classified all reality into seven Padarthas (substance, quality, action, generality, particularity, inherence, non-existence).",
      "Purva Mimamsa (Jaimini): Orthopraxic philosophy of Vedic action and ritual; asserts that the Vedas are eternal (Apaurusheya) and infallible; Dharma consists in meticulous performance of Vedic sacrifices generating unseen spiritual merit (Apurva).",
      "Uttara Mimamsa (Vedanta): Culmination of Upanishadic thought; inquires into Brahman (Ultimate Reality) and Atman. Evolved three master sub-schools: Advaita (Adi Shankara - absolute non-dualism: Nirguna Brahman, world is Maya); Vishishtadvaita (Ramanuja - qualified non-dualism, personal devotion to Vishnu); and Dvaita (Madhvacharya - absolute dualism between God and souls)."
    ],
    "upscFact": "UPSC Prelims Question: The Vaisheshika school propounded the atomic theory (Paramanuvada) in ancient India; Adi Shankara established 4 mathas at Sringeri, Puri, Dwaraka, and Badrinath to propagate Advaita Vedanta.",
    "timelineRef": "vedic-age",
    "bookRef": "Nitin Singhania, Ch. 14; S. Radhakrishnan, Indian Philosophy; A.L. Basham, Ch. 7"
  }
"""

# Insert before closing bracket of CULTURE_DATA
closing_bracket = '\n];\n\n// Tab Switching'
idx_cb = content.find(closing_bracket)
if idx_cb != -1:
    content = content[:idx_cb] + new_cards + content[idx_cb:]
    print("SUCCESS: Added epigraphic-numismatic-art and six-darshanas-philosophy to CULTURE_DATA")
else:
    print("Error: could not find CULTURE_DATA closing bracket!")

with open('art-culture.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully written enriched art-culture.html!")
