from typing import Dict, Any, Literal
from pydantic import BaseModel, Field

class WebSocketMessage(BaseModel):
    type: Literal["research_update", "graph_update", "notification"]
    data: Dict[str, Any]

class ResearchUpdateMessage(WebSocketMessage):
    type: Literal["research_update"]
    data: Dict[str, Any] = Field(
        ...,
        example={
            "research_id": "123",
            "status": "completed",
            "results": {"key": "value"},
        },
    )

class GraphUpdateMessage(WebSocketMessage):
    type: Literal["graph_update"]
    data: Dict[str, Any] = Field(
        ...,
        example={
            "nodes": [
                {
                    "id": "1",
                    "label": "Person",
                    "properties": {"name": "John Doe"},
                }
            ],
            "edges": [
                {
                    "id": "1",
                    "source": "1",
                    "target": "2",
                    "type": "KNOWS",
                }
            ],
        },
    )

class NotificationMessage(WebSocketMessage):
    type: Literal["notification"]
    data: Dict[str, Any] = Field(
        ...,
        example={
            "type": "info",
            "message": "Research completed successfully",
            "duration": 5000,
        },
    ) 