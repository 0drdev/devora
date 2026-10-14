# Proposal

## Why

Existe demanda de convertir documentos confidenciales (PDF, Word, PowerPoint y otros) a Markdown para reutilizarlos en modelos o agentes de IA, sin exponerlos a bases de datos ni a servicios que los retengan. Hoy no existe en este proyecto una herramienta propia que haga esa conversión de forma accesible, verificable y efímera.

## What Changes

- Nueva herramienta web que recibe documentos cargados por el usuario y los convierte a Markdown usando `microsoft/markitdown` localmente en el servidor.
- Flujo mínimo: cargar archivo → presionar convertir → ver Markdown → copiar y descargar. Sin cuentas, sin persistencia en base de datos.
- Procesamiento efímero: archivos y resultados viven solo en memoria/filesystem temporal durante la sesión y se purgan al convertir/descartar/expirar.
- Cobertura amplia de Markitdown (no solo PDF/DOCX/PPTX): p. ej. PDF, DOCX, PPTX, XLSX/CSV, imágenes con OCR/alt-text, audio/transcripción, HTML, texto plano, y otros que Markitdown soporte; con matriz explícita de formatos y límites.
- Énfasis en fidelidad: preservar texto, jerarquía de encabezados, tablas, listas, enlaces e imágenes/texto alternativo; reportar advertencias cuando algo no sea convertible en lugar de perderlo en silencio.
- Accesibilidad completa (teclado, lector de pantalla, contraste, foco, estados de carga/error) y robustez (validación, límites de tamaño/tipo, manejo de archivos corruptos o protegidos).
- Base Python web simple (decidido con el usuario), documentada, testeada y verificada en local, con paridad replicable en un despliegue gratuito por definir en diseño (Vercel vs Render vs Cloudflare, con comparativa de cuotas).
- Gobernanza de decisiones: ningún supuesto material se implementa sin verificación del usuario; checkpoints explícitos antes de fijar stack de despliegue, límites y criterios de fidelidad.

## Capabilities

### New Capabilities

- `document-conversion`: ingesta de documentos y conversión fiel a Markdown mediante Markitdown, con matriz de formatos, límites, preservación de estructura y reporte de pérdidas/advertencias.
- `ephemeral-privacy`: garantías de confidencialidad efímera — sin base de datos, retención solo temporal en memoria/disco efímero, purga determinista, sin telemetría de contenido y mensajes de privacidad verificables.
- `accessible-converter-ui`: interfaz web accesible y robusta para cargar, convertir, previsualizar, copiar y descargar Markdown, con estados, errores comprensibles y operación solo por teclado y lector de pantalla.

### Modified Capabilities

- Ninguna (proyecto greenfield, sin specs previas en `openspec/specs/`).

## Impact

- Código nuevo: aplicación web Python + frontend (sin framework pesado), dependencia `markitdown` y sus extras (OCR, transcripción, ofimática).
- Sin base de datos ni almacenamiento persistente; solo almacenamiento temporal del runtime.
- Nuevos docs: guía local (instalación, verificación, tests), matriz de fidelidad por formato y guía de despliegue gratuito con paridad local/prod.
- Riesgos/dependencias: Markitdown y sus binarios/modelos (p. ej. OCR), límites de memoria/tiempo en planes gratuitos, archivos protegidos o escaneados de baja calidad que reducen fidelidad.
