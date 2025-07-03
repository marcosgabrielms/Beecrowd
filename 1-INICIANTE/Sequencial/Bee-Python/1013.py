def main():

    a, b, c = map(int, input().split())

    maiorAB = (a + b + abs(a - b)) / 2
    maiorAC = (a + c + abs(a - c)) / 2

    if maiorAB > maiorAC:
        print(f"{maiorAB:.0f} eh o maior")
    else:
        print(f"{maiorAC:.0f} eh o maior")

if __name__ == '__main__':
    main()