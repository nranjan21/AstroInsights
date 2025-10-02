from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Tuple


@dataclass
class CacheEntry:
    date_key: str
    value: dict


class DailyCache:
    def __init__(self) -> None:
        self._store: Dict[Tuple[str, str], CacheEntry] = {}

    @staticmethod
    def _today_key() -> str:
        return datetime.utcnow().strftime("%Y-%m-%d")

    def get(self, user_key: str, variant: str) -> dict | None:
        key = (user_key, variant)
        entry = self._store.get(key)
        if entry and entry.date_key == self._today_key():
            return entry.value
        return None

    def set(self, user_key: str, variant: str, value: dict) -> None:
        key = (user_key, variant)
        self._store[key] = CacheEntry(date_key=self._today_key(), value=value)


