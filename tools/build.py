"""Dependency-free source assembly. Run from any directory."""
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
APP=ROOT/'tarnstead' if (ROOT/'tarnstead').is_dir() else ROOT
SRC=APP/'src'
manifest=json.loads((SRC/'manifest.json').read_text())
assert len(manifest)==len(set(manifest))
parts=[]
index=['# Codekaart (gegenereerd)\n','Zoek eerst de functienaam hieronder; lees daarna alleen het relevante bronbestand.\n']
for name in manifest:
    text=(SRC/name).read_text()
    parts.append(text)
    index.append('\n## '+name+'\n')
    for number,line in enumerate(text.splitlines(),1):
        symbols=re.findall(r'(?:function\s+([A-Za-z_$][\w$]*)\s*\(|^([A-Za-z_$][\w$]*)\s*=\s*function)',line)
        if symbols:index.append(f'- {number}: '+', '.join(a or b for a,b in symbols)+'\n')
outputs={APP/'dist/app.js':''.join(parts),APP/'dist/style.css':(SRC/'style.css').read_text(),SRC/'INDEX.md':''.join(index)}
if '--check' in sys.argv:
    stale=[str(p.relative_to(ROOT)) for p,text in outputs.items() if not p.exists() or p.read_text()!=text]
    if stale:raise SystemExit('Build verouderd: '+', '.join(stale))
else:
    for p,text in outputs.items():p.write_text(text)
print('Broncode en distributie gecontroleerd.' if '--check' in sys.argv else 'Broncode samengevoegd; codekaart bijgewerkt.')
