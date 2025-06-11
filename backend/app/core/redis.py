from redis.asyncio import Redis, ConnectionPool
from app.core.config import settings

# Initialize connection pool
redis_pool: ConnectionPool = None

async def init_redis_pool():
    """Initialize Redis connection pool"""
    global redis_pool
    redis_pool = ConnectionPool.from_url(
        settings.REDIS_URL,
        decode_responses=True
    )

async def get_redis() -> Redis:
    """Get Redis connection from pool"""
    if redis_pool is None:
        await init_redis_pool()
    return Redis(connection_pool=redis_pool)

async def close_redis_pool():
    """Close Redis connection pool"""
    if redis_pool:
        await redis_pool.disconnect() 