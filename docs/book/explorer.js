(function () {
  "use strict";

  const STORY_FIELDS = [
    ["situation", "Situation"],
    ["task", "Task"],
    ["action", "Action"],
    ["result", "Result"],
    ["reflection", "Reflection"],
    ["systemChange", "System Change"]
  ];
  const STORY_LABELS = new Map(STORY_FIELDS);

  const els = {
    title: document.getElementById("pageTitle"),
    icon: document.getElementById("pageIcon"),
    meta: document.getElementById("datasetMeta"),
    nav: document.getElementById("sectionNav"),
    status: document.getElementById("explorerStatus"),
    content: document.getElementById("content")
  };

  const state = {
    manifest: null,
    datasets: new Map(),
    currentId: null,
    currentEntry: null,
    currentSection: "brief",
    spec: null
  };

  const sections = [
    { id: "brief", label: "Competency Brief", render: renderBrief },
    { id: "visual-summary", label: "Visual Summary", render: renderVisualSummary },
    { id: "story", label: "Story Anatomy", render: renderStory },
    { id: "examples", label: "Concrete Examples", render: renderExampleStories },
    { id: "answer-contrast", label: "Answer Contrast", render: renderAnswerContrast },
    { id: "follow-ups", label: "Follow-Up Probes", render: renderFollowUps },
    { id: "evaluation", label: "Evaluation Rubric", render: renderEvaluation },
    { id: "practice", label: "Practice Template", render: renderPractice },
    { id: "related", label: "Related Scenarios", render: renderRelated },
    { id: "to-probe-further", label: "To Probe Further", render: renderToProbeFurther }
  ];
  const sectionAliases = new Map([
    ["prompt", "brief"],
    ["strong", "answer-contrast"],
    ["weak", "answer-contrast"]
  ]);

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

  function normalizeList(value) {
    return Array.isArray(value) ? value : [];
  }

  function renderList(values) {
    const items = normalizeList(values);
    if (!items.length) {
      return "";
    }
    return `<ul>${items.map((item) => `<li>${inlineHtml(item)}</li>`).join("")}</ul>`;
  }

  function renderChips(values, className) {
    return normalizeList(values)
      .map((value) => `<span class="chip ${className || ""}">${escapeHtml(value)}</span>`)
      .join("");
  }

  function getSectionId(id) {
    return sectionAliases.get(id) || id;
  }

  function getStoryFields(spec) {
    const configured = normalizeList(spec.visualizations && spec.visualizations.timeline)
      .filter((field) => STORY_LABELS.has(field));
    if (configured.length) {
      return configured.map((field) => [field, STORY_LABELS.get(field)]);
    }
    return STORY_FIELDS;
  }

  function getSignalsById(spec) {
    const signals = new Map();
    for (const signal of normalizeList(spec.evaluation && spec.evaluation.signals)) {
      signals.set(signal.id, signal);
    }
    return signals;
  }

  function orderedFollowUps(spec) {
    const probes = normalizeList(spec.followUps);
    const byId = new Map(probes.map((probe) => [probe.id, probe]));
    const ordered = [];
    const seen = new Set();

    for (const id of normalizeList(spec.visualizations && spec.visualizations.followUpTree)) {
      if (byId.has(id)) {
        ordered.push(byId.get(id));
        seen.add(id);
      }
    }
    for (const probe of probes) {
      if (!seen.has(probe.id)) {
        ordered.push(probe);
      }
    }
    return ordered;
  }

  function renderSignalMap(spec) {
    const signals = getSignalsById(spec);
    const ids = normalizeList(spec.visualizations && spec.visualizations.signalMap);
    if (!ids.length) {
      return '<p class="muted-note">No signal map configured.</p>';
    }
    return `
      <div class="signal-map" aria-label="Signal map">
        ${ids.map((id, index) => {
          const signal = signals.get(id);
          return `
            <article>
              <span>${index + 1}</span>
              <h3>${escapeHtml(signal ? signal.name : id)}</h3>
              ${signal ? renderSignalEvidencePair(signal) : `<p>${escapeHtml("No signal description found.")}</p>`}
            </article>
          `;
        }).join("")}
      </div>
    `;
  }

  function datasetBasePath() {
    const path = state.currentEntry && state.currentEntry.path ? state.currentEntry.path : "";
    const slash = path.lastIndexOf("/");
    return slash >= 0 ? path.slice(0, slash + 1) : "";
  }

  function assetUrl(path) {
    if (!path || typeof path !== "string") {
      return "";
    }
    if (/^(https?:)?\/\//.test(path) || path.startsWith("/") || path.startsWith("data:")) {
      return path;
    }
    return datasetBasePath() + path;
  }

  function interviewIconUrl(spec) {
    if (spec.assets && spec.assets.icon) {
      return assetUrl(spec.assets.icon);
    }
    return assetUrl("icon.png");
  }

  function updateHeaderIcon(spec) {
    if (!els.icon) {
      return;
    }
    const icon = interviewIconUrl(spec);
    els.icon.hidden = true;
    if (!icon) {
      els.icon.removeAttribute("src");
      els.icon.removeAttribute("data-src");
      return;
    }
    if (els.icon.dataset.src !== icon) {
      els.icon.dataset.src = icon;
      els.icon.src = icon;
    }
    if (els.icon.complete) {
      els.icon.hidden = els.icon.naturalWidth === 0;
    }
  }

  function renderOptionalImage(path, alt, className) {
    const url = assetUrl(path);
    if (!url) {
      return "";
    }
    return `
      <a class="visual-link" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" title="Open image in a new tab">
        <img class="${escapeHtml(className || "section-visual")}" src="${escapeHtml(url)}" alt="${escapeHtml(alt)}" loading="lazy">
      </a>
    `;
  }

  function renderSignalEvidencePair(signal) {
    const strongImage = renderOptionalImage(signal.strongAiVisual, `${signal.name} strong signal visual`, "signal-visual");
    const weakImage = renderOptionalImage(signal.weakAiVisual, `${signal.name} weak signal visual`, "signal-visual");
    return `
      <div class="signal-evidence-pair">
        <div class="signal-evidence-block strong-signal-evidence">
          <p><strong>Strong:</strong> ${inlineHtml(signal.strong)}</p>
          ${strongImage}
        </div>
        <div class="signal-evidence-block weak-signal-evidence">
          <p><strong>Weak:</strong> ${inlineHtml(signal.weak)}</p>
          ${weakImage}
        </div>
      </div>
    `;
  }

  function probeFurtherLinks(payload) {
    if (!payload) {
      return [];
    }
    if (Array.isArray(payload)) {
      return payload.flatMap((group) => {
        if (!group || typeof group !== "object") {
          return [];
        }
        return normalizeList(group.links).map((link) => ({
          ...link,
          group: link.group || group.group || group.title || "Further Reading",
          groupDescription: link.groupDescription || group.description || ""
        }));
      });
    }
    if (typeof payload === "object") {
      return normalizeList(payload.links);
    }
    return [];
  }

  function probeFurtherGroups(payload) {
    const groups = new Map();
    const order = [];
    for (const link of probeFurtherLinks(payload)) {
      if (!link || typeof link !== "object") {
        continue;
      }
      const name = link.group || "Further Reading";
      if (!groups.has(name)) {
        groups.set(name, {
          name,
          description: link.groupDescription || "",
          links: []
        });
        order.push(name);
      }
      const group = groups.get(name);
      if (!group.description && link.groupDescription) {
        group.description = link.groupDescription;
      }
      group.links.push(link);
    }
    return order.map((name) => groups.get(name)).filter((group) => group.links.length);
  }

  function renderProbeFurtherLinkList(links, compact) {
    const items = normalizeList(links);
    if (!items.length) {
      return "";
    }
    return `
      <ul class="probe-links ${compact ? "compact-probe-links" : ""}">
        ${items.map((item) => {
          const title = item.title || item.name || item.url || "Resource";
          const meta = [item.source, item.type, item.year]
            .map((part) => String(part || "").trim())
            .filter(Boolean)
            .join(" / ");
          return `
            <li class="probe-link-item">
              <a class="probe-link-title" href="${escapeHtml(item.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(title)}</a>
              ${meta ? `<span class="probe-link-meta">${escapeHtml(meta)}</span>` : ""}
              ${item.why ? `<p class="probe-link-why">${inlineHtml(item.why)}</p>` : ""}
            </li>
          `;
        }).join("")}
      </ul>
    `;
  }

  async function fetchJson(path) {
    const response = await fetch(path);
    if (!response.ok) {
      throw new Error(`Failed to load ${path}: ${response.status}`);
    }
    return response.json();
  }

  async function loadManifest() {
    state.manifest = await fetchJson("data/index.json");
    for (const category of normalizeList(state.manifest.groups)) {
      for (const entry of normalizeList(category.datasets)) {
        state.datasets.set(entry.id, { category, entry });
      }
    }
  }

  function parseHash() {
    const raw = decodeURIComponent(window.location.hash.replace(/^#/, ""));
    const [id, rawSection] = raw.split("/");
    const section = getSectionId(rawSection || "brief");
    const firstId = state.datasets.keys().next().value;
    return {
      id: id || firstId,
      section
    };
  }

  async function loadCurrentSpec() {
    const parsed = parseHash();
    const item = state.datasets.get(parsed.id);
    if (!item) {
      throw new Error(`Unknown interview id: ${parsed.id}`);
    }
    state.currentId = parsed.id;
    state.currentEntry = item.entry;
    state.currentSection = sections.some((section) => section.id === parsed.section) ? parsed.section : "brief";
    state.spec = await fetchJson(item.entry.path);
  }

  function updateHash(sectionId) {
    const nextHash = `#${encodeURIComponent(state.currentId)}/${encodeURIComponent(sectionId)}`;
    if (window.location.hash !== nextHash) {
      window.location.hash = nextHash;
    } else {
      state.currentSection = sectionId;
      render();
    }
  }

  function renderMeta() {
    const spec = state.spec;
    els.title.textContent = spec.title;
    updateHeaderIcon(spec);
    els.meta.innerHTML = `
      <p>${inlineHtml(spec.description)}</p>
      <div class="chip-row">${renderChips(spec.roleFocus)}</div>
      <div class="chip-row">
        <span class="chip family-chip">${escapeHtml(spec.competency && spec.competency.family)}</span>
        <span class="chip">${escapeHtml(spec.difficulty || "standard")}</span>
      </div>
    `;
  }

  function renderNav() {
    els.nav.innerHTML = sections
      .map((section, index) => `
        <button type="button" class="${section.id === state.currentSection ? "active" : ""}" data-section="${section.id}">
          <span>${index + 1}</span>
          ${escapeHtml(section.label)}
        </button>
      `)
      .join("");

    els.nav.querySelectorAll("button").forEach((button) => {
      button.addEventListener("click", () => updateHash(button.dataset.section));
    });
  }

  function renderBrief(spec) {
    const competency = spec.competency || {};
    const prompt = spec.prompt || {};
    const intent = normalizeList(spec.prompt && spec.prompt.interviewerIntent);
    return `
      <section class="content-section">
        <p class="eyebrow">${escapeHtml(competency.family)}</p>
        <h2>${escapeHtml(competency.name || spec.title)}</h2>
        <p class="lead">${inlineHtml(competency.definition)}</p>
        <div class="info-grid">
          <div>
            <h3>Why It Matters</h3>
            <p>${inlineHtml(competency.whyItMatters)}</p>
          </div>
          <div>
            <h3>Interviewer Intent</h3>
            ${renderList(intent)}
          </div>
        </div>
        <h3>Prompt</h3>
        <blockquote class="large-quote">${inlineHtml(prompt.primary)}</blockquote>
        <h3>Prompt Variants</h3>
        ${renderList(prompt.variants)}
      </section>
    `;
  }

  function renderVisualSummary(spec) {
    const comic = spec.explainerComic;
    const image = renderOptionalImage(comic, `${spec.title} visual summary`, "hero-visual");
    return `
      <section class="content-section">
        <h2>Visual Summary</h2>
        ${image || '<p class="muted-note">No explainer visual has been generated for this interview yet.</p>'}
      </section>
    `;
  }

  function storyValueHtml(value) {
    if (Array.isArray(value)) {
      return renderList(value);
    }
    return `<p>${inlineHtml(value)}</p>`;
  }

  function renderStory(spec) {
    const story = spec.storyAnatomy || {};
    const scenario = spec.scenario || {};
    const timeline = getStoryFields(spec).map(([field, label], index) => `
      <article class="timeline-step">
        <span>${index + 1}</span>
        <h3>${escapeHtml(label)}</h3>
        ${storyValueHtml(story[field])}
      </article>
    `).join("");

    return `
      <section class="content-section">
        <h2>Story Anatomy</h2>
        <p class="lead">${inlineHtml(scenario.signatureExample || "")}</p>
        <div class="scenario-grid">
          <div>
            <h3>Context</h3>
            ${renderList(scenario.context)}
          </div>
          <div>
            <h3>Constraints</h3>
            ${renderList(scenario.constraints)}
          </div>
        </div>
        <div class="timeline">${timeline}</div>
      </section>
    `;
  }

  function renderAnswerContrast(spec) {
    const strong = spec.strongAnswerPattern || {};
    const weak = spec.weakAnswerPattern || {};
    return `
      <section class="content-section">
        <h2>Answer Contrast</h2>
        <div class="contrast-grid">
          <article class="contrast-column strong-column">
            <h3>Strong Pattern</h3>
            <p>${inlineHtml(strong.summary)}</p>
            ${renderOptionalImage(strong.aiVisual, `${spec.title} strong answer pattern visual`, "pattern-visual")}
            <div class="move-list compact-list">
              ${normalizeList(strong.moves).map((move, index) => `
                <article>
                  <span>${index + 1}</span>
                  <p>${inlineHtml(move)}</p>
                </article>
              `).join("")}
            </div>
          </article>
          <article class="contrast-column weak-column">
            <h3>Weak Pattern</h3>
            <p>${inlineHtml(weak.summary)}</p>
            ${renderOptionalImage(weak.aiVisual, `${spec.title} weak answer pattern visual`, "pattern-visual")}
            <div class="red-flag-list">
              ${normalizeList(weak.redFlags).map((flag) => `<p>${inlineHtml(flag)}</p>`).join("")}
            </div>
          </article>
        </div>
        <h3>Signals To Listen For</h3>
        ${renderSignalMap(spec)}
      </section>
    `;
  }

  function renderExampleStories(spec) {
    const examples = normalizeList(spec.exampleStories);
    if (!examples.length) {
      return `
        <section class="content-section">
          <h2>Concrete Examples</h2>
          <p class="muted-note">No concrete examples have been added for this interview yet.</p>
        </section>
      `;
    }

    return `
      <section class="content-section">
        <h2>Concrete Examples</h2>
        <p class="lead">Use these as concrete story shapes, not scripts to memorize. The useful part is the decision pattern and the follow-up surface.</p>
        <div class="example-grid">
          ${examples.map((example) => `
            <article class="example-card">
              <div class="card-topline">
                <span>${escapeHtml(example.level)}</span>
                <span>${escapeHtml(example.id)}</span>
              </div>
              <h3>${escapeHtml(example.title)}</h3>
              <blockquote>${inlineHtml(example.promptVariant)}</blockquote>
              ${renderOptionalImage(example.aiVisual, `${example.title} example visual`, "example-visual")}
              <div class="example-block">
                <h4>Situation</h4>
                <p>${inlineHtml(example.situation)}</p>
              </div>
              <div class="example-block">
                <h4>Strong Answer Sketch</h4>
                ${renderList(example.strongAnswerSketch)}
              </div>
              <div class="example-block">
                <h4>Why It Works</h4>
                ${renderList(example.whyItWorks)}
              </div>
              <div class="weak-example">
                <h4>Weak Version</h4>
                <p>${inlineHtml(example.weakVersion)}</p>
              </div>
              <div class="example-block">
                <h4>Likely Follow-Ups</h4>
                ${renderList(example.followUpAngles)}
              </div>
            </article>
          `).join("")}
        </div>
      </section>
    `;
  }

  function renderProbeAnswerExamples(probe) {
    const examples = probe.exampleAnswers || {};
    const strong = normalizeList(examples.strong);
    const weak = normalizeList(examples.weak);
    if (!strong.length && !weak.length) {
      return "";
    }
    return `
      <div class="probe-answer-examples">
        ${strong.length ? `
          <section class="probe-answer-column strong-probe-answer">
            <h5>Strong Example Answers</h5>
            ${renderList(strong)}
          </section>
        ` : ""}
        ${weak.length ? `
          <section class="probe-answer-column weak-probe-answer">
            <h5>Weak Example Answers</h5>
            ${renderList(weak)}
          </section>
        ` : ""}
      </div>
    `;
  }

  function renderFollowUps(spec) {
    const followUps = orderedFollowUps(spec);
    const groups = new Map();
    const seen = new Set();
    for (const probe of followUps) {
      const key = probe.id || probe.question;
      if (key && seen.has(key)) {
        continue;
      }
      if (key) {
        seen.add(key);
      }
      const tests = normalizeList(probe.tests);
      const primaryTest = tests[0] || "general";
      if (!groups.has(primaryTest)) {
        groups.set(primaryTest, []);
      }
      groups.get(primaryTest).push(probe);
    }
    return `
      <section class="content-section">
        <h2>Follow-Up Probes</h2>
        <p class="lead">Follow-ups are grouped by primary tested signal so each question appears once.</p>
        <div class="probe-groups">
          ${Array.from(groups.entries()).map(([test, probes]) => `
            <article class="probe-group">
              <h3>${escapeHtml(test)}</h3>
              <div class="probe-tree">
                ${probes.map((probe) => `
                  <article>
                    <h4>${inlineHtml(probe.question)}</h4>
                    <div class="chip-row">${renderChips(probe.tests, "signal-chip")}</div>
                    ${renderProbeAnswerExamples(probe)}
                  </article>
                `).join("")}
              </div>
            </article>
          `).join("")}
        </div>
      </section>
    `;
  }

  function renderEvaluation(spec) {
    const evaluation = spec.evaluation || {};
    return `
      <section class="content-section">
        <h2>Evaluation Rubric</h2>
        <h3>Strong vs. Weak Signals</h3>
        <div class="signal-grid">
          ${normalizeList(evaluation.signals).map((signal) => `
            <article>
              <h3>${escapeHtml(signal.name)}</h3>
              ${renderSignalEvidencePair(signal)}
            </article>
          `).join("")}
        </div>
        <h3>Level Calibration</h3>
        <div class="rubric-matrix" role="table" aria-label="Level calibration">
          <div class="rubric-header" role="row">
            <strong role="columnheader">Level</strong>
            <strong role="columnheader">Expected Evidence</strong>
          </div>
          ${normalizeList(evaluation.rubric).map((row) => `
            <div role="row">
              <strong role="cell">${escapeHtml(row.level)}</strong>
              <span role="cell">${inlineHtml(row.expected)}</span>
            </div>
          `).join("")}
        </div>
      </section>
    `;
  }

  function worksheetKey(field) {
    return `behavioral-interview:${state.currentId}:${field}`;
  }

  function renderPractice(spec) {
    const prompts = normalizeList(spec.practiceTemplate && spec.practiceTemplate.prompts);
    return `
      <section class="content-section">
        <div class="section-heading compact-heading">
          <h2>Practice Template</h2>
          <button id="clearWorksheet" class="secondary-button" type="button">Clear Draft</button>
        </div>
        <div class="worksheet">
          ${prompts.map((prompt) => `
            <label>
              <span>${inlineHtml(prompt.label)}</span>
              <textarea data-field="${escapeHtml(prompt.field)}" rows="5">${escapeHtml(localStorage.getItem(worksheetKey(prompt.field)) || "")}</textarea>
            </label>
          `).join("")}
        </div>
      </section>
    `;
  }

  function renderRelated(spec) {
    return `
      <section class="content-section">
        <h2>Related Scenarios</h2>
        ${renderList(spec.relatedScenarios)}
      </section>
    `;
  }

  function renderToProbeFurther(spec) {
    const groups = probeFurtherGroups(spec.toProbeFurther);
    if (!groups.length) {
      return `
        <section class="content-section">
          <h2>To Probe Further</h2>
          <p class="muted-note">No external resources have been researched for this interview yet.</p>
        </section>
      `;
    }
    return `
      <section class="content-section">
        <h2>To Probe Further</h2>
        <p class="lead">Selected external resources for deeper learning. Links open in a new tab.</p>
        <div class="probe-further">
          ${groups.map((group) => `
            <section class="probe-resource-group">
              <h3>${escapeHtml(group.name)}</h3>
              ${group.description ? `<p class="muted-note">${inlineHtml(group.description)}</p>` : ""}
              ${renderProbeFurtherLinkList(group.links)}
            </section>
          `).join("")}
        </div>
      </section>
    `;
  }

  function bindContentEvents() {
    els.content.querySelectorAll("textarea[data-field]").forEach((textarea) => {
      textarea.addEventListener("input", () => {
        localStorage.setItem(worksheetKey(textarea.dataset.field), textarea.value);
      });
    });

    const clear = document.getElementById("clearWorksheet");
    if (clear) {
      clear.addEventListener("click", () => {
        els.content.querySelectorAll("textarea[data-field]").forEach((textarea) => {
          localStorage.removeItem(worksheetKey(textarea.dataset.field));
          textarea.value = "";
        });
      });
    }
  }

  function render() {
    renderMeta();
    renderNav();
    els.status.hidden = true;
    const section = sections.find((item) => item.id === state.currentSection) || sections[0];
    els.content.innerHTML = section.render(state.spec);
    bindContentEvents();
  }

  function stepSection(delta) {
    const index = sections.findIndex((section) => section.id === state.currentSection);
    const next = sections[index + delta];
    if (next) {
      updateHash(next.id);
    }
  }

  if (els.icon) {
    els.icon.addEventListener("load", () => {
      els.icon.hidden = false;
    });
    els.icon.addEventListener("error", () => {
      els.icon.hidden = true;
    });
  }

  document.addEventListener("keydown", (event) => {
    if (event.target && ["TEXTAREA", "INPUT", "SELECT"].includes(event.target.tagName)) {
      return;
    }
    if (event.key === "ArrowRight") {
      stepSection(1);
    }
    if (event.key === "ArrowLeft") {
      stepSection(-1);
    }
  });

  async function boot() {
    await loadManifest();
    await loadCurrentSpec();
    render();
  }

  window.addEventListener("hashchange", () => {
    loadCurrentSpec()
      .then(render)
      .catch((error) => {
        els.status.hidden = false;
        els.status.textContent = error.message;
        els.status.classList.add("error");
      });
  });

  boot().catch((error) => {
    els.status.hidden = false;
    els.status.textContent = error.message;
    els.status.classList.add("error");
  });
})();
