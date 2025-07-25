from pydantic import BaseModel

class RegisterUser(BaseModel):
    username: str
    password: str

class LoginUser(BaseModel):
    username: str
    password: str

class ProductCreate(BaseModel):
    name: str
    price: float

class ProductResponse(BaseModel):
    message: str
    id: int
    name: str
    price: float
    # Include other fields you want to expose
    
    class Config:
        from_attributes = True