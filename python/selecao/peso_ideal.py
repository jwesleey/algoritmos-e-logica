"""
Problema: Tendo como dados de entrada a altura e sexo de uma pessoa, apresentar ao usuário o peso ideal
com base nas seguintes fórmulas:
Homens: (72,7 * altura) - 58;
Mulheres: (62,1 * altura) - 44,7
"""

altura = float(input("Digite a altura no formato X.XX: "))
sexo = str(input("Informe o sexo H/M: "))

sexo = sexo.lower()

if sexo not in ("h", "m"):
    print("Informe o sexo novamente.")
else:
    if sexo == "h":
        peso_ideal = 72.7 * altura - 58
    else:
        peso_ideal = 62.1 * altura - 44.7

    print(f"O peso ideal é de {peso_ideal:.2f}KG.")