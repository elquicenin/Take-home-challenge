from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

model = SQLModel #created a instace of SQLModel  

class user(model, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str 
    email: str = Field(index=True, unique=True)