/**
 * NADF Modern Learning Shell
 * Provides page mode auto-detection, Slide-Over Glossary Drawer, and Interactive Enhancements
 */

(function () {
  // 1. Page Mode Detection (Narrative vs Lesson vs Guide)
  function updatePageMode() {
    const hash = window.location.hash || '';
    const body = document.body;
    body.classList.remove('mode-narrative', 'mode-lesson', 'mode-guide');

    if (hash.includes('/narrative/')) {
      body.classList.add('mode-narrative');
    } else if (hash.includes('/lessons/')) {
      body.classList.add('mode-lesson');
    } else {
      body.classList.add('mode-guide');
    }
  }

  window.addEventListener('hashchange', updatePageMode);
  document.addEventListener('DOMContentLoaded', updatePageMode);

  // 2. Build Slide-Over Glossary Drawer
  function initGlossaryDrawer() {
    // Avoid double initialization
    if (document.getElementById('glossary-drawer')) return;

    // Toggle button
    const toggleBtn = document.createElement('button');
    toggleBtn.id = 'drawer-toggle-btn';
    toggleBtn.innerHTML = '<span>📚</span><span>Glossary</span>';
    toggleBtn.title = 'Open Master Glossary Drawer';
    document.body.appendChild(toggleBtn);

    // Backdrop
    const backdrop = document.createElement('div');
    backdrop.id = 'glossary-backdrop';
    document.body.appendChild(backdrop);

    // Drawer container
    const drawer = document.createElement('div');
    drawer.id = 'glossary-drawer';
    drawer.innerHTML = `
      <div class="drawer-header">
        <div class="drawer-title">
          <span>📚</span>
          <span>Master Glossary</span>
        </div>
        <button class="drawer-close" id="drawer-close-btn">&times;</button>
      </div>
      <div class="drawer-search-wrap">
        <input type="text" id="drawer-search" placeholder="Filter terms or concepts..." autocomplete="off">
      </div>
      <div class="drawer-categories" id="drawer-cats">
        <button class="drawer-cat-pill active" data-cat="all">All</button>
        <button class="drawer-cat-pill" data-cat="telemetry">Telemetry</button>
        <button class="drawer-cat-pill" data-cat="transport">Transport</button>
        <button class="drawer-cat-pill" data-cat="dns">DNS</button>
        <button class="drawer-cat-pill" data-cat="encryption">Encryption</button>
        <button class="drawer-cat-pill" data-cat="application">Application</button>
        <button class="drawer-cat-pill" data-cat="failures">Failures</button>
        <button class="drawer-cat-pill" data-cat="investigation">Investigation</button>
        <button class="drawer-cat-pill" data-cat="judgment">Judgment</button>
      </div>
      <div class="drawer-term-list" id="drawer-terms"></div>
      <div class="drawer-detail-panel" id="drawer-detail" style="display: none;">
        <div class="drawer-detail-title" id="dd-title"></div>
        <div class="drawer-detail-def" id="dd-def"></div>
        <div class="drawer-detail-ctx" id="dd-ctx"></div>
        <button class="drawer-jump-btn" id="dd-jump">Jump to In-Story Passage ↑</button>
      </div>
    `;
    document.body.appendChild(drawer);

    // State
    let selectedCat = 'all';
    let searchQuery = '';
    let selectedTermId = null;

    function openDrawer() {
      drawer.classList.add('open');
      backdrop.classList.add('open');
      document.getElementById('drawer-search').focus();
    }

    function closeDrawer() {
      drawer.classList.remove('open');
      backdrop.classList.remove('open');
    }

    toggleBtn.addEventListener('click', openDrawer);
    document.getElementById('drawer-close-btn').addEventListener('click', closeDrawer);
    backdrop.addEventListener('click', closeDrawer);

    // Render terms list
    function renderDrawerTerms() {
      const container = document.getElementById('drawer-terms');
      const glossary = window.__GLOSSARY__ || {};
      const keys = Object.keys(glossary);

      const filtered = keys.filter(function (k) {
        const item = glossary[k];
        const matchesCat = (selectedCat === 'all') || (item.category === selectedCat);
        const query = searchQuery.toLowerCase();
        const matchesQuery = !query ||
          (item.title && item.title.toLowerCase().includes(query)) ||
          (item.definition && item.definition.toLowerCase().includes(query));
        return matchesCat && matchesQuery;
      }).sort(function (a, b) {
        return (glossary[a].title || a).localeCompare(glossary[b].title || b);
      });

      if (filtered.length === 0) {
        container.innerHTML = '<div style="padding: 1.5rem; color: #94a3b8; font-size: 0.88rem; text-align: center;">No matching terms found.</div>';
        return;
      }

      let html = '';
      filtered.forEach(function (k) {
        const item = glossary[k];
        const isSelected = selectedTermId === k;
        html += `
          <div class="drawer-term-item ${isSelected ? 'selected' : ''}" data-id="${k}">
            <span class="drawer-term-name">${item.title || k}</span>
            <span class="drawer-term-cat">${item.category || 'term'}</span>
          </div>
        `;
      });
      container.innerHTML = html;

      // Bind selection clicks
      container.querySelectorAll('.drawer-term-item').forEach(function (el) {
        el.addEventListener('click', function () {
          selectDrawerTerm(el.getAttribute('data-id'));
        });
      });
    }

    function selectDrawerTerm(id) {
      selectedTermId = id;
      const glossary = window.__GLOSSARY__ || {};
      const item = glossary[id];
      if (!item) return;

      document.querySelectorAll('.drawer-term-item').forEach(function (el) {
        el.classList.toggle('selected', el.getAttribute('data-id') === id);
      });

      const detail = document.getElementById('drawer-detail');
      document.getElementById('dd-title').textContent = item.title || id;
      document.getElementById('dd-def').textContent = item.definition || '';

      const ctxEl = document.getElementById('dd-ctx');
      if (item.context) {
        ctxEl.textContent = item.context;
        ctxEl.style.display = 'block';
      } else {
        ctxEl.style.display = 'none';
      }

      const jumpBtn = document.getElementById('dd-jump');
      const targetEl = document.getElementById(`term-${id}`) || document.querySelector(`.term[data-term="${id}"]`);
      if (targetEl) {
        jumpBtn.style.display = 'inline-block';
        jumpBtn.onclick = function () {
          closeDrawer();
          targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
          targetEl.classList.remove('flash');
          void targetEl.offsetWidth;
          targetEl.classList.add('flash');
          setTimeout(function () {
            targetEl.classList.remove('flash');
          }, 1400);
        };
      } else {
        jumpBtn.style.display = 'none';
      }

      detail.style.display = 'block';
    }

    // Category pills filter
    document.querySelectorAll('.drawer-cat-pill').forEach(function (btn) {
      btn.addEventListener('click', function () {
        document.querySelectorAll('.drawer-cat-pill').forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        selectedCat = btn.getAttribute('data-cat');
        renderDrawerTerms();
      });
    });

    // Search input
    document.getElementById('drawer-search').addEventListener('input', function (e) {
      searchQuery = e.target.value.trim();
      renderDrawerTerms();
    });

    // Initial render when glossary is loaded
    function checkGlossaryLoaded() {
      if (window.__GLOSSARY__ && Object.keys(window.__GLOSSARY__).length > 0) {
        renderDrawerTerms();
      } else {
        setTimeout(checkGlossaryLoaded, 100);
      }
    }
    checkGlossaryLoaded();
  }

  // Hook into Docsify
  window.$docsify = window.$docsify || {};
  window.$docsify.plugins = (window.$docsify.plugins || []).concat([
    function (hook) {
      hook.init(function () {
        updatePageMode();
      });

      hook.doneEach(function () {
        updatePageMode();
        initGlossaryDrawer();
      });
    }
  ]);
})();
