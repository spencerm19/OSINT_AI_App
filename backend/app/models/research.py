from sqlalchemy import Column, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Research(Base):
    __tablename__ = "research"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    query = Column(String, nullable=False)
    source = Column(String, nullable=False)
    status = Column(String, nullable=False)  # pending, running, completed, failed
    results = Column(JSON, nullable=True)
    error = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    # Relationships
    user = relationship("User", back_populates="research")
    nodes = relationship("Node", back_populates="research", cascade="all, delete-orphan")
    edges = relationship("Edge", back_populates="research", cascade="all, delete-orphan") 