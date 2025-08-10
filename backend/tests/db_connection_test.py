from backend.app.database import engine
from sqlalchemy.exc import OperationalError

def test_connection():
    try:
        with engine.connect() as conn:
            print("Connection established")
    except OperationalError as e:
        print("Connection failed")
        print("Error:", e)

if __name__ == "__main__":
    test_connection()
