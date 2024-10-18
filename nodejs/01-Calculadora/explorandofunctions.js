// Simple Function without return
function nome(nome_pessoa){
    console.log("O nome da pessoa é: " + nome_pessoa)
}

// Simples function with return
function nome_return(nome_pessoa){
    return "O nome da pessoa é: " + nome_pessoa
}

// console.log(nome_return('Pedro'))


// Arrow Function: In the arrow functions, 'this' is the owner of the function.
var hello = () => 'Ola Mundo'

// That function it's the same as:
function hello(){
    return 'Ola Mundo'
}

// console.log(hello())

//Arrow Function with parameter
var goodbye = (last_goodbye) => 'So my friend this is my: ' + last_goodbye 

// That function it's the same as:
function goodbye(last_goodbye){
    return 'So my friend this is my: ' + last_goodbye
}

// console.log(goodbye('LastGoodBye'))

//In the arrow functions, 'this' is the owner of the function.
let yarroy = () => { return this }

console.log(yarroy())

//Callback functions: A callback is a function passed as an argument to another function.
// In this exemple, we gonna call the function soma, and pass 3 parameters a,b and callback_function function
function callback_function(algo){
    console.log(algo)
}

function soma(a, b, myCallback){
    let sum = a + b
    myCallback(sum)
}

soma(3, 4, callback_function)

