from sqlalchemy.orm import Mapped, mapped_column

from model.database import Base


class Sala(Base):
    __tablename__ = "salas"

    numero: Mapped[int] = mapped_column(primary_key=True)
