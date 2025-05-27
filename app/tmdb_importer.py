import os
import requests
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from .database import SessionLocal
from .models import Movie

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"

GENRE_MAPPING = {
    28: "Ação",
    12: "Aventura",
    16: "Animação",
    35: "Comédia",
    80: "Crime",
    99: "Documentário",
    18: "Drama",
    10751: "Família",
    14: "Fantasia",
    36: "História",
    27: "Terror",
    10402: "Música",
    9648: "Mistério",
    10749: "Romance",
    878: "Ficção Científica",
    10770: "Filme para TV",
    53: "Thriller",
    10752: "Guerra",
    37: "Faroeste"
}

def get_movie_categories(genre_ids):
    """Converte IDs de gênero para nomes legíveis."""
    return ", ".join([GENRE_MAPPING.get(gid, "Desconhecido") for gid in genre_ids])

def fetch_movies(pages=1):
    """Busca múltiplas páginas de filmes populares da API do TMDb."""
    all_movies = []
    
    for page in range(1, pages + 1):
        url = f"{TMDB_BASE_URL}/movie/popular?api_key={TMDB_API_KEY}&language=pt-BR&page={page}"
        response = requests.get(url)
        
        if response.status_code == 200:
            movies = response.json().get("results", [])
            all_movies.extend(movies)
            print(f"Página {page}: {len(movies)} filmes carregados.")
        else:
            print(f"Erro ao buscar página {page}: {response.status_code}")
            break  # Para de buscar se houver erro

    return all_movies

def get_streaming_services(movie_id):
    """Busca plataformas de streaming disponíveis para um filme no Brasil."""
    url = f"{TMDB_BASE_URL}/movie/{movie_id}/watch/providers?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json().get("results", {})
        br_data = data.get("BR", {})  # Pega dados do Brasil

        if "flatrate" in br_data:
            services = [provider["provider_name"] for provider in br_data["flatrate"]]
            return ", ".join(services)
    
    return None  # Retorna None se não houver serviços disponíveis

def fetch_movie_details(movie_id):
    """Obtém detalhes do filme, incluindo elenco e premiações."""
    details_url = f"{TMDB_BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}&append_to_response=credits,keywords"
    response = requests.get(details_url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Obtendo os três primeiros atores do elenco
        actors = [cast['name'] for cast in data.get('credits', {}).get('cast', [])[:3]]
        actors = ", ".join(actors) if actors else "Não disponível"
        
        # Obtendo palavras-chave relacionadas a premiações
        awards_keywords = ["oscar", "academy award", "golden globe", "best picture"]
        awards = [kw['name'] for kw in data.get('keywords', {}).get('keywords', []) if any(award in kw['name'].lower() for award in awards_keywords)]
        awards = ", ".join(awards) if awards else "Nenhum prêmio encontrado"
        
        return actors, awards
    return "Não disponível", "Nenhum prêmio encontrado"

def save_movies_to_db():
    """Salva os filmes no banco de dados, incluindo plataformas de streaming, atores e premiações."""
    db: Session = SessionLocal()
    movies = fetch_movies()

    for movie in movies:
        existing_movie = db.query(Movie).filter(Movie.title == movie["title"]).first()
        
        if not existing_movie:
            streaming_services = get_streaming_services(movie["id"])  # Obtém serviços de streaming
            actors, awards = fetch_movie_details(movie["id"])
            
            new_movie = Movie(
                title=movie["title"],
                release_date=movie.get("release_date"),
                genre=get_movie_categories(movie.get("genre_ids", [])),
                overview=movie.get("overview"),
                original_language=movie.get("original_language"),
                vote_average=movie.get("vote_average"),
                vote_count=movie.get("vote_count"),
                popularity=movie.get("popularity"),
                poster_path=f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get("poster_path") else None,
                backdrop_path=f"https://image.tmdb.org/t/p/w500{movie.get('backdrop_path')}" if movie.get("backdrop_path") else None,
                adult=movie.get("adult", False),
                video=movie.get("video", False),
                streaming=streaming_services,  # 📺 Adicionando plataformas de streaming
                actors=actors,  # 🎭 Adicionando atores principais
                awards=awards  # 🏆 Adicionando premiações
            )
            db.add(new_movie)
    
    db.commit()
    db.close()
    print(f"{len(movies)} filmes importados!")

if __name__ == "__main__":
    save_movies_to_db()
