using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Exercicios
{
    class Lista1
    {

        public class Ponto {
            public double X;
            public double Y;

            public Ponto(double x, double y)
            {
                X = x;
                Y = y;
            }

            public static double DistanciaPontos(Ponto ponto1, Ponto ponto2) {

                double distancia = Math.Sqrt(Math.Pow((ponto2.X - ponto1.X), 2) + Math.Pow((ponto2.Y - ponto1.Y), 2));

                return distancia;
            }

        }

        public static void Executar() {
            var enunciados = new List<String>();
            bool continuar = true;

            while (continuar) {
                
                enunciados.Add("Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer no plano, P(x1,y1) e P(x2,y2), escreva a distância entre eles.");
                enunciados.Add("Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão: D=((A+B)^2/(B+C)^2)/2");
                enunciados.Add("Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias.");
                enunciados.Add("Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.");
                enunciados.Add("Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente.");
                enunciados.Add("Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa em segundos e mostre-o expresso em horas, minutos e segundos.");
                enunciados.Add("O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.");
                enunciados.Add("Um sistema de equações lineares do tipo: x = (ce - bf)/(ae - bd) e y = (af - cd)/(ae - bd). Escreva um algoritmo que lê os coeficientes a,b,c,d,e e f e calcula e mostra os valores de x e y.");
                enunciados.Add("Calcule a média aritmética das 3 notas de um aluno e mostre, além do valor da média, uma mensagem de 'Aprovado', caso a média seja igual ou superior a 6, ou a mensagem 'reprovado', caso contrário.");
                enunciados.Add("Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem: 'São múltiplos' ou 'Não são múltiplos'.");
                enunciados.Add("Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias: infantil A = 5 - 7 anos | infantil B = 8-10 anos | juvenil A = 11-13 anos | juvenil B = 14-17 anos | adulto = maiores de 18 anos");
                enunciados.Add("Escreva um algoritmo que leia 3 números inteiros e mostre o maior deles.");
                enunciados.Add("Escreva um algoritmo que leia o código de um aluno e suas três notas. Calcule a média ponderada do aluno, considerando que o peso para a maior nota seja 4 e para as duas restantes, 3. Mostre o código do aluno, suas três notas, a média calculada e uma mensagem 'APROVADO' se a média for maior ou igual a 5 e 'REPROVADO' se a média for menor que 5.");
                enunciados.Add("Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando se este número é par ou ímpar, e se é positivo ou negativo.");
                enunciados.Add("Tendo como dados de entrada a altura e o sexo de uma pessoa (?M? masculino e ?F? feminino), construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: para homens: (72.7*h)-58, para mulheres: (62.1*h)-44.7");

                foreach (var e in enunciados) {
                    Console.WriteLine($"{enunciados.IndexOf(e)+1}: {e}");
                    Console.WriteLine("\n");
                }

                Console.WriteLine("Digite o numero do exercicio");
                int ExercicioExecutar = Convert.ToInt32(Console.ReadLine());

                switch (ExercicioExecutar)
                {

                    case 1:
                        Console.WriteLine("Digite o valor X e Y do primeiro Ponto, separados por espaço");
                        double p1X = Convert.ToDouble(Console.ReadLine());
                        double p1Y = Convert.ToDouble(Console.ReadLine());

                        Console.WriteLine("Digite o valor X e Y do segundo Ponto, separados por espaço");
                        double p2X = Convert.ToDouble(Console.ReadLine());
                        double p2Y = Convert.ToDouble(Console.ReadLine());

                        Ponto ponto1 = new Ponto(p1X, p1Y);
                        Ponto ponto2 = new Ponto(p2X, p2Y);


                        Console.WriteLine(Ponto.DistanciaPontos(ponto1, ponto2));

                        break;

                    case 2:

                        Console.WriteLine("Digite os valores de A, B e C para a equação ((A+B)^2/(B+C)^2)/2");

                        int a = Convert.ToInt32(Console.ReadLine());
                        int b = Convert.ToInt32(Console.ReadLine());
                        int c = Convert.ToInt32(Console.ReadLine());

                        double d = (Math.Pow((a + b), 2) + Math.Pow((b + c), 2)) / 2;

                        Console.WriteLine(d);

                        break;
                        
                    case 3:

                        Console.WriteLine("Digite seu dia de nascimento, mes e ano");

                        int dia = Convert.ToInt32(Console.ReadLine());
                        int Mes = Convert.ToInt32(Console.ReadLine());
                        int Ano = Convert.ToInt32(Console.ReadLine());

                        DateTime idade = new DateTime(Ano, Mes, dia);
                        var agora = DateTime.Now;

                        Console.WriteLine($"Você tem {agora.Subtract(idade).Days} dias vividos");

                        break;

                    case 4:

                        Console.WriteLine("Digite quantos dias vc viveu");

                        decimal DiasVividos = Convert.ToInt32(Console.ReadLine());


                        var totalYears = Math.Truncate(DiasVividos/365);
                        var totalMonth = Math.Truncate((DiasVividos % 365) / 30);

                        Console.WriteLine(totalYears);
                        Console.WriteLine(totalMonth);

                        break;

                    case 5:
                        var notas = new List<double>();
                        int PesoNota = 1;
                        double media = 0;

                        for (var i = 0; i < 3; i++) {
                            Console.WriteLine($"Digite o valor da nota numero {i+1}");
                            notas.Add(Convert.ToDouble(Console.ReadLine()));
                        }

                        foreach (var nota in notas) {
                            switch (notas.IndexOf(nota)) {

                                case 0:
                                    PesoNota = 2;
                                    break;

                                case 1:
                                    PesoNota = 3;
                                    break;

                                case 2:
                                    PesoNota = 5;
                                    break;
                            }

                            media += nota*PesoNota;
                        }

                        Console.WriteLine($"Media final do aluno {media/3}");

                        break;

                    case 6:
                        double evento = Convert.ToDouble(Console.ReadLine());
                        var EventoMinutos = (evento/60);
                        var EventoHoras = (EventoMinutos / 60);


                        Console.WriteLine($"O evento tera {EventoMinutos} minutos ou {EventoHoras.ToString("F2")} horas");


                        break;

                    case 7:
                        //O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
                        //Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.
                        double CustoCarro = Convert.ToDouble(Console.ReadLine());
                        var distribuidor = CustoCarro * 0.28;
                        var impostos = CustoCarro * 0.45;

                        Console.WriteLine($"O custo do carro é de {CustoCarro + distribuidor + impostos}");

                        break;

                    case 8:
                        double valor_a = Convert.ToDouble(Console.ReadLine());
                        double valor_b = Convert.ToDouble(Console.ReadLine());
                        double valor_c = Convert.ToDouble(Console.ReadLine());
                        double valor_d = Convert.ToDouble(Console.ReadLine());
                        double valor_e = Convert.ToDouble(Console.ReadLine());
                        double valor_f = Convert.ToDouble(Console.ReadLine());

                        double x = ((valor_c * valor_e) - (valor_b * valor_f))/((valor_a * valor_e) - (valor_b * valor_d));
                        double y = ((valor_a * valor_f) - (valor_c * valor_d)/((valor_a * valor_e) - (valor_b * valor_d)));

                        Console.WriteLine($"Valor de X: {x} --> Valor de Y: {y}");

                        break;

                    case 9:
                        //Calcule a média aritmética das 3 notas de um aluno e mostre, além do valor da média, uma mensagem de 'Aprovado', caso a média seja igual ou superior a 6,
                        //ou a mensagem 'reprovado', caso contrário.
                        double nota1 = Convert.ToDouble(Console.ReadLine());
                        double nota2 = Convert.ToDouble(Console.ReadLine());
                        double nota3 = Convert.ToDouble(Console.ReadLine());

                        double media_9 = (nota1 + nota2 + nota3) / 3;

                        if (media_9 >= 6)
                        {
                            Console.WriteLine($"Aprovado com a media: {media_9}");

                        }
                        else {
                            Console.WriteLine("Reprovado");
                        }

                        break;

                    case 10:
                        //Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem: 'São múltiplos' ou 'Não são múltiplos'.
                        double valor1 = Convert.ToDouble(Console.ReadLine());
                        double valor2 = Convert.ToDouble(Console.ReadLine());

                        if (valor1 > valor2 && valor1 % valor2 == 0)
                        {
                            Console.WriteLine("Sao Multiplos");
                        }
                        else if (valor1 < valor2 && valor2 % valor1 == 0)
                        {
                            Console.WriteLine("Sao Multiplos");
                        }
                        else
                        {
                            Console.WriteLine("Não sao multiplos.");
                        }

                        break;

                    case 11:
                        //Elabore um algoritmo que dada a idade de um nadador classifica - o em uma das seguintes categorias:
                        //infantil A = 5 - 7 anos |
                        //infantil B = 8 - 10 anos |
                        //juvenil A = 11 - 13 anos |
                        //juvenil B = 14 - 17 anos |
                        //adulto = maiores de 18 anos

                        break;

                    default:
                        Console.WriteLine("Nenhuma opção valida digitada, programa finalizado.");
                        continuar = false;
                        break;

                }
                Console.WriteLine("Deseja continuar? [Y/N]");
                continuar = false;

            }

        }
    }
}
