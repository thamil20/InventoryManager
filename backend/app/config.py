from dotenv import load_dotenv
import os
from pathlib import Path
load_dotenv(override=True)
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = 5432
DB_NAME = os.getenv("DB_NAME")
DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
PROJECT_ROOT = Path(__file__).resolve().parent
IMAGE_UPLOAD_DIR = os.getenv("IMAGE_UPLOAD_DIR", str(PROJECT_ROOT / "images"))
