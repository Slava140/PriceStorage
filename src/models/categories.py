from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))

    # products: Mapped[list["Product"]] = relationship(back_populates="category_name")
