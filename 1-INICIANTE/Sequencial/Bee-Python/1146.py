n = int(input())

while n != 0:
    try:
        print(*range(1, n + 1))
        n =int(input())
    except EOFError:
        break