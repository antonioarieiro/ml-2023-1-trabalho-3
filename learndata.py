import matplotlib.pyplot as plt

def learn_data_csv(predicted_salaries, X_test,  scale, data):
    for i, example_profile in enumerate(data):
        print(f"\ Perfil {i+1}:")
    for j, coluna in enumerate(X.columns):
        print(f"{coluna}: {example_profile[j]}")
    print(f"Salario Prev.: {predicted_salaries[i]:.2f} USD")
    for i, example_profile in enumerate(scale):
        print(f"\nExample Profile {i+1}:")
    for j, coluna in enumerate(X.columns):
        original_value = X_test.iloc[i][coluna]  
        print(f"{coluna}: {original_value}")
    print(f"Salario Prev.: {predicted_salaries[i]:.2f} USD") 