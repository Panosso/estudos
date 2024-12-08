from fastapi import APIRouter
from config.database import conexao
from models.jogador import Jogador
from schemas.jogador import jogadorEntidade, listaJogadoresEntidade
from bson import ObjectId

jogador_route = APIRouter()

@jogador_route.get("/")
async def inicio():
    return 'Bemvindo ao fullstack farm'

@jogador_route.get('/todos_jogadores')
async def lista_jogadores():
    return listaJogadoresEntidade(conexao.farm.jogador.find())

@jogador_route.get('/dados_jogador/{jogador_id}')
async def get_jogador_by_id(jogador_id):
    return jogadorEntidade(conexao.farm.jogador.find_one(
        {"_id": ObjectId(jogador_id)}
    ))

#Interface uniforme é quando eu tenho o mesmo nome de rota porém com métodos diferentes:
@jogador_route.post('/inserir')
async def inserir_jogador(jogador: Jogador):
    conexao.farm.jogador.insert_one(dict(jogador))
    return listaJogadoresEntidade(conexao.farm.jogador.find())

#Utilizando a variavel $set é possivel atualizar o dado
@jogador_route.put('/atualizar/{jogador_id}')
async def atualizar_jogador(jogador_id, jogador: Jogador):
    conexao.farm.jogador.find_one_and_update(
        {"_id": ObjectId(jogador_id)},
        {"$set": dict(jogador)}
        )

    return jogadorEntidade(conexao.farm.jogador.find_one(
        {"_id": ObjectId(jogador_id)}
    ))

@jogador_route.delete('/detetar/{jogador_id}')
async def deletar_jogador(jogador_id):
    conexao.farm.jogador.find_one_and_delete({"_id": ObjectId(jogador_id)})

    return "Jogador deletado"