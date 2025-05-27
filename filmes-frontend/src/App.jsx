import { useEffect, useState } from "react";
import { fetchMovies } from "./services/api";
import Filters from "./components/Filters";

export default function App() {
  const [movies, setMovies] = useState([]);
  const [searchParams, setSearchParams] = useState({ title: "", genre: "", year: "", streaming: ""});
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    fetchMovies().then(setMovies);
  }, []);

  const toggleFavorite = (movie) => {
    setFavorites((prev) =>
      prev.some((fav) => fav.id === movie.id)
        ? prev.filter((fav) => fav.id !== movie.id)
        : [...prev, movie]
    );
  };

  const filteredMovies = movies.filter((movie) =>
    (searchParams.title ? movie.title.toLowerCase().includes(searchParams.title.toLowerCase()) : true) &&
    (searchParams.genre ? movie.genre.includes(searchParams.genre) : true) &&
    (searchParams.year ? movie.release_date.startsWith(searchParams.year) : true) &&
    (searchParams.streaming ? (movie.streaming && movie.streaming.toLowerCase().includes(searchParams.streaming.toLowerCase())) : true) &&
    (searchParams.category ? (movie.category && movie.category.toLowerCase().includes(searchParams.category.toLowerCase())) : true)
  );

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <h1 className="text-3xl font-bold text-center mb-6">🎬 Meus Filmes</h1>
      <div className="mb-6 flex flex-col sm:flex-row justify-center gap-4 w-full max-w-4xl mx-auto">
        <Filters setSearchParams={setSearchParams} className="w-full sm:w-3/4 lg:w-2/3 xl:w-1/2" />
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8 place-items-center w-full max-w-6xl mx-auto">
        {filteredMovies.map((movie) => (
          <div key={movie.id} className="bg-gray-800 p-4 rounded-lg shadow-lg transition transform hover:scale-105 hover:shadow-xl flex flex-col items-center text-center border-4 border-white w-full max-w-xs">
            <img 
              src={`https://image.tmdb.org/t/p/w300${movie.poster_path}`} 
              alt={movie.title} 
              className="w-40 h-60 object-cover rounded-lg mt-2"
            />
            <h2 className="text-lg font-bold mt-2">{movie.title}</h2>
            <p className="text-gray-300">📖 {movie.overview}</p>
            <p className="text-sm text-gray-400">📅 {movie.release_date}</p>
            <p className="text-yellow-400 font-semibold mt-1">⭐ {movie.vote_average} / 10</p>
            <p className="text-green-400 text-sm">🔥 {movie.popularity}</p>
            <p className="text-blue-400">🏷 {movie.genre}</p>
            <p className="text-blue-400">🎭 Atores: {movie.actors}</p>
            <p className="text-green-400">🏆 Premiações: {movie.awards}</p>
            {movie.streaming ? (
              <p className="text-purple-400">📡 Disponível em: {movie.streaming}</p>
            ) : (
              <p className="text-gray-500">📡 Streaming não disponível</p>
            )}
            <button
              onClick={() => toggleFavorite(movie)}
              className={`mt-3 px-4 py-2 rounded-md text-white transition ${
                favorites.some((fav) => fav.id === movie.id) 
                  ? "bg-red-500 hover:bg-red-600" 
                  : "bg-blue-500 hover:bg-blue-600"
              }`}
            >
              {favorites.some((fav) => fav.id === movie.id) ? "⭐ Remover Favorito" : "⭐ Adicionar Favorito"}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}