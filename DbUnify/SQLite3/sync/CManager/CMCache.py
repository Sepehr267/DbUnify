import time
from typing import Any, Dict, Tuple, Optional
from collections import OrderedDict

class CMCache:
    def __init__(self, ttl: int = 60, max_size: int = 1000):
        self.ttl = ttl
        self.cache: OrderedDict[str, Tuple[float, Any]] = OrderedDict()
        self.max_size = max_size

    def get(self, query: str) -> Optional[Any]:
        current_time = time.monotonic()
        if query in self.cache:
            timestamp, result = self.cache.pop(query)
            if current_time - timestamp < self.ttl:
                self.cache[query] = (timestamp, result)
                return result
        return None

    def set(self, query: str, result: Any) -> None:
        current_time = time.monotonic()
        if len(self.cache) >= self.max_size:
            self._evict()
        self.cache[query] = (current_time, result)

    def _evict(self) -> None:
        if self.cache:
            self.cache.popitem(last=False)