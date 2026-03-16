def main():

    x = int(input())
    y = int(input())

    if x > y:
        x, y = y, x

    for numero in range(x + 1, y):
        if numero % 5 == 2 or numero % 5 == 3:
            print(numero)

main()