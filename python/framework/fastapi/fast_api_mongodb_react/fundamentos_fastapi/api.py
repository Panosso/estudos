from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

#Referencia da nossa aplicação no fast API
app = FastAPI()

#Pydantic é usado para criar uma modelo base
class Jogador(BaseModel):
    nome: str
    idade: int
    time: str

class AttJogador(BaseModel):
    #Optional faz com que a informação não seja obrigatória para atualizar o jogador
    nome: Optional[str] = None
    idade: Optional[int] = None
    time: Optional[str] = None

jogadores = {
    1: {
        "nome": 'Showmaker',
        "idade": 22,
        "time": 'SKT1'
    },
    2: {
        "nome": 'Faker',
        "idade": 22,
        "time": 'TSM'
    },
    3: {
        "nome": 'Fallen',
        "idade": 22,
        "time": 'TSM'
    },
    4: {
        "nome": 'Fer',
        "idade": 22,
        "time": 'TSM'
    },
    5: {
        "nome": 'Gus',
        "idade": 22,
        "time": 'TSM'
    },
}

@app.get("/")
def inicio():
    return jogadores

#Informação via path conhecido como 'path parameter', ou seja, eu informo o id_jogador no proprio path, exemplo: http://127.0.0.1:8000/get_jogador/1
@app.get("/get_jogador/{id_jogador}")
def get_jogador(id_jogador: int):
    return jogadores[id_jogador]


#Informação via query, conhecido como 'query parameter', ou seja, eu preciso informar o nome da variavel, exemplo: http://localhost:8000/get_jogador_time?time=TSM
@app.get("/get_jogador_time")
def get_jogador_time(time: str):
    jogadores_time = []
    print(jogadores)
    for jogador_id in jogadores:
        if jogadores[jogador_id]['time'] == time:
            jogadores_time.append(jogadores[jogador_id])

    if jogadores_time:
        return jogadores_time

    return {'Dados': 'Nao foi achado'}


#Utilizando o método POST, usado para inserir dados
@app.post("/cadastro_jogador/{jogador_id}")
def cadastro_jogador(jogador_id: int, jogador: Jogador):
    
    if jogador_id in jogadores:
        return {'Erro': 'Jogador ja existe'}

    jogadores[jogador_id] = jogador

    return jogadores[jogador_id]

#Método usado para deletar um registro
@app.delete("/exclusao-jogador/{jogador_id}")
def exclui_jogador(jogador_id: int):
    if jogador_id not in jogadores:
        return {'Erro': 'Jogador ja existe'}

    del jogadores[jogador_id]

    return {'Deletado': 'Jogador ja era!!!'}

#Metodo usado para atualizar um registro
@app.put("/atualizar_jogador/{jogador_id}")
def att_jogador(jogador_id: int, jogador: AttJogador):
    if jogador_id not in jogadores:
        return {'Erro': 'Jogador não existe'}

    if jogador.nome != None:
        jogadores[jogador_id]["nome"] = jogador.nome

    if jogador.idade != None:
        jogadores[jogador_id]["idade"] = jogador.idade

    if jogador.time != None:
        jogadores[jogador_id]["time"] = jogador.time

    return {'Sucesso': 'Deu certo a atualização'}