django-memcached-hashring
=========================

A simple Django cache backend based on `python-memcached`_ using hash_ring_
for consistent hashes. See the individual packages' documentation for more
info.

Use it like this::

    CACHES = {
        'default': {
            'BACKEND': 'memcached_hashring.backend.MemcachedHashRingCache',
            'LOCATION': [
               '10.0.0.1:11211',
               '10.0.0.2:11211',
               '10.0.0.3:11211',
            ],
        },
    }

.. _hash_ring: https://github.com/Doist/hash_ring
.. _`python-memcached`: https://github.com/linsomniac/python-memcached
