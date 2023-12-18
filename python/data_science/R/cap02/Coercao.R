#Coerção
#logical --> integer --> numeric --> complex --> character
y = c(123, "a", 2+1i)
class(y)

y= c(123, 2L, 2+1i)
class(y)

#Objetos podem ser convertidos utilizando o as.<nome_objeto>
x <- c(0,1,3,4,5,-4)
class(x)

#0 é convertido em FALSE e tudo que for diferente é TRUE
as.logical(x)

#Convertento string em numeric, temos o NA no lugar de letras
# pois os numeros mesmo que em string são convertidos, porém eles nao podem
# estar acompanhados de letras.
y = c('a','2L',1,3,4)
as.numeric(y)

#Como o tipo da class de x é string, ele não conseguira
# converter string para logico, mesmo que tenha os numeros
# 1,3,4 o tipo da classe de x é string, portanto o resultado será
# NA NA NA NA NA
as.logical(y)

#Transformando uma lista em factor
sexo = c(1,2,2,1,1,2,3,2,2,1,2)
sexo.fac = as.factor(sexo)
levels(sexo.fac) = c('feminino', 'masculino', 'outros')
sexo.fac
