#Matriz

#Cria uma matriz com os valores de 1 a 6
# com 2 linhas e 3 colunas
# byrow, diz como a matriz será montada iniciando os valores
# linha a linha(byrow = 1) ou coluna a coluna(byrow=0)
m = matrix(data=1:6, nrow=2, ncol=3, byrow = 0, 
           dimnames = list(c('linha1', 'linha2'), 
                           c('coluna1', 'coluna2', 'coluna3')))

m

#Retorna a dimensão da matriz
dim(m)


#Preenchendo com NA
n = matrix(nrow = 3, ncol = 10)
n

#Criando uma matriz com todos os valores iguais, se for passado um vetor
# ele precisa ter o tamanho necessário para completar o que foi definido no
# byrow e então ele será replicado até preencher a matrix
p = matrix(data = 2, nrow= 100, ncol=100)
p

q = matrix(data = c(1:5), nrow = 5, ncol = 4, byrow = T)
q

#Montando uma matriz com 
#cbind Monta uma matriz empilhando os elementos linha a linha
#rbind Monta uma matriz empilhando os elementos coluna a coluna
x <- 1:4
y <- 10:13

rbind(x, y)
cbind(x, y)

#Acessando os dados de uma matriz através da
# matrix[linha, coluna]
z = 1:16
A = matrix(data = z, nrow = 4, ncol = 4, byrow=T)
A

#retorna a segunda linha com todos os valores das colunas
A[2,]

#retorna a segunda linha os valores das colunas 1 a 3
A[2, c(1:3)]

#retorna uma submatriz contendo:
# linhas 1 e 4
# colunas 2 e 3
A[c(1,4), c(2,3)]

#indices negativos excluem o indice indicado
# retorna a matriz inteira exceto a terceira linha
A[-3,]

# retorna a matriz inteira exceto a segunda coluna
A[,-2]

