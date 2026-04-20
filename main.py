import os
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from db import SessionLocal, engine
import models

# This command creates all tables defined in your models
models.Base.metadata.create_all(bind=engine)

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

app = FastAPI()

# 2. Fix CORS (This allows your frontend to talk to your backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, you'd change this to your site's URL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/weather")
def get_weather(city: str):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

@app.get("/forecast")
def get_forecast(city: str):
    
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()