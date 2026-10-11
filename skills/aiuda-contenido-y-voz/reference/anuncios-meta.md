# Anuncios en Meta · detalle

Fuentes: `postpro-321/motor/skills/anuncios-meta.md` y `segmentacion-meta.md`, notas de API de `crm-321/CLAUDE.md`, y `crm-321/docs/08-mapa-del-sistema/03-marketing-ia-motor-publicidad.md` §6 y §8.

## 1. Principio
El anuncio no debe parecer anuncio: estética orgánica de Instagram, con una persona real o el espacio real.

## 2. Ángulos (un anuncio = un ángulo)
dolor · resultado · prueba (solo datos reales de la ficha) · curiosidad · comparación · urgencia (solo si es real) · identidad («para el que…») · contrario.
- Inmobiliario: precio-ubicación, estilo de vida, inversión/rentabilidad (solo con datos de la ficha), objeción.
- Construcción modular: tiempo de entrega, precio frente a la obra tradicional, antes/después, el proceso.
- Cursos: el anuncio y su landing deben parecer de la misma marca (misma paleta y tipografía, regla de diseño «estilo»).

## 3. Formatos (orden de preferencia)
1. Reel 9:16 de 10–15 s (principal): primeros 3 s = el espacio más impactante o la cara del fundador + texto con el hook.
2. Persona a cámara (UGC / «fundador»): el que más convierte cuando alcanzan los créditos.
3. Carrusel 4:5: recorrido de la propiedad o del proceso.
4. Estático 4:5: antes/después, problema/solución o tarjeta de preguntas frecuentes. Evitar muros de logos y tarjetas de reseñas.
- Piezas gráficas: 1080×1080, 1080×1350, 1080×1920; zona segura de 14 % arriba, 35 % abajo y 6 % a los lados en Stories/Reels. Ver skill `aiuda-diseno`.

## 4. Copy
- Texto principal: lo importante en los primeros **125 caracteres**. Titular: máx. **40**. Descripción: máx. **25**.
- Marcos: PAS, BAB y AIDA (propiedades).
- CTA según destino: mensaje de WhatsApp o Instagram con texto precargado («Hola, quiero la ficha de [nombre]»).
- Tono del fundador, sin superlativos vacíos, datos solo de la ficha.
- Botones de CTA admitidos al generar copy de curso: `LEARN_MORE`, `SIGN_UP`, `WHATSAPP_MESSAGE`.

## 5. Hook del video (3 capas, cada una aporta algo distinto)
Visual (qué se ve en el cuadro 1) + hablado + texto en pantalla. Aperturas: vacío de curiosidad, afirmación fuerte, antes/después, POV, pregunta, prueba primero. Ver fórmulas en `guiones-y-formatos.md`.

## 6. Pruebas
- Por campaña: 3–5 ángulos × 2 hooks; cambiar UNA sola variable por prueba.
- Orden de lo que se prueba: concepto > hook > visual > cuerpo > CTA.
- Juzgar con 1.000 impresiones como mínimo. 70 % del presupuesto a lo probado y 30 % a lo nuevo.
- Subir el presupuesto 20 % como máximo cada 3 a 5 días.

## 7. Diagnóstico con métricas
| Síntoma | Acción |
|---|---|
| Hook rate bajo (vistas de 3 s / impresiones < 25 %) | cambiar el inicio visual |
| Retención baja de 3 a 15 s | reescribir el cuerpo |
| CTR bajo (< 1 %) | afinar la promesa o el CTA |
| Muchos clics y pocos mensajes | alinear el destino (mensaje precargado, ficha coherente con el anuncio) |
| CPM alto con CTR bueno | ampliar la audiencia |
| Frecuencia > 3 con CTR en caída | renovar el creativo (fatiga) |

## 8. Segmentación
- Fuente de verdad: el bloque de segmentación de la ficha (lo llena el equipo). Si la ficha lo trae, se respeta; si no, se infiere de la ficha y se marca como «sugerida».
- Meta optimiza mejor con audiencias amplias y creativos específicos: el creativo llama al nicho; la segmentación solo acota lo imprescindible (ubicación, edad, idioma).
- Ubicación: ciudad o radio alrededor del sector de la ficha; para construcción modular, todo el país o las provincias indicadas (el producto se transporta).
- Edad sugerida por línea (orientativa; ver restricción de la API abajo): vivienda para comprar 28–60; inversión y Airbnb 30–65; alquiler 22–45; construcción modular 28–60.
- Intereses solo como pista (Advantage+ audience activo): bienes raíces, inversión, Airbnb, arquitectura, casas modulares o prefabricadas, turismo rural.
- Objetivo: mensajes (WhatsApp o Instagram) para generar leads; tráfico solo si hay landing.
- Presupuesto inicial: $5 a $10 por día por conjunto, 3 a 5 anuncios por conjunto.
- Excluir a quienes ya escribieron (si existe la audiencia) para no pagar dos veces por el mismo lead.

## 9. Notas técnicas de la API de Meta (v22.0, de `crm-321/CLAUDE.md`)
- `advantage_audience=1` obligatorio → `age_min` máximo 25 y `age_max` fijo 65. En la práctica la edad que proponga la IA se ignora.
- CTA de WhatsApp: `{ type: 'WHATSAPP_MESSAGE', value: { app_destination: 'WHATSAPP' } }` **sin** enlace.
- ABO requiere `is_adset_budget_sharing_enabled=false` explícito.
- CBO requiere `budget_rebalance_flag=true` y `daily_budget` en la campaña.
- Imágenes de Google Drive: convertir a URL directa (`toDirectUrl`).
- `slideshow_spec` de Meta NO funciona → generar un MP4 real con ffmpeg.
- Objetivos del CRM → Meta: mensajes de WhatsApp e Instagram → `OUTCOME_ENGAGEMENT` (destino WhatsApp o mensaje directo; conjunto con `CONVERSATIONS`); formulario → `OUTCOME_LEADS`; tráfico → `OUTCOME_TRAFFIC`.
- Flujo: plan → aprobación (equivale a autorizar el gasto) → creativos → creación en Meta **en pausa**. Solo Byron activa desde el administrador.
- Máx. 8 anuncios por plan y máx. 1 de persona a cámara; el enrutador baja de formato si los créditos no alcanzan (presupuesto = 70 % de los créditos).
- Sin verificar: si los anuncios inmobiliarios en Ecuador exigen la categoría especial `HOUSING`; hoy se crean con `special_ad_categories: []`.
- Hallazgo de la auditoría: en casi todas las llamadas el token viaja en la query string y puede quedar en registros; mejor enviarlo en un encabezado. Nunca pegar tokens en documentos ni en piezas.

## 10. Pieza de anuncio de curso (reglas de crm-321)
- Se arma con el precio, la etapa y las fechas de hoy desde la base; la IA solo redacta.
- Foto del hero del curso (no el flyer), cuenta regresiva con fecha real, etapa vigente destacada.
- Mismo estilo que la landing; 3 titulares × formatos para probar.

## Origen
`postpro-321/motor/skills/anuncios-meta.md`, `segmentacion-meta.md`; `crm-321/CLAUDE.md` (Notas Meta API v22.0); `crm-321/docs/08-mapa-del-sistema/03-marketing-ia-motor-publicidad.md` §6, §8; `crm-321/src/lib/academy/ia.ts` (botones y titulares de anuncio); `crm-321/docs/16-diseno-vectorial.md`.
