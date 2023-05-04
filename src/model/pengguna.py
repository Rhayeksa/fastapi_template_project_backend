from sqlalchemy import Column, Integer, String, DateTime

from src.config.database import Base


class Pengguna(Base):
    __tablename__ = "pengguna"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), unique=True, nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
