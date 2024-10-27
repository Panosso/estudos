#Vetor Possui 1 dimensão
vetor1 = c(1:10)
vetor1
length(vetor1)
mode(vetor1)
class(vetor1)
typeof(vetor1)
is.vector(vetor1)

#Outra forma de criar vetor
vector_func <- vector('character', length=15)
vector_func

#Vetor de nomes
vetor_caractere = c('Pedro', 'Jaque', 'Yago')
vetor_caractere

#Vetor floats
vetor_float = c(1.5, 2.6, 3.4)
vetor_float

#Vetor Complexo
vetor_complexo = c(4+5i, 3+10i)
vetor_complexo

#Vetor Logico, lembrando que 1 é true e 0 é false
vetor_logico = c(TRUE, TRUE, 1, FALSE)
vetor_logico

#Vetor de inteiros
vetor_int = c(1,2,3,4,5)
vetor_int

#Indexação de vetores
a <- c(10:15)
a
#Em R o array começa em 1
a[1]

#Erro pois não tem o index 7
#a[7]

#Combinando Vetores
v1 = c(1:5)
v2 = c(2:6)
c(v1, v2)

#Cria um vetor decrescente
y = c(50:40)
y

#Retorna os valores exceto o 3º AO 8º elemento
y[-3:-8]

#Retorna os valores exceto o 3º E 8º elemento
y[c(-3, -8)]

#Usando filtro, nesse exemplo ele procura o elemento 49 no vetor
y[y==45]

#Seleciona os elementos menores que 45
y[y<45]

#Seleciona os elementos não menores que 46
y[!(y<46)]

#Seleciona elementos menores que 49 e maiores que 42
y[(y<49) & (y>42)]

#Seleciona elementos maiores que 49 ou menores que 42
y[(y>49) | (y<42)]

#O R funciona para valores strings, visto que ele
# adimite a ordem alfabética como a correta

x = c("Antônio", "Joana", "Carla", 'Zilma')

#Seleciona valores que comecam com letras após do H
x[x > "H"]

#Atribui ao u um vetor booleano onde todos os valores maiores
# que 46 são FALSE e valores iguais ou menores que 46 são TRUE
u <- y<=46
u

#É possível atribuir um valor para um index
y[1] <- 10
y

#Vetores utilizando a função seq, é uma função que recebe 3 argumentos
# seq(valor_inicial, valor_final, passo)
# O passo possui um valor default 1 para crescente e -1 para decrescente

#Vetor crescente
vetor_seq_cre = seq(1, 10, 2)
vetor_seq_cre

#Vetor decrescente
vetor_seq_decre = seq(10, 1, -3)
vetor_seq_decre


#Vetores utilizando a função rep, ela recebe 2 argumentos
# onde o primeiro é a função e o segundo é o numero de vezes
# que ela vai se repetir.
#É possivel passar para o rep um outro vetor
vetor_rep = rep(x, 3)
vetor_rep

#Operação com vetores, os 2 vetores precisar ser
# do mesmo tamanho
f = seq(10, 15)

#Vai pegar cada elemento e multiplicar por 5
f*5

#Soma os elementos de f com x, elemento por elemento
f+a

#Subtrai os elementos de f com x, elemento por elemento
f-a

#Multipla os vetores, elemento por elemento
f * a

#Vetores Nomeados, equivalente ao dicionário do python
v = c("Pedro", "Panosso", "29", "Masculino")
v
#Define o 'nome' das colunas do vetor
names(v) = c("Nome", "Sobrenome", "Idade", "Sexo")
v
v["Idade"]




