class Animal{

    constructor(nome, idade, preco){

        this.nome = nome
        this.idade = idade
        this.preco = preco

    }

    ChecarEstoque(){
        return 10
    }

    OutroMetodo(){
        console.log('Aqui tem um metodo')
    }

}

class Cachorro extends Animal{

    constructor(nome, idade, preco, raca, pelos){
        super(nome, idade, preco)
        this.raca = raca
        this.pelos = pelos
    }

    Latir(){
        console.log('Au AU')
    }

    // Sobrescreve o método da mae.
    ChecarEstoque(){
        console.log('Aqui tem 10 auau')
    }

    //Adicionando comportamentos para a classe mae
    OutroMetodo(){
        console.log('OutroMetodo do cachorro')
        super.OutroMetodo()
        console.log('Outra linha')
    }


}

var dog = new Cachorro('Dogao', 5, 150, 'xitzu', 'tem muito')

console.log(dog.ChecarEstoque())
console.log(dog.idade)
dog.Latir()
dog.ChecarEstoque()
dog.OutroMetodo()