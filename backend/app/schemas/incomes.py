from typing import Optional
from pydantic import BaseModel, Field

class IncomesBase(BaseModel):
    title: str
    description: str
    income_type: Optional[str] = None
    amount: float

class Create(IncomesBase):
    pass

class Update(IncomesBase):
    title: Optional[str] = None
    description: Optional[str] = None
    income_type: Optional[str] = None
    amount: Optional[float] = None
    class Config:
        from_attributes = True

class Response(IncomesBase):
    id: int = Field(gt=0)
    class Config:
        from_attributes = True