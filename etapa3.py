import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Defina o caminho para o arquivo CSV
arquivo_csv = 'dengue_modificado.csv'

# Carregue o arquivo CSV em um DataFrame
df = pd.read_csv(arquivo_csv, sep=';')

# Exiba os nomes das colunas
print("Colunas do DataFrame:")
print(df.columns)

# Substitua 'nome_da_coluna_target' pelo nome real da coluna alvo no seu DataFrame
nome_da_coluna_target = 'dengue'  # Ajuste este nome conforme necessário

# Separe as variáveis independentes (features) e a variável dependente (target)
X = df.drop(columns=nome_da_coluna_target)
y = df[nome_da_coluna_target]

# Divida o DataFrame em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crie uma instância do classificador KNeighborsClassifier
model = KNeighborsClassifier()

# Treine o modelo com os dados de treinamento
model.fit(X_train, y_train)

# Faça previsões com os dados de teste
y_pred = model.predict(X_test)

# Calcule a matriz de confusão
cm = confusion_matrix(y_test, y_pred)

# Calcule a acurácia
accuracy = accuracy_score(y_test, y_pred)

# Exiba a matriz de confusão e a acurácia
print("Matriz de Confusão:")
print(cm)
print("\nAcurácia do Modelo:")
print(accuracy)
