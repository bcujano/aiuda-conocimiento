# Traducción de herramientas internas a lenguaje de cliente

| Tecnología interna | Cómo se lo decimos al cliente |
|---|---|
| Chatwoot | Centro de conversaciones con varias líneas de WhatsApp (una bandeja por número) |
| n8n | Automatizaciones de fondo que trabajan todo el día |
| Supabase | Base de datos y archivos de tu empresa (tu información es tuya) |
| OpenAI (gpt-4.1, gpt-4.1-mini, Vision, Whisper) | Inteligencia artificial que redacta, analiza, mira imágenes y entiende notas de voz |
| Retell AI | Asistente de voz con IA |
| Twilio y LiveKit | Línea telefónica del asistente |
| Higgsfield | Estudio de imagen y video con IA, con la imagen de tu marca |
| Gemini / Imagen | Respaldo de imágenes con IA |
| Vercel | Plataforma alojada y siempre disponible |
| Railway (servicio `postpro-321`) | Servidor del motor de contenido |
| Meta Graph API / Marketing API | Conexión oficial con Facebook, Instagram, WhatsApp y su publicidad |
| Meta Pixel y API de Conversiones | Medición de qué anuncio trae clientes que compran |
| WhatsApp Cloud API | WhatsApp oficial de empresa |
| PayPhone | Cobro con tarjeta dentro del curso |
| Google Calendar y Gmail | Tu calendario y tu correo, conectados |
| Google Sheets y Drive | Hojas y carpetas existentes (en retiro a favor del CRM) |
| opentype.js, resvg y sharp | Motor propio de diseño de piezas |
| pdfkit, jsPDF, docx y pptxgenjs | Generación de PDF, Word, PowerPoint y ebooks |
| ffmpeg | Edición automática de video |
| Catastro del Municipio y SRI | Datos oficiales de predios y empresas |
| Postgres con memoria del agente | Memoria de cada conversación |

---

## Reglas de uso
- **Decimos** lo que hace y lo que ganas: «un centro de conversaciones con varias líneas de WhatsApp, varios asesores y un agente que responde, califica y agenda».
- **No decimos** nombres de herramientas internas, de proveedores de IA ni de código abierto en la venta, las propuestas, los textos de pantalla y los anuncios.
- Cada pantalla del sistema debe pasar por esta tabla (tarea de la Ruta, fase de marca blanca).

## Una advertencia importante: lenguaje comercial frente a documentos legales
Que el cliente no vea el motor en la venta **no significa ocultarlo en los documentos legales**. La norma de IA de la SPDP exige informar de forma clara el tratamiento y el carácter automatizado, y las resoluciones de la SPDP sobre cláusulas de contratos y transferencias piden identificar a los encargados y subencargados que reciben datos personales. En la práctica:
- **En ventas y pantallas:** lenguaje de función, sin marcas.
- **En el contrato de encargo y en la política de privacidad:** la lista de proveedores que reciben o procesan datos personales (por ejemplo los de inteligencia artificial, mensajería, voz, alojamiento y pagos), con país y finalidad.
- Un programa abierto que Aiuda ejecuta en su propio servidor no es por sí mismo un tercero que reciba los datos; sí lo es el proveedor donde se aloja.

Esta es una **lectura nuestra**, no asesoría legal: debe confirmarla un abogado de protección de datos antes de redactar los documentos.
