from fastapi import FastAPI
from pydantic import BaseModel

class News(BaseModel):
     title: str
     description: str = None