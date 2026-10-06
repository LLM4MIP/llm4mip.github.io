"""Generate the current website results and deterministic result downloads."""
from pathlib import Path
from collections import Counter
from html import escape
import csv
import gzip
import hashlib
import io
import json
import re
import tarfile

SITE = Path(__file__).resolve().parents[1]
STATUS = {
    'optimal': ('Optimal', '#8c1515'),
    'infeasible': ('Infeasible', '#620059'),
    'unbounded': ('Unbounded', '#176b5b'),
    'open': ('Open', '#006cb8'),
}
GRADES = {
    'PE': ('Portable exact certificate', '#8c1515', 'Exact certificates with instance-specific replay requirements.'),
    'HP': ('Checked proof trace', '#b1040e', 'A checked proof trace; external trace availability is documented per instance.'),
    'EX': ('Exhaustive exact verification', '#176b5b', 'Finite exhaustive verification of the stated conclusion.'),
    'LT': ('Published-theorem transfer', '#620059', 'Instance data mapped to a published theorem.'),
    'NS': ('Floating-point zero-gap verification', '#006cb8', 'Solver numerical verification under the reported tolerances.'),
    'MX': ('Mixed computational evidence', '#8a4f00', 'A combination of computational verification methods.'),
    'TC': ('Tolerance-accepted closure', '#666666', 'Closure under the stated numerical tolerance.'),
    'IV': ('Instance-specific proofs and solver verification', '#719bbd', 'Exact structural proofs or solver numerical verification, as specified in each instance summary.'),
}

def read(name):
    return json.loads((SITE/name).read_text(encoding='utf-8'))

def write(name, text):
    path=SITE/name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='\n')

def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2)+'\n'

def bundle(path, files):
    with path.open('wb') as out, gzip.GzipFile(filename='', mode='wb', fileobj=out, mtime=0) as gz:
        with tarfile.open(fileobj=gz, mode='w') as tar:
            for name,raw in sorted(files.items()):
                info=tarfile.TarInfo(name); info.size=len(raw); info.mtime=0; info.mode=0o644
                tar.addfile(info,io.BytesIO(raw))

def replace_block(text, key, replacement):
    pattern=f'<!-- CAMPAIGN_{key}_START -->.*?<!-- CAMPAIGN_{key}_END -->'
    text,n=re.subn(pattern,lambda _:f'<!-- CAMPAIGN_{key}_START -->\n{replacement}\n<!-- CAMPAIGN_{key}_END -->',text,flags=re.S)
    assert n==1, (key,n)
    return text

