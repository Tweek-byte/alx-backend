#!/usr/bin/env python3
"""LRU Caching"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching class """
    def __init__(self):
        super().__init__()
        self.use_order = []

    def put(self, key, item):
        """put meth"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.use_order.pop(0)
                print("DISCARD: {}".format(lru_key))
                del self.cache_data[lru_key]
            self.cache_data[key] = item
            if key in self.use_order:
                self.use_order.remove(key)
            self.use_order.append(key)

    def get(self, key):
        """get meth"""
        if key is None or key not in self.cache_data:
            return None

        if key in self.use_order:
            self.use_order.remove(key)
        self.use_order.append(key)

        return self.cache_data[key]
