#!/usr/bin/env python3
"""Valida el paquete: frontmatter de cada skill y ausencia de datos sensibles."""
import re,sys,pathlib
raiz=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '.')
err=[]
pat={'clave/token':re.compile(r'(sk-[A-Za-z0-9]{20,}|eyJ[A-Za-z0-9_-]{30,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|xox[bp]-[A-Za-z0-9-]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY)'),
     'teléfono EC':re.compile(r'(?<!\d)(\+?593\s?9\d{8}|09\d{8})(?!\d)'),
     'correo':re.compile(r'[A-Za-z0-9._%+-]+@(?!example\.)[A-Za-z0-9.-]+\.[a-z]{2,}')}
for sk in sorted((raiz/'skills').glob('*/SKILL.md')):
    t=sk.read_text(encoding='utf8')
    m=re.match(r'---\n(.*?)\n---\n',t,re.S)
    if not m: err.append(f'{sk}: sin frontmatter');continue
    fm=m.group(1)
    n=re.search(r'^name:\s*(\S+)\s*$',fm,re.M); d=re.search(r'^description:\s*(.+)$',fm,re.M)
    if not n or n.group(1)!=sk.parent.name: err.append(f'{sk}: name no coincide con la carpeta')
    if not d: err.append(f'{sk}: sin description')
    elif len(d.group(1).strip().strip('"\''))>400: err.append(f'{sk}: description de {len(d.group(1))} caracteres (máx. 400)')
    if t.count('\n')>500: err.append(f'{sk}: más de 500 líneas')
for f in raiz.rglob('*'):
    if f.is_file() and f.suffix in ('.md','.json','.sh','.py','.yml','.yaml') and 'validar.py' not in f.name:
        txt=f.read_text(encoding='utf8',errors='ignore')
        for k,p in pat.items():
            for mm in p.finditer(txt): err.append(f'{f.relative_to(raiz)}: posible {k}: {mm.group(0)[:6]}…')
if err:
    print('\n'.join(err));sys.exit(1)
print('Paquete válido.')
