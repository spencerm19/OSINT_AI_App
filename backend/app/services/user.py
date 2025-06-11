from typing import Optional, List
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.security import get_password_hash, verify_password, generate_uuid
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(self, user_id: str) -> Optional[User]:
        """
        Get a user by ID.
        """
        query = select(User).where(User.id == user_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Optional[User]:
        """
        Get a user by email.
        """
        query = select(User).where(User.email == email)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def get_multi(
        self,
        skip: int = 0,
        limit: int = 100,
    ) -> List[User]:
        """
        Get multiple users.
        """
        query = select(User).offset(skip).limit(limit)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def create(self, user_in: UserCreate) -> User:
        """
        Create new user.
        """
        user = User(
            id=generate_uuid(),
            email=user_in.email,
            hashed_password=get_password_hash(user_in.password),
            full_name=user_in.full_name,
            is_active=True,
            is_admin=user_in.is_admin,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def update(
        self,
        user: User,
        user_in: UserUpdate,
    ) -> User:
        """
        Update user.
        """
        update_data = user_in.dict(exclude_unset=True)
        if update_data.get("password"):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password

        update_data["updated_at"] = datetime.utcnow()

        for field, value in update_data.items():
            setattr(user, field, value)

        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def delete(self, user_id: str) -> bool:
        """
        Delete user.
        """
        user = await self.get(user_id)
        if not user:
            return False

        await self.db.delete(user)
        await self.db.commit()
        return True

    async def authenticate(self, email: str, password: str) -> Optional[User]:
        """
        Authenticate user.
        """
        user = await self.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def is_active(self, user: User) -> bool:
        """
        Check if user is active.
        """
        return user.is_active

    async def is_admin(self, user: User) -> bool:
        """
        Check if user is admin.
        """
        return user.is_admin 