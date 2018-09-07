import time
from threading import RLock
import sys
from collections import OrderedDict

class LRU(OrderedDict):
    def __init__(self, max_len, max_age_seconds):
        assert max_age_seconds >= 0
        assert max_len >= 1
        
        OrderedDict.__init__(self)
        self.max_len = max_len
        self.max_age = max_age_seconds
        self.lock = RLock()
        self._safe_keys = lambda: list(self.keys())

    def __contains__(self,key):
        """ Return true if dict has the key, else return False"""
        try:
            with self.lock:
                item = OrderedDict.__getitem__(self, key)
                if time.time() - item[1] < self.max_age:
                    return True
                else:
                    del self[key]
        except KeyError:
            pass
        return False

    def __getitem__(self, key, with_age=False):
        """ Return the item of the dict.Raises a KeyError if key is not in the map."""
        with self.lock:
            item = OrderedDict.__getitem__(self, key)
            item_age = time.time() - item[1]
            if item_age < self.max_age:
                if with_age:
                    return item[0], item_age
                else:
                    return item[0]
            else:
                del self[key]
                raise KeyError(key)

    def __setitem__(self,key,value):
        """ Set d[key] to value. """
        with self.lock:
            if len(self) == self.max_len:
                try:
                    self.popitem(last=False)
                except KeyError:
                    pass
            OrderedDict.__setitem__(self, key, (value, time.time()))
    
    def pop(self, key, default=None):
        """ Get item from the dict and remove it. Return default if expired or does not exist. """
        with self.lock:
            try:
                item = OrderedDict.__getitem__(self,key)
                del self[key]
                return item[0]
            except KeyError:
                return default


    def get(self, key, default=None, with_age=None):
        """ Return the value for key if key is in the dictionary, else default. """
        try:
            return self.__getitem__(key, with_age)
        except KeyError:
            if with_age:
                return default,None
            else:
                return default

    def get_dict_contents(self):
        """ Returns the items in the dictionary as a list """
        items = []
        for key in self._safe_keys():
            try:
                items.append((key, self[key]))
            except KeyError:
                pass
        return items

    def get_values(self):
        """ Returns the items in the dictionary as a list """
        items = []
        for key in self._safe_keys():
            try:
                items.append(self[key])
            except KeyError:
                pass
        return items



cache = LRU(max_len=100, max_age_seconds=10)

cache["key"] = "value"
print("Cache now")
print(cache.get_dict_contents())
print(cache.get("key"))
time.sleep(5)
print("Cache after 5 seconds")
print(cache.get_dict_contents())
cache["one"]="one"
cache["two"]="two"
print("Cache after insertion of two more entries")
print(cache.get_dict_contents())
time.sleep(5)
print("Cache after ten seconds")
print(cache.get_dict_contents())
