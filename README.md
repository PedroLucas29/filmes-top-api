# FilmesTop API

Este é um projeto de API RESTful para gerenciar filmes e o sistema de aluguel de filmes. A aplicação foi desenvolvida em Python utilizando o framework Flask e Flask-RESTful, com banco de dados PostgreSQL, Redis para cache e SQLAlchemy com suporte para operações assíncronas (usando `AsyncSession`). 

## Requisitos

- Docker
- Docker Compose
- Python 3.12+
- Redis
- PostgreSQL

## Tecnologias Utilizadas

- **Flask**: Framework web para construir a API.
- **SQLAlchemy**: ORM para o banco de dados PostgreSQL, com suporte para operações assíncronas usando `AsyncSession`.
- **Redis**: Usado para caching de dados.
- **Docker e Docker Compose**: Para conteinerizar a aplicação e seus serviços (PostgreSQL e Redis).

## Instalação

### Clonar o repositório:
```bash
git clone https://github.com/usuario/filmes-top-api.git
cd filmes-top-api
```
## Configurar variáveis de ambiente:

### Crie um arquivo `.env` no diretório raiz com as seguintes variáveis:
```bash
PG_USER=admin
PG_PASS=admin
PG_DB=filmesdb
REDIS_URL=redis://redis:6379/0
DATABASE_URL=postgresql+asyncpg://admin:admin@postgresql:5432/filmesdb
```

### Subir os containers com Docker Compose:
```bash
docker-compose up -d
Isso irá iniciar os containers para o PostgreSQL, Redis e a aplicação Flask.
```

## Rotas Disponíveis
Algumas das principais rotas são:

- GET /filmes: Lista todos os filmes disponíveis.
- POST /alugar: Aluga um filme.
- GET /alugueis: Exibe todos os filmes que o usuário alugou, com a nota atribuída e a data de locação.


- **GET /filmes**: Lista todos os filmes disponíveis.
  - **Resposta Exemplo:**
    ```json
      {
        "id": 1,
        "titulo": "Filme A",
        "genero": "Ação",
        "ano": 2024,
        "sinopse": "Descrição do Filme A",
        "diretor": "Diretor A"
        
      }
     ```
    
- **POST /alugueis**: Aluga um filme.
  - **Corpo da Requisição:**
    ```json
    {
      "usuario_id": 1,
      "filme_id": 42,
      "nota": 8.5
    }
     ```
  - **Resposta Exemplo:**
  - ```json
    {
      "id": 1,
      "usuario_id": 1,
      "filme_id": 42,
      "data_locacao": "2024-09-15T10:45:00Z",
      "nota": 8.5
    }
     ```
    
- **POST /filmes/alugueis/<int:aluguel_id>/nota',**: Avalia um filme.
  - **Corpo da Requisição:**
    ```json
    {
      "usuario_id": 1,
      "filme_id": 42,
      "nota": 9.0
    }
     ```
  - **Resposta Exemplo:**
    ```json
    {
      "id": 1,
      "usuario_id": 1,
      "filme_id": 42,
      "data_locacao": "2024-09-15T10:45:00Z",
      "nota": 9.0
    }
    ```

- **GET /filmes/<id>**: Busca um filme pelo ID.
  - **Resposta Exemplo:**
    ```json
    {
      "id": 1,
      "titulo": "Filme A",
      "genero": "Ação",
      "ano": 2024,
      "sinopse": "Descrição do Filme A",
      "diretor": "Diretor A",
      "nota_final": 9.0,
      "total_avaliacoes": 100
    }
    ```

- **GET /filmes/genero/<genero>**: Busca filmes pelo gênero.
  - **Resposta Exemplo:**
    ```json 
    [
      {
        "id": 1,
        "titulo": "Filme A",
        "genero": "Ação",
        "ano": 2024,
        "sinopse": "Descrição do Filme A",
        "diretor": "Diretor A",
        "nota_final": 9.0,
        "total_avaliacoes": 100
      },
      {
        "id": 2,
        "titulo": "Filme B",
        "genero": "Ação",
        "ano": 2023,
        "sinopse": "Descrição do Filme B",
        "diretor": "Diretor B",
        "nota_final": 8.5,
        "total_avaliacoes": 150
      }
    ]
    ```

## Comandos Úteis

### Rodar a aplicação localmente:
```bash
flask --app app.py run
```
### Acessar o Redis CLI:
```bash
docker exec -it filmes_top_redis redis-cli
```
### Para recriar os containers:
```bash
docker-compose down
docker-compose up -d
```
### Debug de logs do container PostgreSQL:
```bash
docker logs filmes_top_pg
```
### Debug de logs do container Redis:
```bash
docker logs filmes_top_redis
```

## Contribuição
Se desejar contribuir com o projeto, abra uma issue ou faça um pull request.

