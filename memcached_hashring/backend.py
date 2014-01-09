from django.core.cache.backends.memcached import MemcachedCache

from . import client as memcache

class MemcachedHashRingCache(MemcachedCache):
    "An implementation of a cache binding using python-memcached and hash_ring"
    def __init__(self, server, params):
        super(MemcachedCache, self).__init__(server, params,
                                             library=memcache,
                                             value_not_found_exception=ValueError)
