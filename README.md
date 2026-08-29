# Complete History of India — Interactive Atlas

A static, data-driven, interactive history site covering **Prehistory through the Delhi Sultanate (Khalji Dynasty, 1320 CE)**, built entirely from a supplied set of revision-sheet infographics. Pure HTML/CSS/vanilla JS — no build step, no backend, works on GitHub Pages.

## What's inside

```
/
├── index.html          Home page (hero, journey rail, period grid, featured events/women)
├── timeline.html        Master interactive timeline (filterable, expandable, click-to-detail)
├── period.html           Single dynamic template — renders any period via ?id=<period-id>
├── themes.html           Thematic index (Polity, War, Religion, Economy, Society, Women, Art, Science...)
├── people.html           All personalities, filterable by period
├── women.html            Dedicated "Women in History" section
├── search.html           Full-page client-side search
├── about.html            Sources & method
├── css/style.css         Design system ("Stone & Ink" theme, light + dark)
├── js/
│   ├── data.js            Loads & caches data/history.json + external-links.json
│   ├── app.js              Nav, footer, breadcrumbs, dark mode, UPSC mode, lightbox, external-link renderer
│   ├── search.js           Client-side search index + live search wiring
│   ├── timeline.js         Master timeline rendering & filtering
│   └── period.js           Renders period.html from JSON data
├── data/
│   ├── history.json        THE single source of truth — all periods, phases, events, people, women, UPSC facts
│   └── external-links.json Curated keyword → official/encyclopedic URL map
└── assets/images/        All 17 supplied infographic PNGs (used as "original revision sheet" viewables)
```

## Running locally

No build tools needed. From the project root:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`. (Opening `index.html` directly via `file://` will not work because the pages `fetch()` the JSON data files, which browsers block over `file://`.)

## Deploying to GitHub Pages

1. Create a new GitHub repository (e.g. `history-of-india`).
2. Copy every file in this folder into the repository root, preserving the folder structure above.
3. Commit and push to the `main` branch.
4. In the repository, go to **Settings → Pages**, set **Source** to `main` branch, root folder, and save.
5. Your site will be live at `https://<your-username>.github.io/<repo-name>/`.

All paths in this project are relative, so it works whether the repo is served from the root of a custom domain or from a `/repo-name/` sub-path.

## How the data model works

Everything on the site is driven by **one file: `data/history.json`**. It contains a `periods` array; each period object looks like this (trimmed):

```json
{
  "id": "mauryan-empire",
  "order": 5,
  "title": "The Mauryan Empire",
  "dateRange": "c. 322 – 185 BCE",
  "category": "ancient",
  "tagline": "One of the greatest empires of Ancient India",
  "heroImg": "mauryan_empire_2.png",
  "sourceImages": ["mauryan_empire.png", "mauryan_empire_2.png"],
  "overview": "...",
  "phases": [ { "name": "...", "range": "...", "points": ["..."] } ],
  "aspects": { "Political Administration": ["..."], "Economy": ["..."] },
  "events": [ { "year": "322 BCE", "title": "...", "theme": "polity", "desc": "..." } ],
  "people": [ { "name": "...", "role": "...", "note": "..." } ],
  "women": [ { "name": "...", "role": "...", "note": "..." } ],
  "themes": ["polity", "war", "religion"],
  "upsc": { "prelims": ["..."], "mains": ["..."] },
  "quickFacts": [ ["Founder", "Chandragupta Maurya"] ]
}
```

