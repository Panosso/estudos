var Reader = require("./Reader")
var Processor = require("./Processador")
var Table = require("./Table")
var HtmlParser = require("./HtmlParser")
var Writer = require("./Writer")
var PDFWriter = require("./PDFWriter")

var leitor = new Reader();
var escritor = new Writer();

async function main() {

    var dados = await leitor.Read('./users.csv');
    var dadosProcessados = Processor.Process(dados);
    var usuarios = new Table(dadosProcessados)

    usuarios.rows.push(['Pedro', 'python', 'IA', 4])

    var html = await HtmlParser.Parse(usuarios);

    escritor.Write('meuhtml.html', html)
    PDFWriter.WritePDF('meuhtml.pdf', html)
}

main()