from sqlalchemy.orm import Session
from backend.app import models, schemas

def create(db: Session, item: schemas.incomes.Create):
    income = models.Incomes(
        title=item.title,
        description=item.description,
        income_type=item.income_type,
        amount=item.amount,
    )
    db.add(income)
    db.commit()
    db.refresh(income)
    return income

def get_all(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Incomes).offset(skip).limit(limit).all()

def get_by_id(db: Session, income_id: int):
    return db.query(models.Incomes).filter(models.Incomes.id == income_id).first()

def get_by_type(db: Session, income_type: str, skip: int = 0, limit: int = 50):
    return db.query(models.Incomes).filter(models.Incomes.income_type == income_type).skip(skip).limit(limit).all()

def update(db: Session, income_id: int, updated_items: schemas.expenses.Update):
    income = db.query(models.Incomes).filter(models.Incomes.id == income_id).first()
    if not income:
        return None

    updated_items = updated_items.model_dump(exclude_unset=True)
    for key, value in updated_items.items():
        setattr(income, key, value)

    db.commit()
    db.refresh(income)
    return income

def delete(db: Session, income_id: int):
    income = db.query(models.Incomes).filter(models.Incomes.id == income_id).first()
    if not income:
        return None
    db.delete(income)
    db.commit()
    return income