import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base


class Visit(Base):
    __tablename__ = "visits"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    visited_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"))
    product_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("products.id", ondelete="CASCADE"))
