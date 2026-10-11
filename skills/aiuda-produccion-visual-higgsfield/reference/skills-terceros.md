# Skills de terceros de Higgsfield · cuándo usarlos

Los 8 skills de `.claude/skills/higgsfield-*` (copia espejo en `.agents/skills/`, idéntica según `diff`) son de **higgsfield-ai/skills** (GitHub). **No se copian al centro de conocimiento**: se instalan desde su origen en cada repo. `skills-lock.json` (formato `version: 1`) fija la fuente y el hash calculado de cada `SKILL.md`; el encabezado de cada skill declara `version: 0.12.0`.

| Skill | Hash fijado en `skills-lock.json` (`computedHash` del SKILL.md) |
|---|---|
| higgsfield-brandkit | ffd4e3cee9cec37783b60181090dee3385a833f98cef734919124b2d6f418402 |
| higgsfield-generate | 270c7f8a6067835f9ca0745fa3ad575b067b23cf9a2b7b9c53dae99c00b4b8e7 |
| higgsfield-marketplace-cards | dffdd858efc72915e4d9f600626912180e6b9b40a4c745a28d3099ea88c0dfeb |
| higgsfield-product-photoshoot | 5dd5a272025e954acbb9beb477a6a1c9200ce4e8155ab8ba8cfe13f444d0da64 |
| higgsfield-soul-id | ca60c249db297868051996295d23c24b2477bea78a7dac06401639183ee38fb5 |
| higgsfield-video-explainer | 8e240a9803b998ddb82ba5cea0a9706ecac7cbac75fc5ac98f57fa05fe229e2b |
| higgsfield-websites | 4ca0618c6015bf18983a9edd16775e0ef7f180ee44ea451961864beba8399915 |
| higgsfield-youtube-thumbnail | f549199d92da66913a1f7987ba812a51b40515b001def50c22252531215d43a9 |

Si el hash de un skill instalado no coincide con esta tabla, el skill cambió: leerlo antes de usarlo y avisar al dueño del centro (una actualización puede cambiar defectos de modelo o de costo).

## Cuándo usar cada uno (según la descripción de cada skill; no se probaron todos en este proyecto)
| Skill | Úsalo para | No lo uses para |
|---|---|---|
| `higgsfield-soul-id` | Entrenar el Soul (modelo de la cara) de una persona, una sola vez. Solo con autorización de la persona. | Cambios de cara de una sola vez |
| `higgsfield-generate` | Generar imágenes, video, 3D o audio; Marketing Studio; análisis de viralidad. Encadenar con `soul-id` para identidad. Es el skill de uso diario. | Entrenar Soul, kits de marca, miniaturas, explainers, juegos |
| `higgsfield-brandkit` | Sistema visual de marca: paleta, logo SVG, tipografía, mockups, brandbook PDF/PPTX. Conserva los archivos oficiales del cliente. | Anuncios sueltos |
| `higgsfield-product-photoshoot` | Fotos de producto y creativos de anuncio de producto con prompt asistido. | Escenas sin producto, avatares |
| `higgsfield-marketplace-cards` | Tarjetas de producto para marketplaces con requisitos de cumplimiento. | Fotografía de marca genérica |
| `higgsfield-youtube-thumbnail` | Miniaturas de YouTube y portadas verticales. | Anuncios de Meta |
| `higgsfield-video-explainer` | Video explicativo narrado, sin personas reales, en bloques de 10 s. | Anuncios con personas, UGC, cabeza parlante |
| `higgsfield-websites` | Sitios, apps y juegos desplegados en la plataforma de Higgsfield. | Landings del CRM propio (ver `aiuda-diseno`) |

En el proyecto de origen los anuncios de Meta **no** se hicieron con estos skills: se usaron directamente las herramientas de Higgsfield (`soul_2`, `gpt_image_2_5`, lote de imágenes) y scripts propios de maquetación. Los skills son de apoyo cuando la tarea cae en su descripción.

## Choques entre estos skills y las reglas de AIUDA
1. `higgsfield-generate` dice «No pre-estimar costos ni optimizar por modelo más barato salvo que el usuario lo pida» (línea 48 de su SKILL.md). **Regla AIUDA:** costo y una prueba antes de cualquier lote.
2. `higgsfield-generate` elige GPT Image 2.5 por defecto para «imagen, diseño y texto». **Regla AIUDA:** el texto del anuncio va en HTML, nunca dentro de la imagen.
3. `higgsfield-generate` permite crear un Soul Character automático en modos UGC de Marketing Studio cuando el brief menciona una persona. **Regla AIUDA:** personas solo con el Soul del dueño o de la persona autorizada; no se inventan presentadores (ver `aiuda-contenido-y-voz`: único personaje).
4. `higgsfield-product-photoshoot` dice que el backend arma el prompt final y «nunca se escribe libremente». Para escenas de personas con Soul, el prompt de este centro (`soul-y-fotos.md`) manda.

## No verificado
- Que el hash de `skills-lock.json` corresponda al `SKILL.md` actual en GitHub: no se comprobó contra el origen.
- Cuáles de estos skills conviene instalar en repos de clientes: ninguno se evaluó para clientes finales.

## Origen
- `contenido-higgsfield/skills-lock.json`.
- `contenido-higgsfield/.claude/skills/higgsfield-*/SKILL.md` (encabezado y descripción; líneas 17-18, 48, 83-89, 174, 217 de `higgsfield-generate/SKILL.md`).
- `contenido-higgsfield/.agents/skills/` (espejo).
