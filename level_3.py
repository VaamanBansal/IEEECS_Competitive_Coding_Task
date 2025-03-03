from sortedcontainers import SortedList
from datetime import datetime, timedelta
import time
class Cache:
    def __init__(self):
        self.data = SortedList()
        self.key = {}
    def clear(self):
        now = datetime.now()
        index = self.data.bisect_left([now, timedelta(0)])
        expired = self.data[:index]
        del self.data[:index]  
        for t, exp, k in expired:
            if k in self.key:
                del self.key[k]
    def set(self, key, value, exp):
        self.data.add([datetime.now(), exp, key]) 
        self.key[key] = (value, datetime.now(), exp)
        self.clear()
    def get(self, key):
        self.clear()
        if key in self.key:
            print(self.key[key][0])
        else:
            print("Key Expired or Was Never Added")
cache = Cache()
cache.set("username", "JohnDoe", timedelta(seconds=5))
cache.get("username")
time.sleep(5)
cache.get("username")