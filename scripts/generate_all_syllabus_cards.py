# -*- coding: utf-8 -*-
"""
generate_all_syllabus_cards.py
Compiles the complete 41-card syllabus into syllabus.html
"""

import os
import sys
from cards_sec1_ancient import get_sec1_html
from cards_sec2_medieval import get_sec2_html
from cards_sec3_modern import get_sec3_html
from cards_sec4_post import get_sec4_html
from cards_sec5_world import get_sec5_html
from cards_sec6_culture import get_sec6_html
from cards_partA_up import get_partA_html
from cards_partB_tracks import get_partB_html

def get_header():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Complete Examination Syllabus &amp; Master Study Guide — History, Art &amp; Culture | Complete History of India</title>
<meta name="description" content="Master examination syllabus and comprehensive study guide covering Ancient, Medieval, Modern, Post-Independence, World History, Art & Culture, UP Special, RO/ARO General Hindi, RRB NTPC, and Banking Awareness.">
<link rel="stylesheet" href="css/style.css">
  <!-- Google Analytics Tracking (G-B0Z2G21W4F) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-B0Z2G21W4F"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-B0Z2G21W4F');
  </script>

  <!-- Google AdSense -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>

<style>
/* Syllabus Hub Styles */
.syl-hero {
  padding: 56px 0 44px;
  background: linear-gradient(180deg, var(--bg-raised) 0%, var(--bg) 100%);
  border-bottom: 1px solid var(--line);
}
.syl-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 5px 14px;
  border-radius: 999px;
  background: var(--accent-tint);
  color: var(--accent-strong);
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 16px;
  border: 1px solid rgba(79, 111, 100, 0.25);
}
.syl-nav-strip {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding: 14px 0 16px;
  border-bottom: 2px solid var(--line-soft);
  margin-bottom: 32px;
  scrollbar-width: thin;
}
.syl-nav-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  background: var(--bg-sunken);
  border: 1px solid var(--line);
  border-radius: 6px;
  color: var(--ink);
  font-family: var(--font-body);
  font-size: 0.92rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s ease;
}
.syl-nav-btn:hover {
  background: var(--bg-raised);
  border-color: var(--accent);
  color: var(--accent-strong);
}
.syl-nav-btn.active {
  background: var(--accent-strong);
  color: #ffffff;
  border-color: var(--accent-strong);
  box-shadow: 0 2px 8px rgba(56, 80, 74, 0.25);
}
.syl-section-pane {
  display: none;
  animation: fadeIn 0.25s ease forwards;
}
.syl-section-pane.active {
  display: block;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

.syl-card {
  background: var(--bg-raised);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 26px 30px;
  margin-bottom: 28px;
  box-shadow: var(--shadow);
}
.syl-card-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}
.syl-card-title {
  font-family: var(--font-display);
  font-size: 1.45rem;
  margin: 0;
  color: var(--ink);
}
.syl-img-banner {
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid var(--line);
  margin: 18px 0;
  background: #000;
  max-height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.syl-img-banner img {
  width: 100%;
  height: 100%;
  max-height: 380px;
  object-fit: cover;
  display: block;
}
.syl-action-bar {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid var(--line-soft);
}
.syl-box-gold {
  background: var(--gold-tint);
  border-left: 4px solid var(--gold);
  padding: 14px 18px;
  border-radius: 0 6px 6px 0;
  margin: 16px 0;
  font-size: 0.94rem;
  color: #4a3511;
}
.syl-box-accent {
  background: var(--accent-tint);
  border-left: 4px solid var(--accent);
  padding: 14px 18px;
  border-radius: 0 6px 6px 0;
  margin: 16px 0;
  font-size: 0.94rem;
  color: #17362d;
}
.syl-box-seal {
  background: var(--seal-tint);
  border-left: 4px solid var(--seal);
  padding: 14px 18px;
  border-radius: 0 6px 6px 0;
  margin: 16px 0;
  font-size: 0.94rem;
  color: #4a1515;
}
</style>
</head>
<body>
<a href="#main" class="skip-link">Skip to content</a>
<nav class="site-nav" id="siteNav"></nav>

<main id="main">
  <div class="wrap"><div class="breadcrumb" id="breadcrumb"></div></div>

  <header class="syl-hero">
    <div class="wrap">
      <span class="syl-badge">📋 Master Examination Blueprint &amp; Syllabus Guide</span>
      <h1 style="font-size:clamp(2.2rem,4.8vw,3.4rem); line-height:1.15; margin:0 0 16px;">
        Complete Syllabus of <em>History, Art &amp; Culture</em>
      </h1>
      <p style="font-size:1.1rem; max-width:82ch; color:var(--ink-soft); line-height:1.6; margin:0 0 24px;">
        Designed from canonical academic textbooks and multi-commission syllabi — covering <strong>UPSC Civil Services</strong>, <strong>UPPSC Combined State Services (GS Paper 1, 5 &amp; 6)</strong>, <strong>UP RO/ARO (Samiksha Adhikari)</strong>, <strong>Railway Recruitment Board (RRB NTPC)</strong>, and <strong>Banking Awareness (IBPS/SBI)</strong>. Features 41 dedicated, granular units, authentic iconography exhibits, historiographical debates, key exam terms, and direct 1-click links to the <strong>8,425-Question Practice Hub</strong> and <strong>91 Period Chapters</strong>.
      </p>

      <div class="hero-ctas" style="display:flex; gap:12px; flex-wrap:wrap; margin-bottom:28px;">
        <a href="practice.html" class="btn btn-primary">🎯 Practice Hub (8,425 Questions)</a>
        <a href="up-history.html" class="btn btn-outline">🏛️ Uttar Pradesh Special Hub</a>
        <a href="art-culture.html" class="btn btn-outline">🎨 Art &amp; Culture Deep Metrics</a>
        <a href="books.html" class="btn btn-outline">📚 27 Standard Textbooks</a>
      </div>

      <div class="stat-strip">
        <div class="stat"><span class="num">41</span><span class="lab">Granular Syllabus Cards</span></div>
        <div class="stat"><span class="num">8</span><span class="lab">Integrated Section Panes</span></div>
        <div class="stat"><span class="num">8,160+</span><span class="lab">Prelims MCQs Available</span></div>
        <div class="stat"><span class="num">265+</span><span class="lab">Mains GS Model Frameworks</span></div>
        <div class="stat"><span class="num">100%</span><span class="lab">Syllabus Coverage</span></div>
      </div>
    </div>
  </header>

  <section class="section" style="padding-top:24px;">
    <div class="wrap">

      <!-- Navigation Strip -->
      <nav class="syl-nav-strip" aria-label="Syllabus Sections">
        <button class="syl-nav-btn active" onclick="switchSylTab('sec-ancient')">Section 1: Ancient History</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-medieval')">Section 2: Medieval History</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-modern')">Section 3: Modern History</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-post')">Section 4: Post-Independence</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-world')">Section 5: World History</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-culture')">Section 6: Art &amp; Culture</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-up')">Part A: UP Special &amp; RO/ARO</button>
        <button class="syl-nav-btn" onclick="switchSylTab('sec-rrb-bank')">Part B: RRB NTPC &amp; Banking</button>
      </nav>
