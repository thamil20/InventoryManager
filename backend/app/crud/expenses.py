from sqlalchemy.orm import Session
from backend.app import models, schemas

def create(db: Session, item: schemas.expenses.Create):
    expense = models.Expenses(
        title=item.title,
        description=item.description,
        expense_type=item.expense_type,
        cost=item.cost,
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def get_all(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Expenses).offset(skip).limit(limit).all()

def get_by_id(db: Session, expense_id: int):
    return db.query(models.Expenses).filter(models.Expenses.id == expense_id).first()

def get_by_type(db: Session, expense_type: str, skip: int = 0, limit: int = 50):
    return db.query(models.Expenses).filter(models.Expenses.expense_type == expense_type).skip(skip).limit(limit).all()

def update(db: Session, expense_id: int, updated_items: schemas.expenses.Update):
    expense = db.query(models.Expenses).filter(models.Expenses.id == expense_id).first()
    if not expense:
        return None

    updated_items = updated_items.model_dump(exclude_unset=True)
    for key, value in updated_items.items():
        setattr(expense, key, value)

    db.commit()
    db.refresh(expense)
    return expense

def delete(db: Session, expense_id: int):
    expense = db.query(models.Expenses).filter(models.Expenses.id == expense_id).first()
    if not expense:
        return None
    db.delete(expense)
    db.commit()
    return expense
