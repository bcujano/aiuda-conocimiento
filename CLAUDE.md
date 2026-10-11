# aiuda-conocimiento

Fuente única de skills y reglas de Aiuda. Lee `README.md` y `consumo/LEEME.md` primero.

## Reglas de este repo
- Todo cambio entra por rama y solicitud de revisión; el dueño aprueba. Nada se sube directo a `main`.
- Antes de proponer o fusionar: `python3 consumo/validar.py .` debe decir «Paquete válido».
- Cero claves, teléfonos, correos ni datos de clientes. Cada afirmación con fuente o marcada como no verificada.
- Los skills van en `skills/<nombre>/SKILL.md` (menos de 500 líneas, descripción de menos de 400 caracteres que diga qué hace y cuándo usarlo); el detalle va en `reference/`.
- Lo aprendido en otras sesiones llega como archivo en `propuestas/` (ver `skills/aiuda-actualizar-conocimiento`). Si una propuesta contradice un skill, regístralo en `knowledge/contradicciones-abiertas.md`; no lo resuelvas en silencio.
- Cada cambio aceptado se anota en `CHANGELOG.md`.
