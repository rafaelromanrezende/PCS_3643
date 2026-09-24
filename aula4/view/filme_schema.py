from pydantic import BaseModel, ConfigDict, Field, model_validator

from view.campos import DataBR


class FilmeBase(BaseModel):
    nome: str = Field(min_length=1, max_length=200)
    data_estreia: DataBR
    data_saida: DataBR
    duracao: int = Field(gt=0)
    cartaz_url: str | None = Field(default=None, max_length=500)

    @model_validator(mode="after")
    def validar_periodo(self):
        if self.data_estreia > self.data_saida:
            raise ValueError("data_estreia deve ser anterior a data_saida")
        return self


class FilmeCreate(FilmeBase):
    pass


class FilmeUpdate(BaseModel):
    nome: str | None = Field(default=None, min_length=1, max_length=200)
    data_estreia: DataBR | None = None
    data_saida: DataBR | None = None
    duracao: int | None = Field(default=None, gt=0)
    cartaz_url: str | None = Field(default=None, max_length=500)


class FilmeResponse(FilmeBase):
    model_config = ConfigDict(from_attributes=True)

    codigo: int
