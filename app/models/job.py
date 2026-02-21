from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Boolean
from typing import TYPE_CHECKING
from app.database import Base

if TYPE_CHECKING:
    from .pokemon import Pokemon


class Job(Base):
    __tablename__ = "job"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    required_type: Mapped[str] = mapped_column(String)
    difficulty_level: Mapped[int] = mapped_column(Integer)
    duration: Mapped[int] = mapped_column(Integer)
    exp_reward: Mapped[int] = mapped_column(Integer)
    job_description: Mapped[str] = mapped_column(String)
    is_available: Mapped[bool] = mapped_column(Boolean)
    pokemons: Mapped[list["Pokemon"]] = relationship(
        back_populates="job")
