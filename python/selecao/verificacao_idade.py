"""
Programa que leia a data de nascimento de uma pessoa,
calcula sua idade atual e informa se ela pode votar
e se está apta a tirar a Carteira Nacional de Habilitação
"""

from datetime import date

ano = int(input("Digite o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano

print(f"Idade: {idade}")

if idade < 0:
    print("Ano de nascimento inválido.")
elif idade < 16:
    print("Não possui idade mínima para votar nem para obter habilitação.")
elif idade < 18:
    print("Você não pode tirar carteira de habilitação, mas pode votar.")
else:
    print("Parabéns você é um adulto, pode votar e ter sua carteira de habilitação.")