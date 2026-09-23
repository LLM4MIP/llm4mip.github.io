"""Build focused primal/dual comparisons from pinned, byte-preserved study tables."""
from pathlib import Path
from collections import Counter
from decimal import Decimal, getcontext
import csv
import json
import gzip
import io
import tarfile
import hashlib

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'data/skill-study/source/skills-research/comparisons'
getcontext().prec = 90

def rows(name):
    with (SOURCE/name).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='\n')

def archive(path, files):
    with path.open('wb') as out, gzip.GzipFile(filename='',fileobj=out,mode='wb',mtime=0) as gz, tarfile.open(fileobj=gz,mode='w') as tar:
        for name,p in sorted(files):
            raw=p.read_bytes();info=tarfile.TarInfo(name);info.size=len(raw);info.mtime=0;info.mode=0o644
            tar.addfile(info,io.BytesIO(raw))

def main():
    manifest=json.loads((ROOT/'data/skill-study/source-manifest.json').read_text(encoding='utf-8'))
    for entry in manifest['files']:
        path=ROOT/entry['local'] if 'local' in entry else ROOT/'data/skill-study/source'/entry['path']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256'], path
    pairs=rows('per_instance_comparison.csv')
    portfolio={r['instance']:r for r in rows('skill_portfolio_gap_comparison.csv') if r['portfolio']=='primal_dual' and r['backend_scope']=='gurobi_only'}
    direct={r['instance']:r for r in rows('portfolio_vs_direct_gurobi150m.csv') if r['portfolio']=='primal_dual' and r['backend_scope']=='gurobi_only'}
    assert len(pairs)==len(portfolio)==len(direct)==20
    result=[]
    for r in pairs:
        p=portfolio[r['instance']];d=direct[r['instance']]
        keep=['instance','batch','no_skill_primal','primal_skill_primal','no_skill_dual','dual_gurobi_strongest','dual_independent_certified','primal_method','dual_method','primal_evidence','dual_evidence','primal_row_tolerance','primal_integrality_tolerance','primal_max_row_violation','primal_max_integrality_violation','primal_max_bound_violation','dual_exact_closure']
        item={k:r[k] for k in keep}
        tolerance_accepted = r['instance']=='ns1456591'
        item.update(primal_outcome=r['primal_vs_no_P_at_1e_7'],
                    primal_tolerance_accepted=tolerance_accepted,
                    primal_raw_outcome=r['primal_vs_no_P_at_1e_7'],dual_outcome=r['dual_vs_no_D_at_1e_7'],
                    selected_primal=p['selected_primal'],primal_source=p['primal_source'],selected_dual=p['selected_dual'],dual_source=p['dual_source'],
                    excluded_primal_candidates=p['excluded_primal_candidates'],gap=p['portfolio_gap_fraction'],baseline_gap=p['gurobi_baseline_gap_fraction'],
                    gap_outcome=p['portfolio_vs_gurobi'],gap_reduction_pp=p['gurobi_minus_portfolio_gap_pp'],
                    direct_gap=d['direct_gurobi_gap_fraction'],direct_gap_outcome=d['verdict'],direct_gap_reduction_pp=d['gap_reduction_pp'],
                    copt_primal=p['original_copt_primal'],copt_dual=p['original_copt_dual'],
                    copt_gap=p['original_copt_gap_fraction'],copt_gap_outcome=p['portfolio_vs_copt'],
                    copt_gap_reduction_pp=p['copt_minus_portfolio_gap_pp'],copt_result=p['original_copt_result'],
                    copt_runtime_seconds=p['original_copt_time_seconds'])
        for prefix, baseline_primal in [('direct',d['direct_gurobi_primal']),('copt',p['original_copt_primal'])]:
            feasible_win = not baseline_primal.strip() and Decimal(p['selected_primal']).is_finite()
            item[prefix+'_feasibility_win'] = feasible_win
            if feasible_win:
                item[prefix+'_gap_outcome'] = 'win'
        def finite(value):
            try:
                n=Decimal(value)
                return n if n.is_finite() else None
            except Exception:
                return None
        solver_p=[(finite(v),label) for v,label in [(d['direct_gurobi_primal'],'Gurobi 150 min'),(p['original_copt_primal'],'COPT historical 10h')] if finite(v) is not None]
        solver_d=[(finite(v),label) for v,label in [(d['direct_gurobi_dual'],'Gurobi 150 min'),(p['original_copt_dual'],'COPT historical 10h')] if finite(v) is not None]
        sp=min(solver_p) if solver_p else None
        sd=max(solver_d) if solver_d else None
        sg=(sp[0]-sd[0])/max(Decimal(1),abs(sp[0]),abs(sd[0])) if sp and sd else None
        reduction=sg-Decimal(p['portfolio_gap_fraction']) if sg is not None else None
        item.update(solver_primal=str(sp[0]) if sp else '',solver_dual=str(sd[0]) if sd else '',
                    solver_primal_source=sp[1] if sp else '',solver_dual_source=sd[1] if sd else '',
                    solver_gap=str(sg) if sg is not None else '',solver_feasibility_win=not sp,
                    solver_gap_reduction_pp=str(reduction*100) if reduction is not None else '',
                    solver_gap_outcome='win' if not sp or (reduction is not None and reduction>Decimal('1e-9')) else 'loss' if reduction is not None and reduction<Decimal('-1e-9') else 'tie' if reduction is not None else 'NA')
        for prefix,bp,bd in [('ai',r['no_skill_primal'],r['no_skill_dual']),('solver',item['solver_primal'],item['solver_dual'])]:
            for kind,baseline,skill,sign in [('primal',bp,item['selected_primal'],1),('dual',bd,item['selected_dual'],-1)]:
                base=finite(baseline)
                delta=(base-Decimal(skill))*sign if base is not None else None
                item[prefix+'_portfolio_'+kind+'_outcome']='win' if kind=='primal' and base is None else 'NA' if delta is None else 'win' if delta>Decimal('1e-7') else 'loss' if delta<Decimal('-1e-7') else 'tie'
            for kind,baseline,skill,sign in [('primal',bp,r['primal_skill_primal'],1),('dual',bd,r['dual_gurobi_strongest'],-1)]:
                base=finite(baseline)
                delta=(base-Decimal(skill))*sign if base is not None else None
                item[prefix+'_'+kind+'_skill_outcome']='win' if kind=='primal' and base is None else 'NA' if delta is None else 'win' if delta>Decimal('1e-7') else 'loss' if delta<Decimal('-1e-7') else 'tie'
        result.append(item)
    stats={key:dict(Counter(r[key] for r in result)) for key in ['primal_outcome','primal_raw_outcome','dual_outcome','gap_outcome','direct_gap_outcome','copt_gap_outcome','solver_gap_outcome']}
    for prefix in ['ai','solver']:
        for kind in ['primal','dual']:
            key=prefix+'_'+kind+'_skill_outcome'
            stats[key]=dict(Counter(r[key] for r in result))
    for prefix in ['direct','copt','solver']:
        stats[prefix+'_feasibility_wins']=sum(r[prefix+'_feasibility_win'] for r in result)
    assert stats['primal_outcome']=={'win':10,'tie':9,'loss':1}
    assert stats['solver_primal_skill_outcome']=={'win':17,'tie':1,'loss':2}
    assert stats['dual_outcome']=={'win':17,'tie':1,'loss':2}
    assert stats['gap_outcome']=={'win':18,'loss':2}
    assert stats['direct_gap_outcome']=={'win':17,'tie':1,'loss':2}
    assert stats['copt_gap_outcome']=={'win':19,'loss':1}
    for key in ['gap_reduction_pp','direct_gap_reduction_pp','copt_gap_reduction_pp','solver_gap_reduction_pp']:
        values=[]
        for r in result:
            try:
                v=Decimal(r[key])
                if v.is_finite(): values.append(v)
            except Exception: pass
        stats[key+'_mean']=str(sum(values)/len(values));stats[key+'_pairs']=len(values)
    payload={'rows':result,'stats':stats}
    write(ROOT/'assets/focused-skill-data.js','window.FOCUSED_SKILL_DATA='+json.dumps(payload,ensure_ascii=False,separators=(',',':'))+';\n')
    write(ROOT/'downloads/primal-dual-comparison.json',json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    with (ROOT/'downloads/primal-dual-comparison.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(result[0]));w.writeheader();w.writerows(result)
    for folder in (ROOT/'data/skill-study/packages').iterdir():
        files=[(p.relative_to(folder).as_posix(),p) for p in folder.rglob('*') if p.is_file()]
        files.append(('LICENSE',ROOT/'LICENSE'))
        archive(ROOT/f'downloads/{folder.name}-skill.tar.gz',files)
    evidence=ROOT/'data/skill-study'
    archive(ROOT/'downloads/primal-dual-evidence.tar.gz',[(p.relative_to(ROOT).as_posix(),p) for p in evidence.rglob('*') if p.is_file()]+[('scripts/build_skill_data.py',Path(__file__)),('LICENSE',ROOT/'LICENSE')])
    print(json.dumps(stats))

if __name__=='__main__':main()
