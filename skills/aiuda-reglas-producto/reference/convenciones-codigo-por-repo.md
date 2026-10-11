# Convenciones de código por repo

Verificado leyendo los repos el 2026-10-11. «—» = no hay regla escrita en ese repo.

## Matriz

| Tema | CRM (crm-321) | EMP (aiuda-empresas) | VIP (laundry-vip) | CRE (creator) | ADS (adsboom) | MOTOR (postpro-321) |
|---|---|---|---|---|---|---|
| Stack | Next 16, React 19, TS, Tailwind, Supabase, recharts, jsPDF | Next 16, React 19, TS 6, Tailwind 4, Biome, Vitest, Supabase, Vercel; n8n+Chatwoot en Railway; Gemini + OpenAI respaldo | Next 16, React 19, TS 6, Tailwind 4, Biome, Vitest, Playwright, pnpm, Node 24; n8n+Chatwoot+WhatsApp Cloud; OpenAI `gpt-4.1-mini` y `gpt-transcribe` | Next 16, Supabase, Vercel, Biome, Vitest, pnpm, Node 24; Claude principal, OpenAI respaldo | Next 16 (App Router, «NOT the Next you know»), Tailwind 4, Framer Motion, next-intl, Supabase, PayPal/PayPhone | Python en Railway (Dockerfile, `python main.py`), OpenAI `gpt-4.1-mini` para textos |
| Gestor / lint | npm; `npx tsc --noEmit`, `npx next build` | pnpm; Biome (`pnpm lint`) | pnpm; Biome | pnpm; Biome (comillas simples, sin `;`, 100 col., LF) | npm; ESLint | pip (`requirements.txt`) |
| Gate antes de subir | `npx tsc --noEmit` + `npx next build` + etiqueta git antes y después + `npx vercel --prod --yes` + verificar en producción | `pnpm lint`, `typecheck`, `test`, `build` | `pnpm typecheck`, `lint`, `test`, `build` (todo verde; una advertencia tolerada se vuelve permanente) | `pnpm check` (tipos+lint+45 pruebas) y `pnpm build` | — (checkpoints git con nombre descriptivo) | push a `main` despliega solo en Railway |
| CI | — (sin `.github`) | — (sin `.github`) | `.github/workflows/ci.yml`: typecheck, lint, test (con secrets de Supabase/n8n), playwright chromium, build | `.github/workflows/ci.yml`: typecheck, lint, test en push a `main` y PR; build lo hace Vercel | — | — |
| Tests | Scripts en `scripts/academy-pruebas/` y `scripts/vectorial-*.mts`; probar con datos reales y usuarios temporales que se borran | `tests/unit` (agenda, agente, calendario, reglas) con Vitest; prueba sin red | `tests/unit`, `integration`, `e2e` (Playwright); `sin-secretos.test.ts`; `workflow-laundry-agente.test.ts` exige prompt del JSON idéntico al `.md` | `tests/` con fixtures; prueba de `publico.ts` (lo interno no sale) | — | — |
| Límite de archivo | — | **300 líneas** | **300 líneas** (se divide por responsabilidad) | — | — | — |
| Capas | `src/app`, `src/components`, `src/lib`, `src/types` | `src/app` → `src/server` → supabase; `src/app/**` nunca importa `lib/supabase/admin.ts`; `src/proxy.ts` | igual que EMP; `src/server/**` nunca importa React; `scripts/` no usa alias `@/` (tsx no resuelve paths) | `src/app` rutas delgadas · `src/server` (`import 'server-only'`, service role) · `src/lib` puro/isomórfico · `src/components/<área>` | `(marketing)`, `(auth)`, `(app)`, `(admin)`, `api`; `components/glass`, `layout`, `providers`, `checkout`; `src/messages/{es,en}.json` | `motor/` (router `/api/motor/*` vigente), `legacy/` |
| Migraciones | `sql/NNN_*.sql`, **las pega Byron** en el SQL Editor; nunca se ejecutan solas | `supabase/migrations/000N_*.sql`; nunca se editan; `instalar-todo.sql` solo la 1.ª vez; se pega a mano | `supabase/migrations/`; nunca se editan; `pnpm db:migrate` | `supabase/migrations/000N_nombre.sql` append-only; `pnpm db:migrate` | `supabase/` | — |
| Fechas | `America/Guayaquil` | Quito UTC-5 fijo, sin librería de fechas | `Intl` nativo, UTC-5 fijo | — | — | — |
| Idioma | español con tildes y ñ en toda la UI | español con tildes y ñ: código, comentarios, commits, interfaz | igual | nombres y comentarios en español; comentarios explican el porqué | español por defecto (con tildes y eñe) + inglés (next-intl) | — |
| Secretos | nunca en el repo; `npx vercel env ls` | ninguno en el repo (regla 10) | prueba que falla ante llave literal en JSON de n8n; historial purgado con `git filter-repo` el 2026-09-23 | — | — | — |

## Qué leer primero en cada repo

