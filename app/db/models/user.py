import datetime

from sqlalchemy import BigInteger, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    reg_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    hashes = relationship('Hash', back_populates='user_id', cascade='all, delete-orphan')
    visits = relationship('Visit', back_populates='user_id', cascade='all, delete-orphan')
    product_lists = relationship('ProductList', back_populates='user_id', cascade='all, delete-orphan')
    user_answer_id = relationship('UserAnswer', back_populates='user_id', cascade='all, delete-orphan')
