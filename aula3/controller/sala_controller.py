from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from model.database import get_db
from view.sala_schema import SalaCreate, SalaResponse, SalaUpdate

router = APIRouter(prefix="/salas", tags=["salas"])


@router.post("", response_model=SalaResponse, status_code=status.HTTP_201_CREATED)
def cadastrar(dados: SalaCreate, db: Session = Depends(get_db)):
    pass


@router.get("", response_model=list[SalaResponse])
def listar(db: Session = Depends(get_db)):
    pass


@router.get("/{numero}", response_model=SalaResponse)
def buscar(numero: int, db: Session = Depends(get_db)):
    pass


@router.put("/{numero}", response_model=SalaResponse)
def editar(numero: int, dados: SalaUpdate, db: Session = Depends(get_db)):
    pass


@router.delete("/{numero}", status_code=status.HTTP_204_NO_CONTENT)
def remover(numero: int, db: Session = Depends(get_db)):
    pass
