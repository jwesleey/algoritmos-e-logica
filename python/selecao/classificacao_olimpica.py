"""
Elaborar um algoritmo que leia o nome de três países e a quantidade de
medalhas de ouro, prata e bronze conquistadas por cada um.

A pontuação deve ser calculada considerando os seguintes pesos:
- ouro = 3 pontos
- prata = 2 pontos
- bronze = 1 ponto

Ao final, o algoritmo deve apresentar a classificação dos países
do maior para o menor total de pontos, utilizando estruturas de seleção.
"""

def resultados():
    pais = str(input("Pais: "))

    ouro = int(input("Ouro: "))
    prata = int(input("Prata: "))
    bronze = int(input("Bronze: "))

    total = ouro * 3 + prata * 2 + bronze

    return pais, total


pais1 = resultados()
pais2 = resultados()
pais3 = resultados()

print("Classificação: ")

if pais1[1] > pais2[1] and pais1[1] > pais3[1]:
    if pais2[1] > pais3[1]:
        print(f"1º {pais1}\n2º {pais2}\n3º {pais3}")
    else:
        print(f"1º {pais1}\n2º {pais3}\n3º {pais2}")
elif pais2[1] > pais1[1] and pais2[1] > pais3[1]:
    if pais3[1] > pais1[1]:
        print(f"1º {pais2}\n2º {pais3}\n3º {pais1}")
    else:
        print(f"1º {pais2}\n2º {pais1}\n3º {pais3}")
else:
    if pais2[1] > pais1[1]:
        print(f"1º {pais3}\n2º {pais2}\n3º {pais1}")
    else:
        print(f"1º {pais3}\n2º {pais1}\n3º {pais2}")