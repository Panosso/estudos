from random import choice

#HOF
def somar(a, b):
    return a + b
    
def diminuir(a, b):
    return a * b

def dividir(a, b):
    return a / b
    
def multiplicar(a, b):
    return a * b    

def calcular(num1, num2, funcao):
    return funcao(num1, num2)
    
print(calcular(4, 2, somar))
print(calcular(4, 2, diminuir))
print(calcular(4, 2, multiplicar))
print(calcular(4, 2, dividir))


#Inner Functions
def hello(pessoa):
    
    def humor():
        return choice(('E ai ', 'Salve macaco ', 'Mano só sai da minha frente '))


    return humor() + pessoa


print(hello('Machado'))

def faz_me_rir1(pessoa):
    def dando_risada():
        risada = choice(('hudsahudsa', 'hihihihihih', 'risada do mal'))
        return f'{risada} {pessoa}'
    return dando_risada
    
rindo = faz_me_rir1('Pedro')
print(rindo())


#Retornando funções de outras funções
def faz_me_rir2():
    def rir():
        return choice(('hudsahudsa', 'hihihihihih', 'risada do mal'))
    return rir
    
    
rindo = faz_me_rir2()

print(rindo())

#Decorators como funções, sintax nao recomendada
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer')
        funcao()
        print('Bom dia')
        
    return sendo
    
def saudacao():
    print('Seja bem-vindo')

teste = seja_educado(saudacao)

teste()

#Decoradores com Syntex Certa

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo

#Aplicando Decorador    
@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

apresentando()

#Funcao decoradora: Que será executada antes da funcao
def tudo_maiusculo(funcao):

    def maiusculo(*args, **kw):
        print('Estou no maiusculo')
        print(kw)
        print(args)
        return funcao(*args, **kw).upper()

    return maiusculo

@tudo_maiusculo
def olamundo():
    return 'Olá, mundo!!! <3'

@tudo_maiusculo
def nome(name, idade):
    return f"Your name is: {name} and you have {idade} years"

hello = olamundo()
super_hello = nome('Pedro', 28)
print(hello)

#Decorator pattern, o kwargs nesse exemplo é passado como um opcional, portanto ele nao é obrigatório.
def gritar(funcao):
    def aumentar(*args, **kwargs):
        print('Args')
        for i in args:
            print(i)
            
        print('\n\n')
        print('Kwargs')
        for k, v in kwargs:
            print(k)
            print(v)
        print('\n\n')
        return funcao(*args, **kwargs).upper()
        print('\n\n')
    return aumentar
    
@gritar
def saudacao(nome):
    return f'Olá eu sou o {nome}'
    
@gritar
def ordenar(principal, acompanhamento):
    return f'Olká, eu gostaria de {principal}, acompnhado de {acompanhamento}, pls'


print(saudacao('Pedro'))

print(ordenar('Bife', 'Batatinha'))

#Decorators com argumentos
def verifica_primeiro_arg(valor):
    #funcao = comidas
    #args = ('pizza', 'churrasco', 'chimarrao')
    #valor = pizza
    #**kwargs = {}
    def interno(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                raise Exception(f"Primeiro argumento inválido, ele precisa ser igual a '{valor}'")
            #Retorno da funcao:
            #PRATÃO SHOW: ('PIZZA', 'CHURRASCO', 'CHIMARRAO')
            return(funcao(*args, **kwargs).upper())
        return outra
    return interno
    
@verifica_primeiro_arg('pizza')
def comida(*args):
    return f'Pratão Show: {args}'

print(comida('pizza', 'churrasco', 'chimarrao'))

#Erro pq o primeiro elemento nao é o passado, nesse exemplo
#print(comida('batata', 'pizza', 'churrasco', 'chimarrao'))


#outro exemplo onde

#funcao = soma
#args = (10, 21)
#valor = 10
#**kwargs = {}

@verifica_primeiro_arg(10)
def soma(num1, num2):
    return num1 + num2

print(soma(10, 21))

#Erro pq o primeiro elemento nao é o passado, nesse exemplo
#print(soma(1, 21))

#Decorador implementado em classe e quando for implementado em classe ele precisa ter o método __call__ implementado
class uppercase(object):

    def __init__(self, funcao):
        self.funcao = funcao

    def __call__(self, *args):
        print(f'Args: {args}')
        self.funcao(args[0].upper(), args[1])

@uppercase
def nome(name, idade):
    print(f"Seu nome é: {name} e tem {idade} anos")


nome('Pedro', 22)
