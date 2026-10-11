# Andromeda, estructura de campaña, pruebas y rúbrica · detalle

Etiquetas: [V] oficial, [E] explícito en repo/blog, [T] terceros, [I] inferencia. Fechas de investigación: 2026-10-03/04 (repos) y 2026-10-07 (fuentes oficiales). Enlaces en `fuentes.md`.

## 1. Qué es real y qué es humo (verificado el 2026-10-07)
| Afirmación | Veredicto |
|---|---|
| «Andromeda» existe y cambia la entrega | **Real [V].** Motor de recuperación que filtra decenas de millones de anuncios a miles; +6 % de recuperación y +8 % de calidad de anuncio en segmentos; se apoya en el volumen de creativos elegibles (blog de ingeniería de Meta) |
| «Entity ID» y «similitud > 60 % se suprime» | **No está en la fuente oficial [V].** Los blogs lo presentan como hecho y admiten que Entity ID es término de la industria. Tratar como **heurística útil [T]**, no como ley |
| «El creativo es la segmentación» | Razonable [T/I]. Meta no lo dice con esas palabras |
| Formulario «Higher intent» filtra malos leads | Real [T]: agrega pantalla de revisión, baja el volumen 20 a 40 % y sube la calidad. Meta ofrece verificación por SMS y correo de trabajo [V] |
| Click-to-WhatsApp con optimización de leads: +45 % de leads calificados, −30 % de CPL | Caso de un proveedor [T]. Direccional, no promesa |
| «CPL barato = buen negocio» | **Humo.** Lo que manda es costo por reunión realizada y por contrato firmado |
| Advantage+ de clientes potenciales: −14 % costo por lead y −10 % por lead calificado | Cifras autorreportadas por Meta [V]; ajustes muy restrictivos desactivan la automatización |

Nota: la primera versión de la base (`BASE_CONOCIMIENTO_ADS.md`, 2026-10-04) marcó el «60 %» como [E]; la investigación del 2026-10-07 la corrigió. Vale la segunda.

## 2. Estructura de campaña
1. [E] El creativo es el targeting [I]: primero conocer a la audiencia y hacer el creativo; los filtros después. Segmentación amplia (solo país o ciudad), sin apilar intereses.
2. [E] Concepto ≠ variación. Un concepto = otro ángulo, formato, persona o escena.
3. [E] Con 10 a 20 creativos diversos por conjunto (Heath: mínimo ~20 con distintos ángulos y etapas de conciencia). Con poco presupuesto, «4 buenos > 20 mediocres».
4. [E] Mezclar etapas de conciencia (no consciente, problema, solución, producto) en el mismo conjunto; no separar el embudo en campañas.
5. [E] Estáticos: ~10× más baratos de producir que video, en 2026 suelen igualar o superar al video pulido. Volumen y refresco constante.
6. [E] Consolidar: 1 campaña, 1 a 2 conjuntos; no fragmentar con poco presupuesto.
7. [E] Objetivo de leads o registro (no tráfico ni interacción) y optimizar al evento con datos. Pixel y API de Conversiones bien configurados. Si el cierre es por WhatsApp, el objetivo de mensajes con la misma estructura [I].
8. [E] No editar anuncios vivos (reinicia el aprendizaje): se lanzan nuevos.
9. [I] Para lanzar en Ecuador: 4 a 6 conceptos estáticos distintos (dolor, resultado, prueba, curiosidad, identidad, contrario), cada uno en 4:5 y 9:16 (+1:1 si hay feed cuadrado).

