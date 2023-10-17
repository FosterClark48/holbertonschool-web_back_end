#!/usr/bin/env python3
""" Module for Cache class """


import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """ Cache class """
    def __init__(self):
        """ Cache class constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store the input data in Redis using random key """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        """ Get the value for the given key from Redis """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ Get the value for the given key from Redis as a string """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Get the value for the given key from Redis as an integer"""
        value = self._redis.get(key)
        return int(value)
