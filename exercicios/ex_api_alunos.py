"""
===========================================================
ATIVIDADE – CONSULTA DE DADOS VIA API
OBJETIVO:
- Consultar APIs públicas usando requests
- Entender estrutura JSON
- Transformar resposta em DataFrame
- Trabalhar com parâmetros e TOKENS
- Explorar dados externos
REGRAS:
- NÃO apagar os enunciados.
- Organizar o código.
- Comentar cada etapa importante.
- Mostrar os resultados com print() ou DataFrame.
===========================================================
"""
import requests
import pandas as pd
import matplotlib.pyplot as plt

# ===========================================================
# PARTE 1 – INTRODUÇÃO
# ===========================================================
"""
O que é uma API?
API (Application Programming Interface) permite que um sistema
se comunique com outro.
Quando usamos requests.get(), estamos enviando uma requisição
HTTP para um servidor que retorna dados, geralmente em JSON.
Fluxo básico:
1. Definir URL
2. Enviar requisição
3. Verificar status_code
4. Converter para JSON
5. Transformar em DataFrame (quando necessário)
"""
# ===========================================================
# PARTE 2 – VIACEP (Consulta de CEP)
# ===========================================================
"""
Site: https://viacep.com.br/
Exemplo de consulta:
https://viacep.com.br/ws/01001000/json/

Exercícios:
1. Consulte um CEP da sua escolha.
2. Verifique o status da requisição.
3. Converta a resposta para JSON.
4. Transforme em DataFrame.
5. Mostre as principais informações.
"""
# RESOLVA AQUI:

# 1. Definindo o CEP e a URL
cep = "01310100"  # Avenida Paulista - SP
url_cep = f"https://viacep.com.br/ws/{cep}/json/"

# 2. Enviando a requisição e verificando o status
resposta_cep = requests.get(url_cep)
print("=== PARTE 2 – VIACEP ===")
print("Status da requisição:", resposta_cep.status_code)

# 3. Convertendo para JSON
dados_cep = resposta_cep.json()

# 4. Transformando em DataFrame
df_cep = pd.DataFrame([dados_cep])

# 5. Mostrando as principais informações
print(df_cep[["cep", "logradouro", "bairro", "localidade", "uf"]])
print()


# ===========================================================
# PARTE 3 – BRASILAPI
# ===========================================================
"""
Documentação:
https://brasilapi.com.br/docs
Exercícios:
1. Consulte a lista de bancos.
2. Transforme o resultado em DataFrame.
3. Conte quantos bancos existem.
4. Filtre bancos cujo nome contenha "Brasil".
Explique:
O que você percebe sobre a estrutura do JSON retornado?
"""
# RESOLVA AQUI:

# 1. Consultando a lista de bancos
url_bancos = "https://brasilapi.com.br/api/banks/v1"
resposta_bancos = requests.get(url_bancos)

# 2. Transformando em DataFrame
df_bancos = pd.DataFrame(resposta_bancos.json())

# 3. Contando quantos bancos existem
print("=== PARTE 3 – BRASILAPI ===")
print("Total de bancos:", len(df_bancos))

# 4. Filtrando bancos com "Brasil" no nome
df_brasil = df_bancos[df_bancos["name"].str.contains("BRASIL", case=False, na=False)]
print("Bancos com 'Brasil' no nome:\n", df_brasil[["code", "name"]])
print()

# Estrutura do JSON: retorna uma lista de objetos com campos code, name, fullName


# ===========================================================
# PARTE 4 – SERVIÇO DE DADOS IBGE
# ===========================================================
"""
Documentação:
https://servicodados.ibge.gov.br/api/docs/
Exercícios:
1. Consulte os estados brasileiros.
2. Transforme em DataFrame.
3. Mostre apenas:
   - nome
   - sigla
   - região
4. Pesquise como consultar dados de população.
Desafio:
Consultar a população total de um estado específico.
"""
# RESOLVA AQUI:

# 1. Consultando os estados brasileiros
url_estados = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
resposta_estados = requests.get(url_estados)

# 2. Transformando em DataFrame
df_estados = pd.DataFrame(resposta_estados.json())

# 3. Mostrando nome, sigla e região
df_estados["regiao"] = df_estados["regiao"].apply(lambda x: x["nome"])
print("=== PARTE 4 – IBGE ===")
print(df_estados[["nome", "sigla", "regiao"]].sort_values("nome"))
print()

# 4. Desafio: população do estado de São Paulo (código 35)
url_pop = "https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2022/variaveis/9324?localidades=N3[35]"
resposta_pop = requests.get(url_pop)
dados_pop = resposta_pop.json()
populacao = dados_pop[0]["resultados"][0]["series"][0]["serie"]["2022"]
print("População de São Paulo (2022):", int(populacao))
print()


