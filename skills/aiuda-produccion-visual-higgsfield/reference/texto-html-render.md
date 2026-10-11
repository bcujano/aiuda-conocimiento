# Texto en HTML/CSS y render a imagen · detalle

USO INTERNO. Método tomado de los scripts `render_*.py`, `poster_*.py` y de `BASE_CONOCIMIENTO_ADS.md`.

## 1. Por qué
- El texto dentro de una imagen generada sale con errores (palabras rotas, tildes mal, letras inventadas) y cada ronda de «arreglar un texto» rompe otro. En HTML la ortografía es exacta, las tildes y la ñ salen bien y no hay reintentos pagados.
- Fuente externa que lo respalda: Simo-Dax/claude-code-creative-statics (HTML/CSS por defecto; generar la imagen sin texto, logo ni CTA y componer encima; «casi siempre gana cuando el copy importa»). Otros repos hacen lo contrario (texto dentro de GPT Image) y piden verificar defectos de render. La decisión del proyecto fue la determinista.

## 2. Método
1. Una función por plantilla (HTML + CSS + SVG) que recibe segmento, titular, foto y fase de precio. Sin lógica de marca escrita en la plantilla más allá de paleta y fuentes del juego.
2. La foto va de fondo con `cover` y una posición de enfoque; el texto se maqueta encima, o al lado si la regla de diseño lo pide (ver contradicción 1 en las decisiones).
3. Render con Chrome sin interfaz (headless): `--window-size=1080,<alto>`, `--virtual-time-budget` (se usó 12000) para esperar las fuentes y `--screenshot=salida.png`. Requiere internet si las fuentes vienen de Google Fonts; esperar `document.fonts.ready` antes de capturar.
4. Se renderiza un maestro por formato: 4:5 = 1080×1350 y 9:16 = 1080×1920 (el despacho de abogados exportó a 1440×1800, 1440×2560 y 1440×1440; los vectores no gastan créditos, no hace falta ampliar con IA).
5. Los HTML temporales (`_*.html`) son ignorables.
6. Fases (de precio, de fecha): una variable de entorno `FASE` cambia el resaltado y las etiquetas. Para una fase nueva se agrega el caso en el mapeo y se vuelve a renderizar. El script se edita; la imagen no.

## 3. Medidas (lienzo de 1080 de ancho)
- Titular: 100 a 170 px (mínimo ~64 px según `meta_ads_reglas.md`); subtítulo 52 a 64; cuerpo y chips 36 a 44; microtexto mínimo 30 a 32. Texto secundario ≥ 30 px, titulares ≥ 64 px.
- Margen 4:5: 84 px a los lados y 96 px arriba y abajo (inferencia del repo). 9:16: libres ~250 px arriba y ~340 px abajo (diseno_vectorial_reglas.md).
- Escala de precios: siempre visible, con la fase vigente resaltada.
- Máximo 2 familias tipográficas, color 60-30-10 con un solo acento, nunca #000 ni #FFF puros (tintar). Grano SVG `feTurbulence baseFrequency .8 numOctaves 3` a 5-9 % en overlay, sombras en capas, bordes de 1 px.
- Probar la pieza a 375 px de ancho (se ve en celular).

## 4. Formatos «pantalla» (nota de iPhone, chat de WhatsApp, tweet, ticket)
Se hacen 100 % en HTML (texto exacto en español). Soul solo aporta la foto (avatar, adjunto). Aviso del despacho de abogados: **no dibujar elementos que parezcan funcionar y no funcionen** (botones CTA dibujados, opciones A/B/C que parezcan encuesta, notificaciones o chats imitados): la política de Meta lo trata como funcionalidad inexistente o spam. Ver `aiuda-meta-ads-reglas` §políticas.

## 5. Zona segura 9:16: tres cifras en el repo
`meta_ads_reglas.md`: 250 px (15 %) arriba y 20 % abajo. `diseno_vectorial_reglas.md`: 250 arriba y 340 abajo. Guía oficial citada en `fagal/`: ~14 % arriba, 35 % abajo y 6 % a los lados. Para Reels se usa la oficial (la más estricta). Ver contradicción en `aiuda-meta-ads-reglas`.

## 6. Dependencias del entorno de origen
Windows, Chrome en ruta fija, Python con Pillow y numpy. Algunos scripts tienen rutas absolutas del equipo del dueño (carpetas temporales de otra máquina) y no corren en otra PC sin editar. Al reutilizar: parametrizar la ruta del navegador y de las fuentes.

## Origen
- `contenido-higgsfield/taller_prompting/ads_nativo/render_set3.py`, `render_vector.py`, `render_ads.py`, `render_ads2.py`, `render_set4.py`.
- `contenido-higgsfield/taller_prompting/poster_taller.py`, `poster_taller_v3.py`, `poster_formatos.py`.
- `contenido-higgsfield/fagal/ads_final/render_final.py`, `fagal/ads_v3/render_v3.py`.
- `contenido-higgsfield/taller_prompting/BASE_CONOCIMIENTO_ADS.md` (§2), `diseno_vectorial_reglas.md`, `meta_ads_reglas.md`, `higgsfield_meta_ads_nativo.md` (§2.4).
