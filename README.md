# 🤖 CobraFácil-IA — Agente Inteligente de Controle de Inadimplência

## Contexto

O controle de inadimplência é um dos maiores desafios das pequenas e médias empresas. Muitas organizações ainda dependem de planilhas manuais para acompanhar contratos, vencimentos e pagamentos, o que aumenta erros no cálculo de multa e juros.

O **CobraFácil-IA** é um agente inteligente especializado em **análise de inadimplência empresarial**, utilizando IA Generativa para:

* **Identificar pagamentos em atraso automaticamente**
* **Calcular multa e juros com base em regras definidas**
* **Padronizar respostas e evitar erros humanos**
* **Garantir segurança e evitar alucinação de dados**

O agente utiliza exclusivamente dados estruturados fornecidos no sistema e segue regras rígidas de cálculo e escopo.

---

## O Que o Projeto Entrega

### 1. Documentação do Agente

O CobraFácil-IA foi desenvolvido com foco específico em controle de cobrança empresarial.

* **Caso de Uso:** Analisar contratos, verificar status de pagamento e calcular valores atualizados com multa e juros.
* **Persona e Tom de Voz:** Profissional, objetivo e técnico, focado exclusivamente em cobrança.
* **Arquitetura:** Leitura de arquivos CSV e JSON → montagem de contexto → envio para LLM → resposta estruturada.
* **Segurança:** O agente utiliza apenas dados fornecidos no contexto, não inventa informações e não responde fora do escopo de inadimplência.

📄 **Documentação:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

O agente utiliza dados estruturados na pasta [`data/`](./data/):

| Arquivo          | Formato | Descrição                                           |
| ---------------- | ------- | --------------------------------------------------- |
| `clientes.csv`   | CSV     | Dados cadastrais do cliente (nome, CNPJ, contato)   |
| `contrato.csv`   | CSV     | Tipo de contrato, valor mensal e data de vencimento |
| `financeiro.csv` | CSV     | Status do pagamento (Pago ou Em Aberto)             |
| `regras.json`    | JSON    | Percentual de multa e juros por dia                 |

Esses dados são utilizados para montar o contexto completo antes da análise do modelo.

📄 **Documentação:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

O comportamento do CobraFácil-IA é controlado por um **System Prompt rigoroso**, que define:

* Uso exclusivo dos dados fornecidos
* Proibição de invenção de informações
* Cálculo apenas quando o status for "Em Aberto"
* Estrutura obrigatória de resposta com:

  * Dias de atraso
  * Valor original
  * Multa
  * Juros
  * Total atualizado

Também são definidos:

* Exemplos de cálculo
* Tratamento de perguntas fora do escopo
* Respostas para dados incompletos

📄 **Documentação:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

O projeto possui um protótipo funcional que:

* Lê os dados via **Pandas**
* Monta o contexto dinamicamente
* Calcula dias de atraso com base na data atual
* Envia as informações para o modelo LLM (modelo local via Ollama)
* Retorna resposta estruturada de cobrança

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

A qualidade do agente foi avaliada com base em:

**Métricas Utilizadas:**

* Correção dos cálculos de multa e juros
* Consistência com os dados fornecidos
* Ausência de alucinações
* Respeito ao escopo de cobrança

O modelo utilizado foi o **Llama 3.2 3B Instruct (Q4_K_M)** rodando localmente, garantindo leveza e baixo consumo de recursos.

📄 **Documentação:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

O projeto inclui um pitch explicando:

* O problema da inadimplência empresarial
* Como o CobraFácil-IA automatiza cálculos
* O impacto na redução de erros e melhoria do fluxo de caixa

📄 **Documentação:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Utilizadas

| Categoria                | Ferramentas                    |
| ------------------------ | ------------------------------ |
| **LLM Local**            | Ollama + Llama 3.2 3B Instruct |
| **Desenvolvimento**      | Python + Pandas                |
| **Manipulação de Dados** | CSV e JSON                     |
| **Execução Local**       | Ambiente Python local          |

---

## Estrutura do Repositório

```
📁 cobrafacil-ia/
│
├── 📄 README.md
│
├── 📁 data/                          
│   ├── clientes.csv                 
│   ├── contrato.csv                
│   ├── financeiro.csv               
│   └── regras.json                  
│
├── 📁 docs/                          
│   ├── 01-documentacao-agente.md     
│   ├── 02-base-conhecimento.md       
│   ├── 03-prompts.md                 
│   ├── 04-metricas.md                
│   └── 05-pitch.md                   
│
├── 📁 src/                           
│   └── app.py                        
│
└── 📁 assets/                        
    └── ...
```

---

## Considerações Finais

1. O agente é especializado exclusivamente em controle de inadimplência.
2. Todas as respostas são baseadas em dados fornecidos.
3. O cálculo segue regras fixas de multa e juros.
4. O modelo roda localmente, garantindo baixo custo.
5. O sistema pode ser expandido para integração futura com ERP ou CRM.

---

