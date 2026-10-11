# Decisiones cerradas y «no hacer» — postpro-321 (motor de contenido)

Repo `bcujano/postpro-321`, clonado en `/home/user/postpro-321` (en la PC de Byron `C:\dev\postpro-321`). Python desplegado en
Railway como `postpro-321` (`postpro.321archlab.com`) **automáticamente al subir a `main`**. Sin `CLAUDE.md` propio: la documentación se
mudó el 2026-09-26 a `crm-321/docs/` (aquí quedan el motor `motor/`, los respaldos de workflows n8n `n8n/workflows/` y código `legacy/`).
Nombre viejo: «listapro».

## Decisiones
- Solo el router `/api/motor/*` es vigente; el resto de `main.py` es legacy.
- La CLI de `railway` en `listapro` estaba vinculada a `webhook-321inmo`: usar siempre `-s postpro-321`. Variables:
  `railway variables --service postpro-321 --set "K=V" --skip-deploys` y luego un push despliega una sola vez.
- **Soul de Higgsfield fijo «Byron 3.01»** (`HIGGSFIELD_SOUL_ID`); el sistema nunca elige ni crea personajes.
- Skills editoriales en `motor/skills/*.md` (hooks, carrusel, reel, caption, historia, anuncios Meta, segmentación, voz y reglas,
  diseño de piezas); `diseno-piezas.md` se genera desde `crm-321/src/lib/vectorial/conocimiento.ts` con
  `scripts/exportar-diseno-motor.mts` (HANDOFF §0.6): un cambio a mano se pisaría al regenerarla.
- Lanzamientos: ficha nueva con ≥3 fotos → carrusel + historia a 0 créditos + reel como «propuesta».
- En el CRM (no aquí) que publica lo del motor: Facebook se publica con token de **página** (`src/lib/meta-pagina.ts`; el
  `META_PAGE_ACCESS_TOKEN` es de usuario), publicación parcial = «publicado con aviso», y los reels se recodifican a H.264/AAC vertical
  ≤ 90 s antes de subir (`lib/reel.ts`). Fuente: HANDOFF §0.3 y §0.6.
- Arreglo `images do not match` en `motor/piezas.py::sobre_retrato` (2026-10).

## Reglas duras de redacción (`motor/redaccion.py`, `motor/skills/voz-y-reglas.md`)
- Usar **solo datos de FUENTE** (ficha del CRM); si falta un dato no se menciona; nunca inventar precios, metros, ubicaciones, plazos,
  testimonios, clientes, citas, ventas cerradas, cifras ni resultados; nunca redondear hacia arriba.
- Nunca propietarios, cédulas, teléfonos ni correos de terceros.
- Render generado por IA → línea final «Imagen referencial.»
- Prohibido prometer lo que nadie puede garantizar («plusvalía garantizada», «rentabilidad asegurada»).
- Sin «¡Hola!», «Hola, soy…», «No dudes en contactarnos», «Estamos aquí para ayudarte». Único personaje: Byron.
- Revisor de frases prohibidas (`motor/skills.py::PROHIBIDAS`): si hay, se reescribe.
- Diseño: nunca letras sobre una foto; un botón con verbo y destino; nunca «recargo»; fotos de personas ancladas arriba.
- Modelo de textos: `gpt-4.1-mini` (`MOTOR_MODELO_TEXTO`).

## Respaldos de workflows n8n (`n8n/workflows/`)
`321-iagente-inmo-v2.json` (agente de WhatsApp, copia del respaldo de crm-321), `321-iagente-inmo-chatwoot-crm-v1.json` (v1 obsoleto),
`321-inmo-webhooks-redes.json` (comentarios/DM de redes), `321-seguimiento-automatico-v5-2.json` / `v6.json`, `321-contenido-ia-motor.json`,
`321-marketing-ia-director.json`, `321-post-pro-publicar-programadas.json`, `321-mensaje-manual-crm-v4.json`, `321-inmo-alertas-de-error.json`,
`321-keep-alive-whatsapp-byron.json`. Los JSON pueden traer credenciales literales: no copiarlos a otros repos (en VIP una llave de 321 en
git obligó a purgar el historial).

## «No hacer»
- Reactivar el agente v1 («Byron, asesor SETTER»): ordena «NUNCA digas “soy un asistente virtual / bot / IA”».
- Reutilizar el prompt de `321-inmo-webhooks-redes.json` sin corregir «NO eres un bot» ni las afirmaciones no verificables
  («Siempre decimos SI», «red de agentes en todo el mundo»).
- Editar `diseno-piezas.md` a mano (se regenera); cambiar el Soul; vincular la CLI de Railway al servicio equivocado.
- Publicar en Facebook con el token de usuario.

## Reglas antiguas que se reemplazan
`321-iagente-inmo-chatwoot-crm-v1.json` (línea 1548), `321-iagente-inmo-v2.json` (línea 1558), `321-inmo-webhooks-redes.json`
(nodo «Armar Prompt IA»): ver skill `aiuda-agentes-whatsapp` §13.

## Origen
`/home/user/postpro-321/README.md`, `docs/README.md`, `railway.json`, `motor/redaccion.py`, `motor/skills.py`, `motor/skills/voz-y-reglas.md`,
`motor/skills/diseno-piezas.md`, `n8n/workflows/*.json`, `/home/user/crm-321/docs/HANDOFF.md` (§0.1, §0.3, §0.6, §6).
