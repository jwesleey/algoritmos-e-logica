lista = []

for i in range(5):
    numero = int(input("Número: "))
    lista.append(numero)

print(lista)

max_value = lista[0]
for n in lista:
    if n > max_value:
        max_value = n

print(max_value)

