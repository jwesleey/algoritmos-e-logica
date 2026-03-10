"""
Elaborar um algoritmo que leia o peso e a altura de um adulto e mostrar a sua condição.
Formula IMC: peso / (altura)²
"""

peso = float(input("Digite o peso no formato XX.X: "))
altura = float(input("Digite a altura no formato X.XX: "))

imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25:
    print("Peso normal.")
elif imc <= 30:
    print("Acima do peso.")
else:
    print("Obeso.")