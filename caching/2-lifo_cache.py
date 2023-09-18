#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and implements LIFO caching system.
    """
    def __init__(self):
        """ Initialize the LIFOCache

        Call the parent class initializer and create an item_order list.
        """
        super().__init__()
        self.item_order = []

    def put(self, key, item):
        """ Store a key-value pair in the cache

        This method stores a key-value pair in the cache_data dictionary and
        maintains the most recent insertion order in the item_order list.
        It also evicts the most recently added item if the cache reaches its
        maximum size.
        """
        if key is None or item is None:
            return


        # If cache will overflow after adding the new item, evict
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data: # Only evict if the key is new
                evicted_key = self.item_order.pop(-1)
                del self.cache_data[evicted_key]
                print(f"DISCARD: {evicted_key}")

        # Remove key from item_order list if it exists (updating value)
        if key in self.item_order:
            self.item_order.remove(key)

        # Add new item
        self.item_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve a value from the cache

        This method retrieves a value based on a given key from the cache_data
        dictionary.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
