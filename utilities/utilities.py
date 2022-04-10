#Esta é uma calculadora para movimentos uniformemente variados (MUV).

import math
print("O que você precisa encontrar?")
print("")
print("1) Velocidade final [m/s]")
print("2) Velocidade inicial [m/s]")
print("3) Posição final [m]")
print("4) Posição inicial [m]")
print("5) Aceleração [m/s²]")
print("6) Tempo [s]")
print("")
faltante = int(input("Digite o número do que você deseja encontrar: "))
if faltante == 1: #v
    print("")
    tem = print("O que você tem?")
    print("")
    print("1) Velocidade inicial, aceleração e tempo")
    print("2) Velocidade inicial, aceleração e deslocamento")
    print("")
    resptem = int(input("Digite o número do que você tem: "))
    if resptem == 1:
        print("")
        v0 = float(input("Digite a velocidade inicial(em m/s): "))
        a = float(input("Digite a aceleração(em m/s²): "))
        t = float(input("Digite o tempo(em s): "))
        v = v0 + a*t
        print("")
        print("A velocidade final é", v, "[m/s]")   
    elif resptem == 2:
        print("")
        v0 = float(input("Digite a velocidade inicial(em m/s): "))
        a = float(input("Digite a aceleração(em m/s²): "))
        ds = float(input("Digite o deslocamento(em m): "))
        v2 = (v0**2 + 2*a*ds)
        v = math.sqrt(v2)
        print("")
        print("A velocidade final é", v, "[m/s]")
    elif resptem != 1 or resptem != 2:
        print("")
        print("Algo deu errado!")
elif faltante == 2: #v0
    print(" ")
    tem = print("O que você tem?")
    print("")
    print("1) Velocidade final, aceleração e tempo")
    print("2) Velocidade final, aceleração e deslocamento")
    print("3) Tempo, aceleração e deslocamento")
    print("")
    resptem = int(input("Digite o número do que você tem: "))
    if resptem == 1:
        print("")
        v = float(input("Digite a velocidade final(em m/s): "))
        a = float(input("Digite a aceleração(em m/s²): "))
        t = float(input("Digite o tempo(em s): "))
        v0 = v - a*t
        print("")
        print("A velocidade inicial é", v0, "[m/s]")   
    elif resptem == 2:
        print("")
        v0 = float(input("Digite a velocidade inicial(em m/s): "))
        a = float(input("Digite a aceleração(em m/s²): "))
        ds = float(input("Digite o deslocamento(em m): "))
        v02 = (v0**2 + 2*a*ds)
        v0 = math.sqrt(v02)
        print("")
        print("A velocidade inicial é", v0, "[m/s]")
    elif resptem == 3:
        print("")
        t = float(input("Digite o tempo(em s): "))
        a = float(input("Digite a aceleração(em m/s²): "))
        ds = float(input("Digite o deslocamento(em m): "))
        v0 = (ds - (a*t**2)/2)/t
        print("")
        print("A velocidade inicial é", v0, "[m/s]")
    elif resptem != 1 or resptem != 2 or resptem != 3:
        print("")
        print("Algo deu errado!")
elif faltante == 3: #s
    print(" ")
    tem = print("O que você tem?")
    print("")
    print("1) Posição inicial, velocidade inicial, tempo e aceleração")
    print("2) Velocidade final, velocidade inicial, aceleração e posição inicial")
    print("")
    resptem = int(input("Digite o número do que você tem: "))
    if resptem == 1:
        print("")
        s0 = float(input("Digite a posição inicial(em m): "))
        v0 = float(input("Digite a velocidade inicial (em m/s): "))
        t = float(input("Digite o tempo(em s): "))
        a = float(input("Digite a aceleração(em m/s²): "))
        s = s0 + v0*t + (a*(t**2)/2)
        print("")
        print("A posição final é", s, "[m]")
    elif resptem == 2:
        print("")
        v = float(input("Digite a velocidade final(em m/s): "))
        v0 = float(input("Digite a velocidade inicial(em m/s): "))
        a = float(input("Digite a aceleração(em m/s²): "))
        s0 = float(input("Digite a posição inicial(em m): "))
        s = (v**2 - v0**2 + 2*a*s0)/2*a
        print("")
        print("A posição final é", s, "[m]")
    elif resptem != 1 or resptem != 2:
        print("")
        print("Algo deu errado!")
