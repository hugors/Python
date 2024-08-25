import pandas as pd

# Defina o caminho para o arquivo CSV
arquivo_csv = 'dengue.csv'

# Carregue o arquivo CSV em um DataFrame
df = pd.read_csv(arquivo_csv)

# Exiba as primeiras linhas do DataFrame para verificar
print(df.head())
