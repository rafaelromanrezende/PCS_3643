from pydantic import BaseModel, ConfigDict, Field

from view.campos import TipoSala


class SalaBase(BaseModel):
    capacidade: int = Field (gt=0)
    tipo: TipoSala
    


class SalaCreate(SalaBase):
    numero: int = Field(gt=0)
    

class SalaUpdate(BaseModel):
    capacidade: int | None = Field(default=None, gt=0)
    tipo: TipoSala | None = None    


class SalaResponse(SalaBase):
    model_config = ConfigDict(from_attributes=True)

    numero: int
