def soma(a, b):
    """Soma os numeros a e b
    
        >>> soma(1, 2)
        3
        
        >>> soma(10, 4)
        100
    """
    return a+b


print(soma(5, 7))


#Resultado do console ao ser executado com o comando acima, com um exemplo de sucesso e falha:

#Trying:
#    soma(1, 2)
#Expecting:
#    3
#ok
#Trying:
#    soma(10, 4)
#Expecting:
#    100
#**********************************************************************
#File "/home/machado/cursos/Python3/Curso de Programação em Python - do básico ao avançado/00. projetos/teste_geral.py", line 7, in teste_geral.soma
#Failed example:
#    soma(10, 4)
#Expected:
#    100
#Got:
#    14
#1 items had no tests:
#    teste_geral
#**********************************************************************
#1 items had failures:
#   1 of   2 in teste_geral.soma
#2 tests in 2 items.
#1 passed and 1 failed.
#***Test Failed*** 1 failures.
