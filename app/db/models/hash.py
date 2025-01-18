from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Hash(Base):
    __tablename__ = "hashes"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    hash: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"))
