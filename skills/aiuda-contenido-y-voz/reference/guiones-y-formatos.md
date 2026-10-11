# Guiones y formatos de contenido · detalle

Fuente: `postpro-321/motor/skills/` (`hooks`, `caption`, `carrusel`, `reel`, `historia`) y reglas de `crm-321`. Los marcadores entre corchetes se rellenan SOLO con datos de la ficha; si el dato no existe, se usa otra fórmula.

## 1. Hooks (ganchos que detienen el scroll)
Proceso: escribir 3 candidatos con fórmulas distintas; puntuar cada uno de 1 a 5 en (a) especificidad (número, lugar o plazo), (b) qué está en juego para quien mira, (c) le habla a alguien concreto, (d) lo importante va primero. Usar el de mayor puntaje.

Fórmulas:
1. Precio-zona: «[Tipo] en [sector] por $[precio]. Mira lo que incluye.»
2. Error caro: «Este error al comprar en Quito te puede costar caro.»
3. Deja de: «Deja de pagar arriendo sin revisar esto.»
4. Nadie te dice: «Lo que nadie te dice de construir con contenedores.»
5. Colapso de tiempo: «Obra tradicional: meses. Esta suite: [tiempo de entrega].»
6. Antes/después: «Así llegó este contenedor. Así quedó.»
7. Llamado a nicho: «Si buscas [tipo] en [sector], mira esto.»
8. Pregunta literal: «¿Cuánto cuesta realmente [producto] en Ecuador?»
9. Cara a cara: «Contenedor vs. bloque: ¿cuál conviene?»
10. Demo en frío: arranca en pleno recorrido (puerta abriéndose), sin saludo.
11. Permiso: «No necesitas [obstáculo común] para tener tu primera propiedad.»
12. Contrario: «Comprar terreno barato suele salir caro.»
13. Dato: «[N] m², [N] dormitorios, en [sector].»
14. Insider: «Antes de firmar, reviso siempre esto.»
15. Objeción: «¿Contenedor = casa fría? Te muestro la respuesta.»

Reglas: máx. **10 palabras**; con número, lugar o plazo; el texto en pantalla complementa lo que se dice, no lo repite; un hook que no se cumple en la pieza es un mal hook.

## 2. Reel 9:16
- Movimiento desde el primer cuadro; sin logo, intro ni saludo.
- Ningún tramo de más de **4 s** sin cambio visual (plano, movimiento de cámara o texto nuevo).
- Texto en pantalla: máx. **6 palabras por cartel**, dentro de la zona segura (lejos de bordes y botones).
- Cerrar con lo que prometió el hook; repetir una palabra del hook al final ayuda a que se vuelva a ver (loop).
- Tiempos:
  - 5 s: 0–1,5 hook visual y de texto · 1,5–4 dato o prueba clave · 4–5 CTA.
  - 10 s: 0–2 hook · 2–4 qué está en juego · 4–8 dos ideas de valor (cambio de plano cada ~2 s) · 8–10 lo prometido + CTA.
  - 15 s: 0–2 hook · 2–5 qué está en juego · 5–12 tres ideas (~2,5 s cada una) · 12–15 lo prometido + CTA + loop.
- Movimiento de cámara (el `prompt_visual` va en inglés): propiedad — *slow dolly-in through the doorway, smooth gimbal walk-through, golden-hour light, gentle parallax*; construcción modular — *slow orbit around the container home, drone-style rise revealing the landscape*.
- Nunca pedir personas, texto ni logos dentro del video generado.
- Duraciones que admite el formulario del CRM: reels 5 o 10 s; UGC 8 o 15 s.

## 3. UGC (persona a cámara)
- **~2,2 palabras por segundo como máximo**: 8 s ≈ 17 palabras; 15 s ≈ 33.
- Primera frase = hook. Luego qué está en juego, 1 a 3 ideas y un solo CTA.
- Lenguaje hablado ecuatoriano, frases cortas, sin leer datos de corrido.
- Costos de referencia en créditos: UGC 8 s = 40; UGC 15 s = 75 (medidos).

## 4. Historia (9:16)
- Una idea por historia. Título ≤ 6 palabras; dato o precio visible si la ficha lo tiene.
- Texto fuera de los 270 px de arriba y de abajo (la fuente del motor dice 250; manda 270, 14 % de 1920).
- Pensada para generar mensajes: el pie invita a responder («Responde CASA y te envío la ficha»).
- Tono más cercano e inmediato que el feed («Nuevo», «Hoy», «Última disponible» solo si es verdad según la ficha).

