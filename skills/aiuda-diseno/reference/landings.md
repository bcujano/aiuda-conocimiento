# Landings y páginas de venta · detalle

Fuente principal: `crm-321/docs/14-diseno-landings.md` (investigación del 2026-10-04 y decisiones posteriores). Las cifras de blogs de proveedores son orientativas: lo que importa es el patrón, no el número.

## 1. Decisiones de Byron (mandan sobre la investigación)
- Ningún texto sobre la foto del hero: ni degradado con nombre, ni «Speaker», ni leyenda.
- Datos primordiales (fecha, duración) en piezas flotantes jerárquicas cerca del centro de la foto, no pegadas a los bordes.
- No poner el recargo del 6 % en los botones; se explica en la pantalla de pago.
- Estilo «Kraft» sin copiar «el flyer». Sin nombres de empresa en el código.
- Jerarquía de precio (2026-10-09): el precio **más grande** es el de efectivo o transferencia; el de tarjeta va más pequeño con el ahorro («Ahorras $X pagando en efectivo o transferencia · con tarjeta $Y»). Aplica a los 10 estilos, al tachado, a la escalera de etapas y a botones con precio.
- «Todo premium»: cada pantalla se pule de a una, con captura (HANDOFF).

## 2. Patrones que se repiten en la investigación
1. Hero con 3 respuestas en 3 s (¿es para mí?, ¿qué gano?, ¿confío?): titular 6–12 palabras de **transformación**, subtítulo 15–25 palabras, un CTA, foto/video.
2. Titular = resultado («Aprende a comunicarte con la IA para vender más» antes que «Taller de prompting»).
3. Rostro humano real > stock. El facilitador real es el mejor activo; nunca ilustrarlo.
4. Texto sobre imagen = riesgo de legibilidad (contraste 4.5:1). Solución: foto limpia + texto fuera de la foto.
5. CTA: botón ≥ 48 px, verbo de acción, color de máximo contraste, repetido (hero → tras prueba social → barra fija móvil).
6. CTA fijo en móvil: debe aparecer cuando el hero sale de pantalla.
7. Urgencia solo si es real; contador con el cierre verdadero de cada etapa de precio. Los contadores falsos destruyen confianza.
8. Escalera de precios visible (lanzamiento → preventa → normal), vigente destacada, vencidas tachadas.
9. Orden de secciones: hero → datos clave → resultados → para quién es → temario → facilitador (credenciales) → prueba social/galería → precio y bono/garantía → FAQ → cierre con CTA.
10. Foto del hero recortada para vertical (4:5); una panorámica se vuelve una franja ilegible en móvil.
11. Peso: imágenes < 1 MB (WebP); hero `fetchPriority="high"`; resto `loading="lazy"`.

## 3. Patrones medidos en tres páginas reales (2026-10-04)
- Foto del instructor **sin texto encima**; el texto va al lado o debajo.
- **Panel de compra** con precio, urgencia/garantía y un único CTA grande; en móvil se vuelve **barra fija** con precio + fecha límite + botón.
- Prueba social **numérica** cerca del CTA (inscritos, valoración, reseñas) y avatares.
- Credencial del instructor en **una línea** junto a su nombre; la bio larga va en su sección.
- Muchos testimonios, pero **después** del temario; FAQ al final con garantía y reembolso explícitos.
- Un solo color fuerte para el CTA; el resto, neutro.
- Barra fija inferior permanente con precio + chip de urgencia real + fechas + botón: el equivalente de «datos primordiales».

## 4. Embudo de clase gratis (caso de un creador con audiencia grande)
Patrones replicables (la estructura, no el resultado; las cifras del caso son afirmaciones suyas sin verificar):
1. Clase gratis en vivo (imán) → grupo de WhatsApp → taller de pago.
2. Formulario corto en el hero (nombre + correo/WhatsApp); el diagnóstico va **después**.
3. «Para quién es / para quién NO es» explícito, antes del formulario (filtra y ahorra gasto de anuncios).
4. Sección «esperar te cuesta…» (pérdida) + cuenta regresiva real.
5. «Así funciona» en 3 pasos y CTA repetido ~5 veces.
6. Foto del facilitador recortada, señalando a cámara, sin texto encima de la cara.
7. Enlace en la bio con tarjetas jerarquizadas (clase gratis, regalos por WhatsApp, taller).

## 5. Jerarquía visual (regla de trabajo)
- Una sola cosa grande por pantalla (el titular), una sola de color (el CTA).
- Píldoras flotantes: **máximo 2**. Principal = fecha (acento, mayor); secundaria = «9 h · 3 sesiones» (cristal, pequeña). Solape ~15 % sobre la foto, sin tapar la cara, animación ≥ 6 s con `prefers-reduced-motion`. En móvil, debajo de la foto.
- Escala de espacio: 4/8/12/16/24/32/48/64 px. Márgenes laterales móviles 16–20 px. Nada solapado con texto.
- Un acento; sin degradados agresivos, sin emojis de viñeta, sin orbes de IA.
- No repetir información: lo que dice una píldora no se repite en la franja de datos.

