#!/usr/bin/env python3
"""LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching class """

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """put meth"""

        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.stack.pop()
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """get meth"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
