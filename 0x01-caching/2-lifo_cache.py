#!/usr/bin/env python3
"""
Module: Task 2 - Last-In First-Out caching
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents object that allows storing and
    retrieves items from dictionary with LIFO
    removal mechanism when limit is reached
    """
    def __init__(self):
        """Initializes cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds item in cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves item by key
        """
        return self.cache_data.get(key, None)
