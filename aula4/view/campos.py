from datetime import date, datetime
from typing import Annotated, Literal

from pydantic import BeforeValidator, PlainSerializer

FORMATO_BR = "%d/%m/%Y"

TipoSala = Literal["2D", "3D"]


def _para_data(valor):
    if isinstance(valor, str):
        return datetime.strptime(valor, FORMATO_BR).date()
    return valor


# when_used="json" e' essencial: sem isso o model_dump() do controller
# devolveria a data como string dd/mm/aaaa e o SQLAlchemy recusaria o INSERT
# (SQLite Date type only accepts Python date objects). Na resposta HTTP a
# serializacao continua saindo em dd/mm/aaaa.
DataBR = Annotated[
    date,
    BeforeValidator(_para_data),
    PlainSerializer(
        lambda valor: valor.strftime(FORMATO_BR),
        return_type=str,
        when_used="json",
    ),
]
