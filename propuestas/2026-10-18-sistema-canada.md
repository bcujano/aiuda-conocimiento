# Propuesta · Sistema Canadá: fuentes oficiales de inmigración y lecciones de plataforma

Sesión: SISTEMA-CANADA, 2026-10-18. Sin claves ni datos de clientes.

## 1. Qué aprendí
1. IRCC publica las rondas de Express Entry en un JSON oficial y estable:
   `https://www.canada.ca/content/dam/ircc/documents/json/ee_rounds_123_en.json` (claves `classes` y `rounds`; cada ronda
   trae `drawNumber`, `drawDate`, `drawName`, `drawSize`, `drawCRS`, `drawCutOff`, `drawDistributionAsOn`, `dd1`–`dd18`).
   Se lee sin IA. Desde un contenedor de Claude en la nube `curl` recibe respuesta vacía; con otros clientes carga.
2. El 3-nov-2026 cambia Express Entry: vuelven los puntos por oferta de empleo en ocupaciones de salario alto (50/70/100)
   y por experiencia canadiense en esas ocupaciones (20/40/70), sin LMIA. Anuncio oficial del 16-oct-2026.
   Lección general: **las reglas de dominio regulado se guardan con vigencia desde/hasta**, porque se anuncian antes de regir.
3. Vercel Hobby prohíbe el uso comercial (incluso promocionar un servicio pagado). Cualquier sistema de Aiuda que cobre
   necesita Vercel Pro (US$20/mes) o un proveedor que permita uso comercial gratis.
4. IRPA art. 91 (Canadá): solo abogados, notarios de Quebec, paralegales y RCIC (CICC) pueden asesorar o representar por pago
   en inmigración. Una plataforma pagada debe limitarse a información y organización y aliarse con RCIC.

## 2. Evidencia
- Feed leído el 2026-10-18: última ronda #450 (2026-10-16, francés, 5.000, CRS 435).
- https://www.canada.ca/en/immigration-refugees-citizenship/news/2026/10/changes-to-express-entry-for-high-wage-occupations.html (leída 2026-10-18).
- https://vercel.com/docs/limits/fair-use-guidelines (vía búsqueda, 2026-10-18).
- Página de IRCC «Use of representatives: Who can act as a representative» (vía búsqueda, 2026-10-18).

## 3. Dónde aplica
- 1, 2 y 4: SISTEMA-CANADA; skill nuevo sugerido `aiuda-inmigracion-canada` cuando el catálogo esté verificado.
- 2 (reglas con vigencia): `aiuda-reglas-producto` §2, como regla transversal para normativa (IVA, LOPDP, tarifas).
- 3: `aiuda-repos-utiles` o `aiuda-seguridad` §Entornos (costos reales de producción).

## 4. Cambio sugerido
En `aiuda-reglas-producto` §2, agregar fila:
«**Normas con vigencia:** toda regla legal o tarifa que el sistema aplica se guarda con `vigente_desde`, `vigente_hasta`,
fuente oficial y fecha de verificación; el cálculo recibe la fecha de referencia. Aplica a: SISTEMA-CANADA; recomendada en todos.»

En `aiuda-seguridad` §Entornos, agregar: «Vercel Hobby no permite uso comercial: un sistema que cobra va en Vercel Pro.»

## 5. Qué contradice
Nada de lo vigente. Complementa la decisión del CRM «Supabase Pro cuando se venda» con su par de Vercel.
