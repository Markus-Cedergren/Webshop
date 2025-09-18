from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class User(BaseModel):
    name:str
    password:str


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # för test: tillåt alla
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = [User(name = "markus", password="123"), User(name = "carl", password="hello"), User(name = "lukas", password="321")]


@app.get("/")
def root():
    return {"hello" : "from customer service"}



@app.post("/login")
def get_item(user: User):
    for stored_user in users:
        if (user.name == stored_user.name) and (user.password == stored_user.password):
            return {"loggin_sucess" : True}
    
    return {"loggin_sucess" : False}
    