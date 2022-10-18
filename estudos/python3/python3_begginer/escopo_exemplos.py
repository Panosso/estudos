#Local

f = lambda x: x**2

print(f(2))

x = 50

def func(x):
    """
    O valor de X será alterado apenas dentro da funcao, ou seja ele é uma variavel local a essa funcao, portanto o x na linha 7 nao é o mesmo x da funcao
    """

    print("X is : ", x)
    x = 2
    print("Changed to ", x)

func(x)
print('X still is ', x)

#Enclosing Function

def greet():
    name = 'Sammy'

    """
    Segundo lugar que o python vai procurar o valor da variavel
    """

    def hello():
        """
        Primeiro lugar que o python vai procurar o valor da variavel
        :return:
        """
        print('Hello ' + name)

    hello()

greet()


#Variaveis Global

y = 50

def func():
    """
    Com o global y o valor da variavel será global ou seja, caso ela seja alterada dentro da funcao, será alterada fora da funcao tambem e ela estara disponível para o todo o código
    """
    global y

    print("Y is : ", y)
    y = 2
    print("Changed to ", y)

func()
print('Y is now ', y)

#Existe a possibilidade de acessar a variavel global com o mesmo nome dentro de uma função, para isso é necessário utilizar o 'nonlocal':

def fora():
    contador = 0
    
    #Função que só pode ser acessada dentro da função fora.
    def dentro():
        #Ele está acessando a variavel que está 3 linhas atras, ou seja, fora da função
        nonlocal contador
        
        contador += 1
        return contador
    
    return dentro()

print(fora())
