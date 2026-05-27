base = int(input("Base: "))
expoente = int(input("Expoente: "))
resultado = 1

for _ in range(1, expoente + 1):
    resultado *= base

print(resultado)
