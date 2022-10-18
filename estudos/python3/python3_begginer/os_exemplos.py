import os

#Retorna o diretório de trabalho corrente --> Equivalente ao comando pwd
print(os.getcwd())

#Muda de diretório --> Equivalente ao comando cd
os.chdir('/home/machado')

print(os.getcwd())

#Verifica se um diretório é absoluto, diretório que são escrito desde a raiz
#/home/machado...
#/etc/...

#Diretprios relativos são diretórios que não são escritos desde a raiz
#projeto/
#projeto/django/
#projeto/django/venv
#Todos são diretório relativos.
print(os.path.isabs('/home/machado'))

#identifica o sistema operacional que está rodando.
print(os.name)

#Equivalente ao comando uname -a
print(os.uname())


#Adiciona algo para o getcwd
res = os.path.join(os.getcwd(), 'projeto_flask')

os.chdir(res)

print(os.getcwd())

#lista um diretório, se não for informado nenhum parametro ele retorna do diretório atual. --> Equivalente ao comando ls
print(os.listdir('/home/machado'))

#Retorna a lista de diretorios como um iterador, e cada iterado é um DirEntry
scanner = os.scandir('/home/machado/cursos')
scarn_dir = list(scanner)
print(scarn_dir)

#Metodos que o DirEntry possui.
print(dir(scarn_dir[0]))

#Retorna o inode
print(scarn_dir[0].inode())

#Retorna se é um diretório
print(scarn_dir[0].is_dir())

#Retorna se é um aqruivo
print(scarn_dir[0].is_file())

#Retorna se é um link simbolico
print(scarn_dir[0].is_symlink())

#Retorna o nome
print(scarn_dir[0].name)

#Retorna o caminho
print(scarn_dir[0].path)

#Retorna dados estatisticos
print(scarn_dir[0].stat())

#A função scandir precisa ser fechada
scanner.close()

#Verificando se um arquivo existe. Esse comando verifica se o arquivo ou diretório existe.
if not os.path.exists('mais_um_teste.txt'):
    #Cria um arquivo. Caso o arquivo exista, ele dará um erro.
    os.mknod('mais_um_teste.txt')

#Verificando com um caminho.
if not os.path.exists('/home/machado/cursos/teste_de_criacao.txt'):
    #Pode ser passando um caminho
    os.mknod('/home/machado/cursos/teste_de_criacao.txt')


if not os.path.exists('/home/machado/cursos/teste'):
    #Cria apenas UM diretório
    os.mkdir('/home/machado/cursos/teste')
    
#Cria multiplos diretório
#Nesse exemplo será criado os diretórios 'teste1, teste2 e teste3.txt(SIM COMO UM DIRETÓRIO)'
#exist_ok=True --> Caso o arquivo exista, ele nao dara erro
os.makedirs('/home/machado/cursos/teste/teste1/teste2/teste3.txt', exist_ok=True)

#renomeia o arquivo ou diretório
#Se o diretório não estiver vazio, o comando dara um erro
os.rename('/home/machado/cursos/teste/teste1/teste2/teste3.txt', '/home/machado/cursos/teste/teste1/teste2/batata')

os.chdir('/home/machado/cursos/teste/')

#Cuidados com a parte de deletar, quando deletado um arquivo, ele não irá para a lixeira, mas será APAGADO direto.

#Apagando um arquivo
os.remove('teste1/teste2/batata/dhusahduash.txt')

#O diretório só será apagado caso esteja vazio, apenas se o diretório estiver vazio
os.rmdir('teste1/teste2/batata')

#Removendo diretórios vazios
os.removedirs('teste1/teste2/')

print('Não deu erro')
