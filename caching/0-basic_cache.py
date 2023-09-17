#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class inherits from BaseCaching. It's a basic caching system
    that has no limit on the number of items it can store

    cache_data (dict): A dictionary to store data
    """

    def put(self, key, item):
        """
        This method adds a key-value pair to the cache. If the key or
        item is None, the item will not be stored.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        This method retrieves a value from the cache base on the given key.
        if the key is None or doesn't exist in the cache, it returns None.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
