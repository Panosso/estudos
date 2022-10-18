s = 'hello worlds'

#Transforma a primeira letra apenas em maiusculo.
print(s.capitalize())

#Transforma a string em maiusculo.
print(s.upper())

#Transforma a string em minusculo.
print(s.lower())

#Conta quantas vezes aparece o elemento.
print(s.count('o'))

#Centraliza a string e preenche com o elemento até o tamanho do primeiro parametro
print(s.center(50, 'z'))

s1 = 'hello'

#Verifica se todos os caracteres sao alfanumericos
print(s1.isalnum())

#Verifica se está tudo em upper
print(s1.isupper())

#Verifica se termina com determinado caractere
print(s1.endswith('o'))

#quebra a string e retorna uma lista, por padrao ele quebra no ' ', mas pode ser substituido
print(s.split())

#Particiona em determinado caractere, formando uma parte antes, uma parte no separador e uma parte final
print(s.partition('e'))

string1 = "Teste de join"
lista = ['A', 'B', 'C']

#T-e-s-t-e- -d-e- -j-o-i-n
print('-'.join(string1))

#A-B-C
print('-'.join(lista))