# ===========================================================
# PARTE 5 – IPEA DATA
# ===========================================================
"""
Documentação:
https://www.ipeadata.gov.br/api/
Exercícios:
1. Consulte os metadados de uma série.
2. Identifique:
   - nome da série
   - descrição
   - unidade
3. Consulte os valores históricos da série.
4. Transforme em DataFrame.
"""
# RESOLVA AQUI:

# Série: BM12_TJOVER12 (Taxa Selic Over)
# 1. Consultando metadados da série
url_meta = "http://www.ipeadata.gov.br/api/odata4/Metadados('BM12_TJOVER12')"
resposta_meta = requests.get(url_meta)
meta = resposta_meta.json()

# 2. Identificando informações da série
print("=== PARTE 5 – IPEA DATA ===")
print("Nome:", meta.get("SERNOME"))
print("Unidade:", meta.get("UNINOME"))
print("Fonte:", meta.get("FNTNOME"))
print()

# 3. Consultando os valores históricos
url_valores = "http://www.ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='BM12_TJOVER12')?$top=10&$orderby=VALDATA desc"
resposta_valores = requests.get(url_valores)

# 4. Transformando em DataFrame
df_selic = pd.DataFrame(resposta_valores.json()["value"])
df_selic = df_selic[["VALDATA", "VALVALOR"]].rename(columns={"VALDATA": "data", "VALVALOR": "taxa_selic"})
print("Últimos valores da Taxa Selic:\n", df_selic)
print()


# ===========================================================
# PARTE 6 – BANCO CENTRAL DO BRASIL (BCB)
# ===========================================================
"""
Dados Abertos BCB:
https://dadosabertos.bcb.gov.br/
Exemplo: Consulta PTAX
Parâmetros:
{
 "formato": "json",
 "dataInicial": "01/01/2024",
 "dataFinal": "31/12/2024"
}
Exercícios:
1. Consulte a cotação do dólar em 2024.
2. Transforme em DataFrame.
3. Calcule:
   - média
   - valor máximo
   - valor mínimo
4. Plote gráfico de linha.
"""
# RESOLVA AQUI:

# 1. Consultando a cotação do dólar em 2024 (PTAX)
url_ptax = (
    "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
    "CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinal=@dataFinal)"
    "?@dataInicial='01-01-2024'&@dataFinal='12-31-2024'&$format=json"
)
resposta_ptax = requests.get(url_ptax)

# 2. Transformando em DataFrame
df_dolar = pd.DataFrame(resposta_ptax.json()["value"])
df_dolar["dataHoraCotacao"] = pd.to_datetime(df_dolar["dataHoraCotacao"])
df_dolar = df_dolar.rename(columns={"cotacaoCompra": "compra", "cotacaoVenda": "venda"})

# 3. Calculando estatísticas
print("=== PARTE 6 – BANCO CENTRAL ===")
print(f"Média do dólar (compra): R$ {df_dolar['compra'].mean():.2f}")
print(f"Maior cotação (compra): R$ {df_dolar['compra'].max():.2f}")
print(f"Menor cotação (compra): R$ {df_dolar['compra'].min():.2f}")
print()

# 4. Gráfico de linha
df_dolar.plot(x="dataHoraCotacao", y="compra", kind="line", title="Cotação do Dólar em 2024")
plt.xlabel("Data")
plt.ylabel("R$")
plt.tight_layout()
plt.show()


# ===========================================================
# PARTE 7 – FOOTBALL-DATA.ORG
# ===========================================================
"""
Documentação:
https://www.football-data.org/documentation/quickstart
Observação:
Essa API exige API-KEY.
Exercícios:
1. Consulte as áreas (countries).
2. Filtre o Brasil (CountryCode = "BRA").
3. Consulte competições do Brasil.
4. Consulte os times da temporada 2025.
Explique:
O que são parâmetros de consulta?
"""
# RESOLVA AQUI:

# Token gratuito obtido em: https://www.football-data.org/client/register
TOKEN_FOOTBALL = "SUA_API_KEY_AQUI"
headers_football = {"X-Auth-Token": TOKEN_FOOTBALL}

# 1. Consultando áreas (países)
url_areas = "https://api.football-data.org/v4/areas"
resposta_areas = requests.get(url_areas, headers=headers_football)
df_areas = pd.DataFrame(resposta_areas.json()["areas"])

# 2. Filtrando o Brasil
brasil_area = df_areas[df_areas["countryCode"] == "BRA"]
print("=== PARTE 7 – FOOTBALL-DATA ===")
print("Área do Brasil:\n", brasil_area[["id", "name", "countryCode"]])

# 3. Competições do Brasil
url_comp = "https://api.football-data.org/v4/competitions/?areas=2032"
resposta_comp = requests.get(url_comp, headers=headers_football)
df_comp = pd.DataFrame(resposta_comp.json().get("competitions", []))
print("Competições do Brasil:\n", df_comp[["name", "code"]].head() if not df_comp.empty else "Nenhuma encontrada")

