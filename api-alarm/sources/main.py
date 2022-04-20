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
