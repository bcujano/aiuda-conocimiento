# Decisiones cerradas y «no hacer» — laundry-vip (VIP Laundry)

CRM interno + backend de un agente de IA en WhatsApp para una lavandería de barrio en La Kennedy, Quito. **En producción con
clientes reales.** Repo: `/home/user/bcujano/laundry-vip`. Antes de tocar nada: `docs/CONTINUIDAD.md`; si tocas el agente:
`docs/AGENTE.md` y `docs/DECISIONES.md` (no revertir decisiones sin preguntar al dueño; no reintroducir los fallos de §2).
Stack: Next 16, React 19, TS 6, Tailwind 4, Biome, Vitest, Playwright, pnpm, Node 24; Supabase crudo sin ORM; n8n + Chatwoot
(cuenta 3) + WhatsApp Cloud API; OpenAI `gpt-4.1-mini` y `gpt-transcribe`.

## Quién manda
El dueño y superadmin es Byron. **La dueña del negocio en la operación diaria es María Sol Játiva** (administradora): lo que
ella ordena sobre horario, cobertura, precios y plazos manda sobre el prompt; el agente la trata de usted y por su nombre.

## Reglas del proyecto (CLAUDE.md, 15)
1 Gate por fase (typecheck, lint, test, build; una advertencia tolerada se vuelve permanente) · 2 **máximo 300 líneas por archivo**
· 3 sin Docker, sin ORM, sin librería de fechas (`Intl`, Quito UTC-5), sin SDK de OpenAI dentro del CRM (lo hace n8n) ·
4 **migraciones aplicadas nunca se editan** · 5 `src/app/**` no importa `lib/supabase/admin.ts`; `src/server/**` no importa React ·
6 `scripts/` no usa alias `@/` · 7 ningún secreto en el repo (hay prueba) · 8 **la base es una sola** (pruebas y producción): ninguna
prueba usa ni borra un número real ni depende de un valor que el dueño edita; los precios esperados se leen de la base
(`tests/util/catalogo.ts`) · 9 **el CRM es la fuente de verdad** del catálogo y la configuración; ningún script revierte lo que el
dueño cambió · 10 **nada de dinero por WhatsApp** (excepción 2026-09-30: aviso informativo de discrepancia armado por el servidor,
dentro de las 24 h) · 11 n8n se cambia por MCP solo sobre el workflow autorizado, nunca reimportando · 12 TSX con la herramienta
Edit, no con reemplazos masivos · 13 **lo que el agente promete sale de Configuración; lo que tiene consecuencias lo hace cumplir
el servidor** · 14 cada frase real que falle se convierte en prueba antes de arreglarla; tras subir un prompt, `verificar-prompts.cjs`
· 15 el agente no niega un servicio, no inventa el nombre del cliente y no miente si le preguntan de frente si es una persona.
Origen: `CLAUDE.md`.

## Regla imperativa sobre 321
**No se toca nada de 321 (workflows, credenciales, tablas, cuenta 1 de Chatwoot, ni siquiera para leer). Nunca.** VIP vive en la
cuenta 3 y en credenciales propias; solo se crean cosas nuevas. Comparte instancias de n8n y Chatwoot, y OpenAI (temporal, acordado).

## Decisiones del dueño (no revertir sin preguntarle; `docs/DECISIONES.md` §1)
- El agente es el workflow de 321 **clonado y recortado**; AI Agent de LangChain, no «Tool First»; registro en el CRM en cada turno.
- Tres roles (`superadmin` / `admin` / `operador`); contraseña en vez de enlace mágico; descargas solo superadmin/admin (LOPDP).
- **Dinero:** nada por WhatsApp (2026-09-17, tras una orden inventada con ID falso); excepción del aviso de discrepancia (2026-09-30).
- Resumen diario de las 8:00 para admins, texto libre dentro de las 24 h; la plantilla `resumen_diario_admin` no existe.
- Nombre de WhatsApp = nombre **provisional** del lead; el que diga el cliente lo reemplaza; lo que escribe el equipo no se pisa.
- **El CRM manda sobre catálogo y configuración**; el catálogo: 13 categorías, 54 ítems (`catalogo-lavanderia.xlsx`), nombres no tocados.
- Cada prenda declara método (agua / seco). Promoción por cantidad en columnas, nunca en el prompt (cobijas $5,00 c/u o 3 por $12,00).
- **No hay «combo» ni «a la carta»** («no somos un restaurante»); valores en la base se conservan, pantalla muestra `entregaLegible`.
- Tarifa única de recogida y entrega, aparte del lavado ($2,50 **por pedido**, siempre que la lavandería haga al menos un tramo).
- **Plazo por servicio** (2026-10-09): agua y ropa de cama 24 h; seco, cuero, plumas, tinturado, calzado, peluches y mochilas 72 h;
  alfombras 1 semana hábil; desde que llega a planta, sin domingos ni feriados.
