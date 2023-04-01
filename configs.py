import os

from dotenv import load_dotenv

load_dotenv(".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER = os.getenv("USER")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
DB_USER = os.getenv("DB_NAME")
