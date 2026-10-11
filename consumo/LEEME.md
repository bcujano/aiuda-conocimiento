# Cómo llega el conocimiento a cada sistema

**Mecanismo recomendado (verificado en la documentación de Claude Code):** copiar los skills a `.claude/skills/` de cada repositorio y pegar el bloque corto en su `CLAUDE.md`. Funciona en sesiones locales y en la nube porque viaja con el repo.

1. Crear el repo privado `aiuda-conocimiento` y subir este paquete.
2. Por cada repo: `consumo/sincronizar.sh /ruta/al/repo`, revisar `git diff`, abrir solicitud de revisión.
3. Para que se mantenga solo: copiar `consumo/sincronizar.yml` a `.github/workflows/` de cada repo y crear el secreto `CONOCIMIENTO_TOKEN`.
4. Probar: sesión nueva (local y nube) pidiendo algo que active un skill.

**Opcional, sin probar en la nube:** plugin/marketplace de organización (`consumo/plugin/`). Úsalo solo si lo pruebas primero; no dependas de él.
**No sirve para compartir:** la memoria automática de Claude es por persona/proyecto, no se comparte entre sistemas.
