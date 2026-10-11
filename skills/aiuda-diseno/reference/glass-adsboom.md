# Sistema glass de adsboom · detalle

Alcance: solo el repo adsboom (plataforma de campañas con IA, SaaS / licencia / módulo embebido). Los otros repos NO usan glass: usan tarjetas planas con tokens propios (`ui-plataforma.md`). Las reglas anti-slop de `landings.md` (sin degradados agresivos, un acento) se escribieron para landings de venta; ninguna fuente las extiende a la interfaz de adsboom, y el glass usa degradados y brillos a propósito. Si algún día se mezclan (p. ej. módulo embebido en el CRM), decide Byron.

## 1. Principios (de `adsboom/CLAUDE.md` y `globals.css`)
- Nombre interno: **Liquid Crystal Glass / Crystal Glass 3D**. Losa de vidrio gruesa con bordes direccionales, brillo en la parte alta, sombra flotante y reflejo prismático.
- **CSS puro, no WebGL** (no funciona bien en producción SaaS).
- **Claro y oscuro** con alternancia instantánea; `data-theme` en `<html>`, guardado en `localStorage` (`adsboom-theme`, por defecto `light`), y un script en `<head>` que lo aplica antes de pintar para evitar parpadeo.
- Idioma por defecto español con tildes y ñ (next-intl, `es.json` y `en.json`); pie «Powered by Emprendimientum».
- Sin «próximamente»: todo funciona o no se muestra.

## 2. Tokens (`:root` y `[data-theme="dark"]`)
| Grupo | Claro | Oscuro |
|---|---|---|
| Fondo `--bg-primary/secondary/tertiary` | `#d8dce8` / `#e2e5f0` / `#eceef6` | `#080816` / `#0e0e24` / `#161638` |
| Texto `--text-primary/secondary/muted` | `#1a1a2e` / `#4a4a6a` / `#8888aa` | `#f0f0ff` / `#b0b0d0` / `#6666aa` |
| Vidrio `--glass-bg` / `--glass-bg-hover` | blanco 12 % / 22 % | blanco 4 % / 8 % |
| Desenfoque `--glass-blur` | 16 px | 16 px |
| Bordes `--glass-edge-top/left/right/bottom` | blanco 95 / 60 / 35 / 15 % | blanco 20 / 10 / 6 / 3 % |
| Sombras `--glass-shadow-outer/inner` | 4 capas exteriores + 4 interiores (brillo) | versión oscura más profunda |
| Acento | `--accent-primary #6366f1`, `--accent-secondary #8b5cf6`, `--accent-gradient` índigo→violeta | igual |
| Degradados | `--gradient-red-orange`, `-blue-cyan`, `-green`, `-purple` | igual |
| Estado | `--success #10b981`, `--warning #f59e0b`, `--error #ef4444`, `--info #3b82f6` | igual |
| Layout | `--sidebar-width 260px`, `--header-height 64px` | igual |

Tailwind 4: `@theme inline` expone `bg-primary`, `text-primary/secondary/muted`, `accent`, `accent-secondary`, `success/warning/error/info` y `--font-sans: Inter`.

Borde grueso direccional: arriba 2 px (donde pega la luz), izquierda/derecha 1,5 px, abajo 1,5 px casi transparente.

## 3. Clases
| Clase | Qué es |
|---|---|
| `.glass` | Tarjeta principal: radio 20 px, `backdrop-filter: blur(16px) saturate(2)`, bordes direccionales, sombras exterior+interior, reflejo `::before` a 175°, al pasar el cursor sube 4 px y brilla en índigo |
| `.glass-sm` | Variante compacta: radio 14 px, sube 3 px |
| `.glass-pill` | Radio 9999 px; base de inputs, selects, botones de vidrio y conmutador de tema |
| `.glass-crystal` | Realzada: blur 20 px, saturación 2,5, `overflow: hidden`, barrido de brillo de 6 s |
| `.glass-iridescent` | Capa cónica de arcoíris que rota 10 s (usar en modales y tarjetas destacadas, con contenido en `z-index: 2`) |
| `.glass-prismatic` | Filo de luz arcoíris difuminado en el borde inferior |
| `.btn-gradient` | Botón con degradado y banda de brillo superior; hover: sube 3 px y escala 1,03 |
| `.glass-skeleton` | Carga con brillo desplazado de 1,5 s |
| `.glass-loader-orb(-sm/-lg)` | Orbe giratorio de 56 px (32 / 80) |
| `.wave-topo-bg`, `.marquee-left/right`, `.text-shimmer` | Fondos y animaciones de la landing de marketing; las marquesinas se pausan al pasar el cursor |

