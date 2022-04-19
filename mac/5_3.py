#Este programa verifica se 3 números podem ou não representar os ângulos de um triângulo. O algoritmo solicita que o usuário digite 3 números naturais (representando ângulos em graus) e imprime "Sim!" e os 3 números na sequência digitada, se somarem 180; e "Não!" e a soma dos 3 números em caso contrário.

anguloa = int(input("Digite o valor do primeiro ângulo: "))
angulob = int(input("Digite o valor do segundo ângulo: "))
anguloc = int(input("Digite o valor do terceiro ângulo: "))

while anguloa > 0 and angulob > 0 and anguloc > 0:
    
    soma = anguloa + angulob + anguloc

    if soma == 180:
        print("Sim!", anguloa, angulob, anguloc)
    else:
        print("Não!", soma)
    break
