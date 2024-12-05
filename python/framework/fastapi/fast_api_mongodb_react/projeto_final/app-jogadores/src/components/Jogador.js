import React from "react";
import axios from "axios";

function Jogador(props){
    
    const excluiJogador = (jogadorId) => {
        axios.delete(`http://localhost:8000/jogadores/detetar/${jogadorId}`)
    }

    const editarJogador = (jogador) => {
        props.setJogadorId(jogador.id)
        props.setJogadorNome(jogador.nome)
        props.setJogadorIdade(jogador.idade)
        props.setJogadorTime(jogador.time)
        props.setTextoBotao('Atualizar')
    }

    return (
        <div>
            <p>
                <span className="fw-bold">
                    {props.jogador.nome} - {props.jogador.idade} - {props.jogador.time}
                </span>
                <button className="btn btn-sm"
                        onClick={ () => editarJogador(props.jogador)}>
                    <span className="badge rounded-pill bg-info">Editar</span>
                </button>
                <button className="btn btn-sm"
                        onClick={ () => excluiJogador(props.jogador.id)}>
                    <span className="badge rounded-pill bg-danger">X</span>
                </button>
            </p>
        </div>
    )
}

export default Jogador;