"""Chequeos de fidelidad sobre el Markdown generado (sin dependencias)."""
from __future__ import annotations

import re


def analyze(markdown: str, source_ext: str = "") -> list[str]:
    warnings: list[str] = []
    text = markdown or ""
    if not text.strip():
        if source_ext in {".pdf", ".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp"}:
            return [
                "No se pudo extraer texto del documento. "
                "Si es un PDF escaneado (solo imágenes), la versión actual "
                "no incluye OCR: prueba con el original digital."
            ]
        return ["No se pudo extraer texto del documento."]
    if re.search(r"!\[\s*\]\(", text):
        warnings.append("Una imagen no tenía texto alternativo; se marcó como vacía.")
    if source_ext in {".xlsx", ".csv"} and "|" not in text:
        warnings.append("La hoja no contenía tablas detectables en el resultado.")
    return warnings
