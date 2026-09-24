from datetime import date, time

from sqlalchemy import Date, ForeignKey, Integer, Time, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model.database import Base

class Sessao(Base):
    __tablename__ = "sessoes"

    codigo: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sala_numero: Mapped[int] = mapped_column(
        ForeignKey("salas.numero"), nullable=False
    )
    filme_codigo: Mapped[int] = mapped_column(
        ForeignKey("filmes.codigo"), nullable=False
    )
    data: Mapped[date] = mapped_column(Date, nullable=False)
    hora_inicio: Mapped[time] = mapped_column(Time, nullable=False)

    filme = relationship("Filme")
    sala = relationship("Sala")
    assentos: Mapped[list["Assento"]] = relationship(
        back_populates="sessao",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        UniqueConstraint(
            "sala_numero",
            "data",
            "hora_inicio",
            name="uq_sessao_sala_data_hora",
        ),
    )


class Assento(Base):
    __tablename__ = "assentos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sessao_codigo: Mapped[int] = mapped_column(
        ForeignKey("sessoes.codigo"), nullable=False
    )
    numero: Mapped[int] = mapped_column(Integer, nullable=False)
    ocupado: Mapped[bool] = mapped_column(default=False, nullable=False)

    sessao: Mapped["Sessao"] = relationship(back_populates="assentos")

    __table_args__ = (
        UniqueConstraint(
            "sessao_codigo",
            "numero",
            name="uq_assento_sessao_numero",
        ),
    )
