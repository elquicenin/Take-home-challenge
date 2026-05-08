from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime

#At the moment start project 
App=FastAPI() 

# for the moment we will be using a simple list to save the data, because later i will create a database to save the data 
task = []

class ModelTask(BaseModel): #In fastAPI use Pydantic models to define the structure of the data and validate the type of the data that is being sent  the petition
    id: int
    title: str 
    description: Optional[Text] 
    created_at: datetime = datetime.now()

@App.get("/") # The endpoints in fastAPI are defined using decorators, in this case we are defining a GET endpoint at the root URL ("/") for viewing the home page.
def get_home():
    return {"message": "Hi this is a practices with FastAPI"}


@App.get("/data")
def get_data():
    return task


@App.post("/post_data")
def post_data(post: ModelTask):
    task.append(post)
    return {"message": "Data added successfully"}