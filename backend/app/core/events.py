from typing import Callable
from fastapi import FastAPI
from app.db.session import engine
from app.db.init_db import init_db
import logging

logger = logging.getLogger(__name__)

def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        try:
            # Initialize databases
            await init_db()
            logger.info("Database initialized successfully")
            
            # Additional startup tasks can be added here
            # For example:
            # - Initialize AI models
            # - Set up WebSocket connections
            # - Connect to n8n
            
        except Exception as e:
            logger.error(f"Error during startup: {e}")
            raise e

    return start_app

def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        try:
            # Close database connections
            await engine.dispose()
            logger.info("Database connections closed")
            
            # Additional cleanup tasks can be added here
            
        except Exception as e:
            logger.error(f"Error during shutdown: {e}")
            raise e

    return stop_app 