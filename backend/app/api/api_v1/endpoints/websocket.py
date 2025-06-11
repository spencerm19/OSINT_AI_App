from typing import Any
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from app.core.websocket import ConnectionManager
from app.api import deps
from app.models.user import User
from app.schemas.websocket import WebSocketMessage
import json

router = APIRouter()
manager = ConnectionManager()

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    client_id: str,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    WebSocket endpoint for real-time updates.
    """
    await manager.connect(websocket, client_id, current_user.id)
    try:
        while True:
            data = await websocket.receive_text()
            try:
                message = WebSocketMessage.parse_raw(data)
                # Handle different message types
                if message.type == "research_update":
                    # Broadcast research updates to all connected clients
                    await manager.broadcast_to_user(
                        current_user.id,
                        json.dumps({
                            "type": "research_update",
                            "data": message.data,
                        }),
                    )
                elif message.type == "graph_update":
                    # Broadcast graph updates to all connected clients
                    await manager.broadcast_to_user(
                        current_user.id,
                        json.dumps({
                            "type": "graph_update",
                            "data": message.data,
                        }),
                    )
            except Exception as e:
                await websocket.send_json({
                    "error": f"Invalid message format: {str(e)}"
                })
    except WebSocketDisconnect:
        manager.disconnect(websocket, client_id)

@router.post("/broadcast")
async def broadcast_to_user(
    *,
    user_id: str,
    message: WebSocketMessage,
    current_user: User = Depends(deps.get_current_admin_user),
) -> Any:
    """
    Broadcast a message to all connections of a specific user.
    Requires admin privileges.
    """
    await manager.broadcast_to_user(
        user_id,
        json.dumps({
            "type": message.type,
            "data": message.data,
        }),
    )
    return {"status": "message broadcast"} 