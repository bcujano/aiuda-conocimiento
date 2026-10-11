---
name: aiuda-contenido-y-voz
description: Reglas de redacción y contenido de marketing de AIUDA y 321 Soluciones Inmobiliarias: voz de marca, qué nunca se inventa (testimonios, precios, «desde $», cifras), guiones de reels con límite de palabras por segundo, anuncios Meta, ángulos de venta, captions, carruseles, historias y textos legales. Úsala al escribir copy, guiones, anuncios o avisos.
---

# AIUDA · Contenido y voz

Orden de precedencia cuando dos fuentes chocan: (1) decisión de Byron con fecha, la más reciente primero; (2) reglas escritas en código que se ejecutan (revisor de frases, `promptDiseno()`, validadores); (3) skills del motor de contenido; (4) planes o ejemplos viejos. Choques conocidos al final.

Detalle en `reference/`:
- `reference/voz-y-reglas.md` · voz, prohibiciones, lo que nunca se inventa, redacción con IA, agentes de WhatsApp.
- `reference/anuncios-meta.md` · ángulos, copy, hooks de video, pruebas, métricas, segmentación y notas técnicas de Meta.
- `reference/guiones-y-formatos.md` · reel, UGC, historia, carrusel, caption, hooks, copy de landing, material de cursos y ebooks.
- `reference/legal-y-datos.md` · opinión de valor, descargo, publicidad engañosa, protección de datos, WhatsApp.

## Cuándo usar cada referencia
| Tarea | Lee |
|---|---|
| Cualquier texto de marca, post, respuesta de agente | `voz-y-reglas.md` |
| Campaña o anuncio de Meta, segmentación, métricas | `anuncios-meta.md` |
| Guion de reel/UGC, historia, carrusel, caption, titular, landing | `guiones-y-formatos.md` |
| Informe de valor de un inmueble, consentimiento, baja, política | `legal-y-datos.md` |
| Aspecto visual de la pieza | skill `aiuda-diseno` |

## Reglas que valen para todo texto
1. **Los datos salen solo de la fuente** (ficha del CRM, curso, catálogo). Si falta un dato, se omite; nunca se inventa ni se redondea hacia arriba.
2. **Nunca se inventa:** propiedades, precios, metros, plazos, testimonios, clientes, citas, ventas cerradas, cupos, descuentos, garantías, estudios, nombres, casos reales, cifras ni resultados. Los ejemplos hipotéticos se marcan como tales.
3. **Ningún número lo escribe un modelo de lenguaje.** Precios, fechas, cupos, días y porcentajes los pone el sistema desde la base. Si una IA devuelve montos (`$`, USD, %) o «recargo» en un texto de pieza, se descarta.
4. **Precio exacto de la ficha.** «Desde» solo si la ficha trae precio mínimo o un rango. Por defecto: sin «desde $» (el plan de contenido de octubre salió «sin testimonios ni desde $»).
5. **Testimonios:** solo los que la empresa cargó con nombre y texto real; la IA nunca los redacta. Prueba social numérica (inscritos, valoración) solo con el dato verificable.
6. **No prometer lo que nadie puede garantizar:** nada de «plusvalía garantizada», «rentabilidad asegurada», «la mejor inversión», «precio de oportunidad única», ni promesas de ingresos. Inversión o rentabilidad solo con datos de la ficha.
7. **Urgencia solo si es real** (cierre verdadero de la etapa de precio, «Última disponible» solo si la ficha lo dice). El agente de la academia nunca dice que no hay cupo ni que el curso está lleno.
8. **Un mensaje, un pedido (CTA)**, con verbo + beneficio concreto. Nunca dos pedidos a la vez (mensaje directo y enlace) ni «Más info».
9. **Números > adjetivos. Claro > ingenioso. Voz activa.** Hook que detiene el scroll pero no se cumple en la pieza = mal hook.
10. **Español con tildes y ñ**, tuteo, sin jerga («tu negocio», no «tu funnel»). Español de Ecuador en las piezas hechas para Ecuador.
11. **WhatsApp primero, nunca escribimos primero:** la persona abre la conversación; el CTA invita a escribir con mensaje precargado.
12. **Precio y tarjeta:** el efectivo o la transferencia se presenta como descuento o ahorro; nunca la palabra «recargo» ni el 6 % en un botón.

