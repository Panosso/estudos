# API de Autenticação com JWT

Esta API foi desenvolvida utilizando **FastAPI** e permite autenticação via JWT, com rotas protegidas baseadas em papéis de usuário.

## Funcionalidades

- Geração de token JWT através da rota `/token`.
- Rotas protegidas para usuários e administradores:
  - `/user`: Acessível apenas para usuários com o papel `user`.
  - `/admin`: Acessível apenas para usuários com o papel `admin`.

## Tecnologias Utilizadas

- Python 3.9+
- FastAPI
- SQLite (para persistência básica)
- JWT (para autenticação)

## Pré-requisitos

- Python 3.9 ou superior instalado.
- Gerenciador de pacotes `pip`.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Panosso/k2_challenge.git
   cd k2_challenge
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente criando um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
   ```
   touch .env
   echo "SECRET_KEY=mysecretkey" >> .env
   echo "ALGORITHM=HS256" >> .env
   echo "ACCESS_TOKEN_EXPIRE_MINUTES=30" >> .env
   echo "TOKEN_TYPE="Bearer" >> .env
   echo "API_V1_STR="https://localhost:8000" >> .env
   ```

5. Inicie o servidor:
   ```bash
   uvicorn api:app --reload
   ```

## Docker

Para rodar o projeto em um container Docker:

1. Construa a imagem:
   ```bash
   docker build -t jwt-auth-api .
   ```

2. Rode o container:
   ```bash
   docker run -d -p 8000:8000 --env-file .env jwt-auth-api
   ```

## Uso

Acesse a documentação da API gerada automaticamente em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Endpoints Principais

#### 1. Geração de Token JWT

**Rota**: `/token`

**Método**: `POST`

#### 2. Rota Protegida para Usuário

**Rota**: `/user`

**Método**: `GET`

**Cabeçalho**:
```
Authorization: Bearer <token>
```

#### 3. Rota Protegida para Administrador

**Rota**: `/admin`

**Método**: `GET`

**Cabeçalho**:
```
Authorization: Bearer <token>
```

## Testes

Você pode testar a API utilizando ferramentas como:

- [Postman](https://www.postman.com/)
- [cURL](https://curl.se/)

### Exemplo com cURL

1. **Obter Token**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/token" \
   -H "Content-Type: application/x-www-form-urlencoded" \
   -d "username=user&password=L0XuwPOdS5U"
   ```

2. **Acessar Rota Protegida `/user`**:
   ```bash
   curl -X GET "http://127.0.0.1:8000/user" \
   -H "Authorization: Bearer <token>"
   ```

## Estrutura do Projeto

```
.
├── api.py           # Código principal da API
├── config.py        # Código para carregar as configurações
├── database.py      # Código para criação da database
├── models.py        # Código com modelos que serão utilizados
├── utils.py         # Código com funções uteis para o sistema
├── requirements.txt # Dependências do projeto
├── .env             # Variáveis de ambiente
├── Dockerfile       # Configuração para conteinerização
└── README.md        # Documentação do projeto
```
