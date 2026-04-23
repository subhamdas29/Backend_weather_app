import os
import requests
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from db import SessionLocal, engine, get_db
import models
import schemas
from hashing import Hash
from typing import List
import authentication
import oauth2

models.Base.metadata.create_all(bind=engine)

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

app = FastAPI()

# 2. Fix CORS (This allows your frontend to talk to your backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, you'd change this to your site's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/weather")
def get_weather(city: str,  current_user: schemas.User=Depends(oauth2.get_current_user)):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

@app.get("/forecast")
def get_forecast(city: str,  current_user: schemas.User=Depends(oauth2.get_current_user)):
    
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()



@app.post("/Users")
def create_users(request: schemas.User, db: Session=Depends(get_db) , current_user: schemas.User=Depends(oauth2.get_current_user)):
    
    new_user=models.User(username=request.username, email=request.email, password=Hash.bcrypt(request.password) , home_city=request.home_city)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/Users", response_model=List[schemas.ShowUser])
def get_users(db: Session=Depends(get_db),  current_user: schemas.User=Depends(oauth2.get_current_user)):
    users=db.query(models.User).all()
    return users

app.include_router(authentication.router)