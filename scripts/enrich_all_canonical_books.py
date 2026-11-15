import re

with open('books.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Dictionary of enrichments keyed by exact book title
ENRICHMENTS = {
    "India's Ancient Past": '''<div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes (All 33 Chapters Synthesized)</h4>
            <ul>
              <li><strong>Material Factors &amp; Environment (Ch. 1–6):</strong> Ecological role of the monsoon, alluvial fertility, and dense Gangetic forests requiring iron axes (not bronze); copper belt of Khetri/Singhbhum; lack of domestic tin preventing a full Bronze Age outside the Indus basin.</li>
              <li><strong>Prehistory to Proto-history (Ch. 7–11):</strong> Lower Palaeolithic Acheulian tools (Soan, Attirampakkam); Mesolithic microliths &amp; animal herding (Bagor, Adamgarh); Neolithic agricultural transition (Mehrgarh, Burzahom pit-dwellings, Chirand antler tools, South Indian ash-mounds); Chalcolithic regional limitations (Ahar, Malwa, Jorwe).</li>
              <li><strong>Harappan Urbanism &amp; Aryan Debate (Ch. 12–15):</strong> Gridiron town planning, binary/decimal weights, Meluha maritime trade; Steppe pastoralists, spoked wheels, <em>asva</em>, and transition from Rigvedic pastoral <em>gopati</em> / <em>gavisti</em> to Later Vedic sedentary territorial <em>janapadas</em> and Painted Grey Ware (PGW).</li>
              <li><strong>Second Urbanization &amp; Heterodox Thought (Ch. 16–19):</strong> Mid-Gangetic ironization, Northern Black Polished Ware (NBPW), silver punch-marked coins (<em>karshapanas</em>), merchant guilds (<em>shrenis</em>), and emergence of Buddhism and Jainism backed by the rising Vaishya mercantile class.</li>
              <li><strong>Imperial Mauryas to Post-Mauryan Boom (Ch. 20–25):</strong> Centralized statecraft in Kautilya's <em>Arthashastra</em>, Ashoka's Dhamma; Indo-Greek portrait coins, Kushana gold dinaras pegged to Roman aureus, Satavahana royal land grants to monks/Brahmins (seed of feudalism), Sangam Roman trade.</li>
              <li><strong>Guptas &amp; The Early Medieval Feudalism Debate (Ch. 26–33):</strong> Imperial expansion, classical art/literature (Kalidasa, Aryabhata), land grant economy (<em>Agraharas</em>), <em>vishti</em> (forced labour), decay of urban centers, debased coins, and the <em>Kaliyuga</em> crisis driving early Indian feudalism.</li>
            </ul>
          </div>''',

    "A Brief History of Modern India": '''<div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes (Spectrum Master Synthesis)</h4>
            <ul>
              <li><strong>Advent of Europeans &amp; British Conquest:</strong> Portuguese (Almeida's Blue Water Policy, Albuquerque), Anglo-French Carnatic Wars (Dupleix), Battle of Plassey (1757), Battle of Buxar (1764) &amp; Dual Government of Bengal; Anglo-Mysore, Anglo-Maratha, and Anglo-Sikh Wars.</li>
              <li><strong>Expansionist Doctrines &amp; Annexation Policies:</strong> Ring Fence (Warren Hastings), Subsidiary Alliance (Wellesley: Hyderabad 1798 first), Doctrine of Lapse (Dalhousie: Satara 1848, Sambalpur, Jhansi, Nagpur); Conquest of Sindh (1843, Napier) and Awadh annexation (1856 on misgovernance).</li>
              <li><strong>Economic Drain &amp; Land Revenue Systems:</strong> Permanent Settlement (1793, Cornwallis, sunset law), Ryotwari (1820, Munro &amp; Reed), Mahalwari (1822/1833, Holt Mackenzie &amp; Martin Bird); Deindustrialization of weavers; Dadabhai Naoroji's Drain of Wealth and Home Charges.</li>
              <li><strong>Revolt of 1857 &amp; Resistance:</strong> Causes (greased cartridges, general service enlistment act), leaders (Nana Sahib, Rani Lakshmibai, Kunwar Singh, Begum Hazrat Mahal), suppression by Campbell, Rose, Nicholson; GoI Act 1858 and Queen's Proclamation.</li>
              <li><strong>Socio-Religious Renaissance:</strong> Brahmo Samaj (Rammohan Roy), Arya Samaj (Dayananda Saraswati, <em>Satyarth Prakash</em>), Satyashodhak Samaj (Jyotirao Phule, <em>Gulamgiri</em>), Ramakrishna Mission (Vivekananda), Theosophical Society, Aligarh Movement (Sir Syed Ahmed Khan), Self-Respect Movement (Periyar).</li>
              <li><strong>Freedom Struggle Trajectory (1885–1947):</strong> Moderates (1885–1905, 3Ps), Extremists &amp; Swadeshi (1905–1908, Lal-Bal-Pal), Surat Split (1907), Revolutionary Phase I (Ghadar 1913, Anushilan), Gandhian Satyagrahas (Champaran, Kheda, Ahmedabad, NCM 1920–22, CDM 1930–34, Quit India 1942), Revolutionary Phase II (HRA/HSRA, Bhagat Singh, Surya Sen), INA &amp; Partition 1947.</li>
            </ul>
          </div>''',

    "India's Struggle for Independence": '''<div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes (Nationalist Mass Mobilization)</h4>
            <ul>
              <li><strong>Gramscian Hegemony &amp; Anti-Imperialist Ideology:</strong> The national movement as an ideological struggle undermining British moral hegemony and the "benevolent despotism" myth through constitutional, press, and mass critiques.</li>
              <li><strong>Struggle-Truce-Struggle (S-T-S) Strategy:</strong> Bipan Chandra's definitive analytical paradigm explaining Gandhian mass movements — active confrontation phases (NCM, CDM) alternating with passive consolidation/constructive work phases to regroup mass energy without exhaustion.</li>
              <li><strong>Economic Critique as the Foundation of Nationalism:</strong> The seminal intellectual work of the Early Nationalists (Naoroji, Ranade, R.C. Dutt) in proving that British rule caused systemic structural underdevelopment, turning anti-colonial sentiment into a unified pan-Indian consciousness.</li>
              <li><strong>Multi-Class Coalition &amp; Peasant-Worker Dynamics:</strong> Mobilization of the peasantry (Champaran, Bardoli, Kisan Sabhas) and industrial working class (AITUC 1920); delicate mediation between landlord-peasant tensions to preserve national unity.</li>
              <li><strong>Revolutionary Terrorism vs. Mass Agitation:</strong> Sympathetic critique of revolutionary heroes (Bhagat Singh, Sukhdev, Chandrashekhar Azad) highlighting their ideological evolution towards scientific socialism, while demonstrating the strategic limitations of individual heroic actions compared to organized mass mobilization.</li>
              <li><strong>Communalism &amp; The Tragic Climax of Partition:</strong> Deep historical autopsy of communalism as a modern false consciousness nurtured by British divide-and-rule (separate electorates 1909/1919), culminating in the 1940 Pakistan Resolution, Direct Action Day (1946), and tragic vivisection of 1947.</li>
            </ul>
          </div>''',

    "A New Look at Modern Indian History": '''<div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes (Administrative &amp; Constitutional Rigour)</h4>
            <ul>
              <li><strong>Evolution of British Administrative Institutions:</strong> Detailed institutional breakdown of the Regulating Act of 1773, Pitts India Act of 1784, Charter Acts of 1793, 1813, 1833, 1853; separation of executive from judiciary and the rise of Cornwallis's steel frame Civil Services.</li>
              <li><strong>Comprehensive Profiles of Governors-General &amp; Viceroys:</strong> Warren Hastings (judicial plans), Cornwallis (Permanent Settlement &amp; Code), Wellesley (Subsidiary Alliance), William Bentinck (Abolition of Sati 1829, English education 1835), Dalhousie (Railways 1853, Telegraph, PWD, Lapse), Lytton (Vernacular Press Act 1878, Arms Act), Ripon (Father of Local Self-Government, Ilbert Bill 1883), Curzon (Partition of Bengal 1905).</li>
              <li><strong>Constitutional Reforms Matrix:</strong> Indian Councils Acts of 1861 &amp; 1892 (budget discussion rights); Morley-Minto Reforms (1909, separate electorates for Muslims); Montagu-Chelmsford Reforms (GoI Act 1919, Dyarchy in provinces, bicameralism); Government of India Act 1935 (Provincial Autonomy, All-India Federation, Dyarchy at Centre).</li>
              <li><strong>Anglo-Mysore, Anglo-Maratha &amp; Anglo-Sikh Warfare:</strong> Military strategies, treaties (Madras 1769, Mangalore 1784, Seringapatam 1792; Surat 1775, Purandhar 1776, Salbai 1782, Bassein 1802; Lahore 1846), artillery innovations of Haidar Ali/Tipu, and internal factionalism enabling British conquest.</li>
            </ul>
          </div>''',

    "Sapiens: A Brief History of Humankind": '''<div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes (Anthropological &amp; Civilizational Vectors)</h4>
            <ul>
              <li><strong>The Cognitive Revolution (~70,000 BP):</strong> Emergence of symbolic language enabling <em>Homo sapiens</em> to communicate about imagined realities (myths, religions, nations, legal systems) — the crucial foundation that allowed flexible cooperation in groups exceeding the Dunbar number of 150.</li>
              <li><strong>The Agricultural Revolution (~12,000 BP):</strong> "History's Biggest Fraud" — transition from varied foraging diets to monotonous sedentary cereal farming (wheat, rice); population explosion, private property, permanent hierarchies, and structural gender subordination.</li>
              <li><strong>The Three Great Unifiers of Humankind:</strong>
                <br>&bull; <em>Money:</em> Universal trust system overcoming barter limitations (Punch-Marked coins, Roman denarii).
                <br>&bull; <em>Empires:</em> Political structures integrating diverse ethnic groups under unified legal systems (Mauryas, Romans, Mughals).
                <br>&bull; <em>Universal Religions:</em> Trans-tribal moral orders asserting cosmic law (Buddhism, Christianity, Islam).
              </li>
              <li><strong>The Scientific Revolution (~500 BP):</strong> The discovery of ignorance (<em>Ignoramus</em>), empirical experimentation, and the unprecedented marriage of science with imperial capitalism and industrial technology.</li>
            </ul>
          </div>''',

    "Modern India &amp; World History Master Compendiums": '''<div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes (Visual Pipelines &amp; Thematic Flowcharts)</h4>
            <ul>
              <li><strong>Freedom Struggle Visual Pipelines (21 PPT Modules):</strong> Comprehensive flowcharts tracing Europeans' arrival, British economic exploitation (deindustrialization &amp; drain), 1857 revolt command centers, Moderate-Extremist ideological debates, Revolutionary nationalism phases I &amp; II (Ghadar, HSRA, Chittagong), and the Gandhian mass movement crescendo (1915–1947).</li>
              <li><strong>Atlantic &amp; European Revolutions (World History):</strong> American Revolution (1776, No Taxation without Representation, Constitution), French Revolution (1789, Estates-General, Fall of Bastille, Jacobins, Napoleonic Wars, Waterloo 1815), and Congress of Vienna (1815, Metternich Concert of Europe).</li>
              <li><strong>19th-Century European Nation-State Unification:</strong> Unification of Italy (Mazzini, Garibaldi, Cavour) and Unification of Germany (Bismarck's "Blood and Iron", Franco-Prussian War 1870–71).</li>
              <li><strong>Totalitarian Regimes &amp; World Wars:</strong> Causes and catastrophic trenches of World War I; Russian Revolution 1917 (Lenin, Bolsheviks); Interwar rise of Italian Fascism (Mussolini) and German Nazism (Hitler); World War II (Stalingrad, Pacific War, Holocaust, Atomic bombs).</li>
              <li><strong>Cold War &amp; Decolonization:</strong> US-Soviet bipolar rivalry, Truman Doctrine, Cuban Missile Crisis, Vietnam War, Non-Aligned Movement (NAM, Bandung 1955), and Collapse of the USSR (1991).</li>
            </ul>
          </div>''',

    "From Plassey to Partition and After": '''<div class="book-chapters">
            <h4>Core UPSC Concepts &amp; Key Themes (Critical &amp; Subaltern Historiography)</h4>
            <ul>
              <li><strong>The 18th-Century Transition: Continuity vs. Rupture:</strong> Deconstructs the colonial "Dark Age" myth; highlights dynamic commercialization, regional proto-states (Bengal, Awadh, Mysore, Hyderabad), and how the English East India Company collaborated with indigenous financial capital (Jagat Seths) to conquer Bengal.</li>
              <li><strong>Structure of Colonial Rule:</strong> How the colonial state negotiated between coercion (military, police) and collaboration (zamindars, loyal princes, Westernized babus); the myth of British rule as a modernizing monolith challenged by persistent rural underdevelopment.</li>
              <li><strong>Subaltern &amp; Caste Dimensions of Resistance:</strong> Deep exploration of non-elite mobilization — Dalit assertions (Namashudra movement in Bengal, Satyashodhak Samaj in Maharashtra, Self-Respect in Tamil Nadu), tribal revolts (Santhal, Munda, Rampa), and peasant agrarian leagues (Pabna, Deccan riots).</li>
              <li><strong>Divergent Ideological Currents in Nationalism:</strong> The internal tensions within Indian nationalism: secular territorial nationalism vs. Hindu cultural revivalism; the contested spaces of caste, class, gender, and minority representation during the anti-colonial mass campaigns.</li>
              <li><strong>Partition and After:</strong> Nuanced examination of the communalization process in Bengal and Punjab, the Cabinet Mission breakdown, the human tragedy of refugee displacement, and the monumental task of post-1947 democratic consolidation.</li>
            </ul>
          </div>'''
}

updated_count = 0
for title, new_chapters in ENRICHMENTS.items():
    # Find the book card by title
    pattern = rf'(<h2 class="book-title">{re.escape(title)}</h2>[\s\S]*?)<div class="book-chapters">[\s\S]*?</div>(\s*<div class="book-pdf-box">)'
    m = re.search(pattern, text)
    if m:
        text = re.sub(pattern, rf'\1{new_chapters}\2', text, count=1)
        updated_count += 1
        print(f"Enriched: {title}")
    else:
        print(f"Could not find pattern for: {title}")

print(f"Total books successfully enriched: {updated_count} / {len(ENRICHMENTS)}")

with open('books.html', 'w', encoding='utf-8') as f:
    f.write(text)
