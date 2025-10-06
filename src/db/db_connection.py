import os
import sqlite3

from dotenv import load_dotenv

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
load_dotenv(os.path.join(ROOT_DIR, ".env"))

DB_PATH = os.getenv("DB_PATH")


def get_connection():
    if not DB_PATH:
        raise ValueError("❌ DB_PATH não definido no arquivo .env")
    return sqlite3.connect(DB_PATH)
