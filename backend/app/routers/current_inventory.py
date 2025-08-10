from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.app import crud, schemas
from backend.app.database import get_db

router = APIRouter(
    prefix="/current_inventory",
    tags=["Current Inventory"]
)

@router.post('/', response_model=schemas.current_inventory.Response)
def create_item(item: schemas.current_inventory.Create, db: Session = Depends(get_db)):
    db_item = crud.current_inventory.create(db, item)
    if not db_item:
        raise HTTPException(status_code=400, detail="Item already exists")
    return db_item

@router.get('/', response_model=List[schemas.current_inventory.Response])
def get_all(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return crud.create_inventory.get_all(db=db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=schemas.current_inventory.Response)
def get_by_id(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.current_inventory.get_by_id(db=db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.get('/name/{name}')
def get_by_name(name: str, db: Session = Depends(get_db)):
    db_item = crud.current_inventory.get_by_name(db=db, name=name)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put('/{item_id}', response_model=schemas.current_inventory.Response)
def update(item_id: int, updated_items: schemas.current_inventory.Update,db: Session = Depends(get_db)):
    db_item = crud.current_inventory.update(db=db, item_id=item_id, updated_items=updated_items)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete('/{item_id}', response_model=schemas.current_inventory.Response)
def delete(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.current_inventory.delete(db=db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
