# Diseño de estáticos, copy y políticas · detalle

Solo lo que NO está ya en `aiuda-diseno/reference/piezas-graficas.md` ni en `aiuda-contenido-y-voz/reference/anuncios-meta.md`. Lo repetido se enlaza.

## 1. Formato
- [E] Primario 4:5 (1080×1350), segundo 1:1, tercero 9:16 (1080×1920). Subir versiones nativas de cada una; no depender del recorte automático.
- [V] Oficial (Ads Guide de Meta, consultado el 2026-10-07): 4:5 a 1440×1800 px para Feed; 9:16 a 1440×2560 para Reels o 1080×1920 para Stories; JPG o PNG; texto principal de 50 a 150 caracteres; titular ~27.
- [E] Mensaje clave en el 80 % central; los bordes se recortan.
- [E] Un solo punto focal, sin collages; un ángulo y un mensaje por anuncio (mezclar beneficios penaliza).
- [E] Con texto incrustado, apagar overlays, animación y «enhanced media text»; dejar activos retoques visuales, flex media y mejoras de texto del copy.

## 2. Zonas seguras (tres fuentes distintas)
| Formato | Fuente | Valor |
|---|---|---|
| 4:5 | tenfoldmarc, adkit [E] | 100 px libres arriba y abajo en 1080×1350 |
| 4:5 | diseno_vectorial_reglas [I] | margen 84 px a los lados y 96 px arriba/abajo |
| 9:16 | meta_ads_reglas [E] | ~250 px (15 %) arriba y 20 % abajo; contenido en el 65 % central |
| 9:16 | diseno_vectorial_reglas [E] | ~250 px arriba y ~340 px abajo (en 1080×1920) |
| 9:16 Reels | Ads Guide oficial [V] | ~14 % arriba, **35 % abajo** y 6 % a los lados |
Regla práctica: para Reels usar la oficial; para Stories, 14 % arriba y abajo (`aiuda-diseno`: 270 px).

## 3. Texto en la imagen
- [E] Hook de 3 a 7 palabras; titular de 6 a 8 palabras en pieza vectorial; el resto va en el copy de Meta. Demasiado texto puede verse recargado y afectar el rendimiento [V, mejores prácticas de aspecto de Meta].
- [E/I] Titular ≥ ~64 px y subtexto ≥ ~36 px en lienzo de 1080 (la escala completa está en el skill de producción).
- [E] Texto grande, alto contraste, legible en móvil (80 %+ del tráfico según la fuente).
- [E] Que parezca contenido nativo: texto sobre imagen, notas, mensaje de chat, listicle, estadística, reseña real. Rinden mejor en tráfico frío.
- [E] Cara mirando a cámara si se usa; prueba social con texto real de reseña, no solo «5 estrellas». Sin caras de IA en rubros delicados (adkit); usar foto real del instructor aumenta confianza [I].
- [E] Evitar Inter/Roboto/Arial por defecto y los clichés de IA (crema+serif+terracota, morado-azul, tarjetas idénticas, 01/02/03 decorativo). Sin em dashes.

## 4. Copy
- [E] Texto principal: 125 caracteres visibles antes de «ver más» (hasta 2.200); titular ~27 a 40; descripción ~30 (el skill de contenido usa 25). Lo clave arriba.
- [E] El copy largo funciona si las 2 primeras líneas enganchan; formato con viñetas.
- [E] Fórmulas de gancho: número+prueba · «Deja de X si quieres Y» · «La forma fácil de X sin Z» · romper una creencia · historia personal · «Si eres [perfil], lee esto» · promesa en tiempo corto. Evitar «Presentamos», «Descubre», «¿Estás buscando…?».
- [E] **Segmentar con el copy:** nombrar el perfil («Si tienes un negocio…», «dueño/gerente») y una palabra de identidad en el titular. Escribir con la voz de la audiencia.
- [E] Marco PAS (corto) o 5 pasos: audiencia, problema, solución, quitar 1 a 2 objeciones, CTA. Objeciones típicas de un taller [I]: «no soy técnico», «no tengo tiempo», «ya probé y no sirve», «¿vale la pena el precio?».
- [E] Urgencia y escasez solo reales: fecha límite, cupo numérico, razón del precio de lanzamiento. Sin falsa urgencia ni estadísticas sin respaldo.
- [E] Sin patrones «de IA»: «No es X, es Y», listas de negación, «Di adiós a», «Desbloquea el poder», «¿El resultado?». Sin afirmar atributos personales ni clickbait.
- [E] CTA en frío: «Registrarse» o «Más información» según la fuente; una oferta, una CTA. (El skill de contenido prohíbe «Más info»: usar «Registrarse».)
- [E] Especificidad > vaguedad («ahorra 5 horas a la semana» solo si es verdad), beneficios > funciones.
- Cifras de ahorro como «3 horas a 10 minutos» **no se usan sin un caso medido**: se descartaron por no verificadas.

## 5. Políticas de Meta (verificadas el 2026-10-07)
- **Funcionalidad inexistente [V]:** no mostrar elementos que parecen funcionar y no funcionan (ejemplo oficial: botón de reproducir que no reproduce). La política de spam prohíbe imitar funciones de la plataforma (encuestas, botón de «me gusta», botón de reproducir). Aplicado por criterio propio [I]: sin botones CTA dibujados, sin opciones A/B/C que parezcan encuesta, sin notificaciones ni chats imitados. La CTA es la de Meta.
- **Atributos personales [V]:** no afirmar ni insinuar atributos personales del espectador, incluida situación financiera vulnerable. Hablar de la empresa y del riesgo, no de la persona.
- Sin garantizar resultados.
- Imágenes de IA: Meta puede etiquetarlas [advertencia del repo, no verificada]; no usarlas para mostrar eventos reales.

## 6. Marca y consistencia
- Misma identidad en web, documentos, anuncios y redes: la consistencia construye confianza [F: Pixavas, Walker Advertising, citados en el archivo de abogados].
- El anuncio y su landing deben compartir promesa, precio y fecha (criterio 10 de la rúbrica).

## Origen
- `contenido-higgsfield/taller_prompting/meta_ads_reglas.md` (B, C).
- `contenido-higgsfield/taller_prompting/diseno_vectorial_reglas.md` (§b, §d).
- `contenido-higgsfield/taller_prompting/BASE_CONOCIMIENTO_ADS.md` (§2).
- `contenido-higgsfield/taller_prompting/higgsfield_meta_ads_nativo.md` (§2.1, §2.6, §2.7).
- `contenido-higgsfield/fagal/DISENO_ANUNCIOS_ABOGADOS.md` (sección «Reglas de creativo de Meta verificadas»).
- `contenido-higgsfield/taller_prompting/COPYS_TODOS_LOS_JUEGOS.md` (notas de honestidad).
