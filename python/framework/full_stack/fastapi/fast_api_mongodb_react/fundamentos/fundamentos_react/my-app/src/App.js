import logo from './logo.svg';
import './App.css';
import HelloWorld from './components/HelloWorld';
import MeuNome from './components/MeuNome';
import Profissional from './components/Profissional';

function App() {
  const nome = "Pedro Panosso"
  const novoNome = nome.toUpperCase()
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          {novoNome} <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <HelloWorld/>
        <MeuNome nome="Pedro"/>
        <Profissional nome="Pedro" idade='32' profissao="Programador" foto="https://www.planura.mg.leg.br/imagens/teste.jpg/image_preview"/>
      </header>
    </div>
  );
}

export default App;
