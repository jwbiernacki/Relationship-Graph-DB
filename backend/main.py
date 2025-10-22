from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "EntityGraph API running"}

@app.post("/entities/")
def create_entity(entity: schemas.EntityCreate, db: Session = Depends(get_db)):
    db_entity = models.Entity(id=str(uuid4()), **entity.dict())
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity

@app.get("/entities/")
def read_entities(db: Session = Depends(get_db)):
    return db.query(models.Entity).all()

@app.post("/relationships/")
def create_relationship(rel: schemas.RelationshipCreate, db: Session = Depends(get_db)):
    db_rel = models.Relationship(id=str(uuid4()), **rel.dict())
    db.add(db_rel)
    db.commit()
    db.refresh(db_rel)
    return db_rel

@app.get("/relationships/")
def read_relationships(db: Session = Depends(get_db)):
    return db.query(models.Relationship).all()
