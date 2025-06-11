from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.config import settings
from app.api.api_v1.api import api_router
from app.core.database import init_db
from app.core.redis import init_redis_pool
from app.core.neo4j import init_neo4j_driver

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize connections
    await init_db()
    await init_redis_pool()
    await init_neo4j_driver()
    
    yield
    
    # Cleanup on shutdown
    from app.core.database import engine
    await engine.dispose()
    
    from app.core.redis import redis_pool
    await redis_pool.close()
    
    from app.core.neo4j import driver
    await driver.close()

app = FastAPI(
    title="OSINT Buddy API",
    description="API for OSINT research and visualization platform",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "message": "Welcome to OSINT Buddy API",
        "version": "1.0.0",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
    } 