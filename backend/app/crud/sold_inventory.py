from sqlalchemy.orm import Session
from backend.app import models, schemas

def create(db: Session, current_inventory_id: int, sale_location: str):
    item = db.query(models.current_inventory.CurrentInventory).filters(models.current_inventory.CurrentInventory.id == current_inventory_id).first()
    if not item:
        return None # Handled in routes

    sold_item = models.sold_inventory.SoldInventory(
        name=item.name,
        description=item.description,
        type=item.type,
        age=item.age,
        purchase_price=item.purchase_price,
        sale_price=item.sale_price,
        sale_location=sale_location,
        image=item.image
    )

    db.add(sold_item)
    db.delete(item)
    db.commit()
    db.refresh(sold_item)
    return sold_item

def get_all(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.SoldInventory).offset(skip).limit(limit).all()

def get_by_id(db: Session, sold_id: int):
    return db.query(models.SoldInventory).filters(models.SoldInventory.id == sold_id).first()

def get_by_name(db: Session, name: str):
    return db.query(models.SoldInventory).filters(models.SoldInventory.name == name).first()

def get_by_sale_location(db: Session, sale_location: str):
    return db.query(models.SoldInventory).filters(models.SoldInventory.sale_location == sale_location).first()

def update(db: Session, item_id: int, updated_items: schemas.sold_inventory.Update):
    sold_item = db.query(models.SoldInventory).filter(models.SoldInventory.id == item_id).first()
    if not sold_item:
        return None
    updated_items = updated_items.model_dump(exclude_unset=True)
    for key, value in updated_items.items():
        setattr(sold_item, key, value)
    db.add(sold_item)
    db.commit()
    db.refresh(sold_item)
    return sold_item

def delete(db: Session, item_id: int):
    sold_item = db.query(models.SoldInventory).filter(models.SoldInventory.id == item_id).first()
    if not sold_item:
        return None
    db.delete(sold_item)
    db.commit()
    return sold_item