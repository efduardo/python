#Este é um programa que recebe 3 números inteiros e os imprime em ordem decrescente

entrada1 = int(input("Digite um número inteiro: "))
entrada2 = int(input("Digite outro número inteiro: "))
entrada3 = int(input("Digite mais um número inteiro: "))

if entrada1 >= entrada2 >= entrada3:
  print(entrada1, entrada2, entrada3)
elif entrada1 >= entrada3 >= entrada2:
  print(entrada1, entrada3, entrada2)
elif entrada2 >= entrada1 >= entrada3:
  print(entrada2, entrada1, entrada3)
elif entrada2 >= entrada3 >= entrada1:
  print(entrada1, entrada3, entrada2)
elif entrada3 >= entrada1 >= entrada2:
  print(entrada3, entrada1, entrada2)
else:
  print(entrada3, entrada2, entrada1)
