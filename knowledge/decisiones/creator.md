# Decisiones cerradas y «no hacer» — creator (CREATOR / AiUDA)

Herramienta de AiUDA (línea de negocio de 321 Soluciones Inmobiliarias S.A.S., Ecuador) para la **primera reunión con un cliente**:
entrevista + formulario en el celular → diagnóstico con IA → tres paquetes con precio e IVA → presentación en iPad → cierre
(paquete elegido, desembolsos) → acuerdo para firmar → CRM. Repo: `/home/user/bcujano/creator`; en producción (Vercel).
Leer en orden: `docs/ESTADO.md` → `docs/ARQUITECTURA.md` → `docs/DECISIONES.md`; `docs/OPERACION.md` para despliegue y variables.

## Usuario
Byron Cujano, Director General de 321 / AiUDA. Español. Quiere **velocidad**: decidir con buenos defaults, ejecutar y publicar
(`git push` a `main`, Vercel despliega). Pregunta solo lo que de verdad es suyo decidir. **No inventar números ni cobrar de más.**

## Reglas del código (CLAUDE.md)
- Capas: `src/app` solo rutas delgadas · `src/server` (`import 'server-only'`, service role) · `src/lib` dominio puro e isomórfico ·
  `src/components/<área>`.
- **Los montos los calcula el código, nunca la IA:** `lib/precios.ts`, `lib/analisis.ts`, `lib/pagos.ts`. La IA elige módulos y da
  factores/complejidad.
- **Nada se borra** (`eliminado_en`); análisis y propuestas son versiones inmutables; solo cierre y estado mutan, registrados en `eventos`.
- **Lo interno no sale:** costos, márgenes y notas internas nunca llegan al cliente; todo lo público pasa por `server/publico.ts` (hay prueba).
- **Una sola fuente para todas las salidas:** `server/documento.ts` arma el documento; PDF/Word/PPT/Excel/MD/presentación/acuerdo lo consumen.
- **Migraciones append-only** (`supabase/migrations/000N_nombre.sql`, `pnpm db:migrate`).
- Nombres y comentarios en español (comentarios explican el porqué). Biome: comillas simples, sin `;`, 100 columnas, LF.
- Antes de publicar: `pnpm check` (tipos + lint + pruebas) y `pnpm build`. CI en GitHub Actions (tipos, lint, pruebas); Vercel hace el build.

## Decisiones (`docs/DECISIONES.md`, la más reciente al final; si una cambia se agrega otra, no se reescribe)
1. App propia en Next + Supabase + Vercel; Supabase propio (no el de crm-321) para no mezclar datos de clientes de AiUDA con los de la inmobiliaria.
2. Un solo usuario administrador; autorización en el servidor (`ADMIN_EMAILS` + Supabase Auth); RLS activa **sin políticas**; rutas
   públicas (`/f`, `/p`, `/api/publico`) con tokens aleatorios de 144 bits.
3. **Claude principal, OpenAI de respaldo**; OpenAI además transcribe audio (Anthropic no transcribe); el proveedor usado queda guardado.
4. **Los números los calcula el código** (precios, IVA, márgenes, desembolsos, impacto/ROI).
5. **Cifras de impacto fundamentadas:** producto de factores con fuente y cita; nunca dinero supuesto; máximo un supuesto; al menos
   un dato real; si falta algo, «por cuantificar» + la pregunta exacta («que no te inventes nada»).
6. Versiones inmutables y nada se borra; bitácora `eventos`.
7. Respuestas del cliente separadas de las del consultor (`respuestas_cliente` vs `respuestas`).
8. Cierre mutable, contenido inmutable (`propuestas.cierre`).
9. **Módulos a medida:** solo herramientas/agentes IA nuevos con valor propio; integraciones con lo que el cliente ya usa van **incluidas
   sin costo**; nombres «Agente de… / Sistema de…»; la IA clasifica complejidad y el precio sale de la tabla ($300/$600/$900, el último
   es tope). «No queremos atracar al cliente.»
10. Integración CRM con clave propia de permisos mínimos (`CREATOR_WEBHOOK_SECRET`: solo `new_lead` y `log_activity`); las lecturas (GET)
    siguen exclusivas de n8n.
11. Precios del catálogo aprobados el 23/09/2026 (iAgente WhatsApp $2.500+$190/mes; CRM Básico $3.500+$250; Operativo $6.500+$390;
    Gerencial $12.000+$650; levantamiento documental $2.800; usuario extra $15; margen mínimo $150/mes por cliente; IVA 15 %).
12. Estructura de carpetas por función; CI.
13. **Valoración de módulos a medida grandes: pospuesta** (opciones A/B/C en ESTADO pendiente 1); mientras tanto manda la tabla con tope.
14. Numeración de propuestas desde la 127 (próxima `AIU-2026-0128`; acuerdo `ACU-`).
15. Un número por negociación (versiones comparten número desde la migración `0007`).
16. Presentación descargable en PDF (react-pdf) desde el mismo `Documento`.
17. **El precio grande es el total con IVA**; la base sin IVA es detalle.
18. Brief de arranque del proyecto en Markdown (`server/proyecto.ts`): nunca costos ni márgenes; solo con el cierre guardado.

## Trampas conocidas (no repetir)
Bash en Windows con heredocs de comillas mixtas · `curl` desde Git Bash con tildes → script `tsx` · scripts que importan `src/server`
con `NODE_OPTIONS="--conditions=react-server"` · `jsonb` reordena claves (comparar por valor) · `pptxgenjs` no puede ser
`serverExternalPackages` · Claude + esquema grande («grammar too large» → JSON por instrucciones + zod con un reintento) ·
Vercel Hobby = 300 s por función (esfuerzo `high` ~256 s; default `medium`) · `Font.registerHyphenationCallback` en react-pdf ·
identidad local de git (Byron Cujano), sin identidad global.

## «No hacer»
Poner precio a un módulo a medida con la IA sin tabla · proponer integraciones del cliente como módulos de pago · mostrar la base sin
IVA como cifra principal · borrar filas · editar una migración aplicada · mostrar costos/márgenes/notas internas al cliente ·
reutilizar el secreto de n8n para la integración · dar a la IA permiso de calcular montos.

## Vacíos y contradicciones
- CLAUDE.md dice `pnpm check` con **45 pruebas**; `docs/ESTADO.md` dice **50 pruebas** (manda ESTADO, más reciente: 23-sep).
- Integración CRM «configurada, sin probar el alta real» (ESTADO).
- Sin regla escrita de retención de datos del cliente (entrevista textual, audio) ni de aviso de IA al cliente en el formulario.

## Origen
`/home/user/bcujano/creator/CLAUDE.md`, `docs/DECISIONES.md`, `docs/ESTADO.md`, `package.json`, `.github/workflows/ci.yml`.
