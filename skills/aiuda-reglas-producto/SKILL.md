---
name: aiuda-reglas-producto
description: Reglas de producto, datos y código de la plataforma AIUDA (crm-321, aiuda-empresas, laundry-vip, creator, adsboom, postpro-321). Úsala al escribir pantallas, migraciones, tests, prompts o cálculos en cualquiera de esos repos, o al decidir de dónde sale un precio o un número.
---

# Reglas de producto, datos y código de AIUDA

Fuente única de las reglas que Byron (dueño) fijó y que aplican a todo lo que se construya. Cada regla
dice **a qué repos aplica**. Si una regla no aplica al repo donde trabajas, no la fuerces.

Claves de repos: **CRM** = crm-321 · **EMP** = aiuda-empresas · **VIP** = laundry-vip · **CRE** = creator ·
**ADS** = adsboom · **MOTOR** = postpro-321 (motor Python de contenido). **TODOS** = los seis.

Antes de tocar un repo lee su CLAUDE.md y su doc de estado (rutas en `reference/convenciones-codigo-por-repo.md`).
Si algo choca entre documentos de un mismo repo, manda el más reciente y el que dice «manda» (en CRM:
`docs/HANDOFF.md` > `docs/12-pendientes.md` > mapa `docs/08-mapa-del-sistema/` > `CLAUDE.md`).

## 1. Reglas de producto (no se negocian)

| # | Regla | Aplica a |
|---|---|---|
| A | **Todo término en pantalla lleva su icono de ayuda** con las cuatro líneas: qué es · de dónde sale · cómo afecta · ejemplo. Se define en `src/lib/glosario.ts` y se muestra con `<Ayuda termino="clave" />`. Un término sin ayuda es un error, igual que un `any` sin justificar. | CRM (obligatoria); recomendada en el resto al crear pantallas con jerga |
| B | **Todo resultado se interpreta solo (R1).** Cada pantalla con datos lleva un bloque `<Lecturas>`: plegable, **cerrado por defecto**, sin repetir lo visible, dice qué decisión sale y **con qué cruzarlo** (`cruzar`, con enlace directo). Viven en `src/lib/lecturas*.ts`. | CRM |
| C | **Ningún número lo escribe un modelo de lenguaje.** Toda conclusión es una cuenta sobre datos que el sistema ya tiene, con su origen. Si falta el dato, la lectura **no aparece** y se dice que falta. Nunca se rellena ni se estima en silencio. | TODOS (en CRE: «los montos los calcula el código»; en VIP: «lo que tiene consecuencias lo hace cumplir el servidor») |
| D | **Escrito para el usuario, no para el desarrollador.** «Los leads sin teléfono», nunca «el campo `telefono`». No se explica cómo está hecho el sistema: se dice qué hacer. | TODOS (UI y textos al cliente) |
| E | **Una función, un lugar.** Leads se clasifican solo con `lib/clasificacion.ts`; precios solo del Catálogo 321; el agente de WhatsApp lee del CRM (`/api/agente/contexto`). Nada de listas paralelas. | CRM (nominal); el principio aplica a todos: VIP → catálogo en la base, EMP → `conocimiento`, CRE → `lib/precios.ts` |
| F | **Fuente del dato.** Todo número usa `lib/fuente-dato.ts`: dato 321 si pasa el mínimo; si no, dato público **con enlace**; si no, «sin dato». Un dato oficial se lee de la fuente oficial **sin IA** cuando se puede (`lib/bce.ts`) y llega tal cual. | CRM |
| G | **Notas ≠ Actividad.** Notas del lead = resumen «Campo: valor»; la conversación va a Actividad. | CRM |
| H | **Disco limitado.** Supabase `crm-321` es plan gratis con Disk IO limitado (se cayó el 27-sep): escrituras masivas en lote y con pausa, nunca fila por fila en bucle. | CRM (y cualquier Supabase en plan gratis: EMP) |
| I | **Pruebas con sesión real:** cerrar la sesión de prueba al terminar y, en el navegador integrado, comprobar el dominio antes de escribir una sesión. | CRM |
| J | **Vista previa `?vp=` solo en cursos NO publicados.** En uno publicado crea personas reales. Probar landings con borradores o con el servidor local seguro. Nunca correr `prueba-filtro.mjs` contra producción (dispara el Pixel real). | CRM (Academy) |

