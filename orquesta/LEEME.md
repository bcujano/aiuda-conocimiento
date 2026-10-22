# Ponte al día (protocolo de las sesiones ejecutoras)
Cuando el dueño diga «ponte al día»:
1. Clona (solo lectura) `bcujano/aiuda-conocimiento` y lee `orquesta/COLA.md`.
2. Toma la primera tarea **pendiente de ESTE repo** (el nombre del repo actual). Si no hay, di «sin pendientes» y termina. Si la tarea de arriba es de otro repo, no la toques.
3. Lee su orden en `orquesta/ordenes/` y ejecútala en una rama `claude/<tema>`.
4. Al terminar, escribe el reporte en `.aiuda/reportes/<número-de-orden>.md` de este repo, en la misma rama, con commit. No hace falta que el dueño lo pegue a nadie: el auditor lo lee.
5. Antes de subir a la rama principal de un repo que despliega a producción, muestra un resumen de 10 líneas y espera el «ok» del dueño en esta sesión.
6. Responde al dueño con 5 líneas: qué hiciste, qué falta, qué decidir.
Una sola tarea por vez. Nunca toques un repo ajeno.
