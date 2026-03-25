"""
Escrever um algoritmo que gere a serie de Fibonacci até o vigésimo termo.
"""

a = 0
b = 1

for i in range(20):
    print(a)
    fibonacci = a + b
    a = b
    b = fibonacci
