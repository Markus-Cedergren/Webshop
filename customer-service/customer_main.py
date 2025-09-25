from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import os
import time

class User(BaseModel): #Define class for communicating. (Fast API)
    name:str
    password:str


app = FastAPI()


DB_HOST = os.getenv("DB_HOST") #Get the DB_HOST from env
DB_USER = os.getenv("DB_USER") #Get the DB_USER from env
DB_PASSWORD = os.getenv("DB_PASSWORD") #Get the DB_PASSWORD frome env
DB_NAME = os.getenv("DB_NAME") #Get the DB_NAME from env


def getConnection(): #Create a connection to the database
    return mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_NAME)




def init_database():
    for try_connect in range(10):
        try:
            connection = getConnection()
            cursor = connection.cursor()
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS users(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255),
                    password VARCHAR(255)
                ); '''
            )
            connection.commit()
            cursor.close()
            connection.close()
            print("--initiated users-table --")
            return
        except:
            time.sleep(5)

init_database()




def checkLogin(name, password): #Check if a password and username is existing in the database. 
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

def addCustomer(name, password): #Try to add add a new customer to the database
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


@app.get("/") #Default endpoint
def root():
    return {"hello" : "from customer service"}



@app.post("/login") #Login endpoint
def get_item(user: User):
    if checkLogin(user.name, user.password) == True:
        return {"success": True}
    else:
        return {"success": False}

    
    
@app.post("/addAccount") #addAccount endpoint
def add_account(user: User):
    if addCustomer(user.name, user.password) == True:
        return {"success": True}
    else:
        return {"success": False}
    
        


