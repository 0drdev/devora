"""Registro operativo sin contenido: solo metadatos anonimizados."""
from __future__ import annotations

import logging

logger = logging.getLogger("conversor")


def log_conversion(filename: str, size_bytes: int, ok: bool) -> None:
    ext = "." + filename.lower().rsplit(".", 1)[-1] if "." in filename else ""
    logger.info("conversion ext=%s size=%d ok=%s", ext, size_bytes, ok)
