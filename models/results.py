from pydantic import BaseModel, Field#, HttpUrl
#from typing import Optional
from datetime import datetime

class Text(BaseModel):
    text: str

class Result(BaseModel):
    text: str
    score: float
    label: str
    timestamp: str = Field(example="2023-10-23 14:30:00")
    #id: Optional[str] = None