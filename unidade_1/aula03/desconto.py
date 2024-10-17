# VA = 5%
# VT = 6%
# INSS = 11%
# Auxilio creche = 15%

nome = input("Digite o nome do funcionário: ")
salario_bruto = float(input("Digite o salário bruto: R$ "))

VA = salario_bruto * 0.05
VT = salario_bruto * 0.06
INSS = salario_bruto * 0.11

CRECHE = 0.0

filhos = ''

while filhos != 'S' and filhos != 'N':

    filhos = input("Você possui filhos? (S) Sim | (N) Não: ").upper()

    if filhos != 'S' and filhos != 'N':
        print("Você só pode digitar (S) ou (N).")


if filhos == 'S':
    CRECHE = salario_bruto * 0.15


total_descontos = VA + VT + INSS + CRECHE
salario_liquido = salario_bruto - total_descontos

print(f"{nome} seu salário liquido é R$ {salario_liquido}")
print(f"Total de descontos R$ {total_descontos}")