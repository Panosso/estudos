#Se executado esse arquivo ele simplesmente vai entrar na função soma_lista
# e devolver o resultado.
from panosso.matematica import soma_lista as sl

print(sl([1,2,3,4,5,6]))
#fim arquivo

#Se for executado daqui, esse arquivo vai ser o principal, executando o 'if' que está logo abaixo.
from functools import reduce
pi = 3.14

def soma(a, b):
    return a+b

def soma_lista(*args):
    print('Somando')
    return reduce(lambda x,y: x+y, *args)

if __name__ == '__main__':
    print('Vou somar as bagaça aqui')
    lista = [1,2,3,4,5,6,7,8,9]
    print(soma_lista(lista))
else:
    # __name__ = panosso.matematica
    print(f'Fui importado e nada me importa. {__name__}')
#fim arquivo
