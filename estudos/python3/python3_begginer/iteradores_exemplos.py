#Iterable
nome = "Pedro"
numeros = [1,2,3,4,5,6]

#Iterator
it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

#Quando terminar de iterar, ocorrerá um erro.
#print(next(it1))

print('\n\n\n\n')

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

class Contador:
    
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration
        

con = Contador(1, 61)

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
