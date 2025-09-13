from fastapi import FastAPI
from pydantic import BaseModel
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

items = [Item(name = "bannan", price = 100), Item(name = "Apple", price = 1), Item(name = "Orange", price = 2)]


@app.get("/")
def root():
    return {"hello" : "World"}


@app.post("/items")
def create_item(item:Item):
    return items


@app.get("/all_items")
def get_item():
    return items