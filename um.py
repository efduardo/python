#Este é um programa para ser rodado em Python

print("João tem n maçãs e deve distribuí-las igualmente entre seus colegas de turma e as que restarem deve entregar na secretaria da escola")
print("")

entrada1 = int(input("1) Digite o número total de maçãs: "))
entrada2 = int(input("2) Digite o número de alunos: "))
inteirodadivisao = (entrada1 // entrada2)
restodadivisao = (entrada1 % entrada2)

while entrada1 >= 0 and entrada2 > 0:
  print("")
  print("O número de maçãs a ser entregue a cada aluno é", inteirodadivisao)
  print("")
  print("Sendo assim, o número de maçãs restantesna secretaria é", restodadivisao)
  break
