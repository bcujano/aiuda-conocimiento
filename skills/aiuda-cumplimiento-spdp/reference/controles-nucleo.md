# Controles comunes en el núcleo

| # | Control común | Qué resuelve | Norma relacionada |
|---|---|---|---|
| 1 | **Registro de consentimiento y base legal** (persona, finalidad, canal, texto exacto y versión, fecha, evidencia), exigido antes del primer envío saliente | Lo reutilizan CRM, agente, landings y prospección | LOPDP art. 8; 5.1 |
| 2 | **Servicio de baja y lista de exclusión**: reconoce STOP, BAJA o "no me escriban" y bloquea todo envío automático. Todos los emisores consultan la misma lista | Cubre `baja_solicitada`, seguimientos, reactivaciones y recordatorios | Art. 4 (oposición) |
| 3 | **Módulo de derechos del titular**: portal público y por WhatsApp, identidad verificada, cola con plazo, exportar, rectificar, suprimir o anonimizar en cascada (leads, actividad, conversaciones, hojas, respaldos) | Una solicitud se completa de punta a punta y queda registrada | Art. 4 |
| 4 | **Aviso de IA obligatorio en el primer mensaje**, en WhatsApp y en voz, impuesto por código y no por el prompt; aviso de grabación y opción de no ser grabado; eliminar de los prompts toda instrucción de ocultar la IA | Cumple la transparencia y corrige laundry-vip, postpro-321 y el flujo de crm-321 | 5.1 |
| 5 | **Registro de decisiones y mensajes de IA**: modelo y versión, versión del prompt, entrada enmascarada, salida, decisión y quién la revisó; botón de revisar o anular y de pausar el bot | Trazabilidad y auditoría de calificación, descarte y cotización | 5.5, 7.1, 7.3 |
| 6 | **Capa de enmascarado de datos personales** antes de enviar a proveedores de IA: cédula, teléfono, correo y direcciones; lista de campos permitidos por caso de uso | Minimización y menos exposición en transferencias | 5.3 y transferencias |
| 7 | **Inventario de proveedores y transferencias**: país, datos que reciben, base de la transferencia y estado del contrato | De aquí salen la política pública y el RAT | 5.4; 0024-R y 0004-R |
| 8 | **Política y aviso públicos por cliente**, con responsable, contacto, finalidades, proveedores y plazos; banner de consentimiento para el píxel | Reemplaza las páginas sueltas | 5.1 |
| 9 | **Retención y purga automática** por tabla y cliente, con anonimización (grabaciones, transcripciones, almacenamiento y respaldos) | Cumple el principio de conservación | Principio de conservación; 0030-R |
| 10 | **Etiquetado de contenido generado** (metadato y leyenda visible) antes de publicar. **No lo exige la norma 0009**: es una buena práctica y diferencia | Marca imágenes, videos, voz y avatares sintéticos | No regulado por la 0009 |
| 11 | **Seguridad base compartida**: gestor de secretos y rotación, límite de uso en webhooks, seguridad por fila con pruebas de aislamiento, auditoría de accesos del equipo | Cierra el riesgo número 1 y protege a todos los clientes | 5.3 y 7 |
| 12 | **Paquete de gobierno:** plantilla de contrato de encargo (la cláusula de creator como punto de partida), RAT y evaluación de impacto generados desde los inventarios, designación de delegado y plan de brechas con plantilla de notificación | Lo que pide la autoridad al auditar | 5.2, 5.4, 6, 7.1; 0003-R, 0006-R, 0028-R, 0040-R |

**Cómo se automatiza con IA (propuesta):** la IA puede leer el código y llenar los inventarios (controles 6 y 7), redactar los borradores de políticas, avisos, contratos y evaluaciones (8 y 12), generar las pruebas de aislamiento y de baja (2 y 11) y ayudar a revisar una muestra de decisiones (5). En todos, una persona revisa y un abogado aprueba lo legal.

**Cómo se vende:** un paquete "Cumplimiento SPDP incluido" con evidencia que el cliente puede mostrar a la autoridad. Es una hipótesis comercial a validar con clientes.
