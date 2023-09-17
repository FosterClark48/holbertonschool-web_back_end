#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and implements FIFO caching system.

    cache_data (dict): A dictionary to store data.
    item_order (list): A list to store the order of item insertion.
    """

    def __init__(self):
        """ Initialize the FIFOCache

        Call the parent class initializer and create an item_order list.
        """
        super().__init__()
        self.item_order = []

    def put(self, key, item):
        """ Store a key-value pair in the cache

        This method stores a key-value pair in the cache_data dict and
        maintains the insertion order in the item_order list. It also evicts
        the oldest item if the cache reaches its maximum size.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key not in self.item_order:
            self.item_order.append(key)

        # When cache reaches its max size, the oldest item (0) is evicted
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            evicted_key = self.item_order.pop(0)
            del self.cache_data[evicted_key]
            print(f"DISCARD: {evicted_key}")

    def get(self, key):
        """ Retrieve a value from the cache

        This method retrieves a value based on a given key from the cache_data
        dictionary.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
