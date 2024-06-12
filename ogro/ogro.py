"""
---O PROGRAMA DEVERÁ:
-Receber um inteiro entre 0 e 5, representando o numero de dedos na mão esquerda.
-Receber um inteiro entre 0 e 5, representando o numero de dedos na mão direita
-Verificar se o número de dedos na mão esquerda é maior que o número de dedos na mão direita.
    se sim:
        Resultado = E + D
    se não:
        Resultado = 2 * (D - E)
- Exibir o resultado.

"""
import os
os.system("cls")

E = int(input())
D = int(input())

if E >= 0 and E <= 5 and D >= 0 and D <= 5:
    if E > D:
        Resultado = E + D
    else:
        Resultado = 2 * (D-E)
    print(Resultado)
else:
    print("O NUMERO DE DEDOS INSERIDOS É INVÁLIDO.")