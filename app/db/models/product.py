from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    link: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    # type orm to type.id
    article: Mapped[str] = mapped_column(String, nullable=False)
    file: Mapped[str]
    shop_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("shops.id", ondelete="CASCADE"))
    visits = relationship('Visit', back_populates='product_id', cascade='all, delete-orphan')
