from fastapi import FastAPI, HTTPException, Depends
from typing import Optional
from sqlalchemy.orm import Session
from pydantic import BaseModel
from schemas import RegisterUser,LoginUser,Product
from database import get_db
from model import User, Product

app = FastAPI()
# users_db = {}
# products_db = []
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
def register_user(user:RegisterUser,db:Session=Depends(get_db)):
    db_user= db.query(User).filter(User.username==user.username ).first()
    if db_user:
        raise HTTPException(status_code=400,detail="User Already Exists")
    new_user=User(username=user.username,password=user.password)
    db.add(new_user)
    db.commit()
    """ When you create and commit a new database record:
    The Python object (new_user) initially only has the data you provided (e.g., username and password).
    The database may auto-generate additional values (like id, created_at, or server-side defaults) that aren't 
    in your Python object yet.SO we Use Refresh"""
    db.refresh()
    return {"message": "User registered successfully"}
#login     
@app.post("/login")
def login(user: LoginUser,db:Session=Depends(get_db)):
    db_user= db.query(User).filter(User.username==user.username ).first()
    if not db_user or db_user.password != user.password:  # Later: use password hashing!
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": f"Welcome back, {user.username}!"}
    
#add_product   
@app.post("/add-product")
def add_product(product: Product,db:Session=Depends(get_db)):
    existing_product= db.query(Product).filter(product.name==Product.name).first()
    if existing_product:
        raise HTTPException(status_code=400,detail="Product Already Exists")
    new_product=Product(name=product.name,price=product.price)
    db.add(new_product)
    db.commit()
    db.refresh()
    return {"message": "Product added", "product": product}  

#Shows_products     
@app.get("/showproducts")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return {"products": products}

#delete_products
@app.delete("/delete-product/{product_name}")
def delete_product(product_name: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.name == product_name).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return {"message": f"Product '{product_name}' deleted"}

#update_products
@app.put("/update-product/{product_name}")
def update_product(product_name: str, updated_product: Product, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.name == product_name).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product.name = updated_product.name
    product.price = updated_product.price
    db.commit()
    db.refresh(product)
    return {"message": f"Product '{product_name}' updated"}