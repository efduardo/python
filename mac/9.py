#Este é um programa que recebe um número inteiro não negativo e verifica se ele é par ou ímpar. Se for par imprime 1, caso contrário 0.

entrada = int(input("Digite um número inteiro: "))

condicaopar = (entrada % 2)

while entrada >= 0:
  if condicaopar == 0:
    print(1)
  else:
    print(0)
  break
