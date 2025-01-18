import datetime

from sqlalchemy import BigInteger, DateTime, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class ShopComments(Base):
    __tablename__ = "shop_comments"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    user: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"))
    text: Mapped[str] = mapped_column(Text)
    rating: Mapped[int] = mapped_column(BigInteger, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    shop: Mapped[int] = mapped_column(BigInteger, ForeignKey("shops.id", ondelete="CASCADE"))
    