from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, Integer, String

from model.database import Base


class Sala(Base):
    __tablename__ = "salas"

    numero: Mapped[int] = mapped_column(primary_key=True)
    capacidade: Mapped[int] = mapped_column(Integer, nullable=False)
    tipo: Mapped[str] = mapped_column(String(50), nullable=False)