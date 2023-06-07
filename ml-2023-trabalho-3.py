import pandas as pd
from learndata import learn_data_csv
from correlations import correlations_f
from metrics import not_columns, median
from encoder import encoder
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

not_columns(dataCsv)
median(dataCsv)
encoder(dataCsv)
correlations_f(dataCsv, COL_SALARIO, THRESHOLD)
encoder(dataCsv)
not_columns(dataCsv)
median(dataCsv)
dataCsv_correlacionado = correlations_f(dataCsv)


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
print(f"Absoluto medio(err): {mae:.2f}")
scale = X_test_scaled[:3]  
predicted_salaries = model.predict(scale)

learn_data_csv(predicted_salaries, X_test,  scale, scale)

