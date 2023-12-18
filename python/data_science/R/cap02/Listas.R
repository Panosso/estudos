#Listas
x <- list(5L, "Teste", c(1,5,2), seq(5:10), 3+1i, 2)

#Acessando o dado da lista
x[3]

#Acessando o conteudo do dado da lista
x[[3]]

#lista vazia com comprimento determinado
y = vector("list", length = 3)
y[[1]]

#Acessando os elementos 3 e 1 da lista
x[c(3,1)]

#Acessando os elemntos de 1 até 3 da lista
x[c(1:3)]

#Acessa o 3º elemento da lista e seleciona o 2 registro desse elemento
# equivalente a digitar x[[3]][[2]]
x[[c(3,2)]]
b=list(c(linha=seq(1:2)), c(coluna=seq(1:3)))
b
#Cria um dicionário com chave e valor
# No caso da seq, ele vai criar uma coluna chamada teste + numero da iteração
# portanto teremos teste1, teste2, teste3
a = c(g=123, h=46, teste=seq(13,18,2), 'teste')
a
#Acessa esse dicionario pelo nome da chave
a["teste1"]

#Acessando pelo index
a[1]

#Pegando as keys ou nomes de um dicionario
names(a)

#O elemento da lista NOMINADA tambem pode ser acessado atraves do '$'
y = list(g=123, h=46, teste=seq(13,18,2), 'teste')

#Acessando o elemento que tem a chave g
y
