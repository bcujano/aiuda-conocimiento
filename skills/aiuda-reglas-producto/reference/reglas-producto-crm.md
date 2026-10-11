# Reglas de producto y de datos del CRM 321 (A–J): detalle

Aplican a `crm-321`. El principio de cada una es reutilizable en otros repos (se indica al final de cada bloque).
Origen: `/home/user/crm-321/CLAUDE.md` y `/home/user/crm-321/docs/12-pendientes.md` (tabla «Cómo funciona ahora»).

## A. Todo término lleva su icono de ayuda
- Dictada por Byron el 2026-09-27: «todo debe tener su icono ayuda y su explicación».
- Cada palabra técnica en pantalla se define en `src/lib/glosario.ts` (tipo `Termino`: `titulo`, `que_es`,
  `de_donde`, `efecto`, `ejemplo`) y se muestra con `<Ayuda termino="clave" />`.
- Las cuatro líneas son: qué es · de dónde sale · cómo afecta · ejemplo.
- Un término sin ayuda es un error, igual que un `any` sin justificar: la pantalla no está terminada.
- Cómo aplicarla: antes de cerrar una pantalla, lista cada término que un gerente de inmobiliaria no usaría en
  una conversación normal y verifica que tenga clave en el glosario.

## B. Todo resultado se interpreta solo (regla R1)
- Componente `src/components/Lecturas.tsx` (plegable; botón «Ver N» / «Ocultar»; **cerrado por defecto**).
- Contenido: no repite lo visible; dice qué decisión sale; **con qué cruzarlo** (`cruzar`, con enlace directo).
- Las lecturas viven en `src/lib/lecturas*.ts`. Existe el «mapa R7» y la pantalla «Cruce de datos».
- Se alimenta solo de cuentas sobre datos del sistema (regla C): si falta el dato, la lectura no aparece.

## C. Ningún número lo escribe un modelo de lenguaje
- Una conclusión es una cuenta con origen visible. Si falta un dato: se dice que falta.
- Ejemplos aplicados: tasas del BCE se leen de la tabla oficial sin IA (`lib/bce.ts`); ingreso de hogares del INEC
  leído de microdatos sin IA; diagnóstico de Academy (`guardarDiagnostico`) calculado por el sistema; en el agente
  de Academy, un freno bloquea cualquier link, monto o número de cuenta que no esté en el contexto.
- Extensión a agentes: ver skill `aiuda-agentes-whatsapp` («cero invención»).

## D. Escrito para el usuario
- «Los leads sin teléfono», nunca «el campo `telefono`».
- No se le explica cómo está hecho el sistema; se le dice qué hacer.
- El panel de control se diseña visual, claro y sin rodeos (docs/07 §1b).

## E. Una función, un lugar
- Clasificación de leads: solo `lib/clasificacion.ts` (`clasificarLead`, `clasificacionDe`). La guardada
  (`leads.familia`) manda al contar; un mensaje sin señal no baja un lead a «sin clasificar».
- Precios: solo el **Catálogo 321** (`catalogo_321`, `/api/catalogo-321`). La hoja de Google dejó de ser fuente. Un
  precio es oficial si tiene `precio_fuente`.
- Agente de WhatsApp: lee catálogo e intención del anuncio desde `/api/agente/contexto` (`lib/anuncios.ts`).
- Precio publicado de Academy: una sola función `totalTarjeta` (`lib/academy/precios.ts`); `esGratis` en el mismo archivo.
- Demanda: sin leads de prueba, sin presupuestos del simulador, sin valores iguales a un precio publicado
  (`lib/demanda.ts`).

## F. Fuente del dato
- `lib/fuente-dato.ts` + `components/FuenteDato.tsx`: dato 321 si pasa el mínimo → dato público con enlace → «sin dato».
- Prohibido el scraping de portales (Plusvalía, Properati, Mitula, Remax, eXp/Tokko y OMNI MLS descartados de forma
  definitiva); API de Wasi/ACBIR Guayas **no aprobada**: no se vuelve a mencionar. Solo fuentes oficiales + búsqueda
  con citas + datos propios (docs/06, «Cosas que NO hay que volver a preguntar»).
- Costo de `buscarWeb`: ~$0,048 por consulta; decir siempre el costo mensual antes de proponer algo.

## G. Notas ≠ Actividad
- Notas del lead = resumen corto «Campo: valor» (`lib/notas-lead.ts`). La conversación vive en Actividad
  (`lead_activities`). Se movieron 169 leads el 2026-09-27.

