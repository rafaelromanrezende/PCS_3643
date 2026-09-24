from datetime import date

from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from model.database import Base


class Filme(Base):
    __tablename__ = "filmes"

    codigo: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    data_estreia: Mapped[date] = mapped_column(Date, nullable=False)
    data_saida: Mapped[date] = mapped_column(Date, nullable=False)
    duracao: Mapped[int] = mapped_column(Integer, nullable=False)
    cartaz_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
