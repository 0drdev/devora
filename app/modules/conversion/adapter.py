"""Adaptador Markitdown: importación perezosa, API mínima, sin red remota.

Cumple la guía de seguridad de Markitdown: usar la API más estrecha
(`convert_stream`) y no descargar URLs automáticamente.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ConversionResult:
    markdown: str
    warnings: list[str]


def convert_bytes(data: bytes, filename: str) -> ConversionResult:
    try:
        from markitdown import MarkItDown
    except ImportError as exc:
        raise RuntimeError(
            "Markitdown no está instalado: se requiere Python >= 3.10 "
            "(ver requirements.txt y Dockerfile)."
        ) from exc

    import io

    from app.modules.fidelity.checks import analyze

    md = MarkItDown(enable_plugins=False)
    result = md.convert_stream(io.BytesIO(data), file_extension=_ext(filename))
    text = result.markdown or ""
    return ConversionResult(markdown=text, warnings=analyze(text, _ext(filename)))


def _ext(filename: str) -> str:
    name = (filename or "").lower()
    return "." + name.rsplit(".", 1)[-1] if "." in name else ""
