from typing import Optional
from pydantic import BaseModel, Field


class ExpensesBase(BaseModel):
    title: str
    description: str
    expense_type: Optional[str] = None
    cost: float


class Create(ExpensesBase):
    pass

class Update(ExpensesBase):
    title: Optional[str] = None
    description: Optional[str] = None
    expense_type: Optional[str] = None
    cost: Optional[float] = None
    class Config:
        from_attributes = True

class Response(ExpensesBase):
    id: int = Field(gt=0)
    class Config:
        from_attributes = True