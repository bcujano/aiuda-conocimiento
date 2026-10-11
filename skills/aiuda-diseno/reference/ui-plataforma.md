# UI de las plataformas AIUDA · detalle

Aplica a crm-321, creator, aiuda-empresas, laundry-vip (adsboom tiene su propio sistema: `glass-adsboom.md`). No hay un sistema de diseño compartido entre repos: cada uno define sus tokens. Ver «Vacíos» al final.

## 1. Reglas de producto (crm-321/CLAUDE.md, no se negocian)
**A. Todo término lleva su icono de ayuda.** Definido en el glosario único (`src/lib/glosario.ts`) con cuatro líneas: *qué es · de dónde sale · cómo afecta · ejemplo*; se muestra con `<Ayuda termino="clave" />`. Un término en pantalla sin ayuda es un error, igual que un `any` sin justificar. El componente: icono de interrogación pequeño (13 px), explicación al pasar el cursor **y al tocar**, `aria-label="Qué es …"`.

**B. Todo resultado se interpreta solo (R1).** Cada pantalla con datos lleva `<Lecturas>`: plegable, **cerrado por defecto**, sin repetir lo que ya se ve, diciendo qué decisión sale y **con qué cruzarlo** (`cruzar` con enlace directo). Si hay alertas u oportunidades, el contador se ve con el bloque cerrado (lo urgente no obliga a abrirlo). `aria-expanded` en el botón. Las lecturas viven en `src/lib/lecturas*.ts`.
- Cada lectura: título, texto, fuente (el origen del cálculo), tono (`alerta`, `oportunidad`, `dato`), para quién, y opcionalmente `cruzar`.

**C. Ningún número lo escribe un modelo de lenguaje.** Toda conclusión es una cuenta sobre datos del sistema, con su origen. Si falta el dato, la lectura **no aparece** y se dice que falta. Nunca se rellena ni se estima en silencio.

**D. Escrito para el usuario, no para el desarrollador.** «Los leads sin teléfono», nunca «el campo `telefono`». No se explica cómo está hecho el sistema: se dice qué hacer. (Byron leyó un aviso técnico en pantalla y no lo entendió; se quitó.)

**E–J (datos y pruebas que afectan la UI):** una función, un lugar (clasificación, precios del catálogo); fuente del dato (dato propio si pasa el mínimo, si no dato público **con enlace**, si no «sin dato»); notas ≠ actividad; escrituras masivas en lote y con pausa; pruebas con sesión real y cerrarla al terminar; vista previa `?vp=` solo en cursos no publicados.

## 2. Lenguaje de la interfaz
- Todo en español con tildes y ñ correctas: UI, código, comentarios y commits (crm-321, aiuda-empresas, laundry-vip, adsboom).
- Tuteo, frases cortas, verbos de acción en botones. Sin jerga ni nombres de campos.
- Un estado vacío explica qué falta y qué hacer; no «próximamente». «Todo debe funcionar o no mostrarse» (adsboom).
- Moneda con `Intl.NumberFormat('es-EC', …)`, USD; fechas en hora de Ecuador (`America/Guayaquil`, UTC-5 fijo). Cifras con `tabular-nums` en tablas y KPIs.
- Los textos que ve el cliente final nunca muestran costos, márgenes ni notas internas (creator: todo lo público pasa por una capa única que lo filtra).

## 3. Tokens por repo
Todos usan Tailwind 4 con `@import "tailwindcss"` y tokens como variables CSS; ninguno usa `tailwind.config`. Los nombres de color son semánticos en español o inglés según el repo.

| Repo | Tokens | Notas |
|---|---|---|
| crm-321 | `--color-primary #1a1a2e`, `accent #e94560`, `surface #fff`, `surface-alt #f8f9fc`, `border #e5e7eb`, `text #1f2937`, `text-muted #6b7280`; colores de etapa del embudo (nuevo, contactado, calificado, cotizado, videollamada, negociación, cerrado ganado/perdido) | Títulos de página en serif (Newsreader, `font-display`), cuerpo Inter; radios 1 y 1,25 rem; sombra de tarjeta casi imperceptible; utilidad `eyebrow` (11 px, mayúsculas, 0,08 em) para etiquetas de KPI |
| creator | `--marca`, `--acento`, `--fondo`, `--superficie`, `--superficie-2`, `--borde`, `--tinta`, `--tenue`, `--peligro`, `--aviso`, `--ok` | El color de marca se inyecta en ejecución desde Ajustes; modo oscuro por `prefers-color-scheme` + `data-theme`; `.anillo-foco` con outline de 2 px; `@media print` con `.no-imprimir` |
| aiuda-empresas | `--color-lateral #111827`, `primario #1f3a5f`, `acento #d97706`, `fondo`, `superficie`, `borde`, `texto`, `texto-suave`, y pares `exito/peligro/aviso` + `-suave` | Barra lateral oscura, **un solo acento**; alias en `:root` para usar `var()` en valores arbitrarios |
| laundry-vip | Misma estructura que aiuda-empresas con paleta verde (`primario #0f5c4f`, `acento #e07a2f`, lateral `#0d2b25`) | «Barra lateral oscura, como el CRM 321» |

Reglas derivadas:
- Colores en tokens, nunca hex sueltos en componentes (excepto datos de marca que vienen de la base).
- Cada variante de estado tiene su par fuerte/suave (texto sobre fondo suave) en aiuda-empresas y laundry-vip.
- Estados con color **no dependen solo del color**: acompañar con icono o texto (▲/▼ con porcentaje en los KPI).
- Un solo acento por producto; el resto neutro.

