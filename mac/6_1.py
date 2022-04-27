#Este programa solicita que o usuário digite 6 valores inteiros representando duas datas e imprime qual delas é a maior ou se são iguais.

dia1 = int(input("Digite um dia: "))
mes1 = int(input("Digite um mês: "))
ano1 = int(input("Digite um ano: "))
dia2 = int(input("Digite o próximo dia: "))
mes2 = int(input("Digite o próximo mês: "))
ano2 = int(input("Digite o outro ano: "))

while (dia1 > 0) and (mes1 > 0) and (ano1 > 0) and (dia2 > 0) and (mes2 > 0) and (ano2 > 0):
    if (dia1 == dia2) and (mes1 == mes2) and (ano1 == ano2):
        print("São iguais")
    elif (dia1 < dia2) and (mes1 == mes2) and (ano1 == ano2):
        print("Segunda maior")
    elif (dia1 > dia2) and (mes1 == mes2) and (ano1 == ano2):
        print("Primeira maior")
    elif (dia1 == dia2 or dia1 != dia2) and (mes1 < mes2) and (ano1 == ano2):
        print("Segunda maior")
    elif (dia1 == dia2 or dia1 != dia2) and (mes1 > mes2) and (ano1 == ano2):
        print("Primeira maior")
    elif (dia1 == dia2 or dia1 != dia2) and (mes1 == mes2 or mes1 != mes2) and (ano1 < ano2):
        print("Segunda maior")
    else:
        print("Primeira maior")
    break
