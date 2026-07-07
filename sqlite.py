import sqlite3
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session

app = FastAPI()
DATABASE_URL = "sqlite:///./test.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})

# Create a session factory
sessionLocal = sessionmaker(bind=engine)

# Create a base class for the models
Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)

Base.metadata.create_all(bind=engine)

app = FastAPI()

def db_health_check():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create API 
@app.post("/todos")
def create_todo(title:str, db: Session = Depends(db_health_check)):
    todo = Todo(title=title, completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Created",
        "data":todo
    }