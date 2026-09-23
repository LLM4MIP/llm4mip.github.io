(function () {
  "use strict";
  const data = Array.isArray(window.COMPARISON_DATA) ? window.COMPARISON_DATA : [];
  const metrics = {
    primal: {
      title: "Primal bound (incumbent objective)",
      note: "At absolute tolerance 1e-7, the skill-guided arm produced the better primal bound on 11 instances and tied on nine. Six skill-arm primal bounds were tolerance-indexed.",
      max: 20,
      items: [["Skill-guided better", 11, "#8c1515"], ["Equal within 1e-7", 9, "#77736f"], ["Comparison better", 0, "#006cb8"]]
    },
    dual: {
      title: "Valid global dual bound",
      note: "The comparison arm produced the better dual bound on 12 instances; the skill-guided arm produced the better dual bound on eight.",
      max: 20,
      items: [["Skill-guided better", 8, "#8c1515"], ["Comparison better", 12, "#006cb8"]]
    },
    gap: {
      title: "Smaller relative optimality gap",
      note: "The comparison arm had the smaller normalized relative gap on 11 instances; the skill-guided arm had the smaller gap on nine.",
      max: 20,
      items: [["Skill-guided smaller", 9, "#8c1515"], ["Comparison smaller", 11, "#006cb8"]]
    },
    strict: {
      title: "Strict primal-bound improvements over the frozen public baseline",
      note: "Counts are independent outcomes, not a partition of 20. Each arm is judged under the archived strict acceptance rules.",
      max: 4,
      items: [["Skill-guided arm", 4, "#8c1515"], ["Comparison arm", 2, "#006cb8"]]
    },
    closure: {
      title: "Certified global optimality",
      note: "The skill-guided workflow certified global optimality for two instances in the separate 20-instance comparison; these results are not included in the 30 resolved instances reported for the 112-instance benchmark.",
      max: 2,
      items: [["Skill-guided arm", 2, "#8c1515"], ["Comparison arm", 0, "#006cb8"]]
    }
  };

  const metricChart = document.querySelector("#metric-chart");
  const metricTitle = document.querySelector("#metric-title");
  const metricNote = document.querySelector("#metric-note");
  const metricButtons = document.querySelectorAll("[data-metric]");
  function renderMetric(key) {
    if (!metricChart || !metricTitle || !metricNote) return;
    const metric = metrics[key];
    metricTitle.textContent = metric.title;
    metricNote.textContent = metric.note;
    metricChart.replaceChildren();
    const list = document.createElement("div");
    list.className = "bar-list";
    metric.items.forEach(([label, value, color]) => {
      const row = document.createElement("div");
      row.className = "bar-row";
      row.innerHTML = `<span class="bar-label">${label}</span><div class="bar-track"><div class="bar-fill" style="width:${metric.max ? value / metric.max * 100 : 0}%;background:${color}"></div></div><span class="bar-value">${value}</span>`;
      list.append(row);
    });
    metricChart.append(list);
    metricButtons.forEach(button => button.setAttribute("aria-pressed", String(button.dataset.metric === key)));
  }
  metricButtons.forEach(button => button.addEventListener("click", () => renderMetric(button.dataset.metric)));
  if (metricButtons.length) renderMetric("primal");

  const tableBody = document.querySelector("#comparison-body");
  const search = document.querySelector("#comparison-search");
  const filter = document.querySelector("#comparison-filter");
  const count = document.querySelector("#comparison-count");
  if (!tableBody || !search || !filter || !count) return;

  const labels = {skill_better: "Skill", no_skill_better: "Comparison", tie: "Within tolerance"};
  function compact(raw) {
    if (raw === undefined || raw === null || raw === "") return "—";
    const number = Number(raw);
    if (!Number.isFinite(number)) return raw;
    const magnitude = Math.abs(number);
    if (magnitude !== 0 && (magnitude >= 1e7 || magnitude < 1e-4)) return number.toExponential(5);
    return number.toLocaleString("en-US", {maximumSignificantDigits: 9});
  }
  function outcomeCell(value) {
    const td = document.createElement("td");
    const badge = document.createElement("span");
    badge.className = `badge ${value === "skill_better" ? "concluded" : value === "tie" ? "pending" : "verified-open"}`;
    badge.textContent = labels[value] || value;
    td.append(badge);
    return td;
  }
  function valueCell(primary, secondary, gap) {
    const td = document.createElement("td");
    const p = document.createElement("div");
    p.textContent = `Primal ${compact(primary)}`;
    p.title = primary;
    const d = document.createElement("div");
    d.textContent = `Dual ${compact(secondary)}`;
    d.title = secondary;
    const g = document.createElement("div");
    g.className = "note";
    g.textContent = `relative gap ${(Number(gap) * 100).toFixed(3)}%`;
    td.append(p, d, g);
    return td;
  }
  function matchesFilter(row, selected) {
    if (selected === "all") return true;
    if (selected === "skill-primal") return row.selected_primal_comparison_at_1e_7 === "skill_better";
    if (selected === "skill-dual") return row.dual_comparison_at_1e_7 === "skill_better";
    if (selected === "comparison-dual") return row.dual_comparison_at_1e_7 === "no_skill_better";
    if (selected === "strict") return row.skill_new_strict_vs_frozen_public_baseline === "true";
    if (selected === "exact") return row.skill_exact_global_optimum === "true";
    if (selected === "tolerance") return row.skill_primal_is_tolerance_indexed === "true";
    return true;
  }
  function renderTable() {
    const term = search.value.trim().toLowerCase();
    const selected = filter.value;
    const rows = data.filter(row => matchesFilter(row, selected) && (!term || [row.instance, row.skill_main_method, row.skill_final_status].join(" ").toLowerCase().includes(term)));
    tableBody.replaceChildren();
    rows.forEach(record => {
      const tr = document.createElement("tr");
      const instance = document.createElement("td");
      instance.className = "instance-name";
      instance.textContent = record.instance;
      const batch = document.createElement("td");
      batch.textContent = record.batch;
      const method = document.createElement("td");
      method.className = "finding";
      method.textContent = record.skill_main_method;
      if (record.skill_primal_is_tolerance_indexed === "true") {
        const marker = document.createElement("span");
        marker.className = "badge pending";
        marker.textContent = "Tolerance-indexed primal bound";
        method.prepend(marker, document.createElement("br"));
      }
      tr.append(
        instance,
        batch,
        outcomeCell(record.selected_primal_comparison_at_1e_7),
        outcomeCell(record.dual_comparison_at_1e_7),
        outcomeCell(record.common_gap_comparison),
        valueCell(record.skill_selected_primal, record.skill_dual, record.skill_common_gap_fraction),
        valueCell(record.no_skill_primal, record.no_skill_dual, record.no_skill_common_gap_fraction),
        method
      );
      tableBody.append(tr);
    });
    count.textContent = `Showing ${rows.length} of ${data.length} paired instances`;
  }
  search.addEventListener("input", renderTable);
  filter.addEventListener("change", renderTable);
  renderTable();
}());
