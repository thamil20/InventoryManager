from sqlalchemy.orm import mapped_column, Mapped
from backend.app.models.base import Base

class Incomes(Base):
    __tablename__ = "incomes"
    id: Mapped[int] = mapped_column(default=True, primary_key=True, nullable=False, index=True, unique=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    income_type: Mapped[str] = mapped_column(nullable=True)
    amount: Mapped[float] = mapped_column(nullable=False)

    def __repr__(self):
        return (f"<Income(id={self.id}, "
                f"title={self.title}")
