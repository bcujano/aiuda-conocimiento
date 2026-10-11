# Piezas gráficas (anuncios, carruseles, portadas) · detalle

Fuente de verdad de las reglas: `crm-321/src/lib/vectorial/conocimiento.ts` (`REGLAS_DISENO`, `promptDiseno()`). Documento para personas: `crm-321/docs/16-diseno-vectorial.md`. Si cambia una regla, cambia en el código y en el documento; el motor de contenido recibe una copia exportada (`postpro-321/motor/skills/diseno-piezas.md`, generada: no editarla a mano).

## 1. Las 14 reglas de diseño (el código tiene 14; docs/16 dice 12, el código manda)
1. **Una idea.** Una pieza = una idea = una acción: un titular, una cifra o un precio protagonista, y un solo botón. *El feed se mira en menos de 2 s; dos mensajes compiten.*
2. **Jerarquía de tres niveles.** 1) titular o cifra, 2) precio o dato de apoyo, 3) botón; lo demás, secundario y más pequeño. *Si todo pesa igual no se lee nada.*
3. **Titular corto.** ≤ 9 palabras (máx. 70 caracteres), empieza por el beneficio o un verbo; sin signos de exclamación seguidos ni frases en mayúsculas.
4. **Contraste.** ≥ 4,5:1 texto/fondo (el sistema lo calcula y avisa). Máx. 2 tipografías y 3 colores: fondo, texto y acento.
5. **Sin texto sobre foto.** La foto va sola en su zona; el texto sobre fondo plano (decisión de marca, 2026-10-04).
6. **Zona segura.** Historias y reels (1080×1920): sin texto en el 14 % superior (270 px), el 35 % inferior (672 px) ni el 6 % lateral (65 px). Feed: margen de 76 px a cada lado.
7. **Botón.** Uno solo, con verbo y destino. En este sistema el contacto lo inicia la persona (WhatsApp primero).
8. **Números reales.** Precios, fechas, cupos y días salen de la base; la cifra de impacto lleva su fuente visible; sin fuente no se genera.
9. **Precio.** El publicado es el que paga con tarjeta; el efectivo o la transferencia se presenta como descuento. Nunca la palabra «recargo». (Ver choque con landings en `SKILL.md`.)
10. **Vectorial.** Formas simples, texto convertido a trazados, sin sombras ni efectos de imagen; PNG de 1080 px de ancho para Meta + SVG editable.
11. **Variantes.** 3 titulares distintos × los formatos que se usen, misma estructura, cambiar **una** cosa por prueba.
12. **Estilo.** Usar uno de los 10 estilos de las landings (misma paleta, tipografía y carácter) para que anuncio y página de destino parezcan de la misma marca.
13. **Foco de foto.** Personas ancladas arriba; edificios, productos y espacios al centro. Nunca un flyer con letras como foto.
14. **Idioma.** Español neutro con tildes y ñ, tuteo, sin jerga («tu negocio», no «tu funnel»).

## 2. Formatos (`tipos.ts`)
| Formato | Medidas | Uso | Zona segura sup./inf. | Margen |
|---|---|---|---|---|
| cuadrado | 1080×1080 | publicación de feed | 64 / 64 | 76 |
| vertical | 1080×1350 | feed 4:5 (el que más espacio ocupa) | 72 / 72 | 76 |
| historia | 1080×1920 | Stories y Reels 9:16 | 270 / 672 | 76 (mín. 65) |
| ebook | 1080×1620 | portada 2:3 (ebook, plataformas de venta) | 80 / 90 | 96 |

Meta exige JPG/PNG: el anuncio vectorial se exporta a PNG en servidor. Ventaja: 3 formatos × N titulares al instante, texto nítido, marca consistente.

## 3. Plantillas
| Plantilla | Para qué | Regla propia |
|---|---|---|
| `oferta` | Curso o producto con foto, precio, fecha y botón | Foto sola arriba; nunca letras sobre ella |
| `titular` | Una promesa con tipografía enorme | — |
| `cifra` | Un número que impacta | **Exige `fuente_dato`**; sin ella no se genera |
| `lista` | Hasta 4 beneficios numerados | máx. 8 palabras por punto (regla del redactor IA) |
| `portada` | Portada de ebook o guía (foto arriba sin letras, título, subtítulo, autor) | usa el formato `ebook` |

Etiqueta: máx. 3 palabras. Botón (cta): máx. 4 palabras. Subtítulo ≤ 140 caracteres, titular ≤ 90 al proponer (la regla de 9 palabras/70 caracteres sigue vigente).

