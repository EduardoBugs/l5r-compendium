import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# --- Load environment variables ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
load_dotenv(os.path.join(ROOT_DIR, ".env"))

DB_PATH = os.getenv("DB_PATH")
if not DB_PATH:
    raise ValueError("❌ DB_PATH is not set in .env file")

# --- SQLAlchemy Engine configuration ---
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    DATABASE_URL,
    echo=False,  # set to True for SQL debug logs
    future=True,
)

# --- Session factory ---
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)


# --- Declarative Base ---
class Base(DeclarativeBase):
    """Base class for all ORM models."""

    pass


def get_session():
    """Return a new SQLAlchemy session."""
    return SessionLocal()


def init_db():
    """Create all tables if they do not exist yet."""

    Base.metadata.create_all(bind=engine)
    print("✅ Database schema initialized successfully.")
