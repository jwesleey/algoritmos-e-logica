"""
Descobrir número aleatório.
"""

from random import randint

num = randint(1, 100)
chute = 0
tentativas = 0

while chute != num:
    chute = int(input("Chute? "))
    tentativas = tentativas + 1
    if chute > num:
        print("Chutou alto.")
    else:
        print("Chutou baixo.")

print("Tentativas: ", tentativas)