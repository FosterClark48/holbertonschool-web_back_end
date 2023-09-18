#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Inherits from BaseCaching and implements LRU caching system.
    """
    def __init__(self):
        """ Initialize the LRUCache

        Call the parent class initializer and create an item_order list.
        """
        super().__init__()
        self.item_order = []

    def put(self, key, item):
        """ Store a key-value pair in the cache

        This method stores a key-value pair in the cache_data dict and
        updates the order list to maintain LRU characteristics. It evicts the
        least recently used item if the cache reaches its maximum size.
        """
        # Check for None
        if key is None or item is None:
            return

        # Update Cache
        self.cache_data[key] = item
        # Update order
        if key in self.item_order:  # if key already exists in order list
            self.item_order.remove(key)  # remove old occurrence
        self.item_order.append(key)  # then add it to end of list

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            evicted_key = self.item_order.pop(0)
            del self.cache_data[evicted_key]
            print(f"DISCARD: {evicted_key}")

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