'''

def get_footer():
    return '''
    </div>
  </section>
</main>

<footer id="siteFooter"></footer>

<script src="js/data.js"></script>
<script src="js/app.js"></script>
<script src="js/search.js"></script>
<script src="js/graph.js"></script>
<script>
function switchSylTab(tabId) {
  document.querySelectorAll('.syl-nav-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.syl-section-pane').forEach(p => p.classList.remove('active'));

  const activeBtn = Array.from(document.querySelectorAll('.syl-nav-btn')).find(b => b.getAttribute('onclick').includes(tabId));
  if (activeBtn) activeBtn.classList.add('active');

  const pane = document.getElementById(tabId);
  if (pane) pane.classList.add('active');
}

function initSylHub(){
  renderNav('syllabus.html');
  renderBreadcrumb([{label:'Home',href:'index.html'},{label:'Exam Syllabus & Master Study Guide'}]);
  renderFooter();
  initReveal();
}
initSylHub();
</script>
</body>
</html>
'''

def compile_full_syllabus():
    parts = [
        get_header(),
        get_sec1_html(),
        get_sec2_html(),
        get_sec3_html(),
        get_sec4_html(),
        get_sec5_html(),
        get_sec6_html(),
        get_partA_html(),
        get_partB_html(),
        get_footer()
    ]
    full_html = "".join(parts)
    with open('syllabus.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"SUCCESS: Compiled syllabus.html ({len(full_html)} characters, {len(full_html.splitlines())} lines).")

if __name__ == '__main__':
    compile_full_syllabus()
