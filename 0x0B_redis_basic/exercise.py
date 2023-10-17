#!/usr/bin/env python3
""" Module for Cache class """


import redis
import uuid
import functools
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """ Decorator to count calls made to methods of an instance """
    key = method.__qualname__

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # incr count for method call in Redis
        self._redis.incr(key)

        # Callling original method and return its result
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to store the history of inputs and outputs of a method """
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # Storing input args to input list in Redis
        self._redis.rpush(input_key, str(args))

        # Calling original method to get output
        output = method(self, *args, **kwargs)

        # Storing output to outputs list in Redis
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


def replay(method: Callable) -> None:
    """ Display the history of calls of a particular function """
    # Fetching inputs & outputs from Redis
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    inputs = method.__self__._redis.lrange(input_key, 0, -1)  # get all items
    outputs = method.__self__._redis.lrange(output_key, 0, -1)  # from list

    # Displaying the method name and its call count
    print(f"{method.__qualname__} was called {len(inputs)} times:")

    # Looping over each input/output pair and displaying them
    for inp, out in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{inp.decode('utf-8')})"
                f" -> {out.decode('utf-8')}")


class Cache:
    """ Cache class """
    def __init__(self):
        """ Cache class constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
