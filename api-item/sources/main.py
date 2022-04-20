# from typing import Optional

from fastapi import FastAPI
# from enum import Enum
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    broadcaster: str
    category: str
    price: int
    is_alarm_set: bool

class User(BaseModel):
    id: int
    name: str
    access_token: str


app = FastAPI()
# @app.get("/")
# async def root():
#     return { "message": "Hello World" }

""" 상품 API입니다. """
item_api = 'item_api'
item_id = 'item_id'

@app.get('/{item_api}/')
async def getItemList():
    return [
        { 
            "id": 50, 
            "name": "17WINTER 레그미인",
            "broadcaster": "cjmall",
            "category": "패션·잡화",
            "price": 78900,
            "is_alarm_set": True
        },
        { 
            "id": 50, 
            "name": "17WINTER 레그미인",
            "broadcaster": "cjmall",
            "category": "패션·잡화",
            "price": 78900,
            "is_alarm_set": True
        }
    ]

@app.get('/{item_api}/{item_id}')
async def getItemDetails(item_id: int):
    return {
        "id": item_id, 
        "name": "[역대최다-13종]17WINTER 레그미인",
        "broadcaster": "cjmall",
        "category": "패션·잡화",
        "price": 78900,
        "is_alarm_set": True
    }
