import pandas as pd
import matplotlib.pyplot as pl


# Questão 1: Carregar o DataFrame
# LER arquivo titanic.csv em um DataFrame pandas chamado df?
df = pd.read_csv('titanic.csv')
print(df)

# Questão 2: Filtrar passageiros do sexo feminino
# Filtrar o DataFrame para mostrar apenas as Mulheres?
# (Dica: Filtar onde a coluna "Sex" é igual a "female")
df_mulheres = df[df['Sex'] == 'female']
print(f"Total de mulheres: {len(df_mulheres)}")

# Questão 3: Contar sobreviventes
# Quantos passageiros Sobreviveram?
# (Dica: Sobreviventes têm o valor 1 na coluna "Survived")
total_sobreviventes = df[df['Survived'] == 1].shape[0]
print(f"Total de sobreviventes: {total_sobreviventes}")

# Questão 4: Calcular a média da idade
media_idade = df['Age'].mean()
print(f"Média da idade dos passageiros: {media_idade:.2f} anos")
# Quantos Homens Sobreviveram?
homens_sobreviventes = df[(df['Sex'] == 'male') & (df['Survived'] == 1)].shape[0]
print(f"Homens que sobreviveram: {homens_sobreviventes}")

# Questão 5: Calcular Nome "John"
# Calcular quantos passageiros tem o nome "John"?
# (Dica: Usar a coluna "Name")
total_john = df['Name'].str.contains('John', case=False, na=False).sum()
print(f"Passageiros com o nome 'John': {total_john}")