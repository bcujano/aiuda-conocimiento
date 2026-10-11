---
name: aiuda-arquitectura-modulos
description: Arquitectura de Aiuda: un núcleo y módulos que se enchufan como breakers, con multicliente y marca por cliente. Usar al diseñar o cambiar un módulo, una tabla de cliente, una integración, un precio por módulo o al parametrizar algo que está fijo a un cliente, ciudad o marca.
---

# Núcleo y módulos

Revisado: 2026-10-11 · Responsable: dueño de Aiuda · Fuente de verdad: este repo (los demás repos reciben una copia).

## Idea
Un **núcleo** común (la caja de breakers) y **módulos** que se encienden por cliente, se venden por separado y comparten los datos del cliente. Cada cliente recibe «Aiuda de {cliente}».

## El núcleo contiene
Organizaciones y usuarios aislados por `tenant_id` con reglas por fila · roles y permisos por módulo · suscripciones, módulos activos y medidor de consumo · marca y textos del cliente (datos, no código) · registro de módulos y bus de eventos · agente de IA con contexto de todos los módulos · métricas por cliente y módulo · auditoría, copias de seguridad y observabilidad de costos · **controles de cumplimiento comunes** (consentimiento, baja, derechos del titular, registro de decisiones de IA, enmascarado, retención).

## Contrato de módulo (todo módulo declara)
id, versión y precio (fijo y consumo) · tablas propias, todas con `tenant_id` · eventos que emite y consume (ej. `lead.creado`) · permisos que necesita · rutas de interfaz y entradas de menú · qué se configura por cliente (marca, textos, claves) · sus evaluaciones de impacto y su fila en el RAT si usa IA.

## Decisiones vigentes
- **Monolito modular** en un monorepo (`packages/core`, `packages/modulos/*`), no microservicios.
- **Un cliente = una organización**; todo texto, precio y número vive en la base o en variables de entorno, nunca en el código.
- **Capa de modelos de IA intercambiable**: un adaptador por proveedor, con respaldo.
- **Cobrar el consumo de IA con margen** y con tope de gasto por cliente.
- Una función en un solo lugar (clasificación, precios, agente leen de una fuente única).
- El núcleo parte de `aiuda-empresas`, que ya es multicliente (decisión pendiente de aprobar).

## Qué no se deja fijo en el código
Marca, ciudad y municipio, moneda, IVA y normativa, teléfonos, dominios, identificadores de cuentas, textos legales. Ver `reference/parametrizar.md`.
