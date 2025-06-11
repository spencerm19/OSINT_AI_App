from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.api import deps
from app.schemas.research import (
    ResearchCreate,
    ResearchUpdate,
    ResearchResponse,
    ResearchFilters,
    Research,
)
from app.services.research import ResearchService
from app.core.security import get_current_user
from app.models.user import User
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=Research)
async def create_research(
    research: ResearchCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create new research project"""
    research_service = ResearchService(db)
    return await research_service.create(research)

@router.get("/{research_id}", response_model=Research)
async def get_research(
    research_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get research project by ID"""
    research_service = ResearchService(db)
    research = await research_service.get(research_id)
    if not research:
        raise HTTPException(status_code=404, detail="Research not found")
    return research

@router.get("/", response_model=List[Research])
async def list_research(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    """List research projects"""
    research_service = ResearchService(db)
    return await research_service.list(skip=skip, limit=limit)

@router.put("/{research_id}", response_model=Research)
async def update_research(
    research_id: int,
    research: ResearchUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update research project"""
    research_service = ResearchService(db)
    updated = await research_service.update(research_id, research)
    if not updated:
        raise HTTPException(status_code=404, detail="Research not found")
    return updated

@router.delete("/{research_id}")
async def delete_research(
    research_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete research project"""
    research_service = ResearchService(db)
    success = await research_service.delete(research_id)
    if not success:
        raise HTTPException(status_code=404, detail="Research not found")
    return {"status": "success"} 