## 3. Pruebas y decisiones
- [E] Orden: oferta → ángulo → formato → estilo → gancho → variables menores (titular, color, CTA). No mezclar rondas. Rondas de ~5 ángulos (esperar ~2 buenos).
- [E] Umbrales mínimos para juzgar: ≥ 1.000 impresiones, ≥ 3 conversiones, ≥ 2 días; ventana de 7 a 10 días; confianza ~90 %. Evaluar por costo por resultado, no por interacción.
- [E, un solo repo] Pausar si el CPL llega a ~3× el objetivo con volumen; cerca del objetivo, dar tiempo. No apagar anuncios de tope de embudo por ROAS aislado; reemplazar por uno equivalente.
- [E, un solo repo] Subir presupuesto máximo +20 % cada 3 a 5 días (o 10 a 20 % cada 48 h); no tocar más de una vez cada 48 h; bajar presupuesto en vez de pausar y encender.
- [E] Con < 50 conversiones por semana: agregar anuncios claramente distintos al mismo conjunto, sin rondas múltiples de prueba. Reparto 80/20 o 70/30 (probado/prueba).
- [E] Frecuencia sana 1,8 a 2,8; > 2 por semana en frío es alerta; ≥ 3 en 7 días indica fatiga; ≥ 4 actuar ya.
- [E] Rondas de enfoque: 3 medios + 2 textos + 1 titular (estándar) o 2+1+1 (< $10/día).
- [I] Costo máximo por reunión realizada = ingreso mensual del plan × meses de permanencia × % de cierre × % del margen que el cliente destina a captar. El % de cierre es un supuesto que se mide. Referencia del caso del despacho: tope de ~$145 a $320 por reunión con un plan de $400/mes y 12 meses; pausar con volumen por encima de ~$200 (punto de partida, ajustar con datos). No publicar estos números del cliente.
- [I] Para eventos con precio bajo: punto de equilibrio por lead = precio × tasa de compra del lead; apuntar a menos de la mitad.
- Rotación semanal 3-3-2-2 (ccai-meta-ads-autopilot): 3 duplican ganadores, 3 inspirados en competencia, 2 pilares psicológicos nuevos, 2 comodines. Antipatrón: 10 anuncios con el mismo hook.
- Clonar la **forma** (líneas, movimientos) de anuncios ganadores de la Meta Ad Library, no las palabras ni las afirmaciones (execution-ads-make).

## 4. Diagnóstico de la medición
- Medir por pieza y por perfil: costo por reunión realizada y por contrato firmado, por concepto. Lo que no trae reuniones se pausa; se lanzan conceptos nuevos, no se editan los vivos.
- CPL de abogados en EE.UU. (~$105, 5 a 10 % de leads cierra [T]) no sirve para Ecuador: no hay benchmark verificable; se mide la primera semana.
- Benchmarks de blog: CTR de leads 2,59 %, CPM de LatAm distinto: usar el promedio propio de 28 días.

## 5. Rúbrica previa al gasto (adaptada de creatify-ai/ad-creative-evaluator y meta-ads-pro [I])
| # | Criterio | Peso |
|---|---|---|
| 1 | Gancho que frena el scroll en < 2 s | ×1,5 |
| 2 | Un solo ángulo y mensaje claro en 3 s | ×1,3 |
| 3 | Texto legible en móvil (tamaño, contraste, poco texto) | ×1,0 |
| 4 | Encaje con el perfil y llamado de identidad | ×1,2 |
| 5 | CTA única y visible | ×1,3 |
| 6 | Prueba o credibilidad real (cara, reseña, cifra verificable) | ×1,0 |
| 7 | Seguridad de formato (4:5, 9:16, recorte 1:1) | ×1,0 |
| 8 | Diversidad frente al resto del set (< 40 % parecido) | ×1,2 |
| 9 | Honestidad y políticas (sin falsa urgencia ni atributos personales) | puerta: pasa o no pasa |
| 10 | Coherencia entre anuncio, landing y formulario (misma promesa y precio) | ×1,0 |
Puntaje = suma(nota × peso) / suma(pesos). ≥ 8,5 lanzar y escalar · 7 a 8,4 lanzar con ajustes · 5,5 a 6,9 corregir 2 debilidades · < 5,5 rehacer.

## Origen
- `contenido-higgsfield/taller_prompting/meta_ads_reglas.md` (secciones A, D, E).
- `contenido-higgsfield/taller_prompting/BASE_CONOCIMIENTO_ADS.md` (§2, §3).
- `contenido-higgsfield/taller_prompting/higgsfield_meta_ads_nativo.md` (§2.5).
- `contenido-higgsfield/fagal/INVESTIGACION_FAGAL_B2B.md` (§2, §3, §5), `fagal/SEGMENTACION_DESDE_EL_CREATIVO.md`.
- `contenido-higgsfield/taller_prompting/ads_nativo/ESTRATEGIA_META_ADS_TALLER.md` (§5).
