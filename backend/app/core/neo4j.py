from neo4j import AsyncGraphDatabase, AsyncDriver
from app.core.config import settings

# Global driver instance
driver: AsyncDriver = None

async def init_neo4j_driver():
    """Initialize Neo4j driver"""
    global driver
    driver = AsyncGraphDatabase.driver(
        settings.NEO4J_URI,
        auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
    )
    # Test connection
    async with driver.session() as session:
        await session.run("RETURN 1")

async def get_neo4j_session():
    """Get Neo4j session"""
    if driver is None:
        await init_neo4j_driver()
    return driver.session()

async def close_neo4j_driver():
    """Close Neo4j driver"""
    if driver:
        await driver.close() 