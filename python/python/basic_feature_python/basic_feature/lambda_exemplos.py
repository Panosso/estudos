x = lambda parametro1, parametro2: retorno_funcao

print(x(2))

par = lambda x: x % 2 == 0

print(par(3))

palavra = lambda s: s[0]

print(palavra("macaco"))

inverter = lambda s: s[::-1]

print(inverter("inverter a expressao"))

#expressao lambda com 2 variaveis ou mais:

z = lambda x,y: x+y

print(z(10,9)) #19

print("\n\n\n\n\n")

funcao = lambda x: 3*x+1

teste = lambda x,y: x+y

print(funcao(3))
print(teste(2,3))

autores = ['Angeline Jolie', 'Pedro Panosso', 'Jaqueta Furquim', 'yago falcao callegaris', 'Augusto potato', 'kim katguiri', 'Egidio panosso']

autores.sort(key=lambda sobrenomes: sobrenomes.split(' ')[-1])

print(autores)

def geradore_funcao_quadrado(a,b,c):
    return lambda x: a*x**2 + b*x + c
    
teste = geradore_funcao_quadrado(2,5,7)

print(teste(3))

#Equivalente a seguinte expressao: 2*x**2 + 5*x + 7
#E então será invocada a expressao lambda, ficando: 2*3**2 + 5*3 + 7
#Resultando em: 40
#Isso pode ser escrito da seguinte forma tbm: geradore_funcao_quadrado(2,5,7)(3)
#OUtros exemplos

print(teste(5))
print(teste(2))
print(geradore_funcao_quadrado(2,5,7)(3))
