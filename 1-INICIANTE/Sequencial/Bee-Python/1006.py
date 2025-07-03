def main():
    
    a = float(input())
    b = float(input())
    c = float(input())

    peso1 = 2
    peso2 = 3
    peso3 = 5

    media = (a * peso1 + b * peso2 + c * peso3) / (peso1 + peso2 + peso3)

    print(f"MEDIA = {media:.1f}")

if __name__ == '__main__':
    main()