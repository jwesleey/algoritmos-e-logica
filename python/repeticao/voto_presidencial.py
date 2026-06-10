"""
Elaborar um algoritmo para simular uma votação para quatro candidatos.

Os votos devem ser informados conforme os códigos:

1 - Candidato 1
2 - Candidato 2
3 - Candidato 3
4 - Candidato 4
5 - Voto nulo
6 - Voto em branco
0 - Encerrar votação

Ao final, o programa deve apresentar:
- O total de votos recebidos.
- A quantidade de votos de cada candidato.
- A quantidade de votos nulos e em branco.
- O percentual de votos de cada categoria em relação ao total de votos.
"""
total_candidato1 = 0
total_candidato2 = 0
total_candidato3 = 0
total_candidato4 = 0
total_nulo = 0
total_branco = 0
total_votos = 0

while True:
    print(f"\nCandidato 1 = 1\nCandidato 2 = 2\nCandidato 3 = 3\nCandidato 4 = 4\nNulo = 5\nBranco = 6\nFinalizar votação = 0")

    opcao = int(input("\nDigite aqui: "))

    if opcao == 0:
        break

    if 0 < opcao < 7:
        total_votos += 1

    match opcao:
        case 1:
            total_candidato1 += 1
        case 2:
            total_candidato2 += 1
        case 3:
            total_candidato3 += 1
        case 4:
            total_candidato4 += 1
        case 5:
            total_nulo += 1
        case 6:
            total_branco += 1
        case _:
            print("Inválido.")

def calcular_percentual(tipo_de_voto, total_de_votos):
    return (tipo_de_voto / total_de_votos) * 100

if total_votos > 0:
    percent_candidato1 = calcular_percentual(total_candidato1, total_votos)
    percent_candidato3 = calcular_percentual(total_candidato3, total_votos)
    percent_candidato2 = calcular_percentual(total_candidato2, total_votos)
    percent_candidato4 = calcular_percentual(total_candidato4, total_votos)
    percent_brancos = calcular_percentual(total_branco, total_votos)
    percent_nulos = calcular_percentual(total_nulo, total_votos)

    print(f"""
    Total de Votos: {total_votos}
    Informações da votação:
    TOTAL / Percentual
    Candidato 1 = {total_candidato1} / {percent_candidato1:.2f}%
    Candidato 2 = {total_candidato2} / {percent_candidato2:.2f}%
    Candidato 3 = {total_candidato3} / {percent_candidato3:.2f}%
    Candidato 4 = {total_candidato4} / {percent_candidato4:.2f}%
    Votos em Branco = {total_branco} / {percent_brancos:.2f}%
    Votos em Nulo = {total_nulo} / {percent_nulos:.2f}%""")
else:
    print("Não houve votação")