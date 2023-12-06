#!/usr/bin/env python3
"""
Cache module using Redis
"""
import redis
import uuid

class Cache:
    """
    Cache class for storing data in Redis
    """

    def __init__(self):
        """
        Initializes the Cache instance with a Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """
        Stores the input data in Redis with a randomly generated key.

        Args:
            data: The data to be stored in the cache. Can be str, bytes, int, or float.

        Returns:
            str: The randomly generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

if __name__ == "__main__":
    cache = Cache()
    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))￼Enter
