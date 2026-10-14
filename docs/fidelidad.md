# Matriz de fidelidad

Límite acordado: 10 MB por archivo, retención 15 min, ZIP expansión máxima 200 MB.
Ajustables sin código con `MAX_UPLOAD_MB`, `RETENTION_MINUTES` y `MAX_ZIP_MB`.

| Formato | Qué se preserva | Advertencias posibles |
|---|---|---|
| PDF | texto, encabezados, listas, tablas, enlaces | imagen sin alt-text; página sin texto extraíble |
| DOCX | jerarquía, listas, tablas, enlaces | imagen sin alt-text |
| PPTX | texto de diapositivas, listas, tablas, enlaces | diapositiva sin texto; imagen sin alt-text |
| XLSX/CSV | tablas por hoja | hoja sin tablas detectables |
| JSON/XML/HTML/TXT/MD | texto y estructura equivalente | contenido vacío |
| EPUB | capítulos como encabezados | capítulo sin texto |
| ZIP | contenido de cada miembro soportado | miembro dañado o fuera de matriz |
| Imágenes (PNG/JPG/TIF/BMP) | texto/alt disponible | sin texto alternativo |
| Audio (WAV/MP3) | transcripción (requiere Markitdown completo) | sin transcripción disponible |

Taxonomía de advertencias (`app/modules/fidelity/checks.py`):
- `No se pudo extraer texto del documento.` (+ orientación sobre escaneados/OCR si es PDF o imagen).
- `Una imagen no tenía texto alternativo; se marcó como vacía.`
- `La hoja no contenía tablas detectables en el resultado.`

Regla: ninguna pérdida es silenciosa; el resultado siempre incluye la lista de advertencias.
