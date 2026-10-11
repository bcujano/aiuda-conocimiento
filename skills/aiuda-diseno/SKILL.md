---
name: aiuda-diseno
description: Reglas de diseño de AIUDA para landings de venta, piezas gráficas de anuncios (cuadrado, vertical, historia, portada de ebook), interfaz de las plataformas (tokens, Tailwind, Biome, accesibilidad, ayuda en pantalla) y el sistema glass de adsboom. Úsala al diseñar o revisar cualquier pantalla, landing, anuncio, SVG/PNG o ebook.
---

# AIUDA · Diseño

Orden de precedencia cuando dos fuentes chocan: (1) lo que Byron decidió y quedó escrito con fecha, la más reciente primero; (2) el código vigente (`conocimiento.ts`, `estilos.ts`); (3) la investigación de mercado (orientativa, no ley); (4) borradores y planes viejos. Las contradicciones conocidas están en la sección «Choques» al final.

Detalle por tema en `reference/`:
- `reference/landings.md` · estructura, jerarquía, estilos y lista de verificación de landings.
- `reference/piezas-graficas.md` · generador vectorial, formatos, plantillas, 10 estilos, ebooks.
- `reference/ui-plataforma.md` · tokens por repo, componentes, ayuda en pantalla, lecturas, Biome, accesibilidad.
- `reference/glass-adsboom.md` · sistema glass de adsboom (tokens, clases, componentes, límites).

## Cuándo usar cada referencia
| Tarea | Lee |
|---|---|
| Landing de curso, página de venta, hero, precio, barra fija | `landings.md` |
| Anuncio Meta, portada de ebook, SVG/PNG, carrusel de láminas | `piezas-graficas.md` |
| Pantalla del CRM o de otra plataforma, formulario, tabla, KPI | `ui-plataforma.md` |
| Cualquier cosa en adsboom (tarjetas, botones, modal, tema oscuro) | `glass-adsboom.md` |
| Texto de la pieza, voz, precios, legal | skill `aiuda-contenido-y-voz` |

## Reglas que valen para todo diseño
1. **Una idea, una acción.** Un titular (lo más grande), un color fuerte (el botón), todo lo demás neutro.
2. **Ningún texto sobre la foto** en el hero de landing ni en piezas estáticas: la foto va limpia y el texto en fondo plano o al lado (decisión de Byron, 2026-10-04).
3. **Contraste mínimo 4,5:1** en todo texto (WCAG). Botones de al menos 48 px de alto.
4. **Ningún número lo escribe un modelo de lenguaje.** Precios, fechas, cupos, días y cifras salen de la base con su origen. Cifra sin fuente: no se muestra ni se genera.
5. **Español con tildes y ñ**, tuteo, sin jerga técnica: «tu negocio», no «tu funnel». Se escribe para quien lee, no para quien construyó el sistema.
6. **Replicable:** nombres, colores, logos y precios de una empresa viven en la base o en variables de entorno, nunca en el código. Cambiar de empresa = cambiar datos.
7. **Rostro humano real** del facilitador o asesor; nunca ilustrarlo ni sustituirlo por stock o por un vector.
8. **Anti-slop:** un solo acento, sin degradados agresivos, sin emojis como viñetas, sin orbes de «IA», sin muros de logos.
9. **Móvil primero:** probar a 375 px y a 1440 px mirando la captura; más del 60 % del tráfico pagado es móvil. Márgenes laterales de 16–20 px y cero desborde horizontal.
10. **Movimiento con permiso:** respetar `prefers-reduced-motion`; las píldoras flotantes de landing se animan lento (≥ 6 s).

## Landings (resumen; detalle en `landings.md`)
- El hero responde en 3 segundos: ¿es para mí?, ¿qué gano?, ¿puedo confiar? Titular de 6–12 palabras que dice la **transformación**, no el tema; subtítulo de 15–25 palabras; **un** CTA principal; foto real.
- Fecha y duración van en **máximo 2 píldoras flotantes** jerárquicas (fecha = acento y mayor; duración = cristal y pequeña), solapadas ~15 % sobre la foto, **sin tapar la cara**; en móvil, debajo de la foto.
- Orden de secciones: hero → datos clave → resultados → para quién es (y para quién no) → temario → facilitador → prueba social → precio y bono → preguntas frecuentes → cierre con CTA.
- CTA repetido (hero, tras la prueba social, barra fija en móvil que aparece cuando el hero sale de pantalla). Verbo de acción, color de máximo contraste.
- Urgencia **solo real**: el contador usa el cierre verdadero de la etapa de precio. Escalera de precios visible con la vigente destacada y las vencidas tachadas.
- Precio en landings: el más grande es el de **efectivo o transferencia**; el de tarjeta va más pequeño con el ahorro explicado. El recargo se explica en la pantalla de pago, nunca en el botón ni con la palabra «recargo».
- Fotos: una por sección, sin repetir imagen en la página, < 1 MB (WebP), hero con `fetchPriority="high"`, resto `loading="lazy"`; en móvil recortar el hero a 4:5.
- Los 10 estilos son diseños distintos (otra estructura, tipografía y experiencia), no el mismo diseño con otros colores.

