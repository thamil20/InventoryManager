from backend.app.config import DB_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
logger = logging.getLogger("backend_logger")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
