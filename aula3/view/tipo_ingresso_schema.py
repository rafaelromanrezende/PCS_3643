from pydantic import BaseModel, ConfigDict


class TipoIngressoBase(BaseModel):
    pass


class TipoIngressoCreate(TipoIngressoBase):
    pass


class TipoIngressoUpdate(BaseModel):
    pass


class TipoIngressoResponse(TipoIngressoBase):
    model_config = ConfigDict(from_attributes=True)
