import asyncio
from typing import Any, Dict, Tuple

class Cache:
    """
    # Cache Class

    #### The Cache class provides methods for storing and retrieving query results in a cache to improve performance. It supports automatic cache expiration based on a time-to-live (TTL) value.

    ### Attributes:
        - cache (Dict[str, Tuple[Any, float]]): A dictionary to store cached query results and their expiration times.
        - ttl (int): Time-to-live for cache entries in seconds.

    ### Methods:
        - __init__(self, ttl): Initializes the Cache instance with a TTL value.
        - set(self, key, value): Stores a query result in the cache with an expiration time.
        - get(self, key): Retrieves a query result from the cache if it exists and is not expired.
        - is_expired(self, entry): Checks if a cache entry is expired.

    ### Note:
        - This class is designed to be used in conjunction with the Manager class to cache query results.
    """
    def __init__(self, ttl: int = 300):
        """
        Initialize the Cache instance.

        Args:
            ttl (int): Time-to-live for cache entries in seconds. Default is 300 seconds (5 minutes).
        """
        self.cache: Dict[str, Tuple[Any, float]] = {}
        self.ttl = ttl

    async def set(self, key: str, value: Any) -> None:
        """
        Store a query result in the cache with an expiration time.

        Args:
            key (str): The cache key, usually the query string.
            value (Any): The query result to be cached.
        """
        self.cache[key] = (value, await self._current_time() + self.ttl)

    async def get(self, key: str) -> Any:
        """
        Retrieve a query result from the cache if it exists and is not expired.

        Args:
            key (str): The cache key, usually the query string.

        Returns:
            Any: The cached query result, or None if the cache entry does not exist or is expired.
        """
        if key in self.cache:
            value, expiration = self.cache[key]
            if not await self.is_expired(expiration):
                return value
            else:
                del self.cache[key]
        return None

    async def is_expired(self, expiration: float) -> bool:
        """
        Check if a cache entry is expired.

        Args:
            expiration (float): The expiration time of the cache entry.

        Returns:
            bool: True if the cache entry is expired, False otherwise.
        """
        return await self._current_time() > expiration

    async def _current_time(self) -> float:
        """
        Get the current time in seconds since the epoch.

        Returns:
            float: The current time.
        """
        return asyncio.get_event_loop().time()
