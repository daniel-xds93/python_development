nivel = input("Digite seu nivel: ").upper().strip()

#print("Texto convertido para maiusculo = ", nivel)

#print("A" == nivel)

hrs = int(input("Digite o número de hora(s) trabalhada(s): "))

if nivel == 'A':
    salario = hrs * 35.00
    print(f"Seu salario é R$ {salario}")

elif nivel == 'B':
    salario = hrs * 55.00
    print(f"Seu salário é R$ {salario}")

elif nivel == 'C':
    salario = hrs * 80.00
    print(f"Seu salário é R$ {salario}")

else:
    print("Nível inválido!")