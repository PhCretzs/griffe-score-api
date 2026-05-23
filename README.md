# Griffe Score API

API REST desenvolvida com FastAPI e SQLite para scoring de propensão de compra de clientes de uma marca de roupas premium.

## O que faz
- CRUD completo de clientes e produtos
- Endpoint de scoring que cruza dados do cliente com o produto e utiliza LLM para avaliar a propensão de compra
- Retorna score de 0 a 100 com justificativa da análise

## Tecnologias
- Python
- FastAPI
- SQLite
- Pydantic
- Anthropic SDK (claude-haiku-4-5)
- python-dotenv

## Endpoints
- `GET /clientes` — lista todos os clientes
- `GET /clientes/{id}` — busca cliente por id
- `PATCH /alterar_clientes/{id}` — atualização parcial de cliente
- `DELETE /deletar_clientes/{id}` — remove cliente
- `GET /produtos` — lista todos os produtos
- `GET /produtos/{id}` — busca produto por id
- `PATCH /alterar_produtos/{id}` — atualização parcial de produto
- `DELETE /deletar_produtos/{id}` — remove produto
- `POST /score` — retorna score de propensão de compra via LLM

## Exemplo de resposta do /score
```json
{
  "cliente": "Ana Paula Ferreira",
  "produto": "Calça Alfaiataria Slim",
  "preco": 1200,
  "score": 72,
  "justificativa": "Cliente com renda disponível suficiente e perfil compatível com produto premium..."
}
```

## Como rodar
```bash
pip install -r requirements.txt
fastapi dev main.py
```