from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from model.tipo_ingresso import TipoIngresso
from fastapi import HTTPException
from sqlalchemy.orm import Session

from model.database import get_db
from view.tipo_ingresso_schema import TipoIngressoCreate, TipoIngressoResponse, TipoIngressoUpdate

router = APIRouter(prefix="/tipos-ingresso", tags=["tipos de ingresso"])


@router.post("", response_model=TipoIngressoResponse, status_code=status.HTTP_201_CREATED)
def cadastrar(dados: TipoIngressoCreate, db: Session = Depends(get_db)):
    ingresso = TipoIngresso(**dados.model_dump())
    db.add(ingresso)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status.HTTP_409_CONFLICT, "Ja existe um tipo de ingresso com esse nome")
    return ingresso

@router.get("", response_model=list[TipoIngressoResponse])
def listar(db: Session = Depends(get_db)):
    return db.scalars(select(TipoIngresso)).all()


@router.get("/{codigo}", response_model=TipoIngressoResponse)
def buscar(codigo: int, db: Session = Depends(get_db)):
    ingresso = db.get(TipoIngresso, codigo)
    if ingresso is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Tipo de ingresso nao encontrado")
    return ingresso


@router.put("/{codigo}", response_model=TipoIngressoResponse)
def editar(codigo: int, dados: TipoIngressoUpdate, db: Session = Depends(get_db)):
    ingresso = db.get(TipoIngresso, codigo)
    if ingresso is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Tipo de ingresso nao encontrado")
    for tipo, preco in dados.model_dump(exclude_unset=True).items():
        setattr(ingresso, tipo, preco)
    db.commit()
    db.refresh(ingresso)
    return ingresso


@router.delete("/{codigo}", status_code=status.HTTP_204_NO_CONTENT)
def remover(codigo: int, db: Session = Depends(get_db)):
    ingresso = db.get(TipoIngresso, codigo)
    if ingresso is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Tipo de ingresso nao encontrado")
    db.delete(ingresso)
    db.commit()
