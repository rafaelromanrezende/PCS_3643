from datetime import date, time

from pydantic import BaseModel, ConfigDict, Field


class SessaoBase(BaseModel):
    sala_numero: int = Field(gt=0)
    filme_codigo: int = Field(gt=0)
    data: date
    hora_inicio: time


class SessaoCreate(SessaoBase):
    quantidade_assentos: int = Field(gt=0)


class SessaoUpdate(BaseModel):
    sala_numero: int | None = Field(default=None, gt=0)
    filme_codigo: int | None = Field(default=None, gt=0)
    data: date | None = None
    hora_inicio: time | None = None


class AssentoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    numero: int
    ocupado: bool


class SessaoResponse(SessaoBase):
    model_config = ConfigDict(from_attributes=True)

    codigo: int
    assentos: list["AssentoResponse"]
