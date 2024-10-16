class Leitor{

    Ler(caminho){
        return 'Conteudo Arquivo'
    }

}

class Escritor{

    Escrever(arquivo, conteudo){
        console.log('Conteudo escrito')
    }

}

class Criador{
    Criar(nome){
        console.log('Arquivo criado')
    }
}

class Destruidor{
    Deletar(nome){
        console.log('Deletando')
    }
}

class ManipuladorDeArquivo{

    constructor(nome){
        this.arquivo = nome
        this.ler = new Leitor()
        this.escrever = new Escritor()
        this.criar = new Criador()
        this.destruidor = new Destruidor()
    }

}

class GerenciadorUsuario{

    constructor(){
        this.criador = new Criador()
        this.escritor = new Escritor()
    }

    SalvarListaDeUsuarios(lista){
        this.criador.Criar('Usuarios.txt')
        this.escritor.Escrever('Usuarios.txt', lista)
    }

}