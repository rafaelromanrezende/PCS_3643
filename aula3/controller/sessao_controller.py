from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from model.database import get_db
from model.sessao import Assento, Sessao
from view.sessao_schema import SessaoCreate, SessaoResponse, SessaoUpdate

router = APIRouter(prefix="/sessoes", tags=["sessoes"])


def _buscar(codigo: int, db: Session) -> Sessao:
    sessao = db.get(Sessao, codigo)
    if sessao is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Sessao nao encontrada")
    return sessao


@router.post("", response_model=SessaoResponse, status_code=status.HTTP_201_CREATED)
def cadastrar(dados: SessaoCreate, db: Session = Depends(get_db)):
    dados_sessao = dados.model_dump(exclude={"quantidade_assentos"})
    sessao = Sessao(**dados_sessao)
    sessao.assentos = [
        Assento(numero=numero)
        for numero in range(1, dados.quantidade_assentos + 1)
    ]
    db.add(sessao)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            "Ja existe uma sessao nessa sala, data e horario",
        )
    db.refresh(sessao)
    return sessao


@router.get("", response_model=list[SessaoResponse])
def listar(data: date | None = None, db: Session = Depends(get_db)):
    consulta = select(Sessao).order_by(Sessao.data, Sessao.hora_inicio)
    if data is not None:
        consulta = consulta.where(Sessao.data == data)
    return db.scalars(consulta).all()


@router.get("/{codigo}", response_model=SessaoResponse)
def buscar(codigo: int, db: Session = Depends(get_db)):
    return _buscar(codigo, db)


@router.put("/{codigo}", response_model=SessaoResponse)
def editar(codigo: int, dados: SessaoUpdate, db: Session = Depends(get_db)):
    sessao = _buscar(codigo, db)
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(sessao, campo, valor)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            "Ja existe uma sessao nessa sala, data e horario",
        )
    db.refresh(sessao)
    return sessao


@router.delete("/{codigo}", status_code=status.HTTP_204_NO_CONTENT)
def remover(codigo: int, db: Session = Depends(get_db)):
    db.delete(_buscar(codigo, db))
    db.commit()
