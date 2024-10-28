meu_arquivo = open('arquivo-panosso.txt')
# <_io.TextIOWrapper name='teste.txt' mode='r' encoding='UTF-8'>
# Nome do arquivo e a permissao, nesse exemplo do de leitura 'r' e o encode que o arquivo foi escrito


#Printa apenas o que está salvo no endereço de memória
print(meu_arquivo)

#Le o conteudo do arquivo
print(meu_arquivo.read())

#Retorna onde o cursor do python vai iniciar
meu_arquivo.seek(0)

#Le o conteudo de uma linha
print(meu_arquivo.readline())

#A variavel que está depois do 'in' é chamado de iteravel
for line in meu_arquivo:
    print(line)

#Exemplo geek
meu_arquivo = open('arquivo-panosso.txt')

print(meu_arquivo.read())

#Nao vai aparecer nada pq o curso já está no fim do arquivo
print(meu_arquivo.read())

#Colocando o cursor no index 0 do arquivo
meu_arquivo.seek(0)

print(meu_arquivo.read())

#Colocando na posição 15
meu_arquivo.seek(15)

#Será lido até o caractere 20
print(meu_arquivo.read(20))

meu_arquivo.seek(0)

#Le uma linha do arquivo
print(meu_arquivo.readline())

#Retorna uma lista com todas as linhas do arquivo
print(meu_arquivo.readlines())

#Verifica se um arquivo está aberto ou fechado
print(meu_arquivo.closed)

meu_arquivo.close()

#Abrindo arquivo com o with.
with open('arquivo-panosso.txt') as arquivo:
    print(arquivo.readlines())

#Arquivo ja foi fechado e não pode ser mais acessado.
print(arquivo.read())
