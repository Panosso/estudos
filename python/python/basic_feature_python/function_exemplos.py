#funcao sem parametro
def primeira_funcao():
    """
    O que for escrito nessa parte entre essas aspas é o Docstring, sempre que alguem for ver algo da funcao, o que foi escrito aqui será dado como dica. Então se for digitado 'print(primeira_funcao.__doc__)' ou 'help(primeira_funcao)'
    """

    print("Olá Mundo!!")
    return "Hello World!!"

#funcao com um parametro
def primo(num):
    """
    Método para verificar se um numero é primo
    """

    lista_num = []

    for x in range(2, num):
        if num % x == 0:
            return "Número nao primo"
            print("Nao serei executado.")

    else:
        return "É primo"
        print("Nem eu")

#funcao com mais de um parametros
def calculadora(num1, num2, operacao):

    def somar(num1, num2):
        return num1 + num2

    if operacao == 'soma':
        variavel = somar(2, 3)

    return variavel

#Aqui será impresso o print dentro da função, pois as linhas de execuções passam pelo print
funcao_sem_retorno = primeira_funcao()

#Irá imprimir None, pq o return da função é None
print(funcao_sem_retorno)

lista = [numero for numero in range(0,10)]

x = calculadora(1,2,'soma')

y = primo(17)

print(x)
print(y)

#Funcoes com retorno de mais de um valor
def retorna_valores():
    return 2,3,4,5,6

def retorna_valores2():
    return 2,3,4,5,6

num1, num2, num3, num4, num5 = retorna_valores()

num6 = retorna_valores2()

print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)

def color_change(color: int) -> int:
    print(f'Voce mudou para a cor {color}')

    return color

def soma(num1, num2=1)
    return num1 + num2
    
#Retornara 2 + 4
print(soma(num2=4, num1=2))

def multiplicar(num1, num2=1)
    return num1*num2
    
    
#O valor da segunda variavel ja está definido, sendo assim nao é necessário inforala

#Retornara 3 * 1
print(multiplicar(3))

#Retornara 3 * 4
print(multiplicar(3, 4))

def soma(num1, num2):
    return num1 + num2
    
def sub(num1, num2):
    return num1 - num2
    
#Por padrao ele vai assumir que a função adicionada é a soma, mas pode ser alterada desde que atenda todos os
# requisitos da função.
def mat(num1, num2, fun=soma):
    return fun(num1, num2)
    

print(mat(2,3))
print(mat(2,3, sub))


