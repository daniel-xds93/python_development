import pandas as pd

arquivo = pd.read_csv("base.csv", sep=";")

print(arquivo)

# a linha abaixo retorna aquantidade de registros
print(f"Total de registros: { arquivo["NOME"].count() }")

print(f"Maior valor: { arquivo["VALOR"].max() }")

print(f"Menor valor: { arquivo["VALOR"].min() }")

print(f"Valor total: { round(arquivo['VALOR'].sum(), 2) }")

email_gmail = 0

for email in arquivo['EMAIL']:
    if email.find("gmail") > 0:
        email_gmail += 1

print(f"Total de e-mails gmail: {email_gmail}")
