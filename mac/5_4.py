#Este algoritmo lê três números naturais como entradas e verifica se esses números são pitagóricos. Três números são pitagóricos se o quadrado do maior deles (hipotenusa) é igual à soma do quadrado dos outros dois. Como saída, imprime: se pitagóricos, o valor 1 e o valor da hipotenusa ao quadrado; se não pitagórico, apenas o valor 0.

#Os números são denominados pitagóricos por corresponderem a comprimentos de lados de um triângulo retângulo, ou seja: h² = a² + b².

ladoa = int(input("Digite o valor do primeiro lado: "))
ladob = int(input("Digite o valor do segundo lado: "))
ladoc = int(input("Digite o valor do terceiro lado: "))

while ladoa > 0 and ladob > 0 and ladoc > 0:
    if  ladoa**2 == ladob**2 + ladoc**2:
        print(1, ladoa**2)
    elif ladob**2 == ladoa**2 + ladoc**2:
        print(1, ladob**2)
    elif ladoc**2 == ladoa**2 + ladob**2:
        print(1, ladoc**2)
    else:
        print(0)
    break
