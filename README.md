# Centro de conocimiento Aiuda

Fuente única de lo que Claude debe saber en cualquier sesión de cualquier sistema de Aiuda: reglas de diseño, comportamientos, normas, skills y repos útiles.

## Cómo está armado
- `skills/` — un skill por tema (`aiuda-*`). Claude los activa solo cuando la tarea coincide con la descripción. Es lo que se copia a cada repositorio.
- `CLAUDE.base.md` — bloque corto de reglas universales que se pega en el `CLAUDE.md` de cada repositorio.
- `knowledge/` — decisiones por repositorio y material de apoyo (no se copia a los repos; lo consultan las sesiones auditoras).
- `propuestas/` — buzón: las sesiones dejan aquí propuestas de skills nuevos o cambios. Nada entra al paquete sin revisión humana.
- `consumo/` — cómo llega todo a cada repo: script de sincronización, acción programada, ejemplo de configuración y plugin opcional.
- `consumo/validar.py` — revisa nombre, descripción y que no haya claves ni teléfonos antes de subir.

## Flujo
1. Alguien (tú o una sesión) propone un cambio en `propuestas/`.
2. Se revisa una vez por semana: aceptar, corregir o descartar.
3. Lo aceptado pasa a `skills/` con una solicitud de revisión. Se actualiza `CHANGELOG.md`.
4. La sincronización abre una solicitud de revisión en cada repo con la diferencia.

## Reglas del paquete
- Cero claves, teléfonos, correos ni datos de clientes.
- Cada afirmación con fuente o marcada como no verificada.
- Descripción de cada skill: qué hace y cuándo usarlo, en menos de 400 caracteres.
- SKILL.md de menos de 500 líneas; el detalle va en `reference/`.
