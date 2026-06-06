(function () {
  "use strict";

  const els = {
    catalog: document.getElementById("catalog"),
    status: document.getElementById("overviewStatus"),
    search: document.getElementById("searchInput"),
    role: document.getElementById("roleFilter"),
    family: document.getElementById("familyFilter")
  };

  const state = {
    categories: [],
    datasets: []
  };

  function escapeHtml(value) {
    return String(value ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function inlineHtml(value) {
    return String(value ?? "")
      .split(/(\*\*[^*]+\*\*)/g)
      .map((part) => {
        if (part.startsWith("**") && part.endsWith("**") && part.length > 4) {
          return `<strong>${escapeHtml(part.slice(2, -2))}</strong>`;
        }
        return escapeHtml(part);
      })
      .join("");
  }

  function uniqueSorted(values) {
    return Array.from(new Set(values.filter(Boolean))).sort((a, b) => a.localeCompare(b));
  }

  function normalizeList(value) {
    return Array.isArray(value) ? value : [];
  }

  async function fetchJson(path) {
    const response = await fetch(path);
    if (!response.ok) {
      throw new Error(`Failed to load ${path}: ${response.status}`);
    }
    return response.json();
  }

  async function load() {
    const manifest = await fetchJson("data/index.json");
    const categories = normalizeList(manifest.groups);
    const datasets = [];

    for (const category of categories) {
      for (const entry of normalizeList(category.datasets)) {
        const spec = await fetchJson(entry.path);
        datasets.push({
          categoryId: category.id,
          categoryName: category.name,
          manifest: entry,
          spec
        });
      }
    }

    state.categories = categories;
    state.datasets = datasets;
    populateFilters();
    render();
  }

  function populateFilters() {
    const roles = uniqueSorted(state.datasets.flatMap((item) => normalizeList(item.spec.roleFocus)));
    const families = uniqueSorted(state.datasets.map((item) => item.spec.competency && item.spec.competency.family));

    for (const role of roles) {
      els.role.insertAdjacentHTML("beforeend", `<option value="${escapeHtml(role)}">${escapeHtml(role)}</option>`);
    }
    for (const family of families) {
      els.family.insertAdjacentHTML("beforeend", `<option value="${escapeHtml(family)}">${escapeHtml(family)}</option>`);
    }
  }

  function datasetText(item) {
    const spec = item.spec;
    const signals = normalizeList(spec.evaluation && spec.evaluation.signals).map((signal) => signal.name).join(" ");
    const prompts = [spec.prompt && spec.prompt.primary].concat(normalizeList(spec.prompt && spec.prompt.variants)).join(" ");
    return [
      spec.title,
      spec.description,
      spec.difficulty,
      spec.competency && spec.competency.name,
      spec.competency && spec.competency.family,
      normalizeList(spec.roleFocus).join(" "),
      signals,
      prompts
    ].join(" ").toLowerCase();
  }

  function getFilteredDatasets() {
    const search = els.search.value.trim().toLowerCase();
    const role = els.role.value;
    const family = els.family.value;

    return state.datasets.filter((item) => {
      const spec = item.spec;
      if (role && !normalizeList(spec.roleFocus).includes(role)) {
        return false;
      }
      if (family && (!spec.competency || spec.competency.family !== family)) {
        return false;
      }
      if (search && !datasetText(item).includes(search)) {
        return false;
      }
      return true;
    });
  }

  function renderSignalChips(spec) {
    return normalizeList(spec.evaluation && spec.evaluation.signals)
      .slice(0, 3)
      .map((signal) => `<span class="chip signal-chip">${escapeHtml(signal.name)}</span>`)
      .join("");
  }

  function datasetBasePath(item) {
    const path = item.manifest.path || "";
    const slash = path.lastIndexOf("/");
    return slash >= 0 ? path.slice(0, slash + 1) : "";
  }

  function assetUrl(item, path) {
    if (!path || typeof path !== "string") {
      return "";
    }
    if (/^(https?:)?\/\//.test(path) || path.startsWith("/") || path.startsWith("data:")) {
      return path;
    }
    return datasetBasePath(item) + path;
  }

  function iconUrl(item) {
    const spec = item.spec || {};
    if (spec.assets && spec.assets.icon) {
      return assetUrl(item, spec.assets.icon);
    }
    return datasetBasePath(item) + "icon.png";
  }

  function renderCard(item) {
    const spec = item.spec;
    const id = item.manifest.id || spec.id;
    const icon = iconUrl(item);
    const roleChips = normalizeList(spec.roleFocus)
      .map((role) => `<span class="chip">${escapeHtml(role)}</span>`)
      .join("");
    const prompt = spec.prompt && spec.prompt.primary ? spec.prompt.primary : "No prompt defined.";

    return `
      <a class="case-card" href="explorer.html#${encodeURIComponent(id)}" aria-label="Open ${escapeHtml(spec.title)} explorer">
        <img class="case-icon" src="${escapeHtml(icon)}" alt="" loading="lazy" onerror="this.hidden=true">
        <div class="card-topline">
          <span>${escapeHtml(spec.competency && spec.competency.family)}</span>
          <span>${escapeHtml(spec.difficulty || "standard")}</span>
        </div>
        <h3>${escapeHtml(spec.title)}</h3>
        <p>${inlineHtml(spec.description)}</p>
        <blockquote>${inlineHtml(prompt)}</blockquote>
        <div class="chip-row">${roleChips}</div>
        <div class="chip-row">${renderSignalChips(spec)}</div>
      </a>
    `;
  }

  function render() {
    const filtered = getFilteredDatasets();
    const byCategory = new Map();
    for (const item of filtered) {
      if (!byCategory.has(item.categoryId)) {
        byCategory.set(item.categoryId, []);
      }
      byCategory.get(item.categoryId).push(item);
    }

    els.status.textContent = `${filtered.length} interview${filtered.length === 1 ? "" : "s"}`;

    if (!filtered.length) {
      els.catalog.innerHTML = '<section class="empty-state">No interviews match the current filters.</section>';
      return;
    }

    els.catalog.innerHTML = state.categories
      .filter((category) => byCategory.has(category.id))
      .map((category) => `
        <section class="catalog-section">
          <div class="section-heading">
            <h2>${escapeHtml(category.name)}</h2>
            <span>${byCategory.get(category.id).length} item${byCategory.get(category.id).length === 1 ? "" : "s"}</span>
          </div>
          <div class="card-grid">
            ${byCategory.get(category.id).map(renderCard).join("")}
          </div>
        </section>
      `)
      .join("");
  }

  for (const element of [els.search, els.role, els.family]) {
    element.addEventListener("input", render);
  }

  load().catch((error) => {
    els.status.textContent = error.message;
    els.status.classList.add("error");
  });
})();
