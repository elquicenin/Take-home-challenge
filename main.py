from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Text, Optional, Annotated
from datetime import datetime
from uuid import uuid4
from fastapi.encoders import jsonable_encoder



app = FastAPI()
 
class User(BaseModel):
    id_user: str 
    first_name: str 
    last_name: str
    age: int | None
    task: list = []


Users = []

@app.post('/create-user')
async def create_user(user: User):
    user.id_user = str(uuid4()) #el metodo uuid va a crear un id aleatorio que lo guardara automaticamente en el json o payload
    Users.append(user)
    return Users[-1]

@app.get('/users') # recordar siempre que las rutas de los endpoints deben de ir primero con un / y luego la ruta para llevar una continuidad 
async def all_users():
    print(Users)
    return Users


@app.get('/user/{id_user}')
async def get_user(id_user : str):
    for user in Users:
        if user.id_user == id_user:
            return user
    return False
    
@app.delete('/user-delete/{id_user}')
async def get_user(id_user : str):
    for index, user in enumerate(Users): # el enumerate que enumere el indice de cada obejtop almacenado en la lista y asi poderlo borrar y que los demas ocupen ese ligar en la lista
        if user.id_user == id_user:
            Users.pop(index)
        return "delete sucessful"
    return False


@app.put('/update/{id_user}', response_model=User) 
async def update_item(id_user: str, updateuser: User):
    for index, user in enumerate(Users):
        if user.id_user == id_user:
            update_user_encoded = jsonable_encoder(updateuser)
            Users[index] = update_user_encoded
            return update_user_encoded
    return("update not sucessfull")

