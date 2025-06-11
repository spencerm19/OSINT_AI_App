from fastapi import APIRouter
from app.api.api_v1.endpoints import research, graph, auth, websocket

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(research.router, prefix="/research", tags=["research"])
api_router.include_router(graph.router, prefix="/graph", tags=["graph"])
api_router.include_router(websocket.router, prefix="/ws", tags=["websocket"]) 