# griffe-score-api

API REST com FastAPI e SQLite para scoring de clientes de uma marca de roupas premium. Cruza dados de clientes e produtos e utiliza LLM para avaliar propensão de compra.

# Griffe Score API

API REST desenvolvida com FastAPI e SQLite para scoring de clientes de uma marca de roupas premium.

## O que faz
- Cadastro de clientes e produtos
- CRUD completo via endpoints REST
- Endpoint de scoring que cruza dados do cliente com o produto 
e utiliza LLM para avaliar a propensão de compra

## Tecnologias
- Python
- FastAPI
- SQLite
- LLM (em desenvolvimento)

## Endpoints
- `GET /clientes` — lista todos os clientes
- `GET /produtos` — lista todos os produtos
- `POST /score` — retorna o score de propensão de compra de um cliente para um produto
- `PUT /clientes/{id}` — atualiza dados de um cliente
- `PUT /produtos/{id}` — atualiza dados de um produto
- `DELETE /clientes/{id}` — remove um cliente (em desenvolvimento)
- `DELETE /produtos/{id}` — remove um produto (em desenvolvimento)
