(function () {
  "use strict";
  const data = Array.isArray(window.INSTANCE_DATA) ? window.INSTANCE_DATA : [];
  const body = document.querySelector("#instance-body");
  const search = document.querySelector("#instance-search");
  const filter = document.querySelector("#instance-filter");
  const count = document.querySelector("#instance-count");
  if (!body || !search || !filter || !count) return;

  function formatBytes(bytes) {
    if (bytes < 1024) return `${bytes} B`;
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KiB`;
    return `${(bytes / 1024 / 1024).toFixed(1)} MiB`;
  }

  function cell(text, className) {
    const td = document.createElement("td");
    if (className) td.className = className;
    td.textContent = text ?? "—";
    return td;
  }

  function measureCell(display) {
    const td = document.createElement("td");
    td.className = "measure-cell";
    const value = document.createElement("span");
    value.className = "measure-value";
    value.textContent = display?.value ?? "—";
    td.append(value);
    if (display?.note) {
      const note = document.createElement("small");
      note.className = "measure-note";
      note.textContent = `(${display.note})`;
      td.append(note);
    }
    return td;
  }

  function linksCell(record) {
    const td = document.createElement("td");
    const wrap = document.createElement("div");
    wrap.className = "result-links";
    const summary = document.createElement("a");
    summary.className = "button small";
    summary.href = record.summary;
    summary.textContent = "Summary.md";
    const archive = document.createElement("a");
    archive.className = "button small";
    archive.href = record.archive;
    archive.download = "";
    archive.textContent = `Bundle · ${formatBytes(record.archiveBytes)}`;
    wrap.append(summary, archive);
    const meta = document.createElement("span");
    meta.className = "download-meta";
    meta.textContent = `${record.includedFiles} source files · SHA-256 ${record.archiveSha256.slice(0, 12)}…`;
    td.append(wrap, meta);
    return td;
  }

  function render() {
    const term = search.value.trim().toLowerCase();
    const status = filter.value;
    const visible = data.filter(record => {
      if (status !== "all" && record.status !== status) return false;
      if (!term) return true;
      return [record.instance, record.bestResult, record.bestBound, record.studyStatus, record.globalMethod, record.evidenceLevel]
        .filter(Boolean).join(" ").toLowerCase().includes(term);
    });

    body.replaceChildren();
    visible.forEach(record => {
      const row = document.createElement("tr");
      const name = cell(record.instance, "instance-name");
      const statusCell = document.createElement("td");
      const badge = document.createElement("span");
      badge.className = `badge ${record.status}`;
      badge.textContent = record.statusLabel;
      statusCell.append(badge);
      row.append(
        name,
        statusCell,
        measureCell(record.bestResultDisplay),
        measureCell(record.bestBoundDisplay),
        cell(record.studyStatus, "finding"),
        linksCell(record)
      );
      body.append(row);
    });
    count.textContent = `Showing ${visible.length} of ${data.length} instances`;
    document.querySelectorAll("[data-status-filter]").forEach(button => {
      button.setAttribute("aria-pressed", String(button.dataset.statusFilter === status));
    });
  }

  search.addEventListener("input", render);
  filter.addEventListener("change", render);
  document.querySelectorAll("[data-status-filter]").forEach(button => {
    button.addEventListener("click", () => {
      filter.value = button.dataset.statusFilter;
      render();
      document.querySelector("#catalogue").scrollIntoView({block: "start"});
    });
  });
  render();
}());
