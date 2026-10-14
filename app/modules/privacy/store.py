"""Tienda efímera: solo memoria/tmp con TTL y purga determinista."""
from __future__ import annotations

import shutil
import time
from dataclasses import dataclass, field
from pathlib import Path

from app.config import settings
from app.modules.privacy.sanitize import temp_dir


@dataclass
class EphemeralItem:
    path: Path
    created_at: float = field(default_factory=time.time)


class EphemeralStore:
    def __init__(self) -> None:
        self._items: dict[str, EphemeralItem] = {}

    def put(self, key: str) -> Path:
        path = temp_dir()
        self._items[key] = EphemeralItem(path=path)
        return path

    def purge(self, key: str) -> bool:
        item = self._items.pop(key, None)
        if item is None:
            return False
        shutil.rmtree(item.path, ignore_errors=True)
        return True

    def purge_expired(self, now: float | None = None) -> int:
        ttl = settings.retention_minutes * 60
        now = time.time() if now is None else now
        expired = [k for k, v in self._items.items() if now - v.created_at > ttl]
        for k in expired:
            self.purge(k)
        return len(expired)

    def __contains__(self, key: object) -> bool:
        return key in self._items
