from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class DateRange(BaseModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None

class ResearchFilters(BaseModel):
    source: Optional[List[str]] = None
    status: Optional[str] = None
    date_range: Optional[DateRange] = None

class ResearchBase(BaseModel):
    """Base research model"""
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    tags: List[str] = Field(default_factory=list)

class ResearchCreate(ResearchBase):
    """Research creation model"""
    pass

class ResearchUpdate(ResearchBase):
    """Research update model"""
    title: Optional[str] = Field(None, min_length=1, max_length=255)

class Research(ResearchBase):
    """Research response model"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ResearchInDBBase(ResearchBase):
    id: str
    user_id: str
    status: str
    results: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ResearchResponse(ResearchInDBBase):
    pass

class ResearchInDB(ResearchInDBBase):
    pass

# Node and Edge schemas for graph data
class NodeBase(BaseModel):
    label: str
    type: str
    properties: Dict[str, Any] = Field(default_factory=dict)

class NodeCreate(NodeBase):
    research_id: str

class NodeUpdate(NodeBase):
    pass

class NodeInDBBase(NodeBase):
    id: str
    research_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class NodeResponse(NodeInDBBase):
    pass

class EdgeBase(BaseModel):
    source_id: str
    target_id: str
    type: str
    properties: Dict[str, Any] = Field(default_factory=dict)

class EdgeCreate(EdgeBase):
    research_id: str

class EdgeUpdate(EdgeBase):
    pass

class EdgeInDBBase(EdgeBase):
    id: str
    research_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class EdgeResponse(EdgeInDBBase):
    pass

# Extended research response with graph data
class ResearchWithGraphResponse(ResearchResponse):
    nodes: List[NodeResponse]
    edges: List[EdgeResponse] 