# Flujo de producción de anuncios · detalle

USO INTERNO. Pipeline probado en el proyecto (`BASE_CONOCIMIENTO_ADS.md` §4, `LEEME_PRIMERO.md` §4 y §8, `higgsfield_meta_ads_nativo.md` §3).

## 1. Pasos
1. **Entradas por campaña:** oferta (fecha, lugar, precios, credenciales reales), segmentos, un Soul aprobado (si hay persona), paleta y fuentes del juego, fase de precio vigente.
2. **Conceptos:** 4 a 8 por segmento, con hook de 3 a 7 palabras; el título dice a quién llama («Taller de IA para …»). Los conceptos se aprueban con el usuario antes de gastar. Reparto sugerido y diversidad: `aiuda-meta-ads-reglas`.
3. **Fotos:** `soul_2` + Soul ID, 3:4 (9:16 solo si hace falta), sin texto, con espacio vacío para el titular. Primero UNA prueba con costo. El usuario elige en una hoja numerada y esa es la única foto que se usa.
4. **(Opcional) Pixel art:** ver `soul-y-fotos.md` §4.
5. **Maquetar** en HTML/CSS (una plantilla por concepto) y renderizar a 4:5 y 9:16. Ver `texto-html-render.md`.
6. **Revisar con zoom:** ortografía, tildes, solapes, rostro tapado, zonas seguras, letras basura, ropa, correa, manos. Se corrige en el script, no en la imagen.
7. **Copys** en un archivo único por juego (texto principal, titular, descripción, CTA): `aiuda-meta-ads-reglas/reference/diseno-y-copy.md`.
8. **Rúbrica previa al gasto** (promedio ≥ 7): `aiuda-meta-ads-reglas/reference/andromeda-y-pruebas.md` §rúbrica.
9. **Subir a Meta** por fases de precio y rotar semanalmente.
10. **Entrega al usuario:** carpetas por juego y por fase, con nombres estables (`<campaña>_F<fase>_<n>_<concepto>`).

## 2. Cómo regenerar
- Un script por juego; ejecutarlo desde su carpeta con `FASE=<n> python render_<juego>.py [ids] [4x5|9x16]`.
- Cambiar un texto = editar la función de la plantilla y volver a correr (segundos).
- Cambiar de fase de precio = la variable de fase resalta otra etiqueta y cambia los textos del precio; la fase siguiente exige agregar su caso al mapeo (en el original quedó pendiente la fase 3 hasta antes de su fecha).
- Las fotos elegidas viven en una carpeta propia (`fotos_set3/<ID>_45.png`); el formato 9:16 recorta la misma foto con `cover` (no se genera otra).
- Los IDs de trabajos de las fotos elegidas se guardan en el handoff del proyecto para poder reutilizarlas como referencia; **no** se guardan en el centro de conocimiento.

## 3. Formatos de anuncio que rindieron mejor en el diseño (según fuentes, no medido en este proyecto)
Los formatos «no parecen anuncio» rinden mejor en tráfico frío: conversación tipo chat, tweet, nota de iOS, post nativo, selfie UGC ligeramente imperfecta, testimonio, listicle, dato único grande, flat-lay (gquthier/autonomous-ad-creative). Mezcla recomendada: 2-3 nativos, 1-2 UGC, 1-2 de valor, 1 carrusel, 1 interruptor de patrón. Los formatos de foto (candid, editorial, detrás de cámaras) los genera Soul en una pasada y el texto va después; los de pantalla van 100 % en HTML con la foto como avatar.

## 4. Conceptos vectoriales usados como plantilla (8)
Cartel tipográfico de una palabra gigante · número gigante («9 h») · checklist tipo app de notas · tabla Antes/Después o «sin IA / con IA» · ticket de evento · diagrama de flujo de 3 nodos · quiz con pregunta provocadora · carta del fundador. Cada uno cambia layout, paleta y mensaje; solo logo y botón son constantes. Para clientes de otro rubro se reutiliza la forma del lenguaje gráfico, no los textos.

## 5. Lecciones de proceso
- Dar los valores por defecto y preguntar UNA vez, en una sola pregunta, lo que solo el usuario sabe (presupuesto diario, destino del clic, píxel y API de Conversiones, vigencia de una fase, promesas del temario). No parar la producción por eso.
- No re-investigar repos: la investigación ya está enlazada en `aiuda-meta-ads-reglas/reference/fuentes.md`.
- Una pieza descartada por el usuario no se vuelve a ofrecer (la serie de 8 «m» del despacho se descartó con «prácticamente lo mismo»: variaciones de color sobre el mismo diseño no cuentan como concepto nuevo).
- Registrar al cierre de la sesión: qué gustó, qué no, saldo de créditos y trabajos huérfanos.

## Origen
- `contenido-higgsfield/taller_prompting/LEEME_PRIMERO.md` (§4, §6, §8, §9).
- `contenido-higgsfield/taller_prompting/BASE_CONOCIMIENTO_ADS.md` (§4, §5).
- `contenido-higgsfield/taller_prompting/higgsfield_meta_ads_nativo.md` (§2.1, §3).
- `contenido-higgsfield/taller_prompting/diseno_vectorial_reglas.md` (§c).
- `contenido-higgsfield/fagal/DISENO_ANUNCIOS_ABOGADOS.md`.
