from fastapi import FastAPI
from .routers import movies
from .database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(movies.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 Permite requisições de qualquer frontend
    allow_credentials=True,
    allow_methods=["*"],  # 🔥 Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # 🔥 Permite todos os headers
)