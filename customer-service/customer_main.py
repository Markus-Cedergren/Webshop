from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import os

class User(BaseModel):
    name:str
    password:str


app = FastAPI()


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "test")
DB_PASSWORD = os.getenv("DB_PASSWORD", "pass")
DB_NAME = os.getenv("DB_NAME", "customerdb")



def getConnection():
    return mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_NAME)


def checkLogin(name, password):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute(
        '''SELECT * FROM users WHERE username = %s AND password = %s''', (name, password)
    )
    match = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if match == None:
        return False
    else:
        return True

def addCustomer(name, password):
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(
            ''' INSERT INTO users (username, password) VALUES (%s,%s)''', (name, password)
        )
        connection.commit()
        cursor.close()
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
    
        


