import redis
from django.conf import settings


class Redis:
    def __init__(self, host, port):
        self.redis = redis.Redis(host=host, port=port, db=0)

    def get(self, key: str) -> str:
        return self.redis.get(key).decode("utf-8")

    def set(self, key: str, val: str, ttl=0):
        return self.redis.set(key, val)


host = settings.REDIS.get('HOST')
port = settings.REDIS.get('PORT')
cli = Redis(host, port)





