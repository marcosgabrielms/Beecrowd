def main():

    x = int(input())
    y = int(input())

    if x > y:
        x, y = y, x

    soma_total = 0

    for numero in range(x, y + 1):
        if numero % 13 != 0:
            soma_total += numero

    print(soma_total)

main()