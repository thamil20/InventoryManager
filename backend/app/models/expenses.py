from sqlalchemy.orm import Mapped, mapped_column
from backend.app.models.base import Base

class Expenses(Base):
    __tablename__ = "expenses"
    id: Mapped[int] = mapped_column(default=True, primary_key=True, nullable=False, index=True, unique=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    expense_type: Mapped[str] = mapped_column(nullable=True)
    cost: Mapped[float] = mapped_column(nullable=False)

    def __repr__(self):
        return (f"<Expenses(id={self.id}, "
                f"title={self.title}")
