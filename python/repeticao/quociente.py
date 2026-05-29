"""
Elaborar um algoritmo que leia um dividendo e um divisor inteiros

O cálculo deve ser realizado utilizando apenas estruturas de
repetição e subtrações sucessivas, sem utilizar os operadores
de divisão (/ e //).

Ao final, exibir o quociente obtido.
"""
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
quociente = 0

while dividendo >= divisor:
    dividendo = dividendo - divisor
    quociente += 1

print(quociente)