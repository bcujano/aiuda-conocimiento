<!-- AIUDA-CONOCIMIENTO:INICIO (no editar a mano; lo regenera la sincronización) -->
## Reglas universales de Aiuda
- Los skills `aiuda-*` de `.claude/skills/` aplican a todo trabajo en este repo. Si una tarea toca seguridad, datos personales, diseño, textos al cliente, agentes de WhatsApp o competencia, úsalos antes de escribir código.
- Habla al usuario en español, con tildes y ñ, en lenguaje de cliente: qué hacer, no cómo está hecho por dentro. No reveles el stack interno (Chatwoot, n8n, etc.) en pantallas ni textos para clientes.
- Nunca imprimas, copies ni subas valores de claves o tokens. Si encuentras uno expuesto, repórtalo sin repetirlo.
- Todo sistema cumple SPDP-SPD-2026-0009-R y la LOPDP: todo asistente automático que habla con una persona se presenta como «asistente virtual automático» en el primer mensaje, ofrece pasar con una persona y nunca niega serlo si le preguntan; ver `aiuda-cumplimiento-spdp`.
- Ningún número lo inventa un modelo: sale de datos del sistema con su origen, o se dice que falta.
- Trabaja en rama y con solicitud de revisión; no hagas push directo a la rama principal ni reescribas historial.
- Corre pruebas, tipos y compilación antes de decir que algo está listo; reporta lo que no pudiste verificar.
- Si descubres una regla o técnica útil para otros sistemas, no la guardes solo aquí: déjala como propuesta (`aiuda-actualizar-conocimiento`).
- Si un skill contradice lo que ves en el código, avisa en tu reporte; no lo ignores en silencio.
- Si el usuario dice «ponte al día»: lee `orquesta/LEEME.md` del repo bcujano/aiuda-conocimiento (solo lectura) y sigue su protocolo: ejecuta la primera tarea pendiente de ESTE repo y deja tu reporte en `.aiuda/reportes/`.
<!-- AIUDA-CONOCIMIENTO:FIN -->
