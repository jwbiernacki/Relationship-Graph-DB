from pydantic import BaseModel
from typing import Optional

class EntityBase(BaseModel):
    name: str
    type: str
    description: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    url: Optional[str] = None
    tags: Optional[str] = None

class EntityCreate(EntityBase):
    id: Optional[str] = None

class Entity(EntityBase):
    id: str
    class Config:
        orm_mode = True

class RelationshipBase(BaseModel):
    source_id: str
    target_id: str
    relation_type: str
    notes: Optional[str] = None

class RelationshipCreate(RelationshipBase):
    id: Optional[str] = None

class Relationship(RelationshipBase):
    id: str
    class Config:
        orm_mode = True