## Voz de marca (resumen)
- Marca inmobiliaria 321 INMO: la voz de su fundador y asesor en Quito; directo, seguro, cercano, trato de «tú», español de Ecuador. Es el personaje principal que aparece en video; otros presentadores o modelos generados se permiten solo con autorización escrita de la persona (2026-10-11).
- Academia (agente de WhatsApp): cálido, directo y breve (máx. 4 frases, sin listas largas salvo para mostrar opciones).
- Para otra empresa (producto replicable): la voz, el nombre y el personaje son **datos de configuración**, no código. Usar esta estructura (directo, números, sin relleno) y cambiar la persona.
- Prohibido: «¡Hola!», «Hola, soy…», intros, «No dudes en contactarnos», «Estamos aquí para ayudarte», adjetivos vacíos (espectacular, increíble, de ensueño, único), muletillas de IA (descubre, sumérgete, en el mundo de, eleva tu estilo de vida), exceso de rayas (—), emojis en cada línea, clickbait que la pieza no cumple.
- Máximo 2 emojis en todo un caption; sin emojis como viñetas en landings.

## Guiones y límites numéricos
- **Hook:** ≤ 10 palabras, con número, lugar o plazo; el texto en pantalla complementa lo que se dice, no lo repite.
- **UGC a cámara:** ~2,2 palabras por segundo como máximo → 8 s ≈ 17 palabras; 15 s ≈ 33. Primera frase = hook; luego qué está en juego, 1–3 ideas y un solo CTA; frases cortas, lenguaje hablado.
- **Reel:** movimiento desde el primer cuadro; ningún tramo > 4 s sin cambio visual; cartel de ≤ 6 palabras dentro de la zona segura; sin logo, intro ni saludo; cerrar con lo que prometió el hook.
- **Historia 9:16:** una idea; título ≤ 6 palabras; sin texto en el 14 % superior (270 px), el 35 % inferior (672 px) ni los lados (65 px).
- **Carrusel:** 5–8 láminas; portada con hook ≤ 6 palabras; título de lámina 3–7 palabras y texto ≤ 25 palabras; la última lámina es el CTA único.
- **Caption:** línea 1 ≤ 125 caracteres (hook o dato); cuerpo de 3–5 líneas cortas; 3–5 hashtags (nicho, medio, amplio); cierre con sector + ciudad para búsqueda local.
- **Anuncio Meta:** texto principal con lo importante en los primeros 125 caracteres; titular ≤ 40; descripción ≤ 25.
- **Pieza gráfica:** titular ≤ 9 palabras / 70 caracteres; etiqueta ≤ 3 palabras; botón ≤ 4 palabras.
- **Diapositivas de curso:** una idea; ≤ 5 puntos y ≤ 12 palabras por punto; 2–3 diapositivas por hora de curso.

## Ángulos de venta (un anuncio = un ángulo)
dolor · resultado · prueba (solo datos reales) · curiosidad · comparación · urgencia (solo si es real) · identidad («para el que…») · contrario.
- Inmobiliario: precio-ubicación, estilo de vida, inversión/rentabilidad (solo con datos de la ficha), objeción.
- Construcción modular: tiempo de entrega, precio frente a la obra tradicional, antes/después, el proceso.
- Cursos: transformación en vez de tema; pérdida de esperar («esperar te cuesta…»); «para quién es / para quién no es».
- Marco de copy: PAS (problema → agitar → solución), BAB (antes → después → puente), AIDA para propiedades.
- Probar 3–5 ángulos × 2 hooks, cambiando **una** variable; orden: concepto > hook > visual > cuerpo > CTA.

## Anuncios en Meta (resumen técnico de crm-321/CLAUDE.md, API v22.0)
- `advantage_audience=1` obligatorio → `age_min` máx. 25 y `age_max` fijo 65 (la segmentación por edad que proponga la IA se ignora).
- CTA de WhatsApp: `{ type: 'WHATSAPP_MESSAGE', value: { app_destination: 'WHATSAPP' } }` **sin** enlace.
- ABO exige `is_adset_budget_sharing_enabled=false` explícito. CBO exige `budget_rebalance_flag=true` y `daily_budget` en la campaña.
- Imágenes de Google Drive: convertir a URL directa. `slideshow_spec` no funciona → generar MP4 real con ffmpeg.
- Todo se crea **en pausa**; solo Byron activa. Presupuesto inicial $5–10 por día por conjunto, 3–5 anuncios por conjunto. Subir presupuesto ≤ 20 % cada 3–5 días.
- Dudas abiertas en las fuentes: si los anuncios inmobiliarios en Ecuador exigen la categoría especial de vivienda (`HOUSING`) está **sin verificar**; hoy se crean sin categoría especial.

