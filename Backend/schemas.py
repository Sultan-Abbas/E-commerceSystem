from pydantic import BaseModel

class RegisterUser(BaseModel):
    username: str
    password: str

class LoginUser(BaseModel):
    username: str
    password: str

class Product(BaseModel):
    name: str
    price: float
#Clases