---
name: aiuda-orden-de-trabajo
description: Plantilla de orden de trabajo y de reporte entre la sesión auditora y las sesiones ejecutoras de cada sistema. Usar al recibir o redactar una orden, al ejecutar una tarea de la ruta o al reportar evidencia de lo hecho.
---

# Órdenes de trabajo y reportes

Revisado: 2026-10-11 · Responsable: dueño de Aiuda · Fuente de verdad: este repo (los demás repos reciben una copia).

## Roles
- **Auditor:** redacta la orden, verifica el resultado. No ejecuta.
- **Ejecutor (sesión del sistema):** hace el trabajo en su repo y reporta con evidencia.
- **Dueño:** acciones humanas (consolas, aprobar y unir PR, legal, contador, pagos).

## Estructura de una orden
1. **Contexto:** qué sistema, por qué (hallazgo de la auditoría con su ruta).
2. **Tarea:** pasos numerados, pequeños.
3. **Restricciones:** lo que NO se toca.
4. **Hecho cuando:** criterios verificables.
5. **Reporte esperado:** archivos cambiados, comando de verificación y su resultado.

## Reglas del ejecutor (siempre)
- Trabajar en una **rama** y abrir un **PR**. Nunca push directo a la rama principal.
- **Nunca imprimir ni copiar valores de secretos**; reportar solo rutas y cantidades.
- Una sola sesión ejecutora por repo a la vez; si otra sesión toca el mismo repo, avisar al dueño.
- Nada en producción ni en consolas externas sin la aprobación explícita del dueño.
- No tocar el historial de git salvo orden expresa.
- Correr las pruebas y el CI antes de reportar. Si algo no se pudo probar, decirlo.
- Aplicar los skills `aiuda-*` que correspondan (seguridad, cumplimiento, lenguaje de cliente, diseño, etc.).
- Si aprendes algo reutilizable, no lo guardes aquí: propónlo con el skill `aiuda-actualizar-conocimiento`.

## Formato del reporte
```
Tarea: <id y título>
Estado: hecha / parcial / bloqueada
Archivos cambiados: <rutas>
PR: <enlace>
Verificación: <comando> -> <resultado>
No verificado: <lo que no se pudo probar>
Bloqueos o decisiones para el dueño: <lista>
```

## Estados de una tarea en el Centro de Mando
pendiente → en ejecución → hecha (declarada por el ejecutor o el dueño) → **verificada** (por el auditor con evidencia).