## Textos legales (resumen; detalle en `legal-y-datos.md`)
- El entregable de valor se llama **«Opinión de Valor Referencial de Mercado»**; nunca avalúo, tasación, peritaje, valor oficial ni valor certificado. Siempre un **rango**, nunca una cifra única; vigencia de 90 días; aviso legal obligatorio copiado tal cual.
- Formularios: casilla de **autorización** explícita para usar los datos y contactar, con enlace a la política de privacidad. Sin autorización no se registra.
- Primer mensaje a un contacto: quién escribe, de dónde salió el dato, para qué y cómo darse de baja (responde BAJA). La baja es inmediata y bloquea todo marketing. Atender oposición, eliminación, acceso y rectificación en 15 días.
- Publicidad engañosa (precio, forma de pago, características) está prohibida y sancionada; no usar valor catastral como valor de mercado ni prometer plazos de venta.
- Agentes: ante preguntas de garantía, devolución, reembolso, factura, cuotas o políticas que no estén en el contexto, **no afirmar ni negar**: decir que una persona del equipo lo confirma y escalar.
- Los temas legales y tributarios de cursos se validan con el abogado antes de publicar. Esto es documentación, no asesoría legal.

## Choques entre fuentes (quién manda)
1. **«Desde $».** `voz-y-reglas.md` lo permite si la ficha trae precio mínimo o rango; el plan de octubre lo excluye y un plan viejo de reels (`ADSBOOM-REEL-PRO-PLAN.md`) lo usa en su ejemplo («Desde $150,000»). Manda la regla del motor (solo con dato en la ficha); el ejemplo del plan está obsoleto. Ese plan además usa «Descubre…» e «Inversión segura», prohibidos por el revisor.
2. **Texto sobre imagen en video.** El plan de reels superpone texto con ffmpeg; la regla de diseño prohíbe letras sobre foto en piezas estáticas. Para video rige `reel.md` (cartel ≤ 6 palabras en zona segura).
3. **Zona segura de historia: RESUELTO 2026-10-11.** 14 % arriba (270 px), 35 % abajo (672 px), 6 % lados (65 px); ver `aiuda-diseno`.
4. **Largo del titular:** 9 palabras (pieza), 6 (portada de carrusel), 10 (hook), 40 caracteres (campo de Meta), 80 caracteres (titular de hero de landing). Se aplica el límite del medio.
5. **Saludo:** el revisor prohíbe «Hola» en el texto de marca, pero el mensaje precargado de WhatsApp del anuncio («Hola, quiero la ficha de …») es la voz de la persona que escribe, no de la marca; se permite.
6. **Exclamaciones y mayúsculas:** la regla de pieza pide evitar signos de exclamación seguidos y frases en mayúsculas; el estilo «Alta conversión» pone el titular en mayúsculas tipográficas y el caso de referencia usa «¡QUIERO MI LUGAR GRATIS!». Se entiende que no se **redacta** en mayúsculas ni con exclamaciones dobles; la mayúscula visual la decide el estilo.

## Vacíos
- No hay texto legal de política de privacidad ni de términos y condiciones en los repos: la marca guarda solo una URL (vacía por defecto). Falta guía de protección de datos para la inmobiliaria (pendiente en las fuentes).
- No hay política escrita de garantía o reembolso: solo se muestra si la empresa la configura.
- La voz de marca existe solo para 321 INMO y la academia; no hay voz definida para aiuda-empresas, creator ni adsboom.

## Origen
- `crm-321/CLAUDE.md` (reglas A–J, notas Meta API v22.0); `crm-321/docs/14-diseno-landings.md`, `15-whatsapp-academy.md`, `17-banco-cursos-gratis.md`, `09-marco-legal-avaluos.md`, `04-registro-cambios.md` (plan de octubre), `ADSBOOM-REEL-PRO-PLAN.md`, `08-mapa-del-sistema/03-marketing-ia-motor-publicidad.md` (§2.2, §5.3–5.4, §6, §8).
- `crm-321/src/lib/vectorial/conocimiento.ts`, `ia.ts`; `crm-321/src/lib/academy/ia.ts`, `agente.ts`, `tipos.ts`; `crm-321/src/components/academy/LandingCurso.tsx`.
- `postpro-321/motor/skills/voz-y-reglas.md`, `hooks.md`, `caption.md`, `carrusel.md`, `reel.md`, `historia.md`, `anuncios-meta.md`, `segmentacion-meta.md`, `diseno-piezas.md`, `README.md`.
- `bcujano/aiuda-empresas/CLAUDE.md`, `bcujano/laundry-vip/CLAUDE.md`, `bcujano/creator/CLAUDE.md` (no inventar números, agente sin asesoría ni promesas).
