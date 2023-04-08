import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv(".env")

engine = create_engine("app.db")
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER = os.getenv("USER")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
DB_USER = os.getenv("DB_NAME")
