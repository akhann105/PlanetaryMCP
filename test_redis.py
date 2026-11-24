import redis

# Connect to Redis
client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)

# Check if Redis is connected
print(client.ping())