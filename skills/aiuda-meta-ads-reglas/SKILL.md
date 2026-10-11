---
name: aiuda-meta-ads-reglas
description: Reglas de Meta Ads aprendidas por AIUDA con fuentes y fechas: estructura de campaña, pruebas y umbrales, diseño y copy de estáticos, segmentación desde el creativo, jerarquía dolor-oferta-botón y anuncios para despachos y B2B. Úsalo al planear, diseñar, escribir o medir anuncios de Meta.
---

# AIUDA · Reglas de Meta Ads

Complementa a `aiuda-contenido-y-voz` (voz, qué nunca se inventa, ángulos, notas de la API) y a `aiuda-diseno` (piezas gráficas, formatos, estilos). **No repite lo que ya dicen**: aquí van las reglas de campaña, creativo, segmentación y B2B que ellos no traen, con sus fuentes. Donde chocan, ver «Choques» al final.

Origen de la investigación: sesiones del 2026-10-03/04 (Taller de IA, repos de GitHub y web) y del 2026-10-07 (despacho de abogados, fuentes oficiales de Meta). Etiquetas de las fuentes: **[V]** verificado en fuente primaria, **[E]** dicho explícitamente en un repo o blog, **[T]** dicho por terceros con interés comercial, **[I]** inferencia del equipo (validar con datos propios), **[?]** sin verificar.

Detalle en `reference/`:
- `reference/andromeda-y-pruebas.md` · estructura de campaña, pruebas, umbrales, presupuesto y rúbrica previa al gasto.
- `reference/diseno-y-copy.md` · formato, zonas seguras, texto, copy y hooks, políticas.
- `reference/segmentacion-desde-el-creativo.md` · qué es verificado y qué es heurística; reglas operativas.
- `reference/anuncios-b2b-despachos.md` · jerarquía dolor-oferta, escalera por segmento, diseño para abogados y servicios de confianza, embudo, cumplimiento.
- `reference/estrategia-campana-evento.md` · plan de campaña para un curso/taller por fases de precio, calendario y checklist.
- `reference/fuentes.md` · enlaces y fechas.

## Cuándo usar cada referencia
| Tarea | Lee |
|---|---|
| Armar o auditar la estructura de una campaña, decidir pausar o escalar | `andromeda-y-pruebas.md` |
| Diseñar o escribir un anuncio estático | `diseno-y-copy.md` |
| Decidir a quién le habla cada pieza sin audiencias | `segmentacion-desde-el-creativo.md` |
| Anuncios para despachos, consultoras, servicios que se compran con tiempo | `anuncios-b2b-despachos.md` |
| Campaña de un evento o curso con precio por fases | `estrategia-campana-evento.md` |
| Producir las fotos y piezas | skill `aiuda-produccion-visual-higgsfield` |
| Voz, ángulos, API de Meta, textos legales | skill `aiuda-contenido-y-voz` |
| Tamaños, estilos y plantillas del generador vectorial | skill `aiuda-diseno` |

## Las reglas que más pesan
1. **El creativo es la segmentación.** Audiencia amplia (solo país, ciudad solo si el negocio atiende en una), Advantage+ audience y ubicaciones; cada pieza nombra a su perfil por rol y negocio, nunca por una condición personal. «El creativo es la segmentación» es **inferencia coherente con lo que Meta publica [I]**, no una frase de Meta.
2. **Conceptos distintos, no variaciones.** Cambiar color o titular no es un concepto nuevo: concepto = otro ángulo, escena, formato o persona. «Más de 60 % de similitud = un solo anuncio» y «Entity ID» **no están en la fuente oficial de Meta [V]**: son heurística de blogs [T]. La acción (variar de verdad) es barata y correcta igual.
3. **Un anuncio, un mensaje, una acción.** Hook de 3 a 7 palabras, un punto focal, un solo botón. El botón lo pone Meta (p. ej. «Registrarse»); no se dibujan botones, encuestas ni chats que parezcan funcionar en el creativo.
4. **No editar anuncios vivos**: se lanzan nuevos. Para juzgar: ≥ 1.000 impresiones, ≥ 3 conversiones y ≥ 2 días (ventana de 7 a 10 días), por costo por resultado real, no por likes ni CPL aislado.
5. **Cero atributos personales y cero garantías.** No afirmar ni insinuar condición del espectador («¿Te estafaron?», «¿Tienes deudas?»); hablar de la empresa y del riesgo. Sin «garantizado»; en servicios legales, sin asegurar el triunfo. Urgencia solo real.

## Estructura mínima de campaña (resumen)
- 1 campaña, 1 a 2 conjuntos, objetivo según el destino: clientes potenciales (formulario) o mensajes (WhatsApp). Advantage+ audience y placements.
- 4 a 6 conceptos realmente distintos si el presupuesto es chico; 10 a 20 si alcanza. Cada uno en 4:5 y en 9:16 (1:1 opcional), versión nativa de cada formato.
- Con texto incrustado: apagar overlays, animaciones y «texto de medios mejorado» de Meta; dejar activos retoques visuales y flex media [E].
- Pixel y API de Conversiones instalados y probados con un lead de prueba antes de gastar. Con servicios que se cierran en reunión, enviar a Meta los eventos Lead → Calificado → Reunión realizada → Contrato desde el CRM [V como capacidad; el detalle de eventos de CRM no se confirmó].
- Presupuesto: subir como máximo 20 % cada 3 a 5 días; frecuencia sana 1,8 a 2,8; más de 2 por semana en frío es alerta; 4 o más pide material nuevo.

