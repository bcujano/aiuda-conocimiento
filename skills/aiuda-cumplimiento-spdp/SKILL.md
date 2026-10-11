---
name: aiuda-cumplimiento-spdp
description: Reglas de protección de datos personales e IA de Ecuador (LOPDP y norma SPDP-SPD-2026-0009-R) para cualquier función de Aiuda. Usar cuando se construya o cambie algo que trate datos personales, use IA, envíe mensajes, grabe llamadas, guarde conversaciones, genere contenido o integre un proveedor externo.
---

# Cumplimiento SPDP-SPD-2026-0009-R y LOPDP

Revisado: 2026-10-11 · Responsable: dueño de Aiuda · Fuente de verdad: este repo (los demás repos reciben una copia).
**No es asesoría legal.** Un abogado de protección de datos valida contratos, avisos y la interpretación final.

## Qué exige la norma de IA (texto leído, 10 artículos)
Alcanza a quien desarrolle, despliegue o provea sistemas de IA que traten datos personales de ecuatorianos, sin importar dónde estén los servidores o los modelos. No tiene plazo de adecuación. Detalle: `reference/norma-0009.md`.
- **Art. 4:** derecho a no ser objeto de decisiones basadas solo o en parte en valoraciones automatizadas, a la información y a la oposición.
- **Art. 5.1:** informar de forma clara el tratamiento con IA y su **carácter automatizado**.
- **Arts. 5.2 y 6:** gestión de riesgos y **evaluación de impacto previa** al desarrollo.
- **Arts. 5.3 y 7:** seguridad permanente y continua.
- **Arts. 5.4 y 7.1:** el tratamiento con IA y las decisiones automatizadas entran en el registro de actividades (RAT), disponible para la SPDP.
- **Arts. 5.5 y 7.3:** auditoría según el nivel de riesgo.

La norma **no regula** el etiquetado de contenido generado, las transferencias, las brechas ni el delegado: eso viene de la LOPDP y de otras resoluciones de la SPDP (lista en la referencia). No inventes requisitos que no están.

## Antes de construir cualquier función, responde
1. ¿Qué datos personales entran, para qué finalidad y con qué base legal?
2. ¿Interviene una IA? ¿Decide algo que afecte a una persona? ¿Quién lo revisa?
3. ¿Se informa desde el primer mensaje que es un asistente virtual automático y que puede pedir una persona?
4. ¿Cómo se da de baja el titular y cómo ejerce acceso, rectificación, eliminación y oposición?
5. ¿Qué datos se envían a qué proveedor, en qué país, y están enmascarados lo que no hace falta?
6. ¿Cuánto tiempo se guardan y cómo se borran o anonimizan?
7. ¿Se registra cada respuesta o decisión de IA (modelo, versión del prompt, entrada enmascarada, salida, revisor)?
8. ¿Existe la evaluación de impacto de este módulo? (el art. 6 la pide **antes** de desarrollar)
9. ¿Está en el RAT?

## Reglas duras
- **Prohibido** ordenar a un agente que niegue o se haga pasar por persona («no eres un bot», «nunca digas qué eres»). El primer mensaje lo presenta como asistente virtual automático y ofrece pasar con una persona; no hace falta decir «IA» o «robot» (decisión del dueño, 2026-10-11, apoyada en que el art. 5.1 no fija fórmula). Si la persona pregunta de frente, se responde con verdad.
- Voz automatizada: avisar que es un asistente virtual automático y que la llamada se graba; ofrecer no ser grabado.
- Ningún envío automático a quien pidió la baja (STOP, BAJA, «no me escriban»): todos los emisores consultan la misma lista de exclusión.
- No enviar cédula, RUC, teléfono ni correo a un proveedor de IA si no hace falta; enmascarar antes de enviar.
- No guardar conversaciones, audios ni grabaciones sin plazo de retención.
- No cargar píxeles de seguimiento sin consentimiento.
- Todo módulo de IA nuevo lleva su evaluación de impacto antes de construirse.

## Doce controles que se construyen una vez en el núcleo
Ver `reference/controles-nucleo.md`. Cada módulo los reutiliza en vez de repetirlos.

## Estado actual de los repos
Ver `reference/auditoria-2026-10-11.md` (lo que falta en cada sistema y los 10 mayores riesgos).