`period.html?id=mauryan-empire` reads this object and renders the entire page — hero, phase timeline, event cards, aspect accordions, women/people cards, UPSC panels, quick facts, and previous/next navigation (computed automatically from each period's `order`). The home page, master timeline, themes page, people page and women page are all also generated from this same file, so **everything is connected automatically** — add an event once and it appears in search, the timeline, the home page's featured strip, and the period page.

## Adding a new historical period (e.g. the Mughal Empire)

You do **not** need to touch any HTML or redesign anything:

1. Drop the new infographic image(s) into `assets/images/`.
2. Open `data/history.json` and add a new object to the `periods` array, following the shape above. Give it the next `order` number (e.g. `15`) and a unique `id` (e.g. `"mughal-empire"`).
3. Save. The new period will automatically appear in:
   - the home page's journey rail and period grid
   - the master timeline
   - the themes page (for any `themes` you tag it with)
   - people.html / women.html (for anyone in its `people`/`women` arrays)
   - search results
   - previous/next navigation on the periods immediately before and after it

## Adding or updating external reference links

Edit `data/external-links.json`. It's a flat map of `"Keyword": { "url": "...", "source": "..." }`. Any name that appears in a period's `people` array and matches a key here will automatically render as a styled, tooltipped external link (`Name ↗`) in that period's "Further Reading" panel. Prefer, in order: official Government of India / institutional sites → UN/UNESCO/international bodies → Encyclopaedia Britannica → Wikipedia.

## Design notes

- **Theme:** "Stone & Ink" — a carved-tablet/epigraph aesthetic (sandstone surfaces, ink-indigo type, verdigris + sindoor-red + ochre accent colors), with a full dark mode ("Night Epigraph"). Typography: Fraunces (display), Inter (body), IBM Plex Mono (dates/labels/utility).
- **UPSC Mode:** a toggle in the nav bar (state saved to `localStorage`) that reveals dedicated Prelims/Mains panels on every period page.
- **Dark mode:** toggle in the nav bar, saved to `localStorage`, respects `prefers-color-scheme` on first visit.
- **Accessibility:** semantic headings, visible focus states, `prefers-reduced-motion` respected, alt text on images, keyboard-operable accordions/timeline.
- **Original sheets:** every period page includes a "View Original Revision Sheet" control that opens the source infographic in a zoom/pan lightbox.

## Uttar Pradesh History track (UPPSC)

A parallel, self-contained regional track — **`up-history.html`** — covers Uttar Pradesh's history specifically for UPPSC (GS Paper I & II), from prehistoric settlements through the Vedic Age, Mahajanapadas, Maurya, Post-Maurya, Gupta, Harsha, Gurjara-Pratihara, Kalachuri-Chandella, Gahadavala, Delhi Sultanate, Jaunpur Sultanate, Mughal and Later Mughal periods, to the Revolt of 1857, British administration, and the 19th-century socio-religious reform movements — 20 pages in total.

**How it's kept separate from, yet connected to, the national chronology:**
- Every UP period carries `"region": "up"` in `data/history.json`. The home page (`index.html`) and master timeline (`timeline.html`) filter these out, so the national "one continuous journey" stays exactly as it was.
- `HistoryData.getAdjacent()` computes previous/next navigation *within the same region* — national periods chain among themselves, and the 20 UP periods chain among themselves in their own chronological sequence — so neither prev/next chain gets scrambled by the other.
- `up-history.html` is a dedicated hub (journey rail + grid) scoped to `region: "up"`, in the same visual language as the rest of the site, with its own `up` category colour.
- Nothing else was filtered: `themes.html`, `people.html`, `women.html`, `search.html` and the knowledge graph (`graph.html`) still include UP content alongside national content, because that's where the cross-region connections actually pay off — Akbar, Ashoka, Chandragupta Maurya, Samudragupta, Kanishka, Menander, Pushyamitra Shunga and dozens of other names recur in both tracks and are automatically cross-linked (84 shared names as of this build). Searching "Akbar" or opening his card on either page surfaces the other page too.

## Elaborated content

Both the national and Uttar Pradesh tracks have been through an elaboration pass beyond the initial infographic extraction:

- **Every period's `overview` field** (all 77) was rewritten into a longer, standalone narrative — national overviews average ~250 words, UP overviews ~200 — adding causation, significance, and connective context between periods. The 28 UP overviews additionally cross-reference their national counterpart by name wherever one exists (e.g. the UP Mughal Period page explicitly says what it adds beyond the national Akbar/Jahangir/Shah Jahan pages).
- **Every UP-track aspect-table category** (127 of them, across all 28 pages) now carries an optional `intro` string alongside its `points` array — a short explanatory lead-in rendered above the bullet list on the period page, flagging what's exam-relevant, what connects to another page, or what's easy to misread. `js/period.js`'s aspect-rendering code checks for this `{intro, points}` shape and falls back to the older plain-array format automatically, so the national track's aspect tables (still plain arrays) render exactly as before with no migration needed.

## Knowledge graph

Beyond the static "Related Themes" panel, every period page now includes a **Related Topics** panel and automatic **"↗ also appears in"** links on every person/woman card. These are computed live at page-load time by `js/graph.js` from the same structured fields every period already carries (`themes`, `people`, `women`, `events`) — nothing here is a hand-authored link list:

- **Cross-period people**: any name that recurs across two or more periods' `people`/`women` arrays (e.g. Mahatma Gandhi appearing in *Indian Freedom Struggle*, *Mahatma Gandhi*, *Independence of India* and *India 1947–1964*) is automatically cross-linked, both ways.
- **Theme-sibling events**: each period's "Related Topics" panel surfaces a handful of events from *other* periods that share at least one theme tag (`polity`, `war`, `religion`, `economy`, `society`, `women`, `art`, `science`, `foreign`).
- **Chronological neighbours**: a flattened, site-wide event list (ordered by each period's `order` field) gives every event a computed previous/next neighbour, independent of which period it belongs to.
- **External resources**: resolved through the existing `data/external-links.json` keyword map.

Open **`graph.html`** (linked from every page's nav as "Knowledge Graph") to search any entity directly and see all of the above laid out — the historical period(s) it belongs to, its category, related events, related people/occurrences, related themes, chronological neighbours, and its external resource link.

Because the graph is computed rather than authored, it automatically extends to any new period added to `data/history.json` — a newly-added person or event just needs the same field names the rest of the file already uses.

## Current coverage

**77 periods** in total: **49 in the national chronology** (Palaeolithic Age through India 2020–Present, plus five World History pages) and **28 in the dedicated Uttar Pradesh / UPPSC track**.

National track: Prehistoric Age → Indus Valley Civilization → Vedic Age → Age of Mahajanapadas → Mauryan Empire → Ashoka the Great (deep-dive) → Post-Mauryan Period → Gupta Age → Post-Gupta Age → Early Medieval Period → Kingdoms of the North → Kingdoms of the South → Delhi Sultanate (overview) → Mamluk Dynasty → Khalji Dynasty → Tughlaq Dynasty → Sayyid Dynasty → Lodi Dynasty → Vijayanagara Empire → Mughal Empire (overview) → Babur → Humayun → The Sur Interregnum → Akbar the Great → Jahangir → Shah Jahan → Aurangzeb Alamgir → Later Mughal Empire → Establishment of British Power → The Sikh Empire → British Colonial Rule (overview) → British Administration in India → Socio-Religious Reforms → Indian Freedom Struggle → Mahatma Gandhi → Independence of India (1939–47) → Independent India — Major Phases (overview) → India 1947–1964 → India 1965–1980 → India 1981–1991 → India 1992–2000 → India 2001–2010 → India 2011–2020 → India 2020–Present → World History Chronological Chart (overview, 1750–1945) → The French Revolution → World War I → The Russian Revolution → World War II.

Uttar Pradesh track (28 pages, in corrected chronological order): UP History Overview → Prehistoric & Early Settlements → Vedic Age → Mahajanapadas → Maurya Period → Post-Maurya Period → Gupta Period → Harsha Period → Gurjara-Pratiharas → Kalachuris & Chandellas → Gahadavalas → Foundation of Cities in the Medieval Period → Delhi Sultanate Period → Jaunpur Sultanate → Sayyid & Lodi Dynasties → Mughal Period → Later Mughals → British Rule & Administration → Revolt of 1857 → Freedom Struggle in U.P. → Socio-Religious Movements → United Provinces During Modern India → Formation of Uttar Pradesh → Political Developments in Uttar Pradesh → Reorganisation of Uttar Pradesh → Economic & Social Progress → Uttar Pradesh in the 21st Century → Important Cities & Personalities of Uttar Pradesh.

*(Note: the Jaunpur Sultanate, 1394–1479, now correctly precedes the Sayyid & Lodi Dynasty page, from 1414, fixing an ordering bug from an earlier build.)*

This matches every supplied infographic image across all upload batches; alternate/expanded versions of the same period were merged into one richer entry where the source sheets overlapped (e.g. the two Babur, Akbar and Jahangir sheets; the two Independent-India "Major Phases" overview sheets; the Indian Freedom Struggle page, which draws on both `freedom_struggle.png` and the closely overlapping `movements_national.png`; the second `up_socio_religious_movement.png` upload was recognised as a duplicate and skipped rather than re-added). The five World History pages carry their own `world` category and are flagged as global background rather than part of India's national chronology; the twenty-eight Uttar Pradesh pages carry `region: "up"` and their own `up` category, and are flagged throughout as a UPPSC-focused regional companion rather than a duplicate of the national story.

A small number of dates that were not fully unambiguous in the source sheets (chiefly the exact day Uttar Pradesh was renamed from the United Provinces in January 1950) were checked against independent reference sources; the period page notes this rather than silently picking one date.

**Not yet included** because no source infographic has been supplied for it: nothing currently outstanding — every uploaded sheet has a corresponding page. Future periods, deeper sub-pages, or other state-specific tracks (in the style of the Uttar Pradesh track) can be added the same way — the data model, navigation, search index, knowledge graph, and region-aware prev/next chain all extend automatically from a new entry in `data/history.json`.
