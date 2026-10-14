"""Higiene de nombres y almacenamiento efímero (sin persistencia)."""
from __future__ import annotations

import re
import tempfile
from pathlib import Path

_SAFE = re.compile(r"[^a-zA-Z0-9._-]+")


def safe_filename(name: str) -> str:
    base = (name or "documento").split("/")[-1].split("\\")[-1]
    clean = _SAFE.sub("_", base).strip("._") or "documento"
    return clean[:100]


def download_name(source_filename: str) -> str:
    stem = safe_filename(source_filename)
    stem = stem.rsplit(".", 1)[0] if "." in stem else stem
    return f"{stem}.md"


def temp_dir() -> Path:
    """Directorio temporal desechable por conversión (se purga al cerrar)."""
    return Path(tempfile.mkdtemp(prefix="conv-"))
