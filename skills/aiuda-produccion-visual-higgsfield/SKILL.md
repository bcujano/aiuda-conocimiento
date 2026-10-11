---
name: aiuda-produccion-visual-higgsfield
description: Flujo de AIUDA para producir anuncios y piezas visuales con Higgsfield: Soul ID, escena completa en una generación, prueba y costo antes de lotes, texto en HTML/CSS y no en la imagen, vestuario y errores aprendidos. Úsalo al generar fotos de personas, anuncios o piezas de campaña con IA de imagen.
---

# AIUDA · Producción visual con Higgsfield

**USO INTERNO.** Este skill describe herramientas y método de producción. No se le explica al cliente cómo está hecho (regla D de crm-321): se le entrega la pieza y se le dice qué hacer con ella. Si el cliente pregunta, solo que la imagen es generada por IA y que el texto es siempre exacto.

Fuente: el repo `contenido-higgsfield` (sesiones del 2026-10-03 al 2026-10-07). Todo lo de abajo salió de ahí; lo no comprobado está en «No verificado».

Detalle en `reference/`:
- `reference/flujo-produccion.md` · pasos de idea a archivo final, cómo regenerar por fase de precio, control de calidad.
- `reference/soul-y-fotos.md` · Soul ID, prompts que funcionaron, composición, vestuario y estética.
- `reference/texto-html-render.md` · método de texto en HTML/CSS y render a PNG, tamaños.
- `reference/costos-y-errores.md` · costos medidos, límites de la plataforma, errores que no repetir.
- `reference/skills-terceros.md` · los 8 skills de higgsfield-ai: cuándo usar cada uno y versión fijada.

## Cuándo usar cada referencia
| Tarea | Lee |
|---|---|
| Producir un lote de anuncios de principio a fin | `flujo-produccion.md` |
| Generar fotos de una persona (dueño, instructor, socio) | `soul-y-fotos.md` |
| Montar titulares, precios, botones sobre la foto o en vectorial | `texto-html-render.md` |
| Estimar gasto, entender un fallo de la plataforma | `costos-y-errores.md` |
| Elegir un skill de Higgsfield de terceros | `skills-terceros.md` |
| Qué decir en Meta, segmentación, copy | skill `aiuda-meta-ads-reglas` |
| Reglas de composición de anuncios gráficos y landings | skill `aiuda-diseno` |

## Reglas que no se negocian
1. **Personas siempre con su Soul ID.** El Soul ID del dueño se guarda fuera del centro de conocimiento (en la configuración del sistema). Si hay duda de cuál Soul usar, se confirma antes de crear, no después. Hay un Soul por persona: no mezclar.
2. **La escena completa sale de UNA generación** (fondo, luz, ropa, pose, todo en el prompt). Nunca recortar un sujeto y pegarlo en otro fondo. Nunca usar un modelo de edición con foto de referencia para «cambiar la cara»: pierde el parecido y se nota. Única excepción aprobada: pixel art (ver `soul-y-fotos.md`).
3. **Usar solo las fotos que el usuario eligió.** No generar fotos que no pidió. Se gastaron créditos reales en versiones que el usuario no quería.
4. **Una prueba y su costo antes de cualquier lote.** Se muestra UNA imagen, el costo y se espera la elección. La elección de fotos se hace con una hoja numerada (chooser); el usuario elige él mismo.
5. **El texto va en HTML/CSS y nunca dentro de la imagen generada.** El modelo rompe palabras y tildes («Resultadas», «Aluda», «FENATRARE»); cada arreglo de un texto dentro de la imagen rompe otro. En HTML la ortografía es exacta y no cuesta reintentos.
6. **Generar la foto sin texto, sin logos y con espacio vacío** donde irá el titular («No text, no logos»; zona despejada en la parte superior o a un lado).
7. **Verificar cada pieza con zoom** antes de mostrarla: ortografía, solapes, rostro tapado, letras inventadas en el fondo, manos, ropa.
8. **Decir la verdad sobre errores y costos** y no dejar procesos a medias (trabajos huérfanos en la plataforma se anotan, ver `costos-y-errores.md`).
9. **Solo cifras y datos reales.** Los datos de la oferta (fechas, lugar, precios, credenciales) los da el usuario; no se inventan ni se «mejoran». Si el usuario trae un error (nombre mal escrito), se corrige y se le avisa.

