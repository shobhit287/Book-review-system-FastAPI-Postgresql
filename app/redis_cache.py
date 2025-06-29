import redis
import sys

try:
    redis_client = redis.Redis(
        host="localhost",
        port=6379,
        db=0,
        decode_responses=True  
    )
    redis_client.ping()
    print("Redis connected successfully")
except redis.exceptions.ConnectionError as e:
    print(f"Redis connection failed: {e}")
    sys.exit(1)  
