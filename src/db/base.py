import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# --- Load environment variables ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
load_dotenv(os.path.join(ROOT_DIR, ".env"))

# --- Read environment variables ---
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

if not DB_NAME or not DB_USER:
    raise ValueError("❌ Missing database credentials in .env file")

# --- SQLAlchemy PostgreSQL URL ---
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# --- SQLAlchemy Engine configuration ---
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
