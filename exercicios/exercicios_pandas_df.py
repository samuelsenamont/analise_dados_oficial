"""
Aula - Exercicios de Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados com print.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Pense no DataFrame como uma planilha.
- Resolva um exercicio por vez.
"""

import pandas as pd


# -------------------------------------------------
# BLOCO 1: criar DataFrame e inspecionar estrutura
# -------------------------------------------------

dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

# Exercicio 1:
# a) Crie o DataFrame df_vendas usando dados_vendas
df_vendas = pd.DataFrame(dados_vendas)
print(df_vendas)

# b) Mostre as 5 primeiras linhas
print(df_vendas.head())

# c) Mostre o formato (linhas, colunas)
print("Formato:", df_vendas.shape)

# d) Mostre os tipos de dados das colunas
print(df_vendas.dtypes)


# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------

# Exercicio 2:
# a) Mostre apenas as colunas "mes" e "vendas"
print(df_vendas[["mes", "vendas"]])

# b) Mostre somente a primeira linha
print(df_vendas.iloc[0])

# c) Mostre as linhas de indice 2 ate 4
print(df_vendas.iloc[2:5])


# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------

# Exercicio 3:
# a) Filtre vendas acima de 12000
print(df_vendas[df_vendas["vendas"] > 12000])

# b) Filtre apenas a filial "Centro"
print(df_vendas[df_vendas["filial"] == "Centro"])

# c) Filtre vendas acima de 11000 na filial "Norte"
print(df_vendas[(df_vendas["vendas"] > 11000) & (df_vendas["filial"] == "Norte")])


# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------

# Exercicio 4:
# a) Crie a coluna "ticket_medio" = vendas / clientes
df_vendas["ticket_medio"] = df_vendas["vendas"] / df_vendas["clientes"]

# b) Crie a coluna "meta_batida" com True para vendas >= 13000
df_vendas["meta_batida"] = df_vendas["vendas"] >= 13000

# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"
print(df_vendas[["filial", "mes", "ticket_medio", "meta_batida"]])


# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------

# Exercicio 5:
# a) Calcule total de vendas por filial
total_por_filial = df_vendas.groupby("filial")["vendas"].sum()
print(total_por_filial)

# b) Calcule media de clientes por mes
media_clientes_por_mes = df_vendas.groupby("mes")["clientes"].mean()
print(media_clientes_por_mes)

# c) Descubra a filial com maior total de vendas
filial_maior = total_por_filial.idxmax()
print("Filial com maior total de vendas:", filial_maior)


# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------

# Exercicio 6:
# a) Ordene df_vendas por "vendas" em ordem decrescente
df_ordenado = df_vendas.sort_values("vendas", ascending=False)

# b) Pegue os 3 maiores resultados de vendas
top3 = df_ordenado.head(3)

# c) Mostre um ranking com "filial", "mes", "vendas"
print(top3[["filial", "mes", "vendas"]].reset_index(drop=True))


# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------

# Exercicio 7 (desafio):
# 1) Gere um resumo por filial com:
#    - total_vendas
#    - media_ticket_medio
#    - total_clientes
resumo = df_vendas.groupby("filial").agg(
    total_vendas=("vendas", "sum"),
    media_ticket_medio=("ticket_medio", "mean"),
    total_clientes=("clientes", "sum")
)

# 2) Ordene o resumo por total_vendas (desc)
resumo = resumo.sort_values("total_vendas", ascending=False)
print(resumo)

# 3) Exiba qual filial teve melhor desempenho geral
melhor_filial = resumo.index[0]
print("Filial com melhor desempenho geral:", melhor_filial)


# ---------------------
# CHECKLIST DE REVISAO
# ---------------------
#
# [x] Sei criar um DataFrame com dicionario
# [x] Sei selecionar colunas e linhas
# [x] Sei filtrar dados com condicoes
# [x] Sei criar novas colunas no DataFrame
# [x] Sei agregar dados com groupby
# [x] Sei ordenar e criar ranking
