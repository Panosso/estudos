from fastapi import FastAPI
from routes.jogador import jogador_route
from fastapi.middleware.cors import CORSMiddleware

#Permite adicionar apenas os clientes que podem acessar a API
cliente_app = [
    "http://localhost:3000"
]

app = FastAPI()

app.include_router(jogador_route, prefix='/jogadores')

app.add_middleware(CORSMiddleware,
                   allow_origins=cliente_app,
                   allow_credentials=True,
                   allow_methods = ["*"],
                   allow_headers = ["*"])