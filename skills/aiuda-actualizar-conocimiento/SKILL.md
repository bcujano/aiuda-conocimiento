---
name: aiuda-actualizar-conocimiento
description: Cómo proponer, revisar y actualizar el centro de conocimiento de Aiuda. Usar cuando una sesión aprenda algo reutilizable, descubra una regla nueva, encuentre un error en un skill o vea que un skill está desactualizado.
---

# Actualizar el centro de conocimiento

Revisado: 2026-10-11 · Responsable: dueño de Aiuda · Fuente de verdad: este repo (los demás repos reciben una copia).

## Principio
El conocimiento compartido vive en **un solo repo** (el centro de conocimiento). Los demás repos reciben una copia. Por eso **nunca se edita un skill directamente dentro de un repo de sistema**: se propone el cambio en el centro.

## Cuándo proponer
- Aprendiste una regla, patrón o restricción que otra sesión necesitará.
- Un skill dice algo que ya no es cierto o choca con el código real.
- Descubriste un repo, proveedor, norma o competidor relevante.
- Una tarea se repite y merece su propio skill.

## Cómo proponer
Crea `propuestas/AAAA-MM-DD-tema.md` en el repo del centro (en una rama, con PR) con:
1. **Qué aprendí** (una o dos frases).
2. **Evidencia** (ruta de archivo, enlace con fecha de lectura, resultado de una prueba).
3. **Dónde aplica** (qué repos o skills).
4. **Cambio sugerido** (texto exacto para el skill).
Si no puedes abrir el PR, entrega el texto al dueño en tu reporte.

## Quién revisa
El auditor revisa la evidencia y la redacción. El dueño aprueba y une el PR. Al unir, se actualiza la fecha «Revisado» del skill y el `CHANGELOG.md`.

## Reglas de calidad
- Cada regla sale de un archivo, una fuente con enlace y fecha, o una decisión del dueño registrada. **Nada inventado.**
- Cada skill: descripción clara de **qué hace y cuándo usarlo**, cuerpo conciso, detalle en `reference/`, sección de origen.
- Sin secretos, tokens, teléfonos ni datos de clientes.
- Revisión de todos los skills cada trimestre y cuando cambie una norma.
