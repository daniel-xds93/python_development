
import pandas as pd

# criação de um dataframe 
dados = pd.DataFrame(
    {  'Nome': ['Daniel', 'Vilma', 'Isabella', 'Osvaldo'],
       'Idade': [31, 36, 2, 38],
       'Sexo': ['M', 'F', 'F', 'M'] 
    }
)

# a linha abaixo exporta as informações
dados.to_csv('arquivo_exportado_sem_indice.csv', index=False)