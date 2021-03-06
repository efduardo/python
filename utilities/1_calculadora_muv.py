#Esta é uma calculadora para movimentos uniformemente variados (MUV).

import math

print("O que você precisa encontrar?\n\n1) Velocidade final [m/s]\n2) Velocidade inicial [m/s]\n3) Posição final [m]\n4) Posição inicial [m]\n5) Aceleração [m/s²]\n6) Tempo [s]")

faltante = int(input("\nDigite o número do que você deseja encontrar: "))

while 1 <= faltante <= 6:
    if faltante == 1:
        tem = print("\nO que você tem?")
        print("\n1) Velocidade inicial, aceleração e tempo\n2) Velocidade inicial, aceleração e deslocamento")
        resptem = int(input("\nDigite o número do que você tem: "))
        while 1 <= resptem <= 2:
            if resptem == 1:
                v0 = float(input("\nDigite a velocidade inicial(em m/s): "))
                a = float(input("Digite a aceleração(em m/s²): "))
                t = float(input("Digite o tempo(em s): "))
                v = v0 + a*t
                print("\nA velocidade final é", v, "[m/s]")   
            else:
                v0 = float(input("\nDigite a velocidade inicial(em m/s): "))
                a = float(input("Digite a aceleração(em m/s²): "))
                ds = float(input("Digite o deslocamento(em m): "))
                v2 = (v0**2 + 2*a*ds)
                while v2 >= 0:
                    v = math.sqrt(v2)
                    print("\nA velocidade final é", v, "[m/s]")
                    break
            break
    elif faltante == 2:
        tem = print("\nO que você tem?")
        print("\n1) Velocidade final, aceleração e tempo\n2) Velocidade final, aceleração e deslocamento\n3) Tempo, aceleração e deslocamento")
        resptem = int(input("\nDigite o número do que você tem: "))
        while 1 <= resptem <= 2:
            if resptem == 1:
                v = float(input("\nDigite a velocidade final(em m/s): "))
                a = float(input("Digite a aceleração(em m/s²): "))
                t = float(input("Digite o tempo(em s): "))
                v0 = v - a*t
                print("\nA velocidade inicial é", v0, "[m/s]")   
            elif resptem == 2:
                v0 = float(input("\nDigite a velocidade inicial(em m/s): "))
                a = float(input("Digite a aceleração(em m/s²): "))
                ds = float(input("Digite o deslocamento(em m): "))
                v02 = (v0**2 + 2*a*ds)
                while v02 >= 0:
                    v0 = math.sqrt(v02)
                    print("\nA velocidade inicial é", v0, "[m/s]")
                    break
            else:
                t = float(input("\nDigite o tempo(em s): "))
                a = float(input("Digite a aceleração(em m/s²): "))
                ds = float(input("Digite o deslocamento(em m): "))
                v0 = (ds - (a*t**2)/2)/t
                print("\nA velocidade inicial é", v0, "[m/s]")
            break
    elif faltante == 3:
        tem = print("\nO que você tem?")
        print("\n1) Posição inicial, velocidade inicial, tempo e aceleração\n2) Velocidade final, velocidade inicial, aceleração e posição inicial")
        resptem = int(input("\nDigite o número do que você tem: "))
        while 1 <= resptem <= 2:
            if resptem == 1:
                s0 = float(input("\nDigite a posição inicial(em m): "))
                v0 = float(input("Digite a velocidade inicial (em m/s): "))
                t = float(input("Digite o tempo(em s): "))
                a = float(input("Digite a aceleração(em m/s²): "))
                s = s0 + v0*t + (a*(t**2)/2)
                print("\nA posição final é", s, "[m]")
            else:
                v = float(input("\nDigite a velocidade final(em m/s): "))
                v0 = float(input("Digite a velocidade inicial(em m/s): "))
                a = float(input("Digite a aceleração(em m/s²): "))
                s0 = float(input("Digite a posição inicial(em m): "))
                s = (v**2 - v0**2 + 2*a*s0)/2*a
                print("\nA posição final é", s, "[m]")
            break
    elif faltante == 4:
        tem = print("\nO que você tem?")
        print("\n1) Posição final, velocidade inicial, tempo e aceleração\n2) Velocidade final, velocidade inicial, aceleração e posição final")
        resptem = int(input("\nDigite o número do que você tem: "))
        while 1 <= resptem <= 2:
            if resptem == 1:
                s = float(input("\nDigite a posição final(em m): "))
                v0 = float(input("Digite a velocidade inicial(em m/s): "))
                t = float(input("Digite o tempo(em s): "))
                a = float(input("Digite a aceleração(em m/s): "))
                s0 = s - v0*t - (a*(t**2)/2)
                print("\nA posição inicial é", s0, "[m]")
            else:
                v = float(input("\nDigite a velocidade final(em m/s): "))
                v0 = float(input("Digite a velocidade inicial(em m/s): "))
                a = float(input("Digite a aceleração(em m/s²): "))
                s = float(input("Digite a posição final(em m): "))
                s0 = (v**2 - v0**2 - 2*a*s)/2*a
                print("\nA posição inicial é", s0, "[m]")
            break
    elif faltante == 5:
        tem = print("\nO que você tem?")
        print("\n1) Deslocamento, velocidade inicial e tempo\n2) Deslocamento, velocidade final e velocidade inicial\n3) Velocidade final, velocidade inicial e tempo")
        resptem = int(input("\nDigite o número do que você tem: "))
        while 1 <= resptem <= 3:
            if resptem == 1:
                ds = float(input("\nDigite o deslocamento(em m): "))
                v0 = float(input("Digite a velocidade inicial(em m/s): "))
                t = float(input("Digite o tempo(em s): "))
                a = 2*(ds - v0*t)/t**2
                print("\nA aceleração é", a, "[m/s²]")
            elif resptem == 2:
                ds = float(input("\nDigite o deslocamento(em m): "))
                v = float(input("Digite a velocidade final(em m/s): "))
                v0 = float(input("Digite a velocidade inicial(em m/s): "))
                a = ds*(v**2 - v0**2)/2
                print("\nA aceleração é", a, "[m/s²]")
            else:
                v = float(input("\nDigite a velocidade final(em m/s): "))
                v0 = float(input("Digite a velocidade inicial(em m/s): "))
                t = float(input("Digite o tempo(em s): "))
                a = (v - v0)/t
                print("\nA aceleração é", a, "[m/s²]")
            break
    else:
        tem = print("\nO que você tem?")
        print("\n1) Deslocamento, velocidade inicial e aceleração\n2) Velocidade final, velocidade inicial e aceleração")
        resptem = int(input("\nDigite o número do que você tem: "))
        while 1 <= resptem <= 2:
            if resptem == 1:
                ds = float(input("\nDigite o deslocamento(em m): "))
                v0 = float(input("Digite a velocidade inicial(em m/s): "))
                a = float(input("Digite a aceleração(em m/s²): "))
                delta = (v0**2 + 2*a*ds)
                while delta >= 0:
                    raizdedelta = math.sqrt(delta)
                    t = (-v0 + raizdedelta)/a
                    if t >= 0:
                        print("\nO tempo é", t, "[s]")
                    else:
                        print("\nO resultado é um número negativo. Logo, não convém usá-lo")
                    break
            else:
                v = float(input("\nDigite a velocidade final(em m/s): "))
                v0 = float(input("Digite a velocidade inicial(em m/s): "))
                a = float(input("Digite a aceleração(em m/s²): "))
                t = (v - v0)/a
                if t >= 0:
                    print("\nO tempo é", t, "[s]")
                else:
                    print("\nO resultado é um número negativo. Logo, não convém usá-lo")
            break
    break
