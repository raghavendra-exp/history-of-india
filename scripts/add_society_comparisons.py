import re

with open('society.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '''              <td>Measured primarily by headline GDP growth rate and industrial output indices.</td>
              <td>Measured by Multidimensional Poverty Index (MPI), reduction in stunting/wasting, female workforce participation, and Gini coefficient.</td>
            </tr>
          </tbody>
        </table>
      </div>'''

if target not in html:
    print("ERROR: Target anchor not found in society.html")
    exit(1)

NEW_SOCIETY_COMPARISONS = '''
      <!-- Comparison 3: Caste vs Class System -->
      <h3 style="margin-top:34px;">3. Stratification Systems: Caste (Varna/Jati) vs. Class in Contemporary India</h3>
      <div class="comp-table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th style="width:20%;">Analytical Dimension</th>
              <th style="width:40%;">Caste System (Ascriptive &amp; Ritual Order)</th>
              <th style="width:40%;">Class System (Economic &amp; Open Order)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Basis of Membership</strong></td>
              <td><strong>Ascription (Birth)</strong>: Assigned involuntarily at birth; immutable regardless of individual wealth, education, or personal achievement.</td>
              <td><strong>Achievement</strong>: Based on occupation, education, income, and accumulated economic capital; permeable and subject to upward or downward mobility.</td>
            </tr>
            <tr>
              <td><strong>Purity-Pollution &amp; Hierarchy</strong></td>
              <td>Governed by the religious-ideological hierarchy of ritual purity and pollution (Louis Dumont's <em>Homo Hierarchicus</em>); hereditary taboos governing commensality (inter-dining) and social contact.</td>
              <td>Secular economic differentiation; determined by market relations, ownership of means of production (Marx), or life chances and status honor (Max Weber).</td>
            </tr>
            <tr>
              <td><strong>Marriage Rules</strong></td>
              <td>Strict <strong>Endogamy</strong> (mandate to marry within one's own sub-caste / Jati); inter-caste unions historically resisted through social ostracization or honour killings.</td>
              <td>Normatively open; endogamy is informal rather than institutionalized; inter-class marriages permitted without structural religious prohibition.</td>
            </tr>
            <tr>
              <td><strong>Mechanisms of Mobility</strong></td>
              <td>Group-based cultural emulation through <strong>Sanskritization</strong> (M.N. Srinivas) or political mobilization as a <strong>Dominant Caste</strong>; individual mobility historically impossible.</td>
              <td>Individual merit, educational attainment, skill acquisition, entrepreneurship, and career advancement across generations.</td>
            </tr>
            <tr>
              <td><strong>Modern Transformation in India</strong></td>
              <td>Shift from ritual hierarchy to political interest group ("substantialization of caste" - Rajni Kothari); competitive vote-bank mobilization alongside rising Dalit capitalism.</td>
              <td>Emergence of a massive consumerist middle class; widening wealth inequality (World Inequality Lab: top 1% owning >40% of national wealth).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Comparison 4: Tribal Policy Approaches -->
      <h3 style="margin-top:34px;">4. Tribal Integration Paradigms: Isolationism vs. Assimilation vs. Nehruvian "Tribal Panchsheel"</h3>
      <div class="comp-table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th style="width:20%;">Core Dimension</th>
              <th style="width:26%;">Isolationist Approach<br>(Verrier Elwin / Colonial Era)</th>
              <th style="width:26%;">Assimilationist Approach<br>(G.S. Ghurye / Modernizers)</th>
              <th style="width:28%;">Nehruvian "Tribal Panchsheel"<br>(Democratic Integration)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Guiding Philosophy</strong></td>
              <td>"National Park" approach: Treat tribal communities as pristine indigenous museum societies needing quarantine from corrupting modern civilizational influences.</td>
              <td>"Backward Hindus" thesis: Tribals are imperfectly integrated Hindus whose distinct customs must be rapidly dissolved into mainstream national life.</td>
              <td><strong>Organic Development</strong>: Integrate tribals into the Indian nation-state while preserving their unique cultural autonomy, land rights, and customary institutions.</td>
            </tr>
            <tr>
              <td><strong>State Role &amp; Intervention</strong></td>
              <td>Minimal administrative contact; maintain tribal reserves with restricted outsider entry; preserve status quo.</td>
              <td>Aggressive industrialization, uniform civil laws, standard education, and full-scale market integration into forested hinterlands.</td>
              <td>Build indigenous capacities; train tribal youth for local administration; avoid over-administering tribal lands with alien bureaucratic staff.</td>
            </tr>
            <tr>
              <td><strong>Land &amp; Forest Rights</strong></td>
              <td>Colonial state monopoly over timber and mineral reserves through Forest Acts, disenfranchising tribal customary rights.</td>
              <td>Commercial exploitation of forest reserves for national industrialization (dams, mines, heavy plants), causing involuntary displacement.</td>
              <td>Strict protection of tribal land from alienation to non-tribals; codified in Fifth/Sixth Schedules, PESA 1996, and Forest Rights Act (FRA 2006).</td>
            </tr>
            <tr>
              <td><strong>Socio-Cultural Evaluation</strong></td>
              <td>Romanticized poverty and disease in the name of cultural purity; denied access to modern medicine and literacy.</td>
              <td>Resulted in cultural deracination, debt-bondage to moneylenders, land alienation, and rise of left-wing extremism (Naxalism).</td>
              <td>Celebrates tribal arts, self-governance, and customary law; judges developmental success not by statistics or spent funds, but by the quality of human character fostered.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Comparison 5: Family Structure Transitions -->
      <h3 style="margin-top:34px;">5. Family Dynamics in India: Traditional Joint Family vs. Modified "Functionally Joint" Nuclear Households</h3>
      <div class="comp-table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th style="width:20%;">Structural Feature</th>
              <th style="width:40%;">Traditional Coparcenary Joint Family</th>
              <th style="width:40%;">Modern Modified "Functionally Joint" Household</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Residential Composition</strong></td>
              <td>Multi-generational coresidence under a single roof (grandparents, parents, sons, unmarried daughters, daughters-in-law, grandchildren).</td>
              <td>Residentially nuclear (parents and unmarried children) necessitated by urban migration, housing constraints, and white-collar employment.</td>
            </tr>
            <tr>
              <td><strong>Authority &amp; Decision-Making</strong></td>
              <td>Patriarchal and gerontocratic authority concentrated in the eldest male (<em>Karta</em>); strict filial obedience and subordinate status for younger brides.</td>
              <td>Egalitarian and democratic decision-making; rising female autonomy due to education and independent income; joint spousal negotiations.</td>
            </tr>
            <tr>
              <td><strong>Property &amp; Economic Cooperation</strong></td>
              <td>Common hearth (single kitchen), joint family enterprise, undivided ancestral property (Mitakshara/Dayabhaga legal coparcenary).</td>
              <td>Individualized bank accounts and salary earnings, but regular economic remittances, shared real-estate investments, and mutual funding for family rituals.</td>
            </tr>
            <tr>
              <td><strong>Sociological Reality in India</strong></td>
              <td>Commonly assumed to be the timeless archetype of ancient India, though sociologists (A.M. Shah) prove residential nuclearity always coexisted with joint ideals.</td>
              <td><strong>Instrumental Jointness</strong> (I.P. Desai &amp; A.M. Shah): Indian families have not become isolated Western nuclear islands; they maintain intense emotional, ritual, and emergency kinship support networks across separate urban flats.</td>
            </tr>
          </tbody>
        </table>
      </div>
'''

html_updated = html.replace(target, target + NEW_SOCIETY_COMPARISONS)

with open('society.html', 'w', encoding='utf-8') as f:
    f.write(html_updated)

print("Updated society.html with Comparisons 3, 4, and 5!")
