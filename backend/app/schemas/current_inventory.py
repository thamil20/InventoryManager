from typing import Optional
from pydantic import BaseModel, Field


class CurrentInventoryBase(BaseModel):
    name: str
    description: str
    type: Optional[str]
    age: int
    purchase_price: float
    sale_price: float
    image: Optional[str]

class Create(CurrentInventoryBase):
    pass

class Update(CurrentInventoryBase):
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    age: Optional[int] = Field(default=None, gt=0)
    purchase_price: Optional[float] = Field(default=None, gt=0)
    sale_price: Optional[float] = Field(default=None, gt=0)
    image: Optional[str] = None
    class Config:
        from_attributes = True

class Response(CurrentInventoryBase):
    id: int = Field(gt=0)
    class Config:
        from_attributes = True