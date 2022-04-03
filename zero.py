#Este é um programa para ser rodado em Python

print("ATENÇÃO: O quadrado da soma dos números digitados não pode ser maior que 100"
print("")

entrada1 = int(input("1) Digite um número inteiro: "))
entrada2 = int(input("2) Digite outro número inteiro: "))
a = 1
b = 2
quadradodadiferenca = (entrada1 - entrada2)**2

if quadradodadiferenca <= 100:
  print("")
  print("O quadrado da diferença dos números digitados é", quadradodadiferenca)
elif quadradodadiferenca > 100:
  print("")
  print("TÁ ERRADO AMIGÃO!")
  print("")
  entrada3 = int(input("Quer saber qual foi o erro? (1 para sim e 2 para não): "))
  if entrada3 <= a:
    erro = entrada1 - entrada2
    print("")
    print(erro, "ao quadrado é um número > 100")
  elif entrada3 <= b:
    print("")
    print("OK! Tchau!")
