from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from .database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    release_date = Column(Date, nullable=True)
    genre = Column(String, nullable=True)  # Gêneros armazenados como string (ex: "28, 12, 16")
    overview = Column(String, nullable=True)  # Sinopse
    original_language = Column(String, nullable=True)  # Idioma original
    vote_average = Column(Float, nullable=True)  # Média de votos
    vote_count = Column(Integer, nullable=True)  # Número de votos
    popularity = Column(Float, nullable=True)  # Popularidade do filme
    poster_path = Column(String, nullable=True)  # URL da imagem do pôster
    backdrop_path = Column(String, nullable=True)  # URL da imagem de fundo
    adult = Column(Boolean, default=False)  # Se é para adultos
    video = Column(Boolean, default=False)  # Se contém vídeo
    streaming = Column(String, nullable=True)  # 📺 Novo campo para plataformas de streaming
    actors = Column(String)  # Novo campo para os atores principais
    awards = Column(String)