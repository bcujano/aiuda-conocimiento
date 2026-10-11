#!/usr/bin/env bash
# Copia skills y bloque de reglas del centro de conocimiento a un repositorio.
# Uso: ./sincronizar.sh /ruta/al/repo-destino
set -euo pipefail
FUENTE="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:?Indica la ruta del repo destino}"
[ -d "$DEST/.git" ] || { echo "No es un repositorio git: $DEST" >&2; exit 1; }
python3 "$FUENTE/consumo/validar.py" "$FUENTE" || { echo "El paquete no pasa la validación." >&2; exit 1; }
mkdir -p "$DEST/.claude/skills"
# Solo toca carpetas aiuda-*; no borra skills propios del repo.
for d in "$DEST"/.claude/skills/aiuda-*; do [ -d "$d" ] && rm -rf "$d"; done
cp -R "$FUENTE"/skills/aiuda-* "$DEST/.claude/skills/"
python3 - "$FUENTE/CLAUDE.base.md" "$DEST/CLAUDE.md" <<'PY'
import sys,re,os
base=open(sys.argv[1],encoding='utf8').read().strip()
ini,fin='<!-- AIUDA-CONOCIMIENTO:INICIO','<!-- AIUDA-CONOCIMIENTO:FIN -->'
path=sys.argv[2]
cur=open(path,encoding='utf8').read() if os.path.exists(path) else ''
if ini in cur and fin in cur:
    a=cur.index(ini); b=cur.index(fin)+len(fin)
    new=cur[:a]+base+cur[b:]
else:
    new=(cur.rstrip()+'\n\n' if cur else '')+base+'\n'
open(path,'w',encoding='utf8').write(new)
PY
echo "Sincronizado en $DEST. Revisa con git diff y abre una solicitud de revisión."