## Vestuario y estética (regla del dueño, aprendida con errores)
- Camisa de vestir, no camiseta. Camisa por fuera salvo traje o corbata; cuando se vea la cintura, correa negra de lujo, sin marca ni logo, hebilla negra mate que se camufla con el cuero (nada cromado ni dorado).
- **Sin ropa café ni amarilla.**
- Ropa planchada, sin arrugas, costuras y capas (camisa bajo el saco, cuello, puños) limpias y alineadas, camisa metida con prolijidad. Se revisa en cada foto.
- Barba corta y definida, no leñador. Se ve premium, nunca «stock» (sin sonrisa a cámara de banco de imágenes, sin brazos cruzados, sin oficina de vidrio genérica).
- Fotos grupales: naturales y con rostros distintos entre sí.
- Los textos de prompt exactos están en `reference/soul-y-fotos.md`.

## Resultado esperado de una pieza
- Foto de persona: una sola generación, 3:4 (se recorta a 4:5 o 9:16 con `cover` en el montaje), sin texto.
- Pieza final: PNG a 1080 px de ancho (4:5 = 1080×1350, 9:16 = 1080×1920) o al doble si el cliente lo exige. Ver tamaños y zonas seguras en `texto-html-render.md` y en `aiuda-meta-ads-reglas`.
- Anuncio que no parece anuncio ni parece IA: formato nativo (nota, chat, ticket, checklist) o vectorial caro, un mensaje y un solo botón.

## Reproducibilidad
- Los generadores son scripts por juego de anuncios: una función por plantilla, parametrizable por segmento, titular y foto; cambiar un texto o una fase de precio = editar el script y volver a renderizar (segundos). Detalle en `flujo-produccion.md`.
- Para otro cliente: cambiar datos (nombre, paleta, fuentes, logo, oferta), no código.

## Skills de terceros (resumen; no se copian aquí)
Se instalan en `.claude/skills/` del repo desde `higgsfield-ai/skills`; el archivo `skills-lock.json` fija la fuente y el hash de cada uno (todos versión 0.12.0 en su encabezado). Solo se usan para lo que dice `skills-terceros.md`. **Donde choquen con las reglas de arriba, mandan las reglas de arriba**: por ejemplo, `higgsfield-generate` prefiere GPT Image 2.5 para texto y pide no estimar costos de antemano; aquí el texto va en HTML y el costo se muestra antes de los lotes.

## Interfaces con otros skills
- Voz, precios, qué nunca se inventa: `aiuda-contenido-y-voz`.
- Composición, tipografía, zonas seguras, estilos: `aiuda-diseno`.
- Qué se sube a Meta y cómo se mide: `aiuda-meta-ads-reglas`.
- Conflictos entre estas fuentes y este skill: `knowledge/decisiones/contenido-higgsfield.md` y `knowledge/contradicciones-abiertas.md`.

## No verificado
- Los costos por imagen son los observados en una cuenta con plan Plus en octubre de 2026; Higgsfield puede cambiarlos. Volver a consultar antes de un lote.
- «25 créditos por entrenar un Soul» viene de una fuente de terceros y no se confirmó en la cuenta.
- Que Meta etiquete como «hecho con IA» las imágenes generadas es una advertencia del repo, no una regla leída en la política de Meta.
- Si la regla «sin texto sobre la foto» de `aiuda-diseno` debe aplicarse a los anuncios de este flujo: ver contradicción 1 en `knowledge/decisiones/contenido-higgsfield.md`.

## Origen
- `contenido-higgsfield/CLAUDE.md`, `skills-lock.json`.
- `contenido-higgsfield/taller_prompting/LEEME_PRIMERO.md`, `BASE_CONOCIMIENTO_ADS.md`, `higgsfield_meta_ads_nativo.md`.
- `contenido-higgsfield/taller_prompting/ads_nativo/render_*.py` (método de texto en HTML), `poster_*.py`.
- `contenido-higgsfield/fagal/soul_galarraga/LEEME_FOTOS.md`, `fagal/DISENO_ANUNCIOS_ABOGADOS.md`, `fagal/INVESTIGACION_FAGAL_B2B.md` (§7).
- `contenido-higgsfield/.claude/skills/higgsfield-*/SKILL.md` (solo encabezados y descripciones).
