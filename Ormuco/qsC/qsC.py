# qsC.py
# Binay Kumar
# May 12, 2019

from Ormuco.qsC.lruCache import LruCache
import time

"""
==========
qsC
==========
This module contains functions to test LruCache

Contents
--------
* create_cache()  - This function will create the cache for the testing purpose
* initialize_cache()  - This function will initialize the cache for the testing purpose
* get_cache_value()  - This function will return the cache value for a particular key
"""


def create_cache(cache_size, time_to_live):
    """
    Returns: LruCache object
    ===========
    Description
    ===========
    """
    cache = LruCache(cache_size, time_to_live)
    return cache


def initialize_cache():
    """
    Returns:
    ===========
    Description
    ===========
    Initialize cache with the dummy data for testing purpose
    """

    cache.put_page(1, 'firstValue')
    cache.put_page(2, 'secondValue')
    cache.put_page(3, 'thirdValue')
    cache.put_page(4, 'FourthValue')
    cache.show_deque()


def get_cache_value(key):
    """
    Returns:
    ===========
    Description
    ===========
    fetch cache value
    """

    cache_object = cache.get_page(key)
    if cache_object != -1:
        print(cache_object.value)
    else:
        print('No cache object for key = ' + str(key))
    cache.show_deque()


if __name__ == '__main__':
    # cache size is 10 and time_to_live is 1 second
    cache = create_cache(10, 1)

    initialize_cache()
    print('-------------------')

    time.sleep(5)

    # testing
    get_cache_value(3)
    print('-------------------')

    get_cache_value(1)
