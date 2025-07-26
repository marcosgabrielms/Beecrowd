def main():
    valor = float(input())
    total_centavos = int(valor * 100 + 0.5)

    print("NOTAS:")
    for nota in [10000, 5000, 2000, 1000, 500, 200]:
        qtd = total_centavos // nota
        print(f"{qtd} nota(s) de R$ {nota / 100:.2f}")
        total_centavos %= nota

    print("MOEDAS:")
    for moeda in [100, 50, 25, 10, 5, 1]:
        qtd = total_centavos // moeda
        print(f"{qtd} moeda(s) de R$ {moeda / 100:.2f}")
        total_centavos %= moeda

if __name__ == '__main__':
    main()
