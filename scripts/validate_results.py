"""Check consistency of the published catalogue and every downloadable result."""
from pathlib import Path
from collections import Counter
from decimal import Decimal, getcontext
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import hashlib,json,tarfile

ROOT=Path(__file__).resolve().parents[1]
getcontext().prec=100
def read(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))

def main():
    rows=read('data/campaign-catalogue.json'); metrics=read('data/campaign-metrics.json')
    records=read('instances/instances.json'); download=read('downloads/results-217.json')
    assert len(rows)==len({r['instance'] for r in rows})==217
    assert download['rows']==rows and download['metrics']==metrics
    assert sum(r['primal_improvement'] for r in rows)==59
    assert sum(r['dual_improvement'] for r in rows)==136
    assert Counter(r['status'] for r in records)=={'optimal':49,'infeasible':2,'unbounded':1,'open':165}
    by_name={r['instance']:r for r in rows}
    for record in records:
        row=by_name[record['instance']]
        assert (record['bestResult'],record['bestBound'])==(row['final_primal'],row['final_dual'])
        for flag,field in [('primalImprovement','primal_improvement'),('dualImprovement','dual_improvement')]:assert record[flag]==row[field]
        for result,baseline,gain,sign in [('final_primal','v36_primal','primal_gain',-1),('final_dual','copt10h_dual','dual_gain',1)]:
            if row[result] is not None and row[baseline] is not None and row[gain] is not None:
                a,b,c=(Decimal(row[k]) for k in [result,baseline,gain])
                # Rational values are serialized as finite decimal strings.
                rounding=max(abs(a),abs(b),abs(c),Decimal(1))*Decimal('1e-40')
                assert abs((a-b)*sign-c)<=rounding,row['instance']
        path=ROOT/'instances'/record['archive']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==record['archiveSha256']
        with tarfile.open(path) as tar:
            base=row['instance']+'-findings/'
            assert json.load(tar.extractfile(base+'result.json'))==row
            assert tar.extractfile(base+'summary.md').read()==(ROOT/'instances'/record['summary']).read_bytes()
    with tarfile.open(ROOT/'downloads/results-217.tar.gz') as tar:
        names=tar.getnames()
        assert sum(n.endswith('/result.json') for n in names)==217
        assert json.load(tar.extractfile('results-217.json'))==download
    class Links(HTMLParser):
        def __init__(self): super().__init__();self.links=[];self.ids=set()
        def handle_starttag(self,tag,attrs):
            self.links.extend(v for k,v in attrs if k in ('src','href') and v)
            self.ids.update(v for k,v in attrs if k=='id')
    for name in ['index.html','instances/index.html','skill/index.html','solver-replacement/index.html']:
        path=ROOT/name;p=Links();p.feed(path.read_text(encoding='utf-8'))
        for link in p.links:
            url=urlsplit(link)
            if url.scheme or url.netloc:continue
            if not url.path:
                if url.fragment:assert unquote(url.fragment) in p.ids,(name,link)
                continue
            target=(path.parent/unquote(url.path)).resolve()
            assert target.exists(),(name,link)
    print('PASS: 217 unique instances, counts, decimal differences, 217 result bundles, complete download and local page links.')

if __name__=='__main__':main()
