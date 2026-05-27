dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
quociente = 0

while dividendo >= divisor:
    dividendo = dividendo - divisor
    quociente += 1

print(quociente)