# Decisiones y «no hacer» · contenido-higgsfield (producción de anuncios con IA de imagen)

Repo `bcujano/contenido-higgsfield` (clonado en `/home/user/bcujano/contenido-higgsfield`; en la PC de Byron, la carpeta de proyectos de Higgsfield). Un solo commit inicial («Subida inicial del proyecto HIGGSFIELD»). Material de las sesiones del 2026-10-03 al 2026-10-07. Skills derivados: `aiuda-produccion-visual-higgsfield` y `aiuda-meta-ads-reglas`. Este archivo es para sesiones auditoras (no se copia a los repos).

## 1. Qué es
Carpeta de trabajo, no una aplicación: investigación, reglas, scripts de maquetación y salidas de dos encargos.
1. **Taller de IA de Byron** (curso presencial de 3 días, campaña propia de AIUDA): fotos con el Soul del dueño, 4 juegos de anuncios (fotos, «datos primero», vectorial, pixel art), posters, portada de Facebook y copys. Campaña lanzada por el dueño el 2026-10-07.
2. **Un despacho de abogados cliente de Aiuda Consulting**: investigación B2B, 6 conceptos, decenas de anuncios en varias tandas, Soul del socio, línea de vinculación gremial, cuestionario y mensaje para pedir fotos.
Más 8 skills de terceros de Higgsfield (`.claude/skills/` y espejo `.agents/skills/`) y `skills-lock.json`.

## 2. Estructura
| Ruta | Contenido |
|---|---|
| `CLAUDE.md` | Reglas que no se negocian del proyecto (Soul, escena completa, pruebas antes de lotes, texto en HTML, vestuario) y datos fijos del evento |
| `taller_prompting/LEEME_PRIMERO.md` | Traspaso: datos fijos, reglas del usuario, mapa de archivos, cómo regenerar, datos operativos de Higgsfield, lecciones, estado |
| `taller_prompting/BASE_CONOCIMIENTO_ADS.md`, `reglas_ads.json` | Reglas con fuentes y etiquetas [E]/[I]; 85 reglas estructuradas |
| `taller_prompting/meta_ads_reglas.md`, `higgsfield_meta_ads_nativo.md`, `diseno_vectorial_reglas.md` | Informes de investigación originales |
| `taller_prompting/ads_nativo/` | Estrategia de campaña, `render_*.py`, fotos elegidas y descartadas, juegos y fases |
| `taller_prompting/ads_meta*/`, `soul301_*`, `poster_*`, `portada*`, `grupo_lobby` | Rondas rechazadas, posters y portadas |
| `fagal/` | Documentos del despacho, ocho tandas de anuncios (`ads`, `ads_marca`, `ads_soul`, `ads_soul2`, `ads_v2`, `ads_v3`, `ads_final`, `ads_t5`), Soul, logo, entrega del cliente, formulario (`wizard`) |
| `soul_byron/`, `generados/`, `salida/` | Fotos y pruebas del Soul del dueño (imágenes; ignoradas) |
| `.claude/skills/`, `.agents/skills/` | Skills de higgsfield-ai (no son nuestros) |

## 3. Qué se reutiliza (ya está en los skills)
- **Método de producción:** Soul del dueño, escena completa en una generación, una prueba y costo antes del lote, hoja numerada para elegir, texto en HTML/CSS con render en navegador sin interfaz, verificación con zoom, regenerar por fase editando el script → `aiuda-produccion-visual-higgsfield`.
- **Reglas de Meta, rúbrica previa al gasto, umbrales, segmentación desde el creativo, jerarquía dolor-oferta, diseño para servicios de confianza, embudo B2B, plantilla de campaña por fases** → `aiuda-meta-ads-reglas`.
- **Plantillas de concepto** (8 lenguajes vectoriales y 6 conceptos del taller) como patrones de gancho, no como texto.
- **Mensaje modelo para pedir fotos reales a un cliente** y **cuestionario de 10 preguntas** como esqueleto de onboarding de un cliente de servicios profesionales.
- Los scripts `render_*.py` como plantilla técnica (una función por plantilla, fase por variable). Requieren adaptar rutas de Windows antes de reutilizarse en otro equipo.

