#Através do Kaggle, procurem outros datasets e apliquem os comandos trabalhados anteriormente.

import pandas as pd

# Carregar dados
df_disco = pd.read_csv('synthetic_covid_impact_on_work.csv')

# Visualizar dados
print(df_disco.head())
print(df_disco.tail())

# Configurar opção para exibir até 3 linhas
pd.set_option('display.max_rows', 3)

# Informações do DataFrame
print(df_disco.info())

# Estatísticas descritivas
print(df_disco.describe())

# Verificar valores ausentes
print(df_disco.isnull().sum())






