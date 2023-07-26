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
        """put item into cache_data with LIFO algorithm
        Args:
            key ([type]): key of dictionary
            item ([type]): item to insert in dictionary
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.usage_order:
            discard = self.usage_order.pop(0)
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            if key in self.cache_data:
                self.usage_order.remove(key)
            self.usage_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key using LRU algorithm"""
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end of the usage_order
            # (most recently used)
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
