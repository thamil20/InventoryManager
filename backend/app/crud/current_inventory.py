from sqlalchemy.orm import Session
from backend.app import models, schemas

def create(db: Session, item: schemas.current_inventory.Create):
    db_item = models.CurrentInventory(
        name=item.name,
        description=item.description,
        type=item.type,
        age=item.age,
        purchase_price=item.purchase_price,
        sale_price=item.sale_price,
        image=item.image.filename if item.image else None
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_all(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.CurrentInventory).offset(skip).limit(limit).all()

def get_by_id(db: Session, item_id: int):
    return db.query(models.CurrentInventory).filter(models.CurrentInventory.id == item_id).first()

def get_by_name(db: Session, name: str):
    return db.query(models.CurrentInventory).filter(models.CurrentInventory.name == name).first()

def update(db: Session, item_id: int, updated_items: schemas.current_inventory.Update):
    db_item = db.query(models.CurrentInventory).filter(models.CurrentInventory.id == item_id).first()
    if not db_item:
        return None # Handled in routes

    updated_items = updated_items.model_dump(exclude_unset=True)
    for key, value in updated_items.items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item

def delete(db: Session, item_id: int):
    db_item = db.query(models.CurrentInventory).filter(models.CurrentInventory.id == item_id).first()
    if not db_item:
        return None # Handled in routes

    db.delete(db_item)
    db.commit()
    return db_item
