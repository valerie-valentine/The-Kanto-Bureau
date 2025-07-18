from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated
from .models.test_model import Pokemon
from .database import engine, SessionLocal, Base
from sqlalchemy.orm import Session


app = FastAPI()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class PokemonBase(BaseModel):
    name: str
    type: str
    level: int


@app.get("/")
def root():
    return {"message": "Hello world >:3"}


@app.post("/pokemon")
def create_pokemon(pokemon: PokemonBase, db: db_dependency):
    db_pokemon = Pokemon(
        name=pokemon.name, type=pokemon.type, level=pokemon.level)
    db.add(db_pokemon)
    db.commit()
    return db_pokemon
