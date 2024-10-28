print("\n\n")
print("Geradores")

#Funcao gerador.
def gen_cubes(n):
    for num in range(n):
        yield num ** 3

#[0,1,8]
for x in gen_cubes(10):
    print(x)

#Fibonacci
print("\n\n")
print("Fibonacci")

#Funcao gerador Fibonacci
def genfib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in genfib(10):
    print(num)


#Iteradores
print("\n\n")
print("Iteradores")

s = 'Hello'

s_iter = iter(s)
for i in s_iter:
    print(i)

continuar = 's'
while continuar != 'n':

    print(next(s_iter))
    continuar = input("Deseja continuar?")

print("\n\n")
print("Geradores comprehesions")

pares = (i for i in range(0, 100) if i%2 == 0)

#printa o tipo da variavel pares
print(pares)
#printa os numeros pares de 0 a 100
print(list(pares))


#Tema de casa - Geradores e iteradores.
#Problema 1 - Quadrado dos números
print("Problema 1")
def gerador_quadrado(n):
    for num in range(0, n):
        #return num**2
        yield num**2

lista = (i**2 for i in range(0, 10))

print(list(lista))

for x in gerador_quadrado(10):
    print(x)

print("\n\n")
#Problema 2 - Gerar um numero aleatorio.

print("Problema 2")
import random

def rand_num(low, high, n):
    for i in range(0, n):
        yield random.randint(low, high)

for x in rand_num(0, 10, 12):
    print(x)

print("\n\n")

#Problema 3 - converter string usando iter()
print("Problema 3")
s=iter("hello")

for i in s:
    print(i)

print("\n\n")

#Problema 4 - Explicacao do caso de uso

#Um bom exemplo de gerador é quando eu preciso que a funcao me retorne uma lista, e ao inves de ocupar a memória
# com uma variavel do tipo lista eu posso usar o yield e ir imprimindo ou usando o resultado que já será apagado

#Problema 5 - Crédito extra

#Ele utiliza o gerador comprehension para gerar um gerador que adiciona na variavel gencomp apenas os itens da lista
# que sao maiores que 3
