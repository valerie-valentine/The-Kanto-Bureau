from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from typing import TYPE_CHECKING
from app.database import Base

if TYPE_CHECKING:
    from .pokemon import Pokemon


class PokemonStat(Base):
    __tablename__ = "pokemon_stat"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    level: Mapped[int] = mapped_column(Integer)
    pokemons: Mapped[list["Pokemon"]] = relationship(
        back_populates="pokemon_stat", cascade="all, delete-orphan")