Foco global: `*:focus-visible` con outline de 2 px en `--accent-primary`, offset 2 px. Selección de texto con índigo al 30 %. Scrollbars de 6 px translúcidos.
En móvil (< 1024 px): `overflow-x: hidden`; las tablas se vuelven bloques con scroll horizontal; la barra de ajustes se oculta.

## 4. Componentes (`src/components/glass`, se importan de `index.ts`)
- **GlassCard**: `variant` `default | sm | iridescent`; `padding` `none | sm | md | lg` (0 / 12 / 20 / 32 px); `hover` activable; entra con fundido y subida de 12 px (0,4 s).
- **GlassButton**: `variant` `glass | gradient-red | gradient-blue | gradient-green | gradient-purple | ghost`; `size` `sm | md | lg`; `pill` por defecto (si no, radio xl); `loading` muestra el orbe pequeño y deshabilita; `icon` opcional; escala 1,03 al pasar y 0,97 al presionar.
- **GlassInput**: etiqueta encima (pequeña, `text-secondary`), campo `glass-pill`, icono izquierdo/derecho, error en rojo debajo; anillo de foco de acento al 40 %.
- **GlassSelect**: igual que el input con `appearance-none` y chevron propio; las opciones usan `bg-bg-secondary`.
- **GlassToggle**: `role="switch"`, `aria-checked`; pista degradada acento→secundario al activarse; tamaños `sm`/`md`.
- **GlassModal**: fondo negro al 30 % con desenfoque, tarjeta `glass glass-iridescent`, cierra con Escape y clic fuera, bloquea el scroll del `body`; tamaños `sm … xl`.
- **GlassLoader / GlassSkeleton**: orbe con texto opcional (pantalla completa disponible) y líneas de esqueleto de ancho decreciente.
- **Layout**: `Sidebar` (colapsable de 240 a 72 px, ítem activo con degradado de acento al 15 %), `Header` (altura 56/64 px, pegajoso), `MobileMenu`, `ThemeToggle` (sol/luna con giro).

## 5. Convenciones observadas en el código y en CLAUDE.md
1. Acción principal = `GlassButton` con degradado; el botón por defecto es de vidrio y el `ghost` para acciones discretas.
2. Texto de la interfaz sobre vidrio con `text-primary`/`text-secondary`; `text-muted` solo para ayudas y etiquetas secundarias (ver riesgos: no pasa 4,5:1).
3. Animaciones de entrada suaves (0,3–0,4 s); las infinitas (barrido, iridiscencia, orbe) viven en elementos puntuales (modal, orbe de carga, marquesinas de la landing).
4. Alternancia claro/oscuro instantánea; todo componente usa variables, nunca colores fijos, para que cambie con el tema.
5. Textos de la interfaz por next-intl (`es.json` por defecto), no escritos dentro del componente.
6. Probar ambos temas y 375 px de ancho (regla general de las landings, aplicada aquí por prudencia).

## 6. Riesgos conocidos al reutilizar (hallazgos propios, calculados sobre el código)
- `--text-muted` claro `#8888aa` sobre `#d8dce8` da ≈ 2,5:1 y en oscuro `#6666aa` sobre `#080816` ≈ 3,8:1: **no pasa 4,5:1**. Usar `text-secondary` (≈ 6,2:1 en claro) para texto que importa.
- `GlassModal` no declara `role="dialog"`, `aria-modal` ni atrapa el foco; el botón de cerrar no tiene `aria-label`. Añadirlos.
- `GlassButton` con `loading` no avisa a lector de pantalla; `ThemeToggle` tiene `aria-label` en inglés («Switch to …»): debe ir en español.
- Animaciones infinitas (`glass-refraction`, `crystal-sweep`, `glass-orb-*`, `marquee`) sin `@media (prefers-reduced-motion: reduce)` en `globals.css`.
- `--glass-border` se usa en `GlassToggle`, `Sidebar` y `Header` pero **no está definido** en `globals.css` (existen `--glass-edge-*`): define el token o usa `--glass-edge-left`.
- El `<title>` y la descripción en `layout.tsx` están en inglés aunque la regla del repo es español por defecto.

## Origen
`bcujano/adsboom/CLAUDE.md` (stack, reglas de desarrollo, módulos); `bcujano/adsboom/src/app/globals.css` (tokens, clases, animaciones, foco, móvil); `bcujano/adsboom/src/app/layout.tsx`; `bcujano/adsboom/src/components/glass/*.tsx` y `index.ts`; `bcujano/adsboom/src/components/layout/Sidebar.tsx`, `Header.tsx`, `ThemeToggle.tsx`; `bcujano/adsboom/src/components/providers/ThemeProvider.tsx`. Las cifras de contraste son cálculo propio (WCAG) sobre los hex del CSS.
