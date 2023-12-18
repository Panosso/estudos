#Condicionais if-else

x = 100

#Controle de fluxo if-else
if(x<30){
  print("X é menor que 30")
  } else if(x<100){
  print("X é maior que 30")
  } else {print("X é numero")}

ifelse (x<100, "É menor que 100", "É maior que 100")

ifelse(x<=100, ifelse(x == 100, 'X é 100',  "É menor que 100"), "É maior que 100")

#Controle de fluxo for
for(i in 1:12){
  print("O valor de i é ")
  print(i)
}

for(i in 1:100){
  if(i%%2 == 0){
    next
  }else{print(i)}
}

func1 <- function(x,y){
  z = x+y
  ifelse(z < 10, z*z, z)
}
func1(2, 9)

#Controle de fluxo Rep
#Vai realizar a função rnorm, 5 vezes
rep(rnorm(2), 5)

#Controle de fluxo Repeat
x=1
repeat {
  x = x+3
  if (x > 99)
  {
    break
  }
  print(x)
}


#Controle de fluxo While
x = 1
while(x<10){
  print(x)
  x = x+1
}




