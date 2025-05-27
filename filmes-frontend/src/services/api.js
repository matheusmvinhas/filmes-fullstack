import axios from "axios";

const API_BASE_URL = "http://localhost:8000/movies/";

export const fetchMovies = async () => {
  try {
    const response = await axios.get(API_BASE_URL);
    return response.data;
  } catch (error) {
    console.error("Erro ao buscar filmes:", error);
    return [];
  }
};