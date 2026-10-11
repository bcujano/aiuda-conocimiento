# Agentes por producto: qué hace cada uno hoy

Descripción de lo que está en el código/prompt (leído 2026-10-11). Lo que contradice el skill principal se marca
**[CAMBIA]** y apunta a la sección de `SKILL.md` que manda.

## 1. 321 INMO (crm-321) — «iAgente 321 INMO V2» (n8n, vía Chatwoot)
Archivo: `/home/user/crm-321/n8n/respaldos/iagente-v2-antes-E10-2026-09-28.json` (nodo «Agente Arqui 321»).
Producción: **no se toca** sin autorización citada y respaldo de versión.

- Rol: **IA SETTER**, no closer. Califica y agenda; no cierra ventas, no firma contratos, no entrega cotizaciones formales.
  Nunca menciona bancos, financiamiento, plazos de crédito ni tasas (321 no trabaja directamente con bancos).
- **5 datos obligatorios para agendar** (cero excepciones): nombre y apellido, servicio, presupuesto (rango o monto),
  ubicación del proyecto, cuándo piensa empezar. Si tras 2–3 turnos evade, cierre cordial + cotizador
  (`cotiza.321archlab.com`). No insiste más de 2 veces en presupuesto.
- Precios: solo del «CATÁLOGO VIGENTE» que llega al final del prompt (`Contexto CRM` → `/api/agente/contexto`) o de las
  herramientas de hojas (honorarios CAE, aranceles, insumos, maquinaria, inventario, portafolio). Un solo número o
  rango cerrado + «es referencial». Sin desglose de cálculo.
- Intención del anuncio: solo si el cliente llegó por un anuncio en las últimas 24 h; el último mensaje del cliente
  siempre manda sobre el anuncio; el precio del anuncio vale solo para ese producto; anuncio no confirmado → confirmar
  el precio antes de comprometerse. Sin anuncio: prohibido asumir producto o dar precio en el turno 1.
- Agenda: videollamada de 30 min **primero** (presencial solo después); siempre consulta «Consultar Calendario»,
  propone 2 horarios reales; «Agendar Cita» solo tras confirmación.
- Herramientas web: cotizador, calculadora ROI, catálogo web; **una por mensaje**; cotizador prohibido en los primeros
  3 turnos salvo excepciones.
- Galerías: envía fotos (casas container / local comercial) ante disparadores; no inventa detalles de la foto.
- Oficina: tiene oficina física; nunca decir «trabajamos solo virtualmente»; la dirección sale del prompt (envía pin).
- Tono: apertura natural y variada (lista de aperturas prohibidas), preguntas rotadas, ≤50 palabras (≤80 en
  comparativos/confirmación de agenda), anti-eco, sin muletillas, tono ecuatoriano espejado, una pregunta por mensaje,
  ≤1 emoji; no pregunta cuando el lead duda/agradece/confirma («Quedo atento…»).
