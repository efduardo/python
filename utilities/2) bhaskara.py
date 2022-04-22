#Esta é uma calculadora para funções quadráticas.

import math

print("Tendo uma equação do tipo ax² + bx + c = 0, vamos encontrar os valores de x")

a = float(input("\n1)Digite o valor de a: "))
b = float(input("2)Digite o valor de b: "))
c = float(input("3)Digite o valor de c: "))

delta = (b**2) - (4*a*c)

while delta >= 0:
    raizdedelta = math.sqrt(delta)
    x1 = (- b + raizdedelta)/(2*a)
    x2 = (- b - raizdedelta)/(2*a)
    
    if raizdedelta > 0:
        print("\nOs possíveis valores de x são", x1, "e", x2)
    else:
        print("\nA função possui raiz biquadrada igual a", x1)
    break
