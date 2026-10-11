# Supervisor de mensajes salientes (crm-321)

Archivo: `/home/user/crm-321/src/app/api/supervisor/mensaje/route.ts` (105 líneas). Plan de origen:
`/home/user/crm-321/docs/07-plan-crm-agentico.md` §1.3. Registro: `docs/04-registro-cambios.md` (entrada del supervisor en vivo).

## Contrato
- `POST` con cabecera `x-webhook-secret` (acepta `N8N_WEBHOOK_SECRET` y `N8N_WEBHOOK_SECRET_NUEVO`; comparación con
  `timingSafeEqual`). Sin secreto válido: 401.
- Entrada: `{ follow_up_id, lead_id | telefono, texto, manual, modo }`. `modo: 'vivo'` = respuesta del agente en tiempo
  real. El teléfono se normaliza a los últimos 9 dígitos y se prueba con `0`, `593` y `+593`.
- Salida: `{ decision: aprobar | reescribir | posponer | bloquear, texto_final, texto_template, motivo }`.
  `texto_template` = texto sin saltos de línea (apto para parámetro de plantilla).
- `maxDuration = 30`.

## Orden de decisión
1. Supervisor apagado en el Panel de Control (`activa('supervisor')`) → aprobar tal cual.
2. Reglas fijas (sin IA):
   - texto vacío → vivo: reescribir con la frase segura; no vivo: bloquear;
   - lead no encontrado → vivo: aprobar («solo revisión de contenido»); no vivo: bloquear («Lead inexistente»);
   - lead en etapa `cerrado*` y no vivo → bloquear;
   - `manual: true` (lo escribió una persona) → aprobar siempre;
   - no vivo y el cliente escribió hace menos de **6 h** → posponer (conversación activa con el agente);
   - no vivo y ya recibió un `seguimiento_auto` en las últimas **20 h** → posponer.
3. Revisión de IA: `gpt-4.1-mini`, temperatura 0, respuesta JSON. Entrada: FICHA del lead (id, nombre, stage,
   temperature, service_type, servicio_detalle, presupuesto_estimado, cotizacion_monto, ubicacion_proyecto,
   ultimo_inbound_at) + hasta 3 seguimientos anteriores + el texto.

## REGLAS DURAS que aplica el modelo
Si se violan: `reescribir` (si se puede quitando la parte problemática) o `bloquear`.
- Nada de precios, montos, descuentos, promociones ni plazos que no estén en la FICHA.
- Nada de promesas legales, contractuales o de resultados garantizados.
- No inventar proyectos, clientes, testimonios, cifras ni fechas.
- No mencionar la fecha ni la hora de una reunión o videollamada YA ocurrida (sí proponer agendar una nueva).
- Tono cordial y profesional, español de Ecuador, trato de «usted» o «tú» consistente, máximo 600 caracteres, sin sonar a spam.
- No repetir casi igual un seguimiento anterior.
- Si cumple todas, se aprueba **tal cual** (no editar por estilo, gusto ni para acortar).
- Un reescrito válido tiene >20 caracteres y se corta a 1000.

## Efectos
- `posponer`: reprograma el seguimiento +24 h (`scheduled_follow_ups.scheduled_at`).
- `bloquear`: cancela el seguimiento (`status: cancelled`) y notifica (`nivel: info`, departamento `seguimientos`) con el
  texto (500 caracteres) y enlace al lead.
- Cualquier decisión distinta de `aprobar` deja una nota en Actividad: «🛡️ Supervisor: {decision} — {motivo}» con
  `metadata {origen, decision, original, final}`.
- Cada revisión registra `ia_uso` (`modulo: supervisor_mensajes`, tokens y costo con $0,40 / $1,60 por millón).

## Modo vivo (el cliente está esperando)
- Nunca se pospone. `bloquear` del modelo se convierte en `reescribir` con la **frase segura**:
  «Déjame confirmar ese dato con el equipo y te respondo enseguida.»
- Si el supervisor falla (OpenAI caído): vivo → se **aprueba el original** (el agente ya tiene sus reglas);
  seguimiento → se **pospone** (nunca sale sin supervisar).
- Nodos n8n: «Supervisor Vivo» y «Texto Supervisado». Si el CRM falla, n8n envía el texto original.

## Límites conocidos (no presentados como arreglados)
- El supervisor no recibe el catálogo ni el contexto del anuncio: un precio correcto del catálogo puede parecer «fuera de
  la FICHA» y reescribirse. No hay prueba automatizada del supervisor en el repo (el CRM no tiene suite de tests).
- No revisa identidad (si el texto dice o no que es IA) ni lista de bajas: añadirlo es parte de la adecuación a la
  norma SPDP (ver `aiuda-cumplimiento-spdp`: todos los emisores deben consultar la misma lista de exclusión).
- Solo cubre mensajes de CRM/321 INMO. VIP usa su guardia `Extraer JSON`; Academy, su freno de links/montos/cuentas; EMP no
  tiene supervisor equivalente.
