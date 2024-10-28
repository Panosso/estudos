lista = [1,2,3,4,5,6,7]

for i in lista:
    if i % 2 == 0:
        print("O número %i é par" %(i))

    else:
        print("O número %i é impar" %(i))

somatorio = 0

for num in lista:
    somatorio += num

print(somatorio)

lista_tupla = [(1,2), (3,4), (5,6)]

for (t1, t2) in lista_tupla:
    print("O valor de t1 é %i e o valor de t2 é %i" %(t1, t2))

d = {'k1': 1, 'k2':2, 'k3':3}

for i in d.items():
    print(i)

for (i, v) in d.items():
    print(i)
    print(v)

for _, valor in enumerate(lista):
    print(valor)
    
x = 1
			
while x <= 10:
    print('O valor de X é %i' %(x))
    x += 1

    #if x == 8:
    #    break

    if x % 2 == 0:
        print('O numero %i é par' %(x))

    else:
        continue

else:
    print('Sai do while')
    
print(list(range(0,10,2))) ==> [0, 2, 4, 6, 8]
