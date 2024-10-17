import pandas as pd
import plotly.express as px

arquivo = pd.read_excel('formula1.xlsx', engine='openpyxl')

pilotos = arquivo['PILOTO']
pontos = arquivo['PONTOS']

grafico = px.bar(x=pontos, y=pilotos, width=1000, height=700, 
                 title="Mundial de formula 1", orientation='h')

grafico.show()