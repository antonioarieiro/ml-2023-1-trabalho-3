def not_columns(dataCsv):
    percentual_dfaltantes = dataCsv.isna().sum() / len(dataCsv) * 100
    colunas_dfaltantes = percentual_dfaltantes[percentual_dfaltantes > 90].index
    cols_dfaltantes = dataCsv[colunas_dfaltantes]
    print(f'\n Colunas com mais de 90% de dados faltantes: { colunas_dfaltantes }')
    return cols_dfaltantes
def median(dataCsv):
    return dataCsv.fillna(dataCsv.median())