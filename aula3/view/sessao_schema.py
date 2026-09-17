from pydantic import BaseModel, ConfigDict


class SessaoBase(BaseModel):
    pass


class SessaoCreate(SessaoBase):
    pass


class SessaoUpdate(BaseModel):
    pass


class SessaoResponse(SessaoBase):
    model_config = ConfigDict(from_attributes=True)
