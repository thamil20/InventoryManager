from backend.app.database import engine, get_db
from backend.app.models import Base
from backend.app.models import CurrentInventory
from backend.app.models import Incomes
from backend.app.models import Expenses
from backend.app.models import SoldInventory
from sqlalchemy import select, insert, update, delete, text

def test_db(db_name):
    db_gen = get_db()
    db = next(db_gen)
    try:
        query = f"SELECT * FROM {db_name}"
        result = db.execute(text(query))
        print(result.scalar())
    finally:
        db_gen.close()

test_db('incomes')
test_db('expenses')
test_db('sold_inventory')
test_db('current_inventory')