def main():
    rows=read('data/campaign-catalogue.json'); metrics=read('data/campaign-metrics.json')
    assert len(rows)==len({r['instance'] for r in rows})==metrics['instances']
    assert sum(r['primal_improvement'] for r in rows)==metrics['primal_improvements']
    assert sum(r['dual_improvement'] for r in rows)==metrics['dual_improvements']
    counts=Counter('optimal' if r['conclusion'].startswith('optimal') else r['conclusion'] for r in rows)
    for key in STATUS: assert counts[key]==metrics[key]
    assert metrics['resolved']==sum(counts[k] for k in ['optimal','infeasible','unbounded'])
    records=[]; all_files={}; license_raw=(SITE/'LICENSE').read_bytes()
    for row in sorted(rows,key=lambda r:r['instance'].lower()):
        name=row['instance']; status='optimal' if row['conclusion'].startswith('optimal') else row['conclusion']
        grade=row['evidence_grade']; folder=SITE/'instances/details'/name; folder.mkdir(parents=True,exist_ok=True)
        conclusion=STATUS[status][0]
        if row['conclusion']=='optimal_with_tolerance': conclusion+=' (tolerance-accepted)'
        summary=f'''# {name}

Result snapshot: {metrics['result_snapshot']}.

## Current result

- Conclusion: {conclusion}
- Primal bound: {row['primal_display']}
- Dual bound: {row['dual_display']}
- Normalized gap: {row['normalized_gap'] or 'Not applicable'}
- Primal improvement vs MIPLIB v36: {row['primal_improvement']}
- MIPLIB v36 primal: {row['v36_primal'] or 'No finite bound'}
- Primal difference (baseline minus result): {row['primal_gain'] or 'Not applicable'}
- Dual improvement vs historical COPT 10h: {row['dual_improvement']}
- Historical COPT 10h dual: {row['copt10h_dual'] or 'No finite bound'}
- Dual difference (result minus baseline): {row['dual_gain'] or 'Not applicable'}

## Verification and qualifications

{row['evidence']}

{row['notes']}

- Primal validation: {row['validation_grade']}
- Dual validation: {row['dual_validation_grade']}
- Primal comparison: {row['primal_comparison']}
- Dual comparison: {row['dual_comparison']}

## Files and provenance

[Result data](result.json) · [Source research record]({row['instance_evidence_url']})

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.
'''
        row_json=dump(row)
        write(f'instances/details/{name}/summary.md',summary)
        write(f'instances/details/{name}/result.json',row_json)
        files={'summary.md':summary.encode(),'result.json':row_json.encode(),'LICENSE':license_raw}
        archive=folder/f'{name}-findings.tar.gz'; bundle(archive,{f'{name}-findings/{k}':v for k,v in files.items()})
        all_files[f'instances/{name}/summary.md']=summary.encode()
        all_files[f'instances/{name}/result.json']=row_json.encode()
        records.append(dict(instance=name,status=status,statusLabel=conclusion,conclusion=row['conclusion'],
            bestResult=row['final_primal'],bestBound=row['final_dual'],
            bestResultDisplay={'value':row['primal_display']},bestBoundDisplay={'value':row['dual_display']},
            studyStatus=' '.join(filter(None,[row['evidence'],row['notes']])),
            evidenceGrade=grade,evidenceLevel=GRADES[grade][0] if grade else None,
            primalImprovement=row['primal_improvement'],dualImprovement=row['dual_improvement'],
            miplibPrimal=row['v36_primal'],coptDual=row['copt10h_dual'],primalDelta=row['primal_gain'],dualDelta=row['dual_gain'],
            sourceUrl=row['instance_evidence_url'],summary=f'details/{name}/summary.md',
            archive=f'details/{name}/{name}-findings.tar.gz',archiveBytes=archive.stat().st_size,
            archiveSha256=hashlib.sha256(archive.read_bytes()).hexdigest(),includedFiles=3))
    grades=Counter(r['evidenceGrade'] for r in records if r['status']!='open')
    assert sum(grades.values())==metrics['resolved']
    campaign=dict(metrics,statusCounts=dict(counts),evidenceCounts=dict(grades),
        statusItems=[[label,counts[k],color] for k,(label,color) in STATUS.items()],
        evidenceItems=[[label,grades[k],color,note] for k,(label,color,note) in GRADES.items() if grades[k]])
    write('instances/instances.json',dump(records))
    write('instances/data.js','window.INSTANCE_DATA='+json.dumps(records,ensure_ascii=False,separators=(',',':'))+';\n')
    write('assets/campaign-data.js','window.CAMPAIGN_DATA='+json.dumps(campaign,ensure_ascii=False,separators=(',',':'))+';\n')
    write('data/site-metrics.json',dump(campaign))
    write('downloads/results-217.json',dump({'metrics':metrics,'rows':rows,'provenance':read('data/result-provenance.json')}))
    with (SITE/'downloads/results-217.csv').open('w',encoding='utf-8',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    for f in ['results-217.json','results-217.csv']: all_files[f]=(SITE/'downloads'/f).read_bytes()
    all_files['LICENSE']=license_raw
    bundle(SITE/'downloads/results-217.tar.gz',all_files)
    status_html='<div class="status-strip" role="group" aria-label="Filter by benchmark outcome">'
    for key,(label,color) in STATUS.items():
        n=counts[key];status_html+=f'<button type="button" data-status-filter="{key}" style="width:{n/len(rows)*100:.6f}%;background:{color}" aria-label="{label}: {n}" aria-pressed="false">{n if n>3 else ""}</button>'
    status_html+='</div><div class="legend legend-4">'
    for label,n,color in campaign['statusItems']: status_html+=f'<div class="legend-item"><span class="swatch" style="background:{color}"></span><span>{label}</span><strong>{n}</strong></div>'
    status_html+='</div>'
    options=[('all',f"All {len(rows)}"),('resolved',f"Resolved ({metrics['resolved']})")]+[(k,f'{label} ({counts[k]})') for k,(label,_) in STATUS.items()]+[('primal-improved',f"Primal improvement ({metrics['primal_improvements']})"),('dual-improved',f"Dual improvement ({metrics['dual_improvements']})")]
    options_html=''.join(f'<option value="{k}">{escape(label)}</option>' for k,label in options)
    page=(SITE/'instances/index.html').read_text(encoding='utf-8')
    page=replace_block(page,'STATUS',status_html);page=replace_block(page,'OPTIONS',options_html)
    write('instances/index.html',page)
    for filename in ['index.html','instances/index.html','solver-replacement/index.html']:
        page=(SITE/filename).read_text(encoding='utf-8')
        page=re.sub(r'(<(?:strong|span)[^>]*data-campaign="([^"]+)"[^>]*>)[^<]*(</(?:strong|span)>)',lambda m:m[1]+str(metrics[m[2]])+m[3],page)
        write(filename,page)
    print(json.dumps(campaign))

if __name__=='__main__': main()
