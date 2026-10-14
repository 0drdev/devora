"""Configuración central (acordada con el usuario,-tunable por entorno)."""
from __future__ import annotations

import os
from dataclasses import dataclass, field


def _int(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, str(default)))
    except ValueError:
        return default


@dataclass(frozen=True)
class Settings:
    max_upload_mb: int = _int("MAX_UPLOAD_MB", 10)
    max_zip_uncompressed_mb: int = _int("MAX_ZIP_MB", 200)
    retention_minutes: int = _int("RETENTION_MINUTES", 15)
    supported_extensions: tuple[str, ...] = field(
        default=(
            ".pdf", ".docx", ".pptx", ".xlsx", ".csv", ".json", ".xml",
            ".html", ".htm", ".txt", ".md", ".epub", ".zip",
            ".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp",
            ".wav", ".mp3",
        )
    )


settings = Settings()
