#clientes.py
from fastapi import APIRouter
from database import get_db
from models import ClientePatch, ClienteAdd

router = APIRouter()

@router.post("/clientes")
def adicionar_cliente(post: ClienteAdd):
    try:
        conn = get_db()
        col = post.model_dump()
        colunas = ", ".join(col.keys())
        placeholders = ", ".join("?" for _ in col.keys())
        valores = tuple(col.values())
        
        conn.execute(
            f"INSERT INTO clientes ({colunas}) VALUES ({placeholders})",
            valores
        )

        conn.commit()

        return {"mensagem": "cliente adicionado com sucesso"}

    finally:
        conn.close()

@router.get("/clientes") #Get que retorna tudo
def listar_clientes(): 
    try:
        conn = get_db() 
        cursor = conn.execute("SELECT * FROM clientes").fetchall()
        
        if not cursor:
            return {"erro": "erro na querry"}
        
        return [dict(c) for c in cursor] #converte cada row para dict e retorna (pq o fastapi só entende dict por conta do json)
    
    finally:
        conn.close()

@router.get("/clientes/{id}") #Get busca especifica
def buscar_um_cliente(id : int):
    try:
        conn = get_db()

        cursor = conn.execute(
            "SELECT * FROM clientes WHERE id = ?", (id,)
            ).fetchone()
        
        if not cursor:
            return {"erro": "cliente não encontrado"}

        return {"cliente": dict(cursor)}
    
    finally:
        conn.close()

@router.patch("/alterar_clientes/{id}")
def alterar_um_cliente(id: int, patch: ClientePatch):
    try:
        conn = get_db()   
        col = patch.model_dump(exclude_none=True)
        
        if not col:
            return {"erro": "nenhum coluna para atualizar"}
        
        sql = ", ".join(f"{col} = ?" for col in col.keys())
        valores = (*col.values(), id)

        cursor = conn.execute(f"UPDATE clientes SET {sql} WHERE id = ?", valores)
        
        if cursor.rowcount == 0:
            return {"erro": "cliente não encontrado"}
        
        conn.commit()

        return {"mensagem": "tabela atualizada com sucesso"}
    
    finally:
        conn.close()

@router.delete("/deletar_clientes/{id}")
def deletar_um_cliente(id:int):
    try:
        conn = get_db()

        cursor = conn.execute(f"DELETE FROM clientes WHERE id = ?", (id,))

        if cursor.rowcount == 0:
            return {"erro": "cliente não encontrado"}

        conn.commit()

        return {"mensagem": "id deletado com sucesso"}

    finally:
        conn.close()