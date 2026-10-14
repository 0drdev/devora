"""Matriz de formatos y validación de ingesta (sin dependencias externas)."""
from __future__ import annotations

from dataclasses import dataclass

from app.config import settings

SUPPORTED_FORMATS: dict[str, str] = {
    ".pdf": "application/pdf",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".csv": "text/csv",
    ".json": "application/json",
    ".xml": "application/xml",
    ".html": "text/html",
    ".htm": "text/html",
    ".txt": "text/plain",
    ".md": "text/markdown",
    ".epub": "application/epub+zip",
    ".zip": "application/zip",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".tif": "image/tiff",
    ".tiff": "image/tiff",
    ".bmp": "image/bmp",
    ".wav": "audio/wav",
    ".mp3": "audio/mpeg",
}


@dataclass
class ValidationError(Exception):
    message: str


def validate_upload(filename: str, size_bytes: int) -> str:
    """Valida nombre, extensión y tamaño. Retorna la extensión normalizada."""
    ext = "." + (filename or "").lower().rsplit(".", 1)[-1] if "." in (filename or "") else ""
    if ext not in SUPPORTED_FORMATS:
        raise ValidationError(
            "Tipo no soportado. Formatos aceptados: "
            + ", ".join(sorted(settings.supported_extensions))
        )
    max_bytes = settings.max_upload_mb * 1024 * 1024
    if size_bytes > max_bytes:
        raise ValidationError(
            f"El archivo supera el límite de {settings.max_upload_mb} MB. "
            "Divide el documento o comprímelo e inténtalo de nuevo."
        )
    return ext
