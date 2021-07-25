from django.conf import settings
from django.core.cache import caches
import redis
redis_conn = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT, db=0)

def set(key, data, duration, *args, **kwargs):
    redis_conn.set(key, data, duration)

def get(key, *args, **kwargs):
    return redis_conn.get(key)

def delete(key, *args, **kwargs):
    return redis_conn.delete( key)