from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()


class Item(BaseModel):
    

@app.get('/')
def index():
    return {'message':'Hello'}

@app.get('/greet/{name}')
def greet_name(name:str):
    return {'greeting':f'Hello {name}'}