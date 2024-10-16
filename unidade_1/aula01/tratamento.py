try:
    num1 = int(input("Digite o 1º número: "))
    num2 = float(input("Digite o 2º número: "))

    resultado = num1 + num2

    print(f"o resultado é = {resultado}")

except ValueError:
    print("Valor digitado não é um número!")