## 4. Datos de cliente o de evento que NO deben entrar al centro
- **Soul IDs** (del dueño, otras versiones y del socio del despacho), IDs de trabajos y de referencias subidas a Higgsfield, saldos de cuenta: viven en la configuración del sistema o en el handoff del proyecto. En los skills solo se dice «el Soul ID del dueño, que se guarda fuera del centro».
- **Nombre, fotos, estado de aprobación y textos finales del despacho:** precios del plan, duración del contrato, ofertas, convenios, nombres de gremios y logos, copys de las tandas, el titular de cada pieza, comisiones y metas económicas acordadas. Se extrajeron solo métodos.
- **Datos del evento del dueño:** fechas, lugar, precios por fase, credenciales y copys finales. Son datos de configuración de la campaña, no conocimiento general.
- **Imágenes** (fotos de personas, anuncios, posters) y logos de terceros: no se versionan en el centro.
- El repo no contiene claves, teléfonos ni correos (comprobado con búsqueda); el formulario `fagal/wizard/ficha_fagal.html` trae una constante de teléfono vacía a propósito. Los accesos a Meta se dan en el administrador, nunca por chat.
- Hay IDs de la cuenta de Higgsfield y rutas absolutas del equipo del dueño en `LEEME_PRIMERO.md` y en `poster_*.py`: no copiar.

## 5. Contradicciones (con los skills existentes y dentro del repo)
Para decidir por Byron. Entre paréntesis, qué se aplicó mientras tanto en los skills nuevos.
1. **Texto sobre la foto.** Los anuncios del Taller maquetan el titular encima de la foto Soul (zona despejada + sombra); `aiuda-diseno` (regla 2, Byron 2026-10-04) dice «ningún texto sobre la foto». El mismo repo pidió «espacio vacío arriba para el texto», lo que implica texto sobre la foto. (Se aplica `aiuda-diseno`: foto sola y texto en fondo plano o al lado; falta que Byron aclare si los estáticos de evento quedan exentos.)
2. **Persona real vs imagen de IA.** `aiuda-diseno` regla 7 y `aiuda-contenido-y-voz`: rostro real del facilitador, único personaje, nunca otros presentadores ni modelos. Este repo genera al dueño con IA (Soul) y fotos grupales con «rostros distintos», y entrenó un Soul del socio de un cliente. En el propio repo, la investigación recomendó «fotos reales de los socios; Soul solo para Byron» y el mismo día se revirtió. La aprobación del socio para su imagen generada sigue pendiente. (Se exige persona real autorizada y no mostrar eventos reales.)
3. **«Entity ID» y «60 % de similitud».** `BASE_CONOCIMIENTO_ADS.md` y `meta_ads_reglas.md` lo marcan [E]; `fagal/INVESTIGACION_FAGAL_B2B.md` y `SEGMENTACION_DESDE_EL_CREATIVO.md` (después) dicen que no está en la fuente oficial. (Vale lo segundo: heurística.) Ningún skill existente lo menciona.
4. **Zona segura de 9:16.** Cuatro valores: 250 px y 20 % (meta_ads_reglas), 250 y 340 px (diseno_vectorial_reglas), 14 % arriba y 35 % abajo y 6 % lados (guía oficial citada en fagal), 270 px simétricos (`aiuda-diseno`). (Reels: oficial; Stories: 14 %.)
5. **Largo del copy.** Descripción ~30 (repo) vs ≤ 25 (`aiuda-contenido-y-voz`); titular 27 a 40 vs ≤ 40; texto principal 125 visibles (repo) vs primeros 125 (igual) y 50 a 150 (oficial). (25 y 40.)
6. **CTA frío.** «Más información»/«Registrarse» (repo) vs «nunca Más info» (`aiuda-contenido-y-voz`).
7. **«Desde $».** El copy del Taller usa «Desde $65» en una descripción; el plan de octubre y el skill de contenido lo excluyen salvo precio mínimo en ficha.
8. **Precio en anuncios.** La escala de precios del Taller resalta la fase vigente; la decisión de Byron del 2026-10-11 pone el precio de efectivo o transferencia como el más grande. El repo no distingue efectivo de tarjeta: falta alinear.
9. **Presupuesto y estructura.** $15 a $20 al día para 6 anuncios y 1 conjunto (evento) vs $5 a $10 por día por conjunto y 3 a 5 anuncios (inmobiliario con mensajes). Son casos distintos; no hay regla común.
10. **Destino y objetivo.** El Taller y el despacho optimizan a formulario o registro («Registrarse»); `aiuda-contenido-y-voz` y los repos inmobiliarios van a mensaje de WhatsApp precargado («WhatsApp primero»). Sin regla de cuándo cada una.
11. **Divulgación de IA en el agente.** Este repo manda «avisar que es asistente virtual» al agente del despacho; consistente con la decisión del 2026-10-11 (ver `aiuda-agentes-whatsapp`). Sin conflicto, pero repetido aquí.
12. **Mayúsculas y marca.** El repo usa «AIUDA» en mayúsculas (porque la I y la l se confunden en sans) y en un copy aparece «AIuda». `aiuda-contenido-y-voz` pide «sin frases en mayúsculas» pero las etiquetas cortas (CUPOS LIMITADOS, GRATIS) son visuales. (Etiquetas sí, redacción no; marca siempre AIUDA.)
13. **Costos.** El skill de terceros `higgsfield-generate` dice no pre-estimar costos; el repo exige costo antes de lotes. Y el skill prefiere GPT Image 2.5 para texto; el repo, HTML. (Mandan las reglas de AIUDA.)

