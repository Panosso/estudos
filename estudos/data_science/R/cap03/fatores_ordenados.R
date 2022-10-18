# Fatores Não-Ordenados
set1 <- c("AA", "B", "BA", "CC", "CA", "AA", "BA", "CC", "CC")
set1

f.set1 = factor(set1)
f.set1
class(f.set1)
is.ordered(f.set1)
levels(f.set1)


o.set1 = factor(set1, levels = levels(f.set1), ordered = T)
o.set1

#Fatores e dataframes
df <- read.csv2("/home/machado/cursos/01. Big Data Analytics com R e Microsoft Azure Machine Learning/Datasets/Parte 2/etnias.csv", sep = ',')
df

#Traz um resumo do dataframe
str(df)

df$Sexo <- factor(df$Sexo, levels = c("Femea", "Macho"))
df
levels(df$Sexo)
