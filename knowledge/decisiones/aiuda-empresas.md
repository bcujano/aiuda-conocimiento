# Decisiones cerradas y «no hacer» — aiuda-empresas

Plataforma multicliente de Aiuda: anuncios en Meta → agente de IA en WhatsApp → reunión agendada, con un CRM por cliente.
Primer cliente: Fagal Abogados. Repo: `/home/user/bcujano/aiuda-empresas`. Stack: Next 16, React 19, TS 6, Tailwind 4, Biome,
Vitest, Supabase, Vercel; n8n + Chatwoot en Railway; Gemini (principal) + OpenAI (respaldo).
Leer primero: `docs/PLAN.md` y `docs/PUESTA-EN-MARCHA.md`.

## Reglas de CLAUDE.md (10)
1. **Un cliente = una organización (datos), nunca código.** Nombres, textos y números de un cliente viven en la base
   (`organizaciones`, `angulos`, `conocimiento`), nunca en el código.
2. **Aislamiento:** toda consulta de `src/server/**` filtra por `organizacion_id`. RLS niega todo por defecto (respaldo); el servidor usa service_role.
3. **Permisos = rol × plan**, decididos en el servidor (`lib/auth.ts::permite`); la pantalla solo oculta.
4. `src/app/**` nunca importa `lib/supabase/admin.ts`: pasa por `src/server/**`.
5. Migraciones aplicadas **nunca se editan**: cambio = archivo nuevo en `supabase/migrations/`.
6. Gate antes de subir: `pnpm lint`, `typecheck`, `test`, `build`.
7. **Máximo 300 líneas por archivo.** Sin ORM, sin librería de fechas (Quito UTC-5 fijo).
8. **WhatsApp: nunca escribimos primero**; solo dentro de la ventana gratis (**72 h anuncio, 24 h otro**).
9. **El agente no da asesoría, no promete resultados y nunca pide detalles del caso.**
10. Ningún secreto en el repo.
Cómo trabaja Byron: español con tildes y ñ en código/comentarios/commits/interfaz; sin paradas; recomendaciones, no menús;
«no ejecutes aún» = analizar y proponer sin tocar. Origen: `/home/user/bcujano/aiuda-empresas/CLAUDE.md`.

## Decisiones cerradas (Byron, 2026-10-09, `docs/PLAN.md` §8)
1. **Número propio para Fagal** con su propio agente; el anuncio es de Aiuda y lleva a ese WhatsApp con el logo de Fagal;
   Fagal autorizó el uso de su nombre y marca.
2. **Privacidad aprobada:** el agente solo pide datos de calificación, nunca detalles del caso. Gemini capa gratis + OpenAI de respaldo.
3. **Supabase en cuenta nueva** (de Aiuda).
4. **Cuestionario = wizard** dentro de la app.
5. **CRM con prueba gratis de 3 meses**; después se paga o queda restringido/suspendido (avisos a 30 y 7 días).
6. Roles superadmin / admin / operador. Landings en la misma app (`/<slug>`, `/<slug>/<angulo>`), sin subdominio.
Otras (PLAN §3–§7): filtro en dos capas (el anuncio habla a gerentes y dueños de empresas con equipo; el agente pregunta
tamaño y cargo antes de ofrecer la reunión); métrica de decisión cada 7 días en el CRM: costo por conversación → % calificadas →
**costo por reunión agendada**; gana el ángulo con menor costo por reunión; ángulos finales se confirman con el wizard de Fagal
(solo se anuncia lo que Fagal realmente hace y cobra bien); Vercel Hobby no permite uso comercial → Pro con el primer cliente que
pague; WhatsApp $0 dentro de la ventana, **no se usan plantillas**; pauta $60–90/mes.

