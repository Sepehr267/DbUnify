import time
from typing import Any, Dict, Tuple

class Cache:
    """
    Cache Class

    The Cache class provides methods for storing and retrieving query results in a cache to improve performance. It supports automatic cache expiration based on a time-to-live (TTL) value.

    Attributes:
        cache (Dict[str, Tuple[Any, float]]): A dictionary to store cached query results and their expiration times.
        ttl (int): Time-to-live for cache entries in seconds.

    Methods:
        __init__(self, ttl): Initializes the Cache instance with a TTL value.
        set(self, key, value): Stores a query result in the cache with an expiration time.
        get(self, key): Retrieves a query result from the cache if it exists and is not expired.
        is_expired(self, expiration): Checks if a cache entry is expired.
        _clean_expired(self): Removes expired cache entries.
    """
    
    def __init__(self, ttl: int = 60):
        """
        Initialize the Cache instance.

        Args:
            ttl (int): Time-to-live for cache entries in seconds. Default is 60 seconds (1 minute).
        """
        self.cache: Dict[str, Tuple[Any, float]] = {}
        self.ttl = ttl

    def set(self, key: str, value: Any) -> None:
        """
        Store a query result in the cache with an expiration time.

        Args:
            key (str): The cache key, usually the query string.
            value (Any): The query result to be cached.
        """
        self._clean_expired()
        self.cache[key] = (value, time.time() + self.ttl)

    def get(self, key: str) -> Any:
        """
        Retrieve a query result from the cache if it exists and is not expired.

        Args:
            key (str): The cache key, usually the query string.

        Returns:
            Any: The cached query result, or None if the cache entry does not exist or is expired.
        """
        self._clean_expired()
        if key in self.cache:
            value, expiration = self.cache[key]
            if not self.is_expired(expiration):
                return value
            else:
                del self.cache[key]
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
        self.cache = {k: v for k, v in self.cache.items() if v[1] > current_time}
