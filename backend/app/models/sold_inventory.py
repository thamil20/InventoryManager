from sqlalchemy.orm import Mapped, mapped_column
from backend.app.models.base import Base

class SoldInventory(Base):
    __tablename__ = "sold_inventory"
    id: Mapped[int] = mapped_column(default=True, primary_key=True, nullable=False, index=True, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    type: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)
    purchase_price: Mapped[float] = mapped_column(nullable=True)
    sale_price: Mapped[float] = mapped_column(nullable=True)
    sale_location: Mapped[str] = mapped_column(nullable=True)
    image: Mapped[str] = mapped_column(nullable=True)

    def __repr__(self):
        return (f"<SoldInventory(id={self.id}, "
                f"name={self.name}")
