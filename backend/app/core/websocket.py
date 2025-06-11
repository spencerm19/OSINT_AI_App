from typing import Dict, Set
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        # Map of user_id to set of WebSocket connections
        self.active_connections: Dict[str, Dict[str, WebSocket]] = {}

    async def connect(
        self,
        websocket: WebSocket,
        client_id: str,
        user_id: str,
    ) -> None:
        """
        Connect a new WebSocket client.
        """
        await websocket.accept()
        if user_id not in self.active_connections:
            self.active_connections[user_id] = {}
        self.active_connections[user_id][client_id] = websocket

    def disconnect(self, websocket: WebSocket, client_id: str) -> None:
        """
        Disconnect a WebSocket client.
        """
        for user_id, connections in self.active_connections.items():
            if client_id in connections and connections[client_id] == websocket:
                del connections[client_id]
                if not connections:
                    del self.active_connections[user_id]
                break

    async def send_personal_message(
        self,
        message: str,
        websocket: WebSocket,
    ) -> None:
        """
        Send a message to a specific WebSocket connection.
        """
        await websocket.send_text(message)

    async def broadcast_to_user(self, user_id: str, message: str) -> None:
        """
        Broadcast a message to all connections of a specific user.
        """
        if user_id in self.active_connections:
            disconnected = []
            for client_id, websocket in self.active_connections[user_id].items():
                try:
                    await websocket.send_text(message)
                except:
                    disconnected.append((websocket, client_id))

            # Clean up any disconnected clients
            for websocket, client_id in disconnected:
                self.disconnect(websocket, client_id)

    async def broadcast(self, message: str) -> None:
        """
        Broadcast a message to all connected clients.
        """
        disconnected = []
        for user_id, connections in self.active_connections.items():
            for client_id, websocket in connections.items():
                try:
                    await websocket.send_text(message)
                except:
                    disconnected.append((websocket, client_id))

        # Clean up any disconnected clients
        for websocket, client_id in disconnected:
            self.disconnect(websocket, client_id) 