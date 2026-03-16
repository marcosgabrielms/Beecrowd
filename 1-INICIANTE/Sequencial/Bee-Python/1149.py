valores = input().split()
a = int(valores[0])
n = 0
posicao = 1

while n <= 0:
    if posicao < len(valores):
        n = int(valores[posicao])
        posicao += 1
    else:
        valores = input().split()
        posicao = 0
    
soma = 0
for i in range(n):
    soma += a + i

print(soma)