from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated
from app.models.test_model import Pokemon
from .database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from sqlalchemy import select


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
    return {"message": "Hello World >:3"}


@app.post("/pokemon")
def create_pokemon(pokemon: PokemonBase, db: db_dependency):
    db_pokemon = Pokemon(
        name=pokemon.name, type=pokemon.type, level=pokemon.level)
    db.add(db_pokemon)
    db.commit()
    return {f"{db_pokemon.name}": "Sucessfully created"}


@app.get("/pokemon")
def get_all_pokemon(db: db_dependency):
    query = select(Pokemon)
    result = db.scalars(query).all()

    return result


# may take a lil bit longer because adding a record to a db; makes a network call
    # RULE: if something is awaitable use await & by default will need to use async
    # when there is a async version of something try to use async
    # research if there are async methods of these methods or is it okay because we're usng async already or do we still need to await this?
