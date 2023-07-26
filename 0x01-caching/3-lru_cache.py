#!/usr/bin/python3
"""LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        """Initialize LRUCache"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item in the cache using LRU algorithm"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.usage_order:
                    # Get the least recently used item
                    # (first item in the usage_order)
                    lru_key = self.usage_order.pop(0)
                    # Remove the least recently used item from the cache_data
                    self.cache_data.pop(lru_key)
                    print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """Get an item by key using LRU algorithm"""
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end of the usage_order
            # (most recently used)
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
