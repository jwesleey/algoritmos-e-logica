def equacao_segundo_grau():
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))

    if a == 0:
        print("Não é equação de segundo grau.")
        return

    delta = b**2 - 4 * a * c

    print(f"Equação: {a}x² + {b}x + {c} = 0")
    print(f"Delta = {delta}")

    if delta < 0:
        print("Nunhuma raiz real.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Raiz única: x = {x}")
    else:
        raiz_delta = delta ** 0.5
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")


equacao_segundo_grau()