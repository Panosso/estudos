#syntax: <all or any>(lista)

lista_true = [True,True,True,True]
lista_false = [False, False, False, False,]

lista_misturada = [True,True,True,False]

print(all(lista_true))
#True

print(all(lista_false))
#False

print(all(lista_misturada))
#False

print(any(lista_true))
#True

print(any(lista_false))
#False

print(any(lista_misturada))
#True
