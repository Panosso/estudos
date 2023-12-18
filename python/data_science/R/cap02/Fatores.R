#Fatores
a = factor(c('branco', 'branco', 'pardo', 'negro'))

#Retorna os niveis do factor, ou seja, os valores unicos que ele
# possui
levels(a)

#Alterando a ordem de relevancia dos fatores
b = factor(c('nenhuma', 'leve', 'media', 'forte'))
b

levels(b) = c('nenhuma', 'leve', 'media', 'forte')
b

grad <- c("graduado", "mestre", "doutor", "phd", "graduado", "mestre", "doutor", "phd", "graduado")

#Cria um fator ordenado, atraves do atributo order e já define os níveis do fator.
fac_grad <- factor(grad, order = T, levels = c( "phd", "doutor",  "mestre", "graduado"))

levels(fac_grad)

fac_grad

#Soma os valores de acordo com os levels definidos, do maior para o menor level.
summary(fac_grad)

#Soma no vetor não possui classificação
summary(grad)


vec2 = c("M", "F", "F", "M", "F", "F", "M", "F", "F", "M", "F", "F", "M", "F", "F", "M", "F", "F")
fact_vec2 <- factor(vec2)
fact_vec2
#Por padrao os fatores são feitos em ordem alfabética, portanto os leveis estão ("F", "M")
# ao definir os levels do fact_vec2 como c("Femea", "Macho")
# o R vai troca o level 1(F) por Femea e o level 2(M) por Macho
levels(fact_vec2) <- c("Femea", "Macho")
fact_vec2
summary(fact_vec2)
summary(vec2)


data = c(1,2,3,2,2,3,1,1,2,3,2,3,2,3,3,1,1,2,2,1,2,1)
fdata = factor(data)
fdata

#Cria o fator e atraves dos leveis altera os labels dos níveis e conseguentemente
# dos dados para o que foi definido em labels.
rdata = factor(data, labels = c("Level I", "Level II", "Level III"))
rdata

