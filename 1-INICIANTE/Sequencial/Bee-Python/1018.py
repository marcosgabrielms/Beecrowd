def main():

    n_inicial = int(input())
    print(n_inicial)

    notas_100 = n_inicial // 100
    valor_restante = n_inicial % 100

    notas_50 = valor_restante // 50
    valor_restante = valor_restante % 50

    notas_20 = valor_restante // 20
    valor_restante = valor_restante % 20

    notas_10 = valor_restante // 10
    valor_restante = valor_restante % 10

    notas_5 = valor_restante // 5
    valor_restante = valor_restante % 5

    notas_2 = valor_restante // 2
    valor_restante = valor_restante % 2

    notas_1 = valor_restante // 1
    valor_restante = valor_restante % 1
    

    print(f"{notas_100} nota(s) de R$ 100,00")
    print(f"{notas_50} nota(s) de R$ 50,00")
    print(f"{notas_20} nota(s) de R$ 20,00")
    print(f"{notas_10} nota(s) de R$ 10,00")
    print(f"{notas_5} nota(s) de R$ 5,00")
    print(f"{notas_2} nota(s) de R$ 2,00")
    print(f"{notas_1} nota(s) de R$ 1,00")

if __name__ == '__main__':
    main()