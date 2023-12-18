#Data Frame

#Criando um dataframe
d = data.frame(id=c("P1", "P2", "P3", "P4", "P5"), 
               sexo = c("feminino", "feminino", "masculino", "masculino","feminino"),
               pad = c(80, 85, 100, 95, 88),
               pas = c(130, 140, 150, 145, 125))

#retorna o nome das colunas do dataframe.
names(d)

#retorna o nome das linhas do dataframe.
row.names(d)

#Define um index para as linhas do dataframe
row.names(d) = c("jaque", "carol", "Pedro", "Yago", 'camila')

#Acessando os elementos de um dataframe
d$sexo

#Acessa todas as linhas porém traz apenas as colunas 2 e 4
d[, c(2,4)]

#Ela tambem pode ser acessada atraves do nome da coluna
d[, c('sexo', "pas")]

#Acessa todas as colunas porém as linha 2 e 4
d[c(2,4), ]

#Acessa todas as colunas porém as linha 2 e 4 não serão retornadas
d[-c(2,4), ]

#Acessa todas as colunas porém as linha com os indices 'carol' e 'Yago'
d[c("carol", "Yago"), ]

#Caso seja informado um valor que não existe no dataframe,
#o R criará apenas para o return uma linha com NA
d[c(2,6), ]

#Fazendo filtro no dataframe

#Traz todos os resultados onde a coluna sexo é diferente de masculino
d[d['sexo'] != "masculino",]
d[d$sexo != "masculino",]

#Cria um novo dataframe sem os ids
a <- d[, -1]
a
