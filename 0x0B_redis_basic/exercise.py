#!/usr/bin/env python3
""" Module for Cache class """


import redis
import uuid
from typing import Union


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
