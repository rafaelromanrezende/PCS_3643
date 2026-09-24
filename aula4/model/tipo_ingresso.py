from sqlalchemy import Float, Integer
from sqlalchemy.orm import Mapped, mapped_column

from model.database import Base
from pydantic import BaseModel, ConfigDict, Field
from typing import Literal

class TipoIngressoBase(BaseModel):
    tipo: Literal[0, 1]
    preco: float = Field(gt=0)

class TipoIngresso(Base):
    __tablename__ = "tipos_ingresso"

    codigo: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tipo: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    preco: Mapped[float] = mapped_column(Float, nullable=False)