elif faltante == 4: #s0
    print("")
    tem = print("O que você tem?")
    print("")
    print("1) Posição final, velocidade inicial, tempo e aceleração")
    print("2) Velocidade final, velocidade inicial, aceleração e posição final")
    print("")
    resptem = int(input("Digite o número do que você tem: "))
    if resptem == 1:
        print("")
        s = float(input("Digite a posição final(em m): "))
        v0 = float(input("Digite a velocidade inicial(em m/s): "))
        t = float(input("Digite o tempo(em s): "))
        a = float(input("Digite a aceleração(em m/s): "))
        s0 = s - v0*t - (a*(t**2)/2)
        print("")
        print("A posição inicial é", s0, "[m]")
    elif resptem == 2:
        print("")
        v = float(input("Digite a velocidade final(em m/s): "))
        v0 = float(input("Digite a velocidade inicial(em m/s): "))
        a = float(input("Digite a aceleração(em m/s²): "))
        s = float(input("Digite a posição final(em m): "))
        s0 = (v**2 - v0**2 - 2*a*s)/2*a
        print("")
        print("A posição inicial é", s0, "[m]")
    elif resptem != 1 or resptem != 2:
        print("")
        print("Algo deu errado!")
elif faltante == 5: #a
    print("")
    tem = print("O que você tem?")
    print("")
    print("1) Deslocamento, velocidade inicial e tempo")
    print("2) Deslocamento, velocidade final e velocidade inicial")
    print("3) Velocidade final, velocidade inicial e tempo")
    print(" ")
    resptem = int(input("Digite o número do que você tem: "))
    if resptem == 1:
        print("")
        ds = float(input("Digite o deslocamento(em m): "))
        v0 = float(input("Digite a velocidade inicial(em m/s): "))
        t = float(input("Digite o tempo(em s): "))
        a = 2*(ds - v0*t)/t**2
        print(" ")
        print("A aceleração é", a, "[m/s²]")
    elif resptem == 2:
        print("")
        ds = float(input("Digite o deslocamento(em m): "))
        v = float(input("Digite a velocidade final(em m/s): "))
        v0 = float(input("Digite a velocidade inicial(em m/s): "))
        a = ds*(v**2 - v0**2)/2
        print("")
        print("A aceleração é", a, "[m/s²]")
    elif resptem == 3:
        print("")
        v = float(input("Digite a velocidade final(em m/s): "))
        v0 = float(input("Digite a velocidade inicial(em m/s): "))
        t = float(input("Digite o tempo(em s): "))
        a = (v - v0)/t
        print("")
        print("A aceleração é", a, "[m/s²]")
    elif resptem != 1 or resptem != 2 or resptem != 3:
        print("")
        print("Algo deu errado!")
elif faltante == 6: #t
    print("")
    tem = print("O que você tem?")
    print("")
    print("1) Deslocamento, velocidade inicial e aceleração")
    print("2) Velocidade final, velocidade inicial e aceleração")
    print("")
    resptem = int(input("Digite o número do que você tem: "))
    if resptem == 1:
        print(" ")
        ds = float(input("Digite o deslocamento(em m): "))
        v0 = float(input("Digite a velocidade inicial(em m/s): "))
        a = float(input("Digite a aceleração(em m/s²): "))
        delta = (v0**2 + 2*a*ds)
        raizdedelta = math.sqrt(delta)
        t = (-v0 + raizdedelta)/a
        if t >= 0:
            print("")
            print("O tempo é", t, "[s]")
        elif t < 0:
            print("")
            print("O resultado é um número negativo. Logo, não convém usá-lo")  
    elif resptem == 2:
        print(" ")
        v = float(input("Digite a velocidade final(em m/s): "))
        v0 = float(input("Digite a velocidade inicial(em m/s): "))
        a = float(input("Digite a aceleração(em m/s²): "))
        t = (v - v0)/a
        if t >= 0:
            print("")
            print("O tempo é", t, "[s]")
        elif t < 0:
            print("")
            print("O resultado é um número negativo. Logo, não convém usá-lo")
    elif resptem != 1 or resptem != 2:
        print("")
        print("Algo deu errado!")
elif faltante != 1 or faltante != 2 or faltante != 3 or faltante != 4 or faltante != 5 or faltante != 6:
        print("")
        print("Algo deu errado!")
