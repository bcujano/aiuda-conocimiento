---
name: aiuda-orquestacion
description: Cómo coordinar varias sesiones o agentes de Claude sobre los repos de Aiuda sin que se pisen (migraciones, ramas, despliegues). Usar cuando haya más de una sesión activa, al repartir tareas entre repos o al numerar migraciones SQL.
---

# Orquestación de sesiones

Revisado: 2026-10-22 · Origen: choques reales de numeración de migraciones en crm-321 (055 y 063) por sesiones simultáneas.

## Reglas
1. **Un orquestador, varios ejecutores.** Una sola sesión reparte el trabajo; los ejecutores no se reparten entre sí.
2. **Un repo, un ejecutor a la vez.** Si dos tareas tocan el mismo repo, van una detrás de otra.
3. **Cada ejecutor trabaja en su propia rama o copia de trabajo (worktree)**, nunca en la misma carpeta que otro.
4. **Los números de migración SQL los asigna solo el orquestador.** El ejecutor pide el siguiente número; si no hay orquestador, usa el nombre con fecha y hora (`AAAAMMDDHHMM_tema.sql`) en vez de un correlativo.
5. **Antes de empezar, el ejecutor hace `git pull` y lee las últimas migraciones.** Si el número que iba a usar ya existe, renumera y lo reporta.
6. **Producción:** en repos cuyo despliegue sale de la rama principal (crm-321), todo cambio a esa rama es un despliegue. Solo sube lo que pasó tipos, pruebas y compilación.
7. **Cada ejecutor termina con el reporte estándar** (ver `aiuda-orden-de-trabajo`) y el orquestador lo contrasta contra el repo antes de marcar «verificada».

## No verificado
- Cuántos ejecutores en paralelo soporta el plan del dueño sin agotar su cuota: medir con 2 antes de subir.

## Lo que crm-321 aprendió en la práctica (2026-10-30, su CLAUDE.md «Trabajo entre sesiones»)
Choques reales: cambios sin subir apartados por otra sesión, `node_modules` vaciada a mitad de una compilación, un SQL en 0 bytes, el estudio local reiniciado por dos sesiones, y números de migración repetidos siete veces en 8 días. Reglas que lo resolvieron y que valen para todos los repos:
1. Cada sesión que edita trabaja en su propio worktree (`.claude/worktrees/<nombre>`), nunca en la carpeta principal.
2. Se sube seguido; nada a medias durante horas.
3. Lo de otra sesión no se toca ni se borra: se compara y se respeta (nada de `git reset --hard`, `push --force` ni `git clean` sobre trabajo ajeno).
4. Un dueño por área; el HANDOFF es por área (`docs/handoff/<área>.md`), no un archivo único.
5. Migraciones: solo con el script del repo (`node scripts/nuevo-sql.mjs nombre`), que lee el número más alto de GitHub, y se sube enseguida para reservarlo.
6. Si `main` está en rojo en CI, se arregla antes de subir otra cosa (hubo más de 12 subidas encima de rojo).
7. La revisión automática vigila números repetidos, archivos vacíos y marcas de conflicto.
Otros repos: copiar estas reglas y su script a su propio CLAUDE.md cuando tengan más de una sesión activa.
