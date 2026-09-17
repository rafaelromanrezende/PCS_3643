from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine(
    "sqlite:///cinema.db",                      # o arquivo do banco
    connect_args={"check_same_thread": False},  # exigido pelo SQLite + FastAPI
)

SessionLocal = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    """Classe-mãe de todas as tabelas."""


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
