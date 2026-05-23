#models.py
from pydantic import BaseModel #vem do pydantic, valida os dados que chegam da requisição. Pro POST.
from typing import Optional


class RequisicaoScore(BaseModel): #classe para definir o que espero receber
    id_cliente: int
    id_produto: int

class ClientePatch(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    genero: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    profissao: Optional[str] = None
    area_formacao: Optional[str] = None
    salario_mensal: Optional[float] = None
    gasto_mensal: Optional[float] = None
    renda_disponivel: Optional[float] = None
    ticket_medio: Optional[float] = None
    tem_cartao_credito: Optional[int] = None
    score_credito: Optional[int] = None
    estilo_preferido: Optional[str] = None
    frequencia_compra_roupas: Optional[str] = None

class ProdutoPatch(BaseModel):
    nome: Optional[str] = None
    categoria: Optional[str] = None
    preco: Optional[float] = None
    marca: Optional[str] = None
    estilo_alvo: Optional[str] = None
    descricao: Optional[str] = None