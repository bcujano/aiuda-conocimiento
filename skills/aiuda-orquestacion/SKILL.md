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
