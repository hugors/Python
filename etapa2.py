import pandas as pd

# Defina o caminho para o arquivo CSV
arquivo_csv = 'dengue.csv'

# Carregue o arquivo CSV em um DataFrame, considerando que as colunas são separadas por ponto e vírgula
df = pd.read_csv(arquivo_csv, sep=';')

# Função para substituir 'sim' por 1 e 'não' por 0
def substituir_sim_nao(valor):
    if valor == 'sim':
        return 1
    elif valor == 'nao':
        return 0
    return valor

# Aplique a função a todas as colunas do DataFrame
df = df.applymap(substituir_sim_nao)

# Exiba as primeiras linhas do DataFrame para verificar a substituição
print(df.head())

# Opcional: salve o DataFrame modificado em um novo arquivo CSV
df.to_csv('dengue_modificado.csv', index=False, sep=';')
