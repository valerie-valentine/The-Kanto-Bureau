from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING
from app.database import Base

if TYPE_CHECKING:
    from .pokemon import Pokemon


class Player(Base):
    __tablename__ = "player"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    pokemons: Mapped[list["Pokemon"]] = relationship(
        back_populates="player", cascade="all, delete-orphan")
