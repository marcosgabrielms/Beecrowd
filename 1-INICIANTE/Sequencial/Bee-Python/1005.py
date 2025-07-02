def main():

    valor1 = float(input())
    valor2 = float(input())
    peso1 = 3.5
    peso2 = 7.5

    media = (valor1 * peso1 + valor2 * peso2) / (peso1 + peso2)

    print(f"MEDIA = {media:.5f}")
        
if __name__ == '__main__':
    main()