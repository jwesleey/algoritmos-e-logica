"""
Com base no código, calcular o valor a ser pago por um produto, considerando o preço normal de etiqueta
e a escolha da forma de pagamento escolhida.
"""

preco = float(input("Informe o valor do produto: "))

print("""
1 - À vista em dinheiro ou cheque, recebe 10% de desconto.
2 - À vista no cartão de crédito, recebe 5% de desconto.
3 - Em duas vezes, preço normal de etiqueta sem juros.
4 - Em três vezes, preço normal de etiqueta mais juros de 10%.
""")

modalidade = int(input("Informe a forma de pagamento: "))

if modalidade not in (1, 2, 3, 4):
    print("Código invalido.")
else:
    match modalidade:
        case 1:
            preco_final = preco * 0.9
            print(f"Preço final: {preco_final:.2f}")
        case 2:
            preco_final = preco * 0.95
            print(f"Preço final: {preco_final:.2f}")
        case 3:
            parcela = preco / 2
            print(f"2x de {parcela:.2f}")
        case 4:
            preco_final = preco * 1.10
            parcela = preco_final / 3
            print(f"3x de {parcela:.2f}")