#!/usr/bin/env python3
"""FIFO Caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFO caching class
    """

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        put meth
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discard = self.queue.pop(0)
                    del self.cache_data[discard]
                    print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
            get meth
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
