from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from schemas import RegisterUser,LoginUser,Product

app = FastAPI()
users_db = {}
products_db = []

@app.get("/")
def read_root():
    return{"message":"Welcome to the Backend of Ecomerce System"}

@app.get("/greet")
def greet_user(name = Optional[str] == None):
    if name:
        return {"message":f"Hello!,{name}"}
    return {"message":"Hello There!"}

@app.post("/register")
def register_user(user:RegisterUser):
    if user in users_db:
        return{"message":"You are already registered"}
    else:
        users_db[user.username]==user.password
        
@app.post("/login")
def login(user: LoginUser):
    if user not in users_db or user.username==user.password:
        return{"message":"Invalid,user name or password in not correct"}
    else:
        return {"message": f"Welcome back, {user.username}!"}
    
@app.post("/add-product")
def add_product(product: Product):
    products_db.append(product)
    return {"message": "Product added", "product": product}       
@app.get("/showproducts")
def get_products(products_db):
    return {"products": products_db}