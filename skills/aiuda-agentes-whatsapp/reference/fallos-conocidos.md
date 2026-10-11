# Fallos reales de agentes (no reintroducir)

Cada línea nació de una conversación o prueba real. Úsalos como casos de prueba al cambiar un prompt o un modelo.
Fuente principal: `/home/user/bcujano/laundry-vip/docs/DECISIONES.md` §2 y `docs/AGENTE.md` §5b–§6.

## Invención
- **Orden inventada** («✅ Orden registrada», ID y monto falsos) sin llamar a la tool → guardia de `Extraer JSON`.
- **Precio y plazo inventados** por `gemini-3.1-flash-lite` («$31,50», «48 horas», declaró `tool_consultada: cotizar_prendas`)
  → el modelo vuelve a OpenAI principal; la guardia reemplaza montos/plazos que no salieron de una herramienta ese turno.
- **«No ofrecemos tinturado / no lavamos zapatos»** teniendo ambos en catálogo (2026-09-24): palabras de pregunta diluían
  la coincidencia, faltaban sinónimos y el modelo traducía «no encontré el nombre» como «no existe».
- **Prometió recogida «en todo Quito»** y fuera de zona (Carcelén Bajo, Llano Grande); explicaba «2,5 km a la redonda»
  → ahora verifica por dentro y solo dice sí o no.
- **Horario distinto al del local** (lunes–sábado 9:30–19:00 contra el real, sábado hasta las 17:00): horario y dirección salen de Configuración.
- **Cerró un pedido sin dirección** y con **nombre inventado** («Juan» para un contacto «Jp»); el nombre del perfil de
  WhatsApp no cuenta como dicho por el cliente.
- **Se contradijo con la dueña** (ella dijo $3,75, el agente $7,50): arrastró «terno» del mensaje anterior en vez de consultar.
- **Cotizó por prenda la ropa de diario** (7 camisetas a $17,50 vs ~$7 por libra).
- **Ofreció métodos (agua/seco/planchado) para ternos** sin consultar el catálogo.
- **Seguimiento con saludo equivocado** («buenos días» a las 5 pm): la hora la fija el código.
- **Preguntó «¿cuántos ternos?» a quien dijo «Tengo 3 ternos»**: el redactor de seguimientos lee la conversación.
- **Citó links, montos o cuentas fuera del catálogo** (Academy): ahora se escala a persona.
- **Afirmó haber ejecutado acciones** que no ocurrieron (gerente del CRM): `frenar()` reemplaza la respuesta.

## Conversación
- **Respondió dos veces seguidas a una ráfaga** y preguntó lo ya contestado → debounce + responder todo en un mensaje.
- **«¿Cuántas fundas?» confundió** a tres clientes → la tool `calcular_vehiculo` se quitó; recogida y entrega siempre en auto.
- **Quedó mudo con la dueña**: la conversación de prueba quedó con la etiqueta `humano` («Mal servicio»).
- **Respondió encima de una persona** (María Sol escribiendo a mano) → detección de remitente ≠ «Agente VIP» pone `humano`.
  El agente se habría callado solo al cambiar de usuario de Chatwoot: el filtro debe usar el nombre del usuario del agente.
- **Aviso de discrepancia**: si el cliente responde, el agente no explica ni discute montos; escala.

## Plataforma
- **27 nodos de n8n sin «continuar si falla»**: el MCP pierde `onError` → `verificar-errores.cjs` tras cada publicación.
- **Transcribir un prompt a mano al MCP se comió una tilde («propón») y metió un carácter cirílico** →
  `verificar-prompts.cjs`.
- **`whisper-1` con apagado programado** → prueba que falla si aparece en el workflow.
- **Cron cada 16,7 min** y **servidor zombi en el puerto 3000** (VIP) → `/api/health` reporta la fase compilada.
- **Expresiones `.item` en la memoria del nodo Agente v3.x** fallan al llamar herramientas → usar `.first()`.
- **Reimportar el JSON entero** cambia el id, apaga el acceso MCP y choca la ruta del webhook → solo `setNodeParameter`.
- **Secreto de 321 en el historial de git de VIP** → purgado con `git filter-repo`; prueba recorre todo lo rastreado.
- **La suite de VIP borró la conversación del dueño** (usaba su número real) → pruebas con operadores propios por corrida.
- **Webhooks de n8n sin autenticación** (`/cotizador-321` enviaba PDF a cualquier número) → cabecera `x-n8n-secret`.
- **Mensaje «This message is unavailable»** (Meta no entregó el contenido): decisión pendiente.

## Cómo probar sin tocar clientes reales
- VIP: `pnpm tsx scripts/simular-cliente.ts "mensaje"` (bandeja API propia, no sale a WhatsApp); `--leer`, `--mensaje`,
  `--limpiar`. Revisar `ai.agent.tool_calls.requested`: 0 con precio dado = inventó.
- Academy: `scripts/academy-pruebas/agente-diagnostico-chat.mts` (teléfono falso, se borra; ≈ $0,02), `agente-ebook.mts`.
- Auditoría barata de transcripciones reales: `pnpm chatwoot:revisar --desde AAAA-MM-DD` (solo lectura, solo su cuenta).
- Nunca disparar Pixel ni WhatsApp reales en pruebas.
