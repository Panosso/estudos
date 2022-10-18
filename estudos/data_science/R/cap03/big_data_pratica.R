getwd()

install.packages('readr')
install.packages("data.table")
library(readr)
library(dplyr)
library(ggplot2)
library(scales)
library(data.table)

#usuário   sistema decorrido 
#47.150     1.294    51.581 s
system.time(df_teste1 <- read.csv2("cursos/01. Big Data Analytics com R e Microsoft Azure Machine Learning/Datasets/Parte 2/TemperaturasGlobais.csv"))

#usuário   sistema decorrido 
#18.319     0.755    21.188 s
system.time(df_teste2 <- read.table("cursos/01. Big Data Analytics com R e Microsoft Azure Machine Learning/Datasets/Parte 2/TemperaturasGlobais.csv"))

rm(df_teste1)
rm(df_teste2)


#usuário   sistema decorrido 
#8.113     0.932    17.281
#Função escrita e otimizada para carregamento de um grande volume de dados
?fread
system.time(df_teste3 <- fread("cursos/01. Big Data Analytics com R e Microsoft Azure Machine Learning/Datasets/Parte 2/TemperaturasGlobais.csv"))
names(df_teste3)

#Cria um subset apenas dos registros que possuem a coluna Country igual a Brazil
cidadeBrasil <- subset(df_teste3, Country == 'Brazil')

#Omite os valores na
cidadeBrasil <- na.omit(cidadeBrasil)

#Primeiros registros do dataset
head(cidadeBrasil)

#Número de linhas
nrow(df_teste3)
nrow(cidadeBrasil)

#Dimensão linha x coluna do dataframe
dim(cidadeBrasil)

#Convertendo as Datas
cidadeBrasil$dt <- as.POSIXct(cidadeBrasil$dt, format="%Y-%m-%d")
cidadeBrasil$Month <- month(cidadeBrasil$dt)
cidadeBrasil$Year <- year(cidadeBrasil$dt)
names(cidadeBrasil)

#Palmas
plm <- subset(cidadeBrasil, City == "Palmas")
plm <- subset(plm, Year %in% c(1796, 1846, 1896, 1946, 1996, 2012))
plm

#Curitiba
crt <- subset(cidadeBrasil, City == "Curitiba")
crt <- subset(crt, Year %in% c(1796, 1846, 1896, 1946, 1996, 2012))
crt

#Recife
rcf <- subset(cidadeBrasil, City == "Recife")
rcf <- subset(rcf, Year %in% c(1796, 1846, 1896, 1946, 1996, 2012))
rcf

#Rib Preto
rp <- subset(cidadeBrasil, City == "Ribeirão Prêto")
rp <- subset(rp, Year %in% c(1796, 1846, 1896, 1946, 1996, 2012))
rp

#Criando os plots
p_plm <- ggplot(plm, aes(x = (Month), y= AverageTemperature, color = as.factor(Year)))+
  geom_smooth(se = FALSE, fill=NA, size = 2) + 
  theme_light(base_size = 20) +
  xlab("Mês") + 
  ylab("Temperatura média") +
  scale_color_discrete("") +
  ggtitle("Temperatura Média ao longo dos anos em Palmas") + 
  theme(plot.title = element_text(size = 18))

plot(p_plm)


p_rp <- ggplot(rp, aes(x = (Month), y= AverageTemperature, color = as.factor(Year)))+
  geom_smooth(se = FALSE, fill=NA, size = 2) + 
  theme_light(base_size = 20) +
  xlab("Mês") + 
  ylab("Temperatura média") +
  scale_color_discrete("") +
  ggtitle("Temperatura Média ao longo dos anos em Rib Preto") + 
  theme(plot.title = element_text(size = 18))
plot(p_rp)
