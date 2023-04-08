import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv(".env")


BASE_DIR = Path(__file__).resolve().parent
MEDIA_DIR = BASE_DIR / ""

engine = create_engine("sqlite:///app.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER = os.getenv("USER")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
DB_USER = os.getenv("DB_NAME")
