from sklearn.preprocessing import LabelEncoder
def encoder(dataCsv):
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