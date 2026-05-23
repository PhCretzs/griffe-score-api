#main.py
import os
import sys
from fastapi import FastAPI
from database import get_db
from routers import clientes, produtos, score
from contextlib import asynccontextmanager

@asynccontextmanager #tratando caso o banco n seja encontrado
async def lifespan(app: FastAPI):
    if not os.path.exists("griffe_db.db"):
        print("banco de dados não encontrado")
        sys.exit(1)
    yield

app = FastAPI(lifespan=lifespan) #criando o objeto app que é minha aplicação web e vai receber as requisições http

app.include_router(clientes.router)
app.include_router(produtos.router)
app.include_router(score.router)