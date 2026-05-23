#produtos.py
from fastapi import APIRouter
from database import get_db
from models import ProdutoPatch, ProdutoAdd

router = APIRouter()

@router.post("/produtos")
def adicionar_produto(post: ProdutoAdd):
    try:
        conn = get_db()
        col = post.model_dump()
        colunas = ", ".join(col.keys())
        placeholders = ", ".join("?" for _ in col.keys())
        valores = tuple(col.values())
        
        conn.execute(
            f"INSERT INTO produtos ({colunas}) VALUES ({placeholders})",
            valores
        )

        conn.commit()

        return {"mensagem": "produto adicionado com sucesso"}

    finally:
        conn.close()

@router.get("/produtos") # Get que retorna tudo
def listar_produtos():
    try:
        conn = get_db()
        cursor = conn.execute("SELECT * FROM produtos").fetchall()
        
        if not cursor:
            return {"erro": "erro na querry"}

        return [dict(p) for p in cursor]

    finally:
        conn.close()

@router.get("/produtos/{id}") #Get busca especifica
def buscar_um_produto(id : int):
    try:
        conn = get_db()

        cursor = conn.execute(
            "SELECT * FROM produtos WHERE id = ?", (id,)
            ).fetchone()
        
        if not cursor:
            return {"erro": "produto não encontrado"}

        return {"produto": dict(cursor)}
    
    finally:
        conn.close()

@router.patch("/alterar_produtos/{id}")
def alterar_um_produto(id: int, patch: ProdutoPatch):
    try:
        conn = get_db()   
        col = patch.model_dump(exclude_none=True)
        
        if not col:
            return {"erro": "nenhum coluna para atualizar"}
        
        sql = ", ".join(f"{col} = ?" for col in col.keys())
        valores = (*col.values(), id)

        cursor = conn.execute(f"UPDATE produtos SET {sql} WHERE id = ?", valores)
        
        if cursor.rowcount == 0:
            return {"erro": "produto não encontrado"}
        
        conn.commit()

        return {"mensagem": "tabela atualizada com sucesso"}
    
    finally:
        conn.close()

@router.delete("/deletar_produtos/{id}")
def deletar_um_produto(id:int):
    try:
        conn = get_db()

        cursor = conn.execute(f"DELETE FROM produtos WHERE id = ?", (id,))

        if cursor.rowcount == 0:
            return {"erro": "produto não encontrado"}

        conn.commit()

        return {"mensagem": "id deletado com sucesso"}

    finally:
        conn.close()