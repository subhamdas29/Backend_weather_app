from sqlalchemy import Column, Integer, String, Boolean
from db import Base  

class User(Base):
    __tablename__ = "users"

    
    username = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    home_city = Column(String, nullable=True)