from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from model.database import get_db
from view.tipo_ingresso_schema import TipoIngressoCreate, TipoIngressoResponse, TipoIngressoUpdate

router = APIRouter(prefix="/tipos-ingresso", tags=["tipos de ingresso"])


@router.post("", response_model=TipoIngressoResponse, status_code=status.HTTP_201_CREATED)
def cadastrar(dados: TipoIngressoCreate, db: Session = Depends(get_db)):
    pass


@router.get("", response_model=list[TipoIngressoResponse])
def listar(db: Session = Depends(get_db)):
    pass


@router.get("/{codigo}", response_model=TipoIngressoResponse)
def buscar(codigo: int, db: Session = Depends(get_db)):
    pass


@router.put("/{codigo}", response_model=TipoIngressoResponse)
def editar(codigo: int, dados: TipoIngressoUpdate, db: Session = Depends(get_db)):
    pass


@router.delete("/{codigo}", status_code=status.HTTP_204_NO_CONTENT)
def remover(codigo: int, db: Session = Depends(get_db)):
    pass
