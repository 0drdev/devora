"""Chequeos de fidelidad sobre el Markdown generado (sin dependencias)."""
from __future__ import annotations

import re


def strip_data_images(markdown: str) -> tuple[str, int]:
    """Reemplaza imágenes incrustadas en base64 por marcadores.

    El base64 no sirve a modelos/LLM, infla el resultado y rompe la
    copia/descarga. Retorna (markdown_limpio, cantidad_reemplazada).
    """
    count = 0

    def _repl(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return f"![imagen incrustada sin texto alternativo](imagen-{count}.png)"

    clean = re.sub(r"!\[[^\]]*\]\(data:[^)]+\)", _repl, markdown or "")
    return clean, count


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
