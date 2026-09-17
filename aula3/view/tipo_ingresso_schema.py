from pydantic import BaseModel, ConfigDict
from typing import Literal
from fastapi import HTTPException


class TipoIngressoBase(BaseModel):
    tipo: Literal[0, 1]
    preco: float


class TipoIngressoCreate(TipoIngressoBase):
    pass


class TipoIngressoUpdate(BaseModel):
    tipo: Literal[0, 1] | None = None
    preco: float | None = None


class TipoIngressoResponse(TipoIngressoBase):
    model_config = ConfigDict(from_attributes=True)

    codigo: int
