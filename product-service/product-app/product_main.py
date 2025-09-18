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

items = [Item(name = "Jeans", price = 100), Item(name = "T-shirt", price = 1), Item(name = "Orange", price = 2)]


@app.get("/")
def root():
    return {"hello" : "from product service"}


@app.get("/products")
def get_item():
    return items

@app.post("/addProduct")
def add_item(item: Item):
    try:
        items.append(Item(name = item.name, price = item.price))
        return {"sucess":"True"}
    except:
        return {"sucess" :"False"}
    