#Exercicios video e site
#Exercicios site (http://www.lampada.uerj.br/arquivosdb/_book2/estruturas-b%C3%A1sicas-no-r.html#exerc%C3%ADcios)

#1. Quais são os resultados das seguintes expressões, respectivamente: 3 + 5*8/2^2 e (3 + 5)*8/(2^2)?
#R. a)13 e 16
a = 3+5*8/2^2 
b = (3+5)*8/(2^2)
resp = c(a, b)
resp

#2. Na expressão 30 - 6^2 / 2 * 3, qual a sequência dos cálculos até chegar ao resultado final?
#R. d)6^2, 36/2, 18*3, 30-54

#3. Após a sequência de comandos “x = 3; y = 4; x = x + 2*y; x=20 ”, qual será o valor de x?
#R. d) 20
x = 3
y = 4
x = x + 2*y
x = 20

#4. Se executarmos a expressão x = 6, qual será a classe do objeto x, se usarmos a função class?
#R. b) numeric
x = 6
class(x)

#5. Associe os vetores abaixo aos respectivos tipos de dados:
a = c(1, 2.5, 4, 0) #Numeric
b = c(TRUE, FALSE, FALSE, TRUE) #Logical
d = 1:40 #integer
e = c("a", "Jeannie", 5) #Character
f = c(2+4i, 3i, 3, 6) #complex
class(a)
class(b)
class(d)
class(e)
class(f)

#6. Se você tiver dois vetores x = c(2, 4, 5, 6) e y = c(-3, -2, 0, 7), qual será o resultado da expressão cbind(x, y)?
#R. c) Uma matriz de 2x4
x = c(2,4,5,6)
y = c(-3,-2,0,7)
cbind(x,y,z)

#7. Uma propriedade de vetores no R é que: (mais de uma resposta)
#a) os elementos de um vetor podem ser de diferentes classes.
#b) os elementos de um vetor precisam ser da mesma classe.
#c) os elementos de um vetor somente podem ser numeric ou character.
#d) se um vetor contiver elementos da classe character e da classe numeric, os elementos do tipo character são convertidos para numeric.
#e) se um vetor contiver elementos da classe character e da classe numeric, os elementos do tipo numeric são convertidos para character.#7. 
#R. b), e)

#8. Suponha que você tenha uma lista definida como x = list(4, “cara”, “coroa”, FALSE). O que a expressão x[[1]] fornece? Marque todas as opções corretas.
#a) um vetor do tipo character contendo o elemento “4”
#b) uma lista com o número 4
#c) um vetor numérico contendo o número 4
#d) um vetor numérico de comprimento 1
#e) uma lista contendo o elemento “4”
#f) um vetor contendo o elemento “cara”
#R. c d

x = list(4, "cara", "coroa", FALSE)
class(x[[1]])

#9. Suponha que você tenha um vetor x = c(4, 6, 8, 9, 12, 3, 2) e que você deseja fazer com que todos os elementos de x menor que 9 sejam iguais a zero. Selecione o código abaixo que gera o resultado esperado.
#R. x[x<9] <- 0
x = c(4, 6, 8, 9, 12, 3, 2)
x[x<9] <- 0

#10. Dado o vetor x = 1:12 , que expressões abaixo irão gerar uma matriz 3x4?
#a) matrix(x, ncol=4)
#b) matrix(x, nrow = 3)
#c) matrix(x, ncol=4, byrow = TRUE)
#d) matrix(x)
#e) matrix(x, nrow = 4)
#f) matrix(x, ncol = 3)
#R. a), b), c)
x = 1:12
matrix(x, ncol=4, byrow = TRUE)
dim(matrix(x, ncol=4, byrow = TRUE))

#11. Dada a matrix gerada pela expressão x = matrix(1:12 , ncol = 4), que afirmações abaixo são verdadeiras?
#a)x[2,3] = 8
#b)x[2,3] = 6
#c)x[1,] = (1, 2, 3, 4)
#d)x[1, ] = (1, 4, 7, 10)
#e)x[c(1,3), 3] = (7, 9)
#f)x[1, c(2,3)] = (1, 2, 3)
#R. a), d), e)
x = matrix(1:12 , ncol = 4)

#12. Que afirmações abaixo são verdadeiras em relação a data frames?
#a) data frames são iguais a matrizes
#b) os componentes de um data frame são listas onde cada lista pode possuir qualquer tamanho
#c) todos os componentes de um data frame têm que ser do mesmo tipo
#d) todos os componentes de um data frame devem possuir o mesmo tamanho
#e) um estudo clínico, em geral, pode gerar um conjunto de dados, onde cada variável é uma coluna de um data frame e cada linha são os valores de cada variável para a unidade de observação correspondente
# R. d), e)

#13.
#R. a) b) c) d)
d = data.frame(id=c("P1", "P2", "P3", "P4", "P5"), 
               sexo = c("feminino", "feminino", "masculino", "masculino","feminino"),
               pad = c(80, 85, 100, 95, 88),
               pas = c(130, 140, 150, 145, 125))
d[3,] = c(NA, NA, NA, NA)
d[[4]][1:5]
d$pas[1:5]
d[1:5, 4]
#14
#R. a)

#Lista de exercicios curso:
# Exercício 1 - Crie um vetor com 12 números inteiros
a = c(1:12)
a

# Exercício 2 - Crie uma matriz com 4 linhas e 4 colunas preenchida com números inteiros
x = matrix(1:16 , ncol = 4, nrow = 4)
x

lista = list(a, x)

# Exercício 4 - Usando a função read.table() leia o arquivo do link abaixo para uma dataframe
# http://data.princeton.edu/wws509/datasets/effort.dat
d = data.frame(read.table('http://data.princeton.edu/wws509/datasets/effort.dat'))

# Exercício 5 - Transforme o dataframe anterior, em um dataframe nomeado com os seguintes
# labels:
# c("config", "esfc", "chang")
names(d) = c("config", "esfc", "chang")

# Exercicio 6 - Imprima na tela o dataframe iris, verifique quantas dimensoes existem no dataframe iris, imprima um resumo do dataset
iris
class(iris)
dim(iris)
summary(iris)
str(iris)

# Exercicio 7 - Crie um plot simples usando as duas primeiras colunas do dataframe iris
plot(iris$Sepal.Length, iris$Sepal.Width)

# Exercício 8 - Usando s função subset, crie um novo dataframe com o conjunto de dados do
# dataframe iris em que Sepal.Length > 7
# Dica: consulte o help para aprender como usar a função subset()

help(subset)
a = subset(iris, Sepal.Length>7)
a

# Exercícios 9 - Crie um dataframe que seja cópia do dataframe iris e usando a função slice(),
# divida o dataframe em um subset de 15 linhas
# Dica 1: você vai ter que instalar e carregar o pacote dplyr
# Dica 2: consulte o help para aprender como usar a função slice()
a = iris
install.packages("dplyr")
library("dplyr")
?slice
slice(a, n=1:15)

# Exercícios 10 - Use a função filter no seu novo dataframe criado no item anterior e retorne
# apenas valores em que Sepal.Length > 6
# Dica: use o RSiteSearch() para aprender como usar a função filter
RSiteSearch("filter")
d = filter(a, a$Sepal.Length >6)
e = filter(a, Sepal.Length >6)








