from fastapi import FastAPI, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from pydantic import BaseModel
from schemas import RegisterUser,LoginUser,Product
from database import get_db
from model import user, product

app = FastAPI()
users_db = {}
products_db = []
#home
@app.get("/home")
def read_root():
    return{"message":"Welcome to the Backend of Ecomerce System"}
#Greet
@app.get("/greet")
def greet_user(name = Optional[str] == None):
    if name:
        return {"message":f"Hello!,{name}"}
    return {"message":"Hello There!"}
#register
@app.post("/register")
def register_user(user:RegisterUser):
    if user in users_db:
        return{"message":"You are already registered"}
    else:
        users_db[user.username]==user.password
#login     
@app.post("/login")
def login(user: LoginUser):
    if user not in users_db or user.username==user.password:
        return{"message":"Invalid,user name or password in not correct"}
    else:
        return {"message": f"Welcome back, {user.username}!"}
    
#add_product   
@app.post("/add-product")
def add_product(product: Product):
    products_db.append(product)
    return {"message": "Product added", "product": product}  

#Shows_products     
@app.get("/showproducts")
def get_products(products_db):
    return {"products": products_db}

#delete_products
@app.delete("/delete-product/{product_name}")
def delete_product(product_name: str):
    for index, product in enumerate(products_db):
        if product.name == product_name:
            products_db.pop(index)
            return {"message": f"Product '{product_name}' deleted"}
    raise HTTPException(status_code=404, detail="Product not found")

#update_products
@app.put("/update-product/{product_name}")
def update_product(product_name: str, updated_product: Product):
    for index, product in enumerate(products_db):
        if product.name == product_name:
            products_db[index] = updated_product
            return {"message": f"Product '{product_name}' updated"}
    raise HTTPException(status_code=404, detail="Product not found")