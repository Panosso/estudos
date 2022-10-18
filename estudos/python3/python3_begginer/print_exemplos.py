frase = "I'm a teacher"

palavra = "string"

numero = 7

flutuante = 13.144

# %s o python converte a string usando o metodo str()
# %r o python converte a string usando o metodo repr()

print ("Temos uma frase %s" %(palavra))
print ("Temos um número %s" %(numero))
print ("Temos um ponto flutuante %1.2f" %(flutuante))
print ("Temos uma %s, e ela contem a frase %r" %(palavra, frase))
print ("Temos uma {a}, que tem {b} de tamanho, {c}".format(a=palavra, b=len(frase), c=repr(frase)))

#Verifica se tem a string em Python, retornando 0 se encontrar e -1 se não encontrar.

txt = "Killer Instinct melhor game de luta"

print(txt.find("Killer"))

#outro metodo que tbm verifica

idade = 22
nome = "Pedro Panosso Machado"
print(f'{idade} {nome}')
