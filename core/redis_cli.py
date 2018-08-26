import redis
from django.conf import settings


class Redis:
    def __init__(self, host, port):
        self.redis = redis.Redis(host=host, port=port, db=0)

    def get(self, key: str) -> str:
        val = self.redis.get(key)
        return val.decode("utf-8") if val else None

    def set(self, key: str, val: str, ttl=0):
        return self.redis.set(key, val, 1000)


host = settings.REDIS.get('HOST')
port = settings.REDIS.get('PORT')
cli = Redis(host, port)