- **[CAMBIA]** Identidad: «Soy la IA de 321 que atiende el primer contacto» solo si preguntan (Secciones 1 y 9 #9) →
  SKILL §1: lo dice en el primer mensaje.
- Escalamiento (Sección 12): escalar_humano en 6 casos; no escalar por «ok/gracias/voy a pensar».
- Señales: urgencia (caliente → acelera agenda), fricción («muy caro» → no insistir, cotizador), corporativo (más
  formal, escala rápido), inversión (argumenta por velocidad y ROI, no por precio), spam, confusión (no asumir:
  preguntar el tipo de proyecto).
- Reglas por tipo: cargotectura <60 m² precios cerrados no modificables; >60 m² personalizado; cargotectura de lujo
  desaconsejada («el container deja de ser ahorro»); edificios 4+ pisos sí se hacen (escala rápido); campamentos 50+ módulos.
- JSON estricto: `respuesta_lead`, `tool_consultada`, `imagenes`, `videos`, `ubicacion`, `escalar_humano`,
  `metadata{temperatura, pain_point, objeciones, next_action, quality_score, tipo_lead, datos_lead}`.
  «Si mencionas precios o productos y tool_consultada es null sin razón, es FALLO.»
- Flujo: Chatwoot Webhook → Filtro Chatwoot → **Filtro Humano** → WhatsApp Inicio → Debounce (30) → combinar textos →
  texto | audio (transcribir) | imagen (explicar con visión) → agente → **Supervisor Vivo** → **Texto Supervisado** →
  envío (texto limpio, imágenes, video, ubicación) → ¿necesita humano? → etiqueta + nota → log. Cita agendada →
  notifica a Byron (email y WhatsApp).
- Seguimientos: workflow «Seguimiento Automatico 321 V6.0» (cada 2 min) consulta el supervisor antes de enviar; pasos de
  secuencia con plantilla e imagen/video opcionales (`step_plantilla`, `step_media_url`); pendiente que fuera de 24 h
  envíe la plantilla del paso (HANDOFF §4.B.1).
- Agentes del CRM (barra «Pregúntale a tu gerente», Super Agente): `lib/agente/turno.ts`; 9 gerentes por
  departamento; herramientas por rol; `MAX_PASOS = 6`; modelos `gpt-4.1-mini` (gerentes) y `gpt-4.1` (super).
  Rangos estrictos (docs/07 §1): **la IA hace sola** primer mensaje a lead nuevo, seguimientos, fichas, agendar en horarios
  libres, mover etapas por señales claras, crear tareas, pausar anuncios con gasto anormal; **siempre escala a humano**
  descuentos, precios fuera de la ficha, promesas legales/contractuales, reclamos, marcar ganado/perdido con monto, gastos
  sobre el umbral (doble verificación), activar pauta o subir presupuesto >20 %.
- Notificaciones (`lib/notificar.ts`): nivel `info` → campana; `importante` → WhatsApp a dirección; `critica` → llamada
  (Retell+Twilio) con respaldo WhatsApp. Máx. 1 llamada/día del vigía.

## 2. AiUDA Academy (crm-321) — agente v2 + cerebro `/api/academy/agente`
Archivo: `/home/user/crm-321/src/lib/academy/agente.ts` (turnoAcademy, recibirAdjunto, enrutar, escalar).

- Número propio de Academy; el router de 321 solo deriva a Academy si el mensaje trae `ACA-`.
- Rol: entender qué busca, recomendar curso y cerrar inscripción: **diagnóstico por chat (obligatorio antes de pagar)**,
  una pregunta por mensaje, el resultado lo calcula `guardarDiagnostico`; el link de pago/precio lo escribe el sistema.
- REGLAS del prompt: (1) usar solo datos del contexto; (2) nunca inventar descuentos, cupos, garantías ni resultados
  económicos; (3) nunca decir que no hay cupo; (4) pegar links tal cual; (5) descuentos, garantía, devolución, reembolso,
  factura, cuotas o política no escrita → no afirmar ni negar, `necesita_humano`; igual si pide una persona o está molesta;
  (6) temas ajenos (construir/comprar casa) → derivar a 321 Soluciones Inmobiliarias.
- Precios: precio publicado = tarjeta; efectivo/transferencia = descuento; nunca «recargo». Curso gratuito: nunca hablar
  de precios, tarjeta, transferencia, efectivo ni descuentos; el sistema confirma el lugar y entrega el acceso.
- Fuera de perfil (nivel de IA fuera del rango): sin link, mensaje fijo, «te avisaremos cuando abramos uno para tu nivel».
- Ebook gratis: se entrega con calidez una sola vez, solo con inscripción confirmada (inicio) o curso terminado (fin).
- Freno: link, monto o cuenta fuera del contexto → `escalar()` («Una persona del equipo te responde en breve»), nota en
  Actividad y aviso por WhatsApp al equipo.
- Tope: `gastoDelMes() >= TOPE_MENSUAL_USD` → escalar.
- Modelo `gpt-4.1-mini`, temperatura 0.3, respuesta JSON `{respuesta, necesita_humano, motivo, diagnostico}`; máx. 4 frases.
- Memoria: Actividad de Academy (`academy_actividades`, últimos 30 mensajes). Independiente del agente de 321.
- Adjuntos: audio → transcripción (n8n); imagen/archivo de quien tiene inscripción pendiente = posible comprobante →
  persona confirma con «Marcar pagada».
- **[CAMBIA]** Se presenta como «asistente de la academia» sin decir IA → SKILL §1.
- Voz Academy (apagada): `scripts/academy-voz/crear-agente.mjs`; tutea; no da precios/fechas de memoria; si pide persona,
  se molesta o no quiere más llamadas, agradece, anota «no llamar» y termina. **[CAMBIA]** declarar IA y grabación.

## 3. Laundry VIP (laundry-vip) — agente de clientes y agente de planta
Archivos: `/home/user/bcujano/laundry-vip/n8n/prompt-agente-laundry.md`, `n8n/prompt-operador-laundry.md`, `docs/AGENTE.md`.

- Clientes: 6 herramientas (`cotizar_prendas`, `obtener_proxima_ventana`, `verificar_cobertura`,
  `find_or_create_client`, `crear_pedido`, `consultar_estado_pedido`) + Calculator, todas por `POST /api/webhook` con
  `x-webhook-secret`. Los permisos los decide el servidor.
- Reglas de negocio no negociables: siempre un estimado en dólares; dos formas de cobrar (ropa de diario al peso, por
  libra; resto por prenda; cortinas por kilo); plazo por servicio (agua/cama 24 h; seco, cuero, plumas, tinturado,
  calzado, peluches, mochilas 72 h; alfombras 1 semana hábil; desde que llega a planta, sin domingos ni feriados);
  tarifa única de recogida/entrega aparte; **no existen «combos» ni «a la carta»** (palabras prohibidas); no hay descuentos
  ni negociación por este canal; no hablar de fundas/vehículo; sin dirección no hay pedido; nombre solo el que el cliente
  escribió; nunca mencionar kilómetros/radio; nunca prometer «en todo Quito»; confirmar pedido solo con «sí» explícito
  («ok», «gracias» o silencio no cuentan); fecha de recolección = la que devolvió la herramienta.
- Estilo: usted cálido, ≤60 palabras, una pregunta, saludo de la casa (`negocio.saludo`) + resto variado, lista negra de
  frases de call center; primer mensaje: saluda, atiende lo pedido y pregunta el nombre; el catálogo en imagen llega solo
  tras el primer mensaje (adjunto nativo, sin enlaces).
- Imágenes y voz: ver SKILL §9. Escalamiento: ver SKILL §6. Seguimientos: SKILL §3.
- **[CAMBIA]** «NUNCA DIGAS QUÉ ERES» → SKILL §1 (pero se conserva «lee el tono», «sin relleno»).
- Planta/dueña (`prompt-operador-laundry.md`): niveles operador/admin; nada de dinero por WhatsApp; admin se trata de
  usted y por su nombre, con datos del CRM + siguiente paso útil; nunca digas que algo quedó registrado sin `ok:true`;
  «Eso lo ve el administrador» si el operador pide algo de admin.
- Datos del negocio (nombre, dirección, horario, tarifa, plazo, cobertura) vienen del CRM en cada mensaje.

## 4. Aiuda Empresas (aiuda-empresas) — agente para Fagal Abogados (multicliente)
Archivo: `/home/user/bcujano/aiuda-empresas/n8n/agente-aiuda-empresas.sdk.ts`.

- Un workflow para todas las organizaciones; el negocio entra por `phone_number_id` → `/api/agente/contexto`.
  Gemini principal + OpenAI `gpt-4.1-mini` de respaldo (nodo con modelo de reserva), `maxIterations: 5`.
- Reglas del prompt (12): usted, ≤3 frases, una pregunta; **nunca asesoría legal, opinión del caso, resultados ni
  honorarios** (los define el abogado en la reunión); **nunca pide detalles del caso, documentos ni datos sensibles**;
  llamar solo por el nombre que la persona dijo; particulares, trabajadores contra su empleador o `no_para_quien` →
  se cierra con amabilidad y etapa `descartado` + motivo; no inventar datos del estudio; agenda solo con fechas de
  `ver_horarios` en ese mismo turno; nunca decir «agendada» sin `ok=true` de `agendar_cita`; si hay reunión vigente se
  reprograma; ante queja o confusión, disculpa una sola vez.
- Salida JSON `{respuesta, datos{nombre, empresa, cargo, colaboradores, ciudad, necesidad, urgencia, encaje, etapa,
  motivo_descarte}}`; solo etapas `calificado`/`descartado` las pone el agente; agendar va por herramienta.
- Si la respuesta no se puede leer: «Gracias por escribir. En un momento le ayudamos.»
- Flujo: ¿etiqueta `humano`? → ¿dentro del tope diario? → agente → CRM → Chatwoot. Persona escribe → etiqueta `humano`.
- Landing: `FAG-TRI` etc. como referencia; atribución por `referral.source_id` o referencia en el texto; sin pista →
  `null` (nunca se adivina).
- **[CAMBIA]** «asistente virtual» solo si preguntan → SKILL §1.

## 5. Creator (creator) — IA que no habla con clientes por WhatsApp
Claude (principal) y OpenAI (respaldo) generan análisis/propuestas; los números los calcula el código (`lib/precios.ts`,
`lib/analisis.ts`, `lib/pagos.ts`). Reglas de IA: módulos a medida = herramienta/agente IA nuevo con valor propio;
integraciones con lo que el cliente ya usa van incluidas sin costo; nombres «Agente de… / Sistema de…»; precio por tabla
($300/$600/$900, el último es tope). Preguntas de entrevista: busca ≥2 dolores ocultos distintos de los nombrados.

## 6. Motor de contenido (postpro-321)
Redacta captions con `gpt-4.1-mini`. REGLAS DURAS: solo datos de FUENTE, nunca inventar precios/metros/ubicaciones/plazos,
nunca propietarios/cédulas/teléfonos/correos de terceros, «Imagen referencial.» si es render de IA. Revisor de frases
prohibidas (`motor/skills.py::PROHIBIDAS`) que obliga a reescribir. Único personaje: Byron. Bot de comentarios y DM
(`321-inmo-webhooks-redes.json`): **[CAMBIA]** «NO eres un bot» → SKILL §1; capta al lead hacia WhatsApp, nunca propone
visitas/citas, spam → responde solo `IGNORAR`.

## Origen
Rutas indicadas en cada sección; además `/home/user/crm-321/docs/07-plan-crm-agentico.md`, `docs/15-whatsapp-academy.md`,
`docs/HANDOFF.md`, `/home/user/bcujano/creator/docs/DECISIONES.md`, `/home/user/postpro-321/motor/`.
