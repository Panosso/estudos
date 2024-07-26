var http = require("http")
var auxiliar = require("./auxiliar")

http.createServer(function (request, response){
    response.end("Bem vindo ao meu site")
}).listen(8181);

console.log('Servidor Rodando');


