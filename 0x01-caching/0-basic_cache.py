#!/usr/bin/python3
"""
class BasicCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache that inherits from BaseCaching
    """

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for thekey
 """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        value = self.cache_data.get(key)
        return value
