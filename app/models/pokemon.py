from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer
from typing import Optional, TYPE_CHECKING
from app.database import Base

if TYPE_CHECKING:
    from .pokemon_stat import PokemonStat
    from .player import Player
    from .job import Job


class Pokemon(Base):
    __tablename__ = "pokemon"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player_id: Mapped[int] = mapped_column(
        ForeignKey("player.id"))
    player = Mapped["Player"] = relationship(back_populates="pokemons")
    pokemon_stat_id: Mapped[int] = mapped_column(
        ForeignKey("pokemon_stat.id"))
    pokemon_stat = Mapped["PokemonStat"] = relationship(
        back_populates="pokemons")
    current_level: Mapped[int] = mapped_column(Integer)
    current_hp: Mapped[int] = mapped_column(Integer)
    job_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("job.id"), nullable=True)
    job: Mapped[Optional["Job"]] = relationship(back_populates="pokemons")