Detalle, ejemplos y por qué de cada una: `reference/reglas-producto-crm.md`.

## 2. Reglas de datos y de producto transversales

| Regla | Aplica a |
|---|---|
| **Producto replicable:** nombres, precios, cuentas y textos de la empresa viven en la base o en variables de entorno, nunca en el código. Se cambian **datos, no código**. | CRM, EMP (regla 1), VIP (regla 13) |
| **Un cliente = una organización (datos), nunca código.** Ningún nombre, texto o número de un cliente va en el código; vive en `organizaciones`, `angulos`, `conocimiento`. | EMP |
| **Aislamiento:** toda consulta de `src/server/**` filtra por `organizacion_id`. RLS niega todo por defecto (respaldo); el servidor usa service_role. | EMP |
| **Permisos = rol × plan**, decididos en el servidor (`lib/auth.ts::permite`). La pantalla solo oculta; cada acción vuelve a comprobar. | EMP, VIP (`permisos.ts`), CRE (`ADMIN_EMAILS`) |
| **El CRM manda sobre catálogo y configuración.** Ningún script, siembra o prueba revierte lo que el dueño cambió en pantalla (`pnpm db:seed` no pisa; `--forzar` sí). | VIP |
| **Lo que el agente promete sale de Configuración, no del prompt.** | VIP, CRM, EMP |
| **Lo interno no sale:** costos, márgenes y notas internas nunca llegan al cliente; todo lo público pasa por `server/publico.ts` (hay prueba). | CRE |
| **Nada se borra:** `eliminado_en` (soft delete); análisis y propuestas son versiones inmutables; solo el cierre y el estado mutan, con registro en `eventos`. | CRE |
| **No inventar números ni cobrar de más al cliente.** Cada cifra de impacto = producto de factores con fuente y cita; nunca dinero supuesto; máximo un supuesto; al menos un dato real; si falta, «por cuantificar» + la pregunta exacta. | CRE |
| **Dinero por WhatsApp: nada.** Pagos, montos, discrepancias, cancelar y borrar solo en el CRM. Única excepción VIP (2026-09-30): aviso informativo de discrepancia armado por el servidor, dentro de la ventana de 24 h. | VIP (y criterio para todo agente) |
| **Contenido sin inventos:** datos solo de la FUENTE (ficha del CRM); si falta un dato se omite; imagen generada por IA lleva «Imagen referencial.»; nunca propietarios, cédulas ni teléfonos de terceros. | MOTOR, CRM (marketing) |
| **Cobertura / ámbito:** el agente no niega un servicio («lo confirmo con planta»), no inventa el nombre del cliente, no promete recogida fuera de zona. | VIP |
| **Opinión de Valor, no «avalúo»:** nunca «avalúo», «tasación», «valor oficial»; siempre rango, con aviso legal y vigencia de 90 días. | CRM (docs/09 §6) |
| **LOPDP:** cada contacto guarda base legal y origen; la cédula de persona natural no sale del servidor; primer mensaje de prospección dice quién, de dónde salió el dato, para qué y cómo darse de baja; baja en un paso; 15 días para atender derechos. | CRM, EMP, VIP |
| **Descargas de clientes/pedidos solo superadmin y admin** (datos personales). | VIP |

## 3. Reglas de código y proceso (resumen; matriz completa en `reference/convenciones-codigo-por-repo.md`)

1. **Idioma:** toda la UI, comentarios, commits y nombres de dominio **en español con tildes y ñ correctas**
   (TODOS; en ADS el CLAUDE.md pide tildes y eñe aunque su propio texto no las usa: corrígelo al tocarlo).
   Los comentarios explican el **porqué**.
