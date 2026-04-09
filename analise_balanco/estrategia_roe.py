
import pandas as pd
import requests

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "SeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyNzk5LCJpYXQiOjE3NzQzNTA3OTksImp0aSI6ImIyZjhjYzg5MzA1MzQ2ZDg4ZDAwZGM0NjU1MzQyMDA5IiwidXNlcl9pZCI6IjEwNSJ9.HIh3rBik0-GoJ_DLERqgLGY9-WOgGPrUwOg-6esxD7UJWT"
resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2026-03-23"},
)
dados = resp.json()
df = pd.DataFrame(dados)
maximo = df["roe"].max()
filtro = df["roe"]==maximo
df[filtro]


base_url = "https://laboratoriodefinancas.com/api/v2"
token = "SeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyNzk5LCJpYXQiOjE3NzQzNTA3OTksImp0aSI6ImIyZjhjYzg5MzA1MzQ2ZDg4ZDAwZGM0NjU1MzQyMDA5IiwidXNlcl9pZCI6IjEwNSJ9.HIh3rBik0-GoJ_DLERqgLGY9-WOgGPrUwOg-6esxD7UJWT"
params = {"ticker": "PETR4", "data_ini": "2024-01-01", "data_fim": "2024-12-31"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
dados = resp.json()
df_preco = pd.DataFrame(dados)