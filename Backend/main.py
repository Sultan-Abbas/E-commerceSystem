from fastapi import FastAPI, HTTPException, Depends
from typing import Optional
from sqlalchemy.orm import Session
from pydantic import BaseModel
from schemas import RegisterUser,LoginUser,ProductCreate,ProductResponse
from database import get_db
from model import UserModel , Product as ProductModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 Allows all origins. Use caution in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# users_db = {}
# products_db = []
#home
@app.get("/home")
def read_root():
    return{"message":"Welcome to the Backend of Ecomerce System"}
#Greet
@app.get("/greet")
def greet_user(name : Optional[str] = None):
    if name:
        return {"message":f"Hello!,{name}"}
    return {"message":"Hello There!"}
#register
@app.post("/register")
def register_user(user: RegisterUser, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User Already Exists")
    
    new_user = UserModel(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}
#login     
@app.post("/login")
def login(user: LoginUser,db:Session=Depends(get_db)):
    db_user= db.query(UserModel).filter(UserModel.username==user.username ).first()
    if not db_user or db_user.password != user.password:  
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": f"Welcome back, {user.username}!"}
    
#add_product   
@app.post("/addproduct", response_model=ProductResponse)
def add_product(product: ProductCreate,db:Session=Depends(get_db)):
    existing_product= db.query(ProductModel).filter(ProductModel.name==product.name).first()
    if existing_product:
        raise HTTPException(status_code=400,detail="Product Already Exists")
    new_product=ProductModel(name=product.name,price=product.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return ProductResponse(
        message="Product added",
        id=new_product.id,
        name=new_product.name,
        price=new_product.price
    )

#Shows_products     
@app.get("/showproducts",response_model=ProductResponse)
def get_products(db: Session = Depends(get_db)):
    products = db.query(ProductModel).all()
    return products

#delete_products
@app.delete("/deleteproduct/{product_name}")
def delete_product(product_name: str, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.name == product_name).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return {"message": f"Product '{product_name}' deleted"}

#update_products
@app.put("/updateproduct/{product_name}")
def update_product(product_name: str, updated_product: ProductCreate, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.name == product_name).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product.name = updated_product.name
    product.price = updated_product.price
    db.commit()
    db.refresh(product)
    return {"message": f"Product '{product_name}' updated"}