/**
 * NADF Modern Learning Shell — LNK Benchmark Alignment
 * Implements the Docked Right Glossary Aside matching:
 * https://cwarloe.github.io/learning-narrative-kit/itm310-vanguard-edge/
 */

(function () {
  let selectedId = null;
  let activeFilter = 'all';
  let searchQuery = '';

  function mountLnkGlossaryAside() {
    const content = document.querySelector('.content');
    if (!content) return;

    // Create or locate the aside
    let aside = document.getElementById('lnk-glossary-aside');
    if (!aside) {
      aside = document.createElement('aside');
      aside.id = 'lnk-glossary-aside';
      aside.innerHTML = `
        <h3>Glossary</h3>
        <div class="sidebar-meta" id="term-count">Loading terms…</div>
        <div class="filter-bar" role="group" aria-label="Category filter">
          <button type="button" class="filter-btn active" data-cat="all">All</button>
          <button type="button" class="filter-btn" data-cat="telemetry">Telemetry</button>
          <button type="button" class="filter-btn" data-cat="transport">Transport</button>
          <button type="button" class="filter-btn" data-cat="application">App</button>
        </div>
        <input type="text" id="search-box" placeholder="Filter terms…" autocomplete="off">
        <div class="term-list" id="term-list"></div>
        <div class="detail-panel empty" id="detail-panel">Select a term to see definition and context.</div>
      `;
      content.appendChild(aside);

      // Event listeners for filter bar
      aside.querySelectorAll('.filter-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
          aside.querySelectorAll('.filter-btn').forEach(function (b) { b.classList.remove('active'); });
          btn.classList.add('active');
          activeFilter = btn.getAttribute('data-cat');
          renderGlossaryList();
        });
      });

      // Search box listener
      const searchInput = aside.querySelector('#search-box');
      searchInput.addEventListener('input', function (e) {
        searchQuery = (e.target.value || '').trim().toLowerCase();
        renderGlossaryList();
      });
    }

    renderGlossaryList();
    bindInStoryTermClicks();
  }

  function renderGlossaryList() {
    const termList = document.getElementById('term-list');
    const termCount = document.getElementById('term-count');
    if (!termList || !termCount) return;

    const glossary = window.__GLOSSARY__ || {};
    const keys = Object.keys(glossary);
    if (keys.length === 0) return;

    const filtered = keys.filter(function (k) {
      const item = glossary[k];
      const catMatch = (activeFilter === 'all') || (item.category === activeFilter);
      const textMatch = !searchQuery ||
        (item.title && item.title.toLowerCase().includes(searchQuery)) ||
        (item.definition && item.definition.toLowerCase().includes(searchQuery)) ||
        (k.toLowerCase().includes(searchQuery));
      return catMatch && textMatch;
    }).sort(function (a, b) {
      return (glossary[a].title || a).localeCompare(glossary[b].title || b);
    });

    termCount.textContent = `Showing ${filtered.length} of ${keys.length} terms`;

    if (filtered.length === 0) {
      termList.innerHTML = '<div style="padding: 1.25rem; color: #94a3b8; font-size: 0.82rem; text-align: center;">No matching terms found.</div>';
      return;
    }

    let html = '';
    filtered.forEach(function (k) {
      const item = glossary[k];
      const isSelected = selectedId === k;
      const cat = item.category || 'telemetry';
      html += `
        <div class="term-item ${isSelected ? 'selected' : ''}" data-id="${k}">
          <span>${item.title || k}</span>
          <span class="badge ${cat}">${cat}</span>
        </div>
      `;
    });
    termList.innerHTML = html;

    // Attach click events to term items
    termList.querySelectorAll('.term-item').forEach(function (el) {
      el.addEventListener('click', function () {
        const id = el.getAttribute('data-id');
        selectTerm(id, true);
      });
    });
  }

  function selectTerm(id, scrollToStory) {
    selectedId = id;
    const glossary = window.__GLOSSARY__ || {};
    const item = glossary[id];
    if (!item) return;

    // Update active highlight in the aside term list
    document.querySelectorAll('.term-item').forEach(function (el) {
      el.classList.toggle('selected', el.getAttribute('data-id') === id);
    });

    // Update Detail Panel at the bottom of the aside
    const detailPanel = document.getElementById('detail-panel');
    if (detailPanel) {
      detailPanel.className = 'detail-panel';
      const cat = item.category || 'telemetry';
      detailPanel.innerHTML = `
        <div class="d-tier ${cat}">${cat.toUpperCase()}</div>
        <div class="d-title">${item.title || id}</div>
        <div class="d-def">${item.definition || ''}</div>
        ${item.context ? `<div class="d-context">${item.context}</div>` : ''}
      `;
    }

    // Bidirectional sync: smooth scroll into story and flash amber
    if (scrollToStory) {
      const targetEl = document.getElementById(`term-${id}`) || document.querySelector(`.term[data-term="${id}"]`);
      if (targetEl) {
        targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
        targetEl.classList.remove('flash', 'story-highlight');
        void targetEl.offsetWidth; // Force reflow
        targetEl.classList.add('flash');
        setTimeout(function () {
          targetEl.classList.remove('flash');
        }, 1400);
      }
    }
  }

  function bindInStoryTermClicks() {
    // When the user clicks an in-text term in the narrative, sync to the aside
    document.querySelectorAll('.term').forEach(function (el) {
      el.addEventListener('click', function () {
        const id = el.getAttribute('data-term');
        selectTerm(id, false);

        // On mobile, smoothly glide down to the glossary aside so the user sees the definition
        if (window.innerWidth < 1100) {
          const detailPanel = document.getElementById('detail-panel');
          if (detailPanel) {
            detailPanel.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }
      });
    });
  }

  // Hook into Docsify
  window.$docsify = window.$docsify || {};
  window.$docsify.plugins = (window.$docsify.plugins || []).concat([
    function (hook) {
      hook.doneEach(function () {
        // Mount aside once content is rendered
        mountLnkGlossaryAside();

        // If glossary.json was still in flight on first mount, poll briefly until loaded
        if (!window.__GLOSSARY__ || Object.keys(window.__GLOSSARY__).length === 0) {
          let attempts = 0;
          const interval = setInterval(function () {
            attempts++;
            if (window.__GLOSSARY__ && Object.keys(window.__GLOSSARY__).length > 0) {
              clearInterval(interval);
              renderGlossaryList();
            } else if (attempts > 30) {
              clearInterval(interval);
            }
          }, 100);
        }
      });
    }
  ]);
})();
