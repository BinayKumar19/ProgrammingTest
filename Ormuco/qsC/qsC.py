from Ormuco.qsC.lruCache import LruCache
import time


def create_cache(cache_size, time_to_live):
    cache = LruCache(cache_size, time_to_live)
    return cache


def intialise_cache():
    cache.put(1, 'firstValue')
    cache.put(2, 'secondValue')
    cache.put(3, 'thirdValue')
    cache.put(4, 'FourthValue')
    cache.show_deque()


def get_cache_value(key):
    cache_object = cache.get(key)
    if cache_object != -1:
        print(cache_object.value)
    else:
        print('No cache object for key = ' + str(key))
    cache.show_deque()


cache = create_cache(10,1)  #time_to_live is in seconds
intialise_cache()
print('-------------------')
time.sleep(5)

get_cache_value(3)
print('-------------------')
get_cache_value(1)
