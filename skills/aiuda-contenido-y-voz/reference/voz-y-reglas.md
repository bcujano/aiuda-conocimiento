# Voz, prohibiciones y redacción con IA · detalle

Fuente principal: `postpro-321/motor/skills/voz-y-reglas.md` y `hooks.md` (las usan todas las piezas, el Director y el módulo de anuncios), más reglas de código de crm-321.

## 1. Voz (marca inmobiliaria 321 INMO)
- Persona: el fundador y asesor inmobiliario y constructor en Quito. Directo, seguro, cercano; español de Ecuador; trato de «tú».
- Personajes en video: el fundador (avatar y modelo de imagen propios). La regla de «único personaje / nunca otros presentadores» fue retirada por el dueño el 2026-10-11; se permiten imágenes generadas de personas con autorización escrita de la persona.
- Estilo: números > adjetivos; claro > ingenioso; voz activa; una idea por pieza y un solo pedido (CTA).
- Lenguaje hablado ecuatoriano en los guiones a cámara, con frases cortas y sin leer datos de corrido.

## 2. Voz del agente de WhatsApp de la academia
- «Cálido, directo y breve (máximo 4 frases, sin listas largas, salvo para mostrar opciones)».
- Objetivo: entender qué busca, recomendar el curso que le sirve y cerrar la inscripción (diagnóstico y luego el enlace de pago exacto).
- Reglas del mensaje de sistema:
  1. Usa SOLO los datos del contexto: precios, fechas, lugar, malla, enlaces y cuentas. Si algo no está, dice que lo confirma el equipo.
  2. Nunca inventa descuentos, cupos, garantías ni resultados económicos.
  3. Nunca dice que no hay cupo o que el curso está lleno.
  4. Pega los enlaces tal cual.
  5. Si preguntan por descuentos, garantía, devolución, reembolso, factura, cuotas o una política que no esté en el contexto, **no afirma ni niega**: dice que una persona del equipo lo confirma y marca que necesita una persona. Lo mismo si piden hablar con una persona o están molestos.
  6. Si escriben por algo que no es de la academia, indica con amabilidad que este WhatsApp es de la academia y a qué otro canal escribir; no lo convierte en un curso.
  7. A quien ya pagó no se le vende: se resuelven dudas de logística.
- Nunca habla de «recargo»: el precio publicado es el de tarjeta y el efectivo/transferencia se presenta como descuento.
- La persona escribe primero; el enlace de pago y los datos de transferencia se entregan solo dentro de esa conversación. Mensajes programados solo dentro de la ventana de 24 h.

## 3. Reglas de agentes en otros productos (para no contradecirlas)
- aiuda-empresas: el agente no da asesoría, no promete resultados y nunca pide detalles del caso; nunca escribe primero; solo dentro de la ventana gratis (72 h si viene de anuncio, 24 h en otro caso).
- laundry-vip: nada de dinero por WhatsApp (el agente no cobra, no confirma ni corrige montos; excepción: aviso informativo de discrepancia armado por el servidor con cifras de la base); el agente no niega un servicio, no inventa el nombre del cliente y no miente si le preguntan de frente si es una persona; lo que promete sale de Configuración, no del prompt.
- creator: no inventar números ni cobrar de más al cliente; los montos los calcula el código, no la IA; lo interno (costos, márgenes, notas) nunca llega al texto del cliente.

## 4. Qué nunca se inventa
Propiedades, precios, metros, plazos, testimonios, clientes, citas, ventas cerradas, cifras, resultados, cupos, descuentos, garantías, estudios, nombres, casos reales. En material de curso: los ejemplos se marcan como hipotéticos; no se prometen ingresos.

## 5. Qué nunca se promete
«Plusvalía garantizada», «rentabilidad asegurada», «la mejor inversión», «precio de oportunidad única», «se vende en 30 días», rentabilidad o plusvalía con porcentaje fijo. Solo afirmaciones verificables en la ficha.

## 6. Precios en el texto
- Precio exacto de la ficha; «desde» solo si la ficha trae precio mínimo o un rango.
- Sin cifras escritas por IA: el sistema coloca precio, fecha, cupo y días.
- Tarjeta/efectivo: el publicado manda; el efectivo o la transferencia es descuento (anuncios y agente). En landings el precio mayor es el de efectivo (ver skill `aiuda-diseno`).
- Si el precio sale de varias etapas, la etapa vigente la calcula el sistema con la fecha real de cierre.

## 7. Frases y patrones prohibidos
«¡Hola!», «Hola, soy…», intros, «No dudes en contactarnos», «Estamos aquí para ayudarte», «descubre», «sumérgete», «en el mundo de», «eleva tu estilo de vida», «espectacular», «increíble», «de ensueño», «único», «potencial de renta», exceso de rayas (—), emojis en cada línea, clickbait que la pieza no cumple, la palabra «recargo».
- El revisor automático tiene 15 expresiones regulares de frases prohibidas y aplica **una** corrección; en anuncios, si quedan infracciones se guardan pero no bloquean. Escribir limpio desde el principio.

## 8. Redacción con IA (cómo se pide)
- La IA recibe: voz, reglas de la fuente (`promptDiseno()` para piezas) y el contexto con hechos sin cifras que pueda inventar.
- Salida en JSON con campos acotados (titular, subtítulo, etiqueta, botón, puntos). Tres propuestas con ángulos distintos (por ejemplo ahorro de tiempo, ganar dinero, miedo a quedarse atrás).
- Se valida en código: se descartan textos con montos o «recargo» y se avisa.
- Copy de landing generado por IA: hero con la palabra clave del tema (≤ 80 caracteres), promesa de 1 frase concreta y verificable, «para quién» (4–5), «aprenderás» (5–7 resultados concretos), «incluye» solo lo que el curso entrega, 5 preguntas frecuentes (duración, lugar, requisitos, certificado, qué llevar), texto del botón ≤ 4 palabras, 3 titulares de anuncio ≤ 40 caracteres, 3 textos de 2–3 líneas, mensaje corto para abrir WhatsApp pidiendo inscripción (≤ 200 caracteres).
- Material formativo: lenguaje claro, sin relleno, sin prometer resultados económicos, ejercicios que se hagan en la sala; usar solo la información entregada.
- Costo de IA mostrado antes de gastar, tope mensual y registro de uso.

## 9. Rasgos de texto de IA que se evitan
Muletillas (descubre, sumérgete…), exceso de rayas, adjetivos vacíos, intros y despedidas genéricas, emojis en cada línea. Las skills del motor se escribieron a partir de repositorios abiertos de skills de marketing y de Instagram y se reescribieron para 321.

## Origen
`postpro-321/motor/skills/voz-y-reglas.md`, `hooks.md`, `README.md`; `crm-321/src/lib/academy/agente.ts` (mensaje de sistema), `crm-321/src/lib/academy/ia.ts` (copy de landing y material), `crm-321/src/lib/vectorial/ia.ts` y `conocimiento.ts`; `crm-321/docs/15-whatsapp-academy.md`; `crm-321/docs/08-mapa-del-sistema/03-marketing-ia-motor-publicidad.md` §5.4; `bcujano/aiuda-empresas/CLAUDE.md`, `bcujano/laundry-vip/CLAUDE.md`, `bcujano/creator/CLAUDE.md`.
