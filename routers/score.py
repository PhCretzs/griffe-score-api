from fastapi import APIRouter
from database import get_db
from models import RequisicaoScore
from dotenv import load_dotenv
import anthropic
import os
import json

router = APIRouter()

load_dotenv()

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
        
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

        message = client.messages.create(
                    model="claude-haiku-4-5",
                    max_tokens=100,
                    system=
                    """
                        Você é um especialista em análise de perfil de consumo de uma loja de grife fictícia.
                        Dado o perfil de um cliente e um produto específico, analise a propensão de compra.

                        Retorne APENAS um JSON válido, sem texto adicional, sem markdown, sem explicações. Exatamente nesse formato:
                        {"score": 85, "justificativa": "texto curto aqui"}

                        Regras:
                        - score é um número inteiro de 0 a 100
                        - justificativa é uma frase curta explicando os principais fatores
                        - Não use markdown. Não use blocos de código. Retorne apenas o JSON puro
                    """,
                    messages=[
                        {
                            "role": "user",
                            "content": 
                            f"""
                                CLIENTE:
                                - Nome: {cliente['nome']}
                                - Idade: {cliente['idade']} anos
                                - Gênero: {cliente['genero']}
                                - Profissão: {cliente['profissao']} ({cliente['area_formacao']})
                                - Salário mensal: R${cliente['salario_mensal']}
                                - Gasto mensal: R${cliente['gasto_mensal']}
                                - Renda disponível: R${cliente['renda_disponivel']}
                                - Ticket médio: R${cliente['ticket_medio']}
                                - Tem cartão de crédito: {'Sim' if cliente['tem_cartao_credito'] else 'Não'}
                                - Score de crédito: {cliente['score_credito']}
                                - Estilo preferido: {cliente['estilo_preferido']}
                                - Frequência de compra: {cliente['frequencia_compra_roupas']}

                                PRODUTO:
                                - Nome: {produto['nome']}
                                - Categoria: {produto['categoria']}
                                - Marca: {produto['marca']}
                                - Preço: R${produto['preco']}
                                - Estilo alvo: {produto['estilo_alvo']}
                                - Descrição: {produto['descricao']}

                                Analise e retorne o JSON.
                            """
                        }
                    ]
                )
        
        texto = message.content[0].text
        texto = texto.replace("```json", "").replace("```", "").strip()
        resposta = json.loads(texto)

        return {
                "cliente": cliente["nome"],
                "produto": produto["nome"],
                "preco": produto["preco"],
                "score": resposta["score"],
                "justificativa": resposta["justificativa"]
            }
    
    finally:
        conn.close()