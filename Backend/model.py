from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(100))

class Product(Base):
    __tablename__ ="products"
    id=Column(Integer,index=True,primary_key=True)
    name = Column(String,unique=True,index=True)
    price = Column(Float)