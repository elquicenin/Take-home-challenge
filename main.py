from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Text, Optional, Annotated
from datetime import datetime
from uuid import uuid4
from fastapi.encoders import jsonable_encoder
from app.db.CreateModels import create_db_and_tables



app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables
    
### en pocas palabras despues de estudiar mas la clean architecture entiendo porque se deberia de aplicar a proyectos de software ###