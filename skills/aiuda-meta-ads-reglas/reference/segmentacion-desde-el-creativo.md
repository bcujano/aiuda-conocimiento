# Segmentar desde el creativo (sin audiencias) · detalle

Decisión del dueño (2026-10-07): nada de audiencias inventadas ni listas. La campaña va abierta (solo país) y cada anuncio se segmenta a sí mismo por lo que dice y lo que muestra. Método tomado del trabajo con un despacho de abogados cliente; sirve para cualquier negocio.

## 1. Qué dicen las fuentes de Meta
| Afirmación | Estado | Fuente |
|---|---|---|
| Andromeda elige, entre millones de anuncios, los miles relevantes para cada persona; más creativos distintos = más opciones para personalizar | Verificado (Meta) | Blog de ingeniería de Meta y noticia de Meta for Business (+8 % de calidad de anuncio) |
| Advantage+ audience toma las selecciones de audiencia «y se expande más allá de ellas» | Verificado (extracto del buscador; la página no cargó completa) | Ayuda de Advantage+ audience |
| Campañas Advantage+ de clientes potenciales: −14 % costo por lead y −10 % por lead calificado (cifras de Meta); menos entradas y menos campañas con distinta segmentación; conectar el CRM por API de Conversiones; ajustes demasiado restrictivos desactivan la automatización | Verificado, cifras autorreportadas | Página de Advantage+ para leads |
| «El creativo ES la segmentación» | Inferencia del equipo, coherente con lo anterior | blogs de terceros |
| «Entity ID» y «similitud > 60 % se suprime» | NO está en la fuente oficial | ver `andromeda-y-pruebas.md` |

## 2. Reglas operativas
1. **Una pieza = un perfil.** En el primer vistazo va la etiqueta del perfil («Para inmobiliarias», «Corredores y aseguradoras», «Para empresas de transporte», «Para pymes»). Nombrar al perfil por su rol y su negocio, **nunca por una condición personal**.
2. **Dolor propio de ese perfil** en el titular (lo que solo esa persona siente) y objeto visual propio (cláusula, reclamo, chat, cartera, flota). Una pieza genérica para todos pierde frente a una específica.
3. **Conceptos realmente distintos** entre sí: ángulo, escena, formato, tipografía. Cambiar color o titular no cuenta.
4. **Campaña:** objetivo de clientes potenciales, Advantage+ audience con solo el país (ciudad solo si el cliente únicamente atiende en una), sin intereses, sin listas, sin similares; ubicaciones automáticas; API de Conversiones conectada al CRM para optimizar a lead calificado y reunión realizada.
5. **Formulario con preguntas de calificación** (giro, tamaño en rangos, problema): lo que Meta no segmenta, lo filtra el formulario y el agente. Meta no tiene filtro de «facturación 20 a 100 mil»; se logra por el mensaje, las preguntas y listas propias.
6. **Medición por pieza:** costo por reunión realizada y por contrato firmado, por concepto y por perfil. Lo que no trae reuniones se pausa.
7. **Políticas:** no afirmar ni insinuar atributos personales; sin garantizar resultados.

## 3. Segmentos para un taller o curso (método usado, [I])
El título del anuncio es «Taller de IA para …» + perfil: emprendedores, dueños de negocio, empresarios, inmobiliarias, atención al cliente, negocios locales, marketing y contenido, gerentes y directores, negocios sin página web. Cada perfil con una foto y una plantilla distintas; el mapa foto → plantilla → segmento vive en un diccionario del script de render.

## 4. Segmentos para servicios B2B (ver `anuncios-b2b-despachos.md`)
Inmobiliarias · seguros y corredores · concesionarias · fraude y estafa (la empresa como afectada) · cobro de dinero · transporte · pymes sin nicho · dueños y gerentes · empresas medianas.

## Origen
- `contenido-higgsfield/fagal/SEGMENTACION_DESDE_EL_CREATIVO.md`.
- `contenido-higgsfield/fagal/INVESTIGACION_FAGAL_B2B.md` (§2, §4).
- `contenido-higgsfield/taller_prompting/LEEME_PRIMERO.md` (§1), `ads_nativo/render_set3.py` (diccionario `ADS`), `COPYS_TODOS_LOS_JUEGOS.md` (juego 2).
