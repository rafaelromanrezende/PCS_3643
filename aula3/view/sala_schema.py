from pydantic import BaseModel, ConfigDict


class SalaBase(BaseModel):
    pass


class SalaCreate(SalaBase):
    pass


class SalaUpdate(BaseModel):
    pass


class SalaResponse(SalaBase):
    model_config = ConfigDict(from_attributes=True)