## 6. Los 10 estilos (cada uno es otro archivo, otra estructura y otra experiencia)
Código: `src/components/academy/landing/<Estilo>.tsx`; comunes en `landing/comun.tsx`; carga por estilo con `next/dynamic`; las fuentes de cada diseño no se precargan.

| Estilo | Concepto | Tipografía | Rasgo propio |
|---|---|---|---|
| Alta conversión | Embudo de clase gratis | Anton + Inter | Formulario en hero, cinta de urgencia, contador grande, «¿Te pasa esto?», 3 pasos, sí/no, «esperar te cuesta», WhatsApp flotante, CTA ×5 |
| Lujo | Clase magistral | Cormorant Garamond | Foto a sangre + panel negro de compra, filetes dorados, numerales romanos |
| Corporativo | Propuesta ejecutiva | IBM Plex Sans | Anclas, ficha técnica en hero, programa en tabla, FAQ a 2 columnas |
| Aurora | Lanzamiento tecnológico | Space Grotesk | Navegación flotante, hero centrado con titular en degradado, bento, ruta con nodos |
| Vibrante | Pop de redes | Bricolage Grotesque | Bordes gruesos, sombra dura, collage polaroid, stickers |
| Kraft | Cuaderno de taller | Anton + Caveat + Courier Prime | Papel con textura, cinta, máquina de escribir, notas adhesivas, precio como etiqueta |
| Tecnológico | Consola / IDE | JetBrains Mono | Hero como terminal, logros como pruebas que pasan, programa como árbol |
| Editorial | Revista impresa | Newsreader + Inter | Cabecera con edición, letra capital, columnas, preguntas como entrevista |
| Minimalista | Diseño suizo | Inter | Retícula de 12 columnas, secciones numeradas, cifras enormes, un acento |
| Sereno | Lectura tranquila | Fraunces | Una columna de 680 px, foto como lámina, hoja SVG como separador |

Reglas que se mantienen en los 10: ninguna letra sobre la foto; textos y números salen de los datos del curso (sin frases del tema escritas en el código); botones ≥ 48 px; barra fija con la paleta del diseño. Ver un estilo sobre un curso publicado: solo en el servidor local seguro (`?estilo=<id>`). Capturas con Playwright (el panel integrado a veces no pinta).

## 7. Fotos
Cada sección usa su foto (portada, facilitador, cierre, galería). Lo vacío toma otra foto de la biblioteca del facilitador. No repetir imagen en la misma página.

## 8. SVG en landings
- Sí: íconos, divisores, patrones de fondo, diagrama del temario (ruta de aprendizaje), sellos («certificado», «cupo limitado»). Pesan 1–5 KB, respetan el acento.
- No: sustituir fotos de personas.

## 9. Prueba suave de titulares
Hasta 3 alternativas por curso (`landing.hero_titulos`). La persona ve siempre la misma (cookie 30 días), elección al azar la primera vez, se registra en la Actividad al inscribirse y se manda `titular_variante` en ViewContent/Lead. Sin IA. No concluye con pocas inscripciones: hacen falta ~100–200.

## 10. Seguimiento (Pixel)
PageView/ViewContent al cargar; Lead, LeadCalificado, Contact, InitiateCheckout y Purchase con `event_id` compartido.

## 11. Lista de verificación antes de entregar una landing
- [ ] Titular de resultado; un CTA principal; hero sin texto sobre la foto.
- [ ] ≤ 2 píldoras flotantes, jerárquicas, sin tapar la cara; móvil sin desbordes.
- [ ] Contraste ≥ 4.5:1 en todo texto; botones ≥ 48 px.
- [ ] Contador con fecha real; precio vigente destacado; recargo explicado en el pago, no en el botón.
- [ ] Cada sección con su foto; imágenes < 1 MB.
- [ ] Probado a 375 px y 1440 px mirando la captura.
- [ ] Pixel con `event_id` compartido.
- [ ] Casilla de consentimiento antes de enviar datos (ver skill `aiuda-contenido-y-voz`, referencia legal).

## 12. Límites y cuidados
- Vista previa `?vp=` solo en cursos NO publicados: en uno publicado crea personas reales. Nunca correr el script de prueba de filtro contra producción (reglas I y J de `crm-321/CLAUDE.md`).
- Las plantillas de embudo (webinar gratis → low-ticket → alto ticket) son hipótesis, no validadas para Academy.
- Los elementos de garantía y reembolso recomendados por la investigación solo se muestran si la empresa los tiene configurados; el agente de WhatsApp nunca inventa garantías (`crm-321/src/lib/academy/agente.ts`).

## Origen
`crm-321/docs/14-diseno-landings.md` (todas las secciones), `crm-321/docs/13-academy.md`, `crm-321/docs/HANDOFF.md` (línea «todo premium»), `crm-321/CLAUDE.md` (reglas I y J), `crm-321/src/components/academy/landing/comun.tsx`, `crm-321/src/components/academy/LandingCurso.tsx`, `crm-321/src/lib/academy/agente.ts`.