2. **Leer antes de escribir:** archivos existentes primero; investigar a fondo antes de implementar; preferir
   editar sobre reescribir; no parches a ciegas (CRM reglas 1–3).
3. **Probar con datos reales** antes de declarar terminado; verificar contra el sistema real (producción,
   n8n, Chatwoot), no solo con pruebas locales (CRM regla 4, VIP regla 14, DECISIONES §3).
4. **Gate antes de subir:**
   - CRM: `npx tsc --noEmit` y `npx next build` (revisar que no diga «Build error»), etiqueta de git antes y después de cada bloque, `npx vercel --prod --yes`.
   - EMP/VIP: `pnpm lint`, `pnpm typecheck`, `pnpm test`, `pnpm build`. VIP añade: «una advertencia tolerada se vuelve permanente».
   - CRE: `pnpm check` (tipos + lint + pruebas) y `pnpm build`; publica con `git push` a `main` (Vercel).
5. **Archivos ≤ 300 líneas** en EMP y VIP (se divide por responsabilidad). No es regla de CRE/CRM/ADS; no la
   impongas ahí, pero no la contradigas en archivos nuevos.
6. **Migraciones inmutables:** una migración aplicada nunca se edita; todo cambio es un archivo nuevo
   (`supabase/migrations/000N_*.sql` en EMP/VIP/CRE; `sql/NNN_*.sql` en CRM). En CRM **las pega Byron en el
   SQL Editor; nunca se ejecutan solas**. En EMP también se pega a mano (`supabase/instalar-todo.sql` solo la
   primera vez; después solo el archivo nuevo). En VIP/CRE se aplican con `pnpm db:migrate`.
7. **Capas:** `src/app/**` nunca importa `lib/supabase/admin.ts` directo; pasa por `src/server/**`;
   `src/server/**` nunca importa React (EMP, VIP). CRE: `app` rutas delgadas · `server` (`import 'server-only'`) ·
   `lib` dominio puro · `components/<área>`.
8. **Sin ORM; sin librería de fechas** (Quito es UTC-5 fijo, `Intl` nativo; CRM usa `America/Guayaquil`); VIP además
   sin Docker y sin SDK de OpenAI dentro del CRM (eso lo hace n8n).
9. **Ningún secreto en el repo.** VIP y EMP tienen una prueba que falla si aparece una llave literal (`sin-secretos`).
   Variables: `npx vercel env ls` (CRM); nunca se copian al repo. Secretos de webhooks se comparan en tiempo constante.
10. **Una base, un lugar:** VIP usa una sola base (pruebas y producción): ninguna prueba usa ni borra un número real
    ni depende de un valor que el dueño edita; los precios esperados se leen de la base (`tests/util/catalogo.ts`).
11. **Cada frase real que falle se convierte en prueba antes de arreglarla** (VIP; criterio recomendado para todo agente).
12. **Edición de TSX con la herramienta Edit**, no con reemplazos masivos por script (VIP: rompieron JSX).
    En Windows, scripts que escriben archivos: LF, abrir con `newline=''`.
13. **n8n:** respaldo primero; el workflow de producción de 321 no se modifica sin autorización citada; se cambia
    **por MCP** (`setNodeParameter`), nunca reimportando; tras subir un prompt: `node n8n/verificar-prompts.cjs`;
    tras crear nodos: `node n8n/verificar-errores.cjs` (el MCP pierde «continuar si falla»). Detalle en el skill
    `aiuda-agentes-whatsapp` y en `knowledge/decisiones/laundry-vip.md`.
14. **IA:** costo mostrado antes de gastar; tope mensual (CRM $50/mes vía `IA_TOPE_MENSUAL_USD`); presupuesto de
    IA que Byron autorizó gastar sin preguntar: hasta $1 por bloque (2026-09-27). `whisper-1` está prohibido en VIP
    (apagado programado): usar `gpt-transcribe`.
