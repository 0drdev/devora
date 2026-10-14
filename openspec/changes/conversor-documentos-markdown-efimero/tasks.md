# Tasks

## 1. Base Python verificada y gobernanza

- [x] 1.1 Crear esqueleto FastAPI + frontend mínimo y verificar con `pytest -q` y arranque local que `/health` responde.
- [x] 1.2 Fijar dependencias `markitdown[all]` con versión pineada y verificar con `pip install -r requirements.txt` reproducible y `markitdown --version`.
- [x] 1.3 Añadir `Dockerfile`, `.dockerignore` y guía `README-local.md`, y verificar construyendo la imagen y ejecutando la guía paso a paso en limpio.
- [x] 1.4 Checkpoint con el usuario: confirmar plataforma gratuita (Render/HF/Vercel-estático), límites iniciales y TTL, y verificar registrando la decisión en el change antes de desplegar.

## 2. Conversión fiel de documentos

- [x] 2.1 Implementar ingesta con matriz de formatos y validación MIME/extensión/tamaño, y verificar con tests que acepta la matriz y rechaza tipos fuera de ella con mensaje claro.
- [x] 2.2 Integrar Markitdown con `convert_stream`, plugins desactivados y sin fetching remoto, y verificar con test que una URL/enlace del documento no dispara descargas.
- [x] 2.3 Implementar preservación de estructura (encabezados, listas, tablas, enlaces, alt-text) y advertencias por elemento no convertible, y verificar con corpus dorado por formato y aserciones estructurales.
- [x] 2.4 Implementar manejo de corruptos/protegidos/sobredimensionados y ZIP con tope de expansión, y verificar con fixtures que fallan en español sin Markdown parcial silencioso.
- [x] 2.5 Implementar copiar al portapapeles y descarga `.md` con nombre derivado, y verificar manualmente que ambas acciones confirman éxito.
- [x] 2.6 Documentar matriz de formatos, límites y taxonomía de advertencias en `docs/fidelidad.md`, y verificar que cada formato del corpus está en la tabla.

## 3. Privacidad efímera y seguridad

- [x] 3.1 Implementar almacenamiento solo temporal por sesión con purga al descargar/descartar/expirar/cerrar, y verificar con tests que tras la purga el contenido ya no es recuperable.
- [x] 3.2 Sanitizar nombres/rutas y aislar la conversión en directorio temporal desechable, y verificar con tests de path traversal y ZIP con expansión excesiva.
- [x] 3.3 Redactar logs y desactivar telemetría de contenido (solo tipo/tamaño/resultado), y verificar inspeccionando logs tras convertir que no hay texto ni Markdown.
- [x] 3.4 Mostrar aviso de procesamiento efímero y confirmación de purga en la UI, y verificar que ambos textos son visibles sin leer el documento.
- [x] 3.5 Auditar ausencia de base de datos y volúmenes persistentes en código, compose y manifiestos de despliegue, y verificar con revisión que no hay conexión ni disco duradero.

## 4. Interfaz accesible y robusta

- [x] 4.1 Maquetar flujo cargar → convertir → revisar → copiar/descargar con HTML semántico en español, foco visible y orden lógico, y verificar el flujo completo solo con teclado.
- [x] 4.2 Añadir etiquetas/roles y anuncios `aria-live` para progreso, éxito, advertencias y errores, y verificar con lector de pantalla (NVDA/VoiceOver) que cada estado se anuncia.
- [x] 4.3 Presentar Markdown crudo y vista previa renderizada con acciones accesibles de copiar/descargar, y verificar que ambas funcionan desde teclado y anuncian confirmación.
- [ ] 4.4 Aplicar contraste, movimiento reducido, responsive y zoom 200% sin pérdida de acciones, y verificar con `axe` sin violaciones críticas más revisión manual a 200% y en móvil.
- [x] 4.5 Redactar estados y errores en español claro sin detalles técnicos ni contenido del documento, y verificar cada escenario de error de las specs muestra el mensaje esperado.
- [x] 4.6 Integrar Tailwind CSS v4 en la UI (compilado y versionado en `static/app.css`) preservando semántica, foco visible y `aria-live`, y verificar con `pytest -q` y nueva corrida de `axe`.

## 5. Verificación integrada y despliegue gratuito

- [x] 5.1 Ejecutar suite completa local (`pytest`, `axe`, corpus de fidelidad y auditoría de no-persistencia) y verificar que todo pasa antes de desplegar.
- [ ] 5.2 Desplegar a la URL gratuita acordada con HTTPS y checklist de paridad local/prod, y verificar que formatos, purga, logs y accesibilidad se comportan igual que en local.
- [ ] 5.3 Probar en producción solo con archivos no confidenciales incluyendo casos límite, y verificar registrando resultados y rollback (redespliegue del commit anterior) disponible.

## Workflow follow-up

- Archivar el change tras la revisión del usuario y la verificación en producción.
- Verificar el resultado archivado y las specs principales generadas.
