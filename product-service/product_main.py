from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import os

class Item(BaseModel):
    name:str
    price:int


app = FastAPI()


DB_HOST = os.getenv("DB_HOST") #Find the value for DB_HOST
DB_USER = os.getenv("DB_USER") #Find the DB_USER
DB_PASSWORD = os.getenv("DB_PASSWORD") #Find the DB_PASSWORD
DB_NAME = os.getenv("DB_NAME") #Find the DB_NAME



def getConnection(): #Create connection to DB.
    return mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_NAME)


def getAllProducts():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM products''')
    products = cursor.fetchall()
    prodList = []
    for product in products:
        prodList.append(Item(name = product[1], price=product[2]))
    cursor.close()
    connection.close()
    return prodList
    
def addProduct(name, price):
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(
            '''INSERT INTO products (name,price) VALUES (%s,%s)''',(name, price)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except:
        connection.close()
        return False


@app.get("/")
def root():
    return {"hello" : "from product service"}


@app.get("/getProducts")
def get_item():
    return getAllProducts()

@app.post("/addProduct")
def add_item(item: Item):
    if addProduct(item.name, item.price) == True:
        return {"success" : True}
    else:
        return {"success" : False}
    