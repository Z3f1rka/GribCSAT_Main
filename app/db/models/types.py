from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Types(Base):
    __tablename__ = "types"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    product_id = relationship('Type', back_populates='type_id', cascade='all, delete-orphan')
    title: Mapped[str] = mapped_column(String, nullable=False)
