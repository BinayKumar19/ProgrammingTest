# lruCache.py
# Binay Kumar
# May 12, 2019

import collections
from datetime import datetime

"""
==========
lruCache
==========
This module contains a wrapper class LruCache that acts as a Cache with Least Recently used (LRU) functionality 
Missing functionality: Making the LruCache Geo Distributed 

Contents
--------
* CacheObject  - A Cache object class stored by Cache
* LruCache     - A Cache Class with LRU functionality
* get_page()   - Returns a page from the Cache
* put_page()   - Puts a page in the cache
* missing_page_operation() - Handles the case when page is not present in the cache(yet to be coded)
* update_other_lru()   - Update other LRU cache's so that all have consistent data(yet to be coded)

"""


class CacheObject:
    """
    Instances represent an Object stored by Cache.
    ===========
    Description
    ===========
    A cache object contains a value which contains the information of the page and modified time of the page.
    modified_time will be updated whenever the page is requested from the cache.
    """

    def __init__(self, value, creation_time):
        self.value = value
        self.modified_time = creation_time


class LruCache:
    """
    Instances represent an LRU cache .
    ===========
    Description
    ===========
    Cache works with the Least recently used (LRU) functionality.
    """

    def __init__(self, cache_size, time_to_live):
        self.cache_size = cache_size
        self.deque = collections.deque()
        self.cache_objects_storage = {}
        self.time_to_live = time_to_live

    def get_page(self, page_no):
        """
        Returns: The Page number stored in the cache.
        ===========
        Description
        ===========
        If page number exists in the cache, last modified time is checked to see if it is expired, If yes
        missing_page_operation() is called, If no page is returned
        If Page number doesnt exist in the cache, missing_page_operation is called.
        """
        if page_no in self.cache_objects_storage.keys():
            # if page number present in the cache
            cache_object = self.cache_objects_storage[page_no]
            self.deque.remove(page_no)
            time_elapsed_seconds = (datetime.now() - cache_object.modified_time).total_seconds()
            if time_elapsed_seconds > self.time_to_live:
                # if page is expired
                self.cache_objects_storage.pop(page_no)
                cache_object = self.missing_page_operation()
            else:
                self.deque.append(page_no)
                cache_object.modified_time = datetime.now()
        else:
            # not present in the cache
            cache_object = self.missing_page_operation()

        return cache_object

    def put_page(self, page_no, value):
        """
        Returns:
        ===========
        Description
        ===========
        saves a page in the cache.
        If cache is full removes the page number last accessed.
        """
        if len(self.cache_objects_storage) == self.cache_size:
            # Cache is full
            last_page = self.deque.popleft()
            self.cache_objects_storage.pop(last_page)

        cache_object = CacheObject(value, datetime.now())
        self.cache_objects_storage[page_no] = cache_object
        self.deque.append(page_no)

    def missing_page_operation(self):
        """
        Returns: -1 as code is yet to be written
        ===========
        Description
        ===========
        This method will handle the case when When page doesn't exist in the cache
        """
        print('This method will be updated to handle the case when cache doesn''t contain the requested page')
        return -1

    def update_other_lru(self):
        """
        Returns:
        ===========
        Description
        ===========
        This method update other LRU cache's to keep data consistent
        """
        print('This method will send message to other geographical LRU cache')

    def show_deque(self):
        """
        Returns:
        ===========
        Description
        ===========
        This method is used for testing purpose can be removed
        """
        for key in self.deque:
            print(key)
