#O João sempre leva para sua escola as maçãs que sobram do depósito do pai, distribuindo-as entre os colegas que encontra no início das aulas. Como o João ainda não aprendeu divisão, ele precisa de um programa para receber como resposta quantas maçãs deve distribuir para cada colega. Ele não pode usar uma faca, deverá fazer uma distribuição de "maças inteiras" e o que sobrar deverá deixar na secretaria da escola.

#Este programa dirá a quantia de maçãs a ser entregue a cada aluno.

entrada1 = int(input("Digite o número total de maçãs: "))
entrada2 = int(input("Digite o número de alunos: "))
inteirodadivisao = (entrada1 // entrada2)

while entrada1 >= 0 and entrada2 > 0:
  print("O número de maçãs a serem entregues a cada aluno é", inteirodadivisao)
  break
