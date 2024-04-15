from fastapi import APIRouter#, Response, HTTPException , status
from datetime import datetime
from models.results import Result, Text
#from typing import List
import json

from services.text_analyzer import analyze_text


result = APIRouter()

@result.get("/")
def read_root():
    return {"Hello": "World"}

@result.post('/analyze_comment',response_model=Result, tags=["Results"])
async def analyze_comment(payload: Text):    
    
    results = analyze_text(payload.text)

    result = Result(
        text=results['text'],
        score=results['score'],
        label=results['label'],
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    with open("analyzed_comments.jsonl", "a") as f:
        json.dump(dict(result), f)
        f.write("\n")

    return result