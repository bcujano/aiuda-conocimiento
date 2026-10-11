# Contradicciones abiertas (decide el dueño)
Detectadas al escribir los skills. Mientras no se decidan, cada skill indica qué regla aplicar.

1. **Precio en landings vs. anuncios:** RESUELTO 2026-10-11 por Byron: el precio grande es el de efectivo o transferencia en todo. Falta alinear el código de anuncios.
2. **Divulgación de IA:** varios repos mandan no decir que es IA o decirlo solo si preguntan. RESUELTO 2026-10-11 por Byron: cumplir sin decir «IA» ni «robot». Regla vigente: primer mensaje «asistente virtual automático» + oferta de persona; nunca negarlo si preguntan de frente (ver `aiuda-agentes-whatsapp` §1 y §13). La prueba `workflow-laundry-agente.test.ts` (laundry-vip) exige el texto prohibido y debe cambiarse.
3. **«Nunca escribimos primero»:** absoluta en Academy y aiuda-empresas; crm-321 envía seguimientos con plantilla fuera de ventana. RESUELTO 2026-10-11 por Byron: permitido en crm-321 por su secuencia de seguimiento automático.
4. **Tope de IA mensual:** docs dice $20, código $50. Manda el código.
5. **Texto sobre imagen:** prohibido en piezas estáticas; el plan de reels lo usa en video. Se aplicó la distinción estático/video (interpretación, no escrita).
6. **«Desde $»:** permitido con precio mínimo en ficha; el plan de octubre lo excluye.
7. **Tipografías y mayúsculas:** los estilos Alta conversión y Kraft rompen «máx. 2 tipografías / sin mayúsculas».
8. **Sin verificar:** categoría HOUSING en anuncios de Ecuador, texto de la Ley de Corredores, ordenanza de valoración de Quito, registro de «no llamar».
9. **Vacíos:** sin sistema de diseño común, sin política de privacidad/términos, sin política de retención de conversaciones, sin contratos con encargados, sin evaluación de impacto, sin CI en crm-321, aiuda-empresas, adsboom ni postpro-321.
