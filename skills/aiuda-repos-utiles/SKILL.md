---
name: aiuda-repos-utiles
description: Biblioteca de repositorios de código abierto ya evaluados por Aiuda, con licencia y riesgo. Usar antes de construir algo desde cero, antes de integrar una librería o servicio externo, o cuando se pregunte por herramientas para WhatsApp, voz, agentes, privacidad, facturación, mapas, documentos o academia.
---

# Repositorios útiles

Revisado: 2026-10-11 · Responsable: dueño de Aiuda · Fuente de verdad: este repo (los demás repos reciben una copia).

## Regla
**Antes de construir algo, revisa si ya hay un repo evaluado** en `reference/repos.md` (45 repos en 12 categorías, con qué son, utilidad, licencia y riesgo).

## Antes de usar cualquier repo, comprobar
1. **Licencia** leída en el archivo LICENSE, no solo la etiqueta. MIT, Apache y BSD sirven para SaaS. AGPL, GPL y licencias «fair-code» (como la de n8n) o «Sustainable Use» pueden obligar a publicar código o prohibir revender: revisar con el abogado antes.
2. **Actividad:** último commit y si está archivado.
3. **Riesgo de WhatsApp:** los puentes no oficiales (Baileys, whatsapp-web.js, Evolution en modo no oficial) exponen al cliente a bloqueo del número; solo pruebas, nunca producción con clientes.
4. **Datos personales:** si guarda conversaciones o trazas, aplicar `aiuda-cumplimiento-spdp` (enmascarar y limitar retención).
5. **Seguridad:** revisar dependencias y vulnerabilidades antes de integrarlo.

## Los más recomendados
Presidio (enmascarar datos personales) · Langfuse (trazas y costo de IA) · LangGraph (agente como flujo auditable) · Pipecat (voz) · Chatwoot (bandeja con varias líneas) · OpenMeter (consumo) · MapLibre (mapas) · Gotenberg (PDF) · promptfoo (pruebas de agentes) · open-api-facturacion-sri (a auditar).

## Cómo agregar uno nuevo
Con el skill `aiuda-actualizar-conocimiento`: propuesta con licencia, actividad, utilidad y riesgo verificados en la página del repo. No incluir repos sin verificar.
