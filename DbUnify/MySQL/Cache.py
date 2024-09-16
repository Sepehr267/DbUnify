import time
from collections import OrderedDict
from threading import Lock
from typing import Any, Dict, Tuple

class Cache:
    """
    Cache Class

    The Cache class provides methods for storing and retrieving query results in a cache to improve performance. It uses LRU (Least Recently Used) cache eviction and supports automatic cache expiration based on a time-to-live (TTL) value.

    Attributes:
        cache (OrderedDict[str, Tuple[Any, float]]): An ordered dictionary to store cached query results and their expiration times.
        ttl (int): Time-to-live for cache entries in seconds.
        max_size (int): Maximum number of entries allowed in the cache.
        lock (Lock): A threading lock to ensure thread-safe operations.

    Methods:
        __init__(self, ttl, max_size): Initializes the Cache instance with a TTL value and a maximum size.
        set(self, key, value): Stores a query result in the cache with an expiration time.
        get(self, key): Retrieves a query result from the cache if it exists and is not expired.
        is_expired(self, expiration): Checks if a cache entry is expired.
        _clean_expired(self): Removes expired cache entries.
        _evict_if_needed(self): Evicts the least recently used cache entry if the cache is full.
    """

    def __init__(self, ttl: int = 60, max_size: int = 1000):
        """
        Initialize the Cache instance.

        Args:
            ttl (int): Time-to-live for cache entries in seconds. Default is 60 seconds (1 minute).
            max_size (int): Maximum number of entries allowed in the cache. Default is 1000.
        """
        self.cache: OrderedDict[str, Tuple[Any, float]] = OrderedDict()
        self.ttl = ttl
        self.max_size = max_size
        self.lock = Lock()

    def set(self, key: str, value: Any) -> None:
        """
        Store a query result in the cache with an expiration time.

        Args:
            key (str): The cache key, usually the query string.
            value (Any): The query result to be cached.
        """
        with self.lock:
            self._clean_expired()
            if key in self.cache:
                del self.cache[key]
            self.cache[key] = (value, time.time() + self.ttl)
            self._evict_if_needed()

    def get(self, key: str) -> Any:
        """
        Retrieve a query result from the cache if it exists and is not expired.

        Args:
            key (str): The cache key, usually the query string.

        Returns:
            Any: The cached query result, or None if the cache entry does not exist or is expired.
        """
        with self.lock:
            self._clean_expired()
            if key in self.cache:
                value, expiration = self.cache.pop(key)
                if not self.is_expired(expiration):
                    self.cache[key] = (value, expiration)
                    return value
            return None

    def is_expired(self, expiration: float) -> bool:
        """
        Check if a cache entry is expired.

        Args:
            expiration (float): The expiration time of the cache entry.

        Returns:
            bool: True if the cache entry is expired, False otherwise.
        """
        return time.time() > expiration

    def _clean_expired(self) -> None:
        """
        Remove expired cache entries.

        This method iterates through the cache and removes entries that have expired.
        """
        current_time = time.time()
        expired_keys = [key for key, (value, expiration) in self.cache.items() if expiration < current_time]
        for key in expired_keys:
            del self.cache[key]

    def _evict_if_needed(self) -> None:
        """
        Evict the least recently used cache entry if the cache is full.
        """
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)
