import matplotlib.pyplot as plt
def correlations_f(dataCsv, COL_SALARIO, THRESHOLD):
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