'''
    https://leetcode.com/problems/lru-cache/
'''
'''
    LRU Cache implementation using an OrderedDict
    -NOTE: Another implementation could be done using a Doubly linked list and a dictionary
'''

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        # key = key, value = k,v
        self.cache = OrderedDict()
        self.size = 0
        self.capacity = capacity
        
    # move k,v pair to the front of the list
    def _moveToFront(self, key):
        v = self.cache.pop(key)
        self.cache[key] = v
    
    def _update(self, key, val):
        self.cache[key] = val

    def get(self, key: int) -> int:
        if key in self.cache:
            self._moveToFront(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update
            self._update(key, value)
            self._moveToFront(key)
        elif self.size < self.capacity:
            # put without removing
            self.cache[key] = value
            self.size += 1
        else:
            # put and remove lru
            self.cache.popitem(last=False)
            self.cache[key] = value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)