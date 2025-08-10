from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.app import crud, schemas
from backend.app.database import get_db

router = APIRouter(
    prefix="/incomes",
    tags=["Incomes"]
)

@router.post('/', response_model=schemas.current_inventory.Response)
def create(item: schemas.incomes.Create, db: Session = Depends(get_db)):
    income = crud.incomes.create(db, item)
    if income:
        raise HTTPException(status_code=404, detail="Income Already Exists")
    return income

@router.get('/', response_model=List[schemas.current_inventory.Response])
def get_all(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return crud.incomes.get_all(db, skip=skip, limit=limit)

@router.get('/{income_id}', response_model=schemas.current_inventory.Response)
def get_by_id(income_id: int, db: Session = Depends(get_db)):
    income = crud.incomes.get_by_id(db, income_id)
    if not income:
        raise HTTPException(status_code=404, detail="Income not found")
    return income

@router.get('/{income_type}', response_model=List[schemas.current_inventory.Response])
def get_by_type(income_type: str, db: Session = Depends(get_db), skip: int = 0, limit: int = 50):
    return crud.incomes.get_by_type(db, income_type, skip=skip, limit=limit)

@router.put('/{income_id}', response_model=schemas.current_inventory.Response)
def update(income_id: int, updated_items: schemas.incomes.Update, db: Session = Depends(get_db)):
    income = crud.incomes.update(db, income_id, updated_items=updated_items)
    if not income:
        raise HTTPException(status_code=404, detail="Income not found")
    return income

@router.delete('/{income_id}', response_model=schemas.current_inventory.Response)
def delete(income_id: int, db: Session = Depends(get_db)):
    income = crud.incomes.delete(db, income_id)
    if not income:
        raise HTTPException(status_code=404, detail="Income not found")
    return income