"""
Um comerciante maluco cobra 10% de acréscimo para cada prestação em atraso e depois dá um desconto de 10% sobre o valor.
Faça um algoritmo que solicite o valor da prestação em atraso e a apresente o valor final a pagar, assim como o prejuízo do comerciante na operação.
"""

prestacao = float(input("Informe o valor da prestação: "))
valor_final = prestacao * 1.1 * 0.9
prejuizo = prestacao - valor_final

print(f"Valor final da parcela: R$ {valor_final:.2f} \nPrejuízo do comerciante: R$ {prejuizo:.2f}")