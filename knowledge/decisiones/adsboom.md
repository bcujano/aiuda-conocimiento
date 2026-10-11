# Decisiones cerradas y «no hacer» — adsboom (AdsBoom)

Plataforma de gestión de campañas publicitarias con IA (Meta, Google, TikTok, LinkedIn, Pinterest, YouTube). Propietario: Byron
Cujano (Emprendimientum). Repo: `/home/user/bcujano/adsboom`. Es un proyecto de **referencia**, con menos documentación de reglas
que los demás: aquí solo hay lo escrito en `CLAUDE.md` y `AGENTS.md`.

## Identidad y modos de entrega
- Modos: **SaaS** (suscripción mensual/anual), **licencia one-time** (deploy Vercel + Supabase para el cliente) y **embebido**
  (módulo `/ads` dentro de CRM-321; en la UI de CRM se llama «Publicidad iA», «AdsBoom» queda como nombre interno).
- **El sistema es 100 % independiente de CRM-321** aunque exista el modo embebido.
- Planes (USD): Basic $49/mes · $490/año · licencia $890; Pro $99 · $990 · $1.990; Premium $199 · $1.990 · $4.990; Enterprise $399 ·
  $3.990 · $12.990.
- Módulos: Campaign Studio, Intelligence, Autopilot, Funnel Builder, Lead Bridge, Agency Hub, Analytics Pro, Real Estate Mode (listing a
  ad en 1 clic, para CRM-321).
- Checkpoints de git con nombre descriptivo (`FOUNDATION-CORE-SUPABASE` … `CRM321-INTEGRATION-RELEASE` = v1.0).

## Stack
Next 16 (App Router) + TS, Tailwind 4 (Glass Design System «crystal 3D»), Framer Motion, `next-intl` (español por defecto + inglés),
Supabase (auth + PostgreSQL + RLS multi-tenant), PayPal (internacional) y PayPhone (LATAM/Ecuador), OpenAI GPT-4o (copy), Google
Imagen 3 por Vertex AI, Runway Gen-3 Alpha (video), Claude API (estrategia/análisis), Resend, Vercel. ESLint (no Biome).

## Reglas de desarrollo (CLAUDE.md)
- Idioma por defecto: **español con tildes y eñe correctas**.
- Footer: «Powered by Emprendimientum».
- Diseño Crystal Glass 3D con **CSS puro, no WebGL** (WebGL no funciona bien en producción SaaS); dark/light con toggle instantáneo.
- **No usar placeholders «próximamente»**: todo debe funcionar o no mostrarse.
- Ruta local `C:\dev\adsboom`.
- `AGENTS.md`: **esta versión de Next.js tiene cambios incompatibles** (APIs, convenciones, estructura); leer la guía relevante en
  `node_modules/next/dist/docs/` antes de escribir código y atender los avisos de deprecación.

## Notas de la API de Meta que comparte con crm-321 (v22.0, de `crm-321/CLAUDE.md`)
`advantage_audience=1` obligatorio → `age_min` máx. 25, `age_max` fijo 65 · CTA de WhatsApp `{ type: 'WHATSAPP_MESSAGE', value:
{ app_destination: 'WHATSAPP' } }` **sin link** · ABO requiere `is_adset_budget_sharing_enabled=false` explícito · CBO requiere
`budget_rebalance_flag=true` + `daily_budget` en campaña · imágenes de Google Drive necesitan URL directa (`toDirectUrl`) ·
`slideshow_spec` de Meta NO funciona → usar ffmpeg para generar un MP4 real.

## «No hacer»
- Usar WebGL; dejar secciones «próximamente»; escribir la UI sin tildes/eñes; acoplarlo a tablas de CRM-321; olvidar el footer de marca.
- Escribir código de Next 16 de memoria sin leer la guía de `node_modules/next/dist/docs/`.

## Vacíos y contradicciones
- El propio `CLAUDE.md` está escrito sin tildes (p. ej. «Descripcion», «campanas») aunque exige tildes y eñe: se corrige al tocarlo.
- Dice «Sistema 100 % independiente de CRM-321» y a la vez «Embebido: módulo /ads dentro de CRM-321» y lista «Real Estate Mode (para
  CRM-321)»: la independencia es de código y datos; la integración es un modo de entrega.
- No hay reglas escritas de pruebas, CI, límites de archivo, migraciones ni manejo de datos de campañas (tokens de Meta, pagos).
  Hasta que existan, aplica `aiuda-reglas-producto` §2–§3 (secretos fuera del repo, migraciones inmutables, cifras sin inventar).
- Pagos (PayPal/PayPhone): no hay regla escrita de verificación de webhooks; cualquier cambio exige revisar firma y secretos (ver
  el patrón de `secretoValido` de aiuda-empresas).

## Origen
`/home/user/bcujano/adsboom/CLAUDE.md`, `/home/user/bcujano/adsboom/AGENTS.md`, `/home/user/crm-321/CLAUDE.md` (notas Meta),
`/home/user/crm-321/docs/06-estado-y-continuacion.md` (nombre «Publicidad iA»).
