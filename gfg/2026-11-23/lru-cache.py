from collections import OrderedDict


class LRUCache:

    def __init__(self, cap):
        self.cap = cap
        self.cache = OrderedDict()  # least recently used first

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.cap:
            self.cache.popitem(last=False)  # evict the least recently used
        self.cache[key] = value
