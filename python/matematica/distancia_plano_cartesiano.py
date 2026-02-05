print("""
Distância entre dois pontos no Plano Cartesiano
Informe as coordenadas entre os pontos A e B:
A = (x¹, y¹)
B = (x², y²)""")

x1 = float(input("A x¹: "))
y1 = float(input("A y¹: "))
x2 = float(input("B x²: "))
y2 = float(input("B y²: "))

distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

print(f"A distância entre os dois pontos é: {distancia:.2f}")