# Design

## Context

Ver `proposal.md` (Why) y `specs/` para requisitos. Estado actual: proyecto greenfield sin código; solo `openspec/` y `.opencode/`. Restricciones fijadas con el usuario: stack Python web simple, integración con `microsoft/markitdown` en local, cobertura amplia de formatos, procesamiento efímero sin base de datos, accesibilidad total, fidelidad verificable, y paridad local→producción en servicios gratuitos con decisiones verificadas por el usuario.

Referencias verificadas: Markitdown soporta PDF, Office (DOCX/PPTX/XLSX), imágenes (EXIF/OCR), audio (transcripción), HTML, CSV/JSON/XML, ZIP, EPUB, YouTube y plugins; su guía de seguridad exige sanitizar entradas no confiables y usar la API más estrecha (`convert_stream`/`convert_local`) en servidores. Cuotas gratuitas consultadas: Vercel Hobby (uso personal no comercial, ~100 GB transferencia, ~1M edge requests, timeout y pausa al exceder), Render Free (web service Python 512 MB/0.1 CPU, sleep a los 15 min inactivo, ~1 min cold start, 750 h/mes), Cloudflare Workers free (sin Python nativo, CPU ~10 ms) y Hugging Face Spaces como alternativa Python.

## Goals / Non-Goals

**Goals:**
- Una sola unidad desplegable Python que cumpla las tres capacidades con purga efímera y avisos de fidelidad.
- Verificación local completa antes de producción: tests, corpus de fidelidad por formato y auditoría de no-persistencia.
- Guía de despliegue gratuito con paridad y rollback simples.

**Non-Goals:**
- Chat o conversación con IA integrada; el Markdown se reutiliza en herramientas externas.
- OCR con LLM, Azure Document Intelligence/Content Understanding, transcripción remota o fetching de URLs/YouTube.
- Cuentas, multiusuario persistente, historial, analítica de contenido o almacenamiento duradero.

## Decisions

- **App Python única con FastAPI + frontend server-rendered mínimo (HTML/CSS/JS progresivo).** Alternativas: Flask (menos validación/tipado), Django (sobredimensionado), Next.js + microservicio Python (dos despliegues, más costo/complejidad). FastAPI aporta validación, docs OpenAPI para verificación y tests sencillos con `TestClient`, manteniendo un solo servicio gratuito.
- **Integración Markitdown pineada (`markitdown[all]` con versión fijada) usando `convert_stream` sobre bytes subidos.** Alternativa `convert()` genérica o `convert_local` con rutas: se descartan por la guía de seguridad (la genérica acepta URIs remotas). Plugins desactivados, sin `llm_client`, sin Azure, sin descarga automática de URLs. Validación previa: sniff MIME + extensión, límites de tamaño/páginas/expansión ZIP, rechazo de cifrados/corruptos con mensajes en español.
- **Efimeridad por diseño:** sin DB ni volúmenes; solo `tempfile` por sesión con TTL corto y trabajo de purga (al descargar/descartar/expirar/cerrar). Logs con redacción (solo tipo/tamaño/resultado), cabeceras `no-store` para respuestas con contenido, y página que declara retención y confirma purga. Alternativa Blob/S3 o SQLite: descartada por violar confidencialidad y sumar costo.
- **Fidelidad como contrato testeable:** corpus dorado por formato (PDF con tablas, DOCX con jerarquía, PPTX con notas/alt-text, XLSX multi-hoja, imagen, audio corto, HTML, ZIP) con aserciones estructurales (nº encabezados/tablas/enlaces, presencia de alt-text) más taxonomía de advertencias (página/hoja/diapositiva/tabla no extraída). Revisión manual por muestreo antes de cada release; ninguna pérdida silenciosa.
- **Accesibilidad objetivo WCAG 2.2 AA con HTML semántico:** foco visible, orden lógico, etiquetas/roles, `aria-live` para progreso/resultado, contraste, `prefers-reduced-motion`, zoom 200% y responsive. Verificación con `axe` + pruebas manuales de teclado y lector (NVDA/VoiceOver). Español como idioma por defecto de UI y errores.
- **Despliegue gratuito recomendado: Render Free como backend+frontend único; alternativa Hugging Face Spaces; Vercel solo para frontend estático si se separa.** Vercel Hobby es personal/no comercial, con pausa al exceder cuota y runtime serverless poco apto para conversiones pesadas Python/binarios; Cloudflare Workers no ejecuta Markitdown (sin Python, CPU mínima). Render Free ejecuta Python nativo con HTTPS y deploy por Git a costo cero para prototipo (con sleep/cold start asumidos). Decisión final de plataforma y dominio **requiere confirmación del usuario antes de implementar** (gobernanza del change).
- **Calidad y paridad:** `uv`/`venv` + `requirements` fijados, `Dockerfile` para reproducibilidad, `pytest` (conversión, límites, purga, redacción de logs) + smoke accesible, guías `README` local, matriz de fidelidad y checklist de paridad local/prod.

## Risks / Trade-offs

- [Archivos escaneados o de baja calidad reducen fidelidad] → Mitigación: advertencia explícita + guía de qué esperar por formato; sin OCR-LLM en v1.
- [Límites del plan gratuito (RAM/CPU/tiempo, sleep y cold start en Render)] → Mitigación: límites documentados, mensajes de reintento y opción de auto-hospedaje; no prometer SLA.
- [ZIP bombs, nombres con path traversal, PDFs maliciosos] → Mitigación: sanitización, `convert_stream`, topes de expansión y aislamiento en temp dir desechable.
- [Falsas expectativas sobre Vercel] → Mitigación: comparativa de cuotas en la guía y recomendación Render/HF; Vercel solo como estático opcional.
- [Regresiones de fidelidad al actualizar Markitdown] → Mitigación: pin de versión + corpus dorado en CI local antes de cada bump.

## Migration Plan

Greenfield, sin migración de datos. Secuencia: 1) Entorno local documentado y verificado (instalación, tests, corpus). 2) Checkpoint con el usuario para fijar plataforma gratuita, límites y TTL. 3) Despliegue a URL gratuita con checklist de paridad (formatos, purga, logs, accesibilidad, HTTPS). 4) Verificación en prod con archivos de prueba no confidenciales. Rollback: redesplegar el commit anterior etiquetado; como no hay DB, no hay migración de estado.

## Open Questions

- Valores finales de límites (MB por archivo, páginas/hojas máximas, TTL en minutos) tras medir el corpus en la máquina de referencia: ajustables sin cambiar el enfoque.
- Si se habilitará más adelante OCR con LLM como opción explícita y aislada (fuera de v1 por costo y confidencialidad).
