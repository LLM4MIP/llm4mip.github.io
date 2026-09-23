"""Check tracked text and recursively inspect published archives for Han characters.

Run after rebuilding website data or download archives. PDF text is checked
separately with pdftotext when available. Historical Git revisions are excluded.
"""
from pathlib import Path
import gzip
import io
import json
import re
import subprocess
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
HAN = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]')
ESCAPED = re.compile(r'\\u([0-9a-fA-F]{4})')


def inspect(raw, name, findings, counts):
    if name.endswith(('.tar.gz', '.tgz')):
        counts['archives'] += 1
        with tarfile.open(fileobj=io.BytesIO(raw), mode='r:gz') as archive:
            for member in archive:
                if member.isfile():
                    inspect(archive.extractfile(member).read(), name+'!'+member.name, findings, counts)
        return
    if name.endswith('.zip'):
        counts['archives'] += 1
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            for member in archive.infolist():
                if not member.is_dir():
                    inspect(archive.read(member), name+'!'+member.filename, findings, counts)
        return
    if name.endswith('.gz'):
        counts['compressed_files'] += 1
        inspect(gzip.decompress(raw), name[:-3], findings, counts)
        return
    try:
        text = raw.decode('utf-8-sig')
    except UnicodeDecodeError:
        counts['binary_files'] += 1
        return
    if '\x00' in text:
        counts['binary_files'] += 1
        return
    counts['text_files'] += 1
    encoded_han = name.endswith(('.json', '.js', '.log')) and any(HAN.search(chr(int(m[1],16))) for m in ESCAPED.finditer(text))
    if HAN.search(name) or HAN.search(text) or encoded_han:
        findings.append(name)


def main():
    paths = subprocess.check_output(['git','-c','safe.directory='+ROOT.as_posix(),'-C',str(ROOT),'ls-files','-z']).decode().split('\0')
    findings = []
    counts = dict(archives=0, compressed_files=0, binary_files=0, text_files=0)
    for name in paths:
        if name:
            inspect((ROOT/name).read_bytes(), name, findings, counts)
    print(json.dumps(dict(counts=counts, files_with_chinese=findings), indent=2))
    raise SystemExit(bool(findings))


if __name__ == '__main__':
    main()
