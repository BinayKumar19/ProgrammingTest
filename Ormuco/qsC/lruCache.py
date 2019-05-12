import collections
from datetime import datetime


class CacheObject:

    def __init__(self, value, creation_time):
        self.value = value
        self.creation_time = creation_time


class LruCache:

    def __init__(self, cache_size, time_to_live):
        self.cache_size = cache_size
        self.deque = collections.deque()
        self.cache_objects_storage = {}
        self.time_to_live = time_to_live

    def get(self, page_no):

        if page_no in self.cache_objects_storage.keys():
            cache_object = self.cache_objects_storage[page_no]
            self.deque.remove(page_no)
            time_elapsed_seconds = (datetime.now() - cache_object.creation_time).total_seconds()
            if time_elapsed_seconds > self.time_to_live:
                self.cache_objects_storage.pop(page_no)
                cache_object = self.missing_page_operation()
            else:
                self.deque.append(page_no)
                cache_object.creation_time = datetime.now().microsecond
        else:  # not present in the cache
            cache_object = self.missing_page_operation()

        return cache_object

    def put(self, page_no, value):
        if len(self.cache_objects_storage) == self.cache_size:
            last_page = self.deque.popleft()
            self.cache_objects_storage.pop(last_page)

        cache_object = CacheObject(value, datetime.now())
        self.cache_objects_storage[page_no] = cache_object
        self.deque.append(page_no)

    def missing_page_operation(self):
        print('This method will be updated to handle the case when cache doesn''t contain the requested page')
        return -1

    def update_other_lru(self):
        print('This method will broadcast messages to other geographical LRU cache')

    def show_deque(self):
        for key in self.deque:
            print(key)
