#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Inherits from BaseCaching and implements MRU caching system.
    """
    def __init__(self):
        """ Initialize the MRUCache

        Call the parent class initializer and create an item_order list.
        """
        super().__init__()
        self.item_order = []

    def put(self, key, item):
        """ Store a key-value pair in the cache

        This method stores a key-value pair in the cache_data dict and
        updates the order list to maintain MRU characteristics. It evicts the
        most recently used item if the cache reaches its maximum size.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                key not in self.cache_data:
            evicted_key = self.item_order.pop()
            del self.cache_data[evicted_key]
            print(f"DISCARD: {evicted_key}")

        self.cache_data[key] = item
        if key in self.item_order:
            self.item_order.remove(key)
        self.item_order.append(key)

    def get(self, key):
        """ Retrieve a value from the cache

        This method retrieves a value based on a given key from the cache_data
        dictionary and updates the order list
        """
        if key is None:
            return None

        value = self.cache_data.get(key, None)
        if value is not None:
            self.item_order.remove(key)
            self.item_order.append(key)

        return value
