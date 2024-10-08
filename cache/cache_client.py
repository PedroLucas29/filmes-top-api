from flask_caching import Cache

cache = Cache()


def init_cache(app):
    app.config['CACHE_TYPE'] = 'redis'
    app.config['CACHE_REDIS_HOST'] = 'localhost'
    app.config['CACHE_REDIS_PORT'] = 6379
    app.config['CACHE_REDIS_DB'] = 0
    app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'
    app.config['CACHE_DEFAULT_TIMEOUT'] = 300
    cache.init_app(app)


def get_cache(key):
    return cache.get(key)


def set_cache(key, value, timeout=300):
    cache.set(key, value, timeout=timeout)