## 5. Carrusel (5–8 láminas)
Se mide en guardados y en cuántos llegan a la última lámina, no en likes. Una plantilla visual, una idea por lámina, texto grande y corto.
- L1 portada: hook ≤ 6 palabras + la mejor foto; funciona sola en el feed.
- L2 qué está en juego (precio, ubicación, oportunidad, tiempo).
- L3–L5 valor: una idea por lámina (espacios, acabados, ubicación y accesos, proceso, financiamiento).
- L(n−1) resumen: los datos clave de la ficha en una lámina que dé ganas de guardar; título natural («Todo en una lámina», «La ficha en corto»), nunca la palabra «captura».
- L(n) CTA único con WhatsApp.
- Cada lámina: título de 3–7 palabras + texto de ≤ 25 palabras.
- Estructuras: propiedad (recorrido con fotos reales), lista útil («N errores al comprar», un error por lámina, cumplir el número prometido), demo/proceso (resultado final primero e índice de pasos en L2), problema → prueba (solo datos reales).
- En el generador de piezas: una lámina por línea `titular | subtítulo`, numeradas «1/N», botón en la última.

## 6. Caption
- Línea 1 (≤ 125 caracteres): el hook o el dato clave; es lo único que se ve antes de «más».
- Cuerpo: 3–5 líneas cortas con saltos de línea; números en vez de adjetivos; datos solo de la fuente.
- Un solo CTA con verbo + beneficio concreto. En carruseles e historias el cierre visual es WhatsApp: el CTA del caption y el cierre de la pieza apuntan al mismo canal. Ejemplos: «Escríbenos al WhatsApp [número] y te enviamos la ficha completa»; en reel o post educativo sin cierre de WhatsApp: «Escríbeme CASA por mensaje directo y te envío la ficha». Nunca dos pedidos a la vez, nunca «Más info».
- Cierre con sector + ciudad para búsqueda local.
- Hashtags: 3–5 (uno de nicho, uno medio, uno amplio).
- Máximo 2 emojis en todo el caption.

## 7. Copy de landing de curso
- Titular de resultado (transformación, no tema); subtítulo de 1–2 frases; promesa concreta y verificable.
- «Para quién es» (4–5), «Aprenderás» (5–7 resultados concretos), «Incluye» (solo lo que el curso entrega), «Para quién NO es» con criterios claros (filtra a propósito).
- «Esperar te cuesta…» (pérdida) con datos reales; «Así funciona» en 3 pasos.
- 5 preguntas frecuentes: duración, lugar, requisitos, certificado, qué llevar. Garantía o reembolso solo si la empresa los tiene configurados.
- Texto del botón ≤ 4 palabras con verbo. Prueba suave de hasta 3 titulares alternativos.
- Cada afirmación numérica proviene de datos del curso; testimonios solo los cargados por la empresa.

## 8. Material formativo y de ebook
- Diapositivas: una idea; ≤ 5 puntos y ≤ 12 palabras por punto (se lee desde el fondo de la sala); 1 portada + 1 agenda; pausa de 15 min cada ~90 min; 2–3 diapositivas por hora (mín. 12, máx. 45); cierre con el siguiente paso, sin presionar; notas del orador de 2–4 frases.
- Tarjetas de la clase: una cada 10–15 min; se leen en 5 segundos; los minutos suman la duración total.
- Ebook: usar solo lo que dice el curso; sin cifras, precios ni promesas; los ejemplos hipotéticos se marcan; bienvenida y cierre; por capítulo idea clave, resumen, lista de verificación y reflexión.
- Curso gratis (imán): muestra *qué* se logra y *cuánto vale*, con el sistema funcionando en vivo; **no enseña el método** del taller de pago.

## 9. Mensajes de WhatsApp
- Mensaje precargado del botón: corto, pide la acción («Hola, quiero la ficha de [nombre]», «inscripción al curso»), con referencia del origen para atribuir.
- Nunca se escribe primero; recordatorios solo dentro de la ventana de 24 h.

## Origen
`postpro-321/motor/skills/hooks.md`, `reel.md`, `historia.md`, `carrusel.md`, `caption.md`; `crm-321/docs/08-mapa-del-sistema/03-marketing-ia-motor-publicidad.md` §2.2, §5.2; `crm-321/docs/04-registro-cambios.md` (UGC: 2,2 palabras/s); `crm-321/src/lib/academy/ia.ts` (copy de landing, diapositivas, tarjetas, ebook); `crm-321/docs/14-diseno-landings.md`, `17-banco-cursos-gratis.md`, `18-ebooks.md`, `15-whatsapp-academy.md`; `crm-321/docs/16-diseno-vectorial.md` (carrusel).
