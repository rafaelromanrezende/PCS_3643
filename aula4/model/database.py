import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import StaticPool

# Em producao/dev usa o arquivo cinema.db. Os testes apontam CINEMA_DB_URL
# para "sqlite://" (banco em memoria) antes de importar a aplicacao.
URL_BANCO = os.getenv("CINEMA_DB_URL", "sqlite:///cinema.db")

_argumentos = {"connect_args": {"check_same_thread": False}}

if URL_BANCO in ("sqlite://", "sqlite:///:memory:"):
    # StaticPool mantem UMA conexao: sem isso cada Session abriria um banco
    # em memoria proprio e vazio.
    _argumentos["poolclass"] = StaticPool

engine = create_engine(URL_BANCO, **_argumentos)

SessionLocal = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
