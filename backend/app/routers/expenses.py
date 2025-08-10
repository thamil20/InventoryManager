from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.app import crud, schemas
from backend.app.database import get_db

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

@router.post('/', response_model=schemas.expenses.Response)
def create_expense(item: schemas.expenses.Create, db: Session = Depends(get_db)):
    expense = crud.expenses.create(db=db, item=item)
    if expense:
        raise HTTPException(status_code=404, detail="Expense already exists")
    return expense

@router.get('/', response_model=List[schemas.expenses.Response])
def get_all(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return crud.expenses.get_all(db=db, skip=skip, limit=limit)

@router.get('/{expense_id}', response_model=schemas.expenses.Response)
def get_by_id(expense_id: int, db: Session = Depends(get_db)):
    expense = crud.expenses.get_by_id(db=db, expense_id=expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.put('/{expense_id}', response_model=schemas.expenses.Response)
def get_by_type(expense_type: str, db: Session = Depends(get_db), skip: int = 0, limit: int = 50):
    return crud.expenses.get_by_type(db=db, expense_type=expense_type, skip=skip, limit=limit)

@router.put('/{expense_id}', response_model=schemas.expenses.Response)
def update(expense_id: int, updated_items: schemas.expenses.Update, db: Session = Depends(get_db)):
    expense = crud.expenses.update(db=db, expense_id=expense_id, updated_items=updated_items)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.delete('/{expense_id}', response_model=schemas.expenses.Response)
def delete(expense_id: int, db: Session = Depends(get_db)):
    expense = crud.expenses.get_by_id(db=db, expense_id=expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense
