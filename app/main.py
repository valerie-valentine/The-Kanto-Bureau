from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class PokemonBase(BaseModel):
    pass


@app.get("/")
async def root():
    return {"message": "Hello world >:3"}
