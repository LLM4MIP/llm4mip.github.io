"""Build the current site from checked-in data; no solver or network access.

Existing bundles remain immutable historical archives. New compact result
bundles contain per-instance results and links, not complete proof archives.
"""
from pathlib import Path
from collections import Counter
import gzip
import hashlib
import io
import json
import re
import tarfile
from html import escape

SITE = Path(__file__).resolve().parents[1]
SOURCE_COMMIT = 'b63b89634917ccde2f9e7dc7aefe1583a3eb55e8'
SOURCE_URL = f'https://github.com/Huangyc98/MIPLIB_openproblem/blob/{SOURCE_COMMIT}/'
STATUS = {
    'concluded': ('Certified optimality / infeasibility', '#8c1515'),
    'verified-open': ('Verified feasible; open', '#006cb8'),
    'numeric-optimal': ('Numerically optimal up to 1e-10 tolerance', '#176b5b'),
    'no-feasible': ('No feasible point found', '#77736f'),
}
# Retain the published 18 September evidence reconciliation for old cases.
# Add the two subsequent exact optima and the two tolerance-accepted genus cases.
GRADES = {
    'PE': ('Portable exact certificate', '#8c1515'),
    'HP': ('Checked proof trace', '#b1040e'),
    'EX': ('Exhaustive exact verification', '#176b5b'),
    'LT': ('Published-theorem transfer', '#620059'),
    'NS': ('Floating-point zero-gap verification', '#006cb8'),
    'MX': ('Mixed computational evidence', '#8A4F00'),
    'TC': ('Tolerance-accepted closure', '#666666'),
}


def read(name):
    return json.loads((SITE/name).read_text(encoding='utf-8'))


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def result_bundle(path, name, row, summary):
    payloads = {'summary.md': summary, 'result.json': json.dumps(row, ensure_ascii=False, indent=2)+'\n',
                'LICENSE': (SITE/'LICENSE').read_text(encoding='utf-8')}
    with path.open('wb') as output:
        with gzip.GzipFile(filename='', mode='wb', fileobj=output, mtime=0) as zipped:
            with tarfile.open(fileobj=zipped, mode='w') as archive:
                for filename, text in payloads.items():
                    raw = text.encode('utf-8'); info = tarfile.TarInfo(f'{name}-findings/{filename}')
                    info.size = len(raw); info.mtime = 0; info.mode = 0o644
                    archive.addfile(info, io.BytesIO(raw))


