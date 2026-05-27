from app.db.engine import engine
from sqlmodel import SQLModel, Session
from typing import Annotated
from fastapi import Depends

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_sesssion():
    with Session(engine) as sesion:
        yield sesion


SessionDep = Annotated[Session, Depends(get_sesssion)]