# 4. Times da Série A 2024 (BSA = Brasileirão)
url_times = "https://api.football-data.org/v4/competitions/BSA/teams?season=2024"
resposta_times = requests.get(url_times, headers=headers_football)
df_times = pd.DataFrame(resposta_times.json().get("teams", []))
print("Times do Brasileirão:\n", df_times[["name", "founded"]].head(10) if not df_times.empty else "Sem dados")
print()

# Parâmetros de consulta: são informações extras passadas na URL (após "?")
# que filtram ou configuram a resposta da API. Ex: ?areas=2032 filtra por área.


# ===========================================================
# PARTE 8 – RAPIDAPI (EXEMPLOS)
# ===========================================================
"""
Exemplos:
Tripadvisor – SearchLocation
querystring = {"query":"brasilia"}
NBA – Estatísticas de jogadores
querystring = {"game":"8133"}
Exercícios:
1. Escolha uma API do RapidAPI.
2. Faça uma consulta.
3. Transforme a resposta em DataFrame.
4. Descreva a estrutura do JSON retornado.
Desafio:
Identifique níveis aninhados no JSON.
"""
# RESOLVA AQUI:

# Usando a API da NBA (API-NBA no RapidAPI)
RAPIDAPI_KEY = "SUA_API_KEY_AQUI"

url_nba = "https://api-nba-v1.p.rapidapi.com/games"
headers_nba = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}
querystring = {"season": "2023"}

resposta_nba = requests.get(url_nba, headers=headers_nba, params=querystring)

print("=== PARTE 8 – RAPIDAPI ===")
if resposta_nba.status_code == 200:
    jogos = resposta_nba.json().get("response", [])
    df_nba = pd.DataFrame(jogos)
    print("Total de jogos:", len(df_nba))
    print(df_nba.head())
else:
    print("Erro na requisição. Verifique sua API Key do RapidAPI.")

# Estrutura do JSON: possui campo "response" com lista de jogos,
# cada jogo tem campos aninhados como "teams" (home/visitors) e "scores"
print()


# ===========================================================
# PARTE 9 – EXPLORAÇÃO LIVRE
# ===========================================================
"""
Pesquise APIs públicas em:
https://github.com/public-apis/public-apis
https://apilayer.com/marketplace
https://app.balldontlie.io/
Exercícios:
1. Escolha uma API pública.
2. Consulte dados.
3. Transforme em DataFrame.
4. Faça uma pequena análise exploratória.
"""
# RESOLVA AQUI:

# API escolhida: PokeAPI (https://pokeapi.co/) - sem necessidade de token
# Consultando os 20 primeiros pokémons

# 1. Consultando dados
url_pokemon = "https://pokeapi.co/api/v2/pokemon?limit=20"
resposta_pokemon = requests.get(url_pokemon)

# 2 e 3. Transformando em DataFrame
df_pokemon = pd.DataFrame(resposta_pokemon.json()["results"])
df_pokemon["id"] = df_pokemon["url"].apply(lambda x: int(x.split("/")[-2]))

print("=== PARTE 9 – EXPLORAÇÃO LIVRE (PokeAPI) ===")
print("Total de pokémons consultados:", len(df_pokemon))
print(df_pokemon[["id", "name"]])

# 4. Análise exploratória: buscando detalhes do primeiro pokémon
url_pika = "https://pokeapi.co/api/v2/pokemon/pikachu"
pika = requests.get(url_pika).json()
print(f"\nDetalhes do Pikachu:")
print(f"  Peso: {pika['weight']} | Altura: {pika['height']}")
print(f"  Tipos: {[t['type']['name'] for t in pika['types']]}")
print(f"  Habilidades: {[h['ability']['name'] for h in pika['abilities']]}")


# ===========================================================
# Revisão FINAL
# ===========================================================
"""
Responda:

1. O que é uma API?
   É uma interface que permite comunicação entre sistemas. Ela define
   como um programa pode solicitar dados ou serviços de outro.

2. O que é um endpoint?
   É a URL específica de uma API que retorna um tipo de dado.
   Ex: /api/v1/banks retorna a lista de bancos.

3. O que são parâmetros?
   São informações extras passadas na URL ou no corpo da requisição
   para filtrar ou configurar a resposta. Ex: ?season=2024

4. O que é JSON?
   JavaScript Object Notation — formato padrão para troca de dados
   entre sistemas. Estrutura de chave:valor, como um dicionário Python.

5. O que é Headers?
   Informações enviadas junto à requisição HTTP que configuram a
   comunicação. Ex: tipo de conteúdo, token de autenticação.

6. O que é Token?
   É uma chave de autenticação gerada pela API para identificar
   quem está fazendo a requisição e controlar o acesso.
"""
