#!/usr/bin/python3
"""MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with an MRU
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initialize MRUCache"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item in the cache using MRU algorithm"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.usage_order:
                    # Get the most recently used item
                    # (last item in the usage_order)
                    mru_key = self.usage_order.pop()
                    # Remove the most recently used item from the cache_data
                    self.cache_data.pop(mru_key)
                    print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """Get an item by key using MRU algorithm"""
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end of the usage_order
            # (most recently used)
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