## Rúbrica previa al gasto (resumen)
Puntaje 0 a 10 por criterio, ponderado; **lanzar con promedio ≥ 7**. Gancho en < 2 s (×1,5) · un ángulo claro (×1,3) · CTA única visible (×1,3) · encaje con el perfil (×1,2) · diversidad < 40 % frente al resto (×1,2) · legibilidad en móvil, prueba real, seguridad de formato, coherencia con la landing (×1 cada una) · honestidad y políticas (pasa/no pasa, puerta). ≥ 8,5 lanzar y escalar; 7 a 8,4 lanzar con ajustes; 5,5 a 6,9 corregir 2 debilidades; < 5,5 rehacer. Tabla completa en `andromeda-y-pruebas.md`.

## Jerarquía de lectura de un anuncio B2B (resumen)
Perfil nombrado → **el dolor** (≈ 60 % del peso visual, concreto, en términos de pérdida de la empresa) → la agravación (costo de no actuar) → la oferta de entrada (lo gratis y qué incluye) → botón único → credencial. No va: precio, lista de servicios, balanzas, garantías, nombres de terceros. Detalle en `anuncios-b2b-despachos.md`.

## Choques entre este skill y los skills existentes
Detectados al escribirlo; mientras Byron no decida, **aplica lo que dice esta tabla**. Están en `knowledge/decisiones/contenido-higgsfield.md` con más detalle.
| Tema | Este repo | Skill existente | Aplica |
|---|---|---|---|
| Texto sobre la foto | Los anuncios del Taller ponen titular encima de la foto, en una zona despejada con sombra suave | `aiuda-diseno` regla 2: ningún texto sobre la foto (Byron 2026-10-04) | La de `aiuda-diseno`; usar foto sola + texto sobre fondo plano o al lado. Pendiente que Byron aclare si los estáticos de evento quedan exentos |
| Descripción del anuncio | ~30 caracteres | `aiuda-contenido-y-voz`: ≤ 25 | 25 |
| Titular | 27 a 40 | ≤ 40 | 40 como máximo, 27 si cabe |
| «Más información» como CTA en frío | Admite «Más información» y «Registrarse» | «Nunca “Más info”» | «Registrarse» o el CTA del destino; nunca «Más info» |
| «Desde $» | El copy del Taller usa «Desde $65» | Por defecto sin «desde $» | Sin «desde» salvo precio mínimo en ficha |
| Presupuesto inicial | ~$15 a $20 por día para 6 anuncios (evento) | $5 a $10 por día por conjunto, 3 a 5 anuncios | Depende del caso; el segundo es para inmobiliario con mensajes |
| Zona segura 9:16 | 250/340 px; 15 %/20 %; 14 %/35 % + 6 % lados | 270 px arriba y abajo (14 %) | Arriba 14 % (270 px), **abajo 35 %** si va en Reels (oficial) |
| Mayúsculas | CUPOS LIMITADOS, AIUDA, GRATIS apilado | Sin frases en mayúsculas | Las etiquetas cortas se permiten; no se redacta en mayúsculas |
| Cara de IA | Soul del dueño; en el despacho también del socio | `aiuda-diseno` regla 7 y `aiuda-contenido-y-voz`: único personaje real | Solo la persona real autorizada |
| Precio vigente | Escala de precios siempre visible con la fase resaltada | Precio grande = efectivo/transferencia (Byron 2026-10-11) | Aplicar la decisión de Byron a la escala |

## No verificado
- Benchmarks (CTR de 2,59 % para leads, CPL de abogados en EE.UU.) son de blogs; no hay benchmark verificable de Ecuador [T]. Se mide en la primera semana.
- La regla «pausar si el CPL llega a ~3× el objetivo» viene de **un solo repo**: guía, no ley. Igual «máximo +20 % cada 3 a 5 días».
- Si los anuncios de servicios legales o inmobiliarios en Ecuador requieren categoría especial: [?].
- Reglas de publicidad del colegio de abogados local: [?], no se leyeron.
- Cifras de Meta sobre Advantage+ (−14 % costo por lead) son autorreportadas por Meta.

## Origen
- `contenido-higgsfield/taller_prompting/BASE_CONOCIMIENTO_ADS.md`, `meta_ads_reglas.md`, `higgsfield_meta_ads_nativo.md`, `diseno_vectorial_reglas.md`, `reglas_ads.json`.
- `contenido-higgsfield/taller_prompting/COPYS_TODOS_LOS_JUEGOS.md`, `ads_meta/copys_meta_ads.md`, `ads_nativo/ESTRATEGIA_META_ADS_TALLER.md`.
- `contenido-higgsfield/fagal/DISENO_ANUNCIOS_ABOGADOS.md`, `JERARQUIA_Y_COPY.md`, `SEGMENTACION_DESDE_EL_CREATIVO.md`, `CONCEPTOS_6_FAGAL.md`, `INVESTIGACION_FAGAL_B2B.md`, `LINEA_FENATRAPE_Y_REQUISITOS.md`, `CUESTIONARIO_FAGAL.md`.
- Skills comparados: `skills/aiuda-contenido-y-voz/SKILL.md` y `reference/anuncios-meta.md`; `skills/aiuda-diseno/SKILL.md` y `reference/piezas-graficas.md`.
