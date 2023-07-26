#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.queue:
                    # Get the oldest item in the cache_data.
                    # (first item in the queue)
                    oldest_key = self.queue.pop(0)
                    # Remove the oldest item from the cache_data
                    self.cache_data.pop(oldest_key)
                    print("DISCARD:", oldest_key)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