Líneas sugeridas para `contradicciones-abiertas.md` (el revisor las agrega; este archivo no la modifica): puntos 1, 2, 4, 6 y 8.

## 6. Vacíos
- No hay medición real: ningún archivo trae resultados de la campaña (CPL, CTR, reuniones). Todo umbral es de blogs o repos; ningún número de Ecuador.
- No hay política escrita de uso de imagen generada de una persona (consentimiento, vigencia, etiquetado de IA).
- No se verificó la política de Meta sobre imágenes de IA; la advertencia es del repo.
- Falta probar los 8 skills de terceros con las reglas de AIUDA; solo se usó la plataforma directamente.
- Los scripts dependen de Windows, Chrome en ruta fija y fuentes de Google; no hay versión parametrizada ni de servidor.
- Quedó pendiente la fase 3 de precios en los scripts del Taller al momento del último traspaso (2026-10-07) y la rotación 3-3-2-2.
- Reglas del colegio de abogados local, categoría especial de anuncios, ética de comisiones: sin leer (marcadas [?] en el origen).
- No hay manual de marca del cliente del despacho ni voz definida para clientes de servicios profesionales.
- El hash de `skills-lock.json` no se comprobó contra GitHub.

## 7. Qué no hacer (aprendido)
- No usar un modelo de edición con foto de referencia para cambiar una cara; no recortar y pegar sujetos.
- No generar fotos que el usuario no pidió; no lanzar lotes sin prueba y costo; no usar `get_cost` dentro del lote de imágenes (lanza un trabajo real).
- No poner texto dentro de la imagen generada; no dibujar botones, encuestas ni chats que parezcan funcionar.
- No presentar variaciones de color como conceptos distintos.
- No dirigir anuncios a personas por una condición personal; no garantizar resultados; no usar logos de terceros sin autorización escrita.
- No pedir al cliente lo que se puede investigar o crear.
- No describir a un cliente el stack interno (Higgsfield, scripts, navegador sin interfaz).

## Origen
- `contenido-higgsfield/CLAUDE.md`, `skills-lock.json`.
- `contenido-higgsfield/taller_prompting/LEEME_PRIMERO.md`, `BASE_CONOCIMIENTO_ADS.md`, `reglas_ads.json`, `meta_ads_reglas.md`, `higgsfield_meta_ads_nativo.md`, `diseno_vectorial_reglas.md`, `COPYS_TODOS_LOS_JUEGOS.md`, `ads_nativo/ESTRATEGIA_META_ADS_TALLER.md`, `ads_meta/copys_meta_ads.md`.
- `contenido-higgsfield/fagal/DISENO_ANUNCIOS_ABOGADOS.md`, `JERARQUIA_Y_COPY.md`, `SEGMENTACION_DESDE_EL_CREATIVO.md`, `CONCEPTOS_6_FAGAL.md`, `LINEA_FENATRAPE_Y_REQUISITOS.md`, `WHATSAPP_PEDIR_FOTOS.md`, `INVESTIGACION_FAGAL_B2B.md`, `CUESTIONARIO_FAGAL.md`, `soul_galarraga/LEEME_FOTOS.md`, `entrega_cliente/LEEME_QUE_PONER_AQUI.md`, `wizard/ficha_fagal.html`.
- Skills comparados: `skills/aiuda-contenido-y-voz/`, `skills/aiuda-diseno/`, `knowledge/decisiones/postpro-321.md`, `knowledge/contradicciones-abiertas.md`.
