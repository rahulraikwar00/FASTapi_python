from fastapi import FastAPI
from fastapi.params import Path
# from pydantic.utils import Representation, is_valid_field
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Ptem(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


inventory = {
    1: {
        'name': 'Milk',
        'price': 3.99,
        'brand': 'Amul'
    }
}


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
def get_item(item_id: int = Path(None, description="The ID of Item needs to be an Integer", gt=0, lt=2)):
    return inventory[item_id]


@app.get('/get-by-name/{item_id}')
def get_item(*, item_id: int, name: Optional[str] = None, test: int,):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {'Data': 'Not Found'}


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Ptem):
    if item_id in inventory:
        return {"Error": "item ID already exists"}
    inventory[item_id] = {"name": item.name,
                          "brand": item.brand, "price": item.price}
    print(inventory)
    return inventory[item_id]
