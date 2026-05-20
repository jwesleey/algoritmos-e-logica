"""
Elaborar um algoritmo capaz de identificar um animal
com base em perguntas e respostas utilizando estruturas
de seleção.

O usuário deverá responder às perguntas com S ou N,
e o programa deverá classificar o animal de acordo
com suas características.

Os animais estão divididos entre:
- mamíferos
- aves
- répteis

Ao final, o algoritmo deve exibir o animal identificado.
"""

def mamifero():
    resposta = str(input("É áquatico? ")).lower()

    if resposta == 's':
        resposta = "Baleia"
    else:
        resposta = str(input("É voador? ")).lower()
        if resposta == 's':
            resposta = "Morcego"
        else:
            resposta = str(input("É bípede? ")).lower()
            if resposta == 's':
                resposta = str(input("É onívoro? ")).lower()
                if resposta == 's':
                    resposta = "Homem"
                else:
                    resposta = "Macaco"
            else:
                resposta = str(input("É carnívoro? ")).lower()
                if resposta == 's':
                    resposta = "Leão"
                else:
                    resposta = "Cavalo"
    return resposta

def aves():
    resposta = str(input("É de rapina? ")).lower()
    if resposta == 's':
        resposta = "Águia"
    else:
        resposta = str(input("É de nadadora? ")).lower()
        if resposta == 's':
            resposta = "Pato"
        else:
            resposta = str(input("É tropical? ")).lower()
            if resposta == 's':
                resposta = "Avestruz"
            else:
                resposta = "Pinguim"

    return resposta

def repteis():
    resposta = str(input("É sem patas? ")).lower()
    if resposta == 's':
        resposta = "Cobra"
    else:
        resposta = str(input("Tem casco? ")).lower()
        if resposta == 's':
            resposta = "Tartaruga"
        else:
            resposta = "Crocodilo"

    return resposta

def iniciar():
    print("Responda com S/N")
    resposta = str(input("É mamífero? ")).lower()
    if resposta == 's':
        return mamifero()
    else:
        resposta = str(input("É réptíl? ")).lower()
        if resposta == 's':
            return repteis()
        else:
            return aves()

print(iniciar())