## Piezas gráficas (resumen; detalle en `piezas-graficas.md`)
- Formatos: cuadrado 1080×1080, vertical 1080×1350 (feed 4:5), historia 1080×1920 (sin texto en el 14 % superior ni inferior = 270 px), portada de ebook 1080×1620 (2:3). Meta acepta JPG/PNG.
- Tres niveles de jerarquía: 1) titular o cifra, 2) precio o dato de apoyo, 3) botón. Titular ≤ 9 palabras y ≤ 70 caracteres, que empiece por el beneficio o un verbo.
- Máximo 2 tipografías y 3 colores (fondo, texto, acento) en la regla general; un solo botón con verbo y destino («Escríbenos por WhatsApp», nunca «Click aquí»).
- Dibujo vectorial con texto convertido a trazados (se ve igual en cualquier programa); sin sombras ni efectos de imagen; exportar PNG 1080 px de ancho + SVG editable.
- Fotos de personas ancladas arriba (`foco: arriba`); edificios, productos y espacios al centro. Nunca un flyer con letras como foto.
- Probar con 3 titulares × los formatos que se usen, misma estructura, cambiando **una** sola cosa por prueba.
- La pieza usa uno de los 10 estilos de las landings para que anuncio y página parezcan de la misma marca.
- Plantilla `cifra`: sin `fuente_dato` no se genera.

## UI de plataforma (resumen; detalle en `ui-plataforma.md`)
- **Todo término técnico lleva su icono de ayuda** con cuatro líneas: qué es · de dónde sale · cómo afecta · ejemplo (glosario único).
- **Todo resultado se interpreta solo:** bloque plegable «Lecturas», cerrado por defecto, que dice qué decisión sale del dato y con qué cruzarlo; no repite lo que ya se ve; si falta el dato, la lectura no aparece y se dice que falta.
- Tokens como variables CSS en `:root` + `@theme inline` de Tailwind 4; modo oscuro con `prefers-color-scheme` protegido por `:root:not([data-theme="light"])` y espejo en `:root[data-theme="dark"]` (patrón de creator).
- Biome en los repos aiuda-empresas, creator y laundry-vip: comillas simples, sin punto y coma, 100 columnas, 2 espacios, comas finales; máximo 300 líneas por archivo.
- Nada de «próximamente»: o funciona o no se muestra.

## Glass de adsboom (resumen; detalle en `glass-adsboom.md`)
- Solo para adsboom. Tokens `--glass-*`, clases `.glass`, `.glass-sm`, `.glass-pill`, componentes `GlassCard/Button/Input/Select/Toggle/Modal/Loader`.
- CSS puro, **sin WebGL**. Tema claro/oscuro con `data-theme` en `<html>`.
- Riesgos conocidos: `--text-muted` claro no pasa 4,5:1; el modal no atrapa foco ni declara `role="dialog"`; animaciones infinitas sin `prefers-reduced-motion`. Corregir al reutilizar.

## Choques entre fuentes (quién manda)
1. **Precio en landings vs. en anuncios.** Landings (docs/14, Byron 2026-10-09): el efectivo/transferencia es el precio más grande. Anuncios vectoriales (`conocimiento.ts` regla «precio» y `anuncio-vectorial.ts`): el precio publicado es el de tarjeta y el efectivo va como nota/descuento. **Decidido por Byron (2026-10-11): el precio grande es el de efectivo o transferencia, también en anuncios.** El de tarjeta va más pequeño. Los archivos de código de anuncios (`conocimiento.ts`, `anuncio-vectorial.ts`) y `docs/15` deben alinearse a esto.
2. **Texto sobre foto.** La regla «nunca letras sobre una foto» aplica a landings y piezas estáticas. En reels/video el texto en pantalla es parte del formato (`reel.md`), siempre dentro de la zona segura y sin tapar rostros. Esta delimitación es una interpretación: ninguna fuente la escribe tal cual.
3. **Zona segura de historias:** 270 px (14 %, `tipos.ts`) frente a 250 px (`historia.md`). Usar 270 (más estricta).
4. **Titulares:** ≤ 9 palabras / 70 caracteres en la pieza; 6–12 palabras en el hero de landing; 40 caracteres en el campo titular del anuncio en Meta; hooks ≤ 10 palabras. Son medios distintos: aplicar el límite del medio donde va el texto.
5. **Mayúsculas y tipografías:** la regla general dice «sin frases en mayúsculas» y «máx. 2 tipografías», pero los estilos Alta conversión y Kraft usan mayúsculas tipográficas (`mayus: true`) y Kraft combina Anton, Courier y Caveat. Se entiende que la regla es de redacción y que el estilo puede imponer mayúsculas o una tercera familia de apoyo; no está escrito explícitamente.

## Origen
- `crm-321/CLAUDE.md` (reglas A–J, producto replicable, stack).
- `crm-321/docs/14-diseno-landings.md` (decisiones de Byron, investigación, 10 estilos, jerarquía, checklist, precio, prueba de titulares).
- `crm-321/docs/16-diseno-vectorial.md`, `crm-321/docs/18-ebooks.md`.
- `crm-321/src/lib/vectorial/conocimiento.ts`, `estilos.ts`, `tipos.ts`, `ia.ts`; `crm-321/src/lib/marketing/base-anuncio.ts`, `piezas.ts`; `crm-321/src/lib/academy/anuncio-vectorial.ts`; `crm-321/src/lib/lecturas-vectorial.ts`.
- `crm-321/src/components/Ayuda.tsx`, `Lecturas.tsx`, `ui.tsx`, `src/app/globals.css`, `src/lib/glosario.ts`.
- `postpro-321/motor/skills/diseno-piezas.md`, `historia.md`, `reel.md`.
- `bcujano/creator/src/app/globals.css`, `biome.json`; `bcujano/aiuda-empresas/src/app/globals.css`, `biome.json`, `CLAUDE.md`; `bcujano/laundry-vip/src/app/globals.css`, `biome.json`, `CLAUDE.md`.
- `bcujano/adsboom/CLAUDE.md`, `src/app/globals.css`, `src/components/glass/*`, `src/components/layout/ThemeToggle.tsx`.
