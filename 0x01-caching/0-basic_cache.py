#!/usr/bin/env python3
"""Basic caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        BaseCache class
    """

    def put(self, key, item):
        """
            put meth
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
            get meth
        """
        return self.cache_data.get(key, None)
