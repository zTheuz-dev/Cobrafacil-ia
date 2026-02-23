import json
import pandas as pd
import requests
import streamlit as st
from datetime import datetime

# ============ Configuração ==========

OLLAMA_URL= "http://localhost:11434/api/generate"
MODELO = "llama3.2:3b-instruct-q4_K_M"
#===========carregar dados==========

cliente = pd.read_csv('./data/cliente.csv')
contrato = pd.read_csv('./data/contrato.csv')
financeiro = pd.read_csv('./data/financeiro.csv')
regras = json.load(open('./data/regras.json'))

# ========== MONTAR CONTEXTO ==========

data_atual = datetime.today().strftime("%Y-%m-%d")

contexto = f"""
CLIENTE:
Nome: {cliente['nome']}
CNPJ: {cliente['cnpj']}
Tipo de Contrato: {contrato['tipo_contrato']}

DADOS DO CONTRATO:
Valor Mensal: R$ {contrato['valor_mensal']}
Data de Vencimento: {contrato['data_vencimento']}

SITUAÇÃO FINANCEIRA:
Status do Pagamento: {financeiro['status_pagamento']}
Data de Pagamento: {financeiro['data_pagamento']}

REGRAS DE COBRANÇA:
Multa: {regras['multa_percentual']}%
Juros ao dia: {regras['juros_dia_percentual']}%
Data Atual: {data_atual}
"""

# ========= SYSTEM PROMPT =========

SYSTEM_PROMPT = """
Você é o CobraFácil AI, um especialista em controle de inadimplência empresarial.

OBJETIVO:
Analisar dados de clientes, identificar atrasos e calcular valores atualizados com multa e juros.

REGRAS:
- Use apenas os dados fornecidos no contexto.
- Nunca invente valores, datas ou clientes.
- Se faltar informação, diga claramente.
- Só calcule multa e juros se o status for "Em Aberto".
- Se o status for "Pago", informe que não há pendências.
- Não responda perguntas fora do escopo de cobrança.
- Responda de forma clara, objetiva e profissional.

CÁLCULOS:
Multa = valor_original . (multa_percentual / 100)
Juros = valor_original . (juros_dia_percentual / 100) . dias_atraso
Total = valor_original + multa + juros

Sempre mostrar:
- Dias de atraso
- Valor original
- Multa
- Juros
- Total atualizado
"""
# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    data = r.json()
    print(data)  # debug para ver o que realmente vem
    if "response" in data:
        return data["response"]
    elif "message" in data:
        return data["message"]
    else:
        return f"Formato inesperado: {data}"


# ============ INTERFACE ============
st.title("🎓 CobraFacil ia, Seu Assistente Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre cobranças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))