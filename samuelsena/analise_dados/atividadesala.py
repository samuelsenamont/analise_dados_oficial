# 1 - como identificar uma lista em python?
# Visualmente, uma lista é definida pelo uso de colchetes [] e seus elementos são separados por vírgulas.

# 2 - como pegar o 1° elemento de uma lista em python?
# O Python começa a contar a partir do zero. Logo, o primeiro elemento está no índice [0].

# 3 - como identificar um dicionário em python?
# Dicionários são definidos por chaves {}

# 4 - como pegar um elemento em dicionário?
# usando o método .get()

# 5 - como identfificar uma lusta em dicionário?
# Se você quer verificar se o valor de uma chave específica é uma lista, use type()

# 6 - como teansformar um alista de dicionário em um DataFrame?
# lista_dicionarios = [{"nome": "Ana", "idade": 25}, {"nome": "Carlos", "idade": 32}]
df = pd.DataFrame(lista_dicionarios)

# 7 - como consumir um arquivo csv no DataFrame?
df = pd.read_csv("meu_arquivo.csv")

# 8 - como consumir um arquivo excel no DataFrame?
df = pd.read_excel("minha_planilha.xlsx")

# 9 - como filtrar uma coluna de valores?
df_filtrado = df[df["idade"] > 25]

# 10 - como filtrar uma coluna de string?
df_contem = df[df["cidade"].str.contains("Paulo")]

# 11 -Como fazer dois filtros no DataFrame?
# & para "E" (ambas as condições precisam ser verdadeiras) e | para "OU" (pelo menos uma das condições precisa ser verdadeira).