def pegar_valor(dicionario, chave):
    try:
        return dicionario[chave]
    
    except KeyError:
        return None

dicionario = {'nome': 'Pedro'}

print(pegar_valor(dicionario, 'nomedsad'))

#Tente executar esse trecho de cod
try:

    #Erro
    #f=open('potato.txt', 'wr')

    #Nao Erro
    f=open('potato.txt', 'r')

#Caso voce encontre o erro abaixo, realize esse trecho de código
except ValueError as e:
    print("Deu o erro '%s'" %(e))


#Senao realize o trecho abaixo
else:
    print(f.readline())
    
#Tento ou nao erro, o finally SEMPRE será executado. Usado para sempre garantir que um arquivo será finalizado ou um cursor seja finalizado.
finally:
    print("Executei")

Tema de casa - Tratamento
    
#Problema 1
try:
    for i in ["a", "b", "c"]:
        print(i**2)

#É possivel passar mais de um erro caso encontrado. Ou simplesmente escrever Exception.
except (TypeError, ValueError) as e:
    print("Apenas numeros pode ser elevados ao quadrado\n Erro: {erro}".format(erro=e))

finally:
    print("Executei só de zoas")

#Problema 2
try:
    x=5
    y=0

    print(x/y)

except ZeroDivisionError as e:
    print("Impossível dividir por Zero. Erro: {erro}".format(erro=e))

finally:
    print("All Done")

#Problema 3
def ask():
    while True:
        try:
            numero = int(input("Digite um número: "))

            print(numero**2)

        except ValueError as e:
            print("Digite um NUMERO carai!")
            continue

ask()
