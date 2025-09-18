from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

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

db_path = "mydatabase.db"



def checkLogin(name, password):
    connection = sqlite3.connect(db_path)
    cursor = connection.execute(
        '''SELECT * FROM users WHERE username = ? AND password = ?''', (name, password)
    )
    match = cursor.fetchone()
    connection.close()
    if match == None:
        return False
    else:
        return True

def addCustomer(name, password):
    try:
        connection = sqlite3.connect(db_path)
        connection.execute(
            ''' INSERT INTO users (username, password) VALUES (?,?)''', (name, password)
        )
        connection.commit()
        connection.close()
        return True
    except:
        return False


@app.get("/")
def root():
    return {"hello" : "from customer service"}



@app.post("/login")
def get_item(user: User):
    if checkLogin(user.name, user.password) == True:
        return {"success": True}
    else:
        return {"success": False}

    
    
@app.post("/addAccount")
def add_account(user: User):
    if addCustomer(user.name, user.password) == True:
        return {"success": True}
    else:
        return {"success": False}
    
        


