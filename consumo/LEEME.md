# Cómo llega el conocimiento a cada sistema

**Mecanismo recomendado (verificado en la documentación de Claude Code):** copiar los skills a `.claude/skills/` de cada repositorio y pegar el bloque corto en su `CLAUDE.md`. Funciona en sesiones locales y en la nube porque viaja con el repo.

1. Crear el repo privado `aiuda-conocimiento` y subir este paquete.
2. Por cada repo: `consumo/sincronizar.sh /ruta/al/repo`, revisar `git diff`, abrir solicitud de revisión.
3. Para que se mantenga solo: copiar `consumo/sincronizar.yml` a `.github/workflows/` de cada repo y crear el secreto `CONOCIMIENTO_TOKEN`.
4. Probar: sesión nueva (local y nube) pidiendo algo que active un skill.

**Opcional, sin probar en la nube:** plugin/marketplace de organización (`consumo/plugin/`). Úsalo solo si lo pruebas primero; no dependas de él.
**No sirve para compartir:** la memoria automática de Claude es por persona/proyecto, no se comparte entre sistemas.

## Cómo llega lo que aprende cada sesión al centro (verificado 2026-10-11, docs de Claude Code)
- Las sesiones en la nube solo escriben en los repos adjuntos: no pueden abrir un PR en el centro. Por eso la sesión deja `.aiuda-propuestas/*.md` en su propio repo y `consumo/enviar-propuestas.yml` lo reenvía al centro cuando el dueño une el PR. Dos aprobaciones humanas: el PR del repo y el PR del centro.
- La memoria automática de Claude no sale de la máquina ni llega a la nube: no sirve como canal.
- Los hooks del repo corren en la nube solo si la sesión tiene **un** repo. No depender de ellos.
- Traer skills del centro al iniciar la sesión no es fiable en la nube; por eso se copian dentro de cada repo.
- Plugins de repo no se instalan en la nube; solo los «server-managed» de claude.ai (Team/Enterprise).
- Sin verificar: que la Action abra PR en otro repo con ese token (probar en un repo primero) y cuántos skills soporta una sesión.
- Límites: descripción hasta 1.536 caracteres, SKILL.md menos de 500 líneas, CLAUDE.md menos de 200.
