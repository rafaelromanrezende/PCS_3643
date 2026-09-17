from datetime import date, datetime
from typing import Annotated, Literal

from pydantic import BeforeValidator, PlainSerializer

FORMATO_BR = "%d/%m/%Y"

TipoSala = Literal["2D", "3D"]


def _para_data(valor):
    if isinstance(valor, str):
        return datetime.strptime(valor, FORMATO_BR).date()
    return valor


DataBR = Annotated[
    date,
    BeforeValidator(_para_data),
    PlainSerializer(lambda valor: valor.strftime(FORMATO_BR), return_type=str),
]
