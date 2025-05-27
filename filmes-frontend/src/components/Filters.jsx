import React, { useState, useEffect } from "react";

export default function Filters({ setSearchParams, className }) {
  const [title, setTitle] = useState("");
  const [year, setYear] = useState("");
  const [genre, setGenre] = useState("");
  const [streaming, setStreaming] = useState("");

  useEffect(() => {
    setSearchParams({ title, year, genre, streaming });
  }, [title, year, genre, streaming, setSearchParams]);

  return (
    <div className={`bg-gray-800 p-4 rounded-lg shadow-lg ${className}`}>
      <div className="flex flex-col sm:flex-row gap-4">
        <input
          type="text"
          placeholder="Buscar por título..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="p-2 w-full sm:w-1/3 rounded bg-gray-700 text-white placeholder-gray-400 border border-gray-600"
        />
        <input
          type="number"
          placeholder="Ano"
          value={year}
          onChange={(e) => setYear(e.target.value)}
          className="p-2 w-full sm:w-1/4 rounded bg-gray-700 text-white placeholder-gray-400 border border-gray-600"
        />
        <select
          value={genre}
          onChange={(e) => setGenre(e.target.value)}
          className="p-2 w-full sm:w-1/4 rounded bg-gray-700 text-white border border-gray-600"
        >
          <option value="">Todos os Gêneros</option>
          <option value="Ação">Ação</option>
          <option value="Comédia">Comédia</option>
          <option value="Drama">Drama</option>
          <option value="Ficção Científica">Ficção Científica</option>
          <option value="Terror">Terror</option>
        </select>
        <select
          value={streaming}
          onChange={(e) => setStreaming(e.target.value)}
          className="p-2 w-full sm:w-1/4 rounded bg-gray-700 text-white border border-gray-600"
        >
          <option value="">Todos os Streamings</option>
          <option value="Max">Max</option>
          <option value="Claro tv+">Claro tv+</option>
          <option value="Max Amazon Channel">Max Amazon Channel</option>
          <option value="Netflix">Netflix</option>
          <option value="Netflix basic with Ads">Netflix basic with Ads</option>
        </select>
      </div>
    </div>
  );
}