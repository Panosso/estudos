import axios from 'axios';
import './App.css';
import {useState, useEffect} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import JogadorList from './components/JogadorList';

function App() {

    // equivalente ao get e set em linguagens como Java
    const [jogadorList, setJogadorList] = useState([{}])
    const [jogadorId, setJogadorId] = useState('');
    const [jogadorNome, setJogadorNome] = useState('');
    const [jogadorIdade, setJogadorIdade] = useState('');
    const [jogadorTime, setJogadorTime] = useState('');
    const [textoBotao, setTextoBotao] = useState('Cadastrar')

    useEffect(() => {
    axios.get('http://localhost:8000/jogadores/todos_jogadores')
            .then( resposta => {
            console.log(resposta.data)
            setJogadorList(resposta.data)
            })
            .catch((error) => {console.log(error)})
    })


    const adicionarAtualizaJogador = () => {

        const jogador = {
            'jogador_nome': jogadorNome,
            'jogador_idade': jogadorIdade,
            'jogador_time': jogadorTime
        }

        if(jogadorId !== ''){
            atualizaJogador(jogador)
        }else{
            adicionaJogador(jogador)
        }
    }

    const adicionaJogador = (jogador) => {

        axios.post('http://localhost:8000/jogadores/inserir', jogador).then(resposta => {
            console.log('Criado com sucesso')
        }).catch((error) => {
            console.log(error)
        })

    }

    const atualizaJogador = (jogador) => {
        axios.put(`http://localhost:8000/jogadores/atualizar/${jogadorId}`, jogador)
        .then(resposta => {
            alert('Jogador Atualizado')
        }).catch((error) => {
            console.log(error);
        })
    }

    return (
    <div className="container">
        <div className='mt3 justify-content-center -align-items-center mx-auto' style={{"width": "70vw", "backgroundColor": "#ffffff"}}>

        <h2 className='text-center text-white bg-success mb-1'>Gerenciamento de jogadores</h2>
        <h6 className='card text-center text-white bg-success mb-1 pb-1'>Informações do Jogador</h6>

        <div className='card-body text-center'>

            <h5 className='card text-center text-white bg-dark mb-2 pb-1'>Cadastro Jogador</h5>
            <span className='card-text'>

            <input className='mb-2 form-control' placeholder='Informe o nome' onChange={evento => setJogadorNome(evento.target.value)} value={jogadorNome}/>
            <input className='mb-2 form-control' placeholder='Informe a idade' onChange={evento => setJogadorIdade(evento.target.value)} value={jogadorIdade}/>
            <input className='mb-2 form-control' placeholder='Informe o time' onChange={evento => setJogadorTime(evento.target.value)} value={jogadorTime}/>
            <button className='btn btn-outline-success mb-4' onClick={adicionarAtualizaJogador}>{textoBotao}</button>
            </span>
            <h5 className='card text-center text-white bg-dark pb-1'>Lista de jogadores</h5>

            <div>
            <JogadorList 
                jogadorList={jogadorList} 
                setJogadorId={setJogadorId}
                setJogadorNome={setJogadorNome}
                setJogadorIdade={setJogadorIdade}
                setJogadorTime={setJogadorTime}
                setTextoBotao={setTextoBotao}
                
                />
            </div>

            <h6 className='card text-center text-light bg-success py-1'>&copy; Pedro Panosso 2024</h6>
        </div>

        </div>
    </div>
    );
}

export default App;
