from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.app import crud, schemas
from backend.app.database import get_db

router = APIRouter(
    prefix="/sold_inventory",
    tags=["Sold Inventory"]
)

@router.post('/', response_model=schemas.sold_inventory.Response)
def create_sold_item(current_item_id: int, sale_location: str, db: Session = Depends(get_db)):
    current_item = crud.current_inventory.get_by_id(db, current_item_id)
    if not current_item:
        raise HTTPException(status_code=404, detail="Item not found in Current Inventory")
    return crud.sold_inventory.create(db=db, current_inventory_id=current_item.id, sale_location=sale_location)

@router.get('/', response_model=List[schemas.current_inventory.Response])
def get_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.sold_inventory.get_all(db=db, skip=skip, limit=limit)

@router.get('/{item_id}', response_model=schemas.current_inventory.Response)
def get_by_id(item_id: int, db: Session = Depends(get_db)):
    sold_item = crud.sold_inventory.get_by_id(db, item_id)
    if not sold_item:
        raise HTTPException(status_code=404, detail="Item not found in Sold Inventory")
    return sold_item

@router.get('/{item_id}', response_model=schemas.current_inventory.Response)
def get_by_name(name: str, db: Session = Depends(get_db)):
    sold_item = crud.sold_inventory.get_by_name(db, name)
    if not sold_item:
        raise HTTPException(status_code=404, detail="Item not found in Sold Inventory")
    return sold_item

@router.put('/{item_id}', response_model=schemas.current_inventory.Response)
def update(item_id: int, updated_items: schemas.sold_inventory.Update, db: Session = Depends(get_db)):
    sold_item = crud.sold_inventory.update(db=db, item_id=item_id, updated_items=updated_items)
    if not sold_item:
        raise HTTPException(status_code=404, detail="Item not found in Sold Inventory")
    return sold_item

@router.delete('/{item_id}', response_model=schemas.current_inventory.Response)
def delete(item_id: int, db: Session = Depends(get_db)):
    sold_item = crud.sold_inventory.delete(db=db, item_id=item_id)
    if not sold_item:
        raise HTTPException(status_code=404, detail="Item not found in Sold Inventory")
    return sold_item
