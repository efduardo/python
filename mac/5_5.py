#Este é um programa que lê um número natural e computa a maior soma de naturais consecutivos, que seja menor ou igual ao valor digitado.

#Se o usuário digitar um número n, então o programa irá computar a somatória 0 + 1 +... = x, onde x <= n.

n = int(input("Digite um número inteiro: "))

total = 0
i = 0

while total <= n and n > 0:
    i += 1
    total += i
    a = i - 1

sn = (1 + a)*a/2

print("A maior soma de números naturais é", int(sn))
