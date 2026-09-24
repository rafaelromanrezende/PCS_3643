from pydantic import BaseModel, ConfigDict, Field
from typing import Literal


class TipoIngressoBase(BaseModel):
    tipo: Literal[0, 1]
    preco: float = Field(gt=0)


class TipoIngressoCreate(TipoIngressoBase):
    pass


class TipoIngressoUpdate(BaseModel):
    tipo: Literal[0, 1] | None = None
    preco: float | None = Field(default=None, gt=0)


class TipoIngressoResponse(TipoIngressoBase):
    model_config = ConfigDict(from_attributes=True)

    codigo: int
