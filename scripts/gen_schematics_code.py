# Generate the HTML for the Visual Schematics & Mnemonics section
def generate_visual_schematics_html():
    return '''
      <!-- ==========================================
           VISUAL ARCHITECTURAL SCHEMATICS & MNEMONICS
           ========================================== -->
      <div class="visual-schematics-container" style="margin-bottom: 40px;">
        <div style="background: linear-gradient(135deg, rgba(212,175,55,0.08), rgba(184,51,42,0.05)); border: 1px solid var(--gold); border-radius: var(--radius-lg); padding: 24px; margin-bottom: 30px;">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
            <span style="font-size:1.8rem;">📐</span>
            <div>
              <h3 style="margin:0; font-family:var(--font-display); font-size:1.4rem; color:var(--ink);">Master Visual Memory Schematics &amp; Architectural Blueprints</h3>
              <p style="margin:2px 0 0; color:var(--ink-soft); font-size:0.92rem;">Direct visual anatomical cross-sections and flowcharts designed for photographic exam recall in UPSC Prelims &amp; Mains GS-1.</p>
            </div>
          </div>
          <div style="display:flex; flex-wrap:wrap; gap:10px; margin-top:14px;">
            <a href="#schematic-stupa" class="btn btn-outline btn-sm" style="font-size:0.8rem;">☸️ Stupa Anatomy</a>
            <a href="#schematic-temple" class="btn btn-outline btn-sm" style="font-size:0.8rem;">🏛️ Nagara vs. Dravida</a>
            <a href="#schematic-engineering" class="btn btn-outline btn-sm" style="font-size:0.8rem;">🧱 Trabeate vs. Arcuate</a>
            <a href="#schematic-scripts" class="btn btn-outline btn-sm" style="font-size:0.8rem;">📜 Scripts Genealogy Tree</a>
            <a href="#schematic-coinage" class="btn btn-outline btn-sm" style="font-size:0.8rem;">🪙 Ancient Coinage Evolution</a>
          </div>
        </div>

        <!-- SCHEMATIC 1: BUDDHIST STUPA ANATOMY -->
        <div class="schematic-card" id="schematic-stupa" style="background:var(--bg-raised); border:1px solid var(--line); border-radius:var(--radius-lg); padding:24px; margin-bottom:32px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
            <div>
              <span class="badge" style="background:rgba(212,175,55,0.15); color:var(--gold); border:1px solid var(--gold); padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:600;">ANATOMY SCHEMA 01</span>
              <h3 style="margin:6px 0 2px; font-family:var(--font-display); font-size:1.25rem;">Anatomy of a Classical Buddhist Stupa (Cosmic &amp; Funerary Architecture)</h3>
              <p style="margin:0; font-size:0.88rem; color:var(--ink-soft);">Sanchi Stupa No. 1 Prototype • Cosmological Axis Mundi &amp; Circumambulatory Symbolism</p>
            </div>
            <span style="font-size:1.6rem;">☸️</span>
          </div>

          <div style="width:100%; overflow-x:auto; background:var(--bg); border:1px solid var(--line); border-radius:var(--radius); padding:16px; margin-bottom:16px;">
            <svg viewBox="0 0 760 380" style="width:100%; min-width:680px; height:auto; display:block; font-family:var(--font-sans);">
              <defs>
                <linearGradient id="domeGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#e0bb6b" stop-opacity="0.35"/>
                  <stop offset="100%" stop-color="#b8860b" stop-opacity="0.15"/>
                </linearGradient>
                <linearGradient id="baseGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#8c2d19" stop-opacity="0.2"/>
                  <stop offset="100%" stop-color="#8c2d19" stop-opacity="0.4"/>
                </linearGradient>
              </defs>

              <!-- Base Ground Line -->
              <line x1="20" y1="340" x2="740" y2="340" stroke="var(--ink-faint)" stroke-width="2"/>
              <text x="380" y="365" text-anchor="middle" font-size="12" fill="var(--ink-faint)" font-weight="600">Ground Level (Bhumi) / Outer Processional Circumambulation</text>

              <!-- Outer Railing (Vedika) Left & Right -->
              <rect x="70" y="270" width="16" height="70" fill="var(--line)" stroke="var(--ink-soft)" stroke-width="1.5"/>
              <rect x="96" y="270" width="16" height="70" fill="var(--line)" stroke="var(--ink-soft)" stroke-width="1.5"/>
              <rect x="654" y="270" width="16" height="70" fill="var(--line)" stroke="var(--ink-soft)" stroke-width="1.5"/>
              <rect x="680" y="270" width="16" height="70" fill="var(--line)" stroke="var(--ink-soft)" stroke-width="1.5"/>
              <!-- Crossbars (Suchi) -->
              <line x1="60" y1="285" x2="120" y2="285" stroke="var(--ink-soft)" stroke-width="2"/>
              <line x1="60" y1="305" x2="120" y2="305" stroke="var(--ink-soft)" stroke-width="2"/>
              <line x1="60" y1="325" x2="120" y2="325" stroke="var(--ink-soft)" stroke-width="2"/>
              <line x1="645" y1="285" x2="705" y2="285" stroke="var(--ink-soft)" stroke-width="2"/>
              <line x1="645" y1="305" x2="705" y2="305" stroke="var(--ink-soft)" stroke-width="2"/>
              <line x1="645" y1="325" x2="705" y2="325" stroke="var(--ink-soft)" stroke-width="2"/>

              <!-- Torana (Gateway) Left Front Profile -->
              <rect x="40" y="210" width="12" height="130" fill="#b8860b" stroke="var(--ink)" stroke-width="1.5"/>
              <rect x="70" y="210" width="12" height="130" fill="#b8860b" stroke="var(--ink)" stroke-width="1.5"/>
              <rect x="30" y="220" width="62" height="8" rx="2" fill="#d4af37" stroke="var(--ink)" stroke-width="1.5"/>
              <rect x="30" y="235" width="62" height="8" rx="2" fill="#d4af37" stroke="var(--ink)" stroke-width="1.5"/>
              <rect x="30" y="250" width="62" height="8" rx="2" fill="#d4af37" stroke="var(--ink)" stroke-width="1.5"/>
              <!-- Dharma-chakra finial on torana -->
              <circle cx="61" cy="205" r="7" fill="none" stroke="var(--ink)" stroke-width="1.5"/>

              <!-- Medhi (Circular Elevated Drum Base) -->
              <rect x="140" y="260" width="480" height="80" rx="4" fill="url(#baseGrad)" stroke="var(--ink)" stroke-width="2"/>
              <!-- Upper Railing on Medhi -->
              <line x1="150" y1="250" x2="610" y2="250" stroke="var(--ink-soft)" stroke-width="2" stroke-dasharray="6,4"/>

              <!-- Anda (Hemispherical Dome) -->
              <path d="M 180,260 A 200,160 0 0,1 580,260 Z" fill="url(#domeGrad)" stroke="var(--ink)" stroke-width="2.5"/>

              <!-- Harmika (Square Balcony Box) -->
              <rect x="345" y="85" width="70" height="25" fill="#f4ecd8" stroke="var(--ink)" stroke-width="2"/>
              <line x1="345" y1="92" x2="415" y2="92" stroke="var(--ink-soft)" stroke-width="1"/>
              <line x1="345" y1="100" x2="415" y2="100" stroke="var(--ink-soft)" stroke-width="1"/>
              <!-- Small vertical railing bars on Harmika -->
              <line x1="357" y1="85" x2="357" y2="110" stroke="var(--ink-soft)" stroke-width="1"/>
              <line x1="370" y1="85" x2="370" y2="110" stroke="var(--ink-soft)" stroke-width="1"/>
              <line x1="390" y1="85" x2="390" y2="110" stroke="var(--ink-soft)" stroke-width="1"/>
              <line x1="403" y1="85" x2="403" y2="110" stroke="var(--ink-soft)" stroke-width="1"/>

              <!-- Yashti (Central Mast / Axis Mundi) -->
              <line x1="380" y1="25" x2="380" y2="85" stroke="var(--ink)" stroke-width="3"/>

              <!-- Chhatravali (Three Triple Parasols) -->
              <path d="M 350,65 Q 380,55 410,65 Z" fill="#b8332a" stroke="var(--ink)" stroke-width="1.5"/>
              <path d="M 356,48 Q 380,40 404,48 Z" fill="#b8332a" stroke="var(--ink)" stroke-width="1.5"/>
              <path d="M 364,32 Q 380,26 396,32 Z" fill="#b8332a" stroke="var(--ink)" stroke-width="1.5"/>

              <!-- ================= ANNOTATIONS & LEADER LINES ================= -->
              <!-- Chhatra -->
              <line x1="412" y1="48" x2="520" y2="35" stroke="#b8332a" stroke-width="1.5"/>
              <circle cx="520" cy="35" r="3" fill="#b8332a"/>
              <text x="530" y="32" font-size="12" font-weight="700" fill="#b8332a">CHHATRAVALI (3 Parasols)</text>
              <text x="530" y="47" font-size="10.5" fill="var(--ink-soft)">Triratna: Buddha, Dharma, Sangha</text>

              <!-- Yashti -->
              <line x1="380" y1="25" x2="380" y2="12" stroke="var(--ink)" stroke-width="1"/>
              <line x1="380" y1="12" x2="270" y2="12" stroke="var(--ink)" stroke-width="1.5"/>
              <circle cx="270" cy="12" r="3" fill="var(--ink)"/>
              <text x="260" y="15" text-anchor="end" font-size="12" font-weight="700" fill="var(--ink)">YASHTI (Axis Mundi)</text>
              <text x="260" y="28" text-anchor="end" font-size="10.5" fill="var(--ink-soft)">Cosmic pillar connecting earth to heavens</text>

              <!-- Harmika -->
              <line x1="416" y1="97" x2="550" y2="97" stroke="var(--ink)" stroke-width="1.5"/>
              <circle cx="550" cy="97" r="3" fill="var(--ink)"/>
              <text x="560" y="94" font-size="12" font-weight="700" fill="var(--ink)">HARMIKA (Square Balcony)</text>
              <text x="560" y="108" font-size="10.5" fill="var(--ink-soft)">Abode of the Gods (Heavenly realm atop dome)</text>

              <!-- Anda -->
              <line x1="480" y1="190" x2="580" y2="175" stroke="#b8860b" stroke-width="1.5"/>
              <circle cx="580" cy="175" r="3" fill="#b8860b"/>
              <text x="590" y="172" font-size="13" font-weight="700" fill="#b8860b">ANDA (Hemispherical Mound)</text>
              <text x="590" y="186" font-size="10.5" fill="var(--ink-soft)">Cosmic egg / Universe containing relics (Dhatu)</text>

              <!-- Medhi -->
              <line x1="560" y1="290" x2="630" y2="250" stroke="#8c2d19" stroke-width="1.5"/>
              <circle cx="630" cy="250" r="3" fill="#8c2d19"/>
              <text x="640" y="247" font-size="12" font-weight="700" fill="#8c2d19">MEDHI (Circular Drum Base)</text>
              <text x="640" y="261" font-size="10.5" fill="var(--ink-soft)">Upper Pradakshina Path reached by stairs (Sopana)</text>

              <!-- Torana -->
              <line x1="60" y1="215" x2="60" y2="140" stroke="#b8860b" stroke-width="1.5"/>
              <circle cx="60" cy="140" r="3" fill="#b8860b"/>
              <text x="60" y="125" font-size="12" font-weight="700" fill="#b8860b">TORANA (Carved Gateway)</text>
              <text x="60" y="138" font-size="10.5" fill="var(--ink-soft)">4 Cardinal Gates with Jatakas &amp; Salabhanjikas</text>

              <!-- Vedika -->
              <line x1="105" y1="300" x2="160" y2="330" stroke="var(--ink-soft)" stroke-width="1.5"/>
              <circle cx="160" cy="330" r="3" fill="var(--ink-soft)"/>
              <text x="170" y="328" font-size="11.5" font-weight="700" fill="var(--ink)">VEDIKA (Ground Stone Railing)</text>
              <text x="170" y="340" font-size="10" fill="var(--ink-soft)">Separates sacred enclosure from mundane world</text>
            </svg>
          </div>

          <!-- Mnemonic Box -->
          <div style="background:var(--bg); border-left:4px solid var(--gold); padding:12px 16px; border-radius:0 var(--radius) var(--radius) 0; font-size:0.88rem;">
            <strong>🎯 Memory Formula for Stupa Elements (Top to Bottom):</strong>
            <span style="display:inline-block; margin-left:8px; font-family:var(--font-mono); font-weight:700; color:var(--crimson);">C - Y - H - A - M - V - T</span>
            <div style="margin-top:4px; color:var(--ink-soft); line-height:1.5;">
              <strong>C</strong>hhatra (Parasols / Triratna) → <strong>Y</strong>ashti (Central Axis) → <strong>H</strong>armika (Sacred Balcony) → <strong>A</strong>nda (Dome / Cosmic Egg) → <strong>M</strong>edhi (Upper Terrace) → <strong>V</strong>edika (Stone Railing) → <strong>T</strong>orana (Carved Gateways). Circumambulation is always <em>clockwise</em> (Pradakshina).
            </div>
          </div>
        </div>

        <!-- SCHEMATIC 2: TEMPLE ARCHITECTURE - NAGARA VS DRAVIDA -->
        <div class="schematic-card" id="schematic-temple" style="background:var(--bg-raised); border:1px solid var(--line); border-radius:var(--radius-lg); padding:24px; margin-bottom:32px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
            <div>
              <span class="badge" style="background:rgba(184,51,42,0.15); color:var(--crimson); border:1px solid var(--crimson); padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:600;">ANATOMY SCHEMA 02</span>
              <h3 style="margin:6px 0 2px; font-family:var(--font-display); font-size:1.25rem;">Nagara vs. Dravida Temple Elevation &amp; Ground Structural Schematics</h3>
              <p style="margin:0; font-size:0.88rem; color:var(--ink-soft);">Curvilinear Shikhara (North) vs. Stepped-Pyramidal Vimana &amp; Towering Gopuram (South)</p>
            </div>
            <span style="font-size:1.6rem;">🏛️</span>
          </div>

          <div style="width:100%; overflow-x:auto; background:var(--bg); border:1px solid var(--line); border-radius:var(--radius); padding:16px; margin-bottom:16px;">
            <svg viewBox="0 0 760 410" style="width:100%; min-width:700px; height:auto; display:block; font-family:var(--font-sans);">
              <!-- Center Separator -->
              <line x1="380" y1="20" x2="380" y2="390" stroke="var(--line)" stroke-width="2" stroke-dasharray="6,4"/>

              <!-- LEFT: NAGARA STYLE -->
              <g id="nagara-diagram">
                <text x="180" y="30" text-anchor="middle" font-size="14" font-weight="700" fill="#b8860b">NAGARA STYLE (North India)</text>
                <text x="180" y="46" text-anchor="middle" font-size="10.5" fill="var(--ink-soft)">Khajuraho, Odisha, Modhera</text>

                <!-- Ground Level -->
                <line x1="20" y1="360" x2="360" y2="360" stroke="var(--ink-faint)" stroke-width="2"/>

                <!-- Jagati (Elevated Plinth) -->
                <rect x="40" y="335" width="310" height="25" fill="#e8dfce" stroke="var(--ink)" stroke-width="1.5"/>
                <text x="195" y="352" text-anchor="middle" font-size="10" font-weight="600" fill="var(--ink-soft)">JAGATI (Elevated Stone Plinth)</text>

                <!-- Ardhamandapa (Entrance Porch) -->
                <rect x="50" y="280" width="45" height="55" fill="#f4ecd8" stroke="var(--ink)" stroke-width="1.5"/>
                <polygon points="45,280 72,250 100,280" fill="#d4af37" opacity="0.6" stroke="var(--ink)" stroke-width="1.5"/>

                <!-- Mandapa (Pillared Assembly Hall) -->
                <rect x="105" y="260" width="70" height="75" fill="#f4ecd8" stroke="var(--ink)" stroke-width="1.5"/>
                <!-- Tiered Phamsana roof on Mandapa -->
                <polygon points="100,260 140,205 180,260" fill="#d4af37" opacity="0.6" stroke="var(--ink)" stroke-width="1.5"/>
                <polygon points="112,235 140,205 168,235" fill="#b8860b" opacity="0.4" stroke="var(--ink)" stroke-width="1"/>

                <!-- Antarala (Vestibule) -->
                <rect x="180" y="250" width="30" height="85" fill="#ebdcb9" stroke="var(--ink)" stroke-width="1.5"/>

                <!-- Garbhagriha Base -->
                <rect x="215" y="240" width="105" height="95" fill="#d8c49d" stroke="var(--ink)" stroke-width="1.5"/>
                <!-- Sanctum Deity indicator -->
                <circle cx="267" cy="300" r="8" fill="#b8332a"/>
                <text x="267" y="322" text-anchor="middle" font-size="9" font-weight="700" fill="var(--ink)">GARBHAGRIHA</text>

                <!-- Curvilinear Shikhara (Latina / Rekha-Prasada) -->
                <path d="M 215,240 Q 235,140 260,85 L 275,85 Q 300,140 320,240 Z" fill="#e0bb6b" stroke="var(--ink)" stroke-width="2"/>
                <!-- Horizontal bhumi rathas -->
                <line x1="225" y1="200" x2="310" y2="200" stroke="var(--ink-soft)" stroke-width="1"/>
                <line x1="236" y1="165" x2="299" y2="165" stroke="var(--ink-soft)" stroke-width="1"/>
                <line x1="248" y1="125" x2="287" y2="125" stroke="var(--ink-soft)" stroke-width="1"/>

                <!-- Amalaka (Ribbed Stone Disc) -->
                <ellipse cx="267" cy="80" rx="18" ry="6" fill="#b8860b" stroke="var(--ink)" stroke-width="1.5"/>
                <!-- Kalasha (Pot finial) -->
                <path d="M 264,74 Q 260,68 267,62 Q 274,68 270,74 Z" fill="#d4af37" stroke="var(--ink)" stroke-width="1.5"/>
                <!-- Flag (Dhvaja) -->
                <line x1="267" y1="62" x2="267" y2="50" stroke="var(--ink)" stroke-width="1.5"/>
                <polygon points="267,50 280,55 267,60" fill="#b8332a"/>

                <!-- Annotations -->
                <text x="330" y="130" font-size="11" font-weight="700" fill="#b8860b">SHIKHARA</text>
                <text x="330" y="143" font-size="9" fill="var(--ink-soft)">Curvilinear beehive</text>
                <text x="330" y="80" font-size="11" font-weight="700" fill="var(--ink)">AMALAKA &amp; KALASHA</text>
                <text x="140" y="195" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--ink)">MANDAPA</text>
                <text x="65" y="240" font-size="9.5" fill="var(--ink-soft)">Ardhamandapa</text>
                <text x="195" y="240" text-anchor="middle" font-size="9" fill="var(--ink-soft)">Antarala</text>
              </g>

              <!-- RIGHT: DRAVIDA STYLE -->
              <g id="dravida-diagram">
                <text x="570" y="30" text-anchor="middle" font-size="14" font-weight="700" fill="#b8332a">DRAVIDA STYLE (South India)</text>
                <text x="570" y="46" text-anchor="middle" font-size="10.5" fill="var(--ink-soft)">Brihadisvara, Shore Temple, Meenakshi</text>

                <!-- Ground Level -->
                <line x1="400" y1="360" x2="740" y2="360" stroke="var(--ink-faint)" stroke-width="2"/>

                <!-- Outer Enclosure Wall (Prakara) -->
                <rect x="410" y="280" width="14" height="80" fill="#8c2d19" stroke="var(--ink)" stroke-width="1.5"/>
                <rect x="720" y="280" width="14" height="80" fill="#8c2d19" stroke="var(--ink)" stroke-width="1.5"/>
                <text x="417" y="270" text-anchor="middle" font-size="9.5" font-weight="700" fill="#8c2d19">PRAKARA</text>

                <!-- Temple Water Tank (Kalyani / Pushkarini) inside Prakara -->
                <rect x="435" y="340" width="55" height="18" fill="#4682b4" opacity="0.6" stroke="var(--ink)" stroke-width="1.5"/>
                <text x="462" y="353" text-anchor="middle" font-size="8.5" font-weight="700" fill="#fff">KALYANI</text>

                <!-- Pillared Mandapa -->
                <rect x="500" y="295" width="60" height="65" fill="#f4ecd8" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="515" y1="295" x2="515" y2="360" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="530" y1="295" x2="530" y2="360" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="545" y1="295" x2="545" y2="360" stroke="var(--ink)" stroke-width="1.5"/>
                <text x="530" y="285" text-anchor="middle" font-size="10" font-weight="700" fill="var(--ink)">MANDAPA</text>

                <!-- Garbhagriha Sanctum Base -->
                <rect x="570" y="270" width="100" height="90" fill="#d8c49d" stroke="var(--ink)" stroke-width="1.5"/>
                <circle cx="620" cy="320" r="8" fill="#b8332a"/>
                <text x="620" y="342" text-anchor="middle" font-size="9" font-weight="700" fill="var(--ink)">GARBHAGRIHA</text>

                <!-- Stepped Pyramidal VIMANA (Talas) -->
                <!-- Storey 1 -->
                <rect x="575" y="235" width="90" height="35" fill="#dfa467" stroke="var(--ink)" stroke-width="1.5"/>
                <!-- Storey 2 -->
                <rect x="585" y="200" width="70" height="35" fill="#dfa467" stroke="var(--ink)" stroke-width="1.5"/>
                <!-- Storey 3 -->
                <rect x="595" y="165" width="50" height="35" fill="#dfa467" stroke="var(--ink)" stroke-width="1.5"/>
                <!-- Storey 4 -->
                <rect x="605" y="130" width="30" height="35" fill="#dfa467" stroke="var(--ink)" stroke-width="1.5"/>

                <!-- Crowning Shikhara / Stupika (Dome shaped) -->
                <ellipse cx="620" cy="115" rx="16" ry="14" fill="#b8332a" stroke="var(--ink)" stroke-width="1.5"/>
                <circle cx="620" cy="98" r="4" fill="#d4af37" stroke="var(--ink)" stroke-width="1.5"/>

                <!-- Towering Gopuram at Entrance (Far Right) -->
                <polygon points="695,360 705,170 735,170 745,360" fill="#c26352" stroke="var(--ink)" stroke-width="1.5"/>
                <rect x="710" y="325" width="20" height="35" fill="#f4ecd8" stroke="var(--ink)" stroke-width="1.5"/>
                <path d="M 700,170 Q 720,155 740,170 Z" fill="#b8860b" stroke="var(--ink)" stroke-width="1.5"/>
                <text x="720" y="145" text-anchor="middle" font-size="10.5" font-weight="700" fill="#b8332a">GOPURAM</text>
                <text x="720" y="157" text-anchor="middle" font-size="8.5" fill="var(--ink-soft)">Monumental Gate</text>

                <!-- Annotations -->
                <text x="560" y="180" text-anchor="end" font-size="11" font-weight="700" fill="#b8332a">VIMANA</text>
                <text x="560" y="193" text-anchor="end" font-size="9" fill="var(--ink-soft)">Stepped pyramid (Talas)</text>
                <text x="590" y="112" text-anchor="end" font-size="10.5" font-weight="700" fill="var(--ink)">STUPIKA</text>
              </g>
            </svg>
          </div>

          <!-- Comparative Key Takeaways -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:12px; font-size:0.86rem; color:var(--ink-soft); line-height:1.45;">
            <div style="background:var(--bg); padding:10px 14px; border-radius:var(--radius); border-left:3px solid #b8860b;">
              <strong style="color:var(--ink);">Nagara Rule of Thumb:</strong> Tower is called <em>Shikhara</em> (curvilinear beehive). The highest shikhara sits directly over the <em>Garbhagriha</em>. Plinth (<em>Jagati</em>) is elevated. Boundary walls and inner water tanks are <em>absent</em>.
            </div>
            <div style="background:var(--bg); padding:10px 14px; border-radius:var(--radius); border-left:3px solid #b8332a;">
              <strong style="color:var(--ink);">Dravida Rule of Thumb:</strong> Tower over sanctum is called <em>Vimana</em> (stepped pyramid). Entrance gate is the massive <em>Gopuram</em> (often dwarfing the vimana in later Vijayanagara/Nayaka eras). Surrounded by <em>Prakara</em> walls and sacred <em>Kalyani</em> tank.
            </div>
          </div>
        </div>

        <!-- SCHEMATIC 3: STRUCTURAL ENGINEERING (TRABEATE VS ARCUATE) -->
        <div class="schematic-card" id="schematic-engineering" style="background:var(--bg-raised); border:1px solid var(--line); border-radius:var(--radius-lg); padding:24px; margin-bottom:32px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
            <div>
              <span class="badge" style="background:rgba(46,117,89,0.15); color:#2e7559; border:1px solid #2e7559; padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:600;">ENGINEERING SCHEMA 03</span>
              <h3 style="margin:6px 0 2px; font-family:var(--font-display); font-size:1.25rem;">Structural Engineering Transition: Trabeate vs. Arcuate Systems</h3>
              <p style="margin:0; font-size:0.88rem; color:var(--ink-soft);">Indigenous Post-and-Lintel &amp; Corbelled Slabs vs. True Arch, Keystone, Squinch &amp; True Dome</p>
            </div>
            <span style="font-size:1.6rem;">🧱</span>
          </div>

          <div style="width:100%; overflow-x:auto; background:var(--bg); border:1px solid var(--line); border-radius:var(--radius); padding:16px; margin-bottom:16px;">
            <svg viewBox="0 0 740 320" style="width:100%; min-width:680px; height:auto; display:block; font-family:var(--font-sans);">
              <!-- Center Line -->
              <line x1="370" y1="20" x2="370" y2="300" stroke="var(--line)" stroke-width="2" stroke-dasharray="6,4"/>

              <!-- LEFT: TRABEATE SYSTEM -->
              <g id="trabeate-system">
                <text x="185" y="30" text-anchor="middle" font-size="13.5" font-weight="700" fill="#8c2d19">TRABEATE SYSTEM (Ancient / Hindu)</text>
                <text x="185" y="46" text-anchor="middle" font-size="10.5" fill="var(--ink-soft)">Post &amp; Lintel / Corbelled Courses</text>

                <!-- Ground -->
                <line x1="40" y1="270" x2="330" y2="270" stroke="var(--ink-faint)" stroke-width="2"/>

                <!-- Two Vertical Pillars (Posts) -->
                <rect x="80" y="140" width="28" height="130" fill="#d8c49d" stroke="var(--ink)" stroke-width="1.5"/>
                <rect x="230" y="140" width="28" height="130" fill="#d8c49d" stroke="var(--ink)" stroke-width="1.5"/>

                <!-- Corbelled Brackets (Sirsha) -->
                <polygon points="70,140 118,140 108,125 80,125" fill="#b8860b" stroke="var(--ink)" stroke-width="1.5"/>
                <polygon points="220,140 268,140 258,125 230,125" fill="#b8860b" stroke="var(--ink)" stroke-width="1.5"/>

                <!-- Horizontal Beam (Lintel / Beam) -->
                <rect x="55" y="105" width="230" height="20" fill="#c2a677" stroke="var(--ink)" stroke-width="2"/>
                <text x="170" y="120" text-anchor="middle" font-size="10" font-weight="700" fill="var(--ink)">HORIZONTAL LINTEL / BEAM</text>

                <!-- Corbelled Roof Courses above Lintel -->
                <rect x="75" y="90" width="190" height="15" fill="#d8c49d" stroke="var(--ink)" stroke-width="1.5"/>
                <rect x="95" y="75" width="150" height="15" fill="#d8c49d" stroke="var(--ink)" stroke-width="1.5"/>
                <rect x="115" y="60" width="110" height="15" fill="#d8c49d" stroke="var(--ink)" stroke-width="1.5"/>
                <polygon points="115,60 170,35 225,60" fill="#b8860b" stroke="var(--ink)" stroke-width="1.5"/>

                <!-- Downward Gravity Force Arrows -->
                <line x1="170" y1="130" x2="170" y2="175" stroke="#b8332a" stroke-width="2" marker-end="url(#arrow)"/>
                <text x="170" y="195" text-anchor="middle" font-size="9" font-weight="700" fill="#b8332a">Direct Tensile Strain</text>
                <text x="170" y="208" text-anchor="middle" font-size="8.5" fill="var(--ink-soft)">(Stone cracks under wide span)</text>

                <text x="94" y="220" text-anchor="middle" font-size="9.5" font-weight="600" fill="var(--ink)">Vertical Pillar</text>
                <text x="244" y="220" text-anchor="middle" font-size="9.5" font-weight="600" fill="var(--ink)">Vertical Pillar</text>
              </g>

              <!-- RIGHT: ARCUATE SYSTEM -->
              <g id="arcuate-system">
                <text x="555" y="30" text-anchor="middle" font-size="13.5" font-weight="700" fill="#2e7559">ARCUATE SYSTEM (Indo-Islamic / Sultanate)</text>
                <text x="555" y="46" text-anchor="middle" font-size="10.5" fill="var(--ink-soft)">True Arch (Keystone) &amp; True Dome (Squinch)</text>

                <!-- Ground -->
                <line x1="410" y1="270" x2="700" y2="270" stroke="var(--ink-faint)" stroke-width="2"/>

                <!-- Piers / Jambs -->
                <rect x="440" y="150" width="35" height="120" fill="#b2c9b8" stroke="var(--ink)" stroke-width="1.5"/>
                <rect x="635" y="150" width="35" height="120" fill="#b2c9b8" stroke="var(--ink)" stroke-width="1.5"/>

                <!-- Impost Blocks -->
                <rect x="435" y="142" width="45" height="8" fill="#2e7559" stroke="var(--ink)" stroke-width="1.5"/>
                <rect x="630" y="142" width="45" height="8" fill="#2e7559" stroke="var(--ink)" stroke-width="1.5"/>

                <!-- True Arch Radial Voussoirs -->
                <!-- Semicircular true arch with radiating stones -->
                <path d="M 458,142 A 97,97 0 0,1 652,142 L 635,142 A 80,80 0 0,0 475,142 Z" fill="#d9e6dc" stroke="var(--ink)" stroke-width="1.5"/>
                <!-- Central KEYSTONE -->
                <polygon points="545,45 565,45 560,62 550,62" fill="#b8332a" stroke="var(--ink)" stroke-width="2"/>
                <text x="555" y="40" text-anchor="middle" font-size="10.5" font-weight="800" fill="#b8332a">KEYSTONE</text>

                <!-- Radiating Radial Lines representing Voussoirs -->
                <line x1="475" y1="110" x2="455" y2="105" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="495" y1="80" x2="480" y2="70" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="525" y1="65" x2="515" y2="50" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="585" y1="65" x2="595" y2="50" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="615" y1="80" x2="630" y2="70" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="635" y1="110" x2="655" y2="105" stroke="var(--ink)" stroke-width="1.5"/>

                <!-- Thrust Force Arrows spreading laterally -->
                <path d="M 540,65 Q 500,85 465,150" fill="none" stroke="#2e7559" stroke-width="2" stroke-dasharray="4,3"/>
                <path d="M 570,65 Q 610,85 645,150" fill="none" stroke="#2e7559" stroke-width="2" stroke-dasharray="4,3"/>
                <text x="555" y="115" text-anchor="middle" font-size="9" font-weight="700" fill="#2e7559">Compressive Lateral Thrust</text>
                <text x="555" y="128" text-anchor="middle" font-size="8.5" fill="var(--ink-soft)">Transferred to massive abutment piers</text>

                <!-- Spandrel Label -->
                <text x="475" y="85" font-size="8.5" font-weight="600" fill="var(--ink-faint)">Spandrel</text>
                <text x="610" y="85" font-size="8.5" font-weight="600" fill="var(--ink-faint)">Spandrel</text>

                <!-- Squinch System Note -->
                <rect x="480" y="200" width="150" height="55" rx="4" fill="var(--bg-raised)" stroke="#2e7559" stroke-width="1"/>
                <text x="555" y="218" text-anchor="middle" font-size="9.5" font-weight="700" fill="#2e7559">Squinch Arch System</text>
                <text x="555" y="232" text-anchor="middle" font-size="8" fill="var(--ink-soft)">Diagonal arches across square corners</text>
                <text x="555" y="244" text-anchor="middle" font-size="8" fill="var(--ink-soft)">Converts square room → octagonal dome base</text>
              </g>
            </svg>
          </div>

          <div style="background:var(--bg); border-left:4px solid #2e7559; padding:12px 16px; border-radius:0 var(--radius) var(--radius) 0; font-size:0.88rem;">
            <strong>⚖️ Core Engineering Contrast:</strong>
            <span style="color:var(--ink-soft); line-height:1.5; display:block; margin-top:4px;">
              Ancient Indian builders mastered <strong>Trabeate (beam-and-bracket)</strong> geometry, requiring dense clusters of interior pillars to support massive stone slabs. The Turkish Sultanate introduced the <strong>Arcuate system</strong> (true arch with keystone + mortar + squinch), enabling enormous column-free prayer halls and soaring hemispherical domes (e.g. Alai Darwaza 1311, Gol Gumbaz, Taj Mahal).
            </span>
          </div>
        </div>

        <!-- SCHEMATIC 4: GENEALOGY TREE OF INDIAN SCRIPTS -->
        <div class="schematic-card" id="schematic-scripts" style="background:var(--bg-raised); border:1px solid var(--line); border-radius:var(--radius-lg); padding:24px; margin-bottom:32px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
            <div>
              <span class="badge" style="background:rgba(212,175,55,0.15); color:var(--gold); border:1px solid var(--gold); padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:600;">PALAEOGRAPHY SCHEMA 04</span>
              <h3 style="margin:6px 0 2px; font-family:var(--font-display); font-size:1.25rem;">Genealogical Tree &amp; Evolution of Indian Scripts from Brahmi</h3>
              <p style="margin:0; font-size:0.88rem; color:var(--ink-soft);">Ashokan Brahmi Root • Northern vs. Southern Lineages • Trans-Oceanic Southeast Asian Scripts</p>
            </div>
            <span style="font-size:1.6rem;">📜</span>
          </div>

          <div style="width:100%; overflow-x:auto; background:var(--bg); border:1px solid var(--line); border-radius:var(--radius); padding:16px; margin-bottom:16px;">
            <svg viewBox="0 0 760 360" style="width:100%; min-width:700px; height:auto; display:block; font-family:var(--font-sans);">
              <!-- Root Box: Ashokan Brahmi -->
              <rect x="290" y="15" width="180" height="40" rx="6" fill="#d4af37" stroke="var(--ink)" stroke-width="2"/>
              <text x="380" y="35" text-anchor="middle" font-size="12.5" font-weight="800" fill="#000">BRAHMI SCRIPT</text>
              <text x="380" y="48" text-anchor="middle" font-size="9" font-weight="600" fill="#333">c. 3rd Century BCE (Ashokan)</text>

              <!-- Main Divergence Lines -->
              <line x1="380" y1="55" x2="380" y2="75" stroke="var(--ink)" stroke-width="2"/>
              <line x1="170" y1="75" x2="590" y2="75" stroke="var(--ink)" stroke-width="2"/>
              <line x1="170" y1="75" x2="170" y2="100" stroke="var(--ink)" stroke-width="2"/>
              <line x1="590" y1="75" x2="590" y2="100" stroke="var(--ink)" stroke-width="2"/>

              <!-- BRANCH 1: NORTHERN BRAHMI -->
              <g id="tree-northern">
                <rect x="85" y="100" width="170" height="32" rx="4" fill="#f4ecd8" stroke="#b8860b" stroke-width="2"/>
                <text x="170" y="118" text-anchor="middle" font-size="11" font-weight="700" fill="#b8860b">NORTHERN LINEAGE</text>
                <text x="170" y="128" text-anchor="middle" font-size="8.5" fill="var(--ink-soft)">Gupta Brahmi (4th–5th c. CE)</text>

                <line x1="170" y1="132" x2="170" y2="155" stroke="#b8860b" stroke-width="1.5"/>

                <!-- Siddhamatrika / Kutila -->
                <rect x="90" y="155" width="160" height="30" rx="4" fill="#ebdcb9" stroke="var(--ink)" stroke-width="1.5"/>
                <text x="170" y="172" text-anchor="middle" font-size="10" font-weight="700" fill="var(--ink)">Siddhamatrika / Kutila</text>
                <text x="170" y="181" text-anchor="middle" font-size="8" fill="var(--ink-soft)">6th–8th Century CE</text>

                <!-- Sub-branches from Siddhamatrika -->
                <line x1="170" y1="185" x2="170" y2="205" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="55" y1="205" x2="285" y2="205" stroke="var(--ink)" stroke-width="1.5"/>

                <line x1="55" y1="205" x2="55" y2="225" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="130" y1="205" x2="130" y2="225" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="210" y1="205" x2="210" y2="225" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="285" y1="205" x2="285" y2="225" stroke="var(--ink)" stroke-width="1.5"/>

                <!-- Devanagari -->
                <rect x="15" y="225" width="80" height="55" rx="3" fill="var(--bg-raised)" stroke="#b8860b" stroke-width="1.5"/>
                <text x="55" y="242" text-anchor="middle" font-size="10" font-weight="700" fill="#b8860b">Devanagari</text>
                <text x="55" y="254" text-anchor="middle" font-size="7.5" fill="var(--ink-soft)">Nagari (10th c.)</text>
                <text x="55" y="266" text-anchor="middle" font-size="7" fill="var(--ink)">Hindi, Sanskrit,</text>
                <text x="55" y="275" text-anchor="middle" font-size="7" fill="var(--ink)">Marathi, Nepali</text>

                <!-- Sharada -->
                <rect x="100" y="225" width="60" height="55" rx="3" fill="var(--bg-raised)" stroke="var(--line)" stroke-width="1.5"/>
                <text x="130" y="242" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--ink)">Sharada</text>
                <text x="130" y="254" text-anchor="middle" font-size="7.5" fill="var(--ink-soft)">9th c. CE</text>
                <text x="130" y="266" text-anchor="middle" font-size="7" fill="var(--ink)">Kashmiri,</text>
                <text x="130" y="275" text-anchor="middle" font-size="7" fill="var(--ink)">Gurmukhi (via Landa)</text>

                <!-- Eastern: Gaudi / Bengali-Assamese -->
                <rect x="165" y="225" width="85" height="55" rx="3" fill="var(--bg-raised)" stroke="var(--line)" stroke-width="1.5"/>
                <text x="207" y="242" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--ink)">Proto-Bengali</text>
                <text x="207" y="254" text-anchor="middle" font-size="7.5" fill="var(--ink-soft)">Gaudi (11th c.)</text>
                <text x="207" y="266" text-anchor="middle" font-size="7" fill="var(--ink)">Bengali,</text>
                <text x="207" y="275" text-anchor="middle" font-size="7" fill="var(--ink)">Assamese, Tirhuta</text>

                <!-- Odia -->
                <rect x="255" y="225" width="60" height="55" rx="3" fill="var(--bg-raised)" stroke="var(--line)" stroke-width="1.5"/>
                <text x="285" y="242" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--ink)">Odia</text>
                <text x="285" y="254" text-anchor="middle" font-size="7.5" fill="var(--ink-soft)">Kalinga root</text>
                <text x="285" y="266" text-anchor="middle" font-size="7" fill="var(--ink)">Rounded loops</text>
                <text x="285" y="275" text-anchor="middle" font-size="7" fill="var(--ink)">for palm-leaf</text>
              </g>

              <!-- BRANCH 2: SOUTHERN BRAHMI -->
              <g id="tree-southern">
                <rect x="505" y="100" width="170" height="32" rx="4" fill="#fbebe8" stroke="#b8332a" stroke-width="2"/>
                <text x="590" y="118" text-anchor="middle" font-size="11" font-weight="700" fill="#b8332a">SOUTHERN LINEAGE</text>
                <text x="590" y="128" text-anchor="middle" font-size="8.5" fill="var(--ink-soft)">Bhattiprolu &amp; Early Kadamba</text>

                <line x1="590" y1="132" x2="590" y2="155" stroke="#b8332a" stroke-width="1.5"/>

                <!-- Kadamba / Grantha Hub -->
                <rect x="500" y="155" width="180" height="30" rx="4" fill="#f4dcd9" stroke="var(--ink)" stroke-width="1.5"/>
                <text x="590" y="172" text-anchor="middle" font-size="10" font-weight="700" fill="var(--ink)">Kadamba &amp; Pallava Grantha</text>
                <text x="590" y="181" text-anchor="middle" font-size="8" fill="var(--ink-soft)">4th–6th Century CE</text>

                <!-- Sub-branches from Southern -->
                <line x1="590" y1="185" x2="590" y2="205" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="430" y1="205" x2="710" y2="205" stroke="var(--ink)" stroke-width="1.5"/>

                <line x1="430" y1="205" x2="430" y2="225" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="530" y1="205" x2="530" y2="225" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="620" y1="205" x2="620" y2="225" stroke="var(--ink)" stroke-width="1.5"/>
                <line x1="710" y1="205" x2="710" y2="225" stroke="var(--ink)" stroke-width="1.5"/>

                <!-- Telugu-Kannada -->
                <rect x="385" y="225" width="90" height="55" rx="3" fill="var(--bg-raised)" stroke="#b8332a" stroke-width="1.5"/>
                <text x="430" y="242" text-anchor="middle" font-size="9" font-weight="700" fill="#b8332a">Telugu-Kannada</text>
                <text x="430" y="254" text-anchor="middle" font-size="7.5" fill="var(--ink-soft)">Halegannada</text>
                <text x="430" y="266" text-anchor="middle" font-size="7" fill="var(--ink)">Common till 13th c.</text>
                <text x="430" y="275" text-anchor="middle" font-size="7" fill="var(--ink)">Split into modern</text>

                <!-- Tamil-Brahmi & Vatteluttu -->
                <rect x="485" y="225" width="85" height="55" rx="3" fill="var(--bg-raised)" stroke="var(--line)" stroke-width="1.5"/>
                <text x="527" y="242" text-anchor="middle" font-size="9" font-weight="700" fill="var(--ink)">Tamil-Brahmi</text>
                <text x="527" y="254" text-anchor="middle" font-size="7.5" fill="var(--ink-soft)">Vatteluttu</text>
                <text x="527" y="266" text-anchor="middle" font-size="7" fill="var(--ink)">Sangam era →</text>
                <text x="527" y="275" text-anchor="middle" font-size="7" fill="var(--ink)">Modern Tamil</text>

                <!-- Grantha -> Malayalam -->
                <rect x="580" y="225" width="80" height="55" rx="3" fill="var(--bg-raised)" stroke="var(--line)" stroke-width="1.5"/>
                <text x="620" y="242" text-anchor="middle" font-size="9" font-weight="700" fill="var(--ink)">Grantha Script</text>
                <text x="620" y="254" text-anchor="middle" font-size="7.5" fill="var(--ink-soft)">For Sanskrit texts</text>
                <text x="620" y="266" text-anchor="middle" font-size="7" fill="var(--ink)">Mother of</text>
                <text x="620" y="275" text-anchor="middle" font-size="7" fill="var(--ink)">Malayalam script</text>

                <!-- Southeast Asian Scripts -->
                <rect x="670" y="225" width="80" height="55" rx="3" fill="var(--bg-raised)" stroke="#2e7559" stroke-width="1.5"/>
                <text x="710" y="242" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2e7559">Southeast Asia</text>
                <text x="710" y="254" text-anchor="middle" font-size="7.5" fill="var(--ink-soft)">Pallava Maritime</text>
                <text x="710" y="266" text-anchor="middle" font-size="7" fill="var(--ink)">Khmer, Kawi,</text>
                <text x="710" y="275" text-anchor="middle" font-size="7" fill="var(--ink)">Mon, Thai, Balinese</text>
              </g>

              <!-- Bottom Note -->
              <text x="380" y="325" text-anchor="middle" font-size="11" fill="var(--ink-soft)">
                *Kharosthi (North-West) was written Right-to-Left from Aramaic; Brahmi was written Left-to-Right and is ancestral to all indigenous Indian scripts.
              </text>
            </svg>
          </div>
        </div>

        <!-- SCHEMATIC 5: ANCIENT INDIAN COINAGE CHRONOLOGY -->
        <div class="schematic-card" id="schematic-coinage" style="background:var(--bg-raised); border:1px solid var(--line); border-radius:var(--radius-lg); padding:24px; margin-bottom:32px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
            <div>
              <span class="badge" style="background:rgba(212,175,55,0.15); color:var(--gold); border:1px solid var(--gold); padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:600;">NUMISMATIC SCHEMA 05</span>
              <h3 style="margin:6px 0 2px; font-family:var(--font-display); font-size:1.25rem;">Evolutionary Chronology of Ancient Indian Coinage</h3>
              <p style="margin:0; font-size:0.88rem; color:var(--ink-soft);">Punch-Marked Coins → Indo-Greek Portraits → Kushana Fire-Altars → Gupta Imperial Gold Dinars</p>
            </div>
            <span style="font-size:1.6rem;">🪙</span>
          </div>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(160px, 1fr)); gap:14px; margin-top:10px;">
            <!-- Coin 1 -->
            <div style="background:var(--bg); border:1px solid var(--line); border-radius:var(--radius); padding:14px; text-align:center;">
              <div style="width:54px; height:54px; border-radius:4px; background:#d3d3d3; margin:0 auto 10px; display:flex; align-items:center; justify-content:center; border:2px dashed #666;">
                <span style="font-size:1.4rem;">☀️</span>
              </div>
              <h4 style="margin:0 0 4px; font-size:0.95rem;">Punch-Marked (PMC)</h4>
              <span style="font-size:0.75rem; color:var(--gold); font-weight:600;">6th – 2nd c. BCE</span>
              <p style="margin:6px 0 0; font-size:0.8rem; color:var(--ink-soft); line-height:1.4;">
                Silver <em>Karshapanas</em>. Stamped with 5 symbols (Sun, 6-arm, hill, bull, tree). No ruler portraits or dates. Issued by state &amp; merchant guilds (<em>Shrenis</em>).
              </p>
            </div>

            <!-- Coin 2 -->
            <div style="background:var(--bg); border:1px solid var(--line); border-radius:var(--radius); padding:14px; text-align:center;">
              <div style="width:54px; height:54px; border-radius:50%; background:#e6e6fa; margin:0 auto 10px; display:flex; align-items:center; justify-content:center; border:2px solid #708090;">
                <span style="font-size:1.4rem;">👑</span>
              </div>
              <h4 style="margin:0 0 4px; font-size:0.95rem;">Indo-Greek Die-Struck</h4>
              <span style="font-size:0.75rem; color:var(--crimson); font-weight:600;">2nd c. BCE – 1st c. CE</span>
              <p style="margin:6px 0 0; font-size:0.8rem; color:var(--ink-soft); line-height:1.4;">
                First round bilingual &amp; bi-scriptural coins (Greek obverse, Kharosthi reverse). Realistic royal portraits of kings (Menander). Greek deities depicted.
              </p>
            </div>

            <!-- Coin 3 -->
            <div style="background:var(--bg); border:1px solid var(--line); border-radius:var(--radius); padding:14px; text-align:center;">
              <div style="width:54px; height:54px; border-radius:50%; background:#ffd700; margin:0 auto 10px; display:flex; align-items:center; justify-content:center; border:2px solid #b8860b; box-shadow:0 0 8px rgba(212,175,55,0.4);">
                <span style="font-size:1.4rem;">🔥</span>
              </div>
              <h4 style="margin:0 0 4px; font-size:0.95rem;">Kushana Gold Dinar</h4>
              <span style="font-size:0.75rem; color:#b8860b; font-weight:600;">1st – 3rd c. CE</span>
              <p style="margin:6px 0 0; font-size:0.8rem; color:var(--ink-soft); line-height:1.4;">
                First large-scale gold issues pegged to Roman <em>Aureus</em> (~8g). King at fire-altar. Eclectic pantheon: <em>Oesho</em> (Shiva), <em>BODDO</em> (Buddha), Nana, Mithra.
              </p>
            </div>

            <!-- Coin 4 -->
            <div style="background:var(--bg); border:1px solid var(--line); border-radius:var(--radius); padding:14px; text-align:center;">
              <div style="width:54px; height:54px; border-radius:50%; background:#d4af37; margin:0 auto 10px; display:flex; align-items:center; justify-content:center; border:2px solid #8c2d19; box-shadow:0 0 10px rgba(184,51,42,0.3);">
                <span style="font-size:1.4rem;">🏹</span>
              </div>
              <h4 style="margin:0 0 4px; font-size:0.95rem;">Gupta Imperial Gold</h4>
              <span style="font-size:0.75rem; color:#8c2d19; font-weight:600;">4th – 6th c. CE</span>
              <p style="margin:6px 0 0; font-size:0.8rem; color:var(--ink-soft); line-height:1.4;">
                Artistic zenith (<em>Suvarna</em>). Types: King &amp; Queen (Kumaradevi), Archer, Lyrist (Veena), Asvamedha horse, Tiger-slayer. Poetic Sanskrit legends in Brahmi.
              </p>
            </div>

            <!-- Coin 5 -->
            <div style="background:var(--bg); border:1px solid var(--line); border-radius:var(--radius); padding:14px; text-align:center;">
              <div style="width:54px; height:54px; border-radius:50%; background:#c0a060; margin:0 auto 10px; display:flex; align-items:center; justify-content:center; border:2px dashed #8c2d19;">
                <span style="font-size:1.4rem;">📉</span>
              </div>
              <h4 style="margin:0 0 4px; font-size:0.95rem;">Post-Gupta Contraction</h4>
              <span style="font-size:0.75rem; color:var(--ink-faint); font-weight:600;">6th – 10th c. CE</span>
              <p style="margin:6px 0 0; font-size:0.8rem; color:var(--ink-soft); line-height:1.4;">
                Sharp alloy debasement (iron/copper adulteration), scarcity of small coins. R.S. Sharma's prime indicator of feudalization &amp; localized barter economy.
              </p>
            </div>
          </div>
        </div>
      </div>
'''
