from sqlalchemy.orm import Mapped, mapped_column

from model.database import Base


class Sessao(Base):
    __tablename__ = "sessoes"

    codigo: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class Assento(Base):
    __tablename__ = "assentos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
