# Estrategia de campaña para un curso o taller con precio por fases · detalle

Método tomado de la campaña del Taller de IA de Byron (octubre de 2026), sin sus datos finales: precios, fechas, lugar y textos de campaña son del evento y viven en el sistema, no aquí. Etiquetas: [E] repo, [I] inferencia a validar con datos propios.

## 0. Lo que solo el dueño puede dar (preguntar UNA vez, en una sola pregunta, con valores por defecto)
1. Presupuesto diario (por defecto 6 anuncios y ~$15 a $20 por día; si es menor, lanzar solo 4).
2. Destino del clic: formulario de Meta, landing con registro o WhatsApp (por defecto los botones dicen «Reserva tu cupo» y el CTA nativo de Meta es «Registrarse»).
3. Pixel y API de Conversiones instalados (por defecto: asumir que no y pedir un lead de prueba).
4. Hasta qué hora vale la fase vigente el día del cambio (recomendado: termina a las 23:59 del último día y la fase siguiente empieza a las 00:00 del siguiente).
5. Que las promesas del temario sean ciertas (cada promesa del anuncio debe estar en el temario).
Cuando el dueño ya lanzó la campaña, no volver a pedir esos datos salvo que él los traiga.

## 1. Estructura
- 1 campaña de clientes potenciales (o de mensajes si cierra por WhatsApp), 1 conjunto, país + Advantage+ audience + Advantage+ placements. Nada de apilar intereses: el creativo es la segmentación.
- 6 anuncios por fase (4 buenos mejor que 20 mediocres; 10 a 20 diversos si hay presupuesto). Cada pieza en 4:5 (Feed) y 9:16 (Stories y Reels) como personalización de ubicación.
- No editar anuncios activos: si uno falla, lanzar uno nuevo.
- Nombres de anuncio: `<CAMPAÑA>_F<fase>_<n>_<concepto>`.

## 2. Juego de conceptos (seis, distintos entre sí en escena, formato, ángulo y segmento)
| Concepto | Gancho (patrón) |
|---|---|
| Hoja de ruta | «Desde X hasta Y» con los días del programa |
| Creencia rota | «¿Todavía haces X como Y?» + lo que se aprende |
| Checklist de temario | «N días, N cosas que tu negocio ya puede …» |
| Precio que sube | La escala de precios y la próxima fecha (válido solo mientras la escala sea cierta) |
| Nota de iPhone | Lista de lo que se practica, dirigida a un perfil |
| Chat de WhatsApp | Pregunta del perfil + credencial real del instructor |
Reserva para la semana 2 (rotación 3-3-2-2): pregunta directa, un perfil adicional, otro perfil, otro perfil.

## 3. Fases de precio
- Cada fase resalta su precio en una escala visible de todas las fases (la vigente resaltada) y cambia solo el bloque final del copy y el texto del ángulo de precio.
- La fase siguiente se publica como **anuncios nuevos**, y la anterior se pausa a la hora del cambio.
- «Últimos cupos» solo si es verdad. La escala de precios del evento debe mostrar el precio vigente según la decisión de Byron del 2026-10-11 (el de efectivo o transferencia, el más grande); ver `knowledge/decisiones/contenido-higgsfield.md`.

## 4. Calendario tipo (alrededor de un evento)
| Momento | Acción |
|---|---|
| Día 0 | Checklist previo. Publicar la fase 1 (6 anuncios, 1 conjunto) |
| Día 1 | Mirar solo señales: rechazos, entrega, CTR, costo por resultado. No tocar nada |
| Día 2 | Lectura de 48 h. Pausar los que cumplan la regla de pausa. Preparar la fase 2 como anuncios nuevos |
| Cambio de fase | Pausar la fase vigente y publicar la siguiente a la hora exacta |
| Mitad de la fase | Rotación 3-3-2-2: sumar 2 de la reserva y pausar los 2 peores |
| Últimos días | Último empuje; preparar la fase final; retargeting (visitas, interacciones, leads sin compra) |

## 5. Reglas de decisión
Ver `andromeda-y-pruebas.md` §3 (umbrales, pausa, escalado, frecuencia).

## 6. Checklist previo al gasto (pasa o no pasa)
- [ ] Gancho entendible en < 2 s y un solo mensaje por pieza.
- [ ] Texto legible en celular (titulares ≥ 64 px, secundarios ≥ 32 px en 1080).
- [ ] 9:16 con zonas libres (ver `diseno-y-copy.md` §2).
- [ ] Las piezas se ven distintas entre sí (< 40 % parecido).
- [ ] CTA única; mismo precio y fecha que la página de destino.
- [ ] Sin promesas no verificadas ni atributos personales.
- [ ] Sin em dashes ni frases «No es X, es Y».
- [ ] Píxel y API de Conversiones probados con un lead de prueba.

## 7. Copys: estructura que se usó
Archivo único por juego con texto principal (hook en las 2 primeras líneas), titular, descripción y CTA. Bloque final fijo: fechas, horario, lugar, certificado, «cupos limitados» y la frase de la fase de precio. Hay un bloque por fase. Notas de honestidad al pie: qué cifras **no** se usan por no verificadas y cuándo caduca un anuncio.
Las credenciales del instructor (años de experiencia, empresas ayudadas) son datos reales entregados por el dueño: se usan solo tal cual los dio.

## 8. Siguiente paso tras la semana 1
Retargeting en un segundo conjunto con las piezas de reserva; medir por pieza y repetir lo que gane **cambiando una variable** (nuevo gancho, otra foto), no con lo mismo.

## Origen
- `contenido-higgsfield/taller_prompting/ads_nativo/ESTRATEGIA_META_ADS_TALLER.md`.
- `contenido-higgsfield/taller_prompting/LEEME_PRIMERO.md` (§7, §8, §10).
- `contenido-higgsfield/taller_prompting/COPYS_TODOS_LOS_JUEGOS.md`, `ads_meta/copys_meta_ads.md`.
