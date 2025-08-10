from typing import Optional
from pydantic import BaseModel, Field

class SoldInventoryBase(BaseModel):
    name: str
    description: str
    type: Optional[str] = None
    age: int = Field(gt=0)
    purchase_price: float = Field(gt=0)
    sale_price: float = Field(gt=0)
    sale_location: Optional[str] = None
    image: Optional[str] = None

class Create(SoldInventoryBase):
    pass

class Update(SoldInventoryBase):
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    age: int = Field(gt=0, default=None)
    purchase_price: float = Field(gt=0, default=None)
    sale_price: float = Field(gt=0, default=None)
    sale_location: Optional[str] = None
    image: Optional[str] = None
    class Config:
        from_attributes = True

class Response(SoldInventoryBase):
    id: int = Field(gt=0)
    class Config:
        from_attributes = True