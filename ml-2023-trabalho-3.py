import pandas as pd

import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder

##print(os.getcwd(), 'asa')
##capturar o caminho
##dataCsv = pd.read_csv('./ml-2023-1-trabalho-3/ds_salaries.csv')
dataCsv = pd.read_csv('ds_salaries.csv')
THRESHOLD = 0.3

salario = "salary_in_usd"
COL_SALARIO = dataCsv[salario]

def transformar_econder(dataCsv):
    encoder = LabelEncoder()

    for coluna in dataCsv.columns:
        if dataCsv[coluna].dtypes == 'object':
            valores_antes = dataCsv[coluna].values
            tipo_antes_encoder =  dataCsv[coluna].dtypes
            dataCsv[coluna] = dataCsv[coluna].astype(str)
            dataCsv[coluna] = encoder.fit_transform(dataCsv[coluna].values)
            valores_depois = dataCsv[coluna].values
          
            print(f'\n Coluna {coluna}: valores antes  {valores_antes} e valores depois {valores_depois} \n tipo antes {tipo_antes_encoder} e tipo depois {dataCsv[coluna].dtypes}')
    return dataCsv
def colunas_faltantes(dataCsv):
    percentual_dfaltantes = dataCsv.isna().sum() / len(dataCsv) * 100
 
    colunas_dfaltantes = percentual_dfaltantes[percentual_dfaltantes > 90].index
    cols_dfaltantes = dataCsv[colunas_dfaltantes]
    print(f'\n Colunas com mais de 90% de dados faltantes: { colunas_dfaltantes }')
    return cols_dfaltantes
def preencher_mediana(dataCsv):
    return dataCsv.fillna(dataCsv.median())
def correlacao_forte(dataCsv):
    result_correlacao = dataCsv.corrwith(COL_SALARIO, numeric_only=True)
    colunas_correlacionadas = result_correlacao[result_correlacao.abs() > THRESHOLD].index
    print(f"Colunas com correlação acima de {THRESHOLD}: {colunas_correlacionadas}")    
    print(f"Colunas com correlação acima de {THRESHOLD}: {colunas_correlacionadas}") 
    result_correlacao.plot(kind='bar', figsize=(10, 6))
   
    plt.xlabel('Variáveis', fontsize=12)
    plt.ylabel('Correlação', fontsize=12)
    plt.title(f'Correlação das colunas com {COL_SALARIO}', fontsize=14)
  
    plt.legend(['Correlação'], loc='best', fontsize=10)
   
    plt.show()
    return colunas_correlacionadas


transformar_econder(dataCsv)
colunas_faltantes(dataCsv)
preencher_mediana(dataCsv)
dataCsv_correlacionado = correlacao_forte(dataCsv)


dataCsv = dataCsv.drop(columns=set(dataCsv.columns) - set(dataCsv_correlacionado))

print(f'dataCsv columns {dataCsv.columns}')


X = dataCsv.drop(columns=["salary_in_usd"])
y = dataCsv["salary_in_usd"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = MLPRegressor(hidden_layer_sizes=(100, 100), activation='relu', random_state=42, max_iter=500)
model.fit(X_train_scaled, y_train)


y_pred = model.predict(X_test_scaled)


mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae:.2f}")


profile_scale = X_test_scaled[:3]  


predicted_salaries = model.predict(profile_scale)


for i, example_profile in enumerate(profile_scale):
    print(f"\nExample Profile {i+1}:")
    for j, coluna in enumerate(X.columns):
        print(f"{coluna}: {example_profile[j]}")
    print(f"Predicted Salary: {predicted_salaries[i]:.2f} USD")


for i, example_profile in enumerate(profile_scale):
    print(f"\nExample Profile {i+1}:")
    for j, coluna in enumerate(X.columns):
        original_value = X_test.iloc[i][coluna]  
        print(f"{coluna}: {original_value}")
    print(f"Predicted Salary: {predicted_salaries[i]:.2f} USD")