"""Check public text, archive contents and metadata for private environment details."""
from pathlib import Path
import gzip,io,json,re,subprocess,tarfile,zipfile,ipaddress

ROOT=Path(__file__).resolve().parents[1]
MODEL=re.compile(r'\b(?:gpt\s*[-_]?\s*\d+(?:\.\d+)?(?:[\s/_-]*(?:sol|astra|mini|pro|ultra|thinking))*|\d+\.\d+\s*(?:sol|astra)(?:/ultra)?)\b',re.I)
WIN=re.compile(r'(?<![\w])(?:file:///)?[A-Za-z]:[\\/]+[^\s"\x27<>|,)\]`]+')
UNIX=re.compile(r'(?<![\w.])/(?:home|root|mnt|Users|workspace|workspaces|scratch|opt|tmp|var/tmp|private/tmp|data\d*|srv|etc)/[^\s"\x27<>|,)\]`]+')
HARDWARE=re.compile(r'\b(?:Intel\s+Xeon|AMD\s+EPYC|Ubuntu\s*\d|CentOS\s*\d)\b',re.I)
SECRET=re.compile(r'(?:\b(?:ghp_|github_pat_|sk-proj-)[A-Za-z0-9_-]{15,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)')
IP=re.compile(r'(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])')

def inspect(raw,name,counts,findings):
    counts['files']+=1
    if name.endswith(('.tar.gz','.tgz','.tar')):
        counts['archives']+=1
        with tarfile.open(fileobj=io.BytesIO(raw),mode='r:*') as tar:
            for member in tar:
                if member.uname or member.gname:findings.append((name,'archive owner metadata'))
                if member.isfile():inspect(tar.extractfile(member).read(),name+'!'+member.name,counts,findings)
        return
    if name.endswith('.zip'):
        counts['archives']+=1
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            for member in archive.infolist():
                if not member.is_dir():inspect(archive.read(member),name+'!'+member.filename,counts,findings)
        return
    if name.endswith('.gz'):
        inspect(gzip.decompress(raw),name[:-3],counts,findings);return
    if name.endswith('.png'):
        i=8
        while i+12<=len(raw):
            n=int.from_bytes(raw[i:i+4],'big');kind=raw[i+4:i+8]
            if kind in (b'eXIf',b'tEXt',b'iTXt',b'zTXt'):findings.append((name,'image metadata'))
            i+=n+12
        return
    try:text=raw.decode('utf-8-sig')
    except UnicodeDecodeError:return
    if '\x00' in text:return
    counts['text']+=1
    text=re.sub(r'\\u([0-9a-fA-F]{4})',lambda m:chr(int(m[1],16)),text)
    # Public HTTP links can legitimately contain directory names also used on local machines.
    text=re.sub(r'https?://[^\s"\x27<>]+','PUBLIC_URL',text)
    for kind,pattern in [('model configuration',MODEL),('local path',WIN),('server path',UNIX),('hardware identity',HARDWARE),('credential',SECRET)]:
        if pattern.search(text):findings.append((name,kind))
    for match in IP.finditer(text):
        try:address=ipaddress.ip_address(match[0])
        except ValueError:continue
        if not address.is_loopback and not address.is_unspecified:findings.append((name,'IP address'))

def main():
    files=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0')
    counts={'files':0,'archives':0,'text':0};findings=[]
    for name in files:
        if name:inspect((ROOT/name).read_bytes(),name,counts,findings)
    print(json.dumps({'counts':counts,'findings':findings},indent=2))
    raise SystemExit(bool(findings))

if __name__=='__main__':main()
