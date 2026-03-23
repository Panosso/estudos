# Sobre
Ester README tem por objetivo fornecer as informações necessárias para avaliação de candidatos para a linguagem Python.
#  🏗   O que fazer?

Você deve realizar um fork deste repositório e, ao finalizar, enviar o link do seu repositório para a nossa equipe. Lembre-se, NÃO é necessário criar um Pull Request para isso, nós iremos avaliar e retornar por email o resultado do seu teste.

# 🚨 Requisitos

- A API deverá ser construída em Python
- Implementar autenticação e deverá seguir o padrão **JWT**, lembrando que o token a ser recebido deverá ser no formato **Bearer**
- Recomendamos uso de Flask ou Django como framework, no  entanto outros frameworks serão aceitos.
- Para a comunicação com o banco de dados utilize algum **ORM**/**ODM**
- Bancos relacionais permitidos:
      - MySQL
      - MariaDB
      - Postgres
- Bancos não relacionais permitidos:
      - MongoDB
- Sua API deverá seguir os padrões Rest na construção das rotas e retornos
- Sua API deverá conter a collection/variáveis do postman ou algum endpoint da documentação em openapi para a realização do teste
- Descrever de forma clara em seu README os passos para executar seu projeto.
# 🕵🏻‍♂️ Itens a serem avaliados

- Estrutura do Projeto
- Segurança da API, como autenticação, senhas salvas no banco, SQL Injection e outros
- Boas práticas da Linguagem/Framework
- Seu projeto deverá seguir tudo o que foi exigido na seção [O que desenvolver?](##--o-que-desenvolver)
- Migrations para a criação das tabelas do banco relacional caso seja escolhido um banco relacional.

# 🎁 Extra

Esses itens não são obrigatórios, porém desejados.

- Testes unitários
- Linter
- Code Formater


# 🖥 O que desenvolver?
Você deverá construir uma API que faça jogos da mega sena, o usuario deverá escolher a quantidade de dezenas por jogo e sua API irá gerar aleatoriamente dezenas para o usuário. O usuário poderá consultar o resultado do ultimo jogo e comparar com suas dezenas para conferir quantos numeros acertou.

- IMPORTANTE: Para obter o ultimo resultado da megasena você deverá fazer um webscrapping no Google. A seguinte pesquisa te traz o que você precisa obter: https://www.google.com/search?q=caixa+mega+sena 


Rotas necessárias para API:

- Usuário

    - Cadastro
    - Login
    - Edição (o usuário deve está autenticado)
    - Exclusão lógica (O usuário so pode deletar a propria conta)


- Megasena (todos endpoints devem exigir autenticação)
    
    - Realizar um novo jogo.
        - Deverá receber quantos dezenas (entre 6 e 10) o usuário deseja e sortear dezenas de acordo com a quantidade escolhida.
    - Consultar o resultado da ultima megasena (O webscrapping citado acima).
    - Ver quantos numeros acertou no seu ultimo jogo.
    - Listar seus jogos passados.

# 🔗 Links

- Documentação JWT https://jwt.io/
- Frameworks:

    -   https://www.djangoproject.com
    -   https://flask.palletsprojects.com/en/1.1.x/

- Bibliotecas que podem te ajudar:
    - random
    - pandas
    - cfscrape
    - bs4
    - lxml

