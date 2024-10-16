class Filme{

    /*Semelhante ao __init__ do python*/
    constructor(){

        this.titulo = '';
        this.ano = 2000;
        this.genero = '';
        this.diretor = '';
        this.atores = [];
        this.duracao = 0;

    }

    /*Nome dos métodos inicial maiuscula*/
    Reproduzir(){
        console.log('Reproduzindo')
    }

    Pausar(){
        console.log('Pausa')
    }

    Avancar(){
        console.log('Avançar')
    }

    Fechar(){
        console.log('Fechar')
    }

}

var vingadores = new Filme();

vingadores.titulo = 'Vingadores'

vingadores.Reproduzir();

console.log('Filme: ' + vingadores.titulo)