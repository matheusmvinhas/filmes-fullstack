from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas
from typing import List, Optional

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/movies/", response_model=schemas.MovieResponse)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

@router.get("/movies/", response_model=List[schemas.MovieResponse])
def read_movies(
    title: Optional[str] = Query(None, description="Filtrar por título"),
    genre: Optional[str] = Query(None, description="Filtrar por gênero"),
    year: Optional[int] = Query(None, description="Filtrar por ano"),
    db: Session = Depends(get_db)
):
    print(f"\n🔎 Recebendo filtros: title={title}, genre={genre}, year={year}")  # Log dos parâmetros
    movies = crud.get_movies(db, title=title, genre=genre, year=year)
    print(f"🎯 Filmes encontrados: {len(movies)}\n")  # Log da quantidade de filmes encontrados
    return movies