- **CRM:** `docs/HANDOFF.md` → `docs/12-pendientes.md` → `docs/08-mapa-del-sistema/00-LEEME.md` →
  `docs/06-estado-y-continuacion.md` → `docs/14-diseno-landings.md` (antes de tocar diseño). Prompt de arranque:
  `docs/PROMPT-INICIO.md`. Nunca preguntar a Byron qué existe.
- **EMP:** `docs/PLAN.md` y `docs/PUESTA-EN-MARCHA.md`.
- **VIP:** `docs/CONTINUIDAD.md` (estado exacto, IDs, plan, prompt para abrir la siguiente sesión); si tocas el agente:
  `docs/AGENTE.md` y `docs/DECISIONES.md`. Está en producción **con clientes reales**.
- **CRE:** `docs/ESTADO.md` → `docs/ARQUITECTURA.md` → `docs/DECISIONES.md`; `docs/OPERACION.md` (despliegue, variables).
  No pedir contexto al usuario: está todo ahí.
- **ADS:** `CLAUDE.md`; `AGENTS.md` obliga a leer `node_modules/next/dist/docs/` antes de escribir código (esta
  versión de Next tiene cambios incompatibles con lo que el modelo sabe).
- **MOTOR:** la documentación se mudó a `crm-321/docs/` el 2026-09-26; aquí solo viven `motor/`, `n8n/workflows/`
  (respaldos) y `legacy/`.

## Comandos de cierre de sesión

- VIP: «deja todo listo para la siguiente sesión» = reescribir `docs/CONTINUIDAD.md` con el estado **verificado
  contra producción**, sin dejar pendientes solo en el chat, y dar el prompt de arranque. Un hallazgo que no se
  puede arreglar se escribe en CONTINUIDAD §3–§5.
- CRM: al cerrar un bloque, marcar ✅ con fecha en `12-pendientes.md` y registrar el cambio en `04-registro-cambios.md`;
  todo lo que Byron deba copiar (SQL, claves, comandos) va **en el chat**, nunca en un archivo; punto de restauración
  (etiqueta git) antes y después de cada bloque y subirla.
- CRE: `git push` a `main` publica; identidad local del repo (Byron Cujano), sin identidad global.

## Trampas técnicas ya resueltas (no repetirlas)

- Heredocs con comillas mixtas fallan en Bash de Windows: escribir un script en archivo (Write) y ejecutarlo (CRM, CRE).
- Python en Windows escribe CRLF salvo `newline='\n'`; un prompt con `\r` rompe las pruebas que lo comparan (VIP).
- `curl` desde Git Bash codifica mal las tildes: usar un script `tsx` UTF-8 (CRE).
- Scripts que importan `src/server`: `NODE_OPTIONS="--conditions=react-server" npx tsx ...` (CRE, por `server-only`).
- `jsonb` reordena claves: comparar por valor, no con `JSON.stringify` (CRE).
- `pptxgenjs` no puede ser `serverExternalPackages` (falla en Vercel): cargar exportadores con `import()` por formato (CRE).
- Claude + esquema grande: «grammar too large»; caer a JSON por instrucciones + validación zod con un reintento (CRE).
- Vercel Hobby = 300 s por función; análisis `high` ~256 s, default `medium` (CRE). Hobby no permite uso comercial (EMP).
- `react-pdf`: registrar `Font.registerHyphenationCallback` para no cortar palabras (CRE).
- `'use server'` solo puede exportar funciones async; un helper exportado rompió el build (VIP).
- Tailwind v4: clases arbitrarias raras pueden no generarse; usar `style` (CRM).
- `toPathData` de opentype.js genera `NaN`: serializar trazados a mano; `addPage()` de pdfkit pierde el tamaño si no se pasa `size` (CRM).
- `after()` de Next falla fuera de una petición: `try { after(f) } catch { void f() }` (CRM).
- Variables «sensibles» de Vercel no bajan con `env pull`: `printf "valor" | npx vercel env add NOMBRE production` y redeploy (CRM).
- Railway: setear con `railway variables --service postpro-321 --set "K=V" --skip-deploys`; usar siempre `-s postpro-321` (CRM).
- Pruebas que vencen con el calendario (fecha fija) o chocan con datos reales: fechas calculadas y frases únicas (VIP).
- Carrera entre pruebas por un precio compartido: usar otra prenda/fixture (VIP).

## Origen

- `/home/user/crm-321/CLAUDE.md`, `/home/user/crm-321/docs/HANDOFF.md` §2, §3, §6, `/home/user/crm-321/docs/12-pendientes.md`
- `/home/user/bcujano/aiuda-empresas/CLAUDE.md`, `package.json`, `biome.json`, `docs/PUESTA-EN-MARCHA.md`
- `/home/user/bcujano/laundry-vip/CLAUDE.md`, `docs/DECISIONES.md`, `.github/workflows/ci.yml`
- `/home/user/bcujano/creator/CLAUDE.md`, `package.json`, `.github/workflows/ci.yml`
- `/home/user/bcujano/adsboom/CLAUDE.md`, `AGENTS.md` · `/home/user/postpro-321/README.md`, `docs/README.md`, `railway.json`
