from csv import reader
from csv import DictWriter
from csv import writer
from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    #Pula o cabeçalho
    next(leitor_csv)
    for linha in leitor_csv:
        #Cada linha é representada por uma lista.
        print(f'Lutador {linha[0]} , nasceu no {linha[1]} e tem {linha[2]} cm de altura')

with open('lutadores.csv') as arquivo:
    #Retornara um dicionário, se for passado um delimiter, 
    #a função vai atribuir a separação dos dados com o que for passado como valor pra ele.
    #Caso esse parametro seja omitido a biblioteca vai assumir como delimitador a ','
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        print(f"{linha['Nome']}, {linha['País']}, {linha['Altura (em cm)']}")
        
        
with open('filmes.csv', 'a') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])
    while filme != 'sair':
        filme = input("Titulo: ")
        if filme != 'sair':
            
            genero = input("Genrero: ")
            duracao = input("Duracao: ")
            escritor_csv.writerow([filme, genero, duracao])
            
with open('filmes.csv', 'a') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input("Titulo: ")
        if filme != 'sair':
            
            genero = input("Genrero: ")
            duracao = input("Duracao: ")
            escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duracao": duracao})
