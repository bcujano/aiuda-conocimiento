# Qué separar o parametrizar para otra empresa

`CLAUDE.md` ("Producto replicable") declara el objetivo, pero hoy el producto de INMO es de una sola empresa (sin `organizacion_id`; solo Academy tiene `organizaciones`). El patrón destino está en `/home/user/bcujano/aiuda-empresas/CLAUDE.md`: un cliente = una organización, y todo texto y número viven en la base.

- **Marca:** "321 Soluciones Inmobiliarias" aparece en 26 archivos (prompts de avalúo y estudio, PDF, cotización, calculadora, documentos); "Byron" en 58. Los PDF, la firma, los pies y los textos de la IA deberían leer una tabla de organización.
- **Ciudad y municipio:** toda la capa municipal es de Quito (`src/lib/geoquito.ts`, `municipio.ts`, `municipio-historico.ts`; validación lat/lon de Quito en `api/municipio/predio/route.ts`; nombres de capas ArcGIS; AIVA, COS y PUOS/PUGS son conceptos de Quito). Otro municipio implica otro adaptador con la misma interfaz. Las listas `ZONAS_QUITO`, `ZONAS_NACIONALES` y las 19 ciudades están en el código.
- **País, normativa y moneda:** USD; formato `es-EC` en 85 archivos; zona horaria `America/Guayaquil` en 42; IVA 15 % fijo en cotización; IESS 9,45 % y jornal de 8 h en nómina; colegio de arquitectos (R.O. 446); SB/COOTAD/Judicatura en avalúos; BCE, INEC (ciudad 170150), SRI, Banco Mundial `ECU`; RSS de medios ecuatorianos; Ecuador en los prompts.
- **Datos comerciales sueltos en código:** teléfonos de WhatsApp y de dirección como valores por defecto (`notificar.ts`, `calculadora-roi`, `catalogo-publico`), dominio `crm.321archlab.com`, ids de Meta/WhatsApp por defecto, URL del motor y de Chatwoot por defecto. Deben pasar a variables de entorno o a la tabla de organización.
- **Base de precios:** CAMICON y su emparejamiento son locales; `sql/042` dice que otra empresa puede cargar su propio presupuesto tipo.
- **Automatizaciones:** `vercel.json` (7 crons), workflows de n8n (IDs, credenciales y URLs de Chatwoot fijas) y una sola cuenta de WhatsApp.
- **Aislamiento:** hay que añadir `organizacion_id` en todas las tablas del INMO y filtrar cada consulta del servidor.
- **Costos por cliente:** tope de IA y Supabase Pro ($25/mes) cuando se venda (G6).

### Reglas de producto A a J y cómo se materializan

| Regla | Qué exige | Cómo se materializa | Evidencia |
|---|---|---|---|
| A. Todo término con ayuda | Cada palabra técnica se define con 4 líneas | `GLOSARIO` de 124 términos; `<Ayuda termino="...">` 126 usos | `src/lib/glosario.ts`, `src/components/Ayuda.tsx` |
| B. Lecturas | Cada pantalla con datos dice qué decisión sale y con qué cruzarla | `lecturas*.ts` por módulo y `<Lecturas>` plegable | `src/lib/lecturas.ts`, `lecturas-mercado.ts`, `lecturas-municipio.ts`, `index-lectura.ts` |
| C. Ningún número lo escribe un LLM | Toda cifra es una cuenta sobre datos con origen | Los motores (`avaluo.ts`, `factibilidad.ts`, `inversion.ts`, `cruces.ts`) no llaman IA; la IA solo redacta | cabeceras de esos archivos |
| D. Lenguaje de usuario | "Los leads sin teléfono", no el nombre del campo | Textos de pantalla y de lecturas | `src/components/*`, `lib/lecturas*.ts` |
| E. Una función, un lugar | Clasificación, precios y agente leen de un solo sitio | `clasificacion.ts`, Catálogo 321, `/api/agente/contexto` | `src/lib/clasificacion.ts`, `unidades.ts`, `anuncios.ts` |
| F. Fuente del dato | Dato 321 con mínimo, luego mercado con enlace, luego "sin dato" | `fuente-dato.ts` más `MINIMOS`; validación de URL citada; lectura directa del BCE | `fuente-dato.ts`, `bce.ts`, `index-mercado/route.ts` |
| G. Notas ≠ Actividad | Notas son resumen; la conversación va a Actividad | `lib/notas-lead.ts`, `api/leads/limpiar-notas` | `src/lib/notas-lead.ts` |
| H. Disco limitado | Escrituras masivas en lote y con pausa | Cargas por lotes de 500 con pausa; histórico sin escribir en base | `scripts/cargar_042.py`, `api/municipio/historico/route.ts` |
| I. Pruebas con sesión real | Cerrar la sesión de prueba y comprobar el dominio | Solo procedimiento en la documentación | `CLAUDE.md`, `docs/10` §5 |
| J. Vista previa solo en cursos no publicados | `?vp=` crea personas reales en uno publicado | Solo regla de proceso y script; no es un control del código | `CLAUDE.md`, `docs/HANDOFF.md` §2 |
