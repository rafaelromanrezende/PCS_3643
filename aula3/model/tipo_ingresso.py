from sqlalchemy.orm import Mapped, mapped_column

from model.database import Base


class TipoIngresso(Base):
    __tablename__ = "tipos_ingresso"

    codigo: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
