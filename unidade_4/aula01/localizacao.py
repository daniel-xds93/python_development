
import json
from geopy.geocoders import Nominatim

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arq_json:
        return json.load(arq_json)
    
def gerar_JSON(dic, arquivo):
    with open(arquivo, 'w') as arq_json:
        json.dump(dic, arq_json)

geolocaliza = Nominatim(user_agent = "Bora-Ir")

dicionario = ler_arquivo("endereco.json")

lista = dicionario["endereco"]

location = geolocaliza.geocode(lista)

saida = {
    "coordenadas": (location.latitude, location.longitude)
}

gerar_JSON(saida, "arquivo_saida.json")