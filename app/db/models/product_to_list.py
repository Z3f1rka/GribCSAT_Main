from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class ProductToList(Base):
    __tablename__ = "product_to_list"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    list_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("product_lists.id", ondelete="CASCADE"))
    product_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("products.id", ondelete="CASCADE"))
