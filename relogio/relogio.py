import os
os.system("cls")

"""
----O PROGRAMA DEVERÁ:
-ler horario, minutos e segundos, todos inteiros, que constituem a hora inicial do jogo.
-ler o tempo acrescido em segundos
- verificar se o tempo é MENOR que 60 segundos
    se sim: 
        S = S + T, com isso, verificar se agora S é MAIOR que 60
            se sim:
                M = M+1
                S = S-60
                e EXIBE.
            se não:
                EXIBE.
    se não:
        verificar se o tempo em segundos é maior que 3600(equivalente a 60 minuntos)
            se sim: M = M + (T/3600), com isso, verificar se M é maior que 60.
                se sim: 
                    H = H + 1
                    M = M - 60
                    e EXIBE.
                se não:
                    EXIBE
            se não:
                H = H + (T/3600), com isso, verificar se H > 24.
                    se sim:
                        H = H-24
                        EXIBE.
                    se não:
                        EXIBE.
"""

H = int(input())
M = int(input())
S = int(input())
T = int(input())

if T < 60:
    S = S + T
    if S >= 60:
        M = M + 1
        S = S - 60
        if M >= 60:
            H = H + 1
            M = M - 60
            print(H)
            print(M)
            print(S)
            if H >= 24:
                H = H - 24
                print(H)
                print(M)
                print(S)
        else:
            print(H)
            print(M)
            print(S)
    else:
        print(H)
        print(M)
        print(S)
elif T < 3600:
    M = M + (T//60)
    S = T % 60
    if M >= 60:
        H = H + 1
        M = M - 60
        if H > 24:
            H = H - 24
            print(H)
            print(M)
            print(S)
        else:
            print(H)
            print(M)
            print(S)
    else:
        print(H)
        print(M)
        print(S)
else:
    H = H + (T//3600)
    M = (T % 3600) // 60
    S = T % 60
    if H >= 24:
        H = H - 24
        print(H)
        print(M)
        print(S)
    else:
        print(H)
        print(M)
        print(S)