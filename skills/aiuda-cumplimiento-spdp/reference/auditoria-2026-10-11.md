# Estado de cada sistema (auditoría del 2026-10-11)

**Leyenda:** S = sí · P = parcial · N = no encontrado · NA = no aplica o aún no construido · **N\*** = existe una instrucción activa que contradice el control.

| Control | Artículo o norma relacionada | crm-321 | postpro-321 | aiuda-empresas | laundry-vip | creator | adsboom |
|---|---|---|---|---|---|---|---|
| 1 Aviso de privacidad y página de eliminación | 5.1 | P | N | P | P | N | N |
| 2 Consentimiento y baja de mensajes | LOPDP art. 8 | P | N | P | P | N | N |
| 3 Derechos de acceso, rectificación, eliminación y oposición | 4 | P | N | P | N | P | N |
| 4 Aviso de que es IA y aviso de grabación | 5.1 | P (solo si preguntan; voz N) | N\* | P | N\* | NA | NA |
| 5 Intervención humana en decisiones automatizadas | 4 inc. 2 | P | P | S/P | S/P | S | NA |
| 6 Registro y auditoría de la IA | 5.5, 7.1, 7.3 | P | P | P | P | S | N |
| 7 Datos enviados a proveedores de IA (minimización, transferencias) | 5.3 y resoluciones de transferencias | P | P | P | P | P | NA |
| 8 Retención y borrado | principio de conservación; 0030-R | N | N | N | N | N | N |
| 9 Seguridad | 5.3 y 7 | P | P | S/P | S | P | P |
| 10 Etiquetado de contenido generado por IA | no regulado por la 0009 | N | N | NA | NA | N | N |
| 11 Datos sensibles, menores, cédula y prospección | principios; 0041-R | P | N | P | P | N | N |
| 12 RAT, evaluación de impacto, delegado, contratos y subencargados | 5.2, 5.4, 6, 7.1; 0003-R, 0006-R, 0028-R | P | N | P | N | P (cláusula) | N |
| 13 Separación entre clientes | 5.3 | NA | NA | S | NA | P | P |
| 14 Brechas | LOPDP art. 43; 0040-R | N | N | N | N | N | N |

La columna de artículos es una **lectura nuestra** para ordenar el trabajo; confirmar con el abogado.

## Los 10 mayores riesgos, por gravedad
1. **Llave de servicio de Supabase y secreto de webhook escritos en el repo de crm-321** (`scripts/migrate.py:13` y `n8n/seguimiento-321-v5.json`). Quien tenga el repo puede leer y borrar todos los datos. Rotar y limpiar el historial. Además, los documentos dicen que quedan políticas abiertas en dos archivos SQL; no se verificó contra la base.
2. **Agentes que ocultan que son IA.** En postpro-321 el flujo v1 y el bot legado, y en laundry-vip el prompt del agente dicen "nunca digas que eres IA". En crm-321 y aiuda-empresas la IA solo se declara si preguntan. El art. 5.1 pide informar el carácter automatizado.
3. **Sin base legal ni consentimiento registrado al captar leads**, salvo en Academy. Hay campañas, seguimientos y reactivaciones automáticas. En aiuda-empresas el píxel de Meta se carga sin consentimiento.
4. **No hay baja de mensajes implementada.** Existe como diseño o documento, y el campo `baja_solicitada` se escribe pero ningún envío lo lee. La reactivación de leads dormidos no filtra por baja.
5. **Derechos del titular sin flujo operativo.** aiuda-empresas: solo "ELIMINAR" por WhatsApp, a mano. laundry-vip: riesgo aceptado por escrito. crm-321: nada para el titular. creator: borrado lógico.
6. **Datos personales a OpenAI, Google, Anthropic, Retell y Twilio sin documentar transferencias ni contratos, y sin enmascarar.** Incluye `cedula_ruc` en la ruta de documentos de crm-321, historiales, notas, audio e imágenes de WhatsApp y audios de clientes.
7. **Llamadas de voz IA sin aviso de IA ni de grabación**, con grabación y transcripción almacenadas.
8. **Decisiones automatizadas con efecto sobre la persona y poca trazabilidad:** calificación de leads, descarte automático de contactos y supervisor IA que bloquea mensajes. No se guardan prompts ni salidas completas, ni hay vía de oposición. creator es el único con traza completa.
9. **Sin gobierno documental:** RAT, evaluación de impacto, delegado, contratos de encargo, lista de subencargados y plan de brechas. Solo hay una cláusula contractual en creator y la política de Academy.
10. **Sin retención ni purga**, y contenido sintético sin etiquetar (imágenes, video y un avatar generado con IA).

## Hallazgos que cambian la forma de vender
- **La competencia revisada casi no declara cumplimiento:** de 11 competidores leídos, ninguno mostró aviso, consentimiento, derechos y registro de actividades de forma completa. Cumplir de verdad y poder demostrarlo es una ventaja comercial, no solo una carga.
- **laundry-vip y postpro-321 contradicen la norma por instrucción explícita**, no por omisión: corregirlo es de las primeras tareas.