15. **Independencia entre negocios:** no se toca nada de 321 desde VIP (workflows, credenciales, tablas, Chatwoot
    cuenta 1); Academy no mezcla datos con INMO; los workflows de 321, Academy y VIP no se tocan desde EMP;
    ADS es 100 % independiente de CRM-321 aunque pueda embeberse como módulo `/ads`.
16. **Cómo trabaja Byron:** español, directo y sin relleno; no le gustan las paradas («estamos parando muchas veces
    innecesariamente»): avanza y pregunta solo lo que bloquea; recomendaciones, no menús; si dice «no ejecutes aún»,
    analiza y propone sin tocar nada; prefiere ver publicado a pruebas locales largas (CRE); nunca preguntarle qué
    existe (investigar el código, n8n, Supabase, Railway, Vercel); preguntar solo decisiones de negocio.

## 4. Contradicciones y cuál manda

- **Tope de IA:** `docs/07-plan-crm-agentico.md` dice $20/mes; `docs/06`, `HANDOFF` y el código (`TOPE_MENSUAL_USD`)
  dicen **$50/mes**. Manda el código y el HANDOFF (más recientes).
- **CLAUDE.md de CRM dice de sí mismo «tiene partes desactualizadas; si algo choca, manda el mapa».** Las reglas
  A–J no están desactualizadas (Byron las dictó el 2026-09-27); lo viejo son datos operativos (p. ej. el mapa
  `00-LEEME.md` dice «los commits NO están en GitHub», pero HANDOFF §0.1 dice que desde 2026-10-08 todo está
  subido a `bcujano/crm-321`). Manda HANDOFF.
- **Migraciones:** «las pega Byron» (CRM, EMP) vs `pnpm db:migrate` (VIP, CRE). Cada repo manda en lo suyo.
- **Archivos ≤ 300 líneas** solo es regla de EMP/VIP; EMP la declara copiada de VIP («la arquitectura de laundry-vip»).
- **ADS** pide no usar placeholders «próximamente» y Glass Design; CRM pide «todo premium» y sobrio sin burbujas.
  No son transferibles entre sí.

## 5. Cómo usar este skill

1. Identifica el repo → lee su fila en `reference/convenciones-codigo-por-repo.md`.
2. Si construyes pantalla o número: aplica A–G (CRM) o el equivalente del repo (§2).
3. Si tocas agentes de WhatsApp/voz: carga además `aiuda-agentes-whatsapp`.
4. Si dudas si algo ya se decidió: busca en `knowledge/decisiones/<repo>.md` antes de proponer (hay listas de
   «no volver a proponer»).

## Origen

- `/home/user/crm-321/CLAUDE.md` (reglas A–J, reglas de datos E–I, producto replicable, stack, Meta API)
- `/home/user/crm-321/docs/HANDOFF.md` §0.4, §3 · `/home/user/crm-321/docs/12-pendientes.md` (tabla «Cómo funciona ahora»)
- `/home/user/crm-321/docs/09-marco-legal-avaluos.md` §5–§6 · `/home/user/crm-321/docs/07-plan-crm-agentico.md` §1
- `/home/user/crm-321/src/lib/agente/turno.ts` (tope $50) · `/home/user/postpro-321/motor/skills/voz-y-reglas.md`, `motor/redaccion.py`
- `/home/user/bcujano/aiuda-empresas/CLAUDE.md`, `docs/PLAN.md` §4, §8
- `/home/user/bcujano/laundry-vip/CLAUDE.md`, `docs/DECISIONES.md`, `docs/AGENTE.md`, `.github/workflows/ci.yml`
- `/home/user/bcujano/creator/CLAUDE.md`, `docs/DECISIONES.md`, `.github/workflows/ci.yml`
- `/home/user/bcujano/adsboom/CLAUDE.md`, `AGENTS.md`
