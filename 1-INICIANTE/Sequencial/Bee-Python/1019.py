def main():

    n_inicial = int(input())

    tempo_h = n_inicial // 3600
    tempo_restante = n_inicial % 3600

    tempo_m = tempo_restante // 60
    tempo_restante = tempo_restante % 60

    tempo_s = tempo_restante 

    print(f"{tempo_h}:{tempo_m}:{tempo_s}")

if __name__ == '__main__':
    main()
    