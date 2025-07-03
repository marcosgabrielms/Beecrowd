def main():

    tempo_gasto = int(input())
    velocidade_media = int(input())

    qtd_combustivel_gasto = (tempo_gasto * velocidade_media) / 12

    print(f"{qtd_combustivel_gasto:.3f}")

if __name__ == '__main__':
    main()