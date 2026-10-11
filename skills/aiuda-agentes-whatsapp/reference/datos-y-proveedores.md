# Qué datos sí y no se envían a proveedores de IA

Estado **observado en el código** (2026-10-11) más las reglas que ya existen. Donde no hay regla escrita se dice
«VACÍO»; no se inventa una política. La norma y los controles legales viven en el skill hermano `aiuda-cumplimiento-spdp`.

## Proveedores en uso
| Proveedor | Para qué | Dónde |
|---|---|---|
| OpenAI (`gpt-4.1-mini`, `gpt-4.1`, `gpt-transcribe`/Whisper, visión) | agentes CRM/Academy/VIP, supervisor, redacción del motor, transcripción de audio, descripción de imágenes | crm-321, laundry-vip, postpro-321 |
| Google Gemini (capa gratis) | agente principal de aiuda-empresas | aiuda-empresas (`needsFallback` con OpenAI) |
| Anthropic (Claude) | motor principal de análisis/propuestas | creator |
| Higgsfield / Google Imagen / Runway | imágenes y video de marketing | crm-321, postpro-321, adsboom |
| Retell + Twilio | voz (llamadas con IA), grabación, transcripción, resumen | crm-321 |
| Meta (WhatsApp Cloud, Graph/Ads, Pixel, Conversions API) | mensajería y publicidad | todos |
| Chatwoot + n8n en Railway | bandeja y orquestación (propios) | todos |

## Reglas que SÍ existen
1. **La cédula de una persona natural nunca sale del servidor ni se guarda** (`lib/geoquito.ts`, `lib/municipio.ts`,
   LOPDP Art. 7.7). Del catastro no se devuelven datos del propietario salvo nombre cuando es base pública.
2. **EMP minimiza lo que ve el modelo:** el contexto del lead que recibe el agente incluye nombre, empresa, cargo,
   colaboradores, necesidad, urgencia y etapa; **no incluye teléfono ni RUC** (`src/server/agente.ts`). El agente nunca
   pide detalles del caso, documentos ni datos sensibles (CLAUDE.md regla 9; política de privacidad publicada en
   `src/app/privacidad/page.tsx`).
3. **Lo interno no sale (CRE):** costos, márgenes y notas internas nunca llegan al cliente; lo público pasa por
   `server/publico.ts`. El brief de proyecto (`server/proyecto.ts`) incluye entrevista textual y notas internas pero
   nunca costos ni márgenes, y no es público.
4. **Ningún secreto va al modelo ni al repo** (VIP y EMP tienen prueba anti-secretos; el secreto de n8n se compara en
   tiempo constante).
5. **Motor:** nunca mencionar propietarios, cédulas, teléfonos ni correos de terceros en contenido (REGLAS DURAS de
   `motor/redaccion.py`).
6. **Descargas de clientes y pedidos** solo superadmin/admin (VIP; datos personales, LOPDP).
7. **Aviso de datos** una vez, al pedir los datos de cierre (VIP); política de privacidad con derechos y eliminación
   (EMP `/privacidad`, `/eliminacion-de-datos`).
8. **LOPDP en prospección:** cada contacto con base legal y origen; sin listas compradas ni raspadas; baja en un paso;
   15 días para atender derechos (`docs/09` §5.5).
9. **Mensajes salientes del CRM pasan por el supervisor** que ve solo la ficha del lead (ver `supervisor.md`).

## Lo que HOY sí se envía a proveedores (para que decidas con datos)
- **VIP → OpenAI:** teléfono del cliente (`TELÉFONO DEL CLIENTE`) y nombre del perfil de WhatsApp dentro del prompt;
  historial de la conversación; texto de audios (transcripción) y fotos (descripción por visión).
- **CRM agente 321 → OpenAI:** historial, nombre, datos de calificación (presupuesto, ubicación), catálogo; el
  supervisor recibe la ficha (nombre, etapa, presupuesto estimado, monto de cotización, ubicación del proyecto).
- **Academy → OpenAI:** nombre de la persona, historial (30 mensajes), catálogo, respuestas del diagnóstico (hasta 700
  caracteres) e información pública de la academia.
- **EMP → Gemini/OpenAI:** datos de calificación del lead, historial, nombre del perfil, servicios y conocimiento de la
  organización.
- **Voz → Retell:** datos del lead como variables (nombre, servicio, presupuesto, ubicación, historial reciente).
- **Creator → Claude/OpenAI:** entrevista y respuestas del cliente (voz del cliente y del consultor por separado) y
  transcripción de audio por OpenAI (Anthropic no transcribe).

## VACÍOS (no hay regla escrita en los repos)
- Enmascarado de teléfono, nombre, RUC o correo antes de enviar a un modelo (solo EMP excluye teléfono y RUC por diseño).
- Política sobre uso de datos de la **capa gratis de Gemini** (EMP lo aprobó el 2026-10-09 como «privacidad aprobada: el
  agente solo pide datos de calificación, nunca detalles del caso»; no consta análisis de retención/entrenamiento).
- Retención de conversaciones, audios, grabaciones de llamadas y plazos de borrado.
- Registro por turno de modelo, versión de prompt, entrada enmascarada, salida y revisor (hoy solo hay costo/tokens en
  `ia_uso` y la Actividad del lead).
- Aviso de grabación y de carácter automatizado en voz; consentimiento para el Pixel en landings.
- Contratos/encargados del tratamiento con OpenAI, Google, Anthropic, Retell y Twilio; transferencias internacionales.
- Lista de exclusión (baja) única consultada por todos los emisores.
- Evaluación de impacto previa de cada módulo de IA.
Estos vacíos se tratan en `aiuda-cumplimiento-spdp`; no los resuelvas en un prompt: se resuelven en el núcleo.

## Regla práctica para cualquier agente nuevo
Envía al modelo solo lo que necesita para esa respuesta; no envíes cédula/RUC/correo/teléfono salvo necesidad
demostrada; nunca envíes secretos, costos ni márgenes; deja constancia del origen del dato; y si dudas, el dato no
va (regla C: si falta, se dice que falta).

## Origen
`/home/user/bcujano/aiuda-empresas/src/server/agente.ts`, `CLAUDE.md`, `docs/PLAN.md` §8, `src/app/privacidad/page.tsx` ·
`/home/user/bcujano/laundry-vip/n8n/prompt-agente-laundry.md`, `CLAUDE.md`, `docs/DECISIONES.md` ·
`/home/user/crm-321/src/lib/academy/agente.ts`, `src/app/api/supervisor/mensaje/route.ts`, `docs/09-marco-legal-avaluos.md` ·
`/home/user/bcujano/creator/CLAUDE.md`, `docs/DECISIONES.md` · `/home/user/postpro-321/motor/redaccion.py`.