## 4. Modo oscuro (patrón de creator)
```css
:root { --fondo:#f6f7fb; /* … */ }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --fondo:#10121a; /* … */ } }
:root[data-theme="dark"] { --fondo:#10121a; /* … */ }
@theme inline { --color-fondo: var(--fondo); /* … */ }
body { background: var(--fondo); color: var(--tinta); }
```
Asignar siempre un fondo explícito al `body`. crm-321, aiuda-empresas y laundry-vip son solo claros en lo leído.

## 5. Componentes comunes
- **Encabezado de página** (`PageHeader`): etiqueta/fecha arriba, título en serif, subtítulo en gris (máx. ancho 2xl), acciones a la derecha; en pantallas pequeñas se apila.
- **KPI** (`Kpi`): etiqueta en mayúsculas pequeñas, cifra grande con `tabular-nums`, variación en píldora verde/roja con flecha, pista debajo.
- **Píldoras** (`Pills`), saludo (`saludo()`), toasts (`Toaster`), atajos (`Atajos`), estado de datos (`EstadoDatos`), fuente del dato (`FuenteDato`).
- **Primitivos de creator** (`components/ui/primitivos.tsx`): `Boton` con variantes `primario`, `secundario`, `fantasma`, `peligro`; campos y tarjetas; `cx()` para unir clases.
- Tarjetas blancas con borde fino; botones con transición de color; controles cómodos al tacto en iPad y celular (creator: `font: inherit` en controles, `textarea` con `field-sizing: content`).

## 6. Accesibilidad mínima
- Contraste ≥ 4,5:1 en texto; revisar `text-muted` (en crm-321 `#6b7280` sobre `#f8f9fc` da ≈ 4,6:1: justo en el límite, no aclararlo más).
- Foco visible (outline 2 px con offset) en todo elemento interactivo; no quitarlo.
- Botones de icono con `aria-label` en español; interruptores con `role="switch"` y `aria-checked`; acordeones con `aria-expanded`.
- Objetivos táctiles ≥ 48 px en piezas de venta; cómodos en iPad en herramientas de reunión.
- `prefers-reduced-motion`: sin animación del cajón lateral ni de elementos decorativos (aiuda-empresas lo aplica a `.barra-lateral` y `.tarjeta-arrastrable`).
- Móvil: la barra lateral se vuelve cajón (variable `--cajon` y `translate`, sin `!important`); en escritorio (≥ 1024 px) siempre fija; `max-width: 100vw` y `overflow-x: hidden` en `html, body`; tablas con scroll horizontal propio.
- Campo trampa invisible para bots en formularios públicos (`aria-hidden`, `tabIndex={-1}`).

## 7. Código de UI (Biome y organización)
- **Biome** (creator, aiuda-empresas, laundry-vip; versión fijada 2.5.13): preset `recommended`; sangría de 2 espacios; ancho 100; comillas simples; sin punto y coma (`asNeeded`); comas finales `all`; CSS con directivas de Tailwind activas; respeta `.gitignore`. Comandos: `pnpm check` (tipos + lint + pruebas), `pnpm lint`, `pnpm build`.
- crm-321 y adsboom no usan Biome (adsboom usa ESLint con la config de Next; crm-321 no tiene linter propio en `package.json`): antes de desplegar `npx tsc --noEmit` y `npx next build`.
- Máximo **300 líneas por archivo** (aiuda-empresas, laundry-vip); dividir por responsabilidad.
- Capas: `src/app` rutas delgadas; `src/server` lógica de servidor; `src/lib` dominio puro; `src/components/<área>` UI por función. La UI nunca importa el cliente de base con permisos de servicio.
- Nombres y comentarios en español; comentarios que expliquen el porqué.
- Finales de línea LF. Ediciones de TSX con la herramienta de edición, no con reemplazos masivos por script (ya rompieron JSX).
- Next.js 16 / React 19: las versiones cambian APIs; leer la guía local del paquete antes de escribir código (aviso de adsboom).
- Imágenes: preferir WebP < 1 MB; `loading="lazy"` salvo el hero.

## 8. Vacíos detectados
- No existe un set de tokens ni una marca visual AIUDA común a los cuatro repos; cada uno improvisa su paleta.
- crm-321 no documenta tamaños de tipografía ni escala de espacio fuera de las landings; la escala 4/8/12/16/24/32/48/64 está definida solo en `docs/14`.
- No hay reglas escritas de gráficos de datos en las plataformas (ver skill `dataviz` si está disponible).

## Origen
`crm-321/CLAUDE.md`; `crm-321/src/components/Ayuda.tsx`, `Lecturas.tsx`, `ui.tsx`; `crm-321/src/app/globals.css`; `crm-321/src/lib/glosario.ts`; `bcujano/creator/CLAUDE.md`, `biome.json`, `package.json`, `src/app/globals.css`, `src/components/ui/primitivos.tsx`; `bcujano/aiuda-empresas/CLAUDE.md`, `biome.json`, `src/app/globals.css`; `bcujano/laundry-vip/CLAUDE.md`, `biome.json`, `src/app/globals.css`; `bcujano/adsboom/CLAUDE.md`, `package.json`. El cálculo de contraste (≈ 4,6:1) es propio sobre los colores de `globals.css`.
