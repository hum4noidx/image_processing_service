from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from app.db import Base


class Pipeline(Base):
    __tablename__ = "pipeline"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
