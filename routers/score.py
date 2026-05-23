from fastapi import APIRouter
from database import get_db
from models import RequisicaoScore

router = APIRouter()

@router.post("/score") #requisição score IA 
def calcular_score(requisicao: RequisicaoScore):
    try:
        conn = get_db() 
        
        cliente = conn.execute(
            "SELECT * FROM clientes WHERE id = ?", 
            (requisicao.id_cliente,) 
        ).fetchone() 
        
        produto = conn.execute(
            "SELECT * FROM produtos WHERE id = ?", 
            (requisicao.id_produto,)
        ).fetchone()
        
        if not cliente or not produto: #tratamento de erro p n quebrar
            return {"erro": "cliente ou produto não encontrado"}
        
        cliente = dict(cliente)
        produto = dict(produto)
        
        return { #retorna o post
            "cliente": cliente["nome"], #aqui é só colocar a tabela["nome_coluna"] pra retornar o dado que quiser
            "produto": produto["nome"],
            "preco": produto["preco"],
            "mensagem": "mensagem aaaaaaaaaaaaaaaa, llm aq"
        }
    
    finally:
        conn.close()