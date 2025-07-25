from fastapi import FastAPI
from app.routes.pokemon_stat_routes import router as pokemon_stat_router
from app.routes.pokemon_routes import router as pokemon_router
from app.routes.player_routes import router as player_router
from app.routes.job_routes import router as job_router


# Register your routers here
app = FastAPI()
app.include_router(pokemon_stat_router,
                   prefix="/pokemon_stat", tags=["PokemonStat"])
app.include_router(pokemon_router, prefix="/pokemon", tags=["Pokemon"])
app.include_router(player_router, prefix="/player", tags=["Player"])
app.include_router(job_router, prefix="/job", tags=["Job"])


@app.get("/")
def root():
    return {"message": "Hello World >:3"}


# db_dependency = Annotated[Session, Depends(get_db)]


# class PokemonBase(BaseModel):
#     name: str
#     type: str
#     level: int


# @app.post("/pokemon")
# def create_pokemon(pokemon: PokemonBase, db: db_dependency):
#     db_pokemon = Pokemon(
#         name=pokemon.name, type=pokemon.type, level=pokemon.level)
#     db.add(db_pokemon)
#     db.commit()
#     return {f"{db_pokemon.name}": "Sucessfully created"}


# @app.get("/pokemon")
# def get_all_pokemon(db: db_dependency):
#     query = select(Pokemon)
#     result = db.scalars(query).all()

#     return result


# may take a lil bit longer because adding a record to a db; makes a network call
    # RULE: if something is awaitable use await & by default will need to use async
    # when there is a async version of something try to use async
    # research if there are async methods of these methods or is it okay because we're usng async already or do we still need to await this?
