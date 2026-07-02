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

@app.get("/home")
def home(db:Session = Depends(db_health_check)):
    return {
        "message": "Welcome to the FastAPI application with SQLAlchemy database!",
        "database_status": "Connected" if db else "Not Connected"
    }
