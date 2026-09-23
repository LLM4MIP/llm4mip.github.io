(function () {
  "use strict";

  // Shared ordering across all three overview charts: red, blue, green, gray.
  const palette = ['#8c1515', '#006cb8', '#176b5b', '#77736f', '#b66a6a', '#719bbd', '#639b8d'];
  const views = {
    status: {
      title: "What happened across the 132 studied instances?",
      note: "These four categories partition the 132-instance benchmark. A resolved instance has a verified optimality or infeasibility result; official MIPLIB labels may not yet have changed.",
      mode: "stack",
      total: 132,
      items: [
        ["Certified optimality / infeasibility", 32, "#176b5b"],
        ["Verified feasible; open", 94, "#006cb8"],
        ["Numerically optimal up to 1e-10 tolerance", 2, "#8A4F00"],
        ["No feasible point found", 4, "#8c1515"]
      ]
    },
    evidence: {
      title: "How were the 34 optimality / infeasibility results verified?",
      note: "This classifies the basis of verification, not discovery credit. Portable replay after discovery is different from LLM-only discovery.",
      mode: "stack",
      total: 34,
      items: [
        ["Mathematically proven certificate", 20, "#8c1515", "Solver/LLM finds a primal bound. LLM proves a certificate mathematically"],
        ["Logic reasoning", 1, "#b1040e", "Solver/LLM finds a primal bound. LLM finds a certificate through LLM-based logic reasoning"],
        ["Enumeration", 3, "#176b5b", "Solver/LLM finds a primal bound. LLM finds a dual bound by enumeration"],
        ["Published-theorem transfer", 3, "#620059", "Solver/LLM finds a primal bound. LLM plugs instance data into a published theorem statement"],
        ["Floating-point zero-gap verification", 3, "#006cb8", "Solver finds a dual bound. LLM finds a matching primal solution"],
        ["Mixed computational verification", 2, "#8A4F00", "A combination of above methods"],
        ["Numerical closure at 1e-10 tolerance", 2, "#666666", "Residuals below the accepted tolerance"]
      ]
    },
    skill: {
      title: "Solver + primal/dual skill vs Vanilla prompting and solver baseline",
      note: "Vanilla prompting is the historical LLM + solver workflow without the dedicated primal/dual skills. The solver baseline uses the best recorded COPT/Gurobi bounds. All 20 cases count under the original acceptance tolerances.",
      mode: "paired", items: []
    }
  };

  views.evidence.items.sort((a, b) => b[1] - a[1]);

  for (const view of Object.values(views)) {
    view.items.forEach((item, index) => { item[2] = palette[index % palette.length]; });
  }

  const chart = document.querySelector("#overview-chart");
  const title = document.querySelector("#overview-title");
  const note = document.querySelector("#overview-note");
  const table = document.querySelector("#overview-data");
  const tableBody = document.querySelector("#overview-data tbody");
  const explanationHeading = document.querySelector("#overview-explanation-heading");
  const buttons = document.querySelectorAll("[data-overview]");
  if (!chart || !title || !note || !table || !tableBody || !explanationHeading || !buttons.length) return;

  function render(key) {
    const view = views[key];
    title.textContent = view.title;
    note.textContent = view.note;
    chart.replaceChildren();
    tableBody.replaceChildren();
    table.querySelector('thead th:nth-child(2)').textContent=key==='skill'?'Win / Tie / Loss':'Count';
    if (key==='skill') {
      explanationHeading.hidden=true;table.classList.remove('has-explanations');
      const grid=document.createElement('div');grid.className='skill-objective-grid';
      const groups=[['Solver + primal skill vs Vanilla prompting','ai_primal_skill_outcome'],['Solver + primal skill vs solver baseline','solver_primal_skill_outcome'],['Solver + dual skill vs Vanilla prompting','ai_dual_skill_outcome'],['Solver + dual skill vs solver baseline','solver_dual_skill_outcome']];
      for(const [label,statKey] of groups) {
        const counts=window.FOCUSED_SKILL_DATA.stats[statKey];
        const card=document.createElement('article');const heading=document.createElement('h4');heading.textContent=label;
        const stack=document.createElement('div');stack.className='stack';stack.setAttribute('role','img');
        const baselineLabel=statKey.startsWith('ai_')?'Vanilla prompting better':'Solver baseline better';
        const parts=[['win','Solver + skill better',palette[0]],['tie','Tie',palette[1]],['loss',baselineLabel,palette[2]]];
        const detail=document.createElement('p');detail.className='chart-note';
        stack.setAttribute('aria-label',parts.map(([k,l])=>`${l}: ${counts[k]||0}`).join('; '));
        detail.classList.add('overview-skill-legend');
        for(const [k,label,color] of parts) {
          const entry=document.createElement('span');const swatch=document.createElement('span');
          swatch.className='swatch';swatch.style.background=color;
          entry.append(swatch,document.createTextNode(`${label}: ${counts[k]||0}`));detail.append(entry);
        }
        for(const [k,,color] of parts) {const n=counts[k]||0;if(!n)continue;const segment=document.createElement('div');segment.className='stack-segment';segment.style.width=`${n/20*100}%`;segment.style.background=color;segment.textContent=String(n);stack.append(segment);}
        card.append(heading,stack,detail);grid.append(card);
        const tr=document.createElement('tr');const th=document.createElement('th');th.scope='row';th.textContent=label;const td=document.createElement('td');td.textContent=parts.map(([k])=>counts[k]||0).join(' / ');tr.append(th,td);tableBody.append(tr);
      }
      chart.append(grid);
      buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.overview===key)));return;
    }


    if (view.mode === "stack") {
      const stack = document.createElement("div");
      stack.className = "stack";
      stack.setAttribute("role", "img");
      stack.setAttribute("aria-label", view.items.map(item => `${item[0]}: ${item[1]}`).join("; "));
      const legend = document.createElement("div");
      legend.className = `legend legend-${view.items.length} compact-legend`;
      view.items.forEach(([label, value, color]) => {
        const segment = document.createElement("div");
        segment.className = "stack-segment";
        segment.style.width = `${(value / view.total) * 100}%`;
        segment.style.background = color;
        segment.textContent = value >= view.total * 0.08 ? String(value) : "";
        stack.append(segment);

        const item = document.createElement("div");
        item.className = "legend-item";
        item.innerHTML = `<span class="swatch" style="background:${color}"></span><span>${label}</span><strong>${value}</strong>`;
        legend.append(item);
      });
      chart.append(stack, legend);
    } else {
      const list = document.createElement("div");
      list.className = "bar-list";
      view.items.forEach(([label, value, color]) => {
        const row = document.createElement("div");
        row.className = "bar-row";
        row.innerHTML = `<span class="bar-label">${label}</span><div class="bar-track"><div class="bar-fill" style="width:${(value / view.max) * 100}%;background:${color}"></div></div><span class="bar-value">${value}</span>`;
        list.append(row);
      });
      chart.append(list);
    }

    const showExplanations = key === "evidence";
    explanationHeading.hidden = !showExplanations;
    table.classList.toggle("has-explanations", showExplanations);

    view.items.forEach(([label, value, , explanation]) => {
      const row = document.createElement("tr");
      const metric = document.createElement("th");
      const result = document.createElement("td");
      metric.scope = "row";
      metric.textContent = label;
      result.textContent = String(value);
      row.append(metric, result);
      if (showExplanations) {
        const detail = document.createElement("td");
        detail.className = "measure-explanation";
        detail.textContent = explanation;
        row.append(detail);
      }
      tableBody.append(row);
    });

    buttons.forEach(button => button.setAttribute("aria-pressed", String(button.dataset.overview === key)));
  }

  buttons.forEach(button => button.addEventListener("click", () => render(button.dataset.overview)));
  render("status");
}());
