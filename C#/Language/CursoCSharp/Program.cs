using System;
using System.Collections.Generic;

// Imports indicando para o C# onde que ele tem que buscar os executaveis.
using CursoCSharp.Fundamentos;
using CursoCSharp.EstruturaControle;
using CursoCSharp.ClassesEMetodos;
using CursoCSharp.Colecoes;
using CursoCSharp.OO;
using CursoCSharp.Exercicios;
using CursoCSharp.MetodosFuncoes;
using CursoCSharp.Excepts;
using CursoCSharp.Api;
using CursoCSharp.TopicosAvancados;

namespace CursoCSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            var central = new CentralDeExercicios(new Dictionary<string, Action>() {
                { "Lista de Exercicios: https://www.inf.pucrs.br/~pinho/LaproI/Exercicios/SeqDecisao/lista1.htm", Lista1.Executar},
                {"Primeiro Programa - Fundamentos", PrimeiroPrograma.Executar},
                {"Comentário - Fundamentos", Comentarios.Executar},
                {"Variaveis e constantes - Fundamentos", VariaveisEConstantes.Executar},
                {"Inferencia", Inferencia.Executar},
                {"Interpolacao", Interpolacao.Executar},
                {"Notacao Ponto", NotacaoPonto.Executar},
                {"Lendo Dados", LendoDados.Executar},
                {"Formatando Dados", FormatandoNumeros.Executar},
                {"Conversoes", Conversoes.Executar},
                {"operacoes aritmeticas", OperadoresAritmeticos.Executar},
                {"Operadores Relacionais", OperadoresRelacionais.Executar},
                {"Operadores de condicoes", EstruturaIF.Executar},
                {"Classes e metodos", Membro.Executar},
                {"Construtor", Construtores.Executar},
                {"Metodos Com Retorno", MetodosComRetorno.Executar},
                {"Metodos Estaticos", MetodosEstaticos.Executar},
                {"Atributos Estaticos", AtributoEstático.Executar},
                {"Desafio", DesafioAcessarAtributo.Executar},
                {"Param", Params.Executar},
                {"Recursividade", Recursividade.Executar},
                {"Parametros Nomeados", ParametrosNomeados.Executar},
                {"Getter e Setter", GetSet.Executar},
                {"Propriedades", Props.Executar},
                {"Apenas Leitura", Readonly.Executar},
                {"Enum", ExemploEnum.Executar},
                {"Struct", StructExemplo.Executar},
                {"Struct vs Classes", StructVSClasses.Executar},
                {"Valor Vs Referencia", ValorVSReferencia.Executar},
                {"Parametros por Ref", ParametrosPorReferencia.Executar},
                {"Colecao", Arrays.Executar},
                {"Listas", Listas.Executar},
                {"Array Listas", ArrayListExemple.Executar},
                {"Set", SetExemplo.Executar},
                {"Colecoes Queue", ColecoesQueue.Executar},
                {"Igualdade", Igualdade.Executar},
                {"Stack", StackExemplo.Executar},
                {"Dicionario", DicionarioExemplo.Executar},
                {"Heranca", Heranca.Executar},
                {"Construtor This", ConstrutorThis.Executar},
                {"Polimorfismo", Polimorfismo.Executar},
                {"Abstrato", Abstrato.Executar},
                {"Interfaces", InterfaceExemplo.Executar},
                {"ClasseSealed", ClasseSealed.Executar},
                {"Lambda", LambdaExecmple.Executar},
                {"Delegate Lambda", DelegateLambda.Executar},
                {"Delegate Lambda Exemplos", UsingDelegate.Executar},
                {"Delegate Lambda Anonima", FuncoesAnonimas.Executar},
                {"Delegate Com Parametros", DelegateComParametros.Executar},
                {"Metodo Extensao", MetodoExtensao.Executar},
                {"Exercecoes", ExceptTreatment.Executar},
                {"Excecoes Personalizadas", ExcecoesPersolnalizadas.Executar},
                {"Primeiro Arquivo", PrimeiroArquivo.Executar},
                {"Lendo Arquivo", LendoArquivo.Executar},
                {"File Info", FileInfoExemplo.Executar},
                {"Date Time", DateTimeExeplo.Executar},
                {"Time Span", TimeSpanExemplo.Executar},
                {"Linq1", LINQ1.Executar},
                {"Linq2", LINQ2.Executar},
            });

            central.SelecionarEExecutar();
        }
    }
}