from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware
class Item(BaseModel):
    name:str
    price:int


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # för test: tillåt alla
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"customer" : "service"}





@app.get("/show_items")
def items():
    url = f"http://localhost:8000/all_items"
    response = requests.get(url)
    return response.json()
    