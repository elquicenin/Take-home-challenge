from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Text, Optional, Annotated
from datetime import datetime


class PracticeModel(BaseModel):
    name: str
    last_name: str | None = None 
    age: int
    country: str
    task: list[str] = []



#star the take home challenge which will be of notification users autenticated and posibility will have frontend 
app = FastAPI() #Here the created a instance of FastAPI for execute de Project


@app.post('/user/')
async def create_model(user: PracticeModel = Body(embed=True)):
    return user


# @app.put('update/user{user_id}')
# async def update_user(user_id: int, user: Annotated[PracticeModel, Body(embed=True)]):


