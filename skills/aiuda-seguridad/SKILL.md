---
name: aiuda-seguridad
description: Reglas de seguridad para cualquier sistema de Aiuda: secretos, llaves, aislamiento entre clientes, webhooks, límites de uso, entornos y dependencias. Usar al escribir código con credenciales, rutas públicas, webhooks, consultas a la base de datos, scripts, Docker, CI o despliegues.
---

# Seguridad

Revisado: 2026-10-11 · Responsable: dueño de Aiuda · Fuente de verdad: este repo (los demás repos reciben una copia).
Reglas surgidas de la auditoría del 2026-10-11 de 6 repos.

## Secretos
- **Nunca** una llave, token o contraseña en el código, en documentos, en JSON de automatizaciones ni en scripts. Todo va por variables de entorno y se guarda en la bóveda del dueño.
- Cada repo tiene `.env.example` con **todos** los nombres de variables y su explicación, sin valores.
- Si aparece un secreto en el repo: reportar solo la ruta, rotar la credencial, limpiar el historial y activar el escáner de secretos en el CI.
- Rotar tokens de Meta, Chatwoot y llaves de base de datos cuando se sospeche exposición.

## Aislamiento entre clientes
- Toda tabla de cliente lleva `tenant_id` (u `organizacion_id`) y reglas de seguridad por fila.
- Las rutas de cliente usan la identidad del usuario; la llave de servicio solo vive en el servidor y siempre filtra por tenant.
- Cada módulo con datos de cliente tiene pruebas automáticas de aislamiento (un usuario de A no ve B).
- Nunca separar el aislamiento «por convención» sin pruebas.

## Webhooks y rutas públicas
- Todo webhook exige secreto comparado en tiempo constante o firma del proveedor. Sin credencial, no responde.
- Toda ruta pública valida entrada, tiene límite de uso por IP y no devuelve datos internos.
- Los enlaces públicos por token deben poder revocarse y rotarse.
- CORS cerrado a orígenes explícitos; sin `ALLOWALL` ni `frame-ancestors *`.
- Los pagos: monto validado en el servidor contra el plan, firma del webhook, idempotencia y reembolsos.

## Entornos
- Pruebas y producción en bases distintas. **Las pruebas nunca escriben en producción.**
- No usar planes gratuitos para producción (el plan gratis de la base se cayó por límite de disco).
- Sin modo «desarrollo» que acepte cualquier credencial si falta una variable: fallar al arrancar.

## Dependencias y despliegue
- Versiones fijadas (lockfile). Nada de `curl | sh` sin versión ni checksum.
- Contenedores sin root, con healthcheck.
- CI con tipos, estilo, pruebas y escaneo de secretos en cada cambio.
- Registros sin datos personales innecesarios; `console.log` y `print` no vuelcan cuerpos completos de peticiones.

## Cumplimiento
Para datos personales e IA, aplicar también `aiuda-cumplimiento-spdp`.