def main():
    catalogue = read('data/campaign-catalogue.json')
    metrics = read('data/campaign-metrics.json')
    legacy = {r['instance']: r for r in read('data/upstream-catalogue-b48994a.json')}
    assert len(catalogue) == len({r['instance'] for r in catalogue}) == metrics['instances'] == 132
    assert sum(r['project_primal_update'] for r in catalogue) == metrics['project_primal_updates']
    assert sum(r['dual_improved_at_1e_7'] for r in catalogue) == metrics['dual_improvements_at_1e_7']
    records = []
    for row in catalogue:
        name = row['instance']; prior = legacy.get(name, {})
        closed = row['conclusion'].startswith('optimal') or row['conclusion'] == 'infeasible'
        status = 'concluded' if closed else prior.get('status', 'verified-open')
        if row['conclusion'] == 'optimal_with_tolerance': status = 'numeric-optimal'
        grade = prior.get('evidenceGrade')
        if row['conclusion'] == 'optimal_with_tolerance': grade = 'TC'
        elif name in ('ns1456591', 'neos-3682128-sandon'): grade = 'PE'
        if closed: assert grade in GRADES, name
        conclusion = ('Infeasible' if row['conclusion']=='infeasible' else
                      f"OPT = {row['primal']}" + (' (residual < 1e-10)' if grade=='TC' else '')) if closed else None
        r = dict(prior)
        r.update(instance=name, cohort=row['cohort'], status=status, statusLabel=STATUS[status][0],
                 bestResult=row['primal'] if row['primal'] is not None else row['primal_source'],
                 bestBound=row['dual'] if row['dual'] is not None else row['dual_source'],
                 studyStatus=row['evidence_note'], globalConclusion=conclusion,
                 globalMethod=prior.get('globalMethod') or (row['evidence_note'] if closed else None),
                 evidenceGrade=grade, evidenceLevel=GRADES[grade][0] if grade else None,
                 primalImprovement=row['project_primal_update'], dualImprovement=row['dual_improved_at_1e_7'],
                 primalCategory=row['primal_category'], miplibPrimal=row['miplib_primal'],
                 coptDual=row['copt_10h_dual'], primalDelta=row['primal_delta'], dualDelta=row['dual_delta'],
                 sourceUrl=SOURCE_URL+row['source_path'], resultSourceCommit=SOURCE_COMMIT,
                 summary=f'details/{name}/summary.md', archive=f'details/{name}/{name}-findings.tar.gz',
                 bundleKind='historical' if prior else 'result')
        r['sourceEvidenceNote'] = row['audit_evidence'] or row['evidence_note']
        for field in ('bestResult','bestBound'):
            old_display=prior.get(field+'Display',{})
            r[field+'Display']={'value':str(r[field]) if r[field] is not None else '—','note':old_display.get('note')}
        r['bundleSnapshot'] = 'upstream-b48994a' if prior else '2026-09-21'
        if not prior:
            r['sourceBaseCommit'] = SOURCE_COMMIT; r['includedFiles'] = 3; r['excludedFiles'] = 0
        evidence = r['evidenceLevel'] or 'See the stated numerical tolerances and source audits.'
        bundle_note = ('The downloadable research bundle is the unchanged 18 September archive. '
                       'This summary and the current catalogue supersede its historical counts and genus policy.' if prior else
                       'The result bundle contains this summary, the per-instance ledger and license. '
                       'Detailed experiment records and certificates are linked in the research repository; they are not embedded in this compact bundle.')
        summary = f"""# {name}

Snapshot: 21 September 2026. Repository research results; not a live MIPLIB leaderboard.

## Current result

- Cohort: {row['cohort']}
- Status: {r['statusLabel']}
- Primal: {r['bestResult']}
- Dual / certificate: {r['bestBound']}
- Global conclusion: {conclusion or 'Not established'}
- Evidence: {evidence}
- Project primal update vs MIPLIB v36: {row['project_primal_update']} ({row['primal_category']})
- Dual improvement vs historical COPT 10h: {row['dual_improved_at_1e_7']}

{row['evidence_note']}

{row['audit_limits']}

## Evidence and provenance

[Instance evidence]({r['sourceUrl']}) · [Complete campaign ledger]({SOURCE_URL}results/catalogue.json)

The full campaign contains 132 instances: 112 original cases and 20 subsequent evaluation cases.
The subsequent cohort uses post-hoc best valid bounds from separate skill runs; numerical bounds
and independently certified bounds are distinct. Genus g31 closures accept residuals below 1e-10.

## Download scope

{bundle_note}
"""
        folder = SITE/'instances/details'/name; folder.mkdir(parents=True, exist_ok=True)
        archive = SITE/'instances'/r['archive']
        if not prior:
            result_bundle(archive, name, row, summary)
            r['archiveBytes'] = archive.stat().st_size; r['archiveSha256'] = sha(archive)
        else:
            assert archive.exists() and sha(archive)==prior['archiveSha256'], name
        summary += f"\nArchive SHA-256: `{r['archiveSha256']}`\n"
        if not prior:
            write(folder/'summary.md', summary)
        records.append(r)
    records.sort(key=lambda r:r['instance'].lower())
    counts = Counter(r['status'] for r in records)
    grades = Counter(r['evidenceGrade'] for r in records if r['status'] in ('concluded','numeric-optimal'))
    assert counts == {'concluded':32, 'verified-open':94, 'numeric-optimal':2, 'no-feasible':4}
    assert sum(grades.values()) == metrics['optimal_including_tolerance']+metrics['infeasible'] == 34
    campaign = dict(metrics, closed=34, statusCounts=dict(counts), evidenceCounts=dict(grades),
                    sourceCommit=SOURCE_COMMIT, updated='2026-09-21',
                    statusItems=[[label,counts[key],color] for key,(label,color) in STATUS.items()],
                    evidenceItems=[[label,grades[key],color] for key,(label,color) in GRADES.items()])
    write(SITE/'instances/instances.json', json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    write(SITE/'instances/data.js', 'window.INSTANCE_DATA='+json.dumps(records,ensure_ascii=False,separators=(',',':'))+';\n')
    write(SITE/'assets/campaign-data.js', 'window.CAMPAIGN_DATA='+json.dumps(campaign,ensure_ascii=False,separators=(',',':'))+';\n')
    write(SITE/'data/site-metrics.json', json.dumps(campaign,ensure_ascii=False,indent=2)+'\n')
    for page in ('index.html','instances/index.html','skill/index.html','solver-replacement/index.html'):
        path=SITE/page; text=path.read_text(encoding='utf-8')
        status_html = '<div class="status-strip" role="group" aria-label="Filter by campaign status">'
        for key, (label, color) in STATUS.items():
            n = counts[key]
            status_html += f'<button type="button" data-status-filter="{key}" style="width:{n/len(records)*100:.6f}%;background:{color}" aria-label="{escape(label)}: {n}" aria-pressed="false">{n}</button>'
        status_html += '</div><div class="legend legend-4">'
        for label,n,color in campaign['statusItems']:
            status_html += f'<div class="legend-item"><span class="swatch" style="background:{color}"></span><span>{escape(label)}</span><strong>{n}</strong></div>'
        status_html += '</div>'
        options = [('all',f'All {len(records)}')] + [(k,f'{label} ({counts[k]})') for k,(label,_) in STATUS.items()]
        options += [('optimal','Optimal (32)'),('infeasible','Infeasible (2)'),('primal-improved','Primal update (29)'),('dual-improved','Dual improvement (66)')]
        options_html = ''.join(f'<option value="{key}">{escape(label)}</option>' for key,label in options)
        evidence_html = '<div class="stack" role="img" aria-label="'+escape('; '.join(f'{label}: {n}' for label,n,_ in campaign['evidenceItems']))+'">'
        for label,n,color in campaign['evidenceItems']:
            evidence_html += f'<div class="stack-segment" style="width:{n/34*100:.6f}%;background:{color}">{n if n>=3 else ""}</div>'
        evidence_html += '</div><div class="legend">'
        for label,n,color in campaign['evidenceItems']:
            evidence_html += f'<div class="legend-item"><span class="swatch" style="background:{color}"></span><span>{escape(label)}</span><strong>{n}</strong></div>'
        evidence_html += '</div>'
        for key,html in [('STATUS',status_html),('OPTIONS',options_html),('EVIDENCE',evidence_html)]:
            text=re.sub(f'<!-- CAMPAIGN_{key}_START -->.*?<!-- CAMPAIGN_{key}_END -->',f'<!-- CAMPAIGN_{key}_START -->\n{html}\n<!-- CAMPAIGN_{key}_END -->',text,flags=re.S)
        def metric(m): return m[1]+str(campaign[m[2]])+m[3]
        text=re.sub(r'(<(?:strong|span)[^>]*data-campaign="([^"]+)"[^>]*>)[^<]*(</(?:strong|span)>)',metric,text)
        write(path,text)
    print(json.dumps({'instances':len(records),'closed':34,'optimal':32,'infeasible':2,
                      'primal_updates':metrics['project_primal_updates'],'dual_improvements':metrics['dual_improvements_at_1e_7'],
                      'status_counts':dict(counts),'evidence_counts':dict(grades)}))


if __name__=='__main__': main()
