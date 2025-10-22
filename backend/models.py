from sqlalchemy import Column, String, Float, Enum, Text, ForeignKey
from sqlalchemy.dialects.sqlite import BLOB
from sqlalchemy.orm import relationship
from .database import Base

class Entity(Base):
    __tablename__ = "entities"
    id = Column(String, primary_key=True)
    name = Column(String, index=True)
    type = Column(String)
    description = Column(Text)
    lat = Column(Float)
    lon = Column(Float)
    url = Column(String)
    tags = Column(String)

    sources = relationship("Relationship", back_populates="source", foreign_keys="Relationship.source_id")
    targets = relationship("Relationship", back_populates="target", foreign_keys="Relationship.target_id")

class Relationship(Base):
    __tablename__ = "relationships"
    id = Column(String, primary_key=True)
    source_id = Column(String, ForeignKey("entities.id"))
    target_id = Column(String, ForeignKey("entities.id"))
    relation_type = Column(String)
    notes = Column(Text)

    source = relationship("Entity", foreign_keys=[source_id], back_populates="sources")
    target = relationship("Entity", foreign_keys=[target_id], back_populates="targets")
