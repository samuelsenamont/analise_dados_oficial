# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento

import pandas as pd
import requests

df = pd.read_csv('ncr_ride_bookings.csv')

# Questões:
# (0,5) 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset?
corridas_completadas = df[df['Booking Status'] == 'Completed']
qtd_completadas = len(corridas_completadas)
print(qtd_completadas)

# (0,5) 2 - Qual a proporção em relação ao total de corridas?
proporcao = qtd_completadas / len(df)
print(f"{proporcao:.2%}")

# (0,5) 3 - Calcule a média da Distância ("Ride Distance") percorrida por cada Tipo de veículo.
media_distancia = df.groupby('Vehicle Type')['Ride Distance'].mean()
print(f"{media_distancia}")

# (0,5) 4 - Qual o Metodo de Pagamento ("Payment Method") mais utilizado pelas bicicletas ("Bike") ?
bikes = df[df['Vehicle Type'] == 'Bike']
pagamento_mais_usado = bikes['Payment Method'].value_counts().idxmax()
print(f"{pagamento_mais_usado}")

# (0,5) 5 - Qual o valor total arrecadado ("Booking Value") apenas das corridas Completed?
valor_total = corridas_completadas['Booking Value'].sum()
print(f"{valor_total}")

# (0,5) 6 - E qual o ticket médio ("Booking Value") dessas corridas Completed?
ticket_medio = corridas_completadas['Booking Value'].mean()
print(f"{ticket_medio}")


# (1,5) 7 - O IPEA disponibiliza uma API pública com diversas séries econômicas.
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados";
# Transforme em um DataFrame;
# Filtre para encontrar as séries da Fipe relacionadas a venda de imoveis ("vendas - Brasil").
url = "http://www.ipeadata.gov.br/api/odata4/Metadados"
resposta = requests.get(url)
dados = resposta.json()
df_meta = pd.DataFrame(dados['value'])

e_fipe = df_meta['FNTSIGLA'].str.contains('Fipe', na=False)
df_fipe = df_meta[e_fipe]

e_vendas = df_fipe['SERNOME'].str.contains('vendas - Brasil', na=False)
df_vendas = df_fipe[e_vendas]

print(df_vendas)

# (1,5) 8 - Descubra qual é o código da série correspondente (coluna: SERCODIGO).
CODIGO_ENCONTRADO = df_vendas['SERCODIGO'].values[0]
print(CODIGO_ENCONTRADO)

url_valores = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
resposta_valores = requests.get(url_valores)
df_valores = pd.DataFrame(resposta_valores.json()['value'])
df_valores = df_valores[['VALDATA', 'VALVALOR']]
idx_max = df_valores['VALVALOR'].idxmax()
print(df_valores.loc[idx_max])


# (1,5) 9 - Descubra quanto rendeu a VALE no ano de 2025



# (1,5) 10 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON.
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROE (Return on Equity) na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor" e o "roe"
resposta_planilhao = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2024-04-01"},
)
print("PLANILHAO json type:", type(resposta_planilhao.json()))
if isinstance(resposta_planilhao.json(), list):
    print("PLANILHAO colunas:", list(resposta_planilhao.json()[0].keys()))
else:
    print("PLANILHAO keys:", list(resposta_planilhao.json().keys()))
df_planilhao = pd.DataFrame(resposta_planilhao.json()) if isinstance(resposta_planilhao.json(), list) else pd.DataFrame(resposta_planilhao.json()['data'])

e_tecnologia = df_planilhao['setor'].str.lower() == 'tecnologia'
df_tec = df_planilhao[e_tecnologia].dropna(subset=['roe'])

linha_maior_roe = df_tec['roe'].idxmax()
print(df_tec.loc[linha_maior_roe, ['ticker', 'setor', 'roe']])


# (1,5) 11 - Faça a Magic Formula através dos indicadores Return on Capital (roc) e Earning Yield (ey) no dia 2024-04-01.
# Monte uma carteira de investimento com 10 ações baseado na estratégia Magic Formula.


# (1,5) 12 - Quantos setores ("setor") tem essa carteira formada por 10 ações?