## H. Disco limitado
- Supabase `crm-321` en plan gratis; el 27-sep se cayó por Disk IO. Escrituras masivas en lote y con pausa; nunca
  fila por fila en bucle. Publicador y seguimiento van cada 10 min. Supabase Pro ($25/mes) llegará cuando el CRM se
  venda a otras inmobiliarias (decisión de Byron).

## I. Pruebas con sesión real
- Cerrar la sesión de prueba al terminar (`POST /auth/v1/logout`).
- En el navegador integrado, comprobar que la pestaña está en el dominio de producción antes de escribir una sesión
  (el 27-sep se escribió en otro sitio por error).
- Nunca abrir producción en un navegador de pruebas (dispara el Pixel): para producción, leer el HTML con `curl`.

## J. Vista previa `?vp=`
- Solo protege cursos NO publicados. En el Taller (publicado) crea personas reales en producción.
- Probar landings con borradores o con el servidor local seguro (`crm-321-seguro`, puerto 3322, sin Pixel ni
  WhatsApp a dirección). Limpiar con `limpiar-pruebas.mjs`.
- `prueba-filtro.mjs` se corre con `BASE=http://localhost:3322`, nunca contra producción.
- Nunca disparar Pixel ni WhatsApp reales en pruebas. Usuarios temporales: `scripts/academy-pruebas/usuario-temporal.mjs`.

## Reglas de Academy fijadas por Byron (HANDOFF §0.4; no se renegocian)
1. Cliente del Taller = uso **básico** de IA (conversar, redactar, imágenes); intermedio/avanzado → etapa «Otro nivel».
2. Todos los que llenan el formulario quedan en la base y el pipeline; **nunca se descartan**.
3. Diagnóstico de 2 preguntas (el de 8 tenía abandono).
4. Precio publicado = tarjeta (entrada × 1,06 con centavos); efectivo/transferencia se presenta como **descuento**;
   **nunca la palabra «recargo»**. En landings, el precio grande es el de efectivo/transferencia.
5. Las herramientas generales (vectorial, ebooks) viven en Marketing/CRM; Academy las usa.
6. Banco de 23 cursos gratis por nivel; los 4 de nivel 1 publicados: «no tocar lo publicado».
7. Ebooks de 4 niveles. Soul de Higgsfield: «Byron 3.01»; el sistema nunca elige ni crea personajes.
8. No se hace pago real de prueba.
9. **WhatsApp primero y costo cero: nunca escribimos primero**; plantillas apagadas (`ACADEMY_PLANTILLAS_ACTIVAS`).
10. Hero sin letras sobre la foto; los 10 estilos son diseños distintos; todo premium.
11. n8n con respaldo y sin tocar el de producción de 321; SQL lo pega Byron; costo de IA mostrado antes de gastar.

## Reglas de diseño de piezas (motor, `motor/skills/diseno-piezas.md`)
- Nunca letras sobre una foto (texto sobre fondo plano). Un solo botón con verbo y destino («Escríbenos por WhatsApp»,
  nunca «Click aquí»). Fotos de personas ancladas arriba. Nunca la palabra «recargo».
- Voz: sin «¡Hola!», «Hola, soy…», «No dudes en contactarnos», «Estamos aquí para ayudarte»; único personaje: Byron.
- Sin promesas: «plusvalía garantizada» y «rentabilidad asegurada» están prohibidas.

## Guía de diseño de landings
`/home/user/crm-321/docs/14-diseno-landings.md` es **obligatoria antes de tocar diseño**: jerarquía visual (§3),
fotos por sección (§4), SVG (§5), lista de verificación (§6), jerarquía del precio, prueba suave de titulares.

## Marco legal de Opinión de Valor (docs/09 §6)
- El entregable se llama «Opinión de Valor Referencial de Mercado (OVR)»: nunca «avalúo», «tasación», «peritaje»,
  «valor oficial» ni «valor certificado».
- Siempre un rango, nunca una cifra única; aviso legal copiado tal cual en cada informe; vigencia de 90 días.
- Nunca: «su casa vale $X» (siempre «rango de oferta sugerido $X–$Y»), promesas de venta o rentabilidad, que sirva
  para banco/BIESS/juicio/SRI, avalúo catastral presentado como valor de mercado, comparables sin fuente ni fecha.
- Fuente: `/home/user/crm-321/docs/09-marco-legal-avaluos.md`.
