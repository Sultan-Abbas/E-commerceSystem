from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = "root"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = "3307"
DB_NAME = "ecommerce"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



#This is a dependency function used with FastAPI's Depends(). Its job is to provide a database session to your route functions.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()