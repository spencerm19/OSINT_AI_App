import logging
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.base import Base
from app.db.session import engine
from app.core.config import settings

logger = logging.getLogger(__name__)

async def init_db() -> None:
    try:
        # Create database tables
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            logger.info("Created database tables")

        # Initialize vector extension for PostgreSQL
        async with AsyncSession(engine) as session:
            await session.execute('CREATE EXTENSION IF NOT EXISTS vector;')
            await session.commit()
            logger.info("Initialized vector extension")

        # Additional initialization steps can be added here
        # For example:
        # - Create initial admin user
        # - Load initial data
        # - Set up indexes
        # - Configure full-text search

    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise 