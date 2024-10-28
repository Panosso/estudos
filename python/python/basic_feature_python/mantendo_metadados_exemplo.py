from functools import wraps

#def ver_log(funcao):
#    def logar(*args, **kwargs):
#        """Eu sou um funcao (logar) dento de outra"""
#        print(funcao.__name__)
#        print(funcao.__doc__)
#        return funcao(*args, **kwargs)
#    return logar
#
#@ver_log
#def soma(a, b):
#    """Soma 2 numeros"""
#    return print(a+b)
#    
##Vai retornar o doc e o name da função soma
#soma(10, 12)
#
##Vai retornar o doc e o name da função logar
##Gerando assim um problema, pois caso alguem queira consultar a documentação,
## será consultada a documentação errada
#print(soma.__name__)
#print(soma.__doc__)

#Para corrigir esse problema, utilizamos o wraps
def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou um funcao (logar) dento de outra"""
        print(funcao.__name__)
        print(funcao.__doc__)
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma 2 numeros"""
    return print(a+b)

soma(10, 12)

print(soma.__name__)
print(soma.__doc__)
