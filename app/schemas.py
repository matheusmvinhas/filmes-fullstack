from pydantic import BaseModel
from typing import Optional
from datetime import date

class MovieBase(BaseModel):
    title: str
    release_date: Optional[date] = None
    genre: Optional[str] = None
    overview: Optional[str] = None
    original_language: Optional[str] = None
    vote_average: Optional[float] = None
    vote_count: Optional[int] = None
    popularity: Optional[float] = None
    poster_path: Optional[str] = None
    backdrop_path: Optional[str] = None
    adult: Optional[bool] = None
    video: Optional[bool] = None
    streaming: Optional[str] = None  # 📺 Novo campo para plataformas de streaming
    actors: Optional[str] = None
    awards: Optional[str] = None

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int

    class Config:
        orm_mode = True