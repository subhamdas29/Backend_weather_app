from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Fetching variables from .env
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")  # Good practice to provide a default
db_name = "weather_app"

# FIX: Use an f-string to insert the variables into the string
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"

# The engine handles the connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Session setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
# 1. This command scrubs 'db.env' from every single commit in your history
