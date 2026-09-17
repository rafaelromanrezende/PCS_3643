from datetime import date

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from model.database import get_db
from view.sessao_schema import SessaoCreate, SessaoResponse, SessaoUpdate

router = APIRouter(prefix="/sessoes", tags=["sessoes"])


@router.post("", response_model=SessaoResponse, status_code=status.HTTP_201_CREATED)
def cadastrar(dados: SessaoCreate, db: Session = Depends(get_db)):
    pass


@router.get("", response_model=list[SessaoResponse])
def listar(data: date | None = None, db: Session = Depends(get_db)):
    pass


@router.get("/{codigo}", response_model=SessaoResponse)
def buscar(codigo: int, db: Session = Depends(get_db)):
    pass


@router.put("/{codigo}", response_model=SessaoResponse)
def editar(codigo: int, dados: SessaoUpdate, db: Session = Depends(get_db)):
    pass


@router.delete("/{codigo}", status_code=status.HTTP_204_NO_CONTENT)
def remover(codigo: int, db: Session = Depends(get_db)):
    pass
