from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from model.database import get_db
from model.filme import Filme
from view.filme_schema import FilmeCreate, FilmeResponse, FilmeUpdate

router = APIRouter(prefix="/filmes", tags=["filmes"])


def _buscar(codigo: int, db: Session) -> Filme:
    filme = db.get(Filme, codigo)
    if filme is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Filme nao encontrado")
    return filme


@router.post("", response_model=FilmeResponse, status_code=status.HTTP_201_CREATED)
def cadastrar(dados: FilmeCreate, db: Session = Depends(get_db)):
    filme = Filme(**dados.model_dump())
    db.add(filme)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status.HTTP_409_CONFLICT, "Ja existe um filme com esse nome")
    db.refresh(filme)
    return filme


@router.get("", response_model=list[FilmeResponse])
def listar(db: Session = Depends(get_db)):
    return db.scalars(select(Filme)).all()


@router.get("/{codigo}", response_model=FilmeResponse)
def buscar(codigo: int, db: Session = Depends(get_db)):
    return _buscar(codigo, db)


@router.put("/{codigo}", response_model=FilmeResponse)
def editar(codigo: int, dados: FilmeUpdate, db: Session = Depends(get_db)):
    filme = _buscar(codigo, db)
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(filme, campo, valor)
    db.commit()
    db.refresh(filme)
    return filme


@router.delete("/{codigo}", status_code=status.HTTP_204_NO_CONTENT)
def remover(codigo: int, db: Session = Depends(get_db)):
    db.delete(_buscar(codigo, db))
    db.commit()
