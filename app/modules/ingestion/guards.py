"""Defensas de ingesta: vacíos, protegidos, ZIP con tope (mensajes en español)."""
from __future__ import annotations

import io
import zipfile

from app.config import settings
from app.modules.ingestion.formats import ValidationError


def check_bytes(data: bytes, filename: str) -> None:
    if not data:
        raise ValidationError("El archivo está vacío y no se puede convertir.")
    lower = (filename or "").lower()
    if lower.endswith(".pdf") and b"/Encrypt" in data[:4096]:
        raise ValidationError(
            "El PDF está protegido con contraseña y no se puede convertir. "
            "Quita la protección e inténtalo de nuevo."
        )
    if lower.endswith(".zip"):
        _check_zip(data)


def _check_zip(data: bytes) -> None:
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            total = sum(i.file_size for i in zf.infolist())
    except zipfile.BadZipFile:
        raise ValidationError(
            "El ZIP está dañado y no se puede convertir."
        ) from None
    if total > settings.max_zip_uncompressed_mb * 1024 * 1024:
        raise ValidationError(
            "El ZIP supera el límite de expansión permitido."
        )
