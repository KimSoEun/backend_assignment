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

""" 알람 API입니다. """
alarm_api = 'alarm_api'

@app.post("/{alarm_api}/")
async def setAlarm():
    return {}

@app.get("/{alarm_api}/")
async def getAlarmList():
    return []

@app.delete("{alarm_api}/")
async def deleteAlarm():
    return {}

""" 사용자 API입니다. """
user_api = "user_api"

@app.get("{user_api}/")
async def getUserList():
    return [ 
        {
            "id": 10, 
            "name": "박규경",
            "access_token": "4a49145e-45a8-4845-af45-1af2a59bb044"
        },
        {
            "id": 11, 
            "name": "박규",
            "access_token": "4a49145e-45a8-4845-af45-1af2a59bb048"
        }
    ]

@app.get("{user_api}/visit")
async def getVisitedItemList():
    return [
        {
            "id": 50, 
            "name": "[역대최다-13종]17WINTER 레그미인",
            "broadcaster": "cjmall",
            "category": "패션·잡화",
            "price": 78900,
            "is_alarm_set": True
        },
        {
            "id": 49, 
            "name": "[역대최다-12종]17WINTER 레그미인",
            "broadcaster": "cjmall",
            "category": "패션·잡화",
            "price": 78900,
            "is_alarm_set": False
        },
        {
            "id": 48, 
            "name": "[역대최다-11종]17WINTER 레그미인",
            "broadcaster": "cjmall",
            "category": "패션·잡화",
            "price": 78900,
            "is_alarm_set": False
        }
    ]
