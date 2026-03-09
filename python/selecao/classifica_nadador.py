"""
Dada a idade de um nadador, classifique-o em uma das categorias.
"""

idade = int(input("Digite a idade: "))
print(f"Idade: {idade}")
if idade < 5:
    print("Sem categoria para a idade.")
else:
    if 5 <= idade <= 10:
        if idade <= 7:
            print("Infantil A.")
        else:
            print("Infantil B.")
    elif 11 <= idade <= 17:
        if idade <= 13:
            print("Juvenil A.")
        else:
            print("Juvenil B.")
    else:
        print("Adulto.")