#Este programa solicita que o usuário digite um inteiro positivo n, então implementa um laço (while) que computa a soma dos n primeiros números ímpares até o número digitado, imprimindo a soma final.

n = int(input("Digite um número inteiro positivo: "))

i = 1
p = 0

while (n > 0) and (i <= n):
    i += 2
    p += 2
    a = i - 2

if p == n:
    t = n/2
    an = 1 + (t - 1)*2
    sn = (1 + an) * (t / 2)
    print(int(sn))
else:
    a += 1
    t = (n + 1)/2
    an = 1 + (t - 1)*2
    sn = (1 + an) * (t / 2)
    print(int(sn))
