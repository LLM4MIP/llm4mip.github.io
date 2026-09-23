(function () {
  'use strict';
  const {rows, stats} = window.FOCUSED_SKILL_DATA;
  const methodSummaries = {
  "graphdraw-grafo2": {
    "primal": "Reposition connected parts of the drawing and adjust nearby coordinates.",
    "dual": "Bound connected components separately and add valid component cuts."
  },
  "polygonpack4-10": {
    "primal": "Rearrange small groups of polygons and repair their positions and rotations.",
    "dual": "Rule out incompatible polygon combinations using validated conflict cuts."
  },
  "scpm1": {
    "primal": "Exchange selected columns and prioritize low-cost repairs.",
    "dual": "Combine constraints and use exact bounds to rule out better solutions."
  },
  "ger50-17-trans-dfn-3t": {
    "primal": "Adjust linked capacity decisions and reoptimize the remaining continuous variables.",
    "dual": "Add cuts linking flow balance to capacity and strengthen the global bound."
  },
  "eva1aprime6x6opt": {
    "primal": "Exchange groups in the design and repair the remaining variables.",
    "dual": "Identify mutually incompatible choices and add clique constraints."
  },
  "cmflsp60-36-2-6": {
    "primal": "Revise production setups over selected time windows and repair the schedule.",
    "dual": "Strengthen links between setup decisions, product families, and active periods."
  },
  "r4l4-02-tree-bounds-50": {
    "primal": "Adjust linked timetable events and reconstruct a feasible schedule.",
    "dual": "Eliminate redundant timing variables and derive bounds from cycle constraints."
  },
  "sct1": {
    "primal": "Exchange linked choices and repair decisions that compete for tight resources.",
    "dual": "Enforce integrality of activation decisions and strengthen the full-model search."
  },
  "shipsched": {
    "primal": "Change the order of small groups of ships and recompute feasible timings.",
    "dual": "Tighten event-order constraints and remove redundant timing variables."
  },
  "rocII-8-11": {
    "primal": "Change configurations across related periods and repair continuous decisions.",
    "dual": "Use objective-counting bounds and exhaustive case splits to exclude better solutions."
  },
  "ns1856153": {
    "primal": "Exchange tree edges and jointly repair linked placement decisions.",
    "dual": "Replace connectivity logic with cut constraints and verify bounds by tree enumeration."
  },
  "dc1l": {
    "primal": "Replace selected crews and repair the remaining coverage decisions.",
    "dual": "Simplify the coverage model and derive bounds by relaxing selected constraints."
  },
  "neos-5221106-oparau": {
    "primal": "Refit bottleneck routes and exchange route segments.",
    "dual": "Strengthen route bounds with subtour elimination and demand-flow constraints."
  },
  "zeil": {
    "primal": "Recombine timetable choices and repair conflicts around busy intervals.",
    "dual": "Derive bounds from weighted time windows using a minimum-cut relaxation."
  },
  "cdma": {
    "primal": "Combine existing binary solutions and repair groups of linked decisions.",
    "dual": "Simplify and rescale the model, then verify a bound with an exact LP certificate."
  },
  "ns1456591": {
    "primal": "Exchange route blocks and repair continuous variables in the original model.",
    "dual": "Remove route symmetries and enumerate routes to certify the optimal partition."
  },
  "seqsolve1": {
    "primal": "Reassign staff at shortage sites and repair working-hour decisions.",
    "dual": "Use capacity and staffing cuts to rule out better objective values."
  },
  "stockholm": {
    "primal": "Change groups of toll decisions and repair the remaining variables.",
    "dual": "Add path-cover constraints and combine them into a verified lower bound."
  },
  "supportcase22": {
    "primal": "Combine binary patterns and repair inconsistent groups of decisions.",
    "dual": "Propagate constraints and exhaustively check objective-related cases for a bound."
  },
  "neos-3682128-sandon": {
    "primal": "Revise linked scheduling decisions around active penalties.",
    "dual": "Bound setup and assignment choices using scheduling decomposition and dynamic programming."
  }
};
  const definitions = {
    primal: {title:'Solver + primal skill vs Vanilla prompting and solver baseline', key:'primal_outcome', note:'Lower P is better. Against Vanilla prompting: 10 wins / 9 ties / 1 loss. Against the solver baseline: 17 / 1 / 2. Vanilla prompting uses no dedicated skill; the solver baseline uses the best recorded bounds. Absolute tolerance: 1e-7. The outcome filter uses the Vanilla prompting comparison.'},
    dual: {title:'Solver + dual skill vs Vanilla prompting and solver baseline', key:'dual_outcome', note:'Higher D is better. Against Vanilla prompting: 17 wins / 1 tie / 2 losses. Against the solver baseline: 15 / 1 / 4. Vanilla prompting uses no dedicated skill; the solver baseline uses the best recorded bounds. Numerical bounds retain their stated evidence levels. Absolute tolerance: 1e-7. The outcome filter uses the Vanilla prompting comparison.'},
    gap: {title:'Solver + primal/dual skill vs Vanilla prompting', key:'gap_outcome', note:'Post-hoc best valid bounds: 18 smaller gaps and 2 larger gaps; mean reduction 15.8079 percentage points over 20 pairs. Gurobi and independent certificates only.'},
    solver: {title:'Solver + primal/dual skill vs solver baseline', key:'solver_gap_outcome', note:'The solver baseline uses the lowest valid primal and highest valid dual across the recorded solver runs. The skill-assisted workflow wins 16 comparisons (15 smaller gaps + 1 feasible solution where neither solver recorded one), ties 1, and loses 3. Mean reduction: 18.9091 percentage points over 19 finite-gap pairs. Historical budgets and solver configurations differ.'}
  };
  const colors={win:'#8c1515',tie:'#77736f',loss:'#006cb8',NA:'#8A4F00'};
  let activeTab='gap';

  const search=document.querySelector('#focused-search');
  const filter=document.querySelector('#focused-filter');
  function cell(text) {const td=document.createElement('td');td.textContent=text;return td;}
  function percent(value) {const n=Number(value);return value && Number.isFinite(n)?(n*100).toFixed(4)+'%':'Unavailable';}
  function compact(raw) {
    if (raw === '' || raw == null) return 'No feasible solution';
    const n=Number(raw);
    if (!Number.isFinite(n)) return raw;
    return Math.abs(n)>=1e7 ? n.toExponential(5) : n.toLocaleString('en-US',{maximumSignificantDigits:9});
  }
  function badgeCell(outcome, winner='Solver + skill', baseline='Baseline') {
    const td=cell('');const badge=document.createElement('span');
    badge.className='badge '+(outcome==='win'?'concluded':outcome==='loss'?'verified-open':'pending');
    badge.textContent={win:winner,loss:baseline,tie:'Within tolerance',NA:'Not recorded'}[outcome]||outcome;
    td.append(badge);return td;
  }
  function boundsCell(p,d) {
    const td=cell('');
    for(const [label,value] of [['Primal',p],['Dual',d]]) {
      const line=document.createElement('div');line.textContent=label+' '+compact(value);line.title=value;td.append(line);
    }
    return td;
  }
  function methodCell(r, kind) {
    const td=cell(methodSummaries[r.instance][kind]);
    td.className='finding';
    const details=document.createElement('details');
    const summary=document.createElement('summary');summary.textContent='Evidence and experiment details';
    const text=document.createElement('p');
    text.textContent=kind==='primal'?
      (r.primal_tolerance_accepted?'Accepted at the original 1e-6 row and integrality tolerances (max residual 9.9e-7). Numerical objective 988.1403051801293; exact optimum 988.14128344. ':r.primal_evidence+'; row tolerance '+r.primal_row_tolerance+', integrality tolerance '+r.primal_integrality_tolerance+'. ')+r.primal_method:
      r.dual_evidence+'; '+r.dual_method;
    details.append(summary,text);td.append(details);return td;
  }
  function render() {
    const selected=activeTab;

    const def=definitions[selected];
    const filterWinner=filter.querySelector('option[value="win"]');
    const filterBaseline=filter.querySelector('option[value="loss"]');
    filterWinner.textContent=selected==='primal'?'Solver + primal skill better':selected==='dual'?'Solver + dual skill better':'Solver + skill better';
    filterBaseline.textContent=selected==='solver'?'Solver baseline better':'Vanilla prompting better';
    document.querySelector('#focused-title').textContent=def.title;
    document.querySelector('#focused-note').textContent=def.note;
    const chart=document.querySelector('#focused-chart');chart.replaceChildren();
    const groups=(selected==='primal'||selected==='dual')?
      [['vs Vanilla prompting','ai_'+selected+'_skill_outcome'],['vs solver baseline','solver_'+selected+'_skill_outcome']]:[['',def.key]];
    for(const [group,statKey] of groups) {
      if(group){const heading=document.createElement('h4');heading.textContent=group;chart.append(heading);}
    const baselineLabel=statKey.startsWith('ai_')||selected==='gap'?'Vanilla prompting better':'Solver baseline better';
    const labels={win:'Solver + skill better',tie:'Tie',loss:baselineLabel,NA:'Unavailable'};
    for(const [key,label] of Object.entries(labels)) {
      const n=stats[statKey][key]||0;if(!n)continue;
      const row=document.createElement('div');row.className='bar-row';
      row.innerHTML=`<span class="bar-label">${label}</span><div class="bar-track"><div class="bar-fill" style="width:${n/20*100}%;background:${colors[key]}"></div></div><span class="bar-value">${n}</span>`;
      chart.append(row);
    }
    }
    const baselineName=selected==='gap'?'Vanilla prompting':'Solver baseline';
    const headers= selected==='primal'?['Instance','Solver + primal skill P','Vanilla prompting P','Solver baseline P','vs Vanilla prompting','vs solver baseline','Skill-guided method']:
      selected==='dual'?['Instance','Solver + dual skill D','Vanilla prompting D','Solver baseline D','vs Vanilla prompting','vs solver baseline','Skill-guided method']:
      ['Instance','Better primal bound','Better dual bound','Smaller relative gap','Solver + skill bounds',baselineName+' bounds','Gap','Skill-guided method'];
    const head=document.querySelector('#focused-head');head.replaceChildren();
    headers.forEach(x=>{const th=document.createElement('th');th.textContent=x;head.append(th);});
    const body=document.querySelector('#focused-body');body.replaceChildren();
    const visible=rows.filter(r=>(filter.value==='all'||r[def.key]===filter.value)&&[r.instance,r.primal_method,r.dual_method,methodSummaries[r.instance].primal,methodSummaries[r.instance].dual].join(' ').toLowerCase().includes(search.value.trim().toLowerCase()));
    for(const r of visible) {
      const tr=document.createElement('tr');const name=cell(r.instance);name.className='instance-name';tr.append(name);
      if(selected==='primal')tr.append(cell(r.primal_skill_primal),cell(r.no_skill_primal),cell(r.solver_primal||'No feasible solution'),badgeCell(r.ai_primal_skill_outcome,'Solver + primal skill','Vanilla prompting'),badgeCell(r.solver_primal_skill_outcome,'Solver + primal skill','Solver baseline'),methodCell(r,'primal'));
      else if(selected==='dual')tr.append(cell(r.dual_gurobi_strongest),cell(r.no_skill_dual),cell(r.solver_dual),badgeCell(r.ai_dual_skill_outcome,'Solver + dual skill','Vanilla prompting'),badgeCell(r.solver_dual_skill_outcome,'Solver + dual skill','Solver baseline'),methodCell(r,'dual'));
      else {
        const prefix=selected==='gap'?'ai':'solver';
        const feasibilityWin=selected==='solver' && r.solver_feasibility_win;
        const bp=selected==='gap'?r.no_skill_primal:r.solver_primal;
        const bd=selected==='gap'?r.no_skill_dual:r.solver_dual;
        const baseline=selected==='gap'?r.baseline_gap:r.solver_gap;
        const reduction=selected==='gap'?r.gap_reduction_pp:r.solver_gap_reduction_pp;
        const gapCell=cell('');gapCell.className='gap-comparison-cell';
        const lines=[`Solver + primal/dual skill ${percent(r.gap)}`,`${baselineName} ${feasibilityWin?'No feasible solution':percent(baseline)}`,
          feasibilityWin?'Skill found a feasible solution':`Reduction ${Number(reduction).toFixed(4)} pp`];
        lines.forEach(text=>{const line=document.createElement('div');line.textContent=text;gapCell.append(line);});
        const method=cell('');method.className='finding';
        for(const [label,value] of [['Primal-skill',methodSummaries[r.instance].primal],['Dual-skill',methodSummaries[r.instance].dual]]) {
          const line=document.createElement('div');const strong=document.createElement('strong');strong.textContent=label+': ';line.append(strong,document.createTextNode(value));method.append(line);
        }
        if(r.excluded_primal_candidates!=='[]') {
          const note=document.createElement('small');note.textContent='Primal-skill candidate accepted at 1e-6 tolerance; the combined gap uses the independently verified exact feasible lift.';method.prepend(note);
        }
        tr.append(badgeCell(r[prefix+'_portfolio_primal_outcome'],'Solver + skill',baselineName),badgeCell(r[prefix+'_portfolio_dual_outcome'],'Solver + skill',baselineName),badgeCell(r[def.key],'Solver + skill',baselineName),boundsCell(r.selected_primal,r.selected_dual),boundsCell(bp,bd),gapCell,method);
      }
      body.append(tr);
    }
    document.querySelector('#focused-count').textContent=`Showing ${visible.length} of ${rows.length} paired instances`;
    document.querySelectorAll('[data-focused]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.focused===activeTab)));
  }
  document.querySelectorAll('[data-focused]').forEach(b=>b.addEventListener('click',()=>{activeTab=b.dataset.focused;filter.value='all';render();}));

  search.addEventListener('input',render);filter.addEventListener('change',render);render();
}());
