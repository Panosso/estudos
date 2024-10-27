class Dado{

    constructor(faces){
        this.faces = faces
    }

    Rolar(){
        
        console.log("Resultado do dado: " + this.GetRandomNumber(1, this.faces))

    }

    GetRandomNumber(min, max){
        min = Math.ceil(min);
        max = Math.floor(max)
        return Math.floor(Math.random() * (max - min + 1))+ min;
    }
}

var dado = new Dado(20);

dado.Rolar()