## Reglas del agente (n8n SDK, 12 reglas)
Usted, ≤3 frases, una pregunta · sin asesoría legal ni honorarios · nunca pide detalles del caso/documentos/datos sensibles ·
nombre solo el que dijo la persona · particulares/trabajadores contra empleador/`no_para_quien` → descarte con motivo · no inventar
datos del estudio · agenda solo con horas de `ver_horarios` en ese turno · no decir «agendada» sin `ok=true` · reprogramar si hay
cita vigente · audio/archivo → pedir texto · una sola disculpa. Etiqueta `humano` apaga al agente. Tope **40 mensajes/día por
persona** (`TOPE_MENSAJES_DIA`). Origen: `n8n/agente-aiuda-empresas.sdk.ts`, `src/server/agente-reglas.ts`.
**Identidad:** hoy «asistente virtual» y solo lo afirma si preguntan → reemplazado por la regla de IA en el primer mensaje
(skill `aiuda-agentes-whatsapp` §1, §13).

## Datos y arquitectura
- Tablas con `organizacion_id`: `organizaciones`, `usuarios`, `conocimiento`, `angulos`, `leads`, `calificaciones`, `citas`,
  `mensajes`/`actividad`, `uso_ia`. Atribución: `referral.source_id` en los `meta_ad_ids` del ángulo, o referencia (`FAG-TRI`)
  en el texto; sin pista → `null`, **nunca se adivina**.
- El cerebro vive en el CRM (`/api/agente/contexto`, `/lead`, `/agendar`...); **nada del negocio escrito en el prompt**.
- El contexto del modelo **no incluye teléfono ni RUC** del lead.
- Los workflows de 321, Academy y Laundry VIP **no se tocan**; n8n y Chatwoot de Railway ya existen; el webhook va a n8n y
  **no se conecta a Chatwoot** el número de Fagal directamente.
- Recordatorios de cita: 24 h y 2 h antes (n8n cada 15 min); organizaciones suspendidas no reciben.
- Puesta en marcha manual (2026-10-10): Byron pega `supabase/instalar-todo.sql` y crea el usuario superadmin; luego solo migraciones nuevas.

## «No hacer»
- Escribir un nombre, texto o número de un cliente en el código.
- Consultar sin filtrar por `organizacion_id`; importar `supabase/admin` desde `src/app`.
- Editar una migración aplicada; pegar el paquete completo `instalar-todo.sql` otra vez.
- Escribir primero a un lead; usar plantillas (no se usan); responder fuera de la ventana de 72 h/24 h.
- Archivos de más de 300 líneas; ORM; librería de fechas.
- Que el agente opine sobre el caso, dé honorarios o pida documentos.
- Adivinar el ángulo cuando no hay pista.
- Subir cualquier secreto (tokens de Meta, service_role) al repo: van a Vercel.
- Usar Vercel Hobby con un cliente que paga.

## Vacíos y contradicciones
- PLAN §5 menciona herramientas `contexto_organizacion`, `registrar_lead`, `calificar_lead`, `horarios_disponibles`,
  `agendar_reunion`, `escalar_a_persona`; el workflow real tiene solo `ver_horarios` y `agendar_cita` (el escalamiento por
  etiqueta `humano` existe en el flujo, pero el agente no tiene una herramienta explícita de escalar).
- PLAN: audio con transcripción «igual que Academy»; el flujo real pide escribir texto.
- Sin CI (`.github` ausente) aunque la regla 6 pide el gate; sin tope de gasto en dólares, solo de mensajes.
- La política de privacidad ya dice que las respuestas iniciales las da un asistente virtual **con inteligencia artificial**
  (`src/app/privacidad/page.tsx`); el prompt no lo dice al inicio de la conversación.

## Origen
`/home/user/bcujano/aiuda-empresas/CLAUDE.md`, `docs/PLAN.md`, `docs/PUESTA-EN-MARCHA.md`, `n8n/agente-aiuda-empresas.sdk.ts`,
`src/server/agente-reglas.ts`, `src/server/agente.ts`, `src/server/recordatorios.ts`, `src/app/privacidad/page.tsx`, `docs/clientes/fagal/whatsapp-perfil.md`.
