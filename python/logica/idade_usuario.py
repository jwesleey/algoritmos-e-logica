"""
Com base na data de nascimento informada pelo usuario em dia, mês e ano.
Solicitar a data atual em dia, mês e ano e calcular sua idade completa.
"""

d, m, a = int(input("Dia de nascimento: ")), int(input("Mês de nascimento: ")), int(input("Ano de nascimento: "))
da, ma, aa = int(input("Dia atual: ")), int(input("Mês atual: ")), int(input("Ano atual: "))

# Se o dia de hoje é menor que o do nascimento...
if da < d:
    da += 30   # Pega 30 dias emprestados
    ma -= 1    # "Paga" diminuindo 1 mês do atual

total_dias = da - d

# Se o mês de hoje (já ajustado) é menor que o do nascimento...
if ma < m:
    ma += 12   # Pega 12 meses emprestados
    aa -= 1    # "Paga" diminuindo 1 ano do atual

total_meses = ma - m

total_anos = aa - a

print(f"Idade exata: {total_anos} anos, {total_meses} meses e {total_dias} dias.")
