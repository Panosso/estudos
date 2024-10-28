def somador(*args):
    return sum(args)

def verificando_verdade(*args):
    if 'Pedro Panosso' in args or 'Lindao' in args:
        print("Essa pessoa é show de bola")
        return True
    else:
        return False	
    
#Passando parametro por parametro
print(somador(1,2,3,4,5))

#Passando para a função avisando que ela precisa separa ou DESENPACOTAR os dados.
numeros = [1,2,3,4,5,6,7,8,9]
#print(somador(numeros)) -> Erro
print(somador(*numeros))

print(verificando_verdade(1, True, "Pedro Panosso", "Batata"))
print(verificando_verdade(1, True, "Trem", "Lindao"))
print(verificando_verdade(1, True, "Trem", "abacate"))

def cores_favoritas(valor, media, **kwargs):
    print(valor)
    print(media)
    print(kwargs)
    for p, c in kwargs.items():
        print(f'A cor favorita de {p.title()} é {c.upper()}')


cores_favoritas(123, 10, marco='verde', pedro='azul', jaque='azul claro')

print("Não informando os valores para kwargs")
cores_favoritas(123, 10)

#Desempacotando o kwargs
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Pedro', 'sobrenome': 'Panosso'}

print(mostra_nomes(**nomes))
