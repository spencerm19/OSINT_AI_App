from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.research import Research
from app.schemas.research import ResearchCreate, ResearchUpdate, ResearchFilters
from app.core.security import generate_uuid
from datetime import datetime

class ResearchService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user_id: str, research_in: ResearchCreate) -> Research:
        """
        Create a new research entry.
        """
        research = Research(
            id=generate_uuid(),
            user_id=user_id,
            query=research_in.query,
            source=research_in.source,
            status="pending",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        self.db.add(research)
        await self.db.commit()
        await self.db.refresh(research)
        return research

    async def get(self, user_id: str, research_id: str) -> Optional[Research]:
        """
        Get a research entry by ID.
        """
        query = select(Research).where(
            Research.id == research_id,
            Research.user_id == user_id,
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def get_multi(
        self,
        user_id: str,
        skip: int = 0,
        limit: int = 100,
        filters: Optional[ResearchFilters] = None,
    ) -> List[Research]:
        """
        Get multiple research entries with optional filtering.
        """
        query = select(Research).where(Research.user_id == user_id)

        if filters:
            if filters.source:
                query = query.where(Research.source.in_(filters.source))
            if filters.status:
                query = query.where(Research.status == filters.status)
            if filters.date_range:
                if filters.date_range.start:
                    query = query.where(Research.created_at >= filters.date_range.start)
                if filters.date_range.end:
                    query = query.where(Research.created_at <= filters.date_range.end)

        query = query.offset(skip).limit(limit)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def update(
        self,
        user_id: str,
        research_id: str,
        research_in: ResearchUpdate,
    ) -> Optional[Research]:
        """
        Update a research entry.
        """
        research = await self.get(user_id, research_id)
        if not research:
            return None

        update_data = research_in.dict(exclude_unset=True)
        update_data["updated_at"] = datetime.utcnow()

        for field, value in update_data.items():
            setattr(research, field, value)

        await self.db.commit()
        await self.db.refresh(research)
        return research

    async def delete(self, user_id: str, research_id: str) -> bool:
        """
        Delete a research entry.
        """
        research = await self.get(user_id, research_id)
        if not research:
            return False

        await self.db.delete(research)
        await self.db.commit()
        return True

    async def update_status(
        self,
        user_id: str,
        research_id: str,
        status: str,
        results: Optional[dict] = None,
    ) -> Optional[Research]:
        """
        Update research status and results.
        """
        research = await self.get(user_id, research_id)
        if not research:
            return None

        research.status = status
        if results:
            research.results = results
        research.updated_at = datetime.utcnow()

        await self.db.commit()
        await self.db.refresh(research)
        return research 