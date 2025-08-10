from backend.app.models import Base
from backend.app.models import CurrentInventory
from backend.app.models import SoldInventory
from backend.app.models import Expenses
from backend.app.models import Incomes
from backend.app.database import engine

def test_tables():
    Base.metadata.create_all(engine)
    print(CurrentInventory())
    print(SoldInventory())
    print(Expenses())
    print(Incomes())

test_tables()

