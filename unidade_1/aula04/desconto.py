# VA = 5%
# VT = 6%
# INSS = 11%
# Auxilio creche = 15%

from funcoes_funcionario import *

nome = input("Digite o nome do funcionário: ")
salario_bruto = float(input("Digite o salário bruto: R$ "))

VA = desconto_va(salario_bruto)
VT = desconto_vt(salario_bruto)
INSS = desconto_inss(salario_bruto)

CRECHE = 0.0


filhos = ''

while filhos != 'S' and filhos != 'N':

    filhos = input("Você possui filhos? (S) Sim | (N) Não: ").upper()

    if filhos != 'S' and filhos != 'N':
        print("Você só pode digitar (S) ou (N).")


if filhos == 'S':
    CRECHE = desconto_creche(salario_bruto)


print(f"{nome} seu salário liquido é R$ {salario_liquido(salario_bruto, INSS, VA, VT, CRECHE)}")
print(f"Total de descontos R$ { total_descontos(INSS, VA, VT, CRECHE) }")