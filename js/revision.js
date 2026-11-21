/**
 * Quick Revision & Pointer Notes Module (revision.js)
 * High-yield revision hub covering 80 ancient history topics and 37 comparison matrices.
 * Synthesizes R.S. Sharma, PMF IAS, Poonam Dalal Dahiya, and Spectrum.
 */

const HistoryRevision = (() => {
  let revisionData = null;
  let activeCategory = 'all';
  let activeMode = 'pointers'; // 'pointers' | 'comprehensive' | 'tables'
  let searchQuery = '';
  let bookmarkedOnly = false;
  let expandedCards = new Set();
  let bookmarks = new Set();

  // Load bookmarks from localStorage
  try {
    const saved = localStorage.getItem('hist_revision_bookmarks');
    if (saved) {
      bookmarks = new Set(JSON.parse(saved));
    }
  } catch (e) {
    console.warn('Could not read bookmarks from localStorage', e);
  }

  function saveBookmarks() {
    try {
      localStorage.setItem('hist_revision_bookmarks', JSON.stringify(Array.from(bookmarks)));
    } catch (e) {
      console.warn('Could not save bookmarks', e);
    }
  }

  async function init() {
    try {
      const resp = await fetch('data/revision-notes.json');
      if (!resp.ok) throw new Error('Failed to load revision data');
      revisionData = await resp.json();
      
      setupEventListeners();
      renderCategoryFilters();
      renderStats();
      render();
    } catch (err) {
      console.error(err);
      const container = document.getElementById('revisionCardsGrid');
      if (container) {
        container.innerHTML = `<div class="error-box">Unable to load revision notes. Please ensure data/revision-notes.json is present.</div>`;
      }
    }
  }

  function renderStats() {
    if (!revisionData) return;
    const statsEl = document.getElementById('revisionStats');
    if (statsEl) {
      statsEl.innerHTML = `
        <div class="rev-stat-item"><span class="rev-stat-num">${revisionData.totalTopics}</span><span class="rev-stat-label">High-Yield Modules</span></div>
        <div class="rev-stat-item"><span class="rev-stat-num">${revisionData.totalTables}</span><span class="rev-stat-label">Comparison Matrices</span></div>
        <div class="rev-stat-item"><span class="rev-stat-num">6</span><span class="rev-stat-label">Mauryan Lithic Images</span></div>
        <div class="rev-stat-item"><span class="rev-stat-num" id="statBookmarks">${bookmarks.size}</span><span class="rev-stat-label">Bookmarked Topics</span></div>
      `;
    }
  }

  function renderCategoryFilters() {
    if (!revisionData) return;
    const filterContainer = document.getElementById('categoryFilters');
    if (!filterContainer) return;

    // Distinct categories
    const categories = ['all', ...new Set(revisionData.topics.map(t => t.category))];

    filterContainer.innerHTML = categories.map(cat => {
      const label = cat === 'all' ? 'All 80+ Topics' : cat;
      const count = cat === 'all' ? revisionData.topics.length : revisionData.topics.filter(t => t.category === cat).length;
      const isActive = cat === activeCategory ? 'active' : '';
      return `<button class="rev-filter-pill ${isActive}" data-category="${cat}">${label} <span class="pill-badge">${count}</span></button>`;
    }).join('');

    filterContainer.querySelectorAll('.rev-filter-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        filterContainer.querySelectorAll('.rev-filter-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeCategory = btn.dataset.category;
        render();
      });
    });
  }

  function setupEventListeners() {
    // Mode switcher buttons
    document.querySelectorAll('.rev-mode-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.rev-mode-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeMode = btn.dataset.mode;
        render();
      });
    });

    // Search input
    const searchInput = document.getElementById('revisionSearchInput');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value.toLowerCase().trim();
        render();
      });
    }

    // Bookmark toggle
    const bookmarkToggle = document.getElementById('toggleBookmarksBtn');
    if (bookmarkToggle) {
      bookmarkToggle.addEventListener('click', () => {
        bookmarkedOnly = !bookmarkedOnly;
        bookmarkToggle.classList.toggle('active', bookmarkedOnly);
        bookmarkToggle.innerHTML = bookmarkedOnly ? '⭐ Showing Starred Only' : '☆ Show Starred Only';
        render();
      });
    }

    // Copy all visible button
    const copyAllBtn = document.getElementById('copyAllVisibleBtn');
    if (copyAllBtn) {
      copyAllBtn.addEventListener('click', () => copyAllVisibleNotes());
    }

    // Expand all / Collapse all
    const expandAllBtn = document.getElementById('expandAllBtn');
    if (expandAllBtn) {
      expandAllBtn.addEventListener('click', () => {
        if (!revisionData) return;
        revisionData.topics.forEach(t => expandedCards.add(t.id));
        render();
      });
    }

    const collapseAllBtn = document.getElementById('collapseAllBtn');
    if (collapseAllBtn) {
      collapseAllBtn.addEventListener('click', () => {
        expandedCards.clear();
        render();
      });
    }

    // Print button
    const printBtn = document.getElementById('printRevisionBtn');
    if (printBtn) {
      printBtn.addEventListener('click', () => window.print());
    }
  }

  function getFilteredTopics() {
    if (!revisionData) return [];
    return revisionData.topics.filter(t => {
      // Category filter
      if (activeCategory !== 'all' && t.category !== activeCategory) {
        return false;
      }
      // Bookmark filter
      if (bookmarkedOnly && !bookmarks.has(t.id)) {
        return false;
      }
      // Search filter
      if (searchQuery) {
        const titleMatch = t.title.toLowerCase().includes(searchQuery);
        const notesMatch = t.fullNotes.toLowerCase().includes(searchQuery);
        const pointersMatch = t.pointers.some(p => p.toLowerCase().includes(searchQuery));
        const keywordMatch = (t.examKeywords || []).some(k => k.toLowerCase().includes(searchQuery));
        if (!titleMatch && !notesMatch && !pointersMatch && !keywordMatch) {
          return false;
        }
      }
      return true;
    });
  }

  function render() {
    const grid = document.getElementById('revisionCardsGrid');
    const tableContainer = document.getElementById('comparisonTablesView');
    if (!grid) return;

    if (activeMode === 'tables') {
      grid.style.display = 'none';
      if (tableContainer) {
        tableContainer.style.display = 'block';
        renderComparisonTables();
      }
      return;
    }

    grid.style.display = 'grid';
    if (tableContainer) tableContainer.style.display = 'none';

    const topicsToRender = getFilteredTopics();

    if (topicsToRender.length === 0) {
      grid.innerHTML = `
        <div class="rev-no-results">
          <div style="font-size:2.5rem; margin-bottom:12px;">🔍</div>
          <h3>No revision topics match your filter</h3>
          <p>Try clearing your search query "${searchQuery}" or switching the era category filter.</p>
          <button class="btn btn-outline btn-sm" onclick="HistoryRevision.resetFilters()">Reset All Filters</button>
        </div>
      `;
      return;
    }

    grid.innerHTML = topicsToRender.map(topic => renderTopicCard(topic)).join('');

    // Attach card event listeners
    grid.querySelectorAll('.rev-card').forEach(card => {
      const topicId = card.dataset.id;
      
      // Star button
      const starBtn = card.querySelector('.rev-star-btn');
      if (starBtn) {
        starBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          toggleBookmark(topicId);
        });
      }

      // Copy button
      const copyBtn = card.querySelector('.rev-copy-btn');
      if (copyBtn) {
        copyBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          copyTopic(topicId);
        });
      }

      // Expand / Toggle card
      const toggleBtn = card.querySelector('.rev-expand-toggle');
      if (toggleBtn) {
        toggleBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          if (expandedCards.has(topicId)) {
            expandedCards.delete(topicId);
          } else {
            expandedCards.add(topicId);
          }
          render();
        });
      }
    });
  }

  function renderTopicCard(topic) {
    const isBookmarked = bookmarks.has(topic.id);
    const isExpanded = expandedCards.has(topic.id) || activeMode === 'comprehensive';
    const hasImages = topic.images && topic.images.length > 0;
    const hasTables = topic.tables && topic.tables.length > 0;

    let contentHtml = '';

    if (activeMode === 'pointers') {
      contentHtml = `
        <div class="rev-pointers-list">
          ${topic.pointers.map(p => `
            <div class="rev-pointer-item">
              <span class="rev-bullet">⚡</span>
              <div class="rev-pointer-text">${p}</div>
            </div>
          `).join('')}
        </div>
      `;

      // If user expanded this card in pointers mode, show the full notes below
      if (isExpanded) {
        contentHtml += `
          <div class="rev-deep-dive-panel">
            <h4 class="rev-subheading">📖 Detailed Text &amp; Historical Nuance:</h4>
            <div class="rev-full-text">${formatFullNotes(topic.fullNotes)}</div>
            ${hasTables ? renderEmbeddedTables(topic.tables) : ''}
            ${hasImages ? renderEmbeddedImages(topic.images) : ''}
          </div>
        `;
      }
    } else {
      // Comprehensive mode
      contentHtml = `
        <div class="rev-comprehensive-view">
          <div class="rev-full-text">${formatFullNotes(topic.fullNotes)}</div>
          ${hasTables ? renderEmbeddedTables(topic.tables) : ''}
          ${hasImages ? renderEmbeddedImages(topic.images) : ''}
        </div>
      `;
    }

    return `
      <article class="rev-card ${isBookmarked ? 'is-starred' : ''}" data-id="${topic.id}">
        <div class="rev-card-header">
          <div class="rev-meta-left">
            <span class="rev-badge-sl">#${topic.slNo}</span>
            <span class="rev-badge-cat">${escapeHtml(topic.category)}</span>
            ${hasTables ? '<span class="rev-badge-indicator">⚖️ Matrix</span>' : ''}
            ${hasImages ? '<span class="rev-badge-indicator">🖼️ Photos</span>' : ''}
          </div>
          <div class="rev-actions-right">
            <button class="rev-action-icon rev-star-btn" title="${isBookmarked ? 'Remove Bookmark' : 'Bookmark Topic'}">
              ${isBookmarked ? '★' : '☆'}
            </button>
            <button class="rev-action-icon rev-copy-btn" title="Copy Pointer Notes to Clipboard">
              📋
            </button>
            <button class="rev-action-icon rev-expand-toggle" title="${isExpanded ? 'Collapse' : 'Expand Full Notes'}">
              ${isExpanded ? '▲' : '▼'}
            </button>
          </div>
        </div>

        <h3 class="rev-card-title">${escapeHtml(topic.title)}</h3>

        ${topic.examKeywords && topic.examKeywords.length > 0 ? `
          <div class="rev-tags-strip">
            ${topic.examKeywords.map(k => `<span class="rev-tag">${escapeHtml(k)}</span>`).join('')}
          </div>
        ` : ''}

        <div class="rev-card-body">
          ${contentHtml}
        </div>

        <div class="rev-card-footer">
          <div class="rev-books-hint">
            <span>📚 Canonical Source:</span> <em>India's Ancient Past (R.S. Sharma)</em> &bull; <em>PMF IAS</em> &bull; <em>Poonam Dalal Dahiya</em>
          </div>
          <div class="rev-footer-links">
            <a href="practice.html?q=${encodeURIComponent(topic.title)}" class="rev-link-btn" title="Practice MCQs on this topic">🎯 Practice MCQs &rarr;</a>
          </div>
        </div>
      </article>
    `;
  }

  function formatFullNotes(text) {
    if (!text) return '';
    // Format bold headings, subheadings, and paragraphs cleanly
    const safe = escapeHtml(text);
    return safe
      .split('\n\n')
      .map(p => {
        let formatted = p.trim();
        // Bold title before colon
        formatted = formatted.replace(/^([A-Za-z0-9\s—–\(\)\/&]+):/gm, '<strong>$1:</strong>');
        return `<p>${formatted.replace(/\n/g, '<br>')}</p>`;
      })
      .join('');
  }

  function renderEmbeddedTables(tables) {
    if (!tables || tables.length === 0) return '';
    return tables.map(tbl => `
      <div class="rev-table-wrap">
        <table class="rev-comp-table">
          <thead>
            <tr>
              ${tbl.headers.map(h => `<th>${escapeHtml(h)}</th>`).join('')}
            </tr>
          </thead>
          <tbody>
            ${tbl.rows.map(row => `
              <tr>
                ${row.map(cell => `<td>${escapeHtml(cell)}</td>`).join('')}
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    `).join('');
  }

  function renderEmbeddedImages(images) {
    if (!images || images.length === 0) return '';
    return `
      <div class="rev-image-gallery">
        <h4 class="rev-subheading" style="margin-top:16px;">🖼️ Master Architectural &amp; Epigraphic Artifacts:</h4>
        <div class="rev-gallery-grid">
          ${images.map(img => `
            <figure class="rev-fig">
              <div class="rev-fig-img-wrap">
                <img src="${img.path}" alt="${escapeHtml(img.caption)}" loading="lazy" onclick="HistoryRevision.openLightbox('${img.path}', '${escapeHtml(img.caption)}')">
              </div>
              <figcaption>
                <span class="rev-fig-type">${escapeHtml(img.type || 'Artifact')}</span>
                ${escapeHtml(img.caption)}
              </figcaption>
            </figure>
          `).join('')}
        </div>
      </div>
    `;
  }

  function renderComparisonTables() {
    const container = document.getElementById('comparisonTablesView');
    if (!container || !revisionData) return;

    const tables = revisionData.comparisonTables || [];
    if (tables.length === 0) {
      container.innerHTML = `<div class="rev-no-results">No comparison tables available.</div>`;
      return;
    }

    container.innerHTML = `
      <div class="rev-tables-intro">
        <h2 style="margin:0 0 8px; font-family:var(--font-display); color:var(--ink);">37 Master Historical Comparison &amp; Reference Matrices</h2>
        <p style="color:var(--ink-soft); margin-bottom:24px;">Structured comparative analytics synthesized across all 80 syllabus modules for UPSC Prelims classification and Mains comparative questions.</p>
      </div>
      <div class="rev-tables-stack">
        ${tables.map((t, idx) => `
          <div class="rev-table-card">
            <div class="rev-table-header">
              <span class="rev-table-badge">Matrix #${idx + 1} &bull; Topic #${t.topicSl}</span>
              <h3 class="rev-table-title">${escapeHtml(t.topicTitle)}</h3>
            </div>
            <div class="rev-table-wrap">
              <table class="rev-comp-table">
                <thead>
                  <tr>
                    ${t.tableData.headers.map(h => `<th>${escapeHtml(h)}</th>`).join('')}
                  </tr>
                </thead>
                <tbody>
                  ${t.tableData.rows.map(row => `
                    <tr>
                      ${row.map(cell => `<td>${escapeHtml(cell)}</td>`).join('')}
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
          </div>
        `).join('')}
      </div>
    `;
  }

  function toggleBookmark(topicId) {
    if (bookmarks.has(topicId)) {
      bookmarks.delete(topicId);
    } else {
      bookmarks.add(topicId);
    }
    saveBookmarks();
    renderStats();
    render();
  }

  function copyTopic(topicId) {
    if (!revisionData) return;
    const topic = revisionData.topics.find(t => t.id === topicId);
    if (!topic) return;

    let textToCopy = `=== ${topic.title} (#${topic.slNo} - ${topic.category}) ===\n\n`;
    textToCopy += `KEY POINTERS:\n`;
    topic.pointers.forEach(p => {
      textToCopy += `• ${p.replace(/<[^>]+>/g, '')}\n`;
    });
    textToCopy += `\nCOMPREHENSIVE NOTES:\n${topic.fullNotes}\n\n[Source: Complete History of India Revision Hub]`;

    navigator.clipboard.writeText(textToCopy).then(() => {
      showToast(`Copied "${topic.title}" pointer notes to clipboard!`);
    }).catch(err => {
      console.warn('Clipboard write error', err);
    });
  }

  function copyAllVisibleNotes() {
    const visibleTopics = getFilteredTopics();
    if (visibleTopics.length === 0) return;

    let fullBundle = `=== ANCIENT INDIAN HISTORY MASTER QUICK REVISION NOTES ===\n`;
    fullBundle += `Total Modules: ${visibleTopics.length}\n`;
    fullBundle += `Category: ${activeCategory}\n\n`;

    visibleTopics.forEach(t => {
      fullBundle += `--------------------------------------------------------\n`;
      fullBundle += `TOPIC #${t.slNo}: ${t.title} [${t.category}]\n`;
      fullBundle += `--------------------------------------------------------\n`;
      fullBundle += `KEY REVISION POINTERS:\n`;
      t.pointers.forEach(p => {
        fullBundle += `• ${p.replace(/<[^>]+>/g, '')}\n`;
      });
      fullBundle += `\n`;
    });

    navigator.clipboard.writeText(fullBundle).then(() => {
      showToast(`Copied ${visibleTopics.length} topic revision notes to clipboard!`);
    }).catch(err => {
      console.warn('Clipboard write error', err);
    });
  }

  function showToast(msg) {
    let toast = document.getElementById('revToast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'revToast';
      toast.className = 'rev-toast';
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.classList.add('visible');
    setTimeout(() => {
      toast.classList.remove('visible');
    }, 2800);
  }

  function openLightbox(src, caption) {
    let lb = document.getElementById('revLightbox');
    if (!lb) {
      lb = document.createElement('div');
      lb.id = 'revLightbox';
      lb.className = 'rev-lightbox';
      lb.innerHTML = `
        <div class="rev-lb-backdrop" onclick="HistoryRevision.closeLightbox()"></div>
        <div class="rev-lb-content">
          <button class="rev-lb-close" onclick="HistoryRevision.closeLightbox()">&times;</button>
          <img id="revLbImg" src="" alt="">
          <p id="revLbCaption"></p>
        </div>
      `;
      document.body.appendChild(lb);
    }
    document.getElementById('revLbImg').src = src;
    document.getElementById('revLbCaption').textContent = caption;
    lb.classList.add('visible');
  }

  function closeLightbox() {
    const lb = document.getElementById('revLightbox');
    if (lb) lb.classList.remove('visible');
  }

  function resetFilters() {
    activeCategory = 'all';
    searchQuery = '';
    bookmarkedOnly = false;
    const input = document.getElementById('revisionSearchInput');
    if (input) input.value = '';
    const bookmarkBtn = document.getElementById('toggleBookmarksBtn');
    if (bookmarkBtn) {
      bookmarkBtn.classList.remove('active');
      bookmarkBtn.innerHTML = '☆ Show Starred Only';
    }
    renderCategoryFilters();
    render();
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  return {
    init,
    resetFilters,
    openLightbox,
    closeLightbox
  };
})();
