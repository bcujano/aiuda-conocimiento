# Costos, límites y errores aprendidos · detalle

USO INTERNO. Costos observados en una cuenta con plan Plus en octubre de 2026 (cifras de la sesión, no tarifa oficial; volver a consultar).

## 1. Costos medidos
| Concepto | Costo observado |
|---|---|
| `soul_2` 2k, por imagen | ~0,12 créditos |
| `gpt_image_2_5` por imagen | ~0,125 (calidad alta 2k, 3 imágenes generadas con referencia: 20,25 créditos en total en una tanda del despacho) |
| `nano_banana_2` | 1,5 |
| Ampliar 2× (upscale) | ~2 |
| Tanda de 12 fotos Soul (despacho) | 3,44 |
| Entrenar un Soul | ~25 según un tercero; no confirmado |

Saldos de referencia: 130 créditos al cierre de la sesión del 4 de octubre; ~105 al preparar el Soul del despacho. Se anota el saldo antes y después de una operación nueva y se informa el cobro real.

## 2. Límites de la plataforma
- 8 trabajos concurrentes.
- El lote de imágenes exige una lista de pedidos con `count`=1 cada uno y **no tiene consulta de costo: enviar `get_cost` ahí lanza un trabajo real** (y se cobra).
- Subir un archivo local: pedir URL firmada, subir con PUT (esperar HTTP 200) y confirmar.
- La CLI de Higgsfield no muestra el costo antes de entrenar un Soul.

## 3. Errores que no repetir
1. Generar lo que el usuario no pidió: se gastaron ~1,4 créditos en versiones 9:16 no pedidas; trabajos «huérfanos» quedaron en la plataforma sin usarse (se anotan sus IDs en el handoff para no duplicar).
2. Mezclar herramientas para tareas de parecido (GPT Image con referencia para cambiar la cara): rechazado.
3. Banners genéricos tipo «dueños de negocio, tu competencia ya usa IA»: rechazados por el dueño.
4. Primeras rondas con GPT Image y referencias (carpetas `ads_meta`, `ads_meta_v2`): rechazadas, no repetir.
5. No verificar con zoom: se publican palabras rotas («Resultadas», «Bienes», «Aluda»).
6. Tomar sin revisar datos de una referencia del usuario (traía «FENATRARE» mal escrito): corregir y avisar.
7. Estilo «editorial» sin pedir fondo vacío: letras basura en el fondo.
8. Describir barba o pelo de más: cambió el parecido.
9. Los carteles de la oficina con texto roto en fotos clonadas de una referencia.
10. Confiar en una foto generada con rostro rapado o poco parecido: reemplazar antes de pautar.
11. Subir a Meta piezas no revisadas: dejar para después de la rúbrica de `aiuda-meta-ads-reglas`.

## 4. Cómo gastar con criterio
- Una prueba, su costo y la elección del usuario antes de cualquier lote.
- Borradores en calidad baja y calidad alta solo en la versión final (fuente de terceros).
- Los vectores y el HTML no gastan créditos: usarlos para todo lo que no sea una persona o una escena fotográfica.
- No ampliar con IA lo que ya es vector.

## Origen
- `contenido-higgsfield/taller_prompting/LEEME_PRIMERO.md` (§2, §5, §9).
- `contenido-higgsfield/fagal/soul_galarraga/LEEME_FOTOS.md`, `fagal/DISENO_ANUNCIOS_ABOGADOS.md` (costos de tandas).
