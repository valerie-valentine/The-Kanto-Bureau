from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Annotated
from app.models import *
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/pokemon_stat")
def create_pokemon_stat(db: db_dependency):
    pass
