from fastapi import FastAPI
from fastapi.params import Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Ptem(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


inventory = {}


@app.get('/')
def home():
    '''
    it dosent take any parameter as such
    '''
    return {'data': 'data key'}


@app.get('/about')
def about():
    return {'data': 'about'}


class Item:
    def __init__(self) -> None:
        pass


@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(None, description="The ID of Item needs to be an Integer")):
    return inventory[item_id]


@app.get('/get-by-name/')
def get_item(name:str):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {'Data': 'Not Found'}


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Ptem):
    if item_id in inventory:
        return {"Error": "item ID already exists"}
    inventory[item_id] = item
    print(inventory)
    return inventory[item_id]
