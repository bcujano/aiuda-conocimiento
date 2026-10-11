# Soul ID, fotos de personas y estética · detalle

USO INTERNO. Fuente principal: `taller_prompting/LEEME_PRIMERO.md` §2, §5, §9 y `fagal/soul_galarraga/LEEME_FOTOS.md`.

## 1. Soul ID
- Un Soul es un modelo entrenado con la cara de una persona. Se pasa siempre el Soul ID al generar fotos de esa persona. El ID del dueño se guarda fuera del centro de conocimiento.
- Modelo de imagen usado para las escenas: `soul_2` (Soul 2.0) con `soul_id`. Admite 1:1, 16:9, 9:16, 4:3, 3:4, 3:2 y 2:3; **no admite 4:5**: se genera 3:4 y se recorta.
- Soul 2.0 no combina `style_id` con `image_references` (máximo 1 referencia) [fuente de terceros, `higgsfield_meta_ads_nativo.md` §2.2]. Si la cara se desvía: quitar `style_id`, simplificar el prompt, subir `quality` en la versión final (hivijc/higgsfield-ugc-playbook, vía el mismo archivo).
- Nano Banana 2 figura en las fuentes como el de mejor coincidencia facial y el mejor para correcciones pequeñas de una línea, pero **en este proyecto** el dueño rechazó editar caras con otros modelos. Regla: escena nueva con Soul, no parche.
- Hubo tres versiones del Soul del dueño (2.0, 3.0, 3.01). Se usó siempre la más reciente que el dueño eligió. Confirmar cuál antes de cada creación si hay duda.
- Entrenar un Soul: 5 a 20 fotos, ideal 8 a 12; solo la persona en cada foto, cara nítida, ojos visibles, mínimo 1024 px, originales (no capturas de redes, sin texto encima), variedad de ángulos y de luz, look real y constante (barba, peinado, traje). No sirven fotos generadas por IA, de grupo, con disfraces ni repetidas. No entrenar un Soul por un pedido suelto (william-zou21/Higgsfield.UGC.Generator, vía `higgsfield_meta_ads_nativo.md`).
- **Condición antes de entrenar a una tercera persona (cliente):** autorización escrita de esa persona. Las escenas deben ser verosímiles (retrato, oficina, escritorio, reunión): no inventar audiencias, firmas de convenio ni clientes. Una imagen generada de una persona real, usada en un anuncio, debe aprobarla esa persona (quedó pendiente en el caso del despacho de abogados).

## 2. Prompts que funcionaron
Base candid (foto «de iPhone»): `Candid iPhone photo, 24mm, handheld... natural skin texture with visible pores, mild film grain, no retouching... Subject on the right/lower, clean empty wall in the top 40% for text. No text, no logos.`

Elementos útiles (de las fuentes; los marcados [I] son inferencia no comprobada con datos):
- Mirada: fuera de cámara o hacia lo que hace; no señalar a cámara [I].
- Encuadre con aire: «subject placed in the lower third / left third, large clean area of plain wall / out-of-focus background in the upper X%».
- Luz imperfecta, mezcla de luz de ventana y lámpara cálida, grano 35 mm, sin retoque (anti piel plástica).
- Lugar real y verosímil (coworking, café, aula, oficina).

Prompts de vestuario (copiar tal cual al final del prompt):
- Correa: `luxury plain black leather belt, no logo, no branding, matte black buckle that blends into the leather, no shiny metal, no chrome, no gold`
- Prenda impecable: `impeccably tailored, freshly pressed, perfectly smooth fabric with no wrinkles or creases, clean sharp seams, collar and cuffs neatly aligned, shirt tucked in neatly with a clean waistline`
- Barba y pelo: `short dark textured hair, short trimmed beard`. Describir el pelo con otras palabras a veces cambió el parecido (una foto salió rapada y se descartó).

## 3. Qué evitar al generar
- El estilo «editorial / magazine / advertising» hace que Soul **invente letras sin sentido en el fondo**. Pedir: `perfectly plain, empty, uniform seamless backdrop with nothing on it, no graphics, no lettering, no signs`.
- Pantallas, pizarras, aviones u objetos con logo dentro de la foto generan texto basura. Evitarlos.
- Letreros con texto roto en la oficina (en el caso del despacho salió el nombre del cliente mal escrito): se borran con relleno de pared, se recortan o se tapan en el montaje. Mejor evitar que haya placas o carteles en el prompt.
- Oficina clonada de una referencia: el fondo trae placas diminutas ilegibles; revisar con zoom.
- Fotos de clases con pizarra o pantalla: rechazadas por el dueño.
- Look stock: sonrisa a cámara, brazos cruzados, oficina vidriada, apretón de manos genérico, «traje de espaldas».

## 4. Pixel art (única excepción a «escena completa en una generación»)
Soul no hace pixel art directo.
1. Generar el sprite con `gpt_image_2_5` usando una foto Soul como referencia, fondo magenta plano.
2. Quitar el fondo por chroma-key: umbral `r>170 & b>170 & g<120` o distancia a (255,0,255) menor a 120; luego recortar al contenido (`getbbox()`).
3. Máximo 3 anuncios con pixel art por juego. El pelo del busto salió más castaño que el real; el sprite de cuerpo completo fue el más fiel.
4. `nano_banana_2` cuesta mucho más (ver `costos-y-errores.md`); no usarlo salvo que haga falta.

## 5. Fotos para despachos y servicios profesionales
- La investigación inicial recomendó fotos reales de los socios (la cara real es credibilidad; el rostro de IA es riesgo reputacional) y reservar el Soul para el dueño de AIUDA.
- Después se entrenó un Soul del socio del despacho (decisión del dueño, mismo día) y se generaron fotos. Por eso quedó como **pendiente** la aprobación escrita del socio para usar su imagen generada, y la advertencia de que Meta puede etiquetar imágenes de IA y de que **no deben usarse para mostrar eventos reales** (audiencias, firmas, clientes). Ver contradicción 2 en `knowledge/decisiones/contenido-higgsfield.md`.
- Al pedir fotos reales a un cliente (mensaje modelo): 3 o 4 por tipo (abogados en acción, convenios, con clientes); sin texto, logos pegados, marcas de agua, filtros ni collages; caras visibles y buena luz; que no se alcance a leer ningún documento ni pantalla; enviar como «documento» para evitar la compresión; solo personas que aceptan aparecer. Con 10 a 12 fotos alcanza. Las capturas de redes no sirven.

## Origen
- `contenido-higgsfield/taller_prompting/LEEME_PRIMERO.md` (§2, §5, §9, §10).
- `contenido-higgsfield/taller_prompting/higgsfield_meta_ads_nativo.md` (§2.2, §2.3).
- `contenido-higgsfield/taller_prompting/BASE_CONOCIMIENTO_ADS.md` (§2, §4).
- `contenido-higgsfield/fagal/soul_galarraga/LEEME_FOTOS.md`, `fagal/WHATSAPP_PEDIR_FOTOS.md`, `fagal/DISENO_ANUNCIOS_ABOGADOS.md` (tandas final y t5), `fagal/INVESTIGACION_FAGAL_B2B.md` (§7).
