from pydantic import BaseModel
from typing import List
from datetime import datetime

class Payload(BaseModel):
    batchid: str
    payload: List[List[int]]

class Output(BaseModel):
    batchid: str
    response: list
    status: str
    started_at : datetime
    completed_at: datetime


