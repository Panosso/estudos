var nomeMeu = 'Pedro'
var idade = 32

var empresa = {
    nome: 'VAT',
    cidade: 'Rib Preto',
    site: 'www.vatrockbar.com.br',
    email: 'machado@onarockbar.com.br'
}



//Só de colocar as variaveis pelo nome é o equivalente a:
// nome: nome

//e ao colocar os 3 pontos (Spread operator), é somado as 2 variaveis, ficando assim:
// cidade:"Rib Preto"
// email:"machado@onarockbar.com.br"
// idade:32
// nome:"VAT"
// site: "www.vatrockbar.com.br"

var user = {
    nome,
    idade,
    ...empresa
}


//Desestruturação: Modo para 'quebrar' o object em partes:
// Lembrando que é necessário pegar o valor da chave para gerar uma variavel.
var { nome, cidade, email } = empresa

console.log(nome);


//Arrow Function: Funções flecha

//Está atribuindo o callback da função para a variavel mult
var mult = (a, b, c) => {
    console.log(a*b*c);
    
}