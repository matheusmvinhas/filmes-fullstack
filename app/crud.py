from . import models, schemas
from sqlalchemy.orm import Session
from sqlalchemy import and_, cast, String
from .models import Movie
from typing import List, Optional

def get_movies(db: Session, title: Optional[str] = None, genre: Optional[str] = None, year: Optional[int] = None) -> List[Movie]:
    """Busca filmes filtrando por título, gênero ou ano."""
    query = db.query(Movie)

    conditions = []

    if title and title.strip():
        conditions.append(Movie.title.ilike(f"%{title.strip()}%"))  # Busca parcial no título
    
    if genre and genre.strip():
        conditions.append(Movie.genre.ilike(f"%{genre.strip()}%"))  # Busca por gênero
    
    if year:
        conditions.append(cast(Movie.release_date, String).like(f"{year}-%"))  # Converte DATE para STRING

    if conditions:
        query = query.filter(and_(*conditions))

    print(f"🛠 SQL Gerado: {str(query.statement.compile(compile_kwargs={'literal_binds': True}))}")

    result = query.all()
    print(f"🎯 Filmes encontrados: {len(result)}\n")  # Depuração final
    return result

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie