# 📚 Base de Conhecimento

## Dados Utilizados

O agente utiliza apenas os dados essenciais para identificar inadimplência e calcular valores em atraso.

| Arquivo          | Formato | Utilização no Agente                    |
| ---------------- | ------- | --------------------------------------- |
| `clientes.csv`   | CSV     | Nome, CNPJ e contato do cliente         |
| `contratos.csv`  | CSV     | Valor mensal e data de vencimento       |
| `financeiro.csv` | CSV     | Status do pagamento (Pago ou Em Aberto) |
| `regras.json`    | JSON    | Percentual de multa e juros             |


## Adaptações nos Dados

Foram feitas adaptações simples:

* Inclusão do campo **status_pagamento** (Pago / Em Aberto)
* Padronização das datas
* Inclusão do tipo de contrato **"Contrato Completo"**
* Cálculo automático de dias de atraso (sem salvar no banco)

O agente não armazena cálculos — ele apenas calcula quando solicitado.

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos CSV e JSON são carregados no início do sistema.

Quando o usuário consulta um cliente, o sistema:

1. Busca os dados do cliente
2. Verifica se está "Em Aberto"
3. Calcula dias de atraso
4. Aplica multa e juros


### Como os dados são usados no prompt?

Apenas os dados do cliente consultado são enviados ao modelo.

As regras de multa e juros ficam fixas no system prompt.

Exemplo de instrução fixa:

> "Se estiver em atraso, aplicar multa de 2% + juros de 0,03% ao dia."



## Exemplo de Contexto Enviado ao Agente


Cliente: Empresa XPTO
Valor mensal: R$ 2.000,00
Vencimento: 01/02/2026
Status: Em Aberto
Data atual: 20/02/2026

Regras:
Multa: 2%
Juros: 0,03% ao dia
```

O agente então responde:

* Dias de atraso
* Valor atualizado
* Sugestão de cobrança

