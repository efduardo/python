#Este é um algoritmo que recebe dois números inteiros como entrada e imprime o maior dentre os dois números.

entrada1 = int(input("Digite um número inteiro: "))
entrada2 = int(input("Digite outro número inteiro: "))

if entrada1 > entrada2:
    print("O maior número é", entrada1)
elif entrada1 < entrada2:
    print("O maior número é", entrada2)
elif entrada1 == entrada2:
    print("Ambos os números são idênticos e iguais a", entrada1)