- Horario: recolección L–S 9:00–17:00 (2026-10-05); local 9:00–19:00 y sábados hasta las 17:00; se recoge a 2,5 km a la redonda
  (36 sectores de OpenStreetMap); fuera del radio se ofrece traer y retirar sin recargo.
- Peso en **libras**, ropa de diario al peso ($0,70/lb), **cortinas por kilo**. Siempre un estimado en dólares y después «se verifica en planta».
- Nombre del negocio «VIP Laundry» sale de Configuración. Saludo de la casa (campo «Saludo»), resto variado.
- **Recogida y entrega siempre en auto; el agente no pregunta cuántas fundas** (tool `calcular_vehiculo` eliminada, 2026-10-01).
- **Seguimiento** a quien no contesta: 5 min, 1 h, 6 h y 23 h 30 dentro de 24 h; el primero a los 5 minutos (no a 30) y resume el lead
  a la dueña; solo con el local abierto y nunca en el almuerzo; quien contrata o rechaza, no recibe más; barrido del primer seguimiento
  a todos los leads con ventana abierta.
- **Catálogo en imagen:** NO lo genera el CRM; usa la imagen que el dueño pone en Drive (`public/catalogo.png`) como foto nativa (adjunto).
- Motor del agente: **OpenAI `gpt-4.1-mini` principal, Gemini de respaldo** (Gemini flash-lite inventó precio y plazo). `gpt-transcribe`
  para audio, **nunca `whisper-1`**. Para reintentar Gemini: `MOTOR_PRINCIPAL` en `n8n/generador/modelos.cjs` + simulador.
- Cuestionario de María Sol (2026-10-09): tolerancia de peso = la mayor entre 10 % y 2 libras; respuesta humana «en unos 30 minutos»;
  **cancelar con ropa ya recogida se cobra por tramo ($2,50 cada uno)**; servicios fuera del catálogo: «lo confirmo con el equipo», nunca
  se niegan; no se cargan «2 ternos por $15» ni «2 edredones por $10»; Daniel sube a administrador; «hoy a partir de las 9:00».
- **Identidad:** hoy «habla como una persona del local, no se anuncia como asistente virtual» pero **no miente si le preguntan de frente**.
  **Reemplazado** por la regla de IA en el primer mensaje (skill `aiuda-agentes-whatsapp` §1, §13); hay que actualizar
  `tests/unit/workflow-laundry-agente.test.ts` y `n8n/prompt-agente-laundry.md`.
- El aviso de la ley de datos va **al pedir los datos del cierre**, no en el saludo.
- Base entregada **en cero**; no cargar datos de ejemplo (`pnpm db:demo`, con teléfonos de mentira) sin permiso del dueño.
- Session pooler de Supabase (la conexión directa es solo IPv6).

## Procesos
- Cambiar el agente: editar `.md`/generador → `node n8n/generador/generar.cjs` («OK: 116 nodos») → `pnpm biome check --write n8n`
  → gate → subir por MCP con `setNodeParameter` (`/options/systemMessage`) y `publish_workflow` → `verificar-prompts.cjs` →
  `verificar-errores.cjs` → `pnpm chatwoot:revisar`. Probar con `scripts/simular-cliente.ts` antes de dejar publicado.
- Coexistencia persona–agente: usuario propio «Agente VIP»; cualquier otro remitente pone la etiqueta `humano`.
- «Deja todo listo para la siguiente sesión» = reescribir `docs/CONTINUIDAD.md` verificado contra producción + prompt de arranque.
- Tope diario de mensajes por teléfono (`mensajes_diarios`), contado antes de ejecutar; gasto diario avisa pero no corta: poner tope
  duro en la cuenta de OpenAI.

## «No hacer» (fallos ya ocurridos; `docs/DECISIONES.md` §2)
Inventar órdenes/precios/plazos sin herramienta · decir «no ofrecemos X» · prometer recogida «en todo Quito» o fuera de zona ·
horario o dirección de memoria · cerrar pedido sin dirección o con nombre inventado · cotizar por prenda la ropa de diario ·
preguntar «¿cuántas fundas?» · responder dos veces seguidas · responder encima de una persona · pruebas que usan números reales o
precios escritos · reemplazos masivos con `node -e` en TSX · transcribir prompts a mano al MCP · usar `whisper-1` · reimportar el
JSON de n8n · exportar un helper desde un archivo `'use server'` · dejar el JSON de referencia de 321 (con credencial) en git ·
usar el token de Byron para publicar desde el agente o scripts de barrido · pruebas con fecha fija.

## Origen
`/home/user/bcujano/laundry-vip/CLAUDE.md`, `docs/DECISIONES.md`, `docs/AGENTE.md`, `docs/CHATWOOT_Y_WHATSAPP.md`,
`n8n/prompt-agente-laundry.md`, `n8n/prompt-operador-laundry.md`, `tests/unit/workflow-laundry-agente.test.ts`, `.github/workflows/ci.yml`.