## 4. Datos que llevan las piezas
Todo llega como datos, el módulo no sabe de ninguna marca: nombre, colores (#rrggbb), tipografía (`inter`, `fraunces` o `grotesk`), logo claro y logo oscuro (se elige por fondo). Precio ya formateado por el sistema («$79,60»), precio anterior tachado, nota de precio, fecha corta, lugar, foto, cifra y su fuente.
- Fuentes de datos: curso, propiedad, administración Airbnb, producto/servicio del catálogo. Cada una entrega la misma forma (`BaseAnuncio`). Para sumar otra, una rama en `baseAnuncio` y otra en `listarFuentes`.
- Foco: cursos `arriba`; el resto `centro`.
- Marca de la empresa editable (Marketing → Diseño vectorial → Marca); sin ella, un nombre y colores neutros por defecto. Nada de marca escrita en el código.

## 5. Los 10 estilos (`estilos.ts`: paleta, tipografía, decoración y forma de botón)
Mismos ids que las landings. Sin estilo elegido se usan los colores de la marca con tipografía moderna; hay casilla «usar el acento de mi marca».

| Id | Fondo / texto / acento | Decoración · botón |
|---|---|---|
| conversion | #0f172a / #ffffff / #e8501c | círculos · pastilla; titular en mayúsculas |
| lujo | #0b0b0c / #f5efe0 / #d4af37 | filetes dorados · línea |
| corporativo | #0b1b3a / #ffffff / #4f8cff | rejilla · cuadrado |
| aurora | #0a0716 / #f4f1ff / #a78bfa | aurora · pastilla |
| vibrante | #fff1d6 / #1f1147 / #ff5a1f | bloques con sombra dura · duro |
| kraft | #d8bb92 / #1b1410 / #b3202a | papel con cinta · duro; mayúsculas |
| tecnologico | #0b1020 / #e8ecff / #38e0b8 | terminal · cuadrado; letra más chica |
| editorial | #faf7f2 / #1c1917 / #b3202a | filetes de tinta · cuadrado |
| minimalista | #ffffff / #111111 / #2457ff | suizo · cuadrado |
| sereno | #eef3ec / #1c2b22 / #3f7d58 | hojas · pastilla |

Cada estilo ajusta `escala` de letra (condensadas más grandes, monoespaciadas más chicas). Antes de usar un estilo, comprobar el contraste del acento sobre su fondo (calculado aparte: el acento de kraft sobre su fondo da ≈ 3,6:1, por debajo de 4,5; usarlo en elementos grandes, no en texto pequeño).

## 6. Técnica del generador
- Motor determinista (sin IA en el dibujo): `texto.ts` (texto → trazados con opentype.js, letra por letra con kerning acotado), `plantillas.ts` (usa `pila()` para apilar y achicar en bloque, y `bloque()` para texto que achica antes de cortar), `color.ts` (contraste WCAG), `imagen.ts` (logo y foto incrustados; fotos reducidas a 1080 px JPEG; solo `https` público o `public/`), `index.ts` (`componer()` y `aPng()` con resvg).
- **No usar `toPathData` de opentype.js**: genera `NaN` con ciertos decimales y corta el texto; los trazados se serializan a mano.
- Tipografías con licencia abierta (Inter, Fraunces, Space Grotesk y las de los demás estilos). Agregar otra = copiar su TTF a `fuentes/` y registrarla en `texto.ts`.
- Límites: sin ligaduras ni interletraje; foto recortada anclada según `foco`.
- Agregar plantilla/formato: una línea en `FORMATOS`; función en `plantillas.ts` registrada en `DIBUJAR` y en `PLANTILLAS`; validar dentro la regla propia; probar con los scripts de prueba y mirar los PNG a tamaño real.

## 7. Redacción asistida por IA para piezas
- La IA **solo redacta** textos cortos (3 propuestas con ángulos distintos); recibe `promptDiseno()` en su mensaje de sistema.
- Si el texto trae montos (`$`, USD, %) o la palabra «recargo», se **descarta** y se avisa. Precios, fechas, cupos y porcentajes los pone el sistema.
- No prometer resultados garantizados. Costo mostrado antes de gastar, con tope de salida y registro en el uso de IA.

## 8. Carrusel y piezas guardadas
Carrusel: una lámina por línea (`titular | subtítulo`), misma marca y estilo, numeradas «1/N», botón en la última; formatos cuadrado y vertical. Las piezas generadas se guardan (PNG + SVG) con un índice de las 200 últimas. Para la estructura narrativa del carrusel ver skill `aiuda-contenido-y-voz`.

## 9. Ebooks (4 niveles)
| Nivel | Incluye |
|---|---|
| 1 Básico | Portada tipográfica vectorial, índice con páginas reales, un capítulo por módulo, sobre el autor, siguiente paso (sin IA) |
| 2 Estándar | + portada con foto (sin letras encima), bienvenida y cierre, por capítulo: idea clave, resumen, lista de verificación y reflexión |
| 3 Pro | + recorrido y 3 cifras reales de la malla, proceso en pasos, comparación sin/con el método, ejercicio con renglones, plantilla imprimible, glosario |
| 4 Premium | + portadilla, página legal, «Cómo usar», apertura de capítulos, bonos, página de autor con foto, contraportada; 5 archivos: PDF de lectura, PDF 6×9 in para KDP, cubierta completa KDP (ancho = 2×6 in + lomo páginas×0,002252 in + sangrado), EPUB 3, portada 2:3 de 1600×2400 y mockup 1080×1080 |

- Página de 400×600 pt (2:3), cómoda en celular; tipografías incrustadas y texto seleccionable.
- Redacción IA desde el nivel 2: usa solo lo que dice el curso, sin cifras, precios ni promesas; descarta lo que traiga montos.
- El costo de IA se muestra **antes** de generar (se envía un tope y el servidor se niega si el costo real lo supera). Vista previa sin IA ni archivos; el borrador se paga una vez.
- Autor por defecto: el facilitador del curso; solo el superadmin pone autores personalizados y logos propios.
- Ficha de venta (título, subtítulo, descripción, 7 palabras clave, categorías); el precio lo decide la persona.
- Pendiente según la fuente: verificar EPUB y PDF en lectores reales y a 390 px.

## Origen
`crm-321/src/lib/vectorial/conocimiento.ts`, `tipos.ts`, `estilos.ts`, `ia.ts`; `crm-321/src/lib/marketing/base-anuncio.ts`, `piezas.ts`; `crm-321/docs/16-diseno-vectorial.md`, `18-ebooks.md`, `14-diseno-landings.md` (§5, §2d); `crm-321/src/lib/lecturas-vectorial.ts`; `postpro-321/motor/skills/diseno-piezas.md`. El ≈ 3,6:1 de kraft es un cálculo propio (WCAG) sobre los colores de `estilos.ts`, no una cifra de las fuentes.
