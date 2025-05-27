
# 🎬 Filmes App - Catálogo de Filmes com Análise Personalizada

Este projeto é uma aplicação fullstack para importar, categorizar e visualizar dados de filmes de forma automatizada.

---

## 🚀 Funcionalidades

✅ Importação automática de filmes populares via API TMDb  
✅ Armazenamento relacional de filmes, atores, categorias e premiações  
✅ Classificação de gêneros conforme `GENRE_MAPPING`  
✅ Exibição de informações com React + Tailwind CSS  
✅ Filtros por título, ano, gênero e streaming  
✅ Visualização de atores principais e premiações associadas  

---

## 🏗️ Estrutura do Projeto

```
/app
  ├── database.py     # Configuração do banco SQLAlchemy
  ├── models.py       # Modelos: Filme, Ator, Categoria, Premiação
  ├── crud.py         # Operações no banco
  ├── tmdb_importer.py # Script de importação da API TMDb
  └── routers/        # Rotas FastAPI

/filmes-frontend
  ├── src/
  │   ├── components/ # Filtros e outros componentes
  │   ├── App.jsx     # Página principal
  │   ├── api.js      # Serviço de consumo da API
  │   └── index.css   # Estilo com Tailwind
```

---

## ⚙️ Tecnologias

### Backend:
- 🐍 Python 3.10+
- 🚀 FastAPI
- 🐘 PostgreSQL
- 🐳 Docker
- 🛠️ SQLAlchemy

### Frontend:
- ⚛️ React.js
- 🎨 Tailwind CSS
- ⚡ Vite

---

## 📦 Como rodar localmente

### ➡️ Backend:

```bash
cd app
docker-compose up --build
```

Importe os filmes:

```bash
docker-compose exec backend python -m app.tmdb_importer
```

### ➡️ Frontend:

```bash
cd filmes-frontend
npm install
npm run dev
```

Acesse: http://localhost:5173

---

## 🗄️ Banco de Dados

- Estrutura relacional: **Filmes** ↔ **Categorias**, **Atores**, **Premiações**
- Autopreenchimento através de integração com a **API TMDb**.

---

## 🌍 Deploy

Recomendado via:
- **Render** / **Railway** para backend
- **Vercel** / **Netlify** para frontend

---

## 🙌 Contribuições

Contribuições são bem-vindas!  
Sinta-se à vontade para enviar um PR ou abrir uma issue.

---

## 📝 Licença

MIT License.
