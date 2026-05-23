#main.py
import os
import sys
from fastapi import FastAPI
from database import get_db
from models import RequisicaoScore
from routers import clientes, produtos, score

app = FastAPI() #criando o objeto app que é minha aplicação web e vai receber as requisições http

app.include_router(clientes.router)
app.include_router(produtos.router)
app.include_router(score.router)


@app.on_event("startup") #tratando caso o banco n seja encontrado
def verificar_banco():
    if not os.path.exists("griffe_db.db"):
        print("banco de dados não encontrado")
        sys.exit(1)