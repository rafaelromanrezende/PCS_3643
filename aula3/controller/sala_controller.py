from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from model.database import get_db
from model.sala import Sala
from view.sala_schema import SalaCreate, SalaResponse, SalaUpdate

router = APIRouter(prefix="/salas", tags=["salas"])

def _buscar(numero: int, db: Session) -> Sala:
    sala = db.get(Sala, numero)
    if sala is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Sala nao encontrada")
    return sala

@router.post("", response_model=SalaResponse, status_code=status.HTTP_201_CREATED)
def cadastrar(dados: SalaCreate, db: Session = Depends(get_db)):
    sala = Sala(**dados.model_dump())
    db.add(sala)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status.HTTP_409_CONFLICT, "Ja existe uma sala com esse numero")
    db.refresh(sala)
    return sala


@router.get("", response_model=list[SalaResponse])
def listar(db: Session = Depends(get_db)):
    return db.scalars(select(Sala)).all()


@router.get("/{numero}", response_model=SalaResponse)
def buscar(numero: int, db: Session = Depends(get_db)):
    return _buscar(numero, db)


@router.put("/{numero}", response_model=SalaResponse)
def editar(numero: int, dados: SalaUpdate, db: Session = Depends(get_db)):
    sala = _buscar(numero, db)
    for campo, valor in dados.model_dump(exclude_unset=True, exclude_none=True).items():
         setattr(sala, campo, valor)
    db.commit()
    db.refresh(sala)
    return sala


@router.delete("/{numero}", status_code=status.HTTP_204_NO_CONTENT)
def remover(numero: int, db: Session = Depends(get_db)):
    db.delete(_buscar(numero, db))
    db.commit()
