x = int(input())
z = int(input())

soma = 0
contador = 0

while z <= x:
    z = int(input())
    
while soma <= z:
    soma += x
    contador += 1
    x += 1

